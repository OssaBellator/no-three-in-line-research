#!/usr/bin/env python3
from fractions import Fraction

WEIGHTS = (28, 27, 20, 15, 12, 18)
DENOMINATOR = 120
BASE_LOSS = Fraction(7, 30)
MARGIN = Fraction(1, 4)


def marker_witness(n, phase):
    for b in range(phase, n // 7 + 1, 3):
        remainder = n - 7 * b
        if remainder >= 0 and remainder % 4 == 0:
            return remainder // 4, b
    return None


def largest_remainder_counts(n):
    raw = [Fraction(n * weight, DENOMINATOR) for weight in WEIGHTS]
    floors = [value.numerator // value.denominator for value in raw]
    missing = n - sum(floors)
    order = sorted(range(len(raw)), key=lambda i: (raw[i] - floors[i], -i), reverse=True)
    counts = floors[:]
    for i in order[:missing]:
        counts[i] += 1
    return tuple(counts)

return_word = "AAAAABA"
assert len(return_word) == 7
assert "BB" not in return_word
assert return_word.count("A") == 6 and return_word.count("B") == 1
hall_contraction = (Fraction(1, 2) ** 6 * Fraction(3, 4)) ** 2
assert hall_contraction == Fraction(9, 65536) < Fraction(1, 100)

checked = 0
for n in range(361, 5001):
    phase = n % 3
    witness = marker_witness(n, phase)
    assert witness is not None
    a, b = witness
    assert 4 * a + 7 * b == n
    assert b % 3 == phase

    counts = largest_remainder_counts(n)
    assert sum(counts) == n
    errors = [abs(Fraction(counts[i]) - Fraction(n * WEIGHTS[i], DENOMINATOR)) for i in range(6)]
    assert all(error < 1 for error in errors)

    implementation_penalty = sum(errors, Fraction(0)) / n
    assert implementation_penalty < Fraction(6, n)
    assert BASE_LOSS + implementation_penalty < MARGIN

    combined_residue = n % 24
    assert combined_residue % 3 == n % 3
    assert combined_residue % 8 == n % 8
    assert combined_residue % 12 == n % 12
    assert combined_residue % 2 == n % 2
    checked += 1

print({
    "length_interval": [361, 5000],
    "lengths_checked": checked,
    "marker_uniform_threshold": 74,
    "rounding_uniform_threshold": 361,
    "combined_period": 24,
    "hall_two_cycle_contraction": str(hall_contraction),
    "base_loss": str(BASE_LOSS),
    "global_margin": str(MARGIN),
    "status": "passed",
})
