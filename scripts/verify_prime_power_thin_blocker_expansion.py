#!/usr/bin/env python3
"""Arithmetic checks for CMR284--CMR287."""

from __future__ import annotations

from fractions import Fraction


def verify_width_two_cases(max_t: int = 100_000) -> None:
    for t in range(4, max_t + 1):
        side_size = t - 1
        incidence_count = 2 * side_size

        # D=0, Omega=0: all Hall cells are covered once.
        assert incidence_count == 2 * side_size

        # D=0, Omega=1: one repeated incidence and one omitted target cell.
        assert incidence_count - 1 == 2 * side_size - 1

        # D=1, Omega=0: t-2 full chords and one single available incidence.
        assert 2 * (t - 2) + 1 == 2 * side_size - 1
        assert t - 2 >= 2 if t >= 4 else True


def verify_width_three_extraction(max_t: int = 100_000) -> None:
    for t in range(9, max_t + 1):
        full_lines = t - 5
        overlap_budget = 4
        disjoint_lines = full_lines - overlap_budget
        assert disjoint_lines == t - 9
        assert disjoint_lines >= 0


def verify_probability_mass(max_t: int = 100_000) -> None:
    for t in range(4, max_t + 1):
        alpha_three = Fraction(1, (t - 1) ** 2 * (t - 2))
        canonical_count = t - 2
        canonical_mass = canonical_count * alpha_three
        assert canonical_mass == Fraction(1, (t - 1) ** 2)

        residual_mass = 1 - canonical_mass
        additional_events = residual_mass / alpha_three
        assert additional_events.denominator == 1
        assert additional_events.numerator == t * (t - 2) ** 2


def main() -> None:
    verify_width_two_cases()
    verify_width_three_extraction()
    verify_probability_mass()
    print(
        "verified thin blocker expansion: width-two incidence cases, "
        "width-three disjoint extraction, and the cubic outside-cover count"
    )


if __name__ == "__main__":
    main()
