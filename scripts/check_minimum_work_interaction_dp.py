#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache

J = [
    [F(1, 4), F(1, 4), F(0)],
    [F(0), F(1, 5), F(1, 5)],
    [F(1, 10), F(0), F(1, 5)],
]
C = [F(1, 20), F(1, 25), F(1, 30)]


def inverse(matrix):
    n = len(matrix)
    augmented = [
        row[:] + [F(int(i == j)) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for column in range(n):
        pivot = next(row for row in range(column, n) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in augmented]


I_minus_J = [[F(int(i == j)) - J[i][j] for j in range(3)] for i in range(3)]
R = inverse(I_minus_J)
H = [sum(R[i][j] * C[j] for j in range(3)) for i in range(3)]
assert H == [F(5, 57), F(6, 95), F(1, 19)]


def allocations(limit, count):
    if count == 0:
        yield ()
        return

    def recurse(remaining, index, prefix):
        if index == count:
            yield tuple(prefix)
            return
        for value in range(remaining + 1):
            prefix.append(value)
            yield from recurse(remaining - value, index + 1, prefix)
            prefix.pop()

    yield from recurse(limit, 0, [])


choice = {}


@lru_cache(None)
def omitted(state, budget):
    if budget == 0:
        choice[(state, budget)] = ("stop",)
        return H[state]

    best = omitted(state, budget - 1)
    best_choice = ("unused", budget - 1)
    children = [child for child in range(3) if J[state][child]]
    for allocation in allocations(budget - 1, len(children)):
        value = sum(
            J[state][child] * omitted(child, allocation[i])
            for i, child in enumerate(children)
        )
        if value < best:
            best = value
            best_choice = ("expand", tuple(zip(children, allocation)))
    choice[(state, budget)] = best_choice
    return best


curve = [omitted(0, budget) for budget in range(9)]
assert curve[:6] == [
    F(5, 57),
    F(43, 1140),
    F(23, 912),
    F(347, 22800),
    F(1103, 91200),
    F(35, 3648),
]

tolerance = F(1, 100)
minimum_budget = next(budget for budget, value in enumerate(curve) if value <= tolerance)
assert minimum_budget == 5
assert curve[4] > tolerance and curve[5] <= tolerance
assert choice[(0, 5)] == ("expand", ((0, 3), (1, 1)))

print({
    "continuation_prices": [str(x) for x in H],
    "tolerance": str(tolerance),
    "minimum_expansion_budget": minimum_budget,
    "omission_before_budget": str(curve[minimum_budget - 1]),
    "certified_omission": str(curve[minimum_budget]),
    "root_budget_allocation": [[state, budget] for state, budget in choice[(0, 5)][1]],
    "dp_states": omitted.cache_info().currsize,
})
