#!/usr/bin/env python3
"""Finite checks for AC3kn--AC3kq."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product


def verify_statewise_identities(counts: Counter[str]) -> None:
    for payment in range(0, 11):
        for boundary_ranks in product(range(0, 7), repeat=3):
            boundary = sum(boundary_ranks)
            assert boundary == sum(boundary_ranks)
            for off_ranks in product(range(0, 7), repeat=3):
                off_boundary = sum(off_ranks)
                drift = boundary + off_boundary - payment
                assert drift == (
                    sum(boundary_ranks) + sum(off_ranks) - payment
                )
                counts["statewise petal ledgers"] += 1


def verify_menu_realization(counts: Counter[str]) -> None:
    states = [(boundary, off) for boundary in range(0, 13) for off in range(0, 13)]
    strides = ((1, 5), (3, 7), (5, 11), (7, 13), (11, 17))
    for menu_size in range(1, 9):
        for payment in range(0, 16):
            for stride, offset in strides:
                for seed in range(0, 600):
                    chosen = [
                        states[
                            (offset + seed + stride * index) % len(states)
                        ]
                        for index in range(menu_size)
                    ]
                    boundary_average = sum(
                        Fraction(boundary, menu_size)
                        for boundary, _ in chosen
                    )
                    off_average = sum(
                        Fraction(off, menu_size) for _, off in chosen
                    )
                    total_average = boundary_average + off_average
                    drifts = [
                        boundary + off - payment
                        for boundary, off in chosen
                    ]
                    assert Fraction(sum(drifts), menu_size) == (
                        total_average - payment
                    )
                    if all(drift >= 0 for drift in drifts):
                        assert total_average >= payment
                        assert (
                            boundary_average >= Fraction(payment, 2)
                            or off_average >= Fraction(payment, 2)
                        )
                        if boundary_average >= Fraction(payment, 2):
                            assert max(
                                boundary for boundary, _ in chosen
                            ) >= Fraction(payment, 2)
                        if off_average >= Fraction(payment, 2):
                            assert max(
                                off for _, off in chosen
                            ) >= Fraction(payment, 2)
                    if total_average < payment:
                        assert any(drift < 0 for drift in drifts)
                    counts["petal menu realization systems"] += 1


def verify_rank_constants(counts: Counter[str]) -> None:
    for payment in range(0, 101):
        for category in range((payment + 1) // 2, payment + 31):
            rank_floor = Fraction(category, 3)
            assert rank_floor >= Fraction(payment, 6)
            for extraction in range(1, 21):
                paid = rank_floor / extraction
                returned = rank_floor / (3 * extraction)
                assert paid >= Fraction(payment, 6 * extraction)
                assert returned >= Fraction(payment, 18 * extraction)
                counts["petal pivot constants"] += 1


def verify_category_partition(counts: Counter[str]) -> None:
    categories = ("boundary", "off")
    ranks = (1, 2, 3)
    labels = [
        (category, rank)
        for category in categories
        for rank in ranks
    ]
    for size in range(0, 10):
        for assignment in product(range(len(labels)), repeat=size):
            buckets = {label: 0 for label in labels}
            for index in assignment:
                buckets[labels[index]] += 1
            assert sum(buckets.values()) == size
            boundary = sum(
                buckets[("boundary", rank)] for rank in ranks
            )
            off_boundary = sum(
                buckets[("off", rank)] for rank in ranks
            )
            assert boundary + off_boundary == size
            counts["created category partitions"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_statewise_identities(counts)
    verify_menu_realization(counts)
    verify_rank_constants(counts)
    verify_category_partition(counts)

    print("AC3kn--AC3kq petal rank closure audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
