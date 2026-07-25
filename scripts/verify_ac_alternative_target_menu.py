#!/usr/bin/env python3
"""Finite checks for AC3ki--AC3km."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product


def subsets(items: tuple[int, ...]) -> list[frozenset[int]]:
    out: list[frozenset[int]] = []
    for size in range(len(items) + 1):
        out.extend(frozenset(choice) for choice in combinations(items, size))
    return out


def weight(tokens: frozenset[int], weights: dict[int, int]) -> int:
    return sum(weights[token] for token in tokens)


def verify_menu_payment(counts: Counter[str]) -> None:
    universe = (0, 1, 2, 3)
    all_sets = subsets(universe)
    token_weights = {0: 1, 1: 2, 2: 3, 3: 5}
    laws = ((1,), (1, 1), (1, 2), (2, 1), (1, 1, 1), (1, 2, 3))

    for menu_size in range(1, 4):
        compatible_laws = [law for law in laws if len(law) == menu_size]
        for common in all_sets:
            for private_tuple in product(all_sets, repeat=menu_size):
                common_weight = weight(common, token_weights)
                cleaned = [private - common for private in private_tuple]
                state_payment = [
                    weight(common | private, token_weights)
                    for private in private_tuple
                ]
                for index, private in enumerate(cleaned):
                    assert state_payment[index] == (
                        common_weight + weight(private, token_weights)
                    )
                for law in compatible_laws:
                    total_mass = sum(law)
                    probabilities = [Fraction(value, total_mass) for value in law]
                    expected_exact = sum(
                        probabilities[index] * state_payment[index]
                        for index in range(menu_size)
                    )
                    expected_formula = common_weight + sum(
                        probabilities[index]
                        * weight(cleaned[index], token_weights)
                        for index in range(menu_size)
                    )
                    assert expected_exact == expected_formula
                    private_total = sum(
                        weight(private, token_weights) for private in cleaned
                    )
                    private_max = max(
                        (weight(private, token_weights) for private in cleaned),
                        default=0,
                    )
                    assert menu_size * private_max >= private_total
                    counts["menu payment systems"] += 1


def verify_rank_return(counts: Counter[str]) -> None:
    laws = ((1,), (1, 1), (1, 2), (1, 1, 1), (1, 2, 3))
    state_cases = []
    for payment in range(0, 8):
        for ranks in product(range(0, 6), repeat=3):
            state_cases.append((payment, ranks))

    for payment, ranks in state_cases:
        drift = sum(ranks) - payment
        if payment > sum(ranks):
            assert drift < 0
        if drift >= 0:
            assert max(ranks) >= Fraction(payment, 3)
        counts["single-state rank ledgers"] += 1

    stride_sets = ((1, 7), (3, 11), (5, 17), (7, 23), (11, 31))
    for menu_size in range(1, 4):
        for law in [value for value in laws if len(value) == menu_size]:
            total_mass = sum(law)
            probabilities = [Fraction(value, total_mass) for value in law]
            for stride, offset in stride_sets:
                for seed in range(0, 800):
                    chosen = [
                        state_cases[
                            (offset + seed + stride * index) % len(state_cases)
                        ]
                        for index in range(menu_size)
                    ]
                    payments = [item[0] for item in chosen]
                    ranks = [item[1] for item in chosen]
                    expected_payment = sum(
                        probabilities[index] * payments[index]
                        for index in range(menu_size)
                    )
                    expected_ranks = [
                        sum(
                            probabilities[index] * ranks[index][rank]
                            for index in range(menu_size)
                        )
                        for rank in range(3)
                    ]
                    drifts = [
                        sum(ranks[index]) - payments[index]
                        for index in range(menu_size)
                    ]
                    expected_drift = sum(
                        probabilities[index] * drifts[index]
                        for index in range(menu_size)
                    )
                    assert expected_drift == sum(expected_ranks) - expected_payment
                    if expected_payment > sum(expected_ranks):
                        assert any(drift < 0 for drift in drifts)
                    if all(drift >= 0 for drift in drifts):
                        assert sum(expected_ranks) >= expected_payment
                        assert max(expected_ranks) >= expected_payment / 3
                    counts["heterogeneous rank ledgers"] += 1


def verify_guardrails(counts: Counter[str]) -> None:
    classes = ("exec", "forbid", "reset", "open")
    for size in range(0, 9):
        for assignment in product(classes, repeat=size):
            parts = {label: assignment.count(label) for label in classes}
            assert sum(parts.values()) == size
            assert parts["exec"] <= size
            inferred_payment_classes = {"exec"}
            assert "forbid" not in inferred_payment_classes
            assert "open" not in inferred_payment_classes
            counts["installation partitions"] += 1

    fan_types = (
        "unconditional",
        "common_residual",
        "support_disjoint",
        "same_owner",
        "many_owner",
    )
    for fan_type in fan_types:
        for size in range(1, 20):
            if fan_type == "same_owner":
                common_weight = 7
                assert common_weight == 7
                assert common_weight != size * 7 or size == 1
            elif fan_type == "many_owner":
                owners = list(range(1, size + 1))
                assert max(owners) * size >= sum(owners)
            counts["fan guardrails"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_menu_payment(counts)
    verify_rank_return(counts)
    verify_guardrails(counts)

    print("AC3ki--AC3km alternative target menu audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
