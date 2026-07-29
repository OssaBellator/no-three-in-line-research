#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

P0 = Fraction(2, 3)
P1 = Fraction(1, 2)
RISKS = [Fraction(1, 4), Fraction(1, 5), Fraction(1, 6), Fraction(1, 8), Fraction(1, 10)]

# A leaf is (); an internal ordered binary node is (left,right).
@lru_cache(None)
def trees(leaves):
    if leaves == 1:
        return ((),)
    out = []
    for left_count in range(1, leaves):
        right_count = leaves - left_count
        for left in trees(left_count):
            for right in trees(right_count):
                out.append((left, right))
    return tuple(out)


def survivals(tree, value=Fraction(1), word=""):
    if tree == ():
        return [(word, value)]
    left, right = tree
    return survivals(left, value * P0, word + "0") + survivals(right, value * P1, word + "1")


def sorted_assignment_value(tree):
    surv = sorted(survivals(tree), key=lambda item: item[1], reverse=True)
    risks = sorted(RISKS, reverse=True)
    return max(risk / survival for risk, (_, survival) in zip(risks, surv)), surv

all_trees = trees(len(RISKS))
assert len(all_trees) == 14
best = None
best_tree = None
best_surv = None
for tree in all_trees:
    value, surv = sorted_assignment_value(tree)
    if best is None or value < best:
        best, best_tree, best_surv = value, tree, surv

assert best == Fraction(2, 3)
assert best_tree == (((), ()), (((), ()), ()))
assert [word for word, _ in best_surv] == ["00", "01", "11", "100", "101"]

# Verify the exchange principle exhaustively on every tree: the sorted assignment
# is at least as good as all 5! bijections.
permutations_checked = 0
for tree in all_trees:
    sorted_value, surv = sorted_assignment_value(tree)
    survival_values = [value for _, value in surv]
    for perm in permutations(RISKS):
        value = max(risk / survival for risk, survival in zip(perm, survival_values))
        assert sorted_value <= value
        permutations_checked += 1

print({
    "ordered_full_trees": len(all_trees),
    "assignments_checked": permutations_checked,
    "optimal_risk": str(best),
    "optimal_words": [word for word, _ in best_surv],
    "optimal_survivals": [str(value) for _, value in best_surv],
})
