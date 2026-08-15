#!/usr/bin/env python3
"""Compile the exact side-four determinant-realized arithmetic profile stock."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Any


class ArithmeticProfileImportError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticProfileImportError(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def primitive_directions(max_coordinate: int) -> list[tuple[int, int]]:
    return [
        (x, y)
        for x in range(1, max_coordinate + 1)
        for y in range(-max_coordinate, max_coordinate + 1)
        if gcd(x, abs(y)) == 1
    ]


def build_manifest(root: Path) -> dict[str, Any]:
    coverage = load_json(
        root / "data/exact_recurrent_first_host_physical_source_coverage.json"
    )
    crt_rows = [
        row for row in coverage["field_coverage"] if row["field"] == "provenance.crt"
    ]
    require(len(crt_rows) == 1, "CRT field row")
    require(crt_rows[0]["physical_populated"] == 0, "CRT field remains unpopulated")

    side = 4
    max_coordinate = side - 1
    directions = primitive_directions(max_coordinate)
    determinants = [
        first[0] * second[1] - first[1] * second[0]
        for first in directions
        for second in directions
    ]
    nonzero = [value for value in determinants if value]
    magnitudes = sorted({abs(value) for value in nonzero})
    reduced_denominators = sorted(
        {
            Fraction(numerator, denominator).denominator
            for numerator in magnitudes
            for denominator in magnitudes
        }
    )

    require(len(directions) == 15, "direction count")
    require(len(determinants) == 225, "ordered direction pairs")
    require(len(nonzero) == 210, "nonzero determinant pairs")
    require(magnitudes == list(range(1, 14)), "determinant magnitudes")
    require(reduced_denominators == list(range(1, 14)), "reduced denominator set")

    exact_q_max = max(reduced_denominators)
    generic_q_max = 2 * max_coordinate * max_coordinate
    exact_profile_stock = len(directions) ** 2 * sum(range(2, exact_q_max + 1))
    generic_profile_stock = len(directions) ** 2 * sum(range(2, generic_q_max + 1))
    board_anchors = side * side

    return {
        "schema": "exact-recurrent-first-host-side-four-arithmetic-profile-import/v1",
        "scope": {
            "host_id": "s4-75b04c45c1c8eac2",
            "side": side,
            "max_direction_coordinate": max_coordinate,
            "realization_contract": "ratio of determinants of normalized primitive board directions",
        },
        "alternating_core_source": {
            "branch": "research/alternating-core-chain",
            "path": "docs/alternating-core-physical-arithmetic-profile-bound.md",
            "blob_sha": "04047aece5045f81190b36ab6135241e026bc09f",
        },
        "aggregate": {
            "normalized_primitive_directions": len(directions),
            "ordered_direction_pairs": len(determinants),
            "zero_determinant_pairs": len(determinants) - len(nonzero),
            "nonzero_determinant_pairs": len(nonzero),
            "determinant_magnitudes": magnitudes,
            "exact_max_determinant_magnitude": max(magnitudes),
            "generic_safe_denominator_bound": generic_q_max,
            "exact_reduced_denominators": reduced_denominators,
            "exact_nontrivial_denominators": list(range(2, exact_q_max + 1)),
            "exact_max_reduced_denominator": exact_q_max,
            "exact_arithmetic_profile_stock": exact_profile_stock,
            "generic_safe_arithmetic_profile_stock": generic_profile_stock,
            "exact_max_fixed_denominator_profile_stock": exact_q_max * len(directions) ** 2,
            "board_anchor_count": board_anchors,
            "exact_total_non_scalar_address_coefficient": board_anchors * exact_profile_stock,
            "generic_total_non_scalar_address_coefficient": board_anchors * generic_profile_stock,
        },
        "import_gate": {
            "finite_crt_profile_alphabet_under_determinant_realization": 1,
            "exact_side_four_profile_bound_stronger_than_generic_bound": 1,
            "first_host_crt_label_proved_determinant_realized": 0,
            "first_host_crt_label_physically_populated": 0,
            "external_role_dictionary_bound_populated": 0,
            "arithmetic_profile_import_activates_recurrence_closure": 0,
        },
        "conclusion": {
            "conditional_crt_alphabet_size_at_most_20250": 1,
            "conditional_non_scalar_address_stock_at_most_324000_times_L_ext": 1,
            "actual_first_host_crt_profile_identified": 0,
            "promotion_to_physical_signature_allowed": 0,
        },
        "honesty": {
            "physical_occurrence_coverage_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate_manifest(manifest: dict[str, Any]) -> None:
    require(manifest.get("schema") == "exact-recurrent-first-host-side-four-arithmetic-profile-import/v1", "schema")
    aggregate = manifest.get("aggregate", {})
    require(aggregate.get("normalized_primitive_directions") == 15, "directions")
    require(aggregate.get("ordered_direction_pairs") == 225, "ordered pairs")
    require(aggregate.get("zero_determinant_pairs") == 15, "zero determinants")
    require(aggregate.get("nonzero_determinant_pairs") == 210, "nonzero determinants")
    require(aggregate.get("determinant_magnitudes") == list(range(1, 14)), "magnitudes")
    require(aggregate.get("exact_max_determinant_magnitude") == 13, "max determinant")
    require(aggregate.get("generic_safe_denominator_bound") == 18, "generic denominator")
    require(aggregate.get("exact_reduced_denominators") == list(range(1, 14)), "reduced denominators")
    require(aggregate.get("exact_nontrivial_denominators") == list(range(2, 14)), "nontrivial denominators")
    require(aggregate.get("exact_max_reduced_denominator") == 13, "max denominator")
    require(aggregate.get("exact_arithmetic_profile_stock") == 20250, "exact profile stock")
    require(aggregate.get("generic_safe_arithmetic_profile_stock") == 38250, "generic profile stock")
    require(aggregate.get("exact_max_fixed_denominator_profile_stock") == 2925, "fixed denominator stock")
    require(aggregate.get("board_anchor_count") == 16, "anchor count")
    require(aggregate.get("exact_total_non_scalar_address_coefficient") == 324000, "exact address coefficient")
    require(aggregate.get("generic_total_non_scalar_address_coefficient") == 612000, "generic address coefficient")

    source = manifest.get("alternating_core_source", {})
    require(source.get("branch") == "research/alternating-core-chain", "source branch")
    require(source.get("path") == "docs/alternating-core-physical-arithmetic-profile-bound.md", "source path")
    require(source.get("blob_sha") == "04047aece5045f81190b36ab6135241e026bc09f", "source sha")

    gate = manifest.get("import_gate", {})
    require(gate.get("finite_crt_profile_alphabet_under_determinant_realization") == 1, "finite profile alphabet")
    require(gate.get("exact_side_four_profile_bound_stronger_than_generic_bound") == 1, "stronger bound")
    for key in (
        "first_host_crt_label_proved_determinant_realized",
        "first_host_crt_label_physically_populated",
        "external_role_dictionary_bound_populated",
        "arithmetic_profile_import_activates_recurrence_closure",
    ):
        require(gate.get(key) == 0, f"gate {key}")

    conclusion = manifest.get("conclusion", {})
    require(conclusion.get("conditional_crt_alphabet_size_at_most_20250") == 1, "CRT alphabet conclusion")
    require(conclusion.get("conditional_non_scalar_address_stock_at_most_324000_times_L_ext") == 1, "address conclusion")
    require(conclusion.get("actual_first_host_crt_profile_identified") == 0, "actual CRT profile")
    require(conclusion.get("promotion_to_physical_signature_allowed") == 0, "promotion")

    for key, value in manifest.get("honesty", {}).items():
        require(value == 0, f"honesty {key}")


def mutation_audit(manifest: dict[str, Any]) -> int:
    mutations = [
        lambda x: x["aggregate"].update(normalized_primitive_directions=14),
        lambda x: x["aggregate"].update(nonzero_determinant_pairs=209),
        lambda x: x["aggregate"].update(exact_max_determinant_magnitude=18),
        lambda x: x["aggregate"].update(exact_max_reduced_denominator=18),
        lambda x: x["aggregate"].update(exact_arithmetic_profile_stock=38250),
        lambda x: x["aggregate"].update(exact_total_non_scalar_address_coefficient=612000),
        lambda x: x["import_gate"].update(first_host_crt_label_proved_determinant_realized=1),
        lambda x: x["import_gate"].update(first_host_crt_label_physically_populated=1),
        lambda x: x["import_gate"].update(arithmetic_profile_import_activates_recurrence_closure=1),
        lambda x: x["conclusion"].update(promotion_to_physical_signature_allowed=1),
        lambda x: x["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate_manifest(candidate)
        except ArithmeticProfileImportError:
            rejected += 1
    require(rejected == len(mutations), "mutation accepted")
    return rejected


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ArithmeticProfileImportError("unable to locate repository root")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()

    root = repository_root()
    manifest = build_manifest(root)
    validate_manifest(manifest)
    if args.check:
        require(load_json(args.check) == manifest, "manifest mismatch")

    rejected = mutation_audit(manifest)
    aggregate = manifest["aggregate"]
    print(
        "verified exact side-four arithmetic profile import: "
        f"{aggregate['normalized_primitive_directions']} directions, "
        f"maximum reduced denominator {aggregate['exact_max_reduced_denominator']}, "
        f"profile stock {aggregate['exact_arithmetic_profile_stock']} and "
        f"{rejected} rejected corruptions"
    )


if __name__ == "__main__":
    main()
