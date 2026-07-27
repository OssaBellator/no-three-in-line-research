#!/usr/bin/env python3
"""Finite audit for SAS5ei--SAS5em opposite-side comparison."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from random import Random


def split_overlap(
    repaired: dict[int, Fraction],
    opposite: dict[int, Fraction],
) -> tuple[dict[int, Fraction], dict[int, Fraction]]:
    overlap: dict[int, Fraction] = {}
    fresh: dict[int, Fraction] = {}
    for record, weight in repaired.items():
        matched = min(weight, opposite.get(record, Fraction(0)))
        if matched:
            overlap[record] = matched
        residual = weight - matched
        if residual:
            fresh[record] = residual
    return overlap, fresh


def total(weights: dict[int, Fraction]) -> Fraction:
    return sum(weights.values(), Fraction(0))


def exhaustive_unit_audit() -> dict[str, int]:
    checks = 0
    for r1 in range(0, 7):
        for r2 in range(0, 7):
            for o1 in range(0, 7):
                for o2 in range(0, 7):
                    repaired = {0: Fraction(r1), 1: Fraction(r2)}
                    opposite = {0: Fraction(o1), 1: Fraction(o2)}
                    overlap, fresh = split_overlap(repaired, opposite)
                    assert total(repaired) == total(overlap) + total(fresh)
                    checks += 1
    return {"exhaustive_splits": checks}


def random_comparison_audit(seed: int = 90917) -> dict[str, int]:
    rng = Random(seed)
    systems = 0
    overlap_branches = 0
    fresh_branches = 0
    word_column_checks = 0
    integrated_checks = 0

    for _ in range(80_000):
        n = rng.randint(3, 30)
        operation_count = rng.randint(1, 10)
        repaired: dict[int, Fraction] = {}
        bottleneck = Fraction(0)
        next_record = 0
        word_of: dict[int, int] = {}
        scope_of: dict[int, tuple[int, int, int]] = {}

        for _op in range(operation_count):
            b = Fraction(rng.randint(1, 20), rng.randint(1, 8))
            bottleneck += b
            record_count = rng.randint(1, 5)
            local_weights = [
                Fraction(rng.randint(1, 20), rng.randint(1, 8))
                for _ in range(record_count)
            ]
            scale = max(Fraction(1), b / sum(local_weights))
            for weight in local_weights:
                rid = next_record
                next_record += 1
                repaired[rid] = weight * scale
                word_of[rid] = rng.randrange(12)
                scope_of[rid] = tuple(rng.sample(range(n), 3))

        repaired_total = total(repaired)
        assert repaired_total >= bottleneck

        opposite: dict[int, Fraction] = {}
        for rid in range(next_record + rng.randint(0, 8)):
            if rng.random() < 0.65:
                opposite[rid] = Fraction(rng.randint(1, 30), rng.randint(1, 8))

        overlap, fresh = split_overlap(repaired, opposite)
        overlap_total = total(overlap)
        fresh_total = total(fresh)
        assert repaired_total == overlap_total + fresh_total
        assert max(overlap_total, fresh_total) >= repaired_total / 2
        assert max(overlap_total, fresh_total) >= bottleneck / 2

        if overlap_total >= bottleneck / 2:
            overlap_branches += 1
            repaired_residual = repaired_total - overlap_total
            opposite_residual = total(opposite) - overlap_total
            assert repaired_residual >= 0
            assert opposite_residual >= 0
        else:
            fresh_branches += 1
            assert fresh_total >= bottleneck / 2

            word_mass: dict[int, Fraction] = defaultdict(Fraction)
            for rid, weight in fresh.items():
                word_mass[word_of[rid]] += weight
            best_word, best_word_mass = max(word_mass.items(), key=lambda item: item[1])
            assert best_word_mass >= fresh_total / 12

            column_mass: dict[int, Fraction] = defaultdict(Fraction)
            for rid, weight in fresh.items():
                if word_of[rid] == best_word:
                    for column in scope_of[rid]:
                        column_mass[column] += weight
            best_column_mass = max(column_mass.values())
            assert best_column_mass >= 3 * best_word_mass / n
            assert best_column_mass >= fresh_total / (4 * n)
            assert best_column_mass >= bottleneck / (8 * n)
            word_column_checks += 1

        d_pair = rng.randint(0, 100)
        source_pair_mass = bottleneck * (d_pair + 1)
        retained = source_pair_mass / (d_pair + 1)
        assert retained == bottleneck
        assert max(overlap_total, fresh_total) >= retained / 2
        integrated_checks += 1
        systems += 1

    return {
        "systems": systems,
        "overlap_branches": overlap_branches,
        "fresh_branches": fresh_branches,
        "word_column_checks": word_column_checks,
        "integrated_checks": integrated_checks,
    }


def main() -> None:
    result = exhaustive_unit_audit()
    result.update(random_comparison_audit())
    print(result)


if __name__ == "__main__":
    main()
