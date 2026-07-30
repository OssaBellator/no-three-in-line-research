#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import comb, gcd
from pathlib import Path
import gc
import json


def primitive(dx: int, dy: int) -> tuple[int, int]:
    divisor = gcd(abs(dx), abs(dy))
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy


def hyperbola(prime: int, channel: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (x, channel * pow(x, -1, prime) % prime)
        for x in range(1, prime)
    )


def secant_pairs(
    points: tuple[tuple[int, int], ...], candidate: tuple[int, int]
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    direction_classes: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for point in points:
        direction = primitive(point[0] - candidate[0], point[1] - candidate[1])
        direction_classes.setdefault(direction, []).append(point)
    pairs = []
    for cells in direction_classes.values():
        assert len(cells) <= 2
        if len(cells) == 2:
            pairs.append(tuple(sorted(cells)))
    return sorted(pairs)


def secant_pair_count(
    points: tuple[tuple[int, int], ...], candidate: tuple[int, int]
) -> int:
    counts: dict[tuple[int, int], int] = {}
    for point in points:
        direction = primitive(point[0] - candidate[0], point[1] - candidate[1])
        counts[direction] = counts.get(direction, 0) + 1
    assert max(counts.values(), default=0) <= 2
    return sum(value == 2 for value in counts.values())


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def direct_potential(points: set[tuple[int, int]]) -> int:
    return sum(collinear(*triple) for triple in combinations(sorted(points), 3))


class RestrictedLineEngine:
    def __init__(self, points: set[tuple[int, int]]) -> None:
        self.points = sorted(points)
        self.index = {point: index for index, point in enumerate(self.points)}
        line_cells: dict[tuple[int, int, int], set[tuple[int, int]]] = {}
        for first, second in combinations(self.points, 2):
            dx, dy = primitive(second[0] - first[0], second[1] - first[1])
            intercept = dy * first[0] - dx * first[1]
            line_cells.setdefault((dx, dy, intercept), set()).update((first, second))
        self.masks: list[int] = []
        for cells in line_cells.values():
            if len(cells) < 3:
                continue
            mask = 0
            for point in cells:
                mask |= 1 << self.index[point]
            self.masks.append(mask)

    def potential(self, points: set[tuple[int, int]]) -> int:
        mask = 0
        for point in points:
            mask |= 1 << self.index[point]
        return sum(comb((mask & line).bit_count(), 3) for line in self.masks)


def seed_census(prime: int) -> tuple[int, int, dict[int, int]]:
    layers = {
        channel: hyperbola(prime, channel)
        for channel in range(1, prime)
    }
    layer_sets = {channel: set(points) for channel, points in layers.items()}
    count_at_least_seven = 0
    maximum = 0
    histogram: Counter[int] = Counter()
    for anchor_channel in range(1, prime):
        anchor = layers[anchor_channel]
        anchor_set = layer_sets[anchor_channel]
        for switch_channel in range(1, prime):
            if switch_channel == anchor_channel:
                continue
            switch_by_column = dict(layers[switch_channel])
            for first, second in combinations(range(1, prime), 2):
                inserted = (
                    (first, switch_by_column[second]),
                    (second, switch_by_column[first]),
                )
                if inserted[0] in anchor_set or inserted[1] in anchor_set:
                    continue
                for candidate in inserted:
                    pair_count = secant_pair_count(anchor, candidate)
                    maximum = max(maximum, pair_count)
                    if pair_count >= 6:
                        histogram[pair_count] += 1
                    if pair_count >= 7:
                        count_at_least_seven += 1
    return count_at_least_seven, maximum, dict(sorted(histogram.items()))


def evaluate_bank(record: dict) -> dict:
    prime = record["p"]
    anchor = set(hyperbola(prime, record["anchor_channel"]))
    switch = set(hyperbola(prime, record["switch_channel"]))
    first, second = record["switch_rows"]
    switch_by_column = dict(switch)
    removed = {
        (first, switch_by_column[first]),
        (second, switch_by_column[second]),
    }
    inserted = {
        (first, switch_by_column[second]),
        (second, switch_by_column[first]),
    }
    candidate = tuple(record["candidate"])
    assert candidate in inserted
    assert inserted.isdisjoint(anchor)

    pairs = secant_pairs(tuple(sorted(anchor)), candidate)[:7]
    selected = [pair[0] for pair in pairs]
    columns = [point[0] for point in selected]
    rows = [point[1] for point in selected]
    assert len(set(columns)) == len(set(rows)) == 7

    switched = (switch - removed) | inserted
    switched_by_column = dict(switched)
    forbidden = {(index, index) for index in range(7)}
    for index, column in enumerate(columns):
        other_row = switched_by_column[column]
        if other_row in rows:
            forbidden.add((index, rows.index(other_row)))

    bank = [
        permutation
        for permutation in permutations(range(7))
        if all((index, permutation[index]) not in forbidden for index in range(7))
    ]

    anchor_cells = {
        (columns[i], rows[j])
        for i in range(7)
        for j in range(7)
        if (i, j) not in forbidden
    }
    current = anchor | switch
    base = current - set(selected) - removed
    fixed = base | inserted
    assert len(current) == 2 * (prime - 1)
    assert len(fixed) == 2 * (prime - 1) - 7

    current_potential = direct_potential(current)
    fixed_potential = direct_potential(fixed)
    restricted = RestrictedLineEngine(fixed | anchor_cells)
    values = []
    for permutation in bank:
        matching = {
            (columns[index], rows[permutation[index]])
            for index in range(7)
        }
        successor = fixed | matching
        assert len(successor) == len(current)
        values.append(restricted.potential(successor))

    return {
        "pairs": pairs,
        "selected": selected,
        "forbidden": sorted(forbidden),
        "bank_size": len(bank),
        "current_potential": current_potential,
        "fixed_potential": fixed_potential,
        "best_potential": min(values),
        "improving_states": sum(value < current_potential for value in values),
        "potential_sum": sum(values),
        "anchor": anchor,
        "switch": switch,
        "removed": removed,
        "inserted": inserted,
        "base": base,
        "fixed": fixed,
        "columns": columns,
        "rows": rows,
    }


def p31_ac1_audit(bank: dict, expected: dict) -> None:
    columns = bank["columns"]
    rows = bank["rows"]
    forbidden = set(bank["forbidden"])
    anchor_cells = {
        (i, j): (columns[i], rows[j])
        for i in range(7)
        for j in range(7)
        if (i, j) not in forbidden
    }
    items = [
        ("anchor", address, point)
        for address, point in anchor_cells.items()
    ] + [
        ("fixed", None, point)
        for point in bank["fixed"]
    ]

    counts = Counter({1: 0, 2: 0, 3: 0})
    rank_one_degree: Counter[tuple[int, int]] = Counter()
    for triple in combinations(items, 3):
        points = [entry[2] for entry in triple]
        if len(set(points)) < 3 or not collinear(*points):
            continue
        addresses = [
            entry[1] for entry in triple if entry[0] == "anchor"
        ]
        rank = len(addresses)
        if rank == 0:
            continue
        if len({i for i, _ in addresses}) != rank:
            continue
        if len({j for _, j in addresses}) != rank:
            continue
        counts[rank] += 1
        if rank == 1:
            rank_one_degree[addresses[0]] += 1

    assert counts == Counter({
        1: expected["certificate_counts"]["rank_1"],
        2: expected["certificate_counts"]["rank_2"],
        3: expected["certificate_counts"]["rank_3"],
    })
    base_potential = direct_potential(bank["base"])
    d_star = bank["current_potential"] - base_potential
    f_star = bank["fixed_potential"] - base_potential
    gap = bank["current_potential"] - bank["fixed_potential"]
    assert (d_star, f_star, gap) == (
        expected["D_star"],
        expected["F_star"],
        expected["gap"],
    )

    normalized = {
        1: counts[1] / 7,
        2: counts[2] / (7 * 6),
        3: counts[3] / (7 * 6 * 5),
    }
    heavy_rank = max(normalized, key=normalized.get)
    assert heavy_rank == expected["heavy_rank"] == 1
    assert normalized[heavy_rank] >= gap / 384

    heavy_address, heavy_degree = rank_one_degree.most_common(1)[0]
    assert list(heavy_address) == expected["heavy_anchor_address"]
    assert list(anchor_cells[heavy_address]) == expected["heavy_anchor_cell"]
    assert heavy_degree == expected["heavy_anchor_degree"]


def main() -> None:
    record = json.loads(Path("data/ac-prime-seed-census.json").read_text())

    for expected in record["seed_counts"]:
        count, maximum, histogram = seed_census(expected["p"])
        assert count == expected["seeds_at_least_7"]
        assert maximum == expected["max_secant_pairs"]
        expected_histogram = {
            int(key): value
            for key, value in expected.get("high_pair_histogram", {}).items()
        }
        assert histogram == expected_histogram
        gc.collect()

    banks: dict[int, dict] = {}
    for expected in record["canonical_full_state_banks"]:
        actual = evaluate_bank(expected)
        banks[expected["p"]] = actual
        for field in (
            "bank_size",
            "current_potential",
            "fixed_potential",
            "best_potential",
            "improving_states",
            "potential_sum",
        ):
            assert actual[field] == expected[field], (
                expected["p"], field, actual[field], expected[field]
            )
        gc.collect()

    p31 = banks[31]
    assert p31["best_potential"] > p31["current_potential"]
    assert p31["improving_states"] == 0
    p31_ac1_audit(p31, record["p31_ac1_record"])

    print("AC prime-minus-one seed census")
    print("tested_primes: 11, 13, 17, 19, 23, 29, 31, 37")
    print("first_prime_with_seven_pair_seed: 19")
    print("seed_counts_at_19_23_29_31_37: 56, 144, 600, 216, 2512")
    print("canonical_bank_improving_states: 408, 1172, 26, 0")
    print("p31_bank_states: 1088")
    print("p31_current_best_potential: 106, 108")
    print("p31_certificate_counts: 179, 112, 20")
    print("p31_heavy_rank: 1")
    print("p31_heavy_anchor: (12, 12), degree 20")


if __name__ == "__main__":
    main()
