#!/usr/bin/env python3
"""Price the retained-source reservoir needed for two anchors per unary run."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import factorial

N = 30
BINARY = 9
UNARY = 11

dp = [[{False: defaultdict(int), True: defaultdict(int)} for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][0][False][0] = 1
for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for child_root_unary, distribution in dp[size - 1][binary].items():
            for runs, count in distribution.items():
                dp[size][binary][True][runs + (0 if child_root_unary else 1)] += count
        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for _, left_distribution in dp[left_size][left_binary].items():
                        for left_runs, left_count in left_distribution.items():
                            for _, right_distribution in dp[right_size][right_binary].items():
                                for right_runs, right_count in right_distribution.items():
                                    dp[size][binary][False][left_runs + right_runs] += left_count * right_count

histogram = defaultdict(int)
for distribution in dp[N][BINARY].values():
    for runs, count in distribution.items():
        histogram[runs] += count
histogram = dict(sorted(histogram.items()))
expected_histogram = {
    1: 92378, 2: 8314020, 3: 212007510, 4: 2261413440,
    5: 11872420560, 6: 33242777568, 7: 51447155760,
    8: 44097562080, 9: 20211382620, 10: 4491418360,
    11: 367479684,
}
assert histogram == expected_histogram
family = sum(histogram.values())
formula = factorial(N - 1) // (factorial(UNARY) * factorial(BINARY) * factorial(BINARY + 1))
assert family == formula == 168212023980
aggregate_runs = sum(runs * count for runs, count in histogram.items())
aggregate_anchors = 2 * aggregate_runs
aggregate_blockers = UNARY * family
assert aggregate_runs == 1212286655580
assert aggregate_anchors == 2424573311160
assert aggregate_blockers == 1850332263780
assert Fraction(aggregate_runs, family) == Fraction(209, 29)
assert Fraction(aggregate_anchors, family) == Fraction(418, 29)
assert Fraction(aggregate_blockers, aggregate_anchors) == Fraction(29, 38)

print({
    "profile": {"encoded_size": N, "binary_nodes": BINARY, "unary_nodes": UNARY},
    "maximal_unary_run_histogram": histogram,
    "family_size": family,
    "aggregate_runs": aggregate_runs,
    "mean_runs": str(Fraction(aggregate_runs, family)),
    "two_anchors_per_run_aggregate": aggregate_anchors,
    "mean_retained_anchor_reservoir": str(Fraction(aggregate_anchors, family)),
    "maximum_retained_anchor_reservoir": 22,
    "aggregate_anchor_pair_blockers": aggregate_blockers,
    "blockers_per_reserved_anchor": str(Fraction(aggregate_blockers, aggregate_anchors)),
    "remaining_gap": "the required retained source cells have not been identified in the prime-patching geometry",
    "evidence_level": "exact_retained_anchor_reservoir_price",
    "status": "passed",
})
