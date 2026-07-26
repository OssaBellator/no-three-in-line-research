#!/usr/bin/env python3
"""Audit theorem IDs, dependency order, move tags, and active frontier constants."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "proofs" / "product-entry-invariant-dependencies.json"
HEADING = re.compile(r"^### (?:Theorem|Corollary|Lemma) PX(\d+)\b", re.MULTILINE)
INDEX_ROW = re.compile(r"^\| PX(\d+) \|", re.MULTILINE)
FIRST = 397
LAST = 616


def node_start(name: str) -> int:
    return int(name[2:].split("-")[0])


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["range"] == f"PX{FIRST}-PX{LAST}"
    assert manifest["root"] == "PX492"
    assert manifest["frontier_root"] == f"PX{LAST}"

    nodes = manifest["nodes"]
    starts = {name: node_start(name) for name in nodes}
    document_paths: list[Path] = []
    for name, data in nodes.items():
        path = ROOT / data["document"]
        assert path.is_file(), path
        document_paths.append(path)
        assert data["move_space"] in {"rectangle_label", "arithmetic_only"}
        for dependency in data["depends_on"]:
            if dependency in nodes:
                assert starts[dependency] < starts[name]

    occurrences: dict[int, list[str]] = {}
    full_text: list[str] = []
    for path in dict.fromkeys(document_paths):
        text = path.read_text(encoding="utf-8")
        full_text.append(text)
        for match in HEADING.finditer(text):
            theorem_id = int(match.group(1))
            if FIRST <= theorem_id <= LAST:
                occurrences.setdefault(theorem_id, []).append(path.name)
    for theorem_id in range(FIRST, LAST + 1):
        assert len(occurrences.get(theorem_id, [])) == 1, (
            theorem_id,
            occurrences.get(theorem_id),
        )

    indexed: dict[int, list[str]] = {}
    for path in sorted((ROOT / "proofs").glob(
        "product-growing-direction-theorem-index-PX*.md"
    )):
        for value in INDEX_ROW.findall(path.read_text(encoding="utf-8")):
            theorem_id = int(value)
            if FIRST <= theorem_id <= LAST:
                indexed.setdefault(theorem_id, []).append(path.name)
    for theorem_id in range(FIRST, LAST + 1):
        assert len(indexed.get(theorem_id, [])) == 1, (
            theorem_id,
            indexed.get(theorem_id),
        )

    text = "\n".join(full_text)
    for phrase in manifest["safety_rules"]["forbidden_unlifted_move_phrases"]:
        assert phrase not in text

    for token in (
        "A_3=320",
        "C_{8/109}<10^{59}",
        "N_3=10^{2900}",
        "9,991,170",
        "1,201,997,452",
        "989,303",
        "21,644,906,190",
        "20,354,897,736",
        "468{,}452",
        "14,581,646,651",
        "71{,}860",
        "1{,}669{,}828",
        "43{,}726",
        "38{,}553",
        "601,405",
        "2{,}303{,}855",
        "1{,}168{,}800",
        "3{,}472{,}655",
        "927{,}673",
        "4{,}400{,}328",
        "1,919,466",
        "1,375,574",
        "7{,}695{,}368",
        "71{,}276",
        "162",
    ):
        assert token in text, token

    constants = manifest["safety_rules"]["required_constants"]
    assert constants["active_cutoff_power_of_ten"] == 2900
    assert constants["side_seven_cycle52_support_twenty_cached_selector_count"] == 584
    assert constants["side_seven_cycle52_support_twenty_cached_bottom_nodes"] == 7_695_368
    assert constants["side_seven_cycle52_radius_three_support_twenty_remaining"] == 71_276
    assert constants["side_seven_cycle52_support_twenty_next_signature_multiplicity"] == 27
    assert constants["side_seven_cycle52_support_twenty_next_selector_count"] == 162

    print(
        "PX397--PX616 dependency, cutoff, and support-twenty multiplicity audit: PASS"
    )


if __name__ == "__main__":
    main()
