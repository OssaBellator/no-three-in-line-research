#!/usr/bin/env python3
from fractions import Fraction

MAX_N = 2000
PHASE_MODULUS = 3
ROW_BOUND = Fraction(7, 120)


def representation(n, phase):
    """Return the lexicographically least phase-locked (a,b) with 4a+7b=n."""
    candidates = []
    for b in range(phase, n // 7 + 1, PHASE_MODULUS):
        remaining = n - 7 * b
        if remaining >= 0 and remaining % 4 == 0:
            candidates.append((remaining // 4, b))
    return min(candidates) if candidates else None


def boundary_loss(a, b):
    # Exact local block signatures: P contributes 1/30 per unit length,
    # Q contributes 1/20 per unit length, and one seam costs one unit/N.
    n = 4 * a + 7 * b
    action_p = 4 * a
    action_q = 7 * b
    return (Fraction(action_p, 30) + Fraction(action_q, 20) + 1) / n


thresholds = []
for phase in range(PHASE_MODULUS):
    missing = [n for n in range(MAX_N + 1) if representation(n, phase) is None]
    threshold = max(missing) + 1
    thresholds.append(threshold)
    assert all(representation(n, phase) is not None for n in range(threshold, MAX_N + 1))
    # Adding a four-block preserves the phase, so the finite threshold certifies all later lengths.
    assert representation(threshold, phase) is not None

assert thresholds == [60, 67, 74]

certificates = 0
for n in range(74, MAX_N + 1):
    for phase in range(PHASE_MODULUS):
        a, b = representation(n, phase)
        assert 4 * a + 7 * b == n
        assert b % PHASE_MODULUS == phase
        # Additive block signature and controller balance.
        action = (4 * a, 7 * b)
        assert sum(action) == n
        assert boundary_loss(a, b) <= Fraction(1, 20) + Fraction(1, n)
        if n >= 120:
            assert boundary_loss(a, b) <= ROW_BOUND
        certificates += 1

print({
    "phase_thresholds": thresholds,
    "uniform_phase_threshold": max(thresholds),
    "derived_boundary_row_from": 120,
    "derived_boundary_row": str(ROW_BOUND),
    "certificates_checked": certificates,
    "status": "passed",
})
