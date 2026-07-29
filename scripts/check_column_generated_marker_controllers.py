#!/usr/bin/env python3
from fractions import Fraction as F

states = {
    "u0": [
        ("idle", F(0), F(0)),
        ("local", F(1), F(3, 4)),
        ("burst", F(2), F(1)),
    ],
    "u1": [
        ("idle", F(0), F(0)),
        ("local", F(1), F(2, 3)),
        ("burst", F(3), F(4, 3)),
    ],
    "u2": [
        ("idle", F(0), F(0)),
        ("local", F(1), F(1, 2)),
        ("burst", F(2), F(5, 4)),
    ],
}

restricted = {u: {"idle", "local"} for u in states}

def solve_state(u, allowed):
    candidates = []
    for name, gap, cost in states[u]:
        if name in allowed and gap >= 1:
            candidates.append((cost / gap, name, gap, cost))
    assert candidates
    ratio, name, gap, cost = min(candidates)
    return {
        "price": ratio,
        "action": name,
        "action_mass": F(1, 1) / gap,
        "idle_mass": F(1, 1) - F(1, 1) / gap,
        "cost": ratio,
    }

def solve_master(allowed_by_state):
    sol = {u: solve_state(u, allowed_by_state[u]) for u in states}
    return sol, sum(v["cost"] for v in sol.values())

initial, initial_cost = solve_master(restricted)
assert initial_cost == F(23, 12)

negative_columns = []
for u, actions in states.items():
    lam = initial[u]["price"]
    for name, gap, cost in actions:
        if name not in restricted[u]:
            reduced = cost - lam * gap
            if reduced < 0:
                negative_columns.append((u, name, reduced))

assert negative_columns == [
    ("u0", "burst", F(-1, 2)),
    ("u1", "burst", F(-2, 3)),
]
for u, name, _ in negative_columns:
    restricted[u].add(name)

final, final_cost = solve_master(restricted)
assert final_cost == F(13, 9)
assert final["u0"]["action"] == "burst" and final["u0"]["action_mass"] == F(1, 2)
assert final["u1"]["action"] == "burst" and final["u1"]["action_mass"] == F(1, 3)
assert final["u2"]["action"] == "local" and final["u2"]["action_mass"] == F(1)

reduced_costs = {}
for u, actions in states.items():
    lam = final[u]["price"]
    reduced_costs[u] = {name: cost - lam * gap for name, gap, cost in actions}
    assert min(reduced_costs[u].values()) == 0

full_lower_bound = sum(final[u]["price"] for u in states)
assert full_lower_bound == final_cost
bad_budget = F(7, 5)
assert final_cost - bad_budget == F(2, 45)

print({
    "initial_restricted_cost": str(initial_cost),
    "generated_columns": [(u, a, str(rc)) for u, a, rc in negative_columns],
    "final_minimum_budget": str(final_cost),
    "final_policy": {
        u: {
            "action": v["action"],
            "action_mass": str(v["action_mass"]),
            "idle_mass": str(v["idle_mass"]),
        }
        for u, v in final.items()
    },
    "bad_budget": str(bad_budget),
    "dual_margin": str(final_cost - bad_budget),
})
