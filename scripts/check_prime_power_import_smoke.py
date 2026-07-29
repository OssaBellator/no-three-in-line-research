#!/usr/bin/env python3
"""Import-smoke every current prime-power module and seal a reproducible runtime manifest.

Each discovered checker, verifier, runner and test module is imported in a fresh Python interpreter with a
controlled environment and scrubbed import path. The audit catches missing sibling imports, import-time
exceptions and import hangs that syntax compilation cannot detect. Canonical endpoints must contain executable
evidence that the all-n result is fixed at zero; prose alone is insufficient. The emitted manifest records the
exact source inventory and runtime configuration. This is software validation only and permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping

import run_prime_power_current_frontier_regression as regression


class PrimePowerImportSmokeError(RuntimeError):
    """Raised when isolated import, honesty or runtime-manifest validation fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PrimePowerImportSmokeError(message)


SCRIPT_PREFIXES = (
    "check_prime_power_",
    "verify_prime_power_",
    "run_prime_power_",
    "test_prime_power_",
)
IMPORT_TIMEOUT_SECONDS = 30.0
HASH_PROBE_TEXT = "prime-power-current-frontier-runtime-v1"
MANIFEST_SCHEMA_VERSION = 1
PROBE_PREFIX = "IMPORT_AUDIT:"
RUNTIME_PREFIX = "RUNTIME_AUDIT:"

RUNTIME_PROBE = r"""
import json
import sys

payload = {
    "hash_fingerprint": str(hash("prime-power-current-frontier-runtime-v1")),
    "dont_write_bytecode": int(sys.dont_write_bytecode),
    "no_user_site": int(sys.flags.no_user_site),
    "isolated": int(sys.flags.isolated),
}
print("RUNTIME_AUDIT:" + json.dumps(payload, sort_keys=True, separators=(",", ":")))
"""

