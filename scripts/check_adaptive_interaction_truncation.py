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


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def rowmul(v, A):
    return [sum(v[k] * A[k][j] for k in range(len(v))) for j in range(len(A[0]))]


J = [
    [F(1, 5), F(1, 10), F(0)],
    [F(0), F(1, 4), F(1, 10)],
    [F(1, 20), F(0), F(1, 5)],
]
C = [
    [F(1, 10), F(1, 20)],
    [F(1, 20), F(1, 10)],
    [F(1, 8), F(1, 16)],
]
I = eye(3)
H = matmul(inv([[I[i][j] - J[i][j] for j in range(3)] for i in range(3)]), C)
assert H == [[C[i][j] + matmul(J, H)[i][j] for j in range(2)] for i in range(3)]

beta = [F(1), F(0), F(0)]
tolerance = (F(1, 100), F(1, 100))

v = beta[:]
uniform_depth = None
uniform_expansions = 0
level_width = 1
for m in range(10):
    uniform_expansions += level_width
    v = rowmul(v, J)
    tail = rowmul(v, H)
    if all(tail[j] <= tolerance[j] for j in range(2)):
        uniform_depth = m
        break
    level_width *= 2
assert uniform_depth == 2
assert uniform_expansions == 7

frontier = [(F(1), 0)]
retained = [F(0), F(0)]
adaptive_expansions = 0
history = []
while True:
    omitted = [sum(mass * H[state][j] for mass, state in frontier) for j in range(2)]
    history.append(tuple(omitted))
    if all(omitted[j] <= tolerance[j] for j in range(2)):
        break
    idx = max(
        range(len(frontier)),
        key=lambda i: max(frontier[i][0] * H[frontier[i][1]][j] / tolerance[j] for j in range(2)),
    )
    mass, state = frontier.pop(idx)
    adaptive_expansions += 1
    for j in range(2):
        retained[j] += mass * C[state][j]
    for nxt, weight in enumerate(J[state]):
        if weight:
            frontier.append((mass * weight, nxt))

assert adaptive_expansions == 4
assert history[-1] == (F(6789, 959000), F(4101, 479500))
assert all(history[-1][j] <= tolerance[j] for j in range(2))
total = rowmul(beta, H)
omitted = list(history[-1])
assert total == [retained[j] + omitted[j] for j in range(2)]

print({
    "exact_total_outputs": [str(x) for x in total],
    "tolerance": [str(x) for x in tolerance],
    "uniform_depth": uniform_depth,
    "uniform_prefix_expansions": uniform_expansions,
    "adaptive_prefix_expansions": adaptive_expansions,
    "adaptive_frontier_size": len(frontier),
    "certified_omitted_outputs": [str(x) for x in omitted],
})
