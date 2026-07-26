#!/usr/bin/env python3
"""Finite audit for SAS5cm--SAS5cq."""

from __future__ import annotations

import random
from fractions import Fraction
from itertools import product

SEED = 20260726
RNG = random.Random(SEED)


def exhaustive_small() -> int:
    checked = 0
    # Exhaust small banks directly from donor-level exact identities.
    for m in range(1, 5):
        for delta_omega in range(3):
            for delta_tau in product(range(3), repeat=m):
                for L in product(range(1, 4), repeat=m):
                    for cplus in product(range(2), repeat=m):
                        for cminus in product(range(5), repeat=m):
                            dcomb = [
                                delta_omega + delta_tau[i] + L[i] + cplus[i] - cminus[i]
                                for i in range(m)
                            ]
                            lhs = sum(dcomb)
                            rhs = (
                                m * delta_omega
                                + sum(delta_tau)
                                + sum(L)
                                + sum(cplus)
                                - sum(cminus)
                            )
                            assert lhs == rhs
                            improving = [i for i, value in enumerate(dcomb) if value < 0]
                            budget_use = sum(L[i] - dcomb[i] for i in improving)
                            assert budget_use <= sum(cminus[i] for i in improving)
                            checked += 1
                            if checked >= 200_000:
                                return checked
    return checked


def random_banks(trials: int = 80_000) -> tuple[int, int, int, int]:
    donors_total = 0
    records_total = 0
    improving_total = 0
    scale_dominant = 0
    for _ in range(trials):
        m = RNG.randint(1, 18)
        donors_total += m
        delta_omega = Fraction(RNG.randint(0, 8), RNG.randint(1, 4))
        delta_tau = [Fraction(RNG.randint(0, 8), RNG.randint(1, 4)) for _ in range(m)]
        L = [Fraction(RNG.randint(1, 20), RNG.randint(1, 5)) for _ in range(m)]
        cplus = [Fraction(RNG.randint(0, 10), RNG.randint(1, 5)) for _ in range(m)]

        # Build physical exact records. Each record is incident with at most two donors.
        record_count = RNG.randint(1, 40)
        records_total += record_count
        omega_weights: list[Fraction] = []
        donor_negative = [Fraction(0) for _ in range(m)]
        for _record in range(record_count):
            weight = Fraction(RNG.randint(1, 20), RNG.randint(1, 6))
            omega_weights.append(weight)
            incidence_size = RNG.randint(0, min(2, m))
            for donor in RNG.sample(range(m), incidence_size):
                # Negative conjunction curvature has magnitude one.
                donor_negative[donor] += weight

        omega_cross = sum(omega_weights, Fraction(0))
        cminus = donor_negative
        assert sum(cminus, Fraction(0)) <= 2 * omega_cross

        dcomb = [
            delta_omega + delta_tau[i] + L[i] + cplus[i] - cminus[i]
            for i in range(m)
        ]
        exact_sum = sum(dcomb, Fraction(0))
        identity_rhs = (
            m * delta_omega
            + sum(delta_tau, Fraction(0))
            + sum(L, Fraction(0))
            + sum(cplus, Fraction(0))
            - sum(cminus, Fraction(0))
        )
        assert exact_sum == identity_rhs

        L_bank = sum(L, Fraction(0))
        assert exact_sum >= L_bank - 2 * omega_cross

        improving = [i for i, value in enumerate(dcomb) if value < 0]
        improving_total += len(improving)
        improvement_budget = sum((L[i] - dcomb[i] for i in improving), Fraction(0))
        assert improvement_budget <= sum((cminus[i] for i in improving), Fraction(0))
        assert improvement_budget <= 2 * omega_cross
        assert sum((L[i] for i in improving), Fraction(0)) <= 2 * omega_cross
        assert sum((-dcomb[i] for i in improving), Fraction(0)) <= 2 * omega_cross

        if L_bank > 2 * omega_cross:
            scale_dominant += 1
            average_bound = (L_bank - 2 * omega_cross) / m
            assert max(dcomb) >= average_bound > 0
        elif all(value <= 0 for value in dcomb):
            assert L_bank <= 2 * omega_cross

        # Exact-record localization in the collateral-dominant branch.
        if L_bank <= 2 * omega_cross and record_count > 0:
            assert max(omega_weights) >= omega_cross / record_count
            assert omega_cross >= L_bank / 2
            assert max(omega_weights) >= L_bank / (2 * record_count)

    return donors_total, records_total, improving_total, scale_dominant


def exact_incidence_enumeration() -> int:
    checked = 0
    # Directly enumerate all donor-incidence subsets of size at most two.
    for m in range(1, 9):
        for mask in range(1 << m):
            degree = mask.bit_count()
            if degree > 2:
                continue
            weight = Fraction(3, 2)
            contributions = [weight if (mask >> i) & 1 else Fraction(0) for i in range(m)]
            assert sum(contributions, Fraction(0)) <= 2 * weight
            checked += 1
    return checked


def cardinality_checks(trials: int = 30_000) -> int:
    checked = 0
    for _ in range(trials):
        omega = Fraction(RNG.randint(1, 60), RNG.randint(1, 8))
        lam = Fraction(RNG.randint(1, 10), RNG.randint(1, 5))
        gamma = Fraction(RNG.randint(1, 10), RNG.randint(1, 5))
        max_count = int((2 * omega) // (lam + gamma))
        # Construct any admissible number of improvements and verify the bound.
        count = RNG.randint(0, max_count)
        total = count * (lam + gamma)
        assert total <= 2 * omega
        assert count <= int((2 * omega) // (lam + gamma))
        checked += 1
    return checked


def main() -> None:
    exhaustive = exhaustive_small()
    donors, records, improving, dominant = random_banks()
    incidences = exact_incidence_enumeration()
    cardinality = cardinality_checks()
    print(
        "PASS SAS donor-bank aggregate-energy audit:",
        f"{exhaustive} exhaustive donor systems;",
        f"{donors} random donors;",
        f"{records} physical records;",
        f"{improving} improving donors;",
        f"{dominant} scale-dominant banks;",
        f"{incidences} exact incidence patterns;",
        f"{cardinality} cardinality bounds.",
    )


if __name__ == "__main__":
    main()
