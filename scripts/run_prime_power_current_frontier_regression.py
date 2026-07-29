#!/usr/bin/env python3
"""Run dependency-free regression checks for the complete current prime-power frontier.

The suite checks source syntax, the fixed thirteen-frontier/forty-three-target census, canonical endpoint
presence, honesty-ledger synchronization and executable structural self-tests. It validates research
infrastructure only and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


class CurrentFrontierRegressionError(RuntimeError):
    """Raised when the current-frontier source or structural regression suite fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CurrentFrontierRegressionError(message)


REPOSITORY_MARKERS = ("README.md", "STATUS.md", "scripts", "proofs", "docs")
CANONICAL_ENDPOINTS = (
    "check_prime_power_geometry_selector_frontier_v2.py",
    "check_prime_power_auxiliary_semantics_frontier_v2.py",
    "check_prime_power_state_equivalence_frontier.py",
    "check_prime_power_component_scale_frontier.py",
    "check_prime_power_interface_exhaustiveness_frontier.py",
    "check_prime_power_global_rank_frontier.py",
    "check_prime_power_state_predicate_frontier.py",
    "check_prime_power_row_theorem_frontier.py",
    "check_prime_power_global_family_exhaustiveness_frontier.py",
    "check_prime_power_exceptional_chamber_frontier.py",
    "check_prime_power_final_premise_frontiers.py",
    "check_prime_power_canonical_frontier_roots.py",
    "check_prime_power_final_support_handoff_frontiers_v2.py",
)
SELF_TESTS = (
    ("check_prime_power_canonical_frontier_roots.py", "--self-test"),
    ("check_prime_power_final_support_handoff_frontiers_v2.py", "--self-test-roots"),
    ("check_prime_power_all_open_target_fixture.py", "--self-test"),
)
DOCUMENT_EXPECTATIONS: dict[str, tuple[str, ...]] = {
    "README.md": (
        "does **not** contain a complete proof",
        "Python 3.10+",
    ),
    "STATUS.md": (
        "CMR2741",
        "remains open",
        "check_prime_power_final_support_handoff_frontiers_v2.py",
        "check_prime_power_all_open_target_fixture.py",
        "check_prime_power_hard_core_exchange_normal_form.py",
        "check_prime_power_hard_core_exchange_realisability.py",
        "manifest_sha256",
        "all_n_proved_by_checker = 0",
    ),
    "proofs/composite-modulus-theorem-index-live-continuation-8.md": (
        "CMR2734--2741",
        "No finite selector calculation, documentary checker or runtime manifest substitutes",
    ),
    "docs/11-open-bottlenecks.md": (
        "CMR2741",
        "run_prime_power_current_frontier_regression.py",
        "check_prime_power_all_open_target_fixture.py",
        "check_prime_power_hard_core_exchange_normal_form.py",
        "check_prime_power_hard_core_exchange_realisability.py",
        "current-frontier-runtime.json",
        "all_n_proved_by_checker = 0",
    ),
    "docs/427-prime-power-canonical-frontier-roots.md": (
        "CMR2663",
        "all_n_proved_by_checker = 0",
    ),
    "docs/428-prime-power-current-frontier-regression.md": (
        "CMR2664--CMR2675",
        "all_n_proved_by_checker = 0",
    ),
    "docs/429-prime-power-negative-regression-open-fixture.md": (
        "CMR2676--CMR2691",
        "all_n_proved_by_checker = 0",
    ),
    "docs/430-prime-power-isolated-import-honesty-audit.md": (
        "CMR2692--CMR2705",
        "Correction:",
        "all_n_proved_by_checker = 0",
    ),
    "docs/431-prime-power-reproducible-runtime-manifest.md": (
        "CMR2706--CMR2721",
        "manifest_sha256",
        "all_n_proved_by_checker = 0",
    ),
    "docs/432-prime-power-hard-core-exchange-normal-form.md": (
        "CMR2722--CMR2733",
        "ae35c2afa6574f602ccc2bb10124c0a5743ae4d712ebd967f93e56680928b1bf",
        "all_n_proved_by_checker = 0",
    ),
    "docs/433-prime-power-hard-core-exchange-realisability.md": (
        "CMR2734--CMR2741",
        "2b4d743fc4e98d39d63c2c7415ec33639692f8bd7b484dcb630ddb2aefd8896c",
        "all_n_proved_by_checker = 0",
    ),
    ".github/workflows/current-frontier-regression.yml": (
        "actions/upload-artifact@v4",
        "check_prime_power_hard_core_exchange_normal_form.py",
        "check_prime_power_hard_core_exchange_realisability.py",
        "--manifest",
        "current-frontier-runtime-python-${{ matrix.python-version }}",
    ),
}


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if all((candidate / marker).exists() for marker in REPOSITORY_MARKERS):
            return candidate
    raise CurrentFrontierRegressionError("unable to locate repository root")


def source_text(path: Path) -> str:
    require(path.is_file(), f"missing required file: {path}")
    return path.read_text(encoding="utf-8")


