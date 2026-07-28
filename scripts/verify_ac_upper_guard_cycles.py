#!/usr/bin/env python3
"""Finite audit for AC3vg--AC3vk."""

from itertools import product
import random

SEED = 20260728


def states_from(start, increments):
    states = [tuple(start)]
    current = list(start)
    for vector in increments:
        current = [current[i] + vector[i] for i in range(len(current))]
        states.append(tuple(current))
    return states


def audit_case(increments, states, guards, p_bound, counters):
    q = len(states[0])
    assert states[0] == states[-1]
    assert all(all(x >= 0 for x in state) for state in states)
    b = [max(abs(vector[i]) for vector in increments) for i in range(q)]
    guarded = sorted(guards)
    assert guarded

    stock = 1
    for i in guarded:
        u_i = min(threshold for _, threshold in guards[i])
        assert all(states[position][i] <= threshold for position, threshold in guards[i])
        bound = u_i + p_bound * b[i]
        assert all(state[i] <= bound for state in states)
        assert 0 <= states[0][i] <= bound
        stock *= bound + 1
        counters["guarded_coordinates"] += 1

    root_index = 0
    mixed_index = 0
    for i in guarded:
        u_i = min(threshold for _, threshold in guards[i])
        width = u_i + p_bound * b[i] + 1
        mixed_index += states[0][i] * max(1, root_index + 1)
        root_index = root_index * width + states[0][i]
    assert 0 <= root_index < stock

    complement = [i for i in range(q) if i not in guards]
    if complement:
        assert len(complement) < q
        projected_sum = [sum(vector[i] for vector in increments) for i in complement]
        assert all(value == 0 for value in projected_sum)
        counters["partial_guard_cases"] += 1
    else:
        counters["fully_guarded_cases"] += 1

    counters["cases"] += 1
    counters["decoration_stock"] += stock


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
            for extra in range(4):
                start = (-minimum + extra,)
                states = states_from(start, increments)
                for position in range(length):
                    for slack in range(3):
                        guards = {0: [(position, states[position][0] + slack)]}
                        audit_case(increments, states, guards, length, counters)


def random_closed_walk(rng, q, length, step_bound):
    increments = [[0] * q for _ in range(length)]
    slots = list(range(length))
    for i in range(q):
        pair_count = rng.randint(1, max(1, length // 2))
        for _ in range(pair_count):
            a = rng.choice(slots)
            b = rng.choice(slots)
            value = rng.randint(1, step_bound)
            increments[a][i] += value
            increments[b][i] -= value
    return [tuple(vector) for vector in increments]


def randomized_multidimensional(counters):
    rng = random.Random(SEED)
    for _ in range(30000):
        q = rng.randint(2, 5)
        length = rng.randint(2, 8)
        increments = random_closed_walk(rng, q, length, 3)
        prefix = [0] * q
        minimum = [0] * q
        for vector in increments:
            prefix = [prefix[i] + vector[i] for i in range(q)]
            minimum = [min(minimum[i], prefix[i]) for i in range(q)]
        start = tuple(-minimum[i] + rng.randint(0, 5) for i in range(q))
        states = states_from(start, increments)
        guarded_count = rng.randint(1, q)
        guarded = rng.sample(range(q), guarded_count)
        guards = {}
        for i in guarded:
            rows = []
            for _ in range(rng.randint(1, 3)):
                position = rng.randrange(length)
                rows.append((position, states[position][i] + rng.randint(0, 4)))
            guards[i] = rows
        audit_case(increments, states, guards, length + rng.randint(0, 3), counters)


def main():
    counters = {
        "cases": 0,
        "guarded_coordinates": 0,
        "fully_guarded_cases": 0,
        "partial_guard_cases": 0,
        "decoration_stock": 0,
    }
    exhaustive_one_dimension(counters)
    randomized_multidimensional(counters)
    print("AC upper-guard cycle localization audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
