#!/usr/bin/env python3
"""Finite checks for AC3pe--AC3pi."""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import prod
from random import Random


def cap_vector(raw: tuple[int, ...], thresholds: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(min(value, threshold) for value, threshold in zip(raw, thresholds))


def stock_checks(counts: Counter[str]) -> None:
    for q in range(1, 4):
        for thresholds in product(range(3), repeat=q):
            cap_words = set(product(*(range(h + 1) for h in thresholds)))
            assert len(cap_words) == prod(h + 1 for h in thresholds)
            for base_count in range(1, 4):
                signatures = {
                    (base, word) for base in range(base_count) for word in cap_words
                }
                assert len(signatures) == base_count * prod(h + 1 for h in thresholds)
                counts["signature stocks"] += 1


def identity_checks(counts: Counter[str]) -> None:
    for thresholds in ((0,), (1,), (2,), (1, 2), (2, 1), (1, 1, 2)):
        raws = list(product(range(6), repeat=len(thresholds)))
        for left in raws:
            for right in raws:
                same = cap_vector(left, thresholds) == cap_vector(right, thresholds)
                # Above-threshold numerical aliases collapse; below-threshold values do not.
                if same:
                    assert all(
                        l == r or (l >= h and r >= h)
                        for l, r, h in zip(left, right, thresholds)
                    )
                counts["raw alias pairs"] += 1


def boundary_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(60000):
        q = rng.randint(1, 3)
        thresholds = tuple(rng.randint(0, 3) for _ in range(q))
        base_count = rng.randint(1, 3)
        kinds = rng.randint(1, 4)
        cap_words = list(product(*(range(h + 1) for h in thresholds)))
        signatures = [(base, word) for base in range(base_count) for word in cap_words]
        truth = {signature: rng.randrange(2) for signature in signatures}
        false_states = [s for s in signatures if truth[s] == 0]
        true_states = [s for s in signatures if truth[s] == 1]
        if not false_states or not true_states:
            continue

        length = rng.randint(2, 8)
        projected = [rng.choice(signatures) for _ in range(length)]
        projected[0] = rng.choice(false_states)
        projected[-1] = rng.choice(true_states)
        raw_path = []
        for base, capped in projected:
            raw = tuple(
                value if value < threshold else threshold + rng.randint(0, 50)
                for value, threshold in zip(capped, thresholds)
            )
            raw_path.append((base, raw))
        projected_again = [
            (base, cap_vector(raw, thresholds)) for base, raw in raw_path
        ]
        values = [truth[state] for state in projected_again]
        first = next(index for index in range(1, length) if values[index] == 1)
        assert values[first - 1] == 0 and values[first] == 1
        assert all(values[index] == 0 for index in range(first))

        s_count = len(signatures)
        false_count = len(false_states)
        true_count = len(true_states)
        exact_complete_stock = kinds * false_count * true_count
        assert exact_complete_stock <= kinds * (s_count * s_count // 4)
        counts["projected recreation paths"] += 1


def shared_capacity_checks(counts: Counter[str]) -> None:
    rng = Random(91)
    for _ in range(50000):
        capacity = rng.randint(0, 20)
        aliases = rng.randint(1, 50)
        requests = rng.randint(0, 100)
        remaining = capacity
        accepted = 0
        for index in range(requests):
            _alias = index % aliases
            if remaining == 0:
                break
            remaining -= 1
            accepted += 1
        assert accepted <= capacity
        assert remaining == capacity - accepted
        counts["shared alias ticket systems"] += 1


def monotone_supply_checks(counts: Counter[str]) -> None:
    rng = Random(414)
    for _ in range(50000):
        q = rng.randint(1, 8)
        current = [rng.randint(0, 40) for _ in range(q)]
        initial = sum(current)
        accepted = 0
        while sum(current) and rng.randrange(5) != 0:
            live = [i for i, value in enumerate(current) if value]
            coordinate = rng.choice(live)
            amount = rng.randint(1, current[coordinate])
            current[coordinate] -= amount
            accepted += 1
        assert accepted <= initial
        assert sum(current) >= 0
        counts["monotone supply histories"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    stock_checks(counts)
    identity_checks(counts)
    boundary_checks(counts)
    shared_capacity_checks(counts)
    monotone_supply_checks(counts)
    print("AC3pe--AC3pi capped multiplicity quotient audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
