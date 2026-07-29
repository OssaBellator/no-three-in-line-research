#!/usr/bin/env python3
"""Finite checks for BDA5bu--BDA5bx."""

from fractions import Fraction


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def main():
    checks = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for h in range(1, 5):
                for q in range(1, 5):
                    H = h + q
                    d = (a, b)
                    zA = (h * a, h * b)
                    zB = (H * a, H * b)
                    zC = (h * a, H * b)
                    zD = (H * a, h * b)
                    diff = (zC[0] - zD[0], zC[1] - zD[1])
                    base = det(zC, zD)
                    assert base == -a * b * q * (2 * h + q)
                    assert det(diff, zA) == -2 * h * a * b * q
                    assert det(diff, zB) == -2 * H * a * b * q
                    assert det(diff, zC) == base
                    assert det(diff, zD) == base
                    assert det(d, zA) == 0 and det(d, zB) == 0
                    assert det(d, zC) == a * b * q
                    assert det(d, zD) == -a * b * q
                    assert det(diff, d) == -2 * a * b * q

                    for u in range(1, 6):
                        t = Fraction(u * (2 * h + q), 2)
                        # Rational point P+t d satisfies the CD line equation.
                        x = (t * a, t * b)
                        assert det(diff, x) == u * base
                        for v in range(1, 6):
                            resonances = {
                                "A": v * det(diff, zA) == u * base,
                                "B": v * det(diff, zB) == u * base,
                                "C": v * det(diff, zC) == u * base,
                                "D": v * det(diff, zD) == u * base,
                            }
                            assert resonances["A"] == (2 * h * v == u * (2 * h + q))
                            assert resonances["B"] == (2 * H * v == u * (2 * h + q))
                            assert resonances["C"] == (v == u)
                            assert resonances["D"] == (v == u)
                            checks += 4
    print(f"verified {checks} mixed-template resonance identities")


if __name__ == "__main__":
    main()
