#!/usr/bin/env python3
"""Verify side-ten affine transposition orbits and double-coset sizes."""

from __future__ import annotations

import math
import subprocess
import tempfile
from pathlib import Path


N = 10
DISTANCES = (1, 2, 5)
EXPECTED_ORBIT_SIZES = {1: 20, 2: 20, 5: 5}
EXPECTED_INTERSECTIONS = {1: 2, 2: 2, 5: 8}
EXPECTED_DOUBLE_COSETS = {1: 800, 2: 800, 5: 200}


def compose(first: tuple[int, ...], second: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(first[second[index]] for index in range(N))


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * N
    for index, value in enumerate(permutation):
        result[value] = index
    return tuple(result)


def affine_group() -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple((multiplier * value + shift) % N for value in range(N))
        for multiplier in range(N)
        if math.gcd(multiplier, N) == 1
        for shift in range(N)
    )


def transposition(first: int, second: int) -> tuple[int, ...]:
    result = list(range(N))
    result[first], result[second] = result[second], result[first]
    return tuple(result)


def main() -> None:
    group = affine_group()
    assert len(group) == 40
    group_set = set(group)

    double_cosets: dict[int, set[tuple[int, ...]]] = {}
    for distance in DISTANCES:
        representative = transposition(0, distance)
        representative_inverse = representative

        conjugates = {
            compose(element, compose(representative, inverse(element)))
            for element in group
        }
        intersection = {
            element
            for element in group
            if compose(
                representative,
                compose(element, representative_inverse),
            )
            in group_set
        }
        double_coset = {
            compose(left, compose(representative, right))
            for left in group
            for right in group
        }

        assert len(conjugates) == EXPECTED_ORBIT_SIZES[distance]
        assert len(intersection) == EXPECTED_INTERSECTIONS[distance]
        assert len(double_coset) == EXPECTED_DOUBLE_COSETS[distance]
        assert len(double_coset) == len(group) ** 2 // len(intersection)
        double_cosets[distance] = double_coset

    assert double_cosets[1].isdisjoint(double_cosets[2])
    assert double_cosets[1].isdisjoint(double_cosets[5])
    assert double_cosets[2].isdisjoint(double_cosets[5])
    assert len(set().union(*double_cosets.values())) == 1800

    source = Path(__file__).with_name(
        "search_product_transposition_double_coset_ten.cpp"
    )
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "double_coset_search"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        for distance in DISTANCES:
            completed = subprocess.run(
                [str(executable), "cc", str(distance), "0", "0"],
                check=True,
                capture_output=True,
                text=True,
            )
            expected = (
                f"NONE n=10 o=cc distance={distance} "
                f"maps={EXPECTED_DOUBLE_COSETS[distance]} "
                "first=0 pairs=0 total=0 avg=0 max=0"
            )
            assert completed.stdout.strip() == expected

    print(
        "PX980--PX982 side-ten transposition double-coset verifier: PASS"
    )


if __name__ == "__main__":
    main()
