#!/usr/bin/env python3
"""Import-smoke every current prime-power module and audit executable honesty semantics.

Each discovered checker, verifier, runner and test module is imported in a fresh isolated Python interpreter.
The audit catches missing sibling imports, import-time exceptions and import hangs that syntax compilation cannot
detect. Canonical endpoints must contain executable evidence that the all-n result is fixed at zero; a docstring
or error-message phrase alone is insufficient. This is software validation only and permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import run_prime_power_current_frontier_regression as regression


class PrimePowerImportSmokeError(RuntimeError):
    """Raised when isolated import or executable honesty validation fails."""


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
IMPORT_PROBE = r"""
import importlib.util
import sys
from pathlib import Path

path = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(path.parent))
module_name = path.stem
spec = importlib.util.spec_from_file_location(module_name, path)
if spec is None or spec.loader is None:
    raise RuntimeError(f"unable to create import spec for {path}")
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
print(f"IMPORTED:{module_name}")
"""


def script_inventory(scripts_dir: Path) -> list[Path]:
    paths = sorted(
        path
        for path in scripts_dir.glob("*.py")
        if path.name.startswith(SCRIPT_PREFIXES)
    )
    require(paths, "no prime-power modules found")
    return paths


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


def has_executable_zero_honesty(text: str, filename: str) -> bool:
    tree = ast.parse(text, filename=filename)
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for key, value in zip(node.keys, node.values):
                if (
                    isinstance(key, ast.Constant)
                    and key.value in {"all_n", "all_n_proved_by_checker"}
                    and is_literal_zero(value)
                ):
                    return True
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if value is not None and is_literal_zero(value) and any(
                mentions_all_n(target) for target in targets
            ):
                return True
        if isinstance(node, ast.Compare):
            operands = [node.left, *node.comparators]
            if any(is_literal_zero(operand) for operand in operands) and any(
                mentions_all_n(operand) for operand in operands
            ):
                return True
    return False


def validate_endpoint_honesty(filename: str, text: str) -> None:
    require(text.strip(), f"{filename}: empty source")
    compile(text, filename, "exec")
    require(
        has_executable_zero_honesty(text, filename),
        f"{filename}: no executable all-n zero condition",
    )


def import_module_isolated(
    path: Path,
    *,
    timeout_seconds: float = IMPORT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    require(path.is_file(), f"missing import-smoke module: {path}")
    require(timeout_seconds > 0, "import timeout must be positive")
    command = [sys.executable, "-I", "-c", IMPORT_PROBE, str(path)]
    environment = dict(os.environ)
    environment.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    try:
        completed = subprocess.run(
            command,
            cwd=path.parent,
            env=environment,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
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
    marker = f"IMPORTED:{path.stem}"
    output_lines = [line.strip() for line in completed.stdout.splitlines() if line.strip()]
    require(marker in output_lines, f"import smoke marker missing: {path.name}")
    return {
        "filename": path.name,
        "returncode": completed.returncode,
        "stdout_lines": output_lines,
    }


def exact_audit(root: Path) -> dict[str, Any]:
    scripts_dir = root / "scripts"
    paths = script_inventory(scripts_dir)
    imports = [import_module_isolated(path) for path in paths]
    endpoint_files: list[str] = []
    for filename in regression.CANONICAL_ENDPOINTS:
        path = scripts_dir / filename
        validate_endpoint_honesty(filename, regression.source_text(path))
        endpoint_files.append(filename)
    claims = {
        "isolated_imported_prime_power_modules": len(imports),
        "semantic_honesty_endpoints": len(endpoint_files),
        "per_module_timeout_seconds": int(IMPORT_TIMEOUT_SECONDS),
        "fresh_interpreter_per_module": 1,
        "all_n_proved_by_checker": 0,
    }
    return {
        "import_results": imports,
        "semantic_honesty_endpoint_files": endpoint_files,
        "claims": claims,
    }


def mutation_self_test() -> dict[str, int]:
    accepted_controls = 0
    rejected_mutations = 0
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        good = root / "good.py"
        good.write_text("VALUE = 1\n", encoding="utf-8")
        result = import_module_isolated(good, timeout_seconds=10.0)
        require(result["returncode"] == 0, "good import control failed")
        accepted_controls += 1

        failing = root / "failing.py"
        failing.write_text("raise RuntimeError('boom')\n", encoding="utf-8")
        try:
            import_module_isolated(failing, timeout_seconds=10.0)
        except PrimePowerImportSmokeError:
            rejected_mutations += 1
        else:
            raise PrimePowerImportSmokeError("import exception mutation was accepted")

        hanging = root / "hanging.py"
        hanging.write_text("import time\ntime.sleep(1.0)\n", encoding="utf-8")
        try:
            import_module_isolated(hanging, timeout_seconds=0.2)
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

    require(accepted_controls == 3, "exact three positive controls required")
    require(rejected_mutations == 5, "exact five rejected mutations required")
    return {
        "accepted_controls": accepted_controls,
        "rejected_mutations": rejected_mutations,
        "all_n_proved_by_checker": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run the complete import/honesty audit plus five deliberate rejection mutations",
    )
    args = parser.parse_args()
    result = exact_audit(regression.repository_root())
    if args.self_test:
        result["mutation_self_test"] = mutation_self_test()
    print(json.dumps(result["claims"], sort_keys=True))


if __name__ == "__main__":
    main()
