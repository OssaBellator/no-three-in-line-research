#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction

N = 30
J = 9
UNARY = N - 1 - 2 * J
NON_UNARY = N - UNARY

# dp[size][binary][root_is_unary][maximal_unary_runs] = count
dp = [[{False: defaultdict(int), True: defaultdict(int)} for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][0][False][0] = 1

for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for root_unary, histogram in dp[size - 1][binary].items():
            for runs, count in histogram.items():
                dp[size][binary][True][runs + (0 if root_unary else 1)] += count

        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_histogram in dp[left_size][left_binary].values():
                        for left_runs, left_count in left_histogram.items():
                            for right_histogram in dp[right_size][right_binary].values():
                                for right_runs, right_count in right_histogram.items():
                                    dp[size][binary][False][left_runs + right_runs] += left_count * right_count

run_histogram = defaultdict(int)
for histogram in dp[N][J].values():
    for runs, count in histogram.items():
        run_histogram[runs] += count

family = sum(run_histogram.values())
aggregate_runs = sum(runs * count for runs, count in run_histogram.items())
aggregate_anchor_demand = 2 * aggregate_runs
over_budget = sum(count for runs, count in run_histogram.items() if 2 * runs > NON_UNARY)

assert UNARY == 11
assert NON_UNARY == 19
assert family == 168212023980
assert aggregate_runs == 1212286655580
assert Fraction(aggregate_runs, family) == Fraction(209, 29)
assert aggregate_anchor_demand == 2424573311160
assert over_budget == 4858898044
assert Fraction(over_budget, family) == Fraction(289, 10005)
assert run_histogram[10] == 4491418360
assert run_histogram[11] == 367479684

print(
    {
        "profile": {"encoded_size": N, "binary_nodes": J, "unary_nodes": UNARY},
        "family_size": family,
        "maximal_unary_run_histogram": dict(sorted(run_histogram.items())),
        "aggregate_runs": aggregate_runs,
        "mean_runs": str(Fraction(aggregate_runs, family)),
        "aggregate_two_anchor_demand": aggregate_anchor_demand,
        "mean_two_anchor_demand": str(Fraction(aggregate_anchor_demand, family)),
        "available_non_unary_source_cells_under_one_cell_one_anchor_rule": NON_UNARY,
        "trees_exceeding_retained_anchor_budget": over_budget,
        "over_budget_fraction": str(Fraction(over_budget, family)),
        "conclusion": "two retained source anchors per maximal unary run cannot be supplied uniformly from the nineteen non-unary cells",
        "remaining_gap": "anchors must be shared, recycled, drawn from an external source reservoir, or replaced by a different support-chord realization",
        "status": "passed",
    }
)
