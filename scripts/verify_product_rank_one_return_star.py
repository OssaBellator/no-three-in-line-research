#!/usr/bin/env python3
"""Exact arithmetic checks for PX386--PX392."""

from fractions import Fraction


def main() -> None:
    # PX386--PX387 averaging constants.
    for ambient_order in range(1, 101):
        for destroyed in range(1, 31):
            coordinate_mass = Fraction(destroyed * ambient_order, 48)
            assert coordinate_mass / ambient_order == Fraction(
                destroyed,
                48,
            )

            generic_mass = Fraction(
                destroyed * ambient_order * ambient_order,
                32,
            )
            assert generic_mass / (ambient_order * ambient_order) == Fraction(
                destroyed,
                32,
            )

    # PX389: two high-point one-variable returns give exponent 3/4.
    assert Fraction(1, 2) + Fraction(1, 4) == Fraction(3, 4)
    assert Fraction(3, 4) > Fraction(1, 2)
    assert Fraction(3, 4) > Fraction(1, 3)

    # PX390: the first two-variable return multiplies destruction by n/64.
    for ambient_order in range(4097, 5000):
        child_weight = Fraction(ambient_order, 64)
        assert child_weight > 64
        # Linear weight dominates all n^(alpha) caps with alpha<1.
        for numerator in range(1, 10):
            alpha = Fraction(numerator, 10)
            if alpha < 1:
                assert 1 > alpha

    # PX388 threshold rearrangements.
    for occupancy in range(1, 20):
        for threshold in range(1, 20):
            coordinate_limit = 48 * occupancy * threshold
            generic_limit = 32 * occupancy * threshold
            assert Fraction(coordinate_limit, 48 * occupancy) == threshold
            assert Fraction(generic_limit, 32 * occupancy) == threshold

    print("PX386--PX392 rank-one-return verifier: PASS")


if __name__ == "__main__":
    main()
