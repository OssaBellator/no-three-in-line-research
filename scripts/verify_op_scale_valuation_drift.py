#!/usr/bin/env python3
"""Finite audit for OP4as--OP4aw.

The script checks finite valuation vectors and guarded additive drift. The
Markdown note contains the arbitrary-size proof.
"""

import random


def main():
    rng = random.Random(404)
    cases = nonzero = zero = guarded = 0

    for rank in range(1, 5):
        for _ in range(5000):
            lower = tuple(rng.randint(-10, -2) for _ in range(rank))
            upper = tuple(rng.randint(2, 10) for _ in range(rank))
            raw_base = tuple(rng.randint(-8, 8) for _ in range(rank))
            base = tuple(
                min(max(raw_base[i], lower[i]), upper[i])
                for i in range(rank)
            )
            drift = tuple(rng.randint(-3, 3) for _ in range(rank))

            if any(drift):
                nonzero += 1
                for repetitions in range(1, 5):
                    assert tuple(
                        base[i] + repetitions * drift[i]
                        for i in range(rank)
                    ) != base

                bounds = []
                for i, value in enumerate(drift):
                    if value < 0:
                        bounds.append((base[i] - lower[i]) // (-value) + 1)
                    elif value > 0:
                        bounds.append((upper[i] - base[i]) // value + 1)

                first_failure = min(bounds)
                assert all(
                    lower[i]
                    <= base[i] + (first_failure - 1) * drift[i]
                    <= upper[i]
                    for i in range(rank)
                )
                assert any(
                    not (
                        lower[i]
                        <= base[i] + first_failure * drift[i]
                        <= upper[i]
                    )
                    for i in range(rank)
                )
                guarded += 1
            else:
                zero += 1
                assert tuple(base[i] + drift[i] for i in range(rank)) == base

            cases += 1

    print(f"{cases:,} valuation blocks")
    print(f"{nonzero:,} nonzero-drift blocks")
    print(f"{guarded:,} exact guarded first-failure checks")
    print(f"{zero:,} exact zero-drift returns")


if __name__ == "__main__":
    main()
