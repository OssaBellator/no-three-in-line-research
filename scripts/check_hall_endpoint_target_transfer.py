#!/usr/bin/env python3
from fractions import Fraction
import json

N = {
    "x0": ("a", "b", "c"),
    "x1": ("a", "b", "d"),
    "x2": ("a", "e", "f"),
}
mu = {"x0": Fraction(1, 2), "x1": Fraction(1, 3), "x2": Fraction(1, 6)}
mult = {y: sum(y in ys for ys in N.values()) for y in {z for ys in N.values() for z in ys}}
r0 = {x: sum(Fraction(mult[y], len(ys)) for y in ys) for x, ys in N.items()}
assert r0 == {"x0": Fraction(2), "x1": Fraction(2), "x2": Fraction(5, 3)}
expect = sum(mu[x] * r0[x] for x in N)

theta = Fraction(3, 2)
phi = Fraction(1)
H = [x for x in N if r0[x] > theta]
p = sum(mu[x] for x in H)
assert p == 1
M = max(mult.values())

nu_all = {}
for x in H:
    for y in N[x]:
        nu_all[y] = nu_all.get(y, Fraction(0)) + mu[x] * Fraction(1, len(N[x]))

mass_high_target = sum(w for y, w in nu_all.items() if mult[y] > phi)
bound = p * Fraction(theta - phi, M - phi)
assert mass_high_target >= bound
nu = {y: w for y, w in nu_all.items() if mult[y] > phi}
m = sum(nu.values())
chi = sum(w*w for w in nu.values())
beta = max(nu.values())
support = len(nu)
assert Fraction(support) >= m*m/chi
assert Fraction(support) >= m/beta
assert any(mult[y] > theta for y in nu)

print(json.dumps({
    "all_checks_passed": True,
    "raw_ratios": {k: str(v) for k, v in r0.items()},
    "endpoint_expectation": str(expect),
    "high_endpoint_mass": str(p),
    "high_target_mass": str(mass_high_target),
    "threshold_bound": str(bound),
    "target_collision_energy": str(chi),
    "maximum_target_atom": str(beta),
    "distinct_high_targets": support,
}, indent=2))
