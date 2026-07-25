#!/usr/bin/env python3
"""Finite verifier for PX315--PX318."""

from itertools import product


def check_pattern(s: int, states: tuple[int, ...]) -> None:
    arcs = [(u, v) for u in range(s) for v in range(s) if u != v]
    label = dict(zip(arcs, states))

    reset = False
    for u in range(s):
        for v in range(u + 1, s):
            if label[u, v] > 0 and label[v, u] > 0:
                reset = True

    base_rows = [
        sum(label[u, v] == 0 for v in range(s) if v != u)
        for u in range(s)
    ]
    delta0 = max(base_rows, default=0)
    base_count = sum(x == 0 for x in states)

    if not reset:
        assert base_count >= s * (s - 1) // 2
        assert s <= 2 * delta0 + 1


def exhaustive_small() -> None:
    for s in range(1, 5):
        arcs = s * (s - 1)
        for states in product(range(3), repeat=arcs):
            check_pattern(s, states)


def structured_order_five() -> None:
    s = 5
    arcs = [(u, v) for u in range(s) for v in range(s) if u != v]
    pairs = [(u, v) for u in range(s) for v in range(u + 1, s)]
    for orientation_bits in product((0, 1), repeat=len(pairs)):
        required_base = set()
        for bit, (u, v) in zip(orientation_bits, pairs):
            required_base.add((u, v) if bit == 0 else (v, u))
        remaining = [a for a in arcs if a not in required_base]
        candidates = [set(required_base)]
        candidates.extend(required_base | {a} for a in remaining)
        for base_set in candidates:
            states = tuple(0 if a in base_set else 1 for a in arcs)
            check_pattern(s, states)


def sharp_examples() -> None:
    for s in (3, 5, 7):
        arcs = [(u, v) for u in range(s) for v in range(s) if u != v]
        states = []
        half = (s - 1) // 2
        for u, v in arcs:
            states.append(0 if (v - u) % s in range(1, half + 1) else 1)
        check_pattern(s, tuple(states))
        delta0 = half
        assert s == 2 * delta0 + 1


if __name__ == "__main__":
    exhaustive_small()
    structured_order_five()
    sharp_examples()
    print("PX315--PX318 verified")
