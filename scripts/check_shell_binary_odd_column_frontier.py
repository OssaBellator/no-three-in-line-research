#!/usr/bin/env python3

RECORDED = ((1, 0, 1), (1, 1, 0), (0, 1, 1))
TARGET = (12, 10, 8)
ODD_BINARY_COLUMNS = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))

def add_scaled(coefficients, columns):
    return tuple(sum(coefficient * column[index] for coefficient, column in zip(coefficients, columns)) for index in range(3))

def solutions(new_column):
    result = []
    for uses in range(1, 31):
        for first in range(31):
            for second in range(31):
                for third in range(31):
                    coefficients = (first, second, third, uses)
                    if add_scaled(coefficients, RECORDED + (new_column,)) == TARGET:
                        result.append((sum(coefficients), uses, first, second, third))
    return tuple(sorted(result))

frontiers = {}
for column in ODD_BINARY_COLUMNS:
    records = solutions(column)
    assert records
    pairs = sorted({(record[1], record[0]) for record in records})
    pareto = tuple(pair for pair in pairs if not any(other[0] <= pair[0] and other[1] <= pair[1] and other != pair for other in pairs))
    frontiers[column] = (records[0], pareto)

assert frontiers[(1, 0, 0)][0] == (16, 2, 4, 6, 4)
assert frontiers[(0, 1, 0)][0] == (16, 2, 6, 6, 2)
assert frontiers[(0, 0, 1)][0] == (16, 2, 4, 8, 2)
assert frontiers[(1, 1, 1)][0] == (12, 6, 2, 4, 0)
assert tuple((record[1], record[0]) for record in solutions((1, 1, 1))) == ((6, 12), (4, 13), (2, 14))

A, B, _ = RECORDED
D = (1, 1, 1)
determinant = (
    A[0] * (B[1] * D[2] - B[2] * D[1])
    - B[0] * (A[1] * D[2] - A[2] * D[1])
    + D[0] * (A[1] * B[2] - A[2] * B[1])
)
assert abs(determinant) == 1

print({
    "binary_odd_columns_checked": ODD_BINARY_COLUMNS,
    "unit_column_minimum_active_controls": 16,
    "symmetric_column": D,
    "symmetric_column_solution_frontier": ((2, 14), (4, 13), (6, 12)),
    "symmetric_column_minimum_active_controls": 12,
    "recorded_baseline_active_controls": 15,
    "maximum_unit_cost_throughput_improvement": 3,
    "completed_lattice_determinant": abs(determinant),
    "remaining_gap": "the throughput-improving all-cycles action (1,1,1) has no geometric clean-macro realization or audited buffer cost",
    "evidence_level": "exact_binary_odd_column_service_frontier",
    "status": "passed",
})
