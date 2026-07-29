#!/usr/bin/env python3
"""Finite audit for AC3vl--AC3vp."""

from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd, lcm
import random

SEED = 20260728


def rank_q(rows):
    matrix = [[Fraction(value) for value in row] for row in rows]
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    rank = 0
    column = 0
    while rank < m and column < n:
        pivot = next((i for i in range(rank, m) if matrix[i][column]), None)
        if pivot is None:
            column += 1
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for i in range(m):
            if i == rank or not matrix[i][column]:
                continue
            factor = matrix[i][column]
            matrix[i] = [matrix[i][j] - factor * matrix[rank][j] for j in range(n)]
        rank += 1
        column += 1
    return rank


def clear_row(row):
    denominator = 1
    for value in row:
        denominator = lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in row]
    common = reduce(gcd, (abs(value) for value in integers), 0)
    if common:
        integers = [value // common for value in integers]
        denominator //= common
    first = next((value for value in integers if value), 0)
    if first < 0:
        integers = [-value for value in integers]
    return tuple(integers)


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector))


def states_from(start, increments):
    states = [tuple(start)]
    current = list(start)
    for vector in increments:
        current = [current[i] + vector[i] for i in range(len(current))]
        states.append(tuple(current))
    return states


def audit_case(rows, increments, states, lower, upper, p_bound, counters):
    q = len(states[0])
    assert states[0] == states[-1]
    assert all(all(value >= 0 for value in state) for state in states)
    assert rows

    balances = [[dot(row, state) for state in states] for row in rows]
    stock = 1
    for h, row in enumerate(rows):
        deltas = [dot(row, vector) for vector in increments]
        assert all(balances[h][j + 1] == balances[h][j] + deltas[j] for j in range(len(increments)))
        assert sum(deltas) == 0
        b_h = max(abs(value) for value in deltas)
        lower_position, lower_threshold = lower[h]
        upper_position, upper_threshold = upper[h]
        assert balances[h][lower_position] >= lower_threshold
        assert balances[h][upper_position] <= upper_threshold
        lo = lower_threshold - p_bound * b_h
        hi = upper_threshold + p_bound * b_h
        assert all(lo <= value <= hi for value in balances[h])
        width = hi - lo + 1
        assert 0 <= balances[h][0] - lo < width
        stock *= width
        counters["lifted_balances"] += 1

    rank = rank_q(rows)
    assert 1 <= rank <= q
    assert q - rank < q
    if rank == q:
        counters["full_rank_cases"] += 1
    else:
        counters["kernel_reduction_cases"] += 1
    counters["kernel_dimensions"] += q - rank
    counters["decoration_stock"] += stock
    counters["cases"] += 1


def exhaustive_one_dimension(counters):
    for length in range(1, 7):
        for values in product(range(-2, 3), repeat=length):
            if sum(values) != 0:
                continue
            increments = [(value,) for value in values]
            prefix = 0
            minimum = 0
            for value in values:
                prefix += value
                minimum = min(minimum, prefix)
            for extra in range(3):
                states = states_from((-minimum + extra,), increments)
                for alpha in range(-3, 4):
                    if alpha == 0:
                        continue
                    row = (alpha,)
                    balance = [dot(row, state) for state in states]
                    for lower_position in range(length):
                        upper_position = (lower_position + length // 2) % length
                        lower = {0: (lower_position, balance[lower_position] - 2)}
                        upper = {0: (upper_position, balance[upper_position] + 2)}
                        audit_case([row], increments, states, lower, upper, length, counters)


def random_closed_walk(rng, q, length):
    increments = [[0] * q for _ in range(length)]
    for coordinate in range(q):
        for _ in range(rng.randint(1, max(1, length // 2))):
            a = rng.randrange(length)
            b = rng.randrange(length)
            value = rng.randint(1, 3)
            increments[a][coordinate] += value
            increments[b][coordinate] -= value
    return [tuple(vector) for vector in increments]


def randomized_multidimensional(counters):
    rng = random.Random(SEED)
    for _ in range(30000):
        q = rng.randint(2, 5)
        length = rng.randint(2, 8)
        increments = random_closed_walk(rng, q, length)
        prefix = [0] * q
        minimum = [0] * q
        for vector in increments:
            prefix = [prefix[i] + vector[i] for i in range(q)]
            minimum = [min(minimum[i], prefix[i]) for i in range(q)]
        start = tuple(-minimum[i] + rng.randint(0, 5) for i in range(q))
        states = states_from(start, increments)

        rational_rows = []
        while len(rational_rows) < rng.randint(1, q + 2):
            row = tuple(Fraction(rng.randint(-4, 4), rng.randint(1, 4)) for _ in range(q))
            if any(row):
                rational_rows.append(row)
        rows = []
        for row in rational_rows:
            cleared = clear_row(row)
            if any(cleared) and cleared not in rows:
                rows.append(cleared)
        if not rows or rank_q(rows) == 0:
            continue

        lower = {}
        upper = {}
        for h, row in enumerate(rows):
            balance = [dot(row, state) for state in states]
            lower_position = rng.randrange(length)
            upper_position = rng.randrange(length)
            lower[h] = (lower_position, balance[lower_position] - rng.randint(0, 5))
            upper[h] = (upper_position, balance[upper_position] + rng.randint(0, 5))
        audit_case(rows, increments, states, lower, upper, length + rng.randint(0, 3), counters)


def main():
    counters = {
        "cases": 0,
        "lifted_balances": 0,
        "full_rank_cases": 0,
        "kernel_reduction_cases": 0,
        "kernel_dimensions": 0,
        "decoration_stock": 0,
    }
    exhaustive_one_dimension(counters)
    randomized_multidimensional(counters)
    print("AC recurrent linear-balance lift audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
