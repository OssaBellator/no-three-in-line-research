#!/usr/bin/env python3
"""Verify the certified and registered all-n frontier boundary."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tracks" / "all-n-product-frontier-manifest.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def integer(mapping: dict[str, Any], key: str) -> int:
    value = mapping[key]
    require(isinstance(value, int) and not isinstance(value, bool), f"{key} must be an integer")
    return value


def markers(path: str, expected: list[str]) -> None:
    target = ROOT / path
    require(target.is_file(), f"missing tracked file: {path}")
    text = target.read_text(encoding="utf-8")
    for marker in expected:
        require(marker in text, f"{path}: missing marker {marker!r}")


def missing(path: str) -> None:
    require(not (ROOT / path).exists(), f"superseded file remains tracked: {path}")


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(manifest["schema_version"] == 1, "unsupported manifest schema")
    require(manifest["branch"] == "research/all-n-product-construction", "unexpected branch")
    require(manifest["certified_through"] == "PX1217", "unexpected certified theorem boundary")

    side7 = manifest["side_seven"]
    total = integer(side7, "support_twenty_total_selectors")
    infeasible = integer(side7, "certified_infeasible_selectors")
    constructive = integer(side7, "constructive_selectors")
    unclassified = integer(side7, "unclassified_selectors")
    require((total, infeasible, constructive, unclassified) == (71_860, 40_459, 2, 31_399), "side-seven totals mismatch")
    require(infeasible + constructive + unclassified == total, "side-seven partition mismatch")
    require(integer(side7, "certified_rejection_nodes") == 3_295_710_592, "side-seven node boundary mismatch")
    require(side7["multiplicity_two_classified_cases"] == [0, 1429], "classified side-seven interval mismatch")
    require(integer(side7, "multiplicity_two_classified_selectors") == 2_860, "classified selector count mismatch")
    require(integer(side7, "multiplicity_two_infeasible_selectors") == 2_859, "classified infeasible count mismatch")
    require(integer(side7, "multiplicity_two_constructive_selectors") == 1, "classified constructive count mismatch")
    require(integer(side7, "multiplicity_two_unresolved_signatures") == 2_410, "unresolved signature count mismatch")
    require(integer(side7, "multiplicity_two_unresolved_selectors") == 4_820, "unresolved multiplicity-two selector mismatch")
    require(integer(side7, "multiplicity_one_unresolved_selectors") == 26_579, "unresolved multiplicity-one selector mismatch")
    require(4_820 + 26_579 == unclassified, "unresolved decomposition mismatch")
    require(side7["multiplicity_two_next_case"] == 1430, "unexpected next side-seven case")
    require(side7["registered_uncounted_cases"] == [1430, 1439], "unexpected registered side-seven range")

    semantic = manifest["semantic_compression"]
    require(integer(semantic, "reference_count") == 208, "semantic reference count mismatch")
    require(integer(semantic, "relaxed_key_count") == 165, "semantic key count mismatch")
    require(integer(semantic, "covered_top_orders") == 221, "semantic coverage mismatch")
    require(integer(semantic, "uncovered_top_orders") == 34_891, "semantic complement mismatch")
    require(integer(semantic, "covered_top_orders") + integer(semantic, "uncovered_top_orders") == integer(semantic, "clean_top_orders"), "semantic partition mismatch")
    require(semantic["basis_digest"] == "12529763722981785837", "semantic basis digest mismatch")
    require(semantic["expansion_digest"] == "16150749401146711547", "semantic expansion digest mismatch")

    side10 = manifest["side_ten"]
    require(side10["fine_pair_classified_indices"] == [0, 6399], "side-ten classified interval mismatch")
    require(integer(side10, "fc_geometries") == 6_400, "fc geometry count mismatch")
    require(integer(side10, "ff_geometries") == 6_400, "ff geometry count mismatch")
    require(integer(side10, "fc_nodes") == 224_654_411, "fc node count mismatch")
    require(integer(side10, "ff_nodes") == 135_595_069, "ff node count mismatch")
    require(integer(side10, "fc_maximum_nodes") == 1_877_339, "fc maximum mismatch")
    require(integer(side10, "ff_maximum_nodes") == 909_040, "ff maximum mismatch")
    require(integer(side10, "constructive_witnesses") == 0, "side-ten witness count mismatch")
    require(side10["registered_uncounted_indices"] == [6400, 6799], "unexpected registered side-ten range")

    require(len(manifest["frontier_ids"]) == len(set(manifest["frontier_ids"])) == 8, "frontier registry mismatch")

    markers("docs/372-side-seven-multiplicity-two-cases-1420-through-1429.md", [
        "`40,459` certified-infeasible selectors",
        "`31,399` unclassified selectors",
        "`3,295,710,592` certified rejection-CSP nodes",
        "next canonical multiplicity-two case is `1430`",
        "`529,255,348` certified rejection-CSP nodes",
    ])
    markers("docs/373-side-ten-opposite-pair-fine-row-sixteenth-prefix.md", [
        "pair indices `0` through `6399`",
        "`224,654,411` nodes",
        "`135,595,069` nodes",
        "next bounded prefix begins at pair index `6400`",
    ])
    markers("STATUS.md", ["Cases `1430--1439` are registered", "Indices `6400--6799` are registered but uncounted"])
    markers("tracks/all-n-product-current-frontiers.md", ["through PX1217", "Cases `1430--1439` are registered", "Pair indices `6400--6799` are registered but uncounted"])
    markers("AUTOPROMPTER_HANDOFF.md", ["Certified theorem boundary: `PX1217`", "next canonical multiplicity-two case is `1430`", "next bounded prefix begins at pair index `6400`"]) 
    markers(".github/workflows/product-side-seven-frontier.yml", ["case: [1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439]", "run-side-seven-multiplicity-two-1430-1439", "Registered but uncounted"])
    markers(".github/workflows/product-side-ten-opposite-fine-6400-6799.yml", ["first_pair: [6400, 6500, 6600, 6700]", "run-opposite-fine-6400-6799", "Registered but uncounted"])
    markers(".github/workflows/product-promoted-frontier-replay.yml", [
        "verify_product_side_seven_multiplicity2_cases1420_1429.py",
        "verify_product_transposition_double_coset_opposite_fine_ten_6000_6399.py",
        "verify_product_side_seven_multiplicity2_case0_orientation3_semantic_uncovered16.py",
        "cancel-in-progress: true",
    ])
    markers(".github/product-side-seven-multiplicity-two-1430-1439-trigger.txt", ["run-side-seven-multiplicity-two-1430-1439"])
    markers(".github/product-side-ten-opposite-fine-6400-6799-trigger.txt", ["run-opposite-fine-6400-6799"])

    missing(".github/product-side-seven-multiplicity-two-1420-1429-trigger.txt")
    missing(".github/product-side-ten-opposite-fine-6000-6399-trigger.txt")
    missing(".github/workflows/product-side-ten-opposite-fine-6000-6399.yml")

    print(
        "PX1217 frontier manifest: "
        "side7=40459+2+31399 side7_registered=1430--1439 "
        "semantic=208refs,165keys,221covered,34891uncovered "
        "side10_certified=0--6399 side10_registered=6400--6799 "
        "frontiers=8 PASS"
    )


if __name__ == "__main__":
    main()
