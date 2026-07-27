#!/usr/bin/env python3
"""Finite audit for SAS5en--SAS5er."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import math
import random

SEED = 20260727


def reconstructed_column(rows, known, target_position):
    (i, c_i), (j, c_j) = list(known.items())
    r_i = rows[i]
    r_j = rows[j]
    r_k = rows[target_position]
    return Fraction(
        c_i * (r_j - r_i) + (r_k - r_i) * (c_j - c_i),
        r_j - r_i,
    )


def exact_stock_audit(counts):
    for n in range(4, 13):
        row_triples = list(combinations(range(n), 3))
        row_stock = math.comb(n, 3)

        for x in range(n):
            for y in range(n):
                if x == y:
                    continue
                counts["ordered_operations"] += 1

                for i in range(3):
                    for j in range(3):
                        if i == j:
                            continue
                        k = 3 - i - j
                        records = []
                        for rows in row_triples:
                            z = reconstructed_column(rows, {i: x, j: y}, k)
                            if z.denominator == 1:
                                z = int(z)
                                if 0 <= z < n and z not in (x, y):
                                    records.append((rows, i, j, k, z))
                        assert len(records) <= row_stock
                        counts["double_words"] += 1
                        counts["double_records"] += len(records)

                for i in range(3):
                    remaining = [position for position in range(3) if position != i]
                    j, k = remaining[0], remaining[1]
                    records = set()
                    addresses = 0
                    for rows in row_triples:
                        for z in range(n):
                            if z in (x, y):
                                continue
                            addresses += 1
                            z_k = reconstructed_column(rows, {i: x, j: z}, k)
                            if z_k.denominator == 1:
                                z_k = int(z_k)
                                if 0 <= z_k < n and z_k not in (x, y, z):
                                    records.add((rows, i, x, j, z, k, z_k))
                    assert len(records) <= (n - 2) * row_stock
                    counts["singleton_words"] += 1
                    counts["singleton_records"] += len(records)
                    counts["singleton_addresses"] += addresses


def weighted_pigeonhole_audit(counts):
    rng = random.Random(SEED)
    for _ in range(100000):
        n = rng.randint(4, 100)
        row_stock = math.comb(n, 3)
        operation_stock = n * (n - 1)
        interaction_degree = rng.randint(0, 100)
        pair_mass = rng.randint(1, 10_000_000)
        word_type = rng.choice(("double", "singleton"))

        record_stock = row_stock if word_type == "double" else (n - 2) * row_stock
        fresh_word_mass = pair_mass / (24 * (interaction_degree + 1))

        used_operations = min(operation_stock, rng.randint(1, 300))
        raw_operations = [rng.random() for _ in range(used_operations)]
        operation_scale = fresh_word_mass / sum(raw_operations)
        operation_weights = [value * operation_scale for value in raw_operations]
        operation_mass = max(operation_weights)

        assert operation_mass + 1e-12 >= fresh_word_mass / used_operations
        assert fresh_word_mass / used_operations >= fresh_word_mass / operation_stock - 1e-12

        used_records = min(record_stock, rng.randint(1, 500))
        raw_records = [rng.random() for _ in range(used_records)]
        record_scale = operation_mass / sum(raw_records)
        record_weights = [value * record_scale for value in raw_records]

        assert max(record_weights) + 1e-12 >= operation_mass / used_records
        assert operation_mass / used_records >= operation_mass / record_stock - 1e-12
        assert max(record_weights) + 1e-12 >= (
            fresh_word_mass / (operation_stock * record_stock)
        )

        counts["weighted_systems"] += 1
        counts[f"{word_type}_weighted"] += 1


def main():
    counts = defaultdict(int)
    exact_stock_audit(counts)
    weighted_pigeonhole_audit(counts)

    print("SAS fresh repair exact-record audit passed")
    print(f"  ordered repair operations: {counts['ordered_operations']}")
    print(f"  double-scope words: {counts['double_words']}")
    print(f"  valid double-scope records: {counts['double_records']}")
    print(f"  singleton words: {counts['singleton_words']}")
    print(f"  valid singleton records: {counts['singleton_records']}")
    print(f"  canonical singleton addresses: {counts['singleton_addresses']}")
    print(f"  weighted operation/record systems: {counts['weighted_systems']}")
    print(f"  weighted double branches: {counts['double_weighted']}")
    print(f"  weighted singleton branches: {counts['singleton_weighted']}")


if __name__ == "__main__":
    main()
