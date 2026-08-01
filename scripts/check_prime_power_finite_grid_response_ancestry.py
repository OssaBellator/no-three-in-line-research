#!/usr/bin/env python3
"""Execute the finite full-grid and extension-free ancestry for CMR1278--CMR1317."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


class FiniteGridResponseError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise FiniteGridResponseError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


SOURCE_FILES = [
    "docs/264-prime-power-side-three-strict-target-improvement.md",
    "docs/265-prime-power-side-four-finite-improvement.md",
    "docs/266-prime-power-side-five-finite-improvement.md",
    "docs/267-prime-power-extension-free-target-response-family.md",
    "docs/268-prime-power-side-six-target-response-traps.md",
]
VERIFIER_FILES = [
    "scripts/verify_prime_power_side_three_strict_improvement.py",
    "scripts/verify_prime_power_side_four_finite_improvement.py",
    "scripts/verify_prime_power_side_five_finite_improvement.py",
    "scripts/verify_prime_power_extension_free_response.py",
    "scripts/verify_prime_power_side_six_target_response_traps.py",
]
CONTRACT = {
    "schema": "prime-power-finite-grid-response-ancestry/v1",
    "source_range": ["CMR1278", "CMR1317"],
    "source_files": SOURCE_FILES,
    "verifier_files": VERIFIER_FILES,
    "coordinate_scope": "full standard grids and verified translate/common-scale affine copies only",
    "checked_banks": [
        "side-three six-state classification and zero-offspring target response",
        "side-four 216-state strict-improvement policy",
        "side-five 5280-state strict-improvement policy",
        "extension-free response-union identity through side six",
        "side-six immediate traps, equal-response graph and clean joint escape",
    ],
    "honesty_flags": {
        "scattered_residual_finite_grid_policy_proved": 0,
        "one_layer_fixed_target_policy_globally_sufficient": 0,
        "global_target_collateral_inequality_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "caa854d1cac17e5d4680558a9829b01a5d19b86a811e2baae47170d4839f3114"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise FiniteGridResponseError("unable to locate repository root")


def load_module(root: Path, relative_path: str, name: str) -> Any:
    path = root / relative_path
    require(path.is_file(), f"{relative_path}: missing verifier")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{relative_path}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_side_three(module: Any) -> dict[str, int]:
    physical = module.check_six_physical_states()
    labelled = module.check_all_labelled_target_responses()
    zero_entries = module.check_zero_offspring_matrix()
    wall_splits = module.check_wall_child_arithmetic()
    require(len(physical) == 6, "side-three physical state count")
    require(labelled == (12, 8, 24), "side-three labelled response census")
    require(zero_entries == 16, "side-three zero offspring block")
    return {
        "side_three_physical_states": len(physical),
        "side_three_labelled_states": labelled[0],
        "side_three_dirty_states": labelled[1],
        "side_three_clean_target_responses": labelled[2],
        "side_three_zero_offspring_entries": zero_entries,
        "side_three_wall_splits": wall_splits,
    }


def check_side_four(module: Any) -> dict[str, Any]:
    permutations_list, ordered, physical = module.check_state_stock()
    improvements = module.check_all_dirty_improvements(permutations_list, ordered)
    lowering = module.check_lowering_expansion_arithmetic()
    contractions = module.check_contraction_budget()
    require(len(ordered) == 216 and len(physical) == 90, "side-four state census")
    require(improvements[0] == 176 and improvements[1] == 10368, "side-four improvement census")
    require(all(change < 0 for change in improvements[3]), "side-four strict changes")
    return {
        "side_four_ordered_states": len(ordered),
        "side_four_physical_states": len(physical),
        "side_four_dirty_states": improvements[0],
        "side_four_response_instances": improvements[1],
        "side_four_extension_instances": improvements[2],
        "side_four_best_change_distribution": dict(sorted(improvements[3].items())),
        "side_four_lowering_expansion_checks": lowering,
        "side_four_contraction_budget_checks": contractions,
    }


def check_side_five(module: Any) -> dict[str, Any]:
    ordered, physical_potential = module.check_state_stock()
    tables = module.build_response_tables(ordered, physical_potential)
    dirty = module.check_every_dirty_state(ordered, physical_potential, tables[2], tables[3])
    lowering = module.check_restricted_expansion_arithmetic()
    contractions = module.check_contraction_budget()
    require(len(ordered) == 5280 and len(physical_potential) == 2040, "side-five state census")
    require(len(tables[2]) == 2400, "side-five response table")
    require(dirty[0] == 5216 and all(change < 0 for change in dirty[1]), "side-five strict policy")
    return {
        "side_five_ordered_states": len(ordered),
        "side_five_physical_states": len(physical_potential),
        "side_five_bank_size_distribution": dict(sorted(tables[4].items())),
        "side_five_target_response_entries": len(tables[2]),
        "side_five_dirty_states": dirty[0],
        "side_five_best_change_distribution": dict(sorted(dirty[1].items())),
        "side_five_lowering_expansion_checks": lowering,
        "side_five_contraction_budget_checks": contractions,
    }


def check_extension_free(module: Any) -> dict[str, int]:
    union = module.check_union_identity()
    minimum = module.check_minimum_equivalence()
    factorization = module.check_regular_edge_factorization()
    scope = module.check_scope_separation()
    require(union[0] > 0 and union[1] > 0 and union[2] > 0, "extension-free union census")
    return {
        "extension_free_union_identities": union[0],
        "extension_free_response_states": union[1],
        "canonical_forbidden_extensions": union[2],
        "extension_free_minimum_equivalences": minimum,
        "regular_edge_factorization_checks": factorization,
        "fixed_bank_scope_checks": scope,
    }


def check_side_six(module: Any) -> dict[str, Any]:
    disjoint, ordered, information = module.build_data()
    minimum = module.build_minimum_table(disjoint, information)
    result = module.classify_traps(disjoint, ordered, information, minimum)
    module.verify_clean_construction()
    immediate_improvements = sum(
        change is not None and change < 0 for change in result[0].values()
    )
    distance_histogram: dict[int, int] = {}
    for distance in result[2].values():
        distance_histogram[distance] = distance_histogram.get(distance, 0) + 1
    require(len(ordered) == 190800 and len(information) == 67950, "side-six state census")
    require(len(minimum) == 21600, "side-six target response table")
    require(immediate_improvements == 189476, "side-six immediate improvement census")
    require(len(result[1]) == 1208, "side-six immediate trap census")
    require(distance_histogram == {1: 1120, 2: 64}, "side-six equal-response distances")
    require(len(result[3]) == 24 and len(result[4]) == 6, "side-six closed trap core")
    return {
        "side_six_ordered_states": len(ordered),
        "side_six_physical_states": len(information),
        "side_six_target_response_entries": len(minimum),
        "side_six_immediate_improvements": immediate_improvements,
        "side_six_immediate_traps": len(result[1]),
        "side_six_equal_response_distances": distance_histogram,
        "side_six_closed_ordered_traps": len(result[3]),
        "side_six_two_cycles": len(result[4]),
        "side_six_feeder_states": len(result[3]) - 2 * len(result[4]),
        "side_six_clean_joint_escape_verified": 1,
    }


def validate_fixture(fixture: dict[str, Any]) -> None:
    require(fixture.get("side_three_clean_responses") == 24, "fixture side three")
    require(fixture.get("side_four_dirty_states") == 176, "fixture side four")
    require(fixture.get("side_five_dirty_states") == 5216, "fixture side five")
    require(fixture.get("side_six_closed_traps") == 24, "fixture side six")
    require(fixture.get("one_layer_fixed_target_policy_globally_sufficient") == 0, "fixture one-layer honesty")
    require(fixture.get("scattered_residual_finite_grid_policy_proved") == 0, "fixture coordinate honesty")
    require(fixture.get("all_n_proved_by_checker") == 0, "fixture all-n honesty")


def mutation_audit() -> int:
    fixture = {
        "side_three_clean_responses": 24,
        "side_four_dirty_states": 176,
        "side_five_dirty_states": 5216,
        "side_six_closed_traps": 24,
        "one_layer_fixed_target_policy_globally_sufficient": 0,
        "scattered_residual_finite_grid_policy_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    mutations = [
        lambda item: item.update(side_three_clean_responses=23),
        lambda item: item.update(side_four_dirty_states=175),
        lambda item: item.update(side_five_dirty_states=5215),
        lambda item: item.update(side_six_closed_traps=12),
        lambda item: item.update(one_layer_fixed_target_policy_globally_sufficient=1),
        lambda item: item.update(scattered_residual_finite_grid_policy_proved=1),
        lambda item: item.update(all_n_proved_by_checker=1),
        lambda item: item.pop("side_six_closed_traps"),
        lambda item: item.clear(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(fixture)
        mutate(bad)
        try:
            validate_fixture(bad)
        except FiniteGridResponseError:
            rejected += 1
    require(rejected == len(mutations), "finite-grid corruption accepted")
    return rejected


def main() -> None:
    contract = digest(CONTRACT)
    require(contract == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    root = repository_root()
    side_three = load_module(root, VERIFIER_FILES[0], "finite_side_three")
    side_four = load_module(root, VERIFIER_FILES[1], "finite_side_four")
    side_five = load_module(root, VERIFIER_FILES[2], "finite_side_five")
    extension_free = load_module(root, VERIFIER_FILES[3], "extension_free_response")
    side_six = load_module(root, VERIFIER_FILES[4], "finite_side_six")
    report = {
        "checker": "prime-power-finite-grid-response-ancestry",
        "contract_sha256": contract,
        **check_side_three(side_three),
        **check_side_four(side_four),
        **check_side_five(side_five),
        **check_extension_free(extension_free),
        **check_side_six(side_six),
        "rejected_corruptions": mutation_audit(),
        "side_three_full_grid_strict_improvement_exact": 1,
        "side_four_full_grid_finite_improvement_exact": 1,
        "side_five_full_grid_finite_improvement_exact": 1,
        "extension_free_target_response_family_exact": 1,
        "side_six_target_response_traps_exact": 1,
        "finite_grid_response_ancestry_proved": 1,
        "scattered_residual_finite_grid_policy_proved": 0,
        "one_layer_fixed_target_policy_globally_sufficient": 0,
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
