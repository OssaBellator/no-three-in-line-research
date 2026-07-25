#!/usr/bin/env python3
"""Exhaust BDA5o--BDA5p on small primitive-slope data."""

from itertools import product
from math import ceil, gcd


def det(left, right):
    return left[0] * right[1] - left[1] * right[0]


def subtract(left, right):
    return left[0] - right[0], left[1] - right[1]


def scale(value, point):
    return value * point[0], value * point[1]


def primitive(vector):
    x, y = vector
    divisor = gcd(abs(x), abs(y))
    x //= divisor
    y //= divisor
    if x < 0:
        x, y = -x, -y
    return x, y


def verify_dictionary(parameter_bound=3, context_bound=3):
    checks = 0
    values = range(-parameter_bound, parameter_bound + 1)
    contexts = range(-context_bound, context_bound + 1)

    for a, b, h, q, w in product(values, repeat=5):
        if a <= 0 or b == 0 or gcd(a, abs(b)) != 1:
            continue
        if h <= 0 or q <= 0 or w == 0:
            continue

        H = h + q
        d = (a, b)
        channels = {
            "A": (h * a, h * b),
            "B": (H * a, H * b),
            "C": (h * a, H * b),
            "D": (H * a, h * b),
        }

        expected_walls = {
            "A": d,
            "B": d,
            "C": primitive(channels["C"]),
            "D": primitive(channels["D"]),
        }

        for name, z in channels.items():
            assert primitive(z) == expected_walls[name]

            for ex, ey, x0, x1 in product(contexts, repeat=4):
                if ex == 0 or gcd(abs(ex), abs(ey)) != 1:
                    continue
                e = (ex, ey)
                x = (x0, x1)

                # With Y-X=e, the one-local collinearity determinant equals
                # the signed offset difference.
                y = (x[0] + e[0], x[1] + e[1])
                lhs = det(subtract(x, scale(w, z)), subtract(y, scale(w, z)))
                rhs = det(x, e) - w * det(z, e)
                assert lhs == rhs

                if det(z, e) == 0 and lhs == 0:
                    assert det(x, e) == 0
                    assert primitive(e) == primitive(z)
                checks += 1

        z_a = channels["A"]
        z_b = channels["B"]
        z_c = channels["C"]
        z_d = channels["D"]
        reflected = (a, -b)

        assert primitive(subtract(z_c, z_d)) == reflected
        assert primitive(subtract(z_a, z_b)) == d

        for x0, x1 in product(contexts, repeat=2):
            x = (x0, x1)

            cd_lhs = det(
                subtract(scale(w, z_c), x),
                subtract(scale(w, z_d), x),
            )
            cd_rhs = w * q * (
                det(reflected, x) - w * a * b * (2 * h + q)
            )
            assert cd_lhs == cd_rhs

            ab_lhs = det(
                subtract(scale(w, z_a), x),
                subtract(scale(w, z_b), x),
            )
            ab_rhs = w * q * det(d, x)
            assert ab_lhs == ab_rhs
            checks += 2

    return checks


def verify_spread(maximum_weight=3):
    checks = 0
    for direction_count in range(1, 7):
        for weights in product(range(maximum_weight + 1), repeat=direction_count):
            total = sum(weights)
            if total == 0:
                continue
            for beta in range(1, maximum_weight + 1):
                if max(weights) > beta:
                    continue
                positive = sum(weight > 0 for weight in weights)
                assert positive >= ceil(total / beta)
                checks += 1
    return checks


def main():
    dictionary = verify_dictionary()
    spread = verify_spread()
    print(
        "BDA role slope dictionary: verified "
        f"{dictionary} determinant/slope identities and {spread} spread routers"
    )


if __name__ == "__main__":
    main()
