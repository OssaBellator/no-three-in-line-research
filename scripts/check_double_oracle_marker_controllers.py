#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

COST = [F(7), F(5), F(5), F(8), F(4)]
GAP = [
    [F(3), F(0), F(0), F(3), F(3)],
    [F(2), F(-1), F(1), F(-3), F(-3)],
    [F(0), F(3), F(-3), F(4), F(-3)],
    [F(5), F(2), F(-2), F(4), F(2)],
]
ALL_ACTIONS = tuple(range(len(COST)))
ALL_SCENARIOS = tuple(range(len(GAP)))


def solve_square(a, b):
    n = len(b)
    m = [[F(a[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    row = 0
    for col in range(n):
        pivot = next((r for r in range(row, n) if m[r][col]), None)
        if pivot is None:
            return None
        m[row], m[pivot] = m[pivot], m[row]
        scale = m[row][col]
        m[row] = [x / scale for x in m[row]]
        for r in range(n):
            if r != row and m[r][col]:
                scale = m[r][col]
                m[r] = [m[r][j] - scale * m[row][j] for j in range(n + 1)]
        row += 1
    return [m[i][-1] for i in range(n)]


def primal(actions, scenarios):
    n = len(actions)
    active_pool = [("scenario", s) for s in scenarios] + [("zero", i) for i in range(n)]
    best = None
    for active in combinations(active_pool, n - 1):
        a = [[F(1) for _ in range(n)]]
        b = [F(1)]
        for kind, key in active:
            if kind == "scenario":
                a.append([GAP[key][action] for action in actions])
            else:
                row = [F(0)] * n
                row[key] = F(1)
                a.append(row)
            b.append(F(0))
        p = solve_square(a, b)
        if p is None or any(x < 0 for x in p):
            continue
        if any(sum(GAP[s][action] * p[i] for i, action in enumerate(actions)) < 0 for s in scenarios):
            continue
        value = sum(COST[action] * p[i] for i, action in enumerate(actions))
        if best is None or value < best[0]:
            best = (value, p)
    assert best is not None
    return best


def dual(actions, scenarios):
    # maximize alpha subject to alpha + sum_s lambda_s GAP[s,a] <= COST[a], lambda>=0
    m = len(scenarios)
    nvar = 1 + m
    active_pool = [("action", a) for a in actions] + [("zero", j) for j in range(m)]
    best = None
    for active in combinations(active_pool, nvar):
        a = []
        b = []
        for kind, key in active:
            if kind == "action":
                a.append([F(1)] + [GAP[s][key] for s in scenarios])
                b.append(COST[key])
            else:
                row = [F(0)] * nvar
                row[1 + key] = F(1)
                a.append(row)
                b.append(F(0))
        sol = solve_square(a, b)
        if sol is None:
            continue
        alpha, lambdas = sol[0], sol[1:]
        if any(x < 0 for x in lambdas):
            continue
        if any(alpha + sum(lambdas[j] * GAP[s][action] for j, s in enumerate(scenarios)) > COST[action] for action in actions):
            continue
        if best is None or alpha > best[0]:
            best = (alpha, lambdas)
    assert best is not None
    return best


actions = [0, 1]
scenarios = [0]
trace = []
while True:
    value, p = primal(actions, scenarios)
    alpha, lambdas = dual(actions, scenarios)
    assert value == alpha

    scenario_gaps = {
        s: sum(GAP[s][action] * p[i] for i, action in enumerate(actions))
        for s in ALL_SCENARIOS
    }
    violated = [(gap, s) for s, gap in scenario_gaps.items() if gap < 0]
    if violated:
        gap, s = min(violated)
        trace.append(("scenario", s, value, gap))
        if s not in scenarios:
            scenarios.append(s)
        continue

    reduced_costs = {
        action: COST[action] - alpha - sum(lambdas[j] * GAP[s][action] for j, s in enumerate(scenarios))
        for action in ALL_ACTIONS
    }
    improving = [(rc, action) for action, rc in reduced_costs.items() if rc < 0]
    if improving:
        rc, action = min(improving)
        trace.append(("action", action, value, rc))
        if action not in actions:
            actions.append(action)
        continue

    trace.append(("done", value, tuple(p), tuple(actions), tuple(scenarios)))
    break

assert [step[0] for step in trace] == ["scenario", "action", "action", "scenario", "done"]
assert trace[0][1:] == (1, F(5), F(-1))
assert trace[1][1:] == (2, F(17, 3), F(-4, 3))
assert trace[2][1:] == (4, F(5), F(-3))
assert trace[3][1:] == (2, F(19, 4), F(-3))
assert trace[-1][1] == F(5)
assert actions == [0, 1, 2, 4]
assert scenarios == [0, 1, 2]

final_value, final_p = primal(actions, scenarios)
assert final_p == [F(0), F(1, 2), F(1, 2), F(0)]
assert all(sum(GAP[s][action] * final_p[i] for i, action in enumerate(actions)) >= 0 for s in ALL_SCENARIOS)
final_alpha, final_lambda = dual(actions, scenarios)
assert final_value == final_alpha == F(5)
assert final_lambda == [F(1, 3), F(1, 2), F(1, 6)]
assert all(
    COST[action] - final_alpha - sum(final_lambda[j] * GAP[s][action] for j, s in enumerate(scenarios)) >= 0
    for action in ALL_ACTIONS
)

print({
    "trace": [(kind, key, str(value), str(witness)) for kind, key, value, witness, *rest in trace[:-1]],
    "generated_actions": [2, 4],
    "generated_scenarios": [1, 2],
    "global_optimum": str(final_value),
    "final_policy_on_actions_0_1_2_4": [str(x) for x in final_p],
    "final_dual_scenario_prices": [str(x) for x in final_lambda],
})
