#!/usr/bin/env python3
"""Finite checks for CMR1598--CMR1605."""

from __future__ import annotations

from fractions import Fraction
from math import ceil, floor, log2
from random import Random


def band_count(side: int) -> int:
    return 3 * (2 + floor(log2(side))) ** 3


def verify_gap_dichotomy(seed: int = 1605) -> tuple[int, int, int]:
    rng = Random(seed)
    systems = 0
    concentrated = 0
    integer_checks = 0

    for side in range(2, 80):
        classes = band_count(side)
        for _ in range(260):
            active = rng.randint(1, min(classes, 90))
            denominator = rng.randint(1, 500)
            numerators = [rng.randint(0, 4 * denominator) for _ in range(active)]
            contributions = [Fraction(value, denominator) for value in numerators]
            total = sum(contributions, Fraction())

            eta_den = rng.randint(1, 30)
            eta_num = rng.randint(1, eta_den)
            eta = Fraction(eta_num, eta_den)

            if total <= 1 - eta:
                assert total <= 1 - eta
            else:
                witness = max(contributions)
                assert witness > Fraction(1 - eta, classes)
                concentrated += 1

            if total >= 1:
                witness = max(contributions)
                assert witness >= Fraction(1, classes)
                assert sum(numerators) >= denominator
                assert max(numerators) >= ceil(denominator / classes)
                integer_checks += 1

            refinement = rng.randint(1, 12)
            refined: list[Fraction] = []
            for value in numerators:
                pieces = rng.randint(1, refinement)
                cuts = (
                    [0]
                    + sorted(rng.randint(0, value) for _ in range(pieces - 1))
                    + [value]
                )
                refined.extend(
                    Fraction(cuts[index + 1] - cuts[index], denominator)
                    for index in range(pieces)
                )
            assert sum(refined, Fraction()) == total
            if total > 1 - eta:
                assert max(refined) > Fraction(1 - eta, classes * refinement)
            if total >= 1:
                assert max(refined) >= Fraction(1, classes * refinement)

            systems += 1

    return systems, concentrated, integer_checks


def verify_probability_to_count(seed: int = 1600) -> tuple[int, int]:
    rng = Random(seed)
    checked = 0
    line_clean = 0

    for side in range(4, 70):
        classes = band_count(side)
        for rank in (1, 2, 3):
            falling = 1
            for offset in range(rank):
                falling *= side - offset
            for _ in range(180):
                count = rng.randint(1, 6 * side)
                denominators = [rng.randint(1, 200) for _ in range(count)]
                probabilities = [
                    Fraction(rng.randint(0, denominator), denominator)
                    for denominator in denominators
                ]
                contribution = sum(probabilities, Fraction())
                cap = max(probabilities)
                if cap > 0:
                    assert count >= ceil(contribution / cap)
                checked += 1

                kind = rng.choice(("strong", "singleton", "overlap"))
                if kind == "strong":
                    kappa = Fraction(side**side, (side - 2) ** side)
                elif kind == "singleton":
                    kappa = Fraction(
                        (side * (side - 2)) ** side,
                        ((side - 1) * (side - 3)) ** side,
                    )
                else:
                    kappa = Fraction(side**side, (side - 3) ** side)
                uniform_cap = min(Fraction(1), kappa / falling)
                scaled = [
                    uniform_cap * Fraction(rng.randint(0, 100), 100)
                    for _ in range(count)
                ]
                contribution = sum(scaled, Fraction())
                lower = ceil(contribution / uniform_cap) if uniform_cap > 0 else 0
                assert count >= lower
                line_clean += 1

                critical_lower = Fraction(1, classes)
                if contribution >= critical_lower and uniform_cap > 0:
                    formula = ceil(critical_lower / uniform_cap)
                    assert count >= formula

    return checked, line_clean


def verify_restoration_cap() -> int:
    checked = 0
    for side in range(2, 100):
        for eta_den in range(1, 30):
            for eta_num in range(1, eta_den + 1):
                eta = Fraction(eta_num, eta_den)
                for unavailable in range(0, 20):
                    cap = floor(
                        (Fraction(2) + Fraction(unavailable, side - 1)) / eta
                    )
                    candidate = 1 - eta
                    q = cap + 1
                    assert (
                        candidate
                        + Fraction(2, q)
                        + Fraction(unavailable, q * (side - 1))
                        < 1
                    )
                    checked += 1
    return checked


def verify_strict_integer_gap(seed: int = 1602) -> int:
    rng = Random(seed)
    checked = 0
    for side in range(2, 60):
        classes = band_count(side)
        for _ in range(300):
            denominator = rng.randint(1, 1000)
            eta_den = rng.randint(1, 50)
            eta_num = rng.randint(1, eta_den)
            active = rng.randint(1, min(classes, 100))
            nums = [rng.randint(0, 3 * denominator) for _ in range(active)]
            total = Fraction(sum(nums), denominator)
            eta = Fraction(eta_num, eta_den)
            if total > 1 - eta:
                max_num = max(nums)
                assert (
                    eta_den * max_num * classes
                    > (eta_den - eta_num) * denominator
                )
            checked += 1
    return checked


def main() -> None:
    systems, concentrated, integer_checks = verify_gap_dichotomy()
    probability, line_clean = verify_probability_to_count()
    restoration = verify_restoration_cap()
    strict_integer = verify_strict_integer_gap()
    print(
        "verified critical selector localization: "
        f"{systems} class systems with {concentrated} concentrated gap branches "
        f"and {integer_checks} critical integer witnesses; "
        f"{probability} probability-to-count checks, {line_clean} line-clean cap checks, "
        f"{restoration} restoration-gap caps, and {strict_integer} strict integer localizations"
    )


if __name__ == "__main__":
    main()
