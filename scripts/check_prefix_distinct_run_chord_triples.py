#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from math import factorial

N = 30
J = 9


def profile_count(size, binary):
    unary = size - 1 - 2 * binary
    if unary < 0:
        return 0
    return factorial(size - 1) // (
        factorial(unary) * factorial(binary) * factorial(binary + 1)
    )


def choose_two(value):
    return value * (value - 1) // 2


# dp[size][binary][top_unary_run] = [count, guaranteed within-run collinear triples].
# top_unary_run=0 means the root is not unary.
dp = [[defaultdict(lambda: [0, 0]) for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][0][0] = [1, 0]

for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        # Add a unary root. Extending a run of length k to k+1 creates C(k,2)
        # new triples containing the new distinct point.
        for top_run, (count, total) in tuple(dp[size - 1][binary].items()):
            next_run = top_run + 1 if top_run else 1
            increment = choose_two(top_run) if top_run else 0
            record = dp[size][binary][next_run]
            record[0] += count
            record[1] += total + increment * count

        # Add a binary root. Maximal unary runs remain inside the two children.
        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_run, (left_count, left_total) in dp[left_size][left_binary].items():
                        for right_run, (right_count, right_total) in dp[right_size][right_binary].items():
                            record = dp[size][binary][0]
                            record[0] += left_count * right_count
                            record[1] += left_total * right_count + right_total * left_count

family = sum(record[0] for record in dp[N][J].values())
aggregate = sum(record[1] for record in dp[N][J].values())

assert family == profile_count(N, J) == 168212023980
assert aggregate == 396499770810
assert Fraction(aggregate, family) == Fraction(33, 14)

print(
    {
        "profile": {"encoded_size": N, "encoded_binary_nodes": J},
        "family_size": family,
        "distinct_run_point_model": "index maximal unary runs; place the k nodes of each run at distinct integer points on one run-specific vertical line",
        "guaranteed_collinear_triples": "sum over maximal unary runs of C(run_length,3)",
        "aggregate_guaranteed_triples": aggregate,
        "mean_guaranteed_triples": str(Fraction(aggregate, family)),
        "coincident_cells_removed": True,
        "remaining_gap": "the run-specific vertical lines are an encoding geometry, not source-derived prime-patching support chords; cross-run incidences are not charged",
        "evidence_level": "distinct_ancestry_run_collinearity_census",
        "status": "passed",
    }
)
