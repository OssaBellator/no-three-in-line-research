#!/usr/bin/env python3
"""Verify CMR535--CMR540 envelope-signature and joint-persistence arithmetic."""

from __future__ import annotations

from itertools import product
from math import ceil


def pair_signature_count(m: int) -> int:
    signatures = {
        (u, v, x, y)
        for u in range(m)
        for v in range(m)
        for x in range(m)
        for y in range(m)
        if x != u and y != v
    }
    return len(signatures)


def trace_signature_count(m: int) -> int:
    signatures = set()
    for u in range(m):
        for v in range(m):
            for y in range(m):
                if y != v:
                    signatures.add((u, v, "row", y))
            for x in range(m):
                if x != u:
                    signatures.add((u, v, "column", x))
    return len(signatures)


def check_signature_counts() -> None:
    for m in range(1, 12):
        assert pair_signature_count(m) == m * m * (m - 1) * (m - 1)
        assert trace_signature_count(m) == 2 * m * m * (m - 1)


def reintroductions(available: tuple[bool, ...]) -> int:
    return sum(
        available[index] and not available[index - 1]
        for index in range(1, len(available))
    )


def selected_joint_runs(
    sequences: tuple[tuple[bool, ...], ...],
    selected: set[int],
) -> int:
    runs = 0
    inside = False
    for index in range(len(sequences[0])):
        all_absent = all(not sequence[index] for sequence in sequences)
        if not all_absent:
            inside = False
            continue
        if index in selected and not inside:
            runs += 1
            inside = True
    return runs


def check_multi_edge_runs() -> None:
    for edge_count in range(1, 4):
        for length in range(1, 6):
            all_sequences = list(product((False, True), repeat=length))
            for sequences in product(all_sequences, repeat=edge_count):
                joint_times = [
                    index
                    for index in range(length)
                    if all(not sequence[index] for sequence in sequences)
                ]
                for mask in range(1 << len(joint_times)):
                    selected = {
                        time
                        for index, time in enumerate(joint_times)
                        if (mask >> index) & 1
                    }
                    if not selected:
                        continue
                    runs = selected_joint_runs(sequences, selected)
                    budget = 1 + sum(reintroductions(seq) for seq in sequences)
                    assert runs <= budget


def check_pigeonhole_bounds() -> None:
    for stock in range(1, 100):
        for threshold in range(2, 20):
            for total in range(0, 500):
                if total > (threshold - 1) * stock:
                    assert ceil(total / stock) >= threshold

    for h in range(0, 8):
        for t in range(1, 20):
            sides = [max(1, t // (2 ** index)) for index in range(h + 1)]
            pair_sum = sum(m * m * (m - 1) * (m - 1) for m in sides)
            trace_sum = sum(2 * m * m * (m - 1) for m in sides)
            assert pair_sum <= (h + 1) * t * t * (t - 1) * (t - 1)
            assert trace_sum <= 2 * (h + 1) * t * t * (t - 1)


def check_threshold_form() -> None:
    for occurrences in range(1, 100):
        for sigma in range(2, 20):
            for reintro_sum in range(0, 30):
                run_count = 1 + reintro_sum
                largest = ceil(occurrences / run_count)
                if largest < sigma:
                    assert reintro_sum >= ceil(
                        occurrences / (sigma - 1)
                    ) - 1


def main() -> None:
    check_signature_counts()
    check_multi_edge_runs()
    check_pigeonhole_bounds()
    check_threshold_form()
    print("verified envelope cross-signature ledger through three-edge runs")


if __name__ == "__main__":
    main()
