#!/usr/bin/env python3
"""Verify the certified/registered all-n frontier manifest and tracked boundary markers."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "tracks" / "all-n-product-frontier-manifest.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_markers(relative_path: str, markers: list[str]) -> None:
    path = ROOT / relative_path
    require(path.is_file(), f"missing tracked file: {relative_path}")
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        require(marker in text, f"{relative_path}: missing marker {marker!r}")


def require_missing(relative_path: str) -> None:
    require(not (ROOT / relative_path).exists(), f"superseded file remains tracked: {relative_path}")


def as_int(mapping: dict[str, Any], key: str) -> int:
    value = mapping[key]
    require(isinstance(value, int) and not isinstance(value, bool), f"{key} must be an integer")
    return value


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    require(manifest["schema_version"] == 1, "unsupported frontier manifest schema")
    require(manifest["branch"] == "research/all-n-product-construction", "unexpected branch")
    require(manifest["certified_through"] == "PX1196", "unexpected certified theorem boundary")

    side7 = manifest["side_seven"]
    total = as_int(side7, "support_twenty_total_selectors")
    infeasible = as_int(side7, "certified_infeasible_selectors")
    constructive = as_int(side7, "constructive_selectors")
    unclassified = as_int(side7, "unclassified_selectors")
    require((infeasible, constructive, unclassified) == (40_399, 2, 31_459), "side-seven totals mismatch")
    require(infeasible + constructive + unclassified == total, "side-seven selector partition mismatch")
    require(as_int(side7, "certified_rejection_nodes") == 3_285_616_695, "rejection-node boundary mismatch")

    classified_cases = side7["multiplicity_two_classified_cases"]
    require(classified_cases == [0, 1399], "unexpected multiplicity-two classified interval")
    classified_case_count = classified_cases[1] - classified_cases[0] + 1
    classified_selectors = as_int(side7, "multiplicity_two_classified_selectors")
    require(classified_selectors == 2 * classified_case_count == 2_800, "multiplicity-two selector count mismatch")
    require(
        as_int(side7, "multiplicity_two_infeasible_selectors")
        + as_int(side7, "multiplicity_two_constructive_selectors")
        == classified_selectors,
        "multiplicity-two certified partition mismatch",
    )
    require(as_int(side7, "multiplicity_two_infeasible_selectors") == 2_799, "m2 infeasible count mismatch")
    require(as_int(side7, "multiplicity_two_constructive_selectors") == 1, "m2 constructive count mismatch")
    require(
        as_int(side7, "multiplicity_two_unresolved_selectors")
        == 2 * as_int(side7, "multiplicity_two_unresolved_signatures")
        == 4_880,
        "multiplicity-two unresolved selector count mismatch",
    )
    require(
        unclassified
        == as_int(side7, "multiplicity_two_unresolved_selectors")
        + as_int(side7, "multiplicity_one_unresolved_selectors"),
        "side-seven unresolved decomposition mismatch",
    )
    require(side7["multiplicity_two_next_case"] == 1400, "unexpected next multiplicity-two case")
    require(side7["registered_uncounted_cases"] == [1400, 1409], "unexpected registered side-seven range")

    semantic = manifest["semantic_compression"]
    require(as_int(semantic, "baseline_reference_count") == 192, "semantic baseline reference mismatch")
    require(as_int(semantic, "baseline_relaxed_key_count") == 150, "semantic baseline key mismatch")
    require(as_int(semantic, "reference_count") == 208, "semantic reference count mismatch")
    require(as_int(semantic, "relaxed_key_count") == 165, "semantic key count mismatch")
    require(as_int(semantic, "basis_covered_top_orders") == 204, "semantic basis coverage mismatch")
    require(
        as_int(semantic, "covered_top_orders") + as_int(semantic, "uncovered_top_orders")
        == as_int(semantic, "clean_top_orders"),
        "semantic union partition mismatch",
    )
    require(as_int(semantic, "covered_top_orders") == 221, "semantic expanded union mismatch")
    require(as_int(semantic, "uncovered_top_orders") == 34_891, "semantic complement mismatch")
    require(semantic["basis_digest"] == "12529763722981785837", "semantic basis digest mismatch")
    require(semantic["expansion_reference_indices"] == [192, 207], "semantic expansion interval mismatch")
    require(as_int(semantic, "expansion_new_distinct_keys") == 15, "semantic expansion key mismatch")
    require(as_int(semantic, "expansion_extension_sum") == 20, "semantic extension sum mismatch")
    require(as_int(semantic, "expansion_union_growth") == 17, "semantic union growth mismatch")
    require(as_int(semantic, "expansion_bottom_checks") == 201_600, "semantic bottom replay mismatch")
    require(semantic["expansion_digest"] == "16150749401146711547", "semantic expansion digest mismatch")

    template = manifest["constructive_template"]
    require(
        (template["case"], template["selector"], template["orientation"])
        == (1287, 0, 0),
        "constructive template address mismatch",
    )
    require(template["status"] == "verified_constructive", "constructive template status mismatch")

    side10 = manifest["side_ten"]
    classified_indices = side10["fine_pair_classified_indices"]
    require(classified_indices == [0, 5199], "unexpected side-ten classified interval")
    geometry_count = classified_indices[1] - classified_indices[0] + 1
    require(as_int(side10, "fc_geometries") == geometry_count == 5_200, "fc geometry count mismatch")
    require(as_int(side10, "ff_geometries") == geometry_count == 5_200, "ff geometry count mismatch")
    require(as_int(side10, "fc_nodes") == 184_338_885, "fc node count mismatch")
    require(as_int(side10, "ff_nodes") == 112_022_029, "ff node count mismatch")
    require(as_int(side10, "fc_maximum_nodes") == 1_877_339, "fc maximum mismatch")
    require(as_int(side10, "ff_maximum_nodes") == 909_040, "ff maximum mismatch")
    require(side10["registered_uncounted_indices"] == [5200, 5599], "unexpected registered side-ten range")
    require(side10["constructive_witnesses"] == 0, "side-ten witness count must remain zero")

    frontier_ids = manifest["frontier_ids"]
    require(len(frontier_ids) == 8 and len(set(frontier_ids)) == 8, "frontier id registry mismatch")

    require_markers(
        "docs/365-side-seven-multiplicity-two-cases-1390-through-1399.md",
        [
            "`40,399` certified-infeasible selectors",
            "`31,459` unclassified selectors",
            "`3,285,616,695` certified rejection-CSP nodes",
            "next canonical multiplicity-two case is `1400`",
            "`519,161,451` certified rejection-CSP nodes",
        ],
    )
    require_markers(
        "docs/366-side-ten-opposite-pair-fine-row-thirteenth-prefix.md",
        [
            "pair indices `0` through `5199`",
            "`184,338,885` nodes",
            "`112,022,029` nodes",
            "next bounded prefix begins at pair index `5200`",
        ],
    )
    require_markers(
        "docs/367-side-seven-semantic-uncovered-top-expansion-16.md",
        [
            "indices `192` through `207`",
            "vocabulary: `150 -> 165` keys",
            "exact union: `204 -> 221` clean top orders",
            "`34,891` clean top orders",
            "`201,600` exact bottom checks",
            "`16150749401146711547`",
        ],
    )
    require_markers(
        "STATUS.md",
        [
            "Cases `1400--1409` are registered",
            "Indices `5200--5599` are registered but uncounted",
            "`34,891` remain uncovered",
        ],
    )
    require_markers(
        "tracks/all-n-product-current-frontiers.md",
        [
            "through PX1196",
            "Cases `1400--1409` are registered",
            "Pair indices `5200--5599` are registered but uncounted",
            "`16150749401146711547`",
        ],
    )
    require_markers(
        "AUTOPROMPTER_HANDOFF.md",
        [
            "Certified theorem boundary: `PX1196`",
            "The next canonical multiplicity-two case is `1400`",
            "next bounded prefix begins at pair index `5200`",
            "`34,891` clean top orders remain uncovered",
            "Advance all of these",
        ],
    )
    require_markers(
        ".github/workflows/product-side-seven-frontier.yml",
        [
            "case: [1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409]",
            "run-side-seven-multiplicity-two-1400-1409",
            "cancel-in-progress: true",
            "Registered but uncounted",
        ],
    )
    require_markers(
        ".github/workflows/product-side-ten-opposite-fine-5200-5599.yml",
        [
            "orientation: [fc, ff]",
            "first_pair: [5200, 5300, 5400, 5500]",
            "run-opposite-fine-5200-5599",
            "cancel-in-progress: true",
            "Registered but uncounted",
        ],
    )
    require_markers(
        ".github/workflows/product-promoted-frontier-replay.yml",
        [
            "verify_product_side_seven_multiplicity2_cases1390_1399.py",
            "verify_product_transposition_double_coset_opposite_fine_ten_4800_5199.py",
            "verify_product_side_seven_multiplicity2_case0_orientation3_semantic_uncovered16.py",
            "cancel-in-progress: true",
        ],
    )
    require_missing(".github/product-side-seven-multiplicity-two-1390-1399-trigger.txt")
    require_missing(".github/product-side-ten-opposite-fine-4800-5199-trigger.txt")
    require_missing(".github/workflows/product-side-ten-opposite-fine-4800-5199.yml")
    require_missing(".github/workflows/product-side-seven-semantic-uncovered16.yml")

    print(
        "PX1196 frontier manifest: "
        "side7=40399+2+31459 "
        "side7_registered=1400--1409 "
        "semantic=208refs,165keys,221covered,34891uncovered "
        "side10_certified=0--5199 "
        "side10_registered=5200--5599 "
        "frontiers=8 PASS"
    )


if __name__ == "__main__":
    main()
