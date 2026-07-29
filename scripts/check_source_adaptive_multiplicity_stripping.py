#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


NEIGH = {
    "a": {"u", "v", "w", "x"},
    "b": {"u", "v", "y"},
    "c": {"u", "w", "z"},
    "d": {"x", "y", "z"},
}


def multiplicities():
    targets = set().union(*NEIGH.values())
    return {y: sum(y in ns for ns in NEIGH.values()) for y in targets}


def kernel_load(thresholds):
    m = multiplicities()
    cols = {y: Fraction(0) for y in m}
    retained = {}
    for x, ns in NEIGH.items():
        keep = sorted(y for y in ns if m[y] <= thresholds[x])
        if not keep:
            return None, None, None
        retained[x] = keep
        for y in keep:
            cols[y] += Fraction(1, len(keep))
    return max(cols.values()), cols, retained


def main():
    m = multiplicities()
    levels = sorted(set(m.values()))

    global_best = None
    global_choice = None
    for h in levels:
        val, _, _ = kernel_load({x: h for x in NEIGH})
        if val is not None and (global_best is None or val < global_best):
            global_best, global_choice = val, h

    adaptive_best = None
    adaptive_choice = None
    checked = 0
    for vals in product(levels, repeat=len(NEIGH)):
        checked += 1
        thresholds = dict(zip(NEIGH, vals))
        val, cols, retained = kernel_load(thresholds)
        if val is None:
            continue
        direct = max(
            sum(
                Fraction(1, len(retained[x]))
                for x in NEIGH
                if y in retained[x]
            )
            for y in m
        )
        assert val == direct
        if adaptive_best is None or val < adaptive_best:
            adaptive_best = val
            adaptive_choice = thresholds.copy()

    assert adaptive_best <= global_best
    assert adaptive_best < global_best

    print({
        "all_checks_passed": True,
        "assignments_checked": checked,
        "multiplicities": m,
        "best_global_load": str(global_best),
        "best_global_threshold": global_choice,
        "best_adaptive_load": str(adaptive_best),
        "best_adaptive_thresholds": adaptive_choice,
    })


if __name__ == "__main__":
    main()
