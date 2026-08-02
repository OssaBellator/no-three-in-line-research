#!/usr/bin/env python3
"""Verify the certified and registered all-n frontier boundary."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tracks" / "all-n-product-frontier-manifest.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


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
    require(manifest["schema_version"] == 1, "unsupported schema")
    require(manifest["branch"] == "research/all-n-product-construction", "unexpected branch")
    require(manifest["certified_through"] == "PX1224", "unexpected theorem boundary")

    side7 = manifest["side_seven"]
    require(side7["support_twenty_total_selectors"] == 71_860, "side-seven total mismatch")
    require((side7["certified_infeasible_selectors"], side7["constructive_selectors"], side7["unclassified_selectors"]) == (40_479, 2, 31_379), "side-seven partition mismatch")
    require(40_479 + 2 + 31_379 == 71_860, "side-seven partition arithmetic mismatch")
    require(side7["certified_rejection_nodes"] == 3_297_611_555, "side-seven node mismatch")
    require(side7["multiplicity_two_classified_cases"] == [0, 1439], "classified case interval mismatch")
    require(side7["multiplicity_two_classified_selectors"] == 2_880, "classified selector mismatch")
    require(side7["multiplicity_two_infeasible_selectors"] == 2_879, "classified infeasible mismatch")
    require(side7["multiplicity_two_constructive_selectors"] == 1, "classified constructive mismatch")
    require(side7["multiplicity_two_unresolved_signatures"] == 2_400, "unresolved signature mismatch")
    require(side7["multiplicity_two_unresolved_selectors"] == 4_800, "unresolved m2 selector mismatch")
    require(side7["multiplicity_one_unresolved_selectors"] == 26_579, "unresolved m1 selector mismatch")
    require(4_800 + 26_579 == 31_379, "unresolved decomposition mismatch")
    require(side7["multiplicity_two_next_case"] == 1440, "unexpected next side-seven case")
    require(side7["registered_uncounted_cases"] == [1440, 1449], "registered side-seven range mismatch")

    semantic = manifest["semantic_compression"]
    require((semantic["reference_count"], semantic["relaxed_key_count"], semantic["covered_top_orders"], semantic["uncovered_top_orders"]) == (208, 165, 221, 34_891), "semantic boundary mismatch")
    require(semantic["basis_digest"] == "12529763722981785837", "basis digest mismatch")
    require(semantic["expansion_digest"] == "16150749401146711547", "expansion digest mismatch")

    side10 = manifest["side_ten"]
    require(side10["fine_pair_classified_indices"] == [0, 6799], "side-ten interval mismatch")
    require((side10["fc_geometries"], side10["ff_geometries"]) == (6_800, 6_800), "side-ten geometry mismatch")
    require((side10["fc_nodes"], side10["ff_nodes"]) == (232_466_543, 150_194_835), "side-ten node mismatch")
    require((side10["fc_maximum_nodes"], side10["ff_maximum_nodes"]) == (1_877_339, 909_040), "side-ten maximum mismatch")
    require(side10["constructive_witnesses"] == 0, "side-ten witness mismatch")
    require(side10["registered_uncounted_indices"] == [6800, 7199], "registered side-ten range mismatch")

    require(len(manifest["frontier_ids"]) == len(set(manifest["frontier_ids"])) == 8, "frontier registry mismatch")

    markers("docs/374-side-seven-multiplicity-two-cases-1430-through-1439.md", ["`40,479` certified-infeasible selectors", "`31,379` unclassified selectors", "`3,297,611,555` certified rejection-CSP nodes", "next canonical multiplicity-two case is `1440`", "`531,156,311` certified rejection-CSP nodes"])
    markers("docs/375-side-ten-opposite-pair-fine-row-seventeenth-prefix.md", ["pair indices `0` through `6799`", "`232,466,543` nodes", "`150,194,835` nodes", "next bounded prefix begins at pair index `6800`"])
    markers("STATUS.md", ["Cases `1440--1449` are registered but uncounted", "Indices `6800--7199` are registered but uncounted"])
    markers("tracks/all-n-product-current-frontiers.md", ["through PX1224", "Cases `1440--1449` are registered", "Pair indices `6800--7199` are registered"])
    markers("AUTOPROMPTER_HANDOFF.md", ["Certified theorem boundary: `PX1224`", "next canonical multiplicity-two case is `1440`", "next bounded prefix begins at pair index `6800`"])
    markers(".github/workflows/product-side-seven-frontier.yml", ["case: [1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449]", "run-side-seven-multiplicity-two-1440-1449", "Registered but uncounted"])
    markers(".github/workflows/product-side-ten-opposite-fine-6800-7199.yml", ["first_pair: [6800, 6900, 7000, 7100]", "run-opposite-fine-6800-7199", "Registered but uncounted"])
    markers(".github/workflows/product-promoted-frontier-replay.yml", ["verify_product_side_seven_multiplicity2_cases1430_1439.py", "verify_product_transposition_double_coset_opposite_fine_ten_6400_6799.py", "verify_product_side_seven_multiplicity2_case0_orientation3_semantic_uncovered16.py", "cancel-in-progress: true"])
    markers(".github/product-side-seven-multiplicity-two-1440-1449-trigger.txt", ["run-side-seven-multiplicity-two-1440-1449"])
    markers(".github/product-side-ten-opposite-fine-6800-7199-trigger.txt", ["run-opposite-fine-6800-7199"])

    missing(".github/product-side-seven-multiplicity-two-1430-1439-trigger.txt")
    missing(".github/product-side-ten-opposite-fine-6400-6799-trigger.txt")
    missing(".github/workflows/product-side-ten-opposite-fine-6400-6799.yml")

    print(
        "PX1224 frontier manifest: "
        "side7=40479+2+31379 side7_registered=1440--1449 "
        "semantic=208refs,165keys,221covered,34891uncovered "
        "side10_certified=0--6799 side10_registered=6800--7199 "
        "frontiers=8 PASS"
    )


if __name__ == "__main__":
    main()
