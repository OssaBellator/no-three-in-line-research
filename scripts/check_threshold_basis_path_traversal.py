#!/usr/bin/env python3
from fractions import Fraction as F


def solve(t):
    b1 = F(1) + t
    b2 = F(2) - t
    if b1 < b2:
        x = (F(0), b2 - b1, b1)
        basis = (1, 2)
    elif b1 > b2:
        x = (b1 - b2, F(0), b2)
        basis = (0, 2)
    else:
        x = (F(0), F(0), b1)
        basis = (2,)
    value = x[0] + x[1]
    assert value == abs(b1 - b2)
    return basis, x, value


counts = {"left": 0, "breakpoint": 0, "right": 0}
for n in range(101):
    t = F(n, 100)
    basis, x, value = solve(t)
    if t < F(1, 2):
        assert basis == (1, 2)
        counts["left"] += 1
    elif t > F(1, 2):
        assert basis == (0, 2)
        counts["right"] += 1
    else:
        counts["breakpoint"] += 1

left_basic_at_zero = (F(1), F(1))
left_derivative = (F(-2), F(1))
first_breakpoint = -left_basic_at_zero[0] / left_derivative[0]
assert first_breakpoint == F(1, 2)

y_left = (F(-1), F(1))
y_right = (F(1), F(-1))
reduced_left_nonbasic = F(1) - y_left[0]
reduced_right_nonbasic = F(1) - y_right[1]
assert reduced_left_nonbasic == reduced_right_nonbasic == F(2)

print({
    "path_points_checked": 101,
    "region_counts": counts,
    "exact_breakpoint": str(first_breakpoint),
    "left_basis": [2, 3],
    "right_basis": [1, 3],
    "nonbasic_reduced_costs": [str(reduced_left_nonbasic), str(reduced_right_nonbasic)],
    "endpoint_values": [str(solve(F(0))[2]), str(solve(F(1))[2])],
})
