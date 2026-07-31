#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
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

distribution = defaultdict(int)
for root_type in ROOT_TYPES:
    for risk, count in dp[N][J][root_type].items():
        distribution[risk] += count
distribution = dict(sorted(distribution.items()))

assert distribution == {
    0: 367479684,
    1: 4491418360,
    2: 20211382620,
    3: 44097562080,
    4: 51447155760,
    5: 33242777568,
    6: 11872420560,
    7: 2261413440,
    8: 212007510,
    9: 8314020,
    10: 92378,
}

family = sum(distribution.values())
assert family == profile_count(N, J) == 168212023980

unary = N - 1 - 2 * J
encoded_leaves = J + 1
support_inventory = {
    "original_state_0_terminals": encoded_leaves,
    "auxiliary_state_1_terminals": unary,
    "auxiliary_state_2_terminals": J,
}
assert support_inventory == {
    "original_state_0_terminals": 10,
    "auxiliary_state_1_terminals": 11,
    "auxiliary_state_2_terminals": 9,
}
assert sum(support_inventory.values()) == N

aggregate_risk = sum(risk * count for risk, count in distribution.items())
assert aggregate_risk == 638045608200
assert Fraction(aggregate_risk, family) == Fraction(110, 29)
assert min(distribution) == 0
assert max(distribution) == unary - 1 == 10

print(
    {
        "original_automaton_leaf_count": N,
        "encoded_total_nodes": N,
        "encoded_binary_nodes": J,
        "encoded_unary_nodes": unary,
        "encoded_leaves": encoded_leaves,
        "decoded_support_terminal_inventory": support_inventory,
        "support_nesting_risk_definition": "U-parent/U-child edge = consecutive nested state-1 support terminals",
        "risk_distribution": distribution,
        "family_size": family,
        "aggregate_support_nesting_risk": aggregate_risk,
        "mean_support_nesting_risk": str(Fraction(aggregate_risk, family)),
        "decoder_scope": "exact for the original three-state automaton; not yet mapped to coordinate-level support chords",
        "evidence_level": "automaton_decoded_risk_census",
        "status": "passed",
    }
)
