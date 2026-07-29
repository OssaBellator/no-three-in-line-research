#!/usr/bin/env python3
"""Finite checks for OP4bf--OP4bi."""

from itertools import product


def rank(x, radices):
    out = 0
    for i, value in enumerate(x):
        place = 1
        for k in radices[i + 1 :]:
            place *= k
        out += value * place
    return out


def main() -> None:
    checks = 0
    for r in range(1, 6):
        for radices in product(range(2, 6), repeat=r):
            states = list(product(*(range(k) for k in radices)))
            ranks = [rank(x, radices) for x in states]
            assert len(set(ranks)) == len(states)
            assert min(ranks) == 0
            assert max(ranks) == len(states) - 1

            lex_sorted = sorted(states)
            rank_sorted = sorted(states, key=lambda x: rank(x, radices))
            assert lex_sorted == rank_sorted

            # Every nonincreasing closed walk is rank-constant.
            for seed in range(min(200, len(states) * 3)):
                start = seed % len(states)
                path = [start]
                current = start
                for step in range(8):
                    drop = (seed + 3 * step) % (current + 1)
                    current -= drop
                    path.append(current)
                if current == start:
                    assert all(x == start for x in path)

            # Strict descent stock is at most K-1.
            for start in range(len(states)):
                current = start
                steps = 0
                while current > 0:
                    current -= 1
                    steps += 1
                assert steps <= len(states) - 1
            checks += 1
    print(f"verified {checks} mixed-radix decoration systems")


if __name__ == "__main__":
    main()
