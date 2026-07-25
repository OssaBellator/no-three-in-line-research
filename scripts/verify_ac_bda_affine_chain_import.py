#!/usr/bin/env python3
"""Verify AC3hf--AC3hh fixed-cell BDA affine-chain import."""

from __future__ import annotations

from fractions import Fraction


def verify_selected_q_triples() -> int:
    checks = 0
    roles = (None, (0, "u"), (0, "v"), (1, "u"), (1, "v"))
    for a in range(-2, 3):
        for b in range(-2, 3):
            if a == 0 or b == 0:
                continue
            for u in range(-2, 3):
                for v in range(-2, 3):
                    if u == 0 or v == 0 or u == v:
                        continue
                    for h in range(1, 4):
                        for q in range(1, 3):
                            fixed = (5, -4)
                            for role in roles:
                                if role is None:
                                    anchor = fixed
                                    scale = h
                                else:
                                    s, name = role
                                    w = u if name == "u" else v
                                    anchor = (
                                        fixed[0] - (h + s * q) * w * a,
                                        fixed[1] - (h + s * q) * w * b,
                                    )
                                    scale = h + s * q
                                triple = (
                                    anchor,
                                    (
                                        anchor[0] + scale * u * a,
                                        anchor[1] + scale * u * b,
                                    ),
                                    (
                                        anchor[0] + scale * v * a,
                                        anchor[1] + scale * v * b,
                                    ),
                                )
                                assert fixed in triple
                                checks += 1
    return checks


def verify_parity_slot_injectivity(max_slots: int = 19) -> int:
    checks = 0
    for slot_count in range(2, max_slots + 1):
        for parity in (0, 1):
            edges = [
                (j, j + 1)
                for j in range(slot_count - 1)
                if j % 2 == parity
            ]
            for selected_endpoint in (0, 1):
                selected = [edge[selected_endpoint] for edge in edges]
                assert len(selected) == len(set(selected))
                checks += 1
    return checks


def verify_constants(max_weight: int = 100) -> int:
    checks = 0
    for weight in range(1, max_weight + 1):
        assert 10 * Fraction(weight, 10) == weight
        assert 30 * Fraction(weight, 30) == weight
        checks += 1
    return checks


def main() -> None:
    triples = verify_selected_q_triples()
    parity = verify_parity_slot_injectivity()
    constants = verify_constants()
    print(
        "AC BDA affine-chain import verified:",
        f"{triples} selected Q-triples,",
        f"{parity} parity-slot injectivity checks,",
        f"{constants} payment constants",
    )


if __name__ == "__main__":
    main()
