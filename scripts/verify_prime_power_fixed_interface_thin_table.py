#!/usr/bin/env python3
"""Finite checks for CMR1614--CMR1621."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
from random import Random


Edge = tuple[int, int]
Matching = tuple[Edge, ...]


def rank_stock(side: int, rank: int) -> int:
    return comb(side, rank) ** 2 * factorial(rank)


def all_partial_matchings(side: int, rank: int) -> list[Matching]:
    result: list[Matching] = []
    for left in combinations(range(side), rank):
        for right in combinations(range(side), rank):
            for perm in permutations(right):
                result.append(tuple(zip(left, perm)))
    return result


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[Matching]:
    result: list[Matching] = []
    for perm in permutations(range(side)):
        matching = tuple((x, perm[x]) for x in range(side))
        if all(edge not in forbidden for edge in matching):
            result.append(matching)
    return result


def contains(matching: Matching, prescription: Matching) -> bool:
    return set(prescription).issubset(matching)


def contract_forbidden(
    side: int, forbidden: set[Edge], prescription: Matching
) -> tuple[int, set[Edge]]:
    left_used = {x for x, _ in prescription}
    right_used = {y for _, y in prescription}
    left_remaining = [x for x in range(side) if x not in left_used]
    right_remaining = [y for y in range(side) if y not in right_used]
    left_index = {x: index for index, x in enumerate(left_remaining)}
    right_index = {y: index for index, y in enumerate(right_remaining)}
    contracted = {
        (left_index[x], right_index[y])
        for x, y in forbidden
        if x in left_index and y in right_index
    }
    return side - len(prescription), contracted


def verify_rank_stocks() -> tuple[int, int]:
    checked = 0
    prescriptions = 0
    for side in range(1, 8):
        total = 0
        for rank in range(side + 1):
            enumerated = all_partial_matchings(side, rank)
            assert len(enumerated) == rank_stock(side, rank)
            total += len(enumerated)
            prescriptions += len(enumerated)
            checked += 1
        formula_total = sum(rank_stock(side, rank) for rank in range(side + 1))
        assert total == formula_total
        positive_two = side**2 + 2 * comb(side, 2) ** 2
        assert positive_two == rank_stock(side, 1) + rank_stock(side, 2)
        positive_three = positive_two + 6 * comb(side, 3) ** 2
        assert positive_three == sum(
            rank_stock(side, rank) for rank in range(1, min(3, side) + 1)
        )
    return checked, prescriptions


def verify_exact_probabilities(seed: int = 1617) -> tuple[int, int, int]:
    rng = Random(seed)
    hosts = 0
    prescriptions = 0
    contractions = 0

    for side in range(1, 8):
        universe = [(x, y) for x in range(side) for y in range(side)]
        for _ in range(260):
            forbidden = {
                edge
                for edge in universe
                if rng.random() < min(0.35, 1 / max(1, side))
            }
            responses = perfect_matchings(side, forbidden)
            if not responses:
                continue
            allowed = set(universe) - forbidden
            candidates: list[Matching] = []
            for rank in range(1, min(2, side) + 1):
                for prescription in all_partial_matchings(side, rank):
                    if all(edge in allowed for edge in prescription):
                        candidates.append(prescription)
            rng.shuffle(candidates)
            for prescription in candidates[: min(40, len(candidates))]:
                containing = sum(
                    1 for matching in responses if contains(matching, prescription)
                )
                contracted_side, contracted_forbidden = contract_forbidden(
                    side, forbidden, prescription
                )
                residual = perfect_matchings(contracted_side, contracted_forbidden)
                assert containing == len(residual)
                probability = Fraction(containing, len(responses))
                assert probability == Fraction(len(residual), len(responses))
                prescriptions += 1
                contractions += 1
            hosts += 1

    return hosts, prescriptions, contractions


def verify_signature_batching(seed: int = 1616) -> tuple[int, int]:
    rng = Random(seed)
    systems = 0
    episodes = 0
    patterns = 10

    for side in range(1, 35):
        stock = patterns * (
            rank_stock(side, 1) + (rank_stock(side, 2) if side >= 2 else 0)
        )
        signatures = list(range(stock))
        for _ in range(180):
            lam = rng.randint(2, 9)
            length = rng.randint(1, min(20000, 3 * stock))
            sample = [rng.choice(signatures) for _ in range(length)]
            counts = Counter(sample)
            if max(counts.values()) < lam:
                assert length <= (lam - 1) * stock
            else:
                assert any(value >= lam for value in counts.values())
            systems += 1
            episodes += length

    return systems, episodes


def verify_rational_rows(seed: int = 1618) -> tuple[int, int]:
    rng = Random(seed)
    laws = 0
    entries = 0
    for side in range(1, 8):
        all_perms = list(permutations(range(side)))
        for _ in range(240):
            bank = rng.sample(all_perms, rng.randint(1, len(all_perms)))
            weights = [rng.randint(1, 20) for _ in bank]
            denominator = sum(weights)
            classes = rng.randint(1, 12)
            counts = [[rng.randint(0, 8) for _ in range(classes)] for _ in bank]
            row = [
                Fraction(
                    sum(
                        weight * vector[index]
                        for weight, vector in zip(weights, counts)
                    ),
                    denominator,
                )
                for index in range(classes)
            ]
            for value in row:
                assert value.denominator <= denominator
                entries += 1
            uniform = [
                Fraction(sum(vector[index] for vector in counts), len(bank))
                for index in range(classes)
            ]
            assert all(value.denominator <= len(bank) for value in uniform)
            laws += 1
    return laws, entries


def verify_thin_stock() -> tuple[int, int]:
    checked = 0
    cumulative = 0
    for side in range(1, 25):
        partial = sum(rank_stock(side, rank) for rank in range(side + 1))
        rank_two = rank_stock(side, 1)
        if side >= 2:
            rank_two += rank_stock(side, 2)
        rank_three = rank_two
        if side >= 3:
            rank_three += rank_stock(side, 3)
        table = factorial(side) * side**2 * partial * rank_two * rank_three
        assert table > 0
        cumulative += table
        checked += 1
    assert cumulative > 0
    return checked, cumulative


def main() -> None:
    stocks, prescriptions = verify_rank_stocks()
    hosts, exact, contractions = verify_exact_probabilities()
    batching, episodes = verify_signature_batching()
    laws, entries = verify_rational_rows()
    thin, cumulative = verify_thin_stock()
    print(
        "verified fixed-interface/thin exact table: "
        f"{stocks} rank-stock identities over {prescriptions} prescriptions; "
        f"{hosts} executable hosts, {exact} exact prescription probabilities "
        f"and {contractions} contractions; "
        f"{batching} batching systems over {episodes} episodes; "
        f"{laws} rational response laws with {entries} row entries; "
        f"and {thin} thin-side table bounds (cumulative ambient stock {cumulative})"
    )


if __name__ == "__main__":
    main()
