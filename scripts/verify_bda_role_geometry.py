#!/usr/bin/env python3
"""Exhaust BDA5m--BDA5n on small integer decoder data."""

from itertools import product


def det(left, right):
    return left[0] * right[1] - left[1] * right[0]


def subtract(left, right):
    return left[0] - right[0], left[1] - right[1]


def scale(value, point):
    return value * point[0], value * point[1]


def verify_geometry(parameter_bound=2, context_bound=2):
    identity_count = 0
    uniqueness_count = 0
    values = range(-parameter_bound, parameter_bound + 1)
    contexts = range(-context_bound, context_bound + 1)

    for a, b, h, q, u, v in product(values, repeat=6):
        if a == 0 or b == 0 or u == 0 or v == 0:
            continue
        if h <= 0 or q <= 0 or u == v:
            continue

        H = h + q
        channels = {
            "A": (h * a, h * b),
            "B": (H * a, H * b),
            "C": (h * a, H * b),
            "D": (H * a, h * b),
        }

        # One-local-cell identity and common-context wall.
        for z in channels.values():
            for x0, x1, y0, y1 in product(contexts, repeat=4):
                x = (x0, x1)
                y = (y0, y1)
                direction = subtract(y, x)

                vanish = []
                for role in (u, v):
                    lhs = det(
                        subtract(x, scale(role, z)),
                        subtract(y, scale(role, z)),
                    )
                    rhs = det(x, y) - role * det(z, direction)
                    assert lhs == rhs
                    vanish.append(lhs == 0)
                    identity_count += 1

                if all(vanish):
                    assert det(x, y) == 0
                    assert det(z, direction) == 0
                    uniqueness_count += 1

        # Two-local-cell identities for the only same-layer pairs.
        for first, second in (("C", "D"), ("A", "B")):
            z_i = channels[first]
            z_j = channels[second]
            pair_det = det(z_i, z_j)

            for x0, x1 in product(contexts, repeat=2):
                x = (x0, x1)
                vanish = []

                for role in (u, v):
                    lhs = det(
                        subtract(scale(role, z_i), x),
                        subtract(scale(role, z_j), x),
                    )
                    rhs = (
                        role * role * pair_det
                        - role * det(subtract(z_i, z_j), x)
                    )
                    assert lhs == rhs
                    vanish.append(lhs == 0)
                    identity_count += 1

                if first == "C":
                    assert pair_det == -a * b * q * (2 * h + q)
                    assert pair_det != 0
                    assert not all(vanish)
                else:
                    assert pair_det == 0
                    if all(vanish):
                        assert det((a, b), x) == 0
                uniqueness_count += 1

    return identity_count, uniqueness_count


def verify_channel_pigeonhole(maximum_cost=3):
    """Check the six-channel and wall/non-wall constants."""
    checks = 0
    for costs in product(range(maximum_cost + 1), repeat=6):
        total = sum(costs)
        if total == 0:
            continue
        assert max(costs) * 6 >= total

        for wall in range(max(costs) + 1):
            nonwall = max(costs) - wall
            assert max(wall, nonwall) * 2 >= max(costs)
            checks += 1
    return checks


def main():
    identities, uniqueness = verify_geometry()
    pigeonholes = verify_channel_pigeonhole()
    print(
        "BDA decoder-role geometry: verified "
        f"{identities} identities, {uniqueness} role tests, "
        f"and {pigeonholes} pigeonhole tests"
    )


if __name__ == "__main__":
    main()
