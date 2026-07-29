#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# min x1+x2+x3 s.t. x1+x2>=a, x2+x3>=b, x1+x3>=c, x>=0.
# Dual vertices yield value max(a,b,c,(a+b+c)/2).


def solve(a, b, c):
    half = (a + b + c) / 2
    vals = (a, b, c, half)
    v = max(vals)
    if v == half and half >= a and half >= b and half >= c:
        x1 = (a + c - b) / 2
        x2 = (a + b - c) / 2
        x3 = (b + c - a) / 2
        chamber = "central"
        y = (Fraction(1, 2),) * 3
    elif v == a:
        x1, x2, x3 = c, a - c, Fraction(0)
        chamber = "a"
        y = (Fraction(1), Fraction(0), Fraction(0))
    elif v == b:
        x1, x2, x3 = Fraction(0), a, b - a
        chamber = "b"
        y = (Fraction(0), Fraction(1), Fraction(0))
    else:
        x1, x2, x3 = a, Fraction(0), c - a
        chamber = "c"
        y = (Fraction(0), Fraction(0), Fraction(1))
    assert min(x1, x2, x3) >= 0
    assert x1 + x2 >= a and x2 + x3 >= b and x1 + x3 >= c
    assert x1 + x2 + x3 == v
    dual = a * y[0] + b * y[1] + c * y[2]
    assert dual == v
    return v, (x1, x2, x3), y, chamber


hist = {"central": 0, "a": 0, "b": 0, "c": 0}
for ia, ib, ic in product(range(11), repeat=3):
    a, b, c = map(lambda z: Fraction(z, 5), (ia, ib, ic))
    v, x, y, ch = solve(a, b, c)
    assert v == max(a, b, c, (a + b + c) / 2)
    hist[ch] += 1

# Exact path (a,b,c)=(1+2t,1,1), crossing at t=1/2.
path = []
for k in range(101):
    t = Fraction(k, 100)
    v, x, y, ch = solve(1 + 2 * t, Fraction(1), Fraction(1))
    expected = Fraction(3, 2) + t if t <= Fraction(1, 2) else 1 + 2 * t
    assert v == expected
    path.append(ch)
assert path[49] == "central" and path[51] == "a"

print({
    "grid_points": 11 ** 3,
    "chamber_histogram": hist,
    "path_breakpoint": Fraction(1, 2),
    "central_gradient": (Fraction(1, 2),) * 3,
    "dominant_a_gradient": (Fraction(1), Fraction(0), Fraction(0)),
})