def literal_assignment(path: Path, name: str) -> Any:
    tree = ast.parse(source_text(path), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return ast.literal_eval(node.value)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                return ast.literal_eval(node.value)
    raise CurrentFrontierRegressionError(f"{path}: literal assignment {name} not found")


def syntax_inventory(scripts_dir: Path) -> list[str]:
    paths = sorted(
        path
        for path in scripts_dir.glob("*.py")
        if path.name.startswith(
            ("check_prime_power_", "verify_prime_power_", "run_prime_power_", "test_prime_power_")
        )
    )
    require(paths, "no prime-power scripts found")
    for path in paths:
        compile(source_text(path), str(path), "exec")
    return [path.name for path in paths]


def validate_target_frontier_literals(
    target_rows: Any,
    frontiers: Any,
) -> tuple[list[str], list[str]]:
    """Validate literal target/frontier tables without importing the checker module."""
    require(isinstance(target_rows, list), "TARGET_ROWS must be a literal list")
    require(isinstance(frontiers, dict), "FRONTIERS must be a literal dictionary")
    require(len(target_rows) == 43, "atomic target table must contain exactly 43 targets")
    require(len(frontiers) == 13, "frontier table must contain exactly 13 groups")
    require(
        all(isinstance(key, str) and key for key in frontiers),
        "frontier IDs must be nonempty strings",
    )
    require(
        all(isinstance(value, str) and value for value in frontiers.values()),
        "frontier titles must be nonempty strings",
    )

    target_ids: list[str] = []
    frontier_ids: list[str] = []
    for index, row in enumerate(target_rows, start=1):
        require(
            isinstance(row, tuple) and len(row) == 10,
            f"target row {index}: exact ten-field tuple required",
        )
        target_id, frontier_id = row[0], row[1]
        require(isinstance(target_id, str), f"target row {index}: string target ID required")
        require(
            target_id.startswith(f"T{index:02d}_"),
            f"target row {index}: sequential target ID required",
        )
        require(frontier_id in frontiers, f"target {target_id}: unknown frontier {frontier_id}")
        target_ids.append(target_id)
        frontier_ids.append(frontier_id)

    require(len(target_ids) == len(set(target_ids)), "duplicate atomic target ID")
    require(set(frontier_ids) == set(frontiers), "every frontier must contain at least one target")
    return target_ids, list(frontiers)


def exact_target_frontier_census(atomic_path: Path) -> tuple[list[str], list[str]]:
    return validate_target_frontier_literals(
        literal_assignment(atomic_path, "TARGET_ROWS"),
        literal_assignment(atomic_path, "FRONTIERS"),
    )


def validate_endpoint_text(filename: str, text: str) -> None:
    require(text.strip(), f"canonical endpoint {filename}: empty source")
    require(
        "all_n_proved_by_checker" in text,
        f"canonical endpoint {filename}: honesty marker missing",
    )
    compile(text, filename, "exec")


def endpoint_audit(scripts_dir: Path) -> list[str]:
    audited: list[str] = []
    for filename in CANONICAL_ENDPOINTS:
        path = scripts_dir / filename
        validate_endpoint_text(filename, source_text(path))
        audited.append(filename)
    return audited


def validate_document_markers(relative_path: str, text: str, markers: tuple[str, ...]) -> None:
    require(text.strip(), f"{relative_path}: empty document")
    for marker in markers:
        require(marker in text, f"{relative_path}: missing synchronization marker {marker!r}")


def document_audit(root: Path) -> list[str]:
    audited: list[str] = []
    for relative_path, markers in DOCUMENT_EXPECTATIONS.items():
        validate_document_markers(relative_path, source_text(root / relative_path), markers)
        audited.append(relative_path)
    return audited


def run_self_test(root: Path, script: str, argument: str) -> dict[str, Any]:
    command = [sys.executable, str(root / "scripts" / script), argument]
    environment = dict(os.environ)
    environment.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    completed = subprocess.run(
        command,
        cwd=root,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )
    require(
        completed.returncode == 0,
        f"self-test failed: {' '.join(command)}\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
    )
    output = completed.stdout.strip()
    require(output, f"self-test {script} produced no output")
    return {
        "script": script,
        "argument": argument,
        "stdout": output,
        "returncode": completed.returncode,
    }


def exact_regression(root: Path, static_only: bool = False) -> dict[str, Any]:
    scripts_dir = root / "scripts"
    syntax_files = syntax_inventory(scripts_dir)
    target_ids, frontier_ids = exact_target_frontier_census(
        scripts_dir / "check_prime_power_atomic_frontier_execution.py"
    )
    endpoints = endpoint_audit(scripts_dir)
    documents = document_audit(root)
    self_tests = [] if static_only else [
        run_self_test(root, script, argument) for script, argument in SELF_TESTS
    ]
    claims = {
        "syntax_checked_prime_power_scripts": len(syntax_files),
        "frontier_groups": len(frontier_ids),
        "atomic_targets": len(target_ids),
        "canonical_endpoints": len(endpoints),
        "synchronized_documents": len(documents),
        "executable_self_tests": len(self_tests),
        "static_only": int(static_only),
        "python_major_minor": f"{sys.version_info.major}.{sys.version_info.minor}",
        "all_n_proved_by_checker": 0,
    }
    return {
        "syntax_checked_files": syntax_files,
        "frontier_ids": frontier_ids,
        "target_ids": target_ids,
        "canonical_endpoint_files": endpoints,
        "synchronized_document_files": documents,
        "self_test_results": self_tests,
        "claims": claims,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--static-only",
        action="store_true",
        help="skip executable structural self-tests and run source/document checks only",
    )
    args = parser.parse_args()
    result = exact_regression(repository_root(), static_only=args.static_only)
    print(json.dumps(result["claims"], sort_keys=True))


if __name__ == "__main__":
    main()
