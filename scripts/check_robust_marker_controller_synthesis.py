#!/usr/bin/env python3
from fractions import Fraction as F

# One marker state, two candidate actions, two adversarial row scenarios.
# A stationary policy uses action A with probability p and B with probability 1-p.
scenarios = {
    "s0": (F(1, 5), F(4, 5)),
    "s1": (F(4, 5), F(1, 5)),
}
q = F(1, 2)

candidates = set([F(0), F(1)])
for a0, b0 in scenarios.values():
    # a0*p+b0*(1-p)=q
    if a0 != b0:
        candidates.add((q - b0) / (a0 - b0))

feasible = []
for p in candidates:
    if F(0) <= p <= F(1):
        loads = {name: a * p + b * (1 - p) for name, (a, b) in scenarios.items()}
        if max(loads.values()) <= q:
            feasible.append((p, loads))

assert len(feasible) == 1
p, robust_loads = feasible[0]
assert p == F(1, 2)
assert set(robust_loads.values()) == {F(1, 2)}

# Exact resolvent load for root injection b under the worst closed-loop row.
b = F(1, 10)
resolvent_load = b / (1 - q)
assert resolvent_load == F(1, 5)

# At the stricter proposed rate q_bad, the equal scenario weights separate every action.
q_bad = F(2, 5)
eta = (F(1, 2), F(1, 2))
separator_action_values = {}
for action_index, action in enumerate(("A", "B")):
    value = sum(eta[s] * scenarios[name][action_index] for s, name in enumerate(("s0", "s1")))
    separator_action_values[action] = value
assert separator_action_values == {"A": F(1, 2), "B": F(1, 2)}
assert all(value - q_bad == F(1, 10) for value in separator_action_values.values())

print({
    "unique_robust_mix": str(p),
    "scenario_loads": {k: str(v) for k, v in robust_loads.items()},
    "closed_loop_resolvent_load": str(resolvent_load),
    "bad_rate": str(q_bad),
    "separator_weights": [str(x) for x in eta],
    "separator_margin": str(F(1, 10)),
})
