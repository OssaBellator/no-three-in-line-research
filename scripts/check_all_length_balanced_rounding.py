#!/usr/bin/env python3
from fractions import Fraction

WEIGHTS = (28, 27, 20, 15, 12, 18)
DENOMINATOR = sum(WEIGHTS)
TARGET = tuple(Fraction(weight, DENOMINATOR) for weight in WEIGHTS)
assert DENOMINATOR == 120
assert sum(TARGET, Fraction(0)) == 1


def largest_remainder_counts(n):
    raw = [Fraction(n * weight, DENOMINATOR) for weight in WEIGHTS]
    floors = [value.numerator // value.denominator for value in raw]
    missing = n - sum(floors)
    order = sorted(range(len(raw)), key=lambda i: (raw[i] - floors[i], -i), reverse=True)
    counts = floors[:]
    for i in order[:missing]:
        counts[i] += 1
    return tuple(counts)

max_total_error = Fraction(0)
for n in range(1, 2001):
    counts = largest_remainder_counts(n)
    assert sum(counts) == n
    errors = [abs(Fraction(counts[i]) - n * TARGET[i]) for i in range(len(TARGET))]
    assert all(error < 1 for error in errors)
    total_error = sum(errors, Fraction(0))
    assert total_error < 6
    max_total_error = max(max_total_error, total_error)
    if n + DENOMINATOR <= 2001:
        later = largest_remainder_counts(n + DENOMINATOR)
        assert later == tuple(counts[i] + WEIGHTS[i] for i in range(len(WEIGHTS)))

for n in range(361, 2001):
    counts = largest_remainder_counts(n)
    penalty_bound = Fraction(6, n)
    assert penalty_bound < Fraction(1, 60)
    assert Fraction(7, 30) + penalty_bound < Fraction(1, 4)

print({
    "target_denominator": DENOMINATOR,
    "weights": WEIGHTS,
    "lengths_checked": 2000,
    "periodic_increment_verified": True,
    "max_total_rounding_error": str(max_total_error),
    "uniform_slack_threshold": 361,
    "status": "passed",
})
