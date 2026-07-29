#!/usr/bin/env python3
from functools import lru_cache
from itertools import permutations

M = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
N = 4
PERMS = tuple(permutations(range(N)))

assert all(sum(row) == 4 for row in M)
assert all(sum(M[i][j] for i in range(N)) == 4 for j in range(N))


def subtract(mat, p):
    rows = [list(r) for r in mat]
    for i, j in enumerate(p):
        if rows[i][j] == 0:
            return None
        rows[i][j] -= 1
    return tuple(tuple(r) for r in rows)


@lru_cache(None)
def lex_decomposition(mat, steps):
    if steps == 0:
        return () if all(v == 0 for row in mat for v in row) else None
    for p in PERMS:
        nxt = subtract(mat, p)
        if nxt is None:
            continue
        tail = lex_decomposition(nxt, steps - 1)
        if tail is not None:
            return (p,) + tail
    return None


@lru_cache(None)
def ordered_count(mat, steps):
    if steps == 0:
        return int(all(v == 0 for row in mat for v in row))
    total = 0
    for p in PERMS:
        nxt = subtract(mat, p)
        if nxt is not None:
            total += ordered_count(nxt, steps - 1)
    return total

layers = lex_decomposition(M, 4)
assert layers == (
    (0, 1, 2, 3),
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (2, 3, 0, 1),
)
assert ordered_count(M, 4) == 84

reconstructed = [[0] * N for _ in range(N)]
for p in layers:
    assert sorted(p) == list(range(N))
    for i, j in enumerate(p):
        reconstructed[i][j] += 1
assert tuple(tuple(r) for r in reconstructed) == M

print({
    "matrix_size": N,
    "layers": layers,
    "ordered_decompositions": 84,
    "per_slot_source_collisions": 0,
    "per_slot_action_collisions": 0,
    "status": "passed",
})
