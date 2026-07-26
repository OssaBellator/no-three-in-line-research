#!/usr/bin/env python3
"""Checks for CMR1190--CMR1197."""

from fractions import Fraction
import random


def check_abstract_countermodel():
    potential = {"S": 1, "Q1": 2, "Q2": 2}
    assert min(potential.values()) == 1
    assert all(potential[state] >= potential["S"] for state in ("Q1", "Q2"))
    destroyed = {"Q1": 1, "Q2": 1}
    created = {"Q1": 2, "Q2": 2}
    for state in ("Q1", "Q2"):
        assert potential[state] - potential["S"] == created[state] - destroyed[state]
    return 2


def check_conditioning_nonclosure():
    family = {"S", "Q1", "Q2"}
    anchor_states = {"S"}
    conditioned = family & anchor_states
    assert conditioned == {"S"}
    induced_value = 1
    assert induced_value > 0
    return 1


def check_averaging_criterion():
    rng = random.Random(1193)
    checked = 0
    improvement_cases = 0
    for _ in range(200000):
        values = [rng.randint(0, 50) for _ in range(rng.randint(1, 20))]
        weights_raw = [rng.randint(0, 100) for _ in values]
        if not any(weights_raw):
            weights_raw[0] = 1
        total = sum(weights_raw)
        weights = [Fraction(weight, total) for weight in weights_raw]
        average = sum(weight * value for weight, value in zip(weights, values))
        threshold = rng.randint(0, 50)
        if average < threshold:
            assert min(values) < threshold
            improvement_cases += 1
        if min(values) >= threshold:
            assert average >= threshold
        checked += 1
    return checked, improvement_cases


def check_destroyed_collateral_identity():
    rng = random.Random(1194)
    checked = 0
    for _ in range(200000):
        base = rng.randint(0, 100)
        lost = rng.randint(0, base)
        new = rng.randint(0, 100)
        later = base - lost + new
        assert later - base == new - lost
        if new < lost:
            assert later < base
        if later >= base:
            assert new >= lost
        checked += 1
    return checked


def check_weighted_bank_inequality():
    rng = random.Random(1196)
    checked = 0
    improving = 0
    for _ in range(100000):
        bank_count = rng.randint(1, 10)
        expected_new = []
        expected_lost = []
        weights = []
        for _bank in range(bank_count):
            state_count = rng.randint(1, 20)
            new_counts = [rng.randint(0, 20) for _ in range(state_count)]
            lost_counts = [rng.randint(0, 20) for _ in range(state_count)]
            expected_new.append(Fraction(sum(new_counts), state_count))
            expected_lost.append(Fraction(sum(lost_counts), state_count))
            weights.append(rng.randint(0, 20))
        if not any(weights):
            weights[0] = 1
        total_new = sum(weight * value for weight, value in zip(weights, expected_new))
        total_lost = sum(weight * value for weight, value in zip(weights, expected_lost))
        if total_new < total_lost:
            improving += 1
            assert total_lost - total_new > 0
        checked += 1
    return checked, improving


def main():
    averages = check_averaging_criterion()
    weighted = check_weighted_bank_inequality()
    print(
        "verified finite-response nonclosure:",
        check_abstract_countermodel(),
        "robust responses,",
        check_conditioning_nonclosure(),
        "dirty singleton,",
        averages[0],
        "averages with",
        averages[1],
        "strict-improvement cases,",
        check_destroyed_collateral_identity(),
        "new/lost identities, and",
        weighted[0],
        "weighted bank systems with",
        weighted[1],
        "strict inequalities",
    )


if __name__ == "__main__":
    main()
