#!/usr/bin/env python3
from fractions import Fraction as F

def primal(s):
    if s <= F(1, 2):
        return (F(1) - s, F(1) - s, s)
    return (F(1, 2), F(1, 2), F(1, 2))

def dual(s):
    if s < F(1, 2):
        return (F(0), F(1), F(1), F(1))
    return (F(1, 2), F(1, 2), F(1, 2), F(0))

def check(s):
    x1, x2, x3 = primal(s)
    y12, y23, y13, z = dual(s)
    assert min(x1, x2, x3) >= 0
    assert x3 <= s
    assert x1 + x2 >= 1
    assert x2 + x3 >= 1
    assert x1 + x3 >= 1
    assert y12 >= 0 and y23 >= 0 and y13 >= 0 and z >= 0
    assert y12 + y13 <= 1
    assert y12 + y23 <= 1
    assert y13 + y23 - z <= 1
    primal_value = x1 + x2 + x3
    dual_value = y12 + y23 + y13 - s * z
    assert primal_value == dual_value
    expected = F(2) - s if s <= F(1, 2) else F(3, 2)
    assert primal_value == expected
    return primal_value, z

samples = {}
for k in range(101):
    s = F(k, 100)
    value, cap_price = check(s)
    samples[s] = (value, cap_price)

assert samples[F(49, 100)] == (F(151, 100), F(1))
assert samples[F(1, 2)][0] == F(3, 2)
assert samples[F(51, 100)] == (F(3, 2), F(0))

left_slope = (samples[F(1, 2)][0] - samples[F(49, 100)][0]) / F(1, 100)
right_slope = (samples[F(51, 100)][0] - samples[F(1, 2)][0]) / F(1, 100)
assert left_slope == -1
assert right_slope == 0

trial = (F(1), F(0), F(0))
residuals = {
    "12": F(1) - (trial[0] + trial[1]),
    "23": F(1) - (trial[1] + trial[2]),
    "13": F(1) - (trial[0] + trial[2]),
}
assert residuals == {"12": F(0), "23": F(1), "13": F(0)}

print({
    "cap_samples": len(samples),
    "breakpoint": "1/2",
    "left_formula": "(1-s,1-s,s), value 2-s",
    "right_formula": "(1/2,1/2,1/2), value 3/2",
    "one_sided_value_slopes": [str(left_slope), str(right_slope)],
    "cap_dual_prices": ["1 below breakpoint", "0 above breakpoint"],
    "trial_violating_cycle": "23",
})
