#!/usr/bin/env python3
"""Verify product-bank cylinder factorization and collateral averaging."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

State = tuple[int, ...]
Prescription = tuple[tuple[int, int], ...]


def falling(size: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= size - offset
    return result


def states(size: int) -> list[State]:
    return [
        state
        for state in permutations(range(size))
        if all(state[row] not in (row, (row + 1) % size) for row in range(size))
    ]


def prescriptions(state: State, rank: int):
    edges = tuple((row, state[row]) for row in range(len(state)))
    yield from combinations(edges, rank)


def event_count(bank: list[State], prescription: Prescription) -> int:
    return sum(
        all(state[row] == column for row, column in prescription)
        for state in bank
    )


def verify(size: int = 7) -> None:
    bank = states(size)
    samples: list[Prescription] = []
    witness = bank[0]
    for rank in (1, 2):
        samples.extend(list(prescriptions(witness, rank))[:3])

    for left in samples:
        left_count = event_count(bank, left)
        left_rank = len(left)
        assert left_count * falling(size, left_rank) <= 128 * len(bank)
        for right in samples:
            right_count = event_count(bank, right)
            right_rank = len(right)
            joint = Fraction(left_count * right_count, len(bank) ** 2)
            product_bound = Fraction(128, falling(size, left_rank)) * Fraction(
                128, falling(size, right_rank)
            )
            assert joint <= product_bound

    events = (
        (samples[0], samples[1], 2),
        (samples[2], samples[3], 3),
        (samples[4], samples[0], 5),
    )
    exact_expectation = sum(
        weight
        * Fraction(event_count(bank, left), len(bank))
        * Fraction(event_count(bank, right), len(bank))
        for left, right, weight in events
    )
    enumerated_total = 0
    for first, second in product(bank, repeat=2):
        enumerated_total += sum(
            weight
            for left, right, weight in events
            if all(first[row] == column for row, column in left)
            and all(second[row] == column for row, column in right)
        )
    assert Fraction(enumerated_total, len(bank) ** 2) == exact_expectation


def main() -> None:
    verify()
    print("BDA product-bank collateral: verified for two size-seven banks")


if __name__ == "__main__":
    main()
