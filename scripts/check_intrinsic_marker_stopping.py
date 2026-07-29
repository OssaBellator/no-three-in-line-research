#!/usr/bin/env python3
from fractions import Fraction


def load(rows):
    cols = {}
    for row in rows.values():
        for y, p in row.items():
            cols[y] = cols.get(y, Fraction(0)) + p
    return max(cols.values(), default=Fraction(0)), cols


def main():
    stops = {"s0": 1, "s1": 1, "s2": 2, "s3": 2, "s4": 3, "s5": 3}
    q = {1: 3, 2: 6, 3: 12}
    retained = {1: Fraction(1), 2: Fraction(2, 3), 3: Fraction(1, 2)}

    rows = {}
    level_rows = {1: {}, 2: {}, 3: {}}
    for s, i in stops.items():
        targets = [(i, 0)] + [(i, s, j) for j in range(1, q[i])]
        keep = max(1, int(q[i] * retained[i]))
        kept = targets[:keep]
        row = {y: Fraction(1, keep) for y in kept}
        rows[s] = row
        level_rows[i][s] = row

    total, cols = load(rows)
    level_loads = {i: load(level_rows[i])[0] for i in level_rows}
    assert total == max(level_loads.values())

    bounds = {i: Fraction(2, 1) / (retained[i] * q[i]) for i in q}
    for i in q:
        assert level_loads[i] <= bounds[i]
    assert total <= max(bounds.values())

    bad_level = max(level_loads, key=level_loads.get)
    bad_cols = {y: v for y, v in cols.items() if y[0] == bad_level}
    assert max(bad_cols.values()) == total

    print({
        "all_checks_passed": True,
        "combined_load": str(total),
        "level_loads": {i: str(v) for i, v in level_loads.items()},
        "conditioned_bounds": {i: str(v) for i, v in bounds.items()},
        "bad_level": bad_level,
    })


if __name__ == "__main__":
    main()
