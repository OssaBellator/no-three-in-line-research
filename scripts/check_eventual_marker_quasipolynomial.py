#!/usr/bin/env python3
from fractions import Fraction

MAX_N = 300
INF = 10**18

# Two based marker cycles: a length-two cycle of cost three and a
# critical length-three cycle of cost four.
blocks = [(2, 3, (2, 0)), (3, 4, (0, 3))]

dp = [INF] * (MAX_N + 1)
parent = [None] * (MAX_N + 1)
dp[0] = 0
for n in range(1, MAX_N + 1):
    for idx, (length, cost, _) in enumerate(blocks):
        if n >= length and dp[n - length] + cost < dp[n]:
            dp[n] = dp[n - length] + cost
            parent[n] = idx


def formula(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return INF
    q, r = divmod(n, 3)
    if r == 0:
        return 4 * q
    if r == 1:
        return 4 * q + 2  # two length-two cycles and q-1 critical cycles
    return 4 * q + 3      # one length-two cycle and q critical cycles

for n in range(MAX_N + 1):
    assert dp[n] == formula(n), (n, dp[n], formula(n))

# Recover one optimum and audit the O(1/N) action-rate error from the
# all-critical target (0,1).
max_l1_error_scaled = Fraction(0)
residue_excess = {}
for n in range(2, MAX_N + 1):
    counts = [0, 0]
    m = n
    while m:
        idx = parent[m]
        assert idx is not None
        length, _, action_counts = blocks[idx]
        counts[0] += action_counts[0]
        counts[1] += action_counts[1]
        m -= length
    assert sum(counts) == n
    l1 = Fraction(counts[0], n) + abs(Fraction(counts[1], n) - 1)
    max_l1_error_scaled = max(max_l1_error_scaled, n * l1)
    residue_excess[n % 3] = Fraction(3 * dp[n] - 4 * n, 3)

assert residue_excess == {2: Fraction(1, 3), 0: Fraction(0), 1: Fraction(2, 3)}
assert max_l1_error_scaled == 8

print({
    "checked_lengths": MAX_N + 1,
    "critical_mean_cost": Fraction(4, 3),
    "residue_excess": residue_excess,
    "max_N_times_action_L1_error": max_l1_error_scaled,
    "status": "passed",
})
