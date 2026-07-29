#!/usr/bin/env python3
"""Finite checks for OP4ba--OP4be."""

from itertools import product


def first_repeat_bound(states, step):
    seen = {}
    x = states[0]
    for j in range(len(states) + 1):
        if x in seen:
            return seen[x], j
        seen[x] = j
        x = step(x)
    raise AssertionError("finite deterministic map did not repeat")


def main() -> None:
    checks = 0
    for sizes in product(range(1, 5), repeat=3):
        alphabets = [range(k) for k in sizes]
        full = list(product(*alphabets))
        K = 1
        for k in sizes:
            K *= k
        assert len(full) == K

        compatible_sets = [
            full,
            [x for x in full if sum(x) % 2 == 0],
            [x for x in full if x[2] == (x[0] + x[1]) % sizes[2]],
        ]
        for states in compatible_sets:
            if not states:
                continue
            assert len(states) <= K
            index = {x: i for i, x in enumerate(states)}
            step = lambda x, states=states, index=index: states[(index[x] + 1) % len(states)]
            mu, nu = first_repeat_bound(states, step)
            assert 0 <= mu < nu <= len(states)

            # Third coordinate reconstructed from the first two in this compatible subset.
            reconstructed = [x for x in full if x[2] == (x[0] + x[1]) % sizes[2]]
            projection = [(x[0], x[1]) for x in reconstructed]
            assert len(projection) == len(set(projection))
            assert len(reconstructed) <= sizes[0] * sizes[1]
            checks += 1
    print(f"verified {checks} factorized decoration systems")


if __name__ == "__main__":
    main()
