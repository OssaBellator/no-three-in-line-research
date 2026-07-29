#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

nodes = (0, 1, 2)
edges = ((0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2))
edge_index = {edge: i for i, edge in enumerate(edges)}
cycles = [
    ((0, 1), (1, 0)),
    ((1, 2), (2, 1)),
    ((2, 0), (0, 2)),
    ((0, 1), (1, 2), (2, 0)),
    ((0, 2), (2, 1), (1, 0)),
]
edge_excess = [F(1, 2)] * len(edges)
edge_cost = [F(1)] * len(edges)

rows = []
right_hand_sides = []
for cycle in cycles:
    row = [F(0)] * len(edges)
    for edge in cycle:
        row[edge_index[edge]] += 1
    rows.append(row)
    right_hand_sides.append(F(len(cycle), 2))

def solve_linear(matrix, vector):
    n = len(matrix)
    augmented = [list(row) + [vector[i]] for i, row in enumerate(matrix)]
    row = 0
    for column in range(n):
        pivot = next((i for i in range(row, n) if augmented[i][column] != 0), None)
        if pivot is None:
            return None
        augmented[row], augmented[pivot] = augmented[pivot], augmented[row]
        scale = augmented[row][column]
        augmented[row] = [value / scale for value in augmented[row]]
        for i in range(n):
            if i != row and augmented[i][column] != 0:
                factor = augmented[i][column]
                augmented[i] = [
                    augmented[i][j] - factor * augmented[row][j]
                    for j in range(n + 1)
                ]
        row += 1
    return [augmented[i][-1] for i in range(n)]

def restricted_optimum(active_cycles):
    constraints = []
    for i in active_cycles:
        constraints.append((rows[i], right_hand_sides[i]))
    for j in range(len(edges)):
        row = [F(0)] * len(edges)
        row[j] = 1
        constraints.append((row, F(0)))

    best = None
    best_x = None
    for active in combinations(range(len(constraints)), len(edges)):
        matrix = [constraints[i][0] for i in active]
        vector = [constraints[i][1] for i in active]
        x = solve_linear(matrix, vector)
        if x is None or any(value < 0 for value in x):
            continue
        if any(
            sum(rows[i][j] * x[j] for j in range(len(edges))) < right_hand_sides[i]
            for i in active_cycles
        ):
            continue
        objective = sum(edge_cost[j] * x[j] for j in range(len(edges)))
        if best is None or objective < best:
            best = objective
            best_x = x
    assert best is not None
    return best, best_x

def cycle_residual(cycle_index, attenuation):
    return right_hand_sides[cycle_index] - sum(
        rows[cycle_index][j] * attenuation[j] for j in range(len(edges))
    )

def max_mean_residual(attenuation):
    values = []
    for i, cycle in enumerate(cycles):
        residual_sum = cycle_residual(i, attenuation)
        values.append((residual_sum / len(cycle), i, residual_sum))
    return max(values)

restricted_cycles = [0, 1, 2]
restricted_cost, restricted_x = restricted_optimum(restricted_cycles)
assert restricted_cost == 3
mean, violated_cycle, residual_sum = max_mean_residual(restricted_x)
assert violated_cycle == 3 and mean == F(1, 2) and residual_sum == F(3, 2)

restricted_cycles.append(violated_cycle)
full_cost, full_x = restricted_optimum(restricted_cycles)
assert full_cost == 3
assert max_mean_residual(full_x)[0] == 0
assert all(cycle_residual(i, full_x) <= 0 for i in range(len(cycles)))

flow = [F(1)] * len(edges)
for node in nodes:
    outgoing = sum(flow[i] for i, (u, _) in enumerate(edges) if u == node)
    incoming = sum(flow[i] for i, (_, v) in enumerate(edges) if v == node)
    assert outgoing == incoming
assert all(flow[i] <= edge_cost[i] for i in range(len(edges)))
dual_value = sum(edge_excess[i] * flow[i] for i in range(len(edges)))
assert dual_value == full_cost == 3

print({
    "simple_cycles": len(cycles),
    "restricted_cycle_count": 3,
    "restricted_cost": str(restricted_cost),
    "violated_cycle": cycles[violated_cycle],
    "violation_sum": str(residual_sum),
    "violation_mean": str(mean),
    "final_cost": str(full_cost),
    "final_attenuation": [str(x) for x in full_x],
    "compact_circulation_value": str(dual_value),
})
