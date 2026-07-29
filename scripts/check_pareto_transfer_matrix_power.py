#!/usr/bin/env python3

# Transition entries: (work,e1,e2,word)
BASE = {
    (0, 0): [(0, 2, 0, "A")],
    (0, 1): [(1, 0, 1, "B")],
    (1, 1): [(0, 0, 2, "C")],
    (1, 0): [(1, 1, 0, "D")],
}
STATES = (0, 1)


def prune(items):
    # Tuplewise dominance, preserving one canonical word per exact vector.
    best = {}
    for w, e1, e2, word in items:
        best.setdefault((w, e1, e2), word)
        if word < best[(w, e1, e2)]:
            best[(w, e1, e2)] = word
    vals = [(w, e1, e2, word) for (w, e1, e2), word in best.items()]
    nd = []
    for x in vals:
        if not any(
            (y[0] <= x[0] and y[1] <= x[1] and y[2] <= x[2]) and y[:3] != x[:3]
            for y in vals
        ):
            nd.append(x)
    return sorted(nd)


def multiply(M, N):
    R = {}
    for i in STATES:
        for k in STATES:
            items = []
            for j in STATES:
                for a in M.get((i, j), []):
                    for b in N.get((j, k), []):
                        items.append((a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3]))
            R[(i, k)] = prune(items)
    return R


def power(M, n):
    I = {(0, 0): [(0, 0, 0, "")], (1, 1): [(0, 0, 0, "")], (0, 1): [], (1, 0): []}
    R = I
    B = M
    while n:
        if n & 1:
            R = multiply(R, B)
        B = multiply(B, B)
        n //= 2
    return R


def direct(n):
    paths = [(0, 0, 0, 0, "")]
    for _ in range(n):
        nxt = []
        for s, w, e1, e2, word in paths:
            for t in STATES:
                for dw, d1, d2, ch in BASE.get((s, t), []):
                    nxt.append((t, w + dw, e1 + d1, e2 + d2, word + ch))
        paths = nxt
    return prune([(w, e1, e2, word) for s, w, e1, e2, word in paths if s == 0])


P8 = power(BASE, 8)[(0, 0)]
D8 = direct(8)
assert [(x[0], x[1], x[2]) for x in P8] == [(x[0], x[1], x[2]) for x in D8]
assert len(D8) == 17
feasible = [x for x in D8 if x[1] <= 4 and x[2] <= 4]
assert feasible == [(8, 4, 4, "BDBDBDBD")]

print({
    "motif_length": 8,
    "direct_start_end_plans": 128,
    "pareto_vectors": len(D8),
    "squaring_steps": 3,
    "tolerance": (4, 4),
    "unique_plan": feasible[0][3],
    "minimum_work": feasible[0][0],
})
