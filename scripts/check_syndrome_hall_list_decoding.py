#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations, product

P = 5
POINTS = range(4)
CODEWORDS = [
    tuple((a + b * x) % P for x in POINTS)
    for a in range(P) for b in range(P)
]
H = ((0, 1, 3, 1), (1, 0, 2, 2))

def syndrome(word):
    return tuple(sum(row[j] * word[j] for j in POINTS) % P for row in H)

assert len(set(CODEWORDS)) == 25
assert all(syndrome(c) == (0, 0) for c in CODEWORDS)
assert sum(syndrome(w) == (0, 0) for w in product(range(P), repeat=4)) == 25

LOCAL_LISTS = [(a,) for a in range(P)] + list(combinations(range(P), 2))

def syndrome_dp(lists):
    dp = {(0, 0): 1}
    parents = []
    for j, choices in enumerate(lists):
        nxt = defaultdict(int)
        back = {}
        for s, count in dp.items():
            for x in choices:
                ns = tuple((s[r] + H[r][j] * x) % P for r in range(2))
                nxt[ns] += count
                back.setdefault(ns, (s, x))
        parents.append(back)
        dp = dict(nxt)
    return dp.get((0, 0), 0), parents

def reconstruct(lists, parents):
    if (0, 0) not in parents[-1]:
        return None
    s = (0, 0)
    word = []
    for j in range(3, -1, -1):
        prev, x = parents[j][s]
        word.append(x)
        s = prev
    return tuple(reversed(word))

distribution = Counter()
max_count = 0
max_example = None
observations = 0
for lists in product(LOCAL_LISTS, repeat=4):
    count, parents = syndrome_dp(lists)
    brute = [c for c in CODEWORDS if all(c[j] in lists[j] for j in POINTS)]
    assert count == len(brute)
    if count:
        witness = reconstruct(lists, parents)
        assert witness in brute
    distribution[count] += 1
    observations += 1
    if count > max_count:
        max_count = count
        max_example = lists

assert observations == 15 ** 4 == 50625
assert max_count == 2
assert sum(distribution.values()) == observations

for lists in product(LOCAL_LISTS, repeat=4):
    count, _ = syndrome_dp(lists)
    info_bound = min(len(lists[i]) * len(lists[j]) for i, j in combinations(POINTS, 2))
    assert count <= info_bound

assert tuple(len(x) for x in max_example) == (1, 2, 2, 2)

print({
    "outer_codewords": len(CODEWORDS),
    "syndrome_states": P ** 2,
    "local_list_choices": len(LOCAL_LISTS),
    "observations_checked": observations,
    "list_count_distribution": dict(sorted(distribution.items())),
    "maximum_outer_list": max_count,
    "sharp_example": [list(x) for x in max_example],
})
