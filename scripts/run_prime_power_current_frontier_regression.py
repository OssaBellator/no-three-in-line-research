#!/usr/bin/env python3
"""Run dependency-free regression checks for the current prime-power frontier.

The suite checks source syntax, the fixed thirteen-frontier/forty-three-target
census, canonical endpoint presence, honesty-ledger synchronization, executable
structural self-tests, finite theorem checkers and the T03/T21 population bridge.
It validates research infrastructure and stated finite claims only and permanently
reports ``all_n_proved_by_checker = 0``.
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
    pass


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
FINITE_THEOREM_CHECKS = (
    "check_prime_power_canonical_prescription_partition.py",
    "check_prime_power_target_trigger_response_partition.py",
    "check_prime_power_canonical_target_dispatch.py",
    "check_prime_power_hard_core_exchange_normal_form.py",
    "check_prime_power_hard_core_exchange_realisability.py",
    "check_prime_power_hard_core_two_point_classification.py",
    "check_prime_power_hard_core_collinear_backgrounds.py",
    "check_prime_power_hard_core_pivot_line_energy.py",
    "check_prime_power_hard_core_extremal_stability.py",
)
FRONTIER_BRIDGE_CHECKS = (
    ("check_prime_power_hard_core_population_bridge.py", ("--self-test",)),
)
DOCUMENT_EXPECTATIONS: dict[str, tuple[str, ...]] = {
    "README.md": ("does **not** contain a complete proof", "Python 3.10+"),
    "STATUS.md": (
        "CMR2827", "remains open",
        "check_prime_power_final_support_handoff_frontiers_v2.py",
        "check_prime_power_all_open_target_fixture.py",
        *FINITE_THEOREM_CHECKS,
        "check_prime_power_hard_core_population_bridge.py",
        "manifest_sha256", "all_n_proved_by_checker = 0",
    ),
    "proofs/composite-modulus-theorem-index-live-continuation-8.md": (
        "CMR2818--2827",
        "No finite selector calculation, documentary checker or runtime manifest substitutes",
    ),
    "docs/11-open-bottlenecks.md": (
        "CMR2827", "run_prime_power_current_frontier_regression.py",
        "check_prime_power_all_open_target_fixture.py", *FINITE_THEOREM_CHECKS,
        "check_prime_power_hard_core_population_bridge.py",
        "current-frontier-runtime.json", "all_n_proved_by_checker = 0",
    ),
    "docs/427-prime-power-canonical-frontier-roots.md": ("CMR2663", "all_n_proved_by_checker = 0"),
    "docs/428-prime-power-current-frontier-regression.md": ("CMR2664--CMR2675", "all_n_proved_by_checker = 0"),
    "docs/429-prime-power-negative-regression-open-fixture.md": ("CMR2676--CMR2691", "all_n_proved_by_checker = 0"),
    "docs/430-prime-power-isolated-import-honesty-audit.md": ("CMR2692--CMR2705", "Correction:", "all_n_proved_by_checker = 0"),
    "docs/431-prime-power-reproducible-runtime-manifest.md": ("CMR2706--CMR2721", "manifest_sha256", "all_n_proved_by_checker = 0"),
    "docs/432-prime-power-hard-core-exchange-normal-form.md": (
        "CMR2722--CMR2733", "ae35c2afa6574f602ccc2bb10124c0a5743ae4d712ebd967f93e56680928b1bf", "all_n_proved_by_checker = 0"),
    "docs/433-prime-power-hard-core-exchange-realisability.md": (
        "CMR2734--CMR2741", "2b4d743fc4e98d39d63c2c7415ec33639692f8bd7b484dcb630ddb2aefd8896c", "all_n_proved_by_checker = 0"),
    "docs/434-prime-power-hard-core-two-point-classification.md": (
        "CMR2742--CMR2751", "4ee3f69f653544853c04f0bf4822e839d537a52a41fe4612410604d7bc630f47", "all_n_proved_by_checker = 0"),
    "docs/435-prime-power-hard-core-collinear-backgrounds.md": (
        "CMR2752--CMR2761", "3e818c8ece650173676e3afaa94b0adfb65fd0185146dc4b49485131a020c99a", "all_n_proved_by_checker = 0"),
    "docs/436-prime-power-hard-core-pivot-line-energy.md": (
        "CMR2762--CMR2771", "a88ddee378c70d2713734a836aa3c18683d6db193ebbb89d52921efa55efa4f3", "all_n_proved_by_checker = 0"),
    "docs/437-prime-power-hard-core-extremal-stability.md": (
        "CMR2772--CMR2781", "0bddec3bea04c1e38a6b3d11919d9f1f23566e6284644f37223a7c290b4a6131", "all_n_proved_by_checker = 0"),
    "docs/438-prime-power-hard-core-population-bridge.md": (
        "CMR2782--CMR2793", "c7773e0f18779f6fa89db7d31e802c281e4e2618e60096a9a3d86471d08d528c",
        "actual_parent_rule_present = 0", "t21_semantic_chambers_proved = 0", "all_n_proved_by_checker = 0"),
    "docs/439-prime-power-canonical-prescription-parent-rule.md": (
        "CMR2794--CMR2805", "dca487a954f03f5aaebf09394ab427ef5b338f0e107adf6581146d84863ce39c",
        "conditional_parent_rule_clause_ready = 1", "actual_global_parent_rule_complete = 0", "all_n_proved_by_checker = 0"),
    "docs/440-prime-power-target-trigger-response-partition.md": (
        "CMR2806--CMR2817", "c7239521fb73e0347783e76ebfde83d96e968712376745542b5a93888312c0ef",
        "local_target_response_rule_ready = 1", "actual_global_parent_rule_complete = 0", "all_n_proved_by_checker = 0"),
    "docs/441-prime-power-canonical-anchor-target-dispatch.md": (
        "CMR2818--CMR2827", "634318242ece5cab549b9394ba33e116d7c1b01b4c74d5a02e276004fe1e8444",
        "canonical_target_bank_external_choice_required = 0", "local_anchor_dispatch_complete = 1",
        "actual_global_parent_rule_complete = 0", "all_n_proved_by_checker = 0"),
    ".github/workflows/current-frontier-regression.yml": (
        "actions/upload-artifact@v4", *FINITE_THEOREM_CHECKS,
        "check_prime_power_hard_core_population_bridge.py", "--manifest",
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
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            return ast.literal_eval(node.value)
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == name:
            return ast.literal_eval(node.value)
    raise CurrentFrontierRegressionError(f"{path}: literal assignment {name} not found")


def syntax_inventory(scripts_dir: Path) -> list[str]:
    paths = sorted(path for path in scripts_dir.glob("*.py")
                   if path.name.startswith(("check_prime_power_", "verify_prime_power_", "run_prime_power_", "test_prime_power_")))
    require(paths, "no prime-power scripts found")
    for path in paths:
        compile(source_text(path), str(path), "exec")
    return [path.name for path in paths]


def validate_target_frontier_literals(target_rows: Any, frontiers: Any) -> tuple[list[str], list[str]]:
    require(isinstance(target_rows, list) and len(target_rows) == 43, "atomic target table must contain exactly 43 targets")
    require(isinstance(frontiers, dict) and len(frontiers) == 13, "frontier table must contain exactly 13 groups")
    require(all(isinstance(key, str) and key for key in frontiers), "frontier IDs must be nonempty strings")
    require(all(isinstance(value, str) and value for value in frontiers.values()), "frontier titles must be nonempty strings")
    target_ids, frontier_ids = [], []
    for index, row in enumerate(target_rows, start=1):
        require(isinstance(row, tuple) and len(row) == 10, f"target row {index}: exact ten-field tuple required")
        target_id, frontier_id = row[0], row[1]
        require(isinstance(target_id, str) and target_id.startswith(f"T{index:02d}_"), f"target row {index}: sequential target ID required")
        require(frontier_id in frontiers, f"target {target_id}: unknown frontier {frontier_id}")
        target_ids.append(target_id)
        frontier_ids.append(frontier_id)
    require(len(target_ids) == len(set(target_ids)), "duplicate atomic target ID")
    require(set(frontier_ids) == set(frontiers), "every frontier must contain at least one target")
    return target_ids, list(frontiers)


def exact_target_frontier_census(atomic_path: Path) -> tuple[list[str], list[str]]:
    return validate_target_frontier_literals(literal_assignment(atomic_path, "TARGET_ROWS"), literal_assignment(atomic_path, "FRONTIERS"))


def validate_endpoint_text(filename: str, text: str) -> None:
    require(text.strip(), f"canonical endpoint {filename}: empty source")
    require("all_n_proved_by_checker" in text, f"canonical endpoint {filename}: honesty marker missing")
    compile(text, filename, "exec")


def endpoint_audit(scripts_dir: Path) -> list[str]:
    for filename in CANONICAL_ENDPOINTS:
        validate_endpoint_text(filename, source_text(scripts_dir / filename))
    return list(CANONICAL_ENDPOINTS)


def validate_document_markers(relative_path: str, text: str, markers: tuple[str, ...]) -> None:
    require(text.strip(), f"{relative_path}: empty document")
    for marker in markers:
        require(marker in text, f"{relative_path}: missing synchronization marker {marker!r}")


def document_audit(root: Path) -> list[str]:
    for path, markers in DOCUMENT_EXPECTATIONS.items():
        validate_document_markers(path, source_text(root / path), markers)
    return list(DOCUMENT_EXPECTATIONS)


def subprocess_environment() -> dict[str, str]:
    environment = dict(os.environ)
    environment.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    return environment


def run_script(root: Path, script: str, arguments: tuple[str, ...] = ()) -> dict[str, Any]:
    command = [sys.executable, str(root / "scripts" / script), *arguments]
    completed = subprocess.run(command, cwd=root, env=subprocess_environment(), check=False, capture_output=True, text=True)
    require(completed.returncode == 0,
            f"script failed: {' '.join(command)}\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}")
    output = completed.stdout.strip()
    require(output, f"script {script} produced no output")
    return {"script": script, "arguments": list(arguments), "stdout": output, "returncode": completed.returncode}


def run_self_test(root: Path, script: str, argument: str) -> dict[str, Any]:
    result = run_script(root, script, (argument,))
    return {"script": result["script"], "argument": argument,
            "stdout": result["stdout"], "returncode": result["returncode"]}


def exact_regression(root: Path, static_only: bool = False) -> dict[str, Any]:
    scripts = root / "scripts"
    syntax_files = syntax_inventory(scripts)
    target_ids, frontier_ids = exact_target_frontier_census(scripts / "check_prime_power_atomic_frontier_execution.py")
    endpoints = endpoint_audit(scripts)
    documents = document_audit(root)
    self_tests = [] if static_only else [run_self_test(root, script, argument) for script, argument in SELF_TESTS]
    theorem_checks = [] if static_only else [run_script(root, script) for script in FINITE_THEOREM_CHECKS]
    bridge_checks = [] if static_only else [run_script(root, script, arguments) for script, arguments in FRONTIER_BRIDGE_CHECKS]
    claims = {
        "syntax_checked_prime_power_scripts": len(syntax_files),
        "frontier_groups": len(frontier_ids), "atomic_targets": len(target_ids),
        "canonical_endpoints": len(endpoints), "synchronized_documents": len(documents),
        "executable_self_tests": len(self_tests), "finite_theorem_checks": len(theorem_checks),
        "frontier_bridge_checks": len(bridge_checks), "static_only": int(static_only),
        "python_major_minor": f"{sys.version_info.major}.{sys.version_info.minor}",
        "all_n_proved_by_checker": 0,
    }
    return {"syntax_checked_files": syntax_files, "frontier_ids": frontier_ids,
            "target_ids": target_ids, "canonical_endpoint_files": endpoints,
            "synchronized_document_files": documents, "self_test_results": self_tests,
            "finite_theorem_results": theorem_checks, "frontier_bridge_results": bridge_checks,
            "claims": claims}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--static-only", action="store_true",
                        help="skip executable structural, finite-theorem and frontier-bridge checks")
    args = parser.parse_args()
    print(json.dumps(exact_regression(repository_root(), args.static_only)["claims"], sort_keys=True))


if __name__ == "__main__":
    main()
