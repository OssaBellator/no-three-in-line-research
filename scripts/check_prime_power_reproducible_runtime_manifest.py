#!/usr/bin/env python3
"""Run the strict reproducible prime-power import audit and write its sealed runtime manifest.

This entrypoint supersedes the initial import-smoke launcher by disabling all automatic site initialization
(``-S``), disabling the user site (``-s``), suppressing bytecode (``-B``), sanitizing inherited ``PYTHON*``
variables and requiring ``no_site = 1`` in every child process. It validates software infrastructure only and
permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import check_prime_power_import_smoke as legacy
import run_prime_power_current_frontier_regression as regression


class ReproducibleRuntimeManifestError(legacy.PrimePowerImportSmokeError):
    """Raised when the strict runtime launcher or manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReproducibleRuntimeManifestError(message)


STRICT_RUNTIME_PROBE = legacy.RUNTIME_PROBE.replace(
    '"no_user_site": int(sys.flags.no_user_site),',
    '"no_user_site": int(sys.flags.no_user_site),\n'
    '    "no_site": int(sys.flags.no_site),',
)
STRICT_IMPORT_PROBE = legacy.IMPORT_PROBE.replace(
    '"no_user_site": int(sys.flags.no_user_site),',
    '"no_user_site": int(sys.flags.no_user_site),\n'
    '    "no_site": int(sys.flags.no_site),',
)


def strict_run_probe(
    code: str,
    *,
    arguments: list[str] | None = None,
    timeout_seconds: float = 10.0,
) -> subprocess.CompletedProcess[str]:
    require(timeout_seconds > 0, "probe timeout must be positive")
    return subprocess.run(
        [sys.executable, "-B", "-S", "-s", "-c", code, *(arguments or [])],
        env=legacy.controlled_environment(),
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )


def strict_runtime_configuration_probe() -> dict[str, Any]:
    payloads: list[dict[str, Any]] = []
    for index in range(2):
        completed = strict_run_probe(STRICT_RUNTIME_PROBE)
        require(
            completed.returncode == 0,
            (
                f"strict runtime configuration probe {index + 1} failed\n"
                f"stdout:\n{completed.stdout}\n"
                f"stderr:\n{completed.stderr}"
            ),
        )
        payloads.append(
            legacy.parse_probe_payload(
                completed.stdout,
                legacy.RUNTIME_PREFIX,
                "strict runtime configuration",
            )
        )
    require(payloads[0] == payloads[1], "strict runtime configuration is not reproducible")
    payload = payloads[0]
    require(payload.get("dont_write_bytecode") == 1, "bytecode suppression is not active")
    require(payload.get("no_user_site") == 1, "user-site suppression is not active")
    require(payload.get("no_site") == 1, "automatic site initialization is not disabled")
    require(payload.get("isolated") == 0, "unexpected -I isolated mode is active")
    fingerprint = payload.get("hash_fingerprint")
    require(isinstance(fingerprint, str) and fingerprint, "hash fingerprint missing")
    return payload


def strict_import_module(
    path: Path,
    *,
    expected_hash_fingerprint: str,
    timeout_seconds: float = legacy.IMPORT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    require(path.is_file(), f"missing strict import-smoke module: {path}")
    require(timeout_seconds > 0, "import timeout must be positive")
    digest, byte_count = legacy.source_digest(path)
    try:
        completed = strict_run_probe(
            STRICT_IMPORT_PROBE,
            arguments=[str(path)],
            timeout_seconds=timeout_seconds,
        )
    except subprocess.TimeoutExpired as error:
        raise ReproducibleRuntimeManifestError(
            f"strict import smoke timed out after {timeout_seconds:g}s: {path.name}"
        ) from error
    require(
        completed.returncode == 0,
        (
            f"strict import smoke failed: {path.name}\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        ),
    )
    payload = legacy.parse_probe_payload(
        completed.stdout,
        legacy.PROBE_PREFIX,
        path.name,
    )
    require(payload.get("module") == path.stem, f"import module marker mismatch: {path.name}")
    require(
        payload.get("hash_fingerprint") == expected_hash_fingerprint,
        f"hash seed drift during import: {path.name}",
    )
    require(payload.get("dont_write_bytecode") == 1, f"bytecode enabled: {path.name}")
    require(payload.get("no_user_site") == 1, f"user site enabled: {path.name}")
    require(payload.get("no_site") == 1, f"site initialization enabled: {path.name}")
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
        "no_site": payload["no_site"],
        "third_party_path_entries": payload["third_party_path_entries"],
    }


def install_strict_launcher() -> None:
    legacy.RUNTIME_PROBE = STRICT_RUNTIME_PROBE
    legacy.IMPORT_PROBE = STRICT_IMPORT_PROBE
    legacy.run_probe = strict_run_probe
    legacy.runtime_configuration_probe = strict_runtime_configuration_probe
    legacy.import_module_isolated = strict_import_module


def exact_audit(root: Path) -> dict[str, Any]:
    install_strict_launcher()
    manifest = legacy.exact_audit(root)
    payload = legacy.validate_manifest(manifest)
    records = payload["module_import_records"]
    require(records, "strict runtime manifest requires module records")
    require(
        all(record.get("no_site") == 1 for record in records),
        "every module record must disable site initialization",
    )
    payload["python_runtime"]["no_site"] = 1
    payload["claims"]["site_initialization_disabled"] = 1
    payload["claims"]["strict_runtime_manifest"] = 1
    payload["claims"]["all_n_proved_by_checker"] = 0
    return legacy.seal_manifest(payload)


def mutation_self_test() -> dict[str, int]:
    install_strict_launcher()
    result = legacy.mutation_self_test()
    require(result["accepted_controls"] == 6, "strict audit requires six accepted controls")
    require(result["rejected_mutations"] == 6, "strict audit requires six rejected mutations")
    require(result["all_n_proved_by_checker"] == 0, "strict audit honesty drift")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run six accepted controls and six deliberate rejection mutations",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="write the sealed strict runtime manifest to this path",
    )
    args = parser.parse_args()

    manifest = exact_audit(regression.repository_root())
    if args.self_test:
        payload = legacy.validate_manifest(manifest)
        payload["mutation_self_test"] = mutation_self_test()
        manifest = legacy.seal_manifest(payload)
    if args.manifest is not None:
        legacy.write_manifest(args.manifest, manifest)
    claims = legacy.validate_manifest(manifest)["claims"]
    print(json.dumps(claims, sort_keys=True))


if __name__ == "__main__":
    main()
