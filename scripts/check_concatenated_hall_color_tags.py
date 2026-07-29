#!/usr/bin/env python3
from itertools import combinations, product

P = 5
points = [0, 1, 2, 3]
outer = []
for a, b in product(range(P), repeat=2):
    outer.append(tuple((a * x + b) % P for x in points))
assert len(outer) == 25 and len(set(outer)) == 25

def hamming(u, v):
    return sum(a != b for a, b in zip(u, v))

outer_distance = min(hamming(u, v) for i, u in enumerate(outer) for v in outer[i + 1:])
assert outer_distance == 3

concat = [tuple(symbol for x in word for symbol in (x, x)) for word in outer]
concat_distance = min(hamming(u, v) for i, u in enumerate(concat) for v in concat[i + 1:])
assert concat_distance == 6

def compatible_distance(received, codeword):
    return sum(r is not None and r != c for r, c in zip(received, codeword))

def decode(received, t):
    return [i for i, cw in enumerate(concat) if compatible_distance(received, cw) <= t]

checked = 0
for idx, cw in enumerate(concat):
    for t in range(3):
        for pos in combinations(range(8), t):
            replacements = [[v for v in range(P) if v != cw[j]] for j in pos]
            for vals in product(*replacements):
                r = list(cw)
                for j, v in zip(pos, vals):
                    r[j] = v
                assert decode(tuple(r), t) == [idx]
                checked += 1
    for err in range(8):
        for val in range(P):
            if val == cw[err]:
                continue
            remaining = [j for j in range(8) if j != err]
            for erased in combinations(remaining, 2):
                r = list(cw)
                r[err] = val
                for j in erased:
                    r[j] = None
                assert decode(tuple(r), 1) == [idx]
                checked += 1

assert checked == 25 * (1 + 8 * 4 + 28 * 16 + 8 * 4 * 21)

print({
    "colors": len(concat),
    "outer_distance": outer_distance,
    "inner_distance": 2,
    "concatenated_distance": concat_distance,
    "corrected_observations": checked,
    "protected_patterns": ["two errors", "one error plus two erasures"],
})
