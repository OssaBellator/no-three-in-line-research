#!/usr/bin/env python3
"""Verify BDA5ap--BDA5ar fixed-cell affine-chain collapse."""

from __future__ import annotations

from itertools import product


def determinant(p: tuple[int, int], q: tuple[int, int]) -> int:
    return p[0] * q[1] - p[1] * q[0]


def verify_ten_bucket_pigeonhole(max_weight: int = 4) -> int:
    checks = 0
    # Six active representative buckets and four zero-padded buckets keep
    # the finite regression compact while exercising all concentration shapes.
    for values in product(range(max_weight + 1), repeat=6):
        buckets = values + (0,) * 4
        total = sum(buckets)
        if total:
            assert 10 * max(buckets) >= total
        checks += 1
    return checks


def verify_anchor_identities() -> int:
    checks = 0
    roles = (None, (0, "u"), (0, "v"), (1, "u"), (1, "v"))
    for a in range(-3, 4):
        for b in range(-3, 4):
            if a == 0 or b == 0:
                continue
            direction = (a, b)
            for u in range(-3, 4):
                for v in range(-3, 4):
                    if u == 0 or v == 0 or u == v:
                        continue
                    for h in range(1, 5):
                        for q in range(1, 4):
                            fixed = (7, -5)
                            for role in roles:
                                if role is None:
                                    anchor = fixed
                                    selected = anchor
                                else:
                                    s, name = role
                                    w = u if name == "u" else v
                                    anchor = (
                                        fixed[0] - (h + s * q) * w * a,
                                        fixed[1] - (h + s * q) * w * b,
                                    )
                                    selected = (
                                        anchor[0] + (h + s * q) * w * a,
                                        anchor[1] + (h + s * q) * w * b,
                                    )
                                assert selected == fixed
                                support = [anchor]
                                for t in (0, 1):
                                    for w in (u, v):
                                        support.append(
                                            (
                                                anchor[0] + (h + t * q) * w * a,
                                                anchor[1] + (h + t * q) * w * b,
                                            )
                                        )
                                assert all(
                                    determinant(
                                        (point[0] - fixed[0], point[1] - fixed[1]),
                                        direction,
                                    )
                                    == 0
                                    for point in support
                                )
                                checks += 1
    return checks


def main() -> None:
    pigeonholes = verify_ten_bucket_pigeonhole()
    identities = verify_anchor_identities()
    print(
        "BDA affine-chain collapse verified:",
        f"{pigeonholes} ten-bucket weight systems,",
        f"{identities} fixed-cell radial identities",
    )


if __name__ == "__main__":
    main()
