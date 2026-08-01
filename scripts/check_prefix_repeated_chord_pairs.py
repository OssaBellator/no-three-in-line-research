#!/usr/bin/env python3
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

# For each state, map top unary-chain length to (count, repeated-chord-pair total).
dp = [
    [{root: {} for root in ROOT_TYPES} for _ in range(N + 1)]
    for _ in range(N + 1)
]
dp[1][0]["L"][0] = (1, 0)

for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for child_type in ROOT_TYPES:
            for top_length, (count, collision_total) in dp[size - 1][binary][child_type].items():
                new_top = top_length + 1 if child_type == "U" else 1
                added_pairs = top_length if child_type == "U" else 0
                old_count, old_total = dp[size][binary]["U"].get(new_top, (0, 0))
                dp[size][binary]["U"][new_top] = (
                    old_count + count,
                    old_total + collision_total + added_pairs * count,
                )

        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_type in ROOT_TYPES:
                        for _, (left_count, left_total) in dp[left_size][left_binary][left_type].items():
                            for right_type in ROOT_TYPES:
                                for _, (right_count, right_total) in dp[right_size][right_binary][right_type].items():
                                    old_count, old_total = dp[size][binary]["B"].get(0, (0, 0))
                                    dp[size][binary]["B"][0] = (
                                        old_count + left_count * right_count,
                                        old_total
                                        + left_total * right_count
                                        + right_total * left_count,
                                    )

family = 0
aggregate_pairs = 0
for root_type in ROOT_TYPES:
    for count, total in dp[N][J][root_type].values():
        family += count
        aggregate_pairs += total

assert family == profile_count(N, J) == 168212023980
assert aggregate_pairs == 925166131890
assert Fraction(aggregate_pairs, family) == Fraction(11, 2)

print({
    "profile": {"encoded_size": N, "binary_nodes": J},
    "family_size": family,
    "support_geometry": "each unary node uses the chord joining the two endpoint lines at its subtree interval endpoints",
    "collision_rule": "unary nodes on one maximal unary chain reuse the same support chord",
    "aggregate_repeated_chord_pairs": aggregate_pairs,
    "mean_repeated_chord_pairs": str(Fraction(aggregate_pairs, family)),
    "conclusion": "endpoint reuse gives a nonzero exact geometric incidence coordinate absent from the convex point embedding",
    "remaining_gap": "coincident support chords are not yet legal distinct grid support cells in the prime-patching construction",
    "evidence_level": "ancestry_aware_endpoint_reuse_census",
    "status": "passed",
})
