#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

blocks = [
    [
        (0, (F(1), F(7, 10))),
        (1, (F(1, 5), F(7, 10))),
        (2, (F(1, 20), F(2, 5))),
    ],
    [
        (0, (F(7, 10), F(1))),
        (1, (F(7, 10), F(1, 5))),
        (2, (F(2, 5), F(1, 20))),
    ],
    [
        (0, (F(1, 2), F(1, 2))),
        (1, (F(1, 10), F(1, 10))),
    ],
]

def dominates(x, y):
    return x[0] <= y[0] and x[1] <= y[1]

def nondominated(items):
    best_by_error = {}
    for error, witness in items:
        best_by_error.setdefault(error, witness)
    unique = [(error, witness) for error, witness in best_by_error.items()]
    output = []
    for error, witness in unique:
        if any(other != error and dominates(other, error) for other, _ in unique):
            continue
        output.append((error, witness))
    return sorted(output)

block_frontiers = []
for block_index, block in enumerate(blocks):
    max_budget = max(cost for cost, _ in block)
    by_budget = {}
    for budget in range(max_budget + 1):
        by_budget[budget] = nondominated([
            (error, (block_index, option_index))
            for option_index, (cost, error) in enumerate(block)
            if cost <= budget
        ])
    block_frontiers.append(by_budget)

combined = {0: [((F(0), F(0)), tuple())]}
for block_index, by_budget in enumerate(block_frontiers):
    next_combined = {}
    max_previous = max(combined)
    max_block = max(by_budget)
    for total_budget in range(max_previous + max_block + 1):
        candidates = []
        for previous_budget, previous_frontier in combined.items():
            block_budget = total_budget - previous_budget
            if block_budget not in by_budget:
                continue
            for previous_error, previous_witness in previous_frontier:
                for block_error, block_witness in by_budget[block_budget]:
                    error = (
                        previous_error[0] + block_error[0],
                        previous_error[1] + block_error[1],
                    )
                    candidates.append((error, previous_witness + (block_witness,)))
        if candidates:
            next_combined[total_budget] = nondominated(candidates)
    combined = next_combined

brute = []
for choices in product(*[range(len(block)) for block in blocks]):
    cost = sum(blocks[i][choice][0] for i, choice in enumerate(choices))
    error = (
        sum(blocks[i][choice][1][0] for i, choice in enumerate(choices)),
        sum(blocks[i][choice][1][1] for i, choice in enumerate(choices)),
    )
    brute.append((cost, error, choices))

for budget, frontier in combined.items():
    brute_frontier = nondominated([
        (error, choices) for cost, error, choices in brute if cost <= budget
    ])
    assert [error for error, _ in frontier] == [error for error, _ in brute_frontier]

expected_sizes = {0: 1, 1: 3, 2: 3, 3: 3, 4: 2, 5: 1}
assert {budget: len(frontier) for budget, frontier in combined.items()} == expected_sizes

tolerance = (F(1), F(1))
feasible_budget = min(
    budget
    for budget, frontier in combined.items()
    if any(dominates(error, tolerance) for error, _ in frontier)
)
assert feasible_budget == 3
feasible = [
    (error, witness)
    for error, witness in combined[feasible_budget]
    if dominates(error, tolerance)
]
assert len(feasible) == 1 and feasible[0][0] == tolerance
assert not any(dominates(error, tolerance) for error, _ in combined[2])

print({
    "independent_blocks": len(blocks),
    "raw_plan_count": len(brute),
    "frontier_sizes_by_budget": expected_sizes,
    "minimum_tolerance_budget": feasible_budget,
    "unique_feasible_error": [str(x) for x in feasible[0][0]],
    "reconstructed_block_choices": feasible[0][1],
    "budget_two_obstruction": [[str(x) for x in error] for error, _ in combined[2]],
})
