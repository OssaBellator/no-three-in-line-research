#!/usr/bin/env python3
"""Audit theorem IDs, dependency order, move tags, and effective constants."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "proofs/product-entry-invariant-dependencies.json"
INDEXES = [
    ROOT / "proofs/product-growing-direction-theorem-index-PX397-PX450.md",
    ROOT / "proofs/product-growing-direction-theorem-index-PX451-PX478.md",
    ROOT / "proofs/product-growing-direction-theorem-index-PX479-PX482.md",
    ROOT / "proofs/product-growing-direction-theorem-index-PX483-PX487.md",
]
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
)]
HEADING = re.compile(r"^### (?:Theorem|Corollary) PX(\d+)\b", re.MULTILINE)
INDEX_ROW = re.compile(r"^\| PX(\d+) \|", re.MULTILINE)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["range"] == "PX397-PX487"
    assert manifest["root"] == "PX487"
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
    for theorem_id in range(397, 488):
        assert len(occurrences.get(theorem_id, [])) == 1

    index_ids = []
    for path in INDEXES:
        index_ids.extend(int(value) for value in INDEX_ROW.findall(
            path.read_text(encoding="utf-8")
        ))
    assert index_ids == list(range(397, 488))

    text = "\n".join(full_text)
    for phrase in manifest["safety_rules"]["forbidden_unlifted_move_phrases"]:
        assert phrase not in text

    required = manifest["safety_rules"]["required_constants"]
    assert str(required["paired_support_four_denominator"]) in text
    assert "A_3=320" in text
    assert "10^{72}" in text
    assert "N^{1/7}" in text
    assert "10^{2950}" in text
    assert "N_2=10^{2950}" in text
    assert "1900" in text
    print("PX397--PX487 dependency and optimized-cutoff audit: PASS")


if __name__ == "__main__":
    main()
