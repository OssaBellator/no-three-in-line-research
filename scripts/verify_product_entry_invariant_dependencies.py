#!/usr/bin/env python3
"""Audit theorem IDs, dependency order, move tags, and active frontier constants."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "proofs/product-entry-invariant-dependencies.json"
INDEXES = [ROOT / "proofs" / name for name in (
    "product-growing-direction-theorem-index-PX397-PX450.md",
    "product-growing-direction-theorem-index-PX451-PX478.md",
    "product-growing-direction-theorem-index-PX479-PX482.md",
    "product-growing-direction-theorem-index-PX483-PX487.md",
    "product-growing-direction-theorem-index-PX488-PX492.md",
    "product-growing-direction-theorem-index-PX493-PX498.md",
    "product-growing-direction-theorem-index-PX499-PX503.md",
    "product-growing-direction-theorem-index-PX504-PX507.md",
    "product-growing-direction-theorem-index-PX508-PX511.md",
    "product-growing-direction-theorem-index-PX512-PX514.md",
    "product-growing-direction-theorem-index-PX515-PX518.md",
    "product-growing-direction-theorem-index-PX519-PX522.md",
    "product-growing-direction-theorem-index-PX523-PX528.md",
    "product-growing-direction-theorem-index-PX529-PX532.md",
)]
DOCS = [ROOT / "docs" / name for name in (
    "153-px63-one-hit-derangement-entry.md",
    "154-px64-line-cap-return-depth.md",
    "155-channel-free-rectangle-label-return.md",
    "156-host-compatible-first-generation-label-banks.md",
    "157-paired-label-product-packet-decoder.md",
    "158-paired-label-mixed-shadow-and-recurrence.md",
    "159-paired-label-large-block-and-asymptotic-loop.md",
    "160-dependency-and-effective-cutoff-audit.md",
    "161-explicit-cartesian-triple-constant.md",
    "162-explicit-nested-depth-envelope.md",
    "163-explicit-divisor-witness-and-effective-exponents.md",
    "164-packet-family-free-active-repair-path.md",
    "165-explicit-common-asymptotic-cutoff.md",
    "166-exact-depth-plateau-cutoff-compression.md",
    "167-fourteenth-power-divisor-cutoff-compression.md",
    "168-rational-divisor-cutoff-compression.md",
    "169-side-seven-relative-class-census.md",
    "170-side-seven-insertion-recursion-barrier.md",
    "171-side-seven-two-column-selector-normal-form.md",
    "172-side-seven-local-minimum-transposition-boxes.md",
    "173-side-seven-selector-coordinate-orbit-csp.md",
    "174-side-seven-cross-half-obstruction-profile.md",
    "175-side-seven-selector-cycle-graph.md",
    "176-side-seven-radius-one-coordinate-csp.md",
    "177-side-seven-radius-two-selector-layer.md",
    "178-side-seven-radius-two-support-eight-ten-csp.md",
    "179-side-seven-radius-two-support-twelve-csp.md",
)]
HEADING = re.compile(r"^### (?:Theorem|Corollary|Lemma) PX(\d+)\b", re.MULTILINE)
INDEX_ROW = re.compile(r"^\| PX(\d+) \|", re.MULTILINE)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["range"] == "PX397-PX532"
    assert manifest["root"] == "PX492"
    assert manifest["frontier_root"] == "PX532"
    nodes = manifest["nodes"]
    starts = {name: int(name[2:].split("-")[0]) for name in nodes}
    for name, data in nodes.items():
        assert (ROOT / data["document"]).is_file()
        assert data["move_space"] in {"rectangle_label", "arithmetic_only"}
        for dependency in data["depends_on"]:
            if dependency in nodes:
                assert starts[dependency] < starts[name]

    occurrences: dict[int, list[str]] = {}
    full_text = []
    for path in DOCS:
        text = path.read_text(encoding="utf-8")
        full_text.append(text)
        for match in HEADING.finditer(text):
            occurrences.setdefault(int(match.group(1)), []).append(path.name)
    for theorem_id in range(397, 533):
        assert len(occurrences.get(theorem_id, [])) == 1

    index_ids = []
    for path in INDEXES:
        index_ids.extend(int(value) for value in INDEX_ROW.findall(
            path.read_text(encoding="utf-8")
        ))
    assert index_ids == list(range(397, 533))

    text = "\n".join(full_text)
    for phrase in manifest["safety_rules"]["forbidden_unlifted_move_phrases"]:
        assert phrase not in text
    for token in (
        "A_3=320", "C_{8/109}<10^{59}", "N_3=10^{2900}",
        "132", "488", "21,952", "170{,}368", "2{,}227{,}923",
        "926,852", "806,548", "9,991,170", "1,748",
        "1,201,997,452", "989,303", "45,477,868",
        "1,594,005,329", "1,326,750,836", "5,461,931,168",
        "9,312",
    ):
        assert token in text
    print("PX397--PX532 dependency, cutoff, and support-twelve frontier audit: PASS")


if __name__ == "__main__":
    main()
