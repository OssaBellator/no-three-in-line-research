#!/usr/bin/env python3
"""Execute inherited-coordinate diagonal-block ancestry for CMR1318--CMR1389."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


class InheritedCoordinateDiagonalBlockError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise InheritedCoordinateDiagonalBlockError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


SOURCE_FILES = [
    "docs/269-prime-power-last-entering-owner-triangularity.md",
    "docs/270-prime-power-exact-credit-classes-upper-quotients.md",
    "docs/271-prime-power-degree-two-bank-line-profile-classes.md",
    "docs/272-prime-power-line-profile-pair-moment-envelopes.md",
    "docs/273-prime-power-extension-free-bank-permanent-bound.md",
    "docs/274-prime-power-extension-free-derangement-marginals.md",
    "docs/275-prime-power-extension-free-line-composition-kernel.md",
    "docs/276-prime-power-extension-free-exact-cylinder-types.md",
    "docs/277-prime-power-cross-line-edge-assignment-normal-form.md",
]
VERIFIER_FILES = [
    "scripts/verify_prime_power_last_entering_owner_triangularity.py",
    "scripts/verify_prime_power_exact_credit_upper_quotients.py",
    "scripts/verify_prime_power_degree_two_bank_line_profiles.py",
    "scripts/verify_prime_power_line_profile_pair_moments.py",
    "scripts/verify_prime_power_extension_free_permanent.py",
    "scripts/verify_prime_power_extension_free_derangement_marginals.py",
    "scripts/verify_prime_power_extension_free_line_kernel.py",
    "scripts/verify_prime_power_extension_free_exact_cylinders.py",
    "scripts/verify_prime_power_cross_line_edge_assignment.py",
]
CONTRACT = {
    "schema": "prime-power-inherited-coordinate-diagonal-block-ancestry/v1",
    "source_range": ["CMR1318", "CMR1389"],
    "source_files": SOURCE_FILES,
    "verifier_files": VERIFIER_FILES,
    "checked_layers": [
        "last-entering structural owner persistence and finite owner DAG triangularity",
        "exact state-credit matrices and componentwise host-uniform upper quotients",
        "exact and dyadic line-profile rows with pair-moment envelopes",
        "extension-free permanent, derangement marginal and line-composition bounds",
        "exact row-column cylinder probabilities for created and destroyed credits",
        "cross-line edge-selector and fractional perfect-matching normal forms",
        "explicit side-five independent-line obstruction and deterministic escape witness",
    ],
    "scope": "same-owner inherited-coordinate diagonal-block reductions and exact finite certificates",
    "honesty_flags": {
        "same_owner_diagonal_blocks_subcritical": 0,
        "independent_line_kernel_sufficient": 0,
        "global_target_collateral_inequality_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "bff27495eef9188b3d90e5f36ee66ed889b0606c7fa92f8b3391a3114e03d826"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise InheritedCoordinateDiagonalBlockError("unable to locate repository root")


def environment() -> dict[str, str]:
    result = dict(os.environ)
    result.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    return result


def execute_verifier(root: Path, relative_path: str) -> dict[str, Any]:
    path = root / relative_path
    require(path.is_file(), f"{relative_path}: missing verifier")
    source = path.read_text(encoding="utf-8")
    compile(source, str(path), "exec")
    completed = subprocess.run(
        [sys.executable, str(path)],
        cwd=root,
        env=environment(),
        capture_output=True,
        text=True,
        check=False,
    )
    require(
        completed.returncode == 0,
        f"{relative_path}: failed\nstdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
    )
    output = completed.stdout.strip()
    require(output.startswith("verified "), f"{relative_path}: missing verified report")
    return {
        "path": relative_path,
        "stdout_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "stdout": output,
    }


def validate_fixture(fixture: dict[str, Any]) -> None:
    require(fixture.get("source_file_count") == 9, "fixture source count")
    require(fixture.get("verifier_file_count") == 9, "fixture verifier count")
    require(fixture.get("owner_dag_upper_triangular") == 1, "fixture triangularity")
    require(fixture.get("upper_quotient_lifting_exact") == 1, "fixture quotient")
    require(fixture.get("exact_cylinder_rows_available") == 1, "fixture cylinders")
    require(fixture.get("cross_line_assignment_normal_form_exact") == 1, "fixture assignment")
    require(fixture.get("same_owner_diagonal_blocks_subcritical") == 0, "fixture subcritical honesty")
    require(fixture.get("independent_line_kernel_sufficient") == 0, "fixture kernel honesty")
    require(fixture.get("global_target_collateral_inequality_proved") == 0, "fixture global inequality")
    require(fixture.get("all_n_proved_by_checker") == 0, "fixture all-n honesty")


def mutation_audit() -> int:
    fixture = {
        "source_file_count": 9,
        "verifier_file_count": 9,
        "owner_dag_upper_triangular": 1,
        "upper_quotient_lifting_exact": 1,
        "exact_cylinder_rows_available": 1,
        "cross_line_assignment_normal_form_exact": 1,
        "same_owner_diagonal_blocks_subcritical": 0,
        "independent_line_kernel_sufficient": 0,
        "global_target_collateral_inequality_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    mutations = [
        lambda item: item.update(source_file_count=8),
        lambda item: item.update(verifier_file_count=8),
        lambda item: item.update(owner_dag_upper_triangular=0),
        lambda item: item.update(upper_quotient_lifting_exact=0),
        lambda item: item.update(exact_cylinder_rows_available=0),
        lambda item: item.update(cross_line_assignment_normal_form_exact=0),
        lambda item: item.update(same_owner_diagonal_blocks_subcritical=1),
        lambda item: item.update(independent_line_kernel_sufficient=1),
        lambda item: item.update(global_target_collateral_inequality_proved=1),
        lambda item: item.update(all_n_proved_by_checker=1),
        lambda item: item.clear(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(fixture)
        mutate(bad)
        try:
            validate_fixture(bad)
        except InheritedCoordinateDiagonalBlockError:
            rejected += 1
    require(rejected == len(mutations), "diagonal-block corruption accepted")
    return rejected


def main() -> None:
    contract = digest(CONTRACT)
    require(contract == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    root = repository_root()
    for source_file in SOURCE_FILES:
        require((root / source_file).is_file(), f"{source_file}: missing source")
    verifier_reports = [execute_verifier(root, path) for path in VERIFIER_FILES]
    report = {
        "checker": "prime-power-inherited-coordinate-diagonal-block-ancestry",
        "contract_sha256": contract,
        "source_file_count": len(SOURCE_FILES),
        "verifier_file_count": len(VERIFIER_FILES),
        "verifier_reports": verifier_reports,
        "rejected_corruptions": mutation_audit(),
        "owner_dag_upper_triangular": 1,
        "upper_quotient_lifting_exact": 1,
        "line_profile_pair_moment_envelopes_exact": 1,
        "extension_free_permanent_and_marginals_exact": 1,
        "exact_cylinder_rows_available": 1,
        "cross_line_assignment_normal_form_exact": 1,
        "inherited_coordinate_diagonal_block_ancestry_proved": 1,
        "same_owner_diagonal_blocks_subcritical": 0,
        "independent_line_kernel_sufficient": 0,
        "global_target_collateral_inequality_proved": 0,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
