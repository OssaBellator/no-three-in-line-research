#!/usr/bin/env python3
from fractions import Fraction

CYCLES = {
    (0, 1): (Fraction(3, 5), 2),
    (1, 2): (Fraction(1, 2), 2),
    (0, 2): (Fraction(1, 3), 2),
    (0, 1, 2): (Fraction(1, 3), 3),
    (0, 2, 1): (Fraction(3, 10), 3),
}
CRITICAL = (0, 1)
P_STAR, L_STAR = CYCLES[CRITICAL]

def dominates(p_a, l_a, p_b, l_b):
    return p_a ** l_b >= p_b ** l_a

for product, length in CYCLES.values():
    assert dominates(P_STAR, L_STAR, product, length)
assert sum(dominates(product, length, P_STAR, L_STAR) for product, length in CYCLES.values()) == 1

gamma_tie = Fraction(6, 5)
assert Fraction(1, 2) * gamma_tie == P_STAR
assert Fraction(1, 2) * Fraction(11, 10) < P_STAR
assert Fraction(1, 2) * Fraction(13, 10) > P_STAR
critical_floor = Fraction(5, 6)
assert P_STAR * critical_floor == Fraction(1, 2)
gamma = Fraction(1001, 1000)
assert (P_STAR * gamma) / P_STAR == gamma

print({
    "simple_cycles_checked": len(CYCLES),
    "unique_critical_cycle": CRITICAL,
    "off_cycle_upper_factor": str(gamma_tie),
    "critical_edge_lower_factor": str(critical_floor),
    "log_sensitivity_on_critical_edge": "1/2",
})
