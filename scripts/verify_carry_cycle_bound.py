#!/usr/bin/env python3
"""Verify the p=11 frozen carry cycle and the two-colour anchor release."""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import gcd


def inv(x: int, p: int) -> int:
    return pow(x, p - 2, p)


def point(c: int, x: int, p: int) -> tuple[int, int]:
    return x, (c * inv(x, p)) % p


def line_key(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int, int]:
    x1, y1 = p1
    x2, y2 = p2
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    d = gcd(gcd(abs(a), abs(b)), abs(c))
    if d:
        a //= d
        b //= d
        c //= d
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def triple_potential(points: list[tuple[int, int]]) -> int:
    assert len(points) == len(set(points)), "configuration contains a collision"
    lines: dict[tuple[int, int, int], set[tuple[int, int]]] = defaultdict(set)
    for p1, p2 in combinations(points, 2):
        key = line_key(p1, p2)
        lines[key].add(p1)
        lines[key].add(p2)
    return sum(len(line) * (len(line) - 1) * (len(line) - 2) // 6 for line in lines.values())


def main() -> None:
    p, a, b = 11, 2, 3
    red = {x: point(a, x, p) for x in range(1, p)}
    blue = {x: point(b, x, p) for x in range(1, p)}

    cycle_x = [4, 5, 7, 6]
    cycle_y = [red[x][1] for x in cycle_x]
    outside = [red[x] for x in range(1, p) if x not in cycle_x] + list(blue.values())
    outside_set = set(outside)
    outside_phi = triple_potential(outside)

    values: list[int] = []
    valid_states = []
    for perm in permutations(range(4)):
        state = [(cycle_x[i], cycle_y[perm[i]]) for i in range(4)]
        if any(cell in outside_set for cell in state):
            continue
        value = triple_potential(outside + state) - outside_phi
        values.append(value)
        valid_states.append((value, perm, state))

    expected_values = [10, 11, 11, 14, 14, 14, 17, 17, 17, 17, 20, 20, 22, 24]
    assert sorted(values) == expected_values
    assert min(values) == 10
    assert len(valid_states) == 14

    shift_two = tuple((i + 2) % 4 for i in range(4))
    shift_two_value = next(value for value, perm, _ in valid_states if perm == shift_two)
    assert shift_two_value == 24
    ratios = {
        cycle_x[(i + 2) % 4] * inv(cycle_x[i], p) % p
        for i in range(4)
    }
    assert ratios == {10}

    anchor_x = [1, 8, 6, 3, 10, 5]
    anchor_y = [blue[x][1] for x in anchor_x]
    anchor_perm = [0, 5, 1, 2, 4, 3]
    new_blue = [
        (anchor_x[i], anchor_y[anchor_perm[i]])
        for i in range(len(anchor_x))
    ] + [blue[x] for x in range(1, p) if x not in anchor_x]

    old_phi = triple_potential(list(red.values()) + list(blue.values()))
    new_phi = triple_potential(list(red.values()) + new_blue)
    assert old_phi == 16
    assert new_phi == 6

    print("frozen one-colour cycle: verified")
    print(f"valid cycle-block states: {len(valid_states)}")
    print(f"incremental potentials: {sorted(values)}")
    print(f"constant-window shift-two potential: {shift_two_value}")
    print(f"two-colour anchor release: {old_phi} -> {new_phi}")


if __name__ == "__main__":
    main()
