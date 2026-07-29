#!/usr/bin/env python3
from fractions import Fraction as F

# Three simple cycles of a tiny shell graph.
cycles = {
    "C01": {"length": 2, "product": F(1, 4), "exponent": -2},
    "C02": {"length": 2, "product": F(1, 4), "exponent": -2},
    "C0": {"length": 1, "product": F(2, 5), "exponent": 0},
}

# The tied active face C01=C02 descends as x^{-1}; the self-loop is stationary.
active = ("C01", "C02")
assert all(F(cycles[name]["exponent"], cycles[name]["length"]) == -1 for name in active)

# Cross-power equality against C0 gives x^2=25/16, hence x=5/4.
breakpoint_squared = cycles["C01"]["product"] / cycles["C0"]["product"] ** 2
assert breakpoint_squared == F(25, 16)
breakpoint = F(5, 4)
assert breakpoint * breakpoint == breakpoint_squared


def compare_at(x):
    # Compare squared rates, avoiding radicals.
    active_squared = cycles["C01"]["product"] * x ** cycles["C01"]["exponent"]
    loop_squared = cycles["C0"]["product"] ** 2
    if active_squared > loop_squared:
        return ("C01", "C02")
    if active_squared == loop_squared:
        return ("C01", "C02", "C0")
    return ("C0",)

assert compare_at(F(6, 5)) == ("C01", "C02")
assert compare_at(breakpoint) == ("C01", "C02", "C0")
assert compare_at(F(13, 10)) == ("C0",)

points_checked = 0
for i in range(101):
    x = F(1, 1) + F(i, 200)  # [1,3/2]
    active_set = compare_at(x)
    if x < breakpoint:
        assert active_set == ("C01", "C02")
    elif x == breakpoint:
        assert active_set == ("C01", "C02", "C0")
    else:
        assert active_set == ("C0",)
    points_checked += 1

print({
    "initial_active_cycles": list(active),
    "face_slope": "-1",
    "next_breakpoint": str(breakpoint),
    "breakpoint_polynomial": "16*x^2-25",
    "active_at_breakpoint": list(compare_at(breakpoint)),
    "rational_points_checked": points_checked,
})
