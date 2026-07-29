#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

cycles = {
    "C1": ({"a": 1}, F(3, 4), 1),
    "C2": ({"b": 1, "c": 1}, F(9, 16), 2),
    "C3": ({"d": 1}, F(2, 3), 1),
}
assert cycles["C1"][1] ** 2 == cycles["C2"][1]
assert cycles["C3"][1] < cycles["C1"][1]

checked = 0
for ha, hb, hc, hd in product(range(-2, 3), repeat=4):
    slope1 = F(ha)
    slope2 = F(hb + hc, 2)
    predicted = max(slope1, slope2)
    eps = F(1, 1000)
    base = F(1) + eps
    g = {"a": base ** ha, "b": base ** hb, "c": base ** hc, "d": base ** hd}
    lhs = (F(3, 4) * g["a"]) ** 2
    rhs = F(9, 16) * g["b"] * g["c"]
    if slope1 > slope2:
        assert lhs > rhs
    elif slope2 > slope1:
        assert rhs > lhs
    else:
        assert lhs == rhs
    r3 = F(2, 3) * g["d"]
    if lhs >= rhs:
        assert r3 < F(3, 4) * g["a"]
    else:
        assert r3 * r3 < rhs
    assert predicted == max(F(ha), F(hb + hc, 2))
    checked += 1

gamma = {"a": F(6, 5), "b": F(3, 2), "c": F(24, 25), "d": F(1)}
assert gamma["a"] ** 2 == gamma["b"] * gamma["c"]
assert F(3, 4) * gamma["a"] > F(2, 3) * gamma["d"]

print({
    "directions_checked": checked,
    "critical_cycles": ["C1", "C2"],
    "subgradient_extremes": {"C1": {"a": "1"}, "C2": {"b": "1/2", "c": "1/2"}},
    "face_test_gamma": {k: str(v) for k, v in gamma.items()},
})
