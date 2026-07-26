#!/usr/bin/env python3
"""Check deterministic target-line pruning and distinct-helper assignment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    marked_size = int(data["marked_size"])
    helper_count = int(data["helper_count"])
    positive_offsets = [int(value) for value in data["positive_line_offsets"]]
    negative_offsets = [int(value) for value in data["negative_line_offsets"]]

    if marked_size <= 0 or helper_count < marked_size:
        raise AssertionError("invalid marked/helper sizes")

    marked = [(j, j) for j in range(marked_size)]
    helpers = [
        (marked_size + j, marked_size + j)
        for j in range(helper_count)
    ]
    offsets = positive_offsets + negative_offsets
    line_count = len(offsets)

    domains: list[list[int]] = []
    bad_counts: list[int] = []
    for j in range(marked_size):
        marked_column = marked[j][0]
        next_marked_row = marked[(j + 1) % marked_size][1]
        bad: set[int] = set()
        for idx, (helper_column, helper_row) in enumerate(helpers):
            for offset in offsets:
                # The target line is y=x+offset.
                if (
                    helper_row == marked_column + offset
                    or next_marked_row == helper_column + offset
                ):
                    bad.add(idx)
                    break
        bad_counts.append(len(bad))
        domains.append([idx for idx in range(helper_count) if idx not in bad])

    if max(bad_counts, default=0) > 2 * line_count:
        raise AssertionError("one-line one-helper bound failed")

    chosen: list[int] = []
    used: set[int] = set()
    for domain in domains:
        choice = next((idx for idx in domain if idx not in used), None)
        if choice is None:
            raise AssertionError("greedy distinct-helper assignment failed")
        chosen.append(choice)
        used.add(choice)

    for j, choice in enumerate(chosen):
        if choice not in domains[j]:
            raise AssertionError("chosen helper lies on a targeted line")

    min_domain = min(map(len, domains), default=0)
    if min_domain < marked_size:
        raise AssertionError("domains are too small for the greedy theorem")

    print("marked size", marked_size)
    print("helper reservoir", helper_count)
    print("target line count", line_count)
    print("bad helpers by gap", bad_counts)
    print("maximum bad helpers", max(bad_counts, default=0))
    print("minimum target-clean domain", min_domain)
    print("chosen helper indices", chosen)
    print("distinct helpers", len(set(chosen)))
    print("outcome", "line_sparse_anchor_activation_clearing")


if __name__ == "__main__":
    main()
