#!/usr/bin/env python3
"""Exact checks for docs/423 sequential marker trees."""

from fractions import Fraction
from itertools import combinations, product
import json
from math import prod


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


q = (2, 2, 2)
k = len(q)
Q = prod(q)
sources = ("s0", "s1", "s2")
leaves = tuple(product((0, 1), repeat=k))

full_targets = {(x, leaf): (x, leaf) for x in sources for leaf in leaves}
full_load = max(
    sum(Fraction(1, Q) for pair, target in full_targets.items() if target == y)
    for y in full_targets.values()
)
assert full_load == Fraction(1, 8)

safe = {
    x: tuple(leaf for leaf in leaves if leaf != (1, 1, 1))
    for x in sources
}
p = Fraction(7, 8)
safe_load = max(
    sum(
        Fraction(1, len(safe[x]))
        for x in sources
        for leaf in safe[x]
        if (x, leaf) == y
    )
    for y in ((x, leaf) for x in sources for leaf in safe[x])
)
assert safe_load == Fraction(1, 7)
assert safe_load == Fraction(1, 1) / (p * Q)


def live_children(safe_subset, level, prefix):
    values = set()
    for leaf in safe_subset:
        if leaf[: level - 1] == prefix:
            values.add(leaf[level - 1])
    return len(values)


def defect_witness(safe_subset):
    m = len(safe_subset)
    assert 0 < m < Q
    p_local = Fraction(m + 1, Q)
    for level in range(1, k + 1):
        prefixes = {leaf[: level - 1] for leaf in safe_subset}
        for prefix in prefixes:
            b = live_children(safe_subset, level, prefix)
            if b ** k < p_local * (q[level - 1] ** k):
                return level, prefix, b, p_local
    raise AssertionError("missing prefix-defect witness")


witnesses = 0
for m in range(1, Q):
    for subset in combinations(leaves, m):
        level, prefix, b, p_local = defect_witness(subset)
        assert Fraction(m, Q) < p_local
        assert b ** k < p_local * (q[level - 1] ** k)
        witnesses += 1

print(json.dumps({
    "all_checks_passed": True,
    "depth": k,
    "branching": list(q),
    "full_leaf_count": Q,
    "full_load": frac(full_load),
    "conditioned_retained_density": frac(p),
    "conditioned_load": frac(safe_load),
    "proper_safe_subtrees_checked": witnesses,
}, indent=2))
