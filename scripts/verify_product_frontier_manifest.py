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


def as_int(mapping: dict[str, Any], key: str) -> int:
    value = mapping[key]
    require(isinstance(value, int) and not isinstance(value, bool), f"{key} must be an integer")
    return value


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    require(manifest["schema_version"] == 1, "unsupported frontier manifest schema")
    require(manifest["branch"] == "research/all-n-product-construction", "unexpected branch")
    require(manifest["certified_through"] == "PX1186", "unexpected certified theorem boundary")

    side7 = manifest["side_seven"]
    total = as_int(side7, "support_twenty_total_selectors")
    infeasible = as_int(side7, "certified_infeasible_selectors")
    constructive = as_int(side7, "constructive_selectors")
    unclassified = as_int(side7, "unclassified_selectors")
    require(infeasible + constructive + unclassified == total, "side-seven selector partition mismatch")

    classified_cases = side7["multiplicity_two_classified_cases"]
    require(classified_cases == [0, 1389], "unexpected multiplicity-two classified interval")
    classified_case_count = classified_cases[1] - classified_cases[0] + 1
    classified_selectors = as_int(side7, "multiplicity_two_classified_selectors")
    require(classified_selectors == 2 * classified_case_count, "multiplicity-two selector count mismatch")
    require(
        as_int(side7, "multiplicity_two_infeasible_selectors")
        + as_int(side7, "multiplicity_two_constructive_selectors")
        == classified_selectors,
        "multiplicity-two certified partition mismatch",
    )
    require(
        as_int(side7, "multiplicity_two_unresolved_selectors")
        == 2 * as_int(side7, "multiplicity_two_unresolved_signatures"),
        "multiplicity-two unresolved selector count mismatch",
    )
    require(
        unclassified
        == as_int(side7, "multiplicity_two_unresolved_selectors")
        + as_int(side7, "multiplicity_one_unresolved_selectors"),
        "side-seven unresolved decomposition mismatch",
    )
    require(side7["multiplicity_two_next_case"] == 1390, "unexpected next multiplicity-two case")
    require(side7["registered_uncounted_cases"] == [1390, 1399], "unexpected registered side-seven range")

    semantic = manifest["semantic_compression"]
    require(
        as_int(semantic, "covered_top_orders") + as_int(semantic, "uncovered_top_orders")
        == as_int(semantic, "clean_top_orders"),
        "semantic union partition mismatch",
    )
    require(semantic["basis_digest"] == "12529763722981785837", "semantic basis digest mismatch")

    template = manifest["constructive_template"]
    require(
        (template["case"], template["selector"], template["orientation"])
        == (1287, 0, 0),
        "constructive template address mismatch",
    )
    require(template["status"] == "verified_constructive", "constructive template status mismatch")

    side10 = manifest["side_ten"]
    classified_indices = side10["fine_pair_classified_indices"]
    require(classified_indices == [0, 4799], "unexpected side-ten classified interval")
    geometry_count = classified_indices[1] - classified_indices[0] + 1
    require(as_int(side10, "fc_geometries") == geometry_count, "fc geometry count mismatch")
    require(as_int(side10, "ff_geometries") == geometry_count, "ff geometry count mismatch")
    require(side10["registered_uncounted_indices"] == [4800, 5199], "unexpected registered side-ten range")
    require(side10["constructive_witnesses"] == 0, "side-ten witness count must remain zero")

    frontier_ids = manifest["frontier_ids"]
    require(len(frontier_ids) == 8 and len(set(frontier_ids)) == 8, "frontier id registry mismatch")

    require_markers(
        "docs/363-side-seven-multiplicity-two-cases-1380-through-1389.md",
        [
            "`40,379` certified-infeasible selectors",
            "`31,479` unclassified selectors",
            "`3,278,927,685` certified rejection-CSP nodes",
            "next canonical multiplicity-two case is `1390`",
        ],
    )
    require_markers(
        "docs/364-side-ten-opposite-pair-fine-row-twelfth-prefix.md",
        [
            "pair indices `0` through `4799`",
            "`171,920,043` nodes",
            "`100,441,668` nodes",
            "next bounded prefix begins at pair index `4800`",
        ],
    )
    require_markers(
        "STATUS.md",
        [
            "Cases `1390--1399` are registered",
            "Indices `4800--5199` are registered but uncounted",
            "`34,908` clean top orders",
        ],
    )
    require_markers(
        "tracks/all-n-product-current-frontiers.md",
        [
            "through PX1186",
            "Cases `1390--1399` are registered",
            "Pair indices `4800--5199` are registered but uncounted",
            "`12529763722981785837`",
        ],
    )
    require_markers(
        "AUTOPROMPTER_HANDOFF.md",
        [
            "The next canonical multiplicity-two case is `1390`",
            "next bounded prefix begins at pair index `4800`",
            "Advance all of these",
        ],
    )
    require_markers(
        ".github/workflows/product-side-seven-frontier.yml",
        [
            "case: [1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399]",
            "run-side-seven-multiplicity-two-1390-1399",
            "Registered but uncounted",
        ],
    )
    require_markers(
        ".github/workflows/product-side-ten-opposite-fine-4800-5199.yml",
        [
            "orientation: [fc, ff]",
            "first_pair: [4800, 4900, 5000, 5100]",
            "run-opposite-fine-4800-5199",
            "Registered but uncounted",
        ],
    )

    print(
        "PX1186 frontier manifest: "
        "side7=40379+2+31479 "
        "side7_registered=1390--1399 "
        "side10_certified=0--4799 "
        "side10_registered=4800--5199 "
        "frontiers=8 PASS"
    )


if __name__ == "__main__":
    main()
