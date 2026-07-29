#!/usr/bin/env python3
from itertools import combinations, product

P = 5
POINTS = (0, 1, 2, 3)
CODEWORDS = []
for a in range(P):
    for b in range(P):
        CODEWORDS.append(tuple((a + b * x) % P for x in POINTS))
assert len(CODEWORDS) == 25
assert len(set(CODEWORDS)) == 25

# Every pair of coordinates is an information set.
for i, j in combinations(range(4), 2):
    assert len({(c[i], c[j]) for c in CODEWORDS}) == 25

# Minimum distance is three.
def distance(c, d):
    return sum(x != y for x, y in zip(c, d))

assert min(distance(c, d) for c, d in combinations(CODEWORDS, 2)) == 3

CATALOG = [frozenset((x,)) for x in range(P)] + [frozenset(pair) for pair in combinations(range(P), 2)]
assert len(CATALOG) == 15

all_observations = 0
max_list = 0
tight_bounds = 0
for lists in product(CATALOG, repeat=4):
    compatible = [c for c in CODEWORDS if all(c[j] in lists[j] for j in range(4))]
    sizes = sorted(len(s) for s in lists)
    info_bound = sizes[0] * sizes[1]
    assert len(compatible) <= info_bound
    all_observations += 1
    max_list = max(max_list, len(compatible))
    if len(compatible) == info_bound:
        tight_bounds += 1
assert all_observations == 15 ** 4 == 50625
assert max_list == 2

# A true color remains unique when fewer than delta=3 blocks become ambiguous.
protected_observations = 0
for c in CODEWORDS:
    for bad_count in (0, 1, 2):
        for bad in combinations(range(4), bad_count):
            choices = []
            for j in bad:
                choices.append([frozenset((c[j], z)) for z in range(P) if z != c[j]])
            for chosen in product(*choices):
                lists = [frozenset((symbol,)) for symbol in c]
                for j, value in zip(bad, chosen):
                    lists[j] = value
                compatible = [d for d in CODEWORDS if all(d[j] in lists[j] for j in range(4))]
                assert compatible == [c]
                protected_observations += 1
assert protected_observations == 25 * (1 + 4 * 4 + 6 * 16) == 2825

# Exhibit a three-block ambiguity, showing the distance threshold is sharp.
c0 = CODEWORDS[0]
c1 = next(c for c in CODEWORDS if distance(c0, c) == 3)
lists = []
for a, b in zip(c0, c1):
    lists.append(frozenset((a,)) if a == b else frozenset((a, b)))
compatible = [c for c in CODEWORDS if all(c[j] in lists[j] for j in range(4))]
assert c0 in compatible and c1 in compatible and len(compatible) >= 2

print({
    "outer_code": "[4,2,3] Reed-Solomon over F_5",
    "catalog_observations": all_observations,
    "protected_true_color_observations": protected_observations,
    "maximum_compatible_color_list": max_list,
    "information_set_bound_tight_cases": tight_bounds,
    "sharp_three_block_ambiguity": len(compatible),
})
