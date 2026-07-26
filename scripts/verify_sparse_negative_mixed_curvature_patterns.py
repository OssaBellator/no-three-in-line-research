#!/usr/bin/env python3
"""Finite checks for SAS5bs--SAS5bw."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
from random import Random

OMEGA = (0, 1)
TAU = (2, 3)
COLUMNS = range(5)


def swapped(coloring: tuple[int, ...], swap: tuple[int, int], active: int) -> tuple[int, ...]:
    if not active:
        return coloring
    values = list(coloring)
    a, b = swap
    values[a], values[b] = values[b], values[a]
    return tuple(values)


def state_coloring(coloring: tuple[int, ...], epsilon: int, eta: int) -> tuple[int, ...]:
    return swapped(swapped(coloring, OMEGA, epsilon), TAU, eta)


def indicator(coloring: tuple[int, ...], scope: tuple[int, int, int], required: tuple[int, int, int]) -> int:
    return int(all(coloring[column] == label for column, label in zip(scope, required)))


def factor_values(
    coloring: tuple[int, ...],
    scope: tuple[int, int, int],
    required: tuple[int, int, int],
) -> tuple[tuple[int, int], tuple[int, int], int]:
    a_values = []
    b_values = []
    for epsilon in (0, 1):
        current = state_coloring(coloring, epsilon, 0)
        a_values.append(
            int(
                all(
                    current[column] == label
                    for column, label in zip(scope, required)
                    if column in OMEGA
                )
            )
        )
    for eta in (0, 1):
        current = state_coloring(coloring, 0, eta)
        b_values.append(
            int(
                all(
                    current[column] == label
                    for column, label in zip(scope, required)
                    if column in TAU
                )
            )
        )
    c_value = int(
        all(
            coloring[column] == label
            for column, label in zip(scope, required)
            if column not in OMEGA and column not in TAU
        )
    )
    return (a_values[0], a_values[1]), (b_values[0], b_values[1]), c_value


def canonical_pair(scope: tuple[int, int, int]) -> tuple[int, int]:
    pairs = [(a, b) for a in OMEGA for b in TAU if a in scope and b in scope]
    assert pairs
    return min(pairs)


def scope_type(scope: tuple[int, int, int], pair: tuple[int, int]) -> int:
    a, b = pair
    third = next(column for column in scope if column not in pair)
    mate_a = OMEGA[1] if a == OMEGA[0] else OMEGA[0]
    mate_b = TAU[1] if b == TAU[0] else TAU[0]
    if third == mate_a:
        return 1
    if third == mate_b:
        return 2
    return 0


def exhaustive_records(counts: Counter[str]) -> list[tuple[tuple[int, int], int, int]]:
    negative_metadata: list[tuple[tuple[int, int], int, int]] = []
    scopes = [
        scope
        for scope in combinations(COLUMNS, 3)
        if any(column in OMEGA for column in scope)
        and any(column in TAU for column in scope)
    ]

    for coloring in product(range(3), repeat=5):
        for scope in scopes:
            for required in product(range(3), repeat=3):
                table = tuple(
                    indicator(state_coloring(coloring, epsilon, eta), scope, required)
                    for epsilon, eta in ((0, 0), (1, 0), (0, 1), (1, 1))
                )
                curvature = table[3] - table[1] - table[2] + table[0]
                a_values, b_values, c_value = factor_values(coloring, scope, required)
                predicted = c_value * (a_values[1] - a_values[0]) * (b_values[1] - b_values[0])
                assert curvature == predicted
                assert curvature in (-1, 0, 1)
                counts["exhaustive records"] += 1

                if curvature < 0:
                    assert table in ((0, 1, 0, 0), (0, 0, 1, 0))
                    orientation = 0 if table == (0, 1, 0, 0) else 1
                    pair = canonical_pair(scope)
                    kind = scope_type(scope, pair)
                    negative_metadata.append((pair, orientation, kind))
                    counts["negative records"] += 1
                else:
                    assert table not in ((0, 1, 0, 0), (0, 0, 1, 0))
    return negative_metadata


def weighted_localization(
    metadata: list[tuple[tuple[int, int], int, int]], counts: Counter[str]
) -> None:
    rng = Random(20260726)
    assert metadata
    for _ in range(50000):
        bins: dict[tuple[tuple[int, int], int, int], int] = defaultdict(int)
        total = 0
        for _record in range(rng.randint(1, 80)):
            key = rng.choice(metadata)
            weight = rng.randint(1, 20)
            bins[key] += weight
            total += weight
        heaviest = max(bins.values())
        assert heaviest * 24 >= total
        counts["weighted systems"] += 1
        counts["weighted negative mass"] += total

        # Reproduce the two-stage proof: pair, then orientation and scope type.
        by_pair: dict[tuple[int, int], int] = defaultdict(int)
        for (pair, _orientation, _kind), weight in bins.items():
            by_pair[pair] += weight
        pair = max(by_pair, key=by_pair.get)
        pair_weight = by_pair[pair]
        assert pair_weight * 4 >= total
        refined = {
            (orientation, kind): weight
            for (stored_pair, orientation, kind), weight in bins.items()
            if stored_pair == pair
        }
        assert max(refined.values()) * 6 >= pair_weight


def generic_boolean_wall(counts: Counter[str]) -> None:
    negative = []
    for table in product((0, 1), repeat=4):
        curvature = table[3] - table[1] - table[2] + table[0]
        if curvature < 0:
            negative.append((table, curvature))
    assert len(negative) == 5
    assert ((0, 1, 1, 0), -2) in negative
    counts["generic negative Boolean patterns"] = len(negative)


def main() -> None:
    counts: Counter[str] = Counter()
    generic_boolean_wall(counts)
    metadata = exhaustive_records(counts)
    weighted_localization(metadata, counts)
    print("SAS5bs--SAS5bw negative mixed-curvature audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
