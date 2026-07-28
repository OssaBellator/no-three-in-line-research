#!/usr/bin/env python3
"""Finite audit for OP4ad--OP4ah."""

from collections import Counter
from itertools import product
from math import gcd


TYPES = {
    "P1": [[0]],
    "P1+P1": [[0], [1]],
    "P2": [[0, 1]],
    "C2": [[0, 1]],
    "P1+P1+P1": [[0], [1], [2]],
    "P2+P1": [[0, 1], [2]],
    "P3": [[0, 1, 2]],
    "C2+P1": [[0, 1], [2]],
    "C3": [[0, 1, 2]],
}

CYCLE_TYPES = {"C2", "C3"}


def invariants(labels, components, h):
    return tuple(sum(labels[i] for i in comp) % h for comp in components)


def main():
    checked = 0
    fibres = 0
    holonomies = 0
    for h in range(2, 8):
        for name, comps in TYPES.items():
            s = sum(len(c) for c in comps)
            counts = Counter()
            for labels in product(range(h), repeat=s):
                counts[invariants(labels, comps, h)] += 1
                checked += 1
            expected = h ** (s - len(comps))
            assert set(counts.values()) == {expected}
            assert len(counts) == h ** len(comps)
            fibres += len(counts)
            if name in CYCLE_TYPES or name.startswith("C2+") or name == "C3":
                for inv in counts:
                    omega = inv[0]
                    order = 1 if omega == 0 else h // gcd(h, omega)
                    assert (order * omega) % h == 0
                    if order > 1:
                        assert all((j * omega) % h for j in range(1, order))
                    holonomies += 1
    print("OP source-coset holonomy audit passed")
    print(f"  shift assignments checked: {checked}")
    print(f"  normalized invariant fibres: {fibres}")
    print(f"  cycle holonomies checked: {holonomies}")


if __name__ == "__main__":
    main()
