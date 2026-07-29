#!/usr/bin/env python3
from fractions import Fraction

POINT = (Fraction(3, 5), Fraction(1, 2), Fraction(2, 5))
DUALS = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
    (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
)
NAMES = ("a", "b", "c", "central")
CENTRAL = DUALS[3]


def dot(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def quantize_up(point, denominator):
    return tuple(Fraction(ceil_fraction(denominator * x), denominator) for x in point)


def active_duals(point):
    values = tuple(dot(y, point) for y in DUALS)
    optimum = max(values)
    return tuple(NAMES[i] for i, value in enumerate(values) if value == optimum), optimum


def l1(vector):
    return sum(abs(x) for x in vector)


def main():
    active, value = active_duals(POINT)
    assert active == ("central",)
    assert value == Fraction(3, 4)
    competitor_values = [dot(y, POINT) for y in DUALS[:3]]
    gap = min(value - x for x in competitor_values)
    assert gap == Fraction(3, 20)
    lipschitz = max(l1(tuple(CENTRAL[i] - y[i] for i in range(3))) for y in DUALS[:3])
    assert lipschitz == Fraction(3, 2)
    threshold = lipschitz / gap
    assert threshold == 10

    exceptional = []
    for denominator in range(1, 101):
        quantized = quantize_up(POINT, denominator)
        active, quantized_value = active_duals(quantized)
        if denominator >= 11:
            assert active == ("central",)
            assert quantized_value == dot(CENTRAL, quantized)
        if active != ("central",):
            exceptional.append((denominator, quantized, active))

    assert exceptional == [(2, (Fraction(1), Fraction(1, 2), Fraction(1, 2)), ("a", "central"))]
    q11 = quantize_up(POINT, 11)
    assert q11 == (Fraction(7, 11), Fraction(6, 11), Fraction(5, 11))

    print({
        "base_point": tuple(str(x) for x in POINT),
        "active_chamber": "central",
        "chamber_gap": str(gap),
        "dual_l1_radius": str(lipschitz),
        "guaranteed_denominator": 11,
        "quantized_point_M11": tuple(str(x) for x in q11),
        "exceptional_denominators_1_to_100": [x[0] for x in exceptional],
        "audited_denominators": 100,
    })


if __name__ == "__main__":
    main()
