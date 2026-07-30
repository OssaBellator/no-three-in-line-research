#!/usr/bin/env python3
from itertools import product

X = ((1, -1), (0, 0), (-1, 1))
Y = ((-1, 1), (0, 0), (1, -1))


def rotate(seq, k):
    return seq[k:] + seq[:k]


def buffer(seq):
    cumulative = [0, 0]
    minima = [0, 0]
    for step in seq:
        for i in range(2):
            cumulative[i] += step[i]
            minima[i] = min(minima[i], cumulative[i])
    assert cumulative == [0, 0]
    return tuple(-x for x in minima)

records = []
for i, j in product(range(3), repeat=2):
    sx = rotate(X, i)
    sy = rotate(Y, j)
    separate_x = buffer(sx)
    separate_y = buffer(sy)
    pooled = tuple((sx[t][0] + sy[t][0], sx[t][1] + sy[t][1]) for t in range(3))
    pooled_buffer = buffer(pooled)
    records.append((sum(pooled_buffer), i, j, separate_x, separate_y, pooled_buffer, pooled))
    assert sum(pooled_buffer) <= sum(separate_x) + sum(separate_y)

best = min(r[0] for r in records)
optimal = [r for r in records if r[0] == best]
assert best == 0
assert len(optimal) == 3
assert all(sum(r[3]) + sum(r[4]) == 2 for r in optimal)
assert all(r[5] == (0, 0) for r in optimal)

# Repeating any aligned optimal pair stays feasible with zero pooled startup reserve.
chosen = min(optimal, key=lambda r: (r[1], r[2]))
pooled_word = chosen[6] * 100
assert buffer(pooled_word) == (0, 0)

print({
    "phase_pairs_checked": len(records),
    "zero_buffer_alignments": len(optimal),
    "separate_l1_reserve": 2,
    "pooled_l1_reserve": best,
    "periods_checked": 100,
    "status": "passed",
})
