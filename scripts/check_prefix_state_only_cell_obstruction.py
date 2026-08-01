#!/usr/bin/env python3
from collections import defaultdict
from math import factorial

N = 30
J = 9
ROOT_TYPES = ("L", "U", "B")


def profile_count(size, binary):
    unary = size - 1 - 2 * binary
    if unary < 0:
        return 0
    return factorial(size - 1) // (
        factorial(unary) * factorial(binary) * factorial(binary + 1)
    )


# Exact profile/risk DP. Risk counts U-parent/U-child edges.
dp = [
    [
        {root_type: defaultdict(int) for root_type in ROOT_TYPES}
        for _ in range(N + 1)
    ]
    for _ in range(N + 1)
]
dp[1][0]["L"][0] = 1
for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for child_type in ROOT_TYPES:
            for risk, count in dp[size - 1][binary][child_type].items():
                dp[size][binary]["U"][risk + int(child_type == "U")] += count
        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_type in ROOT_TYPES:
                        for left_risk, left_count in dp[left_size][left_binary][left_type].items():
                            for right_type in ROOT_TYPES:
                                for right_risk, right_count in dp[right_size][right_binary][right_type].items():
                                    dp[size][binary]["B"][left_risk + right_risk] += left_count * right_count

risk_distribution = defaultdict(int)
for root_type in ROOT_TYPES:
    for risk, count in dp[N][J][root_type].items():
        risk_distribution[risk] += count
risk_distribution = dict(sorted(risk_distribution.items()))

family = sum(risk_distribution.values())
unary = N - 1 - 2 * J
encoded_leaves = J + 1
terminal_inventory = (encoded_leaves, unary, J)
assert family == profile_count(N, J) == 168212023980
assert terminal_inventory == (10, 11, 9)
assert risk_distribution[0] == 367479684
assert risk_distribution[10] == 92378
assert min(risk_distribution) == 0
assert max(risk_distribution) == 10

# Every object in this profile has the same state-terminal multiset. Since two
# positive subfamilies have different risks, no statistic depending only on that
# multiset—or on a state-only assignment of terminal types to fixed cells—can
# recover support-nesting risk.
state_only_cell_multiset = {
    "state_0_cell": terminal_inventory[0],
    "state_1_cell": terminal_inventory[1],
    "state_2_cell": terminal_inventory[2],
}
assert sum(state_only_cell_multiset.values()) == N
assert risk_distribution[0] > 0 and risk_distribution[10] > 0

print({
    "profile_family_size": family,
    "common_state_terminal_inventory": terminal_inventory,
    "objects_with_risk_zero": risk_distribution[0],
    "objects_with_risk_ten": risk_distribution[10],
    "risk_range": (min(risk_distribution), max(risk_distribution)),
    "obstruction": "state-terminal cell multisets do not determine ancestry-sensitive support nesting",
    "required_decoder_state": "at least parent-child support-chord incidence, not terminal labels alone",
    "evidence_level": "automaton_coordinate_decoder_obstruction",
    "status": "passed",
})
