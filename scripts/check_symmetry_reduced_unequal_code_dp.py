#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

class_weights = (F(1, 64), F(1, 16), F(1, 4))
multiplicities = (3, 3, 2)
weights = tuple(weight for weight, count in zip(class_weights, multiplicities) for _ in range(count))
p0, p1 = F(3, 4), F(1, 2)
K = len(weights)


@lru_cache(None)
def full_dp(mask):
    if mask & (mask - 1) == 0:
        return weights[mask.bit_length() - 1]
    anchor = mask & -mask
    best = None
    sub = (mask - 1) & mask
    while sub:
        if sub & anchor:
            other = mask ^ sub
            if other:
                left, right = full_dp(sub), full_dp(other)
                candidate = min(max(left / p0, right / p1), max(left / p1, right / p0))
                best = candidate if best is None or candidate < best else best
        sub = (sub - 1) & mask
    return best


quotient_split_count = 0


@lru_cache(None)
def quotient_dp(counts):
    global quotient_split_count
    if sum(counts) == 1:
        index = next(i for i, count in enumerate(counts) if count)
        return class_weights[index]
    best = None
    for left in product(*(range(count + 1) for count in counts)):
        if sum(left) == 0 or left == counts:
            continue
        right = tuple(counts[i] - left[i] for i in range(len(counts)))
        if left > right:
            continue
        quotient_split_count += 1
        a, b = quotient_dp(tuple(left)), quotient_dp(right)
        candidate = min(max(a / p0, b / p1), max(a / p1, b / p0))
        best = candidate if best is None or candidate < best else best
    return best


full_optimum = full_dp((1 << K) - 1)
quotient_optimum = quotient_dp(multiplicities)
assert full_optimum == quotient_optimum == F(1, 2)
assert full_dp.cache_info().currsize == 2**K - 1
assert quotient_dp.cache_info().currsize == 47

# Every labeled subset with the same class-count vector has the same base multiset.
count_vectors_seen = set()
for mask in range(1, 1 << K):
    counts = []
    start = 0
    for multiplicity in multiplicities:
        counts.append(sum((mask >> i) & 1 for i in range(start, start + multiplicity)))
        start += multiplicity
    count_vectors_seen.add(tuple(counts))
assert len(count_vectors_seen) == 47

print({
    "banks": K,
    "weight_classes": len(class_weights),
    "labeled_subset_states": full_dp.cache_info().currsize,
    "orbit_subset_states": quotient_dp.cache_info().currsize,
    "quotient_splits_checked": quotient_split_count,
    "exact_optimum": str(quotient_optimum),
})
