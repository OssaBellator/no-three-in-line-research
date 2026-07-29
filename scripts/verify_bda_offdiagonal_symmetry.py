#!/usr/bin/env python3
"""Verify the off-diagonal role-transpose quotient."""

from itertools import permutations


def main():
    words = ("A", "B", "C", "D", "CD", "AB")
    ordered = [(x, y) for x in words for y in words if x != y]
    assert len(ordered) == 30

    seen = set()
    orbits = []
    for pair in ordered:
        if pair in seen:
            continue
        transposed = (pair[1], pair[0])
        assert transposed != pair
        assert (transposed[1], transposed[0]) == pair
        orbit = frozenset((pair, transposed))
        orbits.append(orbit)
        seen.update(orbit)

    assert len(orbits) == 15
    assert len(seen) == 30

    checked = 0
    for x, y in ordered:
        representative = tuple(sorted((x, y)))
        orientation = 0 if (x, y) == representative else 1
        reconstructed = representative if orientation == 0 else representative[::-1]
        assert reconstructed == (x, y)
        checked += 1

    print(f"verified {len(orbits)} transpose orbits and {checked} oriented reconstructions")


if __name__ == "__main__":
    main()
