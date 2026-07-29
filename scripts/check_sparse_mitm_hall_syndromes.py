#!/usr/bin/env python3
from collections import defaultdict
from itertools import product

Q = 5
# [5,2,4] Reed--Solomon evaluation code: c_i=a+i b.
CODE = [tuple((a + i * b) % Q for i in range(5)) for a in range(Q) for b in range(Q)]
H = (
    (1, -2, 1, 0, 0),
    (0, 1, -2, 1, 0),
    (0, 0, 1, -2, 1),
)


def syndrome(word):
    return tuple(sum(row[j] * word[j] for j in range(5)) % Q for row in H)


assert all(syndrome(c) == (0, 0, 0) for c in CODE)


def half_map(lists, indices):
    counts = defaultdict(int)
    witness = {}
    for values in product(*(lists[j] for j in indices)):
        partial = [0] * 5
        for j, v in zip(indices, values):
            partial[j] = v
        s = syndrome(partial)
        counts[s] += 1
        witness.setdefault(s, values)
    return counts, witness


def mitm_count(lists):
    left, wl = half_map(lists, (0, 1))
    right, wr = half_map(lists, (2, 3, 4))
    total = 0
    witness = None
    for s, count in left.items():
        target = tuple((-x) % Q for x in s)
        total += count * right.get(target, 0)
        if witness is None and target in wr:
            vals = [0] * 5
            vals[0], vals[1] = wl[s]
            vals[2], vals[3], vals[4] = wr[target]
            witness = tuple(vals)
    return total, witness, len(left), len(right)

hist = defaultdict(int)
max_list = 0
max_half_states = (0, 0)
for starts in product(range(Q), repeat=5):
    lists = [tuple(sorted({s, (s + 1) % Q})) for s in starts]
    direct = [c for c in CODE if all(c[j] in lists[j] for j in range(5))]
    count, witness, ls, rs = mitm_count(lists)
    assert count == len(direct)
    if count:
        assert witness in direct
    hist[count] += 1
    max_list = max(max_list, count)
    max_half_states = (max(max_half_states[0], ls), max(max_half_states[1], rs))

assert max_list == 2
assert hist == {0: 2350, 1: 750, 2: 25}
assert max_half_states == (4, 8)
print({
    "observations": Q ** 5,
    "list_histogram": dict(sorted(hist.items())),
    "sharp_max_list": max_list,
    "max_sparse_half_states": max_half_states,
    "full_syndrome_space": Q ** 3,
})
