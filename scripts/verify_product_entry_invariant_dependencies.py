#!/usr/bin/env python3
"""Repository audit for PX397--PX455 dependencies and effective cutoff data."""

from __future__ import annotations

import json
import math
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "proofs" / "product-entry-invariant-dependencies.json"
INDEX_PATH = ROOT / "proofs" / "product-growing-direction-theorem-index-PX397-PX450.md"
DOC_PATHS = [ROOT / "docs" / f"{number}-{name}" for number, name in (
    (153, "px63-one-hit-derangement-entry.md"),
    (154, "px64-line-cap-return-depth.md"),
    (155, "channel-free-rectangle-label-return.md"),
    (156, "host-compatible-first-generation-label-banks.md"),
    (157, "paired-label-product-packet-decoder.md"),
    (158, "paired-label-mixed-shadow-and-recurrence.md"),
    (159, "paired-label-large-block-and-asymptotic-loop.md"),
    (160, "dependency-and-effective-cutoff-audit.md"),
)]

HEADING_RE = re.compile(r"^### (?:Theorem|Corollary) PX(\d+)\b", re.MULTILINE)
INDEX_RE = re.compile(r"^\| PX(\d+) \|", re.MULTILINE)


def theorem_block(theorem_id: int) -> str | None:
    ranges = ((397, 403), (404, 410), (411, 419), (420, 427),
              (428, 436), (437, 444), (445, 450))
    for start, end in ranges:
        if start <= theorem_id <= end:
            return f"PX{start}-{end}"
    return None


def check_manifest() -> dict:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    nodes = manifest["nodes"]
    allowed = set(manifest["safety_rules"]["allowed_terminal_move_spaces"])

    for node, data in nodes.items():
        assert data["move_space"] in allowed
        assert (ROOT / data["document"]).is_file()

    # Internal continuation dependencies must point strictly backwards.
    starts = {node: int(node.split("-")[0][2:]) for node in nodes}
    for node, data in nodes.items():
        for dependency in data["depends_on"]:
            if dependency in nodes:
                assert starts[dependency] < starts[node]

    assert manifest["root"] == "PX450"
    return manifest


def check_theorem_ids() -> None:
    occurrences: dict[int, list[str]] = {}
    for path in DOC_PATHS:
        assert path.is_file(), path
        text = path.read_text(encoding="utf-8")
        for match in HEADING_RE.finditer(text):
            theorem_id = int(match.group(1))
            occurrences.setdefault(theorem_id, []).append(path.name)

    for theorem_id in range(397, 456):
        assert len(occurrences.get(theorem_id, [])) == 1, (
            theorem_id,
            occurrences.get(theorem_id, []),
        )

    index_text = INDEX_PATH.read_text(encoding="utf-8")
    index_ids = [int(value) for value in INDEX_RE.findall(index_text)]
    assert index_ids == list(range(397, 451))


def check_safety_text(manifest: dict) -> None:
    text = "\n".join(path.read_text(encoding="utf-8") for path in DOC_PATHS)
    for phrase in manifest["safety_rules"]["forbidden_unlifted_move_phrases"]:
        assert phrase not in text

    constants = manifest["safety_rules"]["required_constants"]
    doc159 = (ROOT / "docs" / "159-paired-label-large-block-and-asymptotic-loop.md").read_text(encoding="utf-8")
    doc153 = (ROOT / "docs" / "153-px63-one-hit-derangement-entry.md").read_text(encoding="utf-8")
    doc155 = (ROOT / "docs" / "155-channel-free-rectangle-label-return.md").read_text(encoding="utf-8")

    assert str(constants["paired_support_four_denominator"]) in doc159
    assert "8192e^{4\\Delta}" not in doc159
    assert f"\\frac9{{(c)_r}}" in doc153 or "9/(c)_r" in doc153
    assert "D/18" in doc153
    assert "four" in doc155.lower()
    assert "two label families" in doc155.lower()


def logsumexp(first: float, second: float) -> float:
    high = max(first, second)
    return high + math.log(math.exp(first - high) + math.exp(second - high))


def check_parameterized_cutoff() -> None:
    # Synthetic effective witness.  We use log N directly to avoid constructing
    # an enormous integer; the test checks the finite inequalities in PX453.
    log_n = 1_000_000.0
    epsilon = 0.10
    rho = 0.05
    eta = 0.01
    a3 = 1_000_000.0

    log2_n = log_n / math.log(2.0)
    depth = math.ceil(math.log2(log2_n)) + 10
    delta = 3 + 2 * depth
    log_t = (0.5 + epsilon) * log_n
    log_b = math.log(max(32.0, 16.0 * delta + 4.0, 16.0 * math.exp(2.0 * delta)))
    log_c = math.log(32768.0 / eta) + 4.0 * delta

    log_q_first = math.log(eta / 128.0) - math.log(math.log(2.0) + log_t)
    log_q_second = log_t - log_c - (1.0 + rho) * log_n
    log_q = min(log_q_first, log_q_second)

    # qT >= B.
    assert log_q + log_t >= log_b

    # N-1-2Delta > 0, checked in log form with huge slack.
    assert log_n > math.log(2.0 * delta + 2.0)

    # 4096 A3 e^(2Delta) (q log(2T)+q^2 log(2T)) <= 1/8.
    log_log_2t = math.log(math.log(2.0) + log_t)
    first_term = log_q + log_log_2t
    second_term = 2.0 * log_q + log_log_2t
    log_parenthesis = logsumexp(first_term, second_term)
    log_internal = math.log(4096.0 * a3) + 2.0 * delta + log_parenthesis
    assert log_internal <= math.log(1.0 / 8.0)


def main() -> None:
    manifest = check_manifest()
    check_theorem_ids()
    check_safety_text(manifest)
    check_parameterized_cutoff()
    print("PX397--PX455 dependency and effective-cutoff audit: PASS")


if __name__ == "__main__":
    main()
