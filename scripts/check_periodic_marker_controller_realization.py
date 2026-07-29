#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

policies = {
    "u0": {"A": F(1, 3), "B": F(2, 3)},
    "u1": {"C": F(1, 2), "D": F(1, 2)},
}
schedules = {"u0": ["B", "A", "B"], "u1": ["D", "C"]}
gaps = {
    "u0": {"A": (F(1), F(-1)), "B": (F(-1, 4), F(3, 4))},
    "u1": {"C": (F(2, 3), F(-1, 3)), "D": (F(-1, 6), F(5, 6))},
}
resources = {
    "u0": {"A": F(1), "B": F(0)},
    "u1": {"C": F(0), "D": F(1)},
}

def mean(state, values):
    return sum(policies[state][a] * values[state][a] for a in policies[state])

mean_gap = {
    u: tuple(mean(u, {s: {a: gaps[s][a][j] for a in gaps[s]} for s in gaps})
             for j in range(2))
    for u in policies
}
mean_resource = {u: mean(u, resources) for u in policies}

assert mean_gap == {"u0": (F(1, 6), F(1, 6)), "u1": (F(1, 4), F(1, 4))}
assert sum(mean_resource.values()) == F(5, 6)

for u, sched in schedules.items():
    M = len(sched)
    for a, p in policies[u].items():
        assert sched.count(a) == M * p

def prefix_deviations(state, value):
    sched = schedules[state]
    avg = sum(policies[state][a] * value[a] for a in policies[state])
    out = [F(0)]
    total = F(0)
    for r, a in enumerate(sched[:-1], 1):
        total += value[a]
        out.append(total - r * avg)
    return out

gap_dev = {}
res_dev = {}
for u in policies:
    gap_dev[u] = []
    for j in range(2):
        value = {a: gaps[u][a][j] for a in gaps[u]}
        gap_dev[u].append(prefix_deviations(u, value))
    res_dev[u] = prefix_deviations(u, resources[u])

gap_bounds = {
    j: sum(max(abs(x) for x in gap_dev[u][j]) for u in policies)
    for j in range(2)
}
resource_bound = sum(max(abs(x) for x in res_dev[u]) for u in policies)

max_gap_error = [F(0), F(0)]
max_resource_error = F(0)
for n0, n1 in product(range(31), repeat=2):
    counts = {"u0": n0, "u1": n1}
    actual_gap = [F(0), F(0)]
    expected_gap = [F(0), F(0)]
    actual_resource = F(0)
    expected_resource = F(0)
    for u, n in counts.items():
        sched = schedules[u]
        for t in range(n):
            a = sched[t % len(sched)]
            for j in range(2):
                actual_gap[j] += gaps[u][a][j]
            actual_resource += resources[u][a]
        for j in range(2):
            expected_gap[j] += n * mean_gap[u][j]
        expected_resource += n * mean_resource[u]
    for j in range(2):
        err = abs(actual_gap[j] - expected_gap[j])
        max_gap_error[j] = max(max_gap_error[j], err)
        assert err <= gap_bounds[j]
    rerr = abs(actual_resource - expected_resource)
    max_resource_error = max(max_resource_error, rerr)
    assert rerr <= resource_bound

assert gap_bounds == {0: F(5, 6), 1: F(7, 6)}
assert resource_bound == F(5, 6)
assert max_gap_error == [F(5, 6), F(7, 6)]
assert max_resource_error == F(5, 6)

print({
    "local_periods": {u: len(s) for u, s in schedules.items()},
    "finite_memory_states": 6,
    "mean_gaps": {u: [str(x) for x in mean_gap[u]] for u in mean_gap},
    "mean_resource": str(sum(mean_resource.values())),
    "prefix_gap_bounds": [str(gap_bounds[j]) for j in range(2)],
    "prefix_resource_bound": str(resource_bound),
    "audited_occurrence_pairs": 31 * 31,
})
