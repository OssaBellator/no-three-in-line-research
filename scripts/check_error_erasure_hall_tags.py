#!/usr/bin/env python3
from itertools import combinations

p = 7
k = 2
t = 1
e = 1
n = k + 2 * t + e
points = list(range(n))

# Reed--Solomon evaluation tags for affine polynomials a+b*x over F_7.
codewords = {}
for a in range(p):
    for b in range(p):
        codewords[(a, b)] = tuple((a + b * x) % p for x in points)

# MDS distance n-k+1=4.
def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))

minimum_distance = min(
    hamming(codewords[u], codewords[v])
    for u, v in combinations(codewords, 2)
)
assert minimum_distance == n - k + 1 == 4
assert 2 * t + e < minimum_distance

observations_checked = 0
for message, word in codewords.items():
    for erased in range(n):
        for error_position in range(n):
            if error_position == erased:
                continue
            for wrong_symbol in range(p):
                if wrong_symbol == word[error_position]:
                    continue
                observed = list(word)
                observed[erased] = None
                observed[error_position] = wrong_symbol

                compatible = []
                for candidate_message, candidate in codewords.items():
                    disagreements = sum(
                        observed[i] is not None and observed[i] != candidate[i]
                        for i in range(n)
                    )
                    if disagreements <= t:
                        compatible.append(candidate_message)
                assert compatible == [message]
                observations_checked += 1

assert observations_checked == p**k * n * (n - 1) * (p - 1)
assert n == k + 2 * t + e

print({
    "field_size": p,
    "colors": p**k,
    "tag_length": n,
    "minimum_distance": minimum_distance,
    "corrected_errors": t,
    "corrected_erasures": e,
    "observations_checked": observations_checked,
    "singleton_optimal": True,
})
