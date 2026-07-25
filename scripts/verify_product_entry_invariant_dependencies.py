#!/usr/bin/env python3
"""Repository audit for PX397--PX478 dependencies and effective cutoff data."""

from __future__ import annotations

import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "proofs" / "product-entry-invariant-dependencies.json"
INDEX_PATHS = [
    ROOT / "proofs" / "product-growing-direction-theorem-index-PX397-PX450.md",
    ROOT / "proofs" / "product-growing-direction-theorem-index-PX451-PX478.md",
]
DOC_PATHS = [ROOT / "docs" / f"{number}-{name}" for number, name in (
    (153, "px63-one-hit-derangement-entry.md"),
    (154, "px64-line-cap-return-depth.md"),
    (155, "channel-free-rectangle-label-return.md"),
    (156, "host-compatible-first-generation-label-banks.md"),
    (157, "paired-label-product-packet-decoder.md"),
    (158, "paired-label-mixed-shadow-and-recurrence.md"),
    (159, "paired-label-large-block-and-asymptotic-loop.md"),
    (160, "dependency-and-effective-cutoff-audit.md"),
    (161, "explicit-cartesian-triple-constant.md"),
    (162, "explicit-nested-depth-envelope.md"),
    (163, "explicit-divisor-witness-and-effective-exponents.md"),
    (164, "packet-family-free-active-repair-path.md"),
    (165, "explicit-common-asymptotic-cutoff.md"),
)]

HEADING_RE = re.compile(r"^### (?:Theorem|Corollary) PX(\d+)\b", re.MULTILINE)
INDEX_RE = re.compile(r"^\| PX(\d+) \|", re.MULTILINE)
BLOCK_START_RE = re.compile(r"^PX(\d+)")


def check_manifest() -> dict:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    nodes = manifest["nodes"]
    allowed = set(manifest["safety_rules"]["allowed_terminal_move_spaces"])

    assert manifest["range"] == "PX397-PX478"
    assert manifest["root"] == "PX478"

    starts: dict[str, int] = {}
    for node, data in nodes.items():
        match = BLOCK_START_RE.match(node)
        assert match is not None, node
        starts[node] = int(match.group(1))
        assert data["move_space"] in allowed
        assert (ROOT / data["document"]).is_file(), data["document"]

    for node, data in nodes.items():
        for dependency in data["depends_on"]:
            if dependency in nodes:
                assert starts[dependency] < starts[node], (dependency, node)

    return manifest


def check_theorem_ids() -> None:
    occurrences: dict[int, list[str]] = {}
    for path in DOC_PATHS:
        assert path.is_file(), path
        text = path.read_text(encoding="utf-8")
        for match in HEADING_RE.finditer(text):
            theorem_id = int(match.group(1))
            occurrences.setdefault(theorem_id, []).append(path.name)

    for theorem_id in range(397, 479):
        assert len(occurrences.get(theorem_id, [])) == 1, (
            theorem_id,
            occurrences.get(theorem_id, []),
        )

    index_ids: list[int] = []
    for path in INDEX_PATHS:
        assert path.is_file(), path
        index_ids.extend(int(value) for value in INDEX_RE.findall(
            path.read_text(encoding="utf-8")
        ))
    assert index_ids == list(range(397, 479)), index_ids


def check_safety_text(manifest: dict) -> None:
    all_text = "\n".join(path.read_text(encoding="utf-8") for path in DOC_PATHS)
    for phrase in manifest["safety_rules"]["forbidden_unlifted_move_phrases"]:
        assert phrase not in all_text

    constants = manifest["safety_rules"]["required_constants"]
    docs = {
        path.name: path.read_text(encoding="utf-8")
        for path in DOC_PATHS
    }
    doc153 = docs["153-px63-one-hit-derangement-entry.md"]
    doc155 = docs["155-channel-free-rectangle-label-return.md"]
    doc159 = docs["159-paired-label-large-block-and-asymptotic-loop.md"]
    doc161 = docs["161-explicit-cartesian-triple-constant.md"]
    doc163 = docs["163-explicit-divisor-witness-and-effective-exponents.md"]
    doc164 = docs["164-packet-family-free-active-repair-path.md"]
    doc165 = docs["165-explicit-common-asymptotic-cutoff.md"]

    assert str(constants["paired_support_four_denominator"]) in doc159
    assert "8192e^{4\\Delta}" not in doc159
    assert "9/(c)_r" in doc153 or "\\frac9{(c)_r}" in doc153
    assert "D/18" in doc153
    assert "four" in doc155.lower()
    assert (
        "two label families" in doc155.lower()
        or "two column-label families" in doc155.lower()
    )
    assert f"A_3={constants['cartesian_triple_constant']}" in doc161
    assert f"10^{{{constants['divisor_constant_power_of_ten']}}}" in doc163
    divisor_exponent = constants["divisor_exponent_denominator"]
    assert f"N^{{1/{divisor_exponent}}}" in doc163
    assert "active packet-family count to zero" in doc164
    assert f"10^{{{constants['explicit_cutoff_power_of_ten']}}}" in doc165
    assert "\\log(4N^{3/5})" in doc165


def check_cutoff_resolution() -> None:
    audit = (ROOT / "docs" / "160-dependency-and-effective-cutoff-audit.md").read_text(
        encoding="utf-8"
    )
    cutoff = (ROOT / "docs" / "165-explicit-common-asymptotic-cutoff.md").read_text(
        encoding="utf-8"
    )
    assert "PX460" in audit and "PX465" in audit and "PX468" in audit
    assert "PX478" in audit
    assert "N_0=10^{4000}" in cutoff
    assert "finite range" in cutoff.lower()


def main() -> None:
    manifest = check_manifest()
    check_theorem_ids()
    check_safety_text(manifest)
    check_cutoff_resolution()
    print("PX397--PX478 dependency and effective-cutoff audit: PASS")


if __name__ == "__main__":
    main()
