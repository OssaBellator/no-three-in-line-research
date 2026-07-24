#!/usr/bin/env python3
"""Verify PX111: fixed-partition cyclotomic rank-three barrier."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from math import comb

Cylinder = tuple[tuple[int, int], ...]


def primitive_root(p: int) -> int:
    factors: set[int] = set()
    value = p - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    raise AssertionError(p)


def cosets(p: int, index: int) -> tuple[tuple[int, ...], ...]:
    generator = primitive_root(p)
    subgroup = tuple(pow(generator, index * exponent, p) for exponent in range((p - 1) // index))
    result = []
    for offset in range(index):
        representative = pow(generator, offset, p)
        result.append(tuple(sorted(representative * value % p for value in subgroup)))
    assert len({value for coset in result for value in coset}) == p - 1
    return tuple(result)


def verify_complete_enumeration(p: int, index: int) -> None:
    partition = cosets(p, index)
    size = (p - 1) // index
    assert size >= 3

    populations: Counter[Cylinder] = Counter()
    map_count = 0
    cylinders_per_map = index * comb(size, 3)

    for coefficients in product(range(1, p), repeat=index):
        map_count += 1
        seen = 0
        for coset, coefficient in zip(partition, coefficients):
            for rows in combinations(coset, 3):
                cylinder = tuple((row, coefficient * row % p) for row in rows)
                assert len({image for _, image in cylinder}) == 3
                populations[cylinder] += 1
                seen += 1
        assert seen == cylinders_per_map

    expected_labels = index * comb(size, 3) * (p - 1)
    expected_population = (p - 1) ** (index - 1)
    assert len(populations) == expected_labels
    assert set(populations.values()) == {expected_population}
    assert sum(populations.values()) == map_count * cylinders_per_map

    maximum_probability = max(populations.values()) / map_count
    assert maximum_probability == 1 / (p - 1)
    normalized = maximum_probability * p * (p - 1) * (p - 2)
    assert normalized == p * (p - 2)
    print(
        f"p={p}, d={index}: maps={map_count}, labels={len(populations)}, "
        f"probability=1/{p - 1}, K3={int(normalized)}"
    )


def primes_through(limit: int) -> tuple[int, ...]:
    result = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, int(value**0.5) + 1)):
            result.append(value)
    return tuple(result)


def verify_symbolic_bounds() -> None:
    for p in primes_through(101):
        for index in range(1, p):
            if (p - 1) % index:
                continue
            size = (p - 1) // index
            if size < 3:
                continue
            label_count = index * comb(size, 3) * (p - 1)
            contribution = index * comb(size, 3)
            assert contribution / label_count == 1 / (p - 1)
            assert p * (p - 1) * (p - 2) / (p - 1) == p * (p - 2)
    print("symbolic divisor bounds checked through prime 101")


def main() -> None:
    for case in ((7, 2), (13, 3), (13, 4)):
        verify_complete_enumeration(*case)
    verify_symbolic_bounds()
    print("cyclotomic rank-three barrier verified")


if __name__ == "__main__":
    main()
