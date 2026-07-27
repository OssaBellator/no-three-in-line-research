#!/usr/bin/env python3
"""Finite audit for AC3rz--AC3sd."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import permutations, product
from math import floor, gcd
import random


def compose_word(maps: list[tuple[int, int]], word: tuple[int, ...]) -> tuple[int, int]:
    """Return (A,B) for chronological application of word."""
    A, B = 1, 0
    for index in word:
        a, b = maps[index]
        A, B = a * A, a * B + b
    return A, B


def defect(left: tuple[int, int], right: tuple[int, int]) -> int:
    """Intercept of left-then-right minus right-then-left."""
    A_i, B_i = left
    A_j, B_j = right
    return (A_j - 1) * B_i - (A_i - 1) * B_j


def defect_gcd(maps: list[tuple[int, int]]) -> int:
    values = [
        abs(defect(maps[i], maps[j]))
        for i in range(len(maps))
        for j in range(i + 1, len(maps))
    ]
    return reduce(gcd, values, 0)


def pairwise_zero_classification(maps: list[tuple[int, int]]) -> None:
    if any(defect(maps[i], maps[j]) for i in range(len(maps)) for j in range(i + 1, len(maps))):
        return
    if all(A == 1 for A, _ in maps):
        return
    index = next(i for i, (A, _) in enumerate(maps) if A != 1)
    A_0, B_0 = maps[index]
    centre = Fraction(B_0, 1 - A_0)
    for A, B in maps:
        if A == 1:
            assert B == 0
        else:
            assert Fraction(B, 1 - A) == centre


def main() -> None:
    rng = random.Random(20260727)
    stats: Counter[str] = Counter()

    atoms = [(A, B) for A in range(-2, 3) for B in range(-3, 4)]
    for family_size in (1, 2, 3):
        for maps_tuple in product(atoms, repeat=family_size):
            maps = list(maps_tuple)
            pairwise_zero_classification(maps)
            stats["classified_families"] += 1

    for _ in range(30_000):
        family_size = rng.randint(2, 6)
        maps = [rng.choice(atoms) for _ in range(family_size)]
        counts = [rng.randint(0, 2) for _ in maps]
        word_list: list[int] = []
        for i, count in enumerate(counts):
            word_list.extend([i] * count)
        if len(word_list) > 9:
            continue

        word = tuple(rng.sample(word_list, len(word_list))) if word_list else ()
        if len(word) >= 2:
            position = rng.randrange(len(word) - 1)
            if word[position] != word[position + 1]:
                swapped = list(word)
                swapped[position], swapped[position + 1] = swapped[position + 1], swapped[position]
                A_1, B_1 = compose_word(maps, word)
                A_2, B_2 = compose_word(maps, tuple(swapped))
                suffix_multiplier = 1
                for index in word[position + 2 :]:
                    suffix_multiplier *= maps[index][0]
                expected = suffix_multiplier * defect(maps[word[position]], maps[word[position + 1]])
                assert A_1 == A_2
                assert B_1 - B_2 == expected
                stats["adjacent_swap_tests"] += 1

        distinct_words = set(permutations(word))
        if len(distinct_words) > 20_000:
            continue
        affine_maps = [compose_word(maps, candidate) for candidate in distinct_words]
        assert len({A for A, _ in affine_maps}) <= 1
        g = defect_gcd(maps)
        if g:
            assert len({B % g for _, B in affine_maps}) <= 1
            stats["same_count_congruence_systems"] += 1

            residues = [(A % g, B % g) for A, B in maps]
            for i in range(len(residues)):
                for j in range(len(residues)):
                    A_i, B_i = residues[i]
                    A_j, B_j = residues[j]
                    left = ((A_j * A_i) % g, (A_j * B_i + B_j) % g)
                    right = ((A_i * A_j) % g, (A_i * B_j + B_i) % g)
                    assert left == right
                    stats["residue_commutativity_tests"] += 1

            h_0 = rng.randint(-10, 10)
            outputs = [A * h_0 + B for A, B in affine_maps]
            if outputs:
                L = min(outputs) - rng.randint(0, 4)
                U = max(outputs) + rng.randint(0, 4)
                feasible = sorted({value for value in outputs if L <= value <= U})
                assert len(feasible) <= floor((U - L) / g) + 1
                stats["bounded_lift_systems"] += 1
                stats["exact_lifts"] += len(feasible)

    # Explicit different-centre involutions: their swap defect is nonzero.
    involutions = [(-1, 2), (-1, 8)]
    assert defect(involutions[0], involutions[1]) != 0
    assert compose_word(involutions, (0, 1)) != compose_word(involutions, (1, 0))
    stats["different_centre_involution_witnesses"] += 1

    print("AC mixed-centre order-defect audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
