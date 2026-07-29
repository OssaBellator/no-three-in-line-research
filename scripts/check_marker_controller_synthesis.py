#!/usr/bin/env python3
from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def inv(A):
    n = len(A)
    aug = [A[i][:] + eye(n)[i] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if aug[i][c])
        aug[c], aug[p] = aug[p], aug[c]
        z = aug[c][c]
        aug[c] = [x / z for x in aug[c]]
        for i in range(n):
            if i != c and aug[i][c]:
                z = aug[i][c]
                aug[i] = [aug[i][j] - z * aug[c][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def rowmul(v, A):
    return [sum(v[k] * A[k][j] for k in range(len(v))) for j in range(len(A[0]))]


w1 = [F(1), F(1, 10), F(9, 10)]
w2 = [F(1), F(9, 10), F(1, 10)]
q = F(1, 2)

action_A = [F(0), F(1), F(0)]
action_B = [F(0), F(0), F(1)]


def ratio(row, w, u):
    return sum(row[j] * w[j] for j in range(3)) / w[u]


ratios = {
    "A": (ratio(action_A, w1, 0), ratio(action_A, w2, 0)),
    "B": (ratio(action_B, w1, 0), ratio(action_B, w2, 0)),
}
assert ratios["A"] == (F(1, 10), F(9, 10))
assert ratios["B"] == (F(9, 10), F(1, 10))

feasible = []
for k in range(21):
    t = F(k, 20)
    mixed = [t * action_A[j] + (1 - t) * action_B[j] for j in range(3)]
    if ratio(mixed, w1, 0) <= q and ratio(mixed, w2, 0) <= q:
        feasible.append(t)
assert feasible == [F(1, 2)]

Q = [
    [F(0), F(1, 2), F(1, 2)],
    [F(0), F(1, 5), F(0)],
    [F(0), F(0), F(1, 5)],
]
for w in (w1, w2):
    Qw = [sum(Q[i][j] * w[j] for j in range(3)) for i in range(3)]
    assert all(Qw[i] <= q * w[i] for i in range(3))

I = eye(3)
R = inv([[I[i][j] - Q[i][j] for j in range(3)] for i in range(3)])
b = [F(1), F(0), F(0)]
B = rowmul(b, R)
assert B == [x + y for x, y in zip(b, rowmul(B, Q))]

q_bad = F(2, 5)
gaps = {}
for name, row in (("A", action_A), ("B", action_B)):
    gaps[name] = (
        ratio(row, w1, 0) - q_bad,
        ratio(row, w2, 0) - q_bad,
    )
assert gaps["A"] == (F(-3, 10), F(1, 2))
assert gaps["B"] == (F(1, 2), F(-3, 10))
eta = (F(1), F(1))
separator_values = {
    name: eta[0] * g[0] + eta[1] * g[1] for name, g in gaps.items()
}
assert separator_values == {"A": F(1, 5), "B": F(1, 5)}

print({
    "unique_state0_mix": str(feasible[0]),
    "closed_loop_resolvent_load": [str(x) for x in B],
    "potential_rates": [str(q), str(q)],
    "bad_rate": str(q_bad),
    "localized_separator": [str(x) for x in eta],
    "separator_margin": str(F(1, 5)),
})
