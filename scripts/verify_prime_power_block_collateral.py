#!/usr/bin/env python3
"""Verify the exact CMR18 collateral identity at N=9."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product


def determinant(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def completed_reciprocal_9():
    values = []
    for x in range(9):
        if x == 0:
            values.append(0)
        elif x % 3:
            values.append(pow(x, -1, 9))
        else:
            values.append(3 * pow(x // 3, -1, 3))
    return values


def companion(y):
    return (4 * y + 1) % 9


def main():
    p = 3
    n = 9
    a = 3
    first = completed_reciprocal_9()
    companion_points = {(x, companion(first[x])) for x in range(n)}
    fixed_nonunits = {(x, first[x]) for x in range(n) if x % p == 0}
    fixed = companion_points | fixed_nonunits

    blocks = []
    for xi in (1, 2):
        columns = [xi + j * a for j in range(p)]
        rows = [first[x] for x in columns]
        blocks.append((columns, rows))

    candidates = set()
    cell_block = {}
    for block_id, (columns, rows) in enumerate(blocks):
        for x in columns:
            for y in rows:
                candidates.add((x, y))
                cell_block[(x, y)] = block_id

    universe = sorted(fixed | candidates)
    weighted = Fraction(0, 1)
    for triple in combinations(universe, 3):
        if determinant(*triple) != 0:
            continue
        movable = [cell for cell in triple if cell in candidates]
        compatible = True
        counts = [0] * len(blocks)
        for block_id in range(len(blocks)):
            cells = [cell for cell in movable if cell_block[cell] == block_id]
            if len({x for x, _ in cells}) != len(cells):
                compatible = False
            if len({y for _, y in cells}) != len(cells):
                compatible = False
            counts[block_id] = len(cells)
        if not compatible:
            continue
        weight = Fraction(1, 1)
        for r in counts:
            falling = 1
            for j in range(r):
                falling *= p - j
            weight /= falling
        weighted += weight

    potentials = []
    block_permutations = list(permutations(range(p)))
    for choices in product(block_permutations, repeat=len(blocks)):
        first_state = set(fixed_nonunits)
        for (columns, rows), pi in zip(blocks, choices):
            first_state.update((columns[j], rows[pi[j]]) for j in range(p))
        selected = sorted(companion_points | first_state)
        assert len(selected) == 2 * n
        potentials.append(
            sum(1 for triple in combinations(selected, 3) if determinant(*triple) == 0)
        )

    average = Fraction(sum(potentials), len(potentials))
    assert average == weighted
    print(
        f"verified CMR18 at N=9: states={len(potentials)}, "
        f"average={average}, minimum={min(potentials)}, maximum={max(potentials)}"
    )


if __name__ == "__main__":
    main()