IMPORT_PROBE = r"""
import importlib.util
import json
import sys
from pathlib import Path

path = Path(sys.argv[1]).resolve()
cwd = Path.cwd().resolve()
clean_entries = []
for entry in sys.path:
    if not entry:
        continue
    resolved = Path(entry).resolve()
    if resolved == cwd or resolved == path.parent:
        continue
    lowered_parts = {part.lower() for part in resolved.parts}
    if "site-packages" in lowered_parts or "dist-packages" in lowered_parts:
        continue
    clean_entries.append(str(resolved))
sys.path[:] = [str(path.parent), *dict.fromkeys(clean_entries)]

module_name = path.stem
spec = importlib.util.spec_from_file_location(module_name, path)
if spec is None or spec.loader is None:
    raise RuntimeError(f"unable to create import spec for {path}")
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

payload = {
    "module": module_name,
    "hash_fingerprint": str(hash("prime-power-current-frontier-runtime-v1")),
    "dont_write_bytecode": int(sys.dont_write_bytecode),
    "no_user_site": int(sys.flags.no_user_site),
    "isolated": int(sys.flags.isolated),
    "third_party_path_entries": sum(
        "site-packages" in {part.lower() for part in Path(entry).parts}
        or "dist-packages" in {part.lower() for part in Path(entry).parts}
        for entry in sys.path
    ),
}
print("IMPORT_AUDIT:" + json.dumps(payload, sort_keys=True, separators=(",", ":")))
"""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def source_digest(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def script_inventory(scripts_dir: Path) -> list[Path]:
    paths = sorted(
        path
        for path in scripts_dir.glob("*.py")
        if path.name.startswith(SCRIPT_PREFIXES)
    )
    require(paths, "no prime-power modules found")
    return paths


def controlled_environment(
    base_environment: Mapping[str, str] | None = None,
) -> dict[str, str]:
    """Remove inherited PYTHON* controls, then install the exact audited startup values."""
    base = dict(os.environ if base_environment is None else base_environment)
    environment = {
        key: value
        for key, value in base.items()
        if not key.upper().startswith("PYTHON")
    }
    environment["PYTHONHASHSEED"] = "0"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return environment


def run_probe(
    code: str,
    *,
    arguments: list[str] | None = None,
    timeout_seconds: float = 10.0,
) -> subprocess.CompletedProcess[str]:
    require(timeout_seconds > 0, "probe timeout must be positive")
    return subprocess.run(
        [sys.executable, "-B", "-s", "-c", code, *(arguments or [])],
        env=controlled_environment(),
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )


def parse_probe_payload(stdout: str, prefix: str, label: str) -> dict[str, Any]:
    payload_lines = [
        line[len(prefix):]
        for line in stdout.splitlines()
        if line.startswith(prefix)
    ]
    require(len(payload_lines) == 1, f"{label}: exact one {prefix!r} payload required")
    try:
        payload = json.loads(payload_lines[0])
    except json.JSONDecodeError as error:
        raise PrimePowerImportSmokeError(f"{label}: malformed JSON payload") from error
    require(isinstance(payload, dict), f"{label}: object payload required")
    return payload


def runtime_configuration_probe() -> dict[str, Any]:
    """Prove that the chosen child-process launcher actually applies its startup controls."""
    payloads: list[dict[str, Any]] = []
    for index in range(2):
        completed = run_probe(RUNTIME_PROBE)
        require(
            completed.returncode == 0,
            (
                f"runtime configuration probe {index + 1} failed\n"
                f"stdout:\n{completed.stdout}\n"
                f"stderr:\n{completed.stderr}"
            ),
        )
        payloads.append(
            parse_probe_payload(completed.stdout, RUNTIME_PREFIX, "runtime configuration")
        )
    require(payloads[0] == payloads[1], "runtime configuration is not reproducible")
    payload = payloads[0]
    require(payload.get("dont_write_bytecode") == 1, "bytecode suppression is not active")
    require(payload.get("no_user_site") == 1, "user-site suppression is not active")
    require(payload.get("isolated") == 0, "unexpected -I isolated mode still active")
    fingerprint = payload.get("hash_fingerprint")
    require(isinstance(fingerprint, str) and fingerprint, "hash fingerprint missing")
    return payload


def is_literal_zero(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and type(node.value) is int and node.value == 0


def mentions_all_n(node: ast.AST) -> bool:
    for child in ast.walk(node):
        if isinstance(child, ast.Name) and child.id in {
            "all_n",
            "all_n_proved_by_checker",
        }:
            return True
        if isinstance(child, ast.Attribute) and "all_n" in child.attr:
            return True
        if isinstance(child, ast.Constant) and child.value in {
            "all_n",
            "all_n_proved_by_checker",
        }:
            return True
    return False


def executable_zero_honesty_evidence(text: str, filename: str) -> list[str]:
    tree = ast.parse(text, filename=filename)
    evidence: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for key, value in zip(node.keys, node.values):
                if (
                    isinstance(key, ast.Constant)
                    and key.value in {"all_n", "all_n_proved_by_checker"}
                    and is_literal_zero(value)
                ):
                    evidence.add("dictionary-literal-zero")
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if value is not None and is_literal_zero(value) and any(
                mentions_all_n(target) for target in targets
            ):
                evidence.add("assignment-literal-zero")
        if isinstance(node, ast.Compare):
            operands = [node.left, *node.comparators]
            if any(is_literal_zero(operand) for operand in operands) and any(
                mentions_all_n(operand) for operand in operands
            ):
                evidence.add("comparison-literal-zero")
    return sorted(evidence)


def validate_endpoint_honesty(filename: str, text: str) -> list[str]:
    require(text.strip(), f"{filename}: empty source")
    compile(text, filename, "exec")
    evidence = executable_zero_honesty_evidence(text, filename)
    require(evidence, f"{filename}: no executable all-n zero condition")
    return evidence


def import_module_isolated(
    path: Path,
    *,
    expected_hash_fingerprint: str,
    timeout_seconds: float = IMPORT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    require(path.is_file(), f"missing import-smoke module: {path}")
    require(timeout_seconds > 0, "import timeout must be positive")
    digest, byte_count = source_digest(path)
    try:
        completed = run_probe(
            IMPORT_PROBE,
            arguments=[str(path)],
            timeout_seconds=timeout_seconds,
        )
    except subprocess.TimeoutExpired as error:
        raise PrimePowerImportSmokeError(
            f"import smoke timed out after {timeout_seconds:g}s: {path.name}"
        ) from error
    require(
        completed.returncode == 0,
        (
            f"import smoke failed: {path.name}\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        ),
    )
    payload = parse_probe_payload(completed.stdout, PROBE_PREFIX, path.name)
    require(payload.get("module") == path.stem, f"import module marker mismatch: {path.name}")
    require(
        payload.get("hash_fingerprint") == expected_hash_fingerprint,
        f"hash seed drift during import: {path.name}",
    )
    require(payload.get("dont_write_bytecode") == 1, f"bytecode enabled: {path.name}")
    require(payload.get("no_user_site") == 1, f"user site enabled: {path.name}")
    require(payload.get("isolated") == 0, f"unexpected -I mode: {path.name}")
    require(
        payload.get("third_party_path_entries") == 0,
        f"third-party import path leaked: {path.name}",
    )
    return {
        "filename": path.name,
        "source_sha256": digest,
        "source_bytes": byte_count,
        "hash_fingerprint": payload["hash_fingerprint"],
        "dont_write_bytecode": payload["dont_write_bytecode"],
        "no_user_site": payload["no_user_site"],
        "third_party_path_entries": payload["third_party_path_entries"],
    }


def seal_manifest(payload: dict[str, Any]) -> dict[str, Any]:
    require("manifest_sha256" not in payload, "manifest payload already sealed")
    sealed = dict(payload)
    sealed["manifest_sha256"] = canonical_digest(payload)
    return sealed


def validate_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest: object required")
    digest = manifest.get("manifest_sha256")
    require(isinstance(digest, str) and len(digest) == 64, "manifest digest required")
    payload = {key: value for key, value in manifest.items() if key != "manifest_sha256"}
    require(canonical_digest(payload) == digest, "manifest digest mismatch")
    require(
        payload.get("claims", {}).get("all_n_proved_by_checker") == 0,
        "manifest honesty value must be zero",
    )
    return payload


def exact_audit(root: Path) -> dict[str, Any]:
    scripts_dir = root / "scripts"
    runtime = runtime_configuration_probe()
    paths = script_inventory(scripts_dir)
    imports = [
        import_module_isolated(
            path,
            expected_hash_fingerprint=runtime["hash_fingerprint"],
        )
        for path in paths
    ]
    endpoint_records: list[dict[str, Any]] = []
    for filename in regression.CANONICAL_ENDPOINTS:
        path = scripts_dir / filename
        text = regression.source_text(path)
        digest, byte_count = source_digest(path)
        endpoint_records.append(
            {
                "filename": filename,
                "source_sha256": digest,
                "source_bytes": byte_count,
                "evidence_kinds": validate_endpoint_honesty(filename, text),
            }
        )
    claims = {
        "isolated_imported_prime_power_modules": len(imports),
        "semantic_honesty_endpoints": len(endpoint_records),
        "per_module_timeout_seconds": int(IMPORT_TIMEOUT_SECONDS),
        "fresh_interpreter_per_module": 1,
        "controlled_hash_seed": 1,
        "bytecode_suppressed": 1,
        "user_site_suppressed": 1,
        "third_party_import_paths_excluded": 1,
        "all_n_proved_by_checker": 0,
    }
    payload = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "python_runtime": {
            "implementation": sys.implementation.name,
            "major_minor": f"{sys.version_info.major}.{sys.version_info.minor}",
            "executable_name": Path(sys.executable).name,
            "hash_fingerprint": runtime["hash_fingerprint"],
            "dont_write_bytecode": runtime["dont_write_bytecode"],
            "no_user_site": runtime["no_user_site"],
        },
        "module_import_records": imports,
        "endpoint_honesty_records": endpoint_records,
        "claims": claims,
    }
    return seal_manifest(payload)


def mutation_self_test() -> dict[str, int]:
    accepted_controls = 0
    rejected_mutations = 0

    hostile = controlled_environment(
        {
            "PATH": "preserved",
            "PYTHONPATH": "/hostile",
            "PYTHONHOME": "/hostile-home",
            "PYTHONHASHSEED": "99",
        }
    )
    require(hostile.get("PATH") == "preserved", "ordinary environment key was lost")
    require("PYTHONPATH" not in hostile and "PYTHONHOME" not in hostile, "hostile Python environment leaked")
    require(hostile["PYTHONHASHSEED"] == "0", "controlled hash seed was not installed")
    require(hostile["PYTHONDONTWRITEBYTECODE"] == "1", "bytecode control was not installed")
    accepted_controls += 1

    runtime = runtime_configuration_probe()
    accepted_controls += 1

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        good = root / "good.py"
        good.write_text("VALUE = 1\n", encoding="utf-8")
        result = import_module_isolated(
            good,
            expected_hash_fingerprint=runtime["hash_fingerprint"],
            timeout_seconds=10.0,
        )
        require(result["source_bytes"] > 0, "good import control failed")
        accepted_controls += 1

        failing = root / "failing.py"
        failing.write_text("raise RuntimeError('boom')\n", encoding="utf-8")
        try:
            import_module_isolated(
                failing,
                expected_hash_fingerprint=runtime["hash_fingerprint"],
                timeout_seconds=10.0,
            )
        except PrimePowerImportSmokeError:
            rejected_mutations += 1
        else:
            raise PrimePowerImportSmokeError("import exception mutation was accepted")

        hanging = root / "hanging.py"
        hanging.write_text("import time\ntime.sleep(1.0)\n", encoding="utf-8")
        try:
            import_module_isolated(
                hanging,
                expected_hash_fingerprint=runtime["hash_fingerprint"],
                timeout_seconds=0.2,
            )
        except PrimePowerImportSmokeError:
            rejected_mutations += 1
        else:
            raise PrimePowerImportSmokeError("import timeout mutation was accepted")

    validate_endpoint_honesty(
        "literal_zero.py",
        'claims = {"all_n_proved_by_checker": 0}\n',
    )
    accepted_controls += 1
    validate_endpoint_honesty(
        "explicit_compare.py",
        'summary = {"all_n": 0}\nassert summary.get("all_n") == 0\n',
    )
    accepted_controls += 1

    for filename, text in (
        ("nonzero.py", 'claims = {"all_n_proved_by_checker": 1}\n'),
        (
            "docstring_only.py",
            '"""all_n_proved_by_checker = 0"""\nVALUE = 1\n',
        ),
        (
            "message_only.py",
            'raise RuntimeError("all_n_proved_by_checker = 0")\n',
        ),
    ):
        try:
            validate_endpoint_honesty(filename, text)
        except PrimePowerImportSmokeError:
            rejected_mutations += 1
        else:
            raise PrimePowerImportSmokeError(f"honesty mutation was accepted: {filename}")

    sample = seal_manifest(
        {
            "schema_version": 1,
            "claims": {"all_n_proved_by_checker": 0},
            "records": [{"filename": "sample.py"}],
        }
    )
    validate_manifest(sample)
    accepted_controls += 1

    corrupted = json.loads(json.dumps(sample))
    corrupted["records"][0]["filename"] = "mutated.py"
    try:
        validate_manifest(corrupted)
    except PrimePowerImportSmokeError:
        rejected_mutations += 1
    else:
        raise PrimePowerImportSmokeError("manifest digest mutation was accepted")

    require(accepted_controls == 6, "exact six positive controls required")
    require(rejected_mutations == 6, "exact six rejected mutations required")
    return {
        "accepted_controls": accepted_controls,
        "rejected_mutations": rejected_mutations,
        "all_n_proved_by_checker": 0,
    }


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    validate_manifest(manifest)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json(manifest) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run six positive controls and six deliberate rejection mutations",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="write the sealed machine-readable runtime manifest to this path",
    )
    args = parser.parse_args()
    manifest = exact_audit(regression.repository_root())
    if args.self_test:
        payload = validate_manifest(manifest)
        payload["mutation_self_test"] = mutation_self_test()
        manifest = seal_manifest(payload)
    if args.manifest is not None:
        write_manifest(args.manifest, manifest)
    claims = validate_manifest(manifest)["claims"]
    print(json.dumps(claims, sort_keys=True))


if __name__ == "__main__":
    main()
