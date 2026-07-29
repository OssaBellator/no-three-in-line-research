#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
from math import comb

p0, p1 = F(3, 4), F(2, 3)
risks = (F(1, 32), F(1, 16), F(1, 8))
full = (3, 3, 2)

def subvectors(m):
    for a in range(m[0] + 1):
        for b in range(m[1] + 1):
            for c in range(m[2] + 1):
                v = (a, b, c)
                if v != (0, 0, 0) and v != m:
                    yield v

def minus(m, a):
    return tuple(m[i] - a[i] for i in range(3))

@lru_cache(None)
def value(m):
    if sum(m) == 1:
        i = next(i for i, x in enumerate(m) if x)
        return risks[i]
    return min(max(value(a) / p0, value(minus(m, a)) / p1) for a in subvectors(m))

@lru_cache(None)
def count_labeled_optima(m):
    if sum(m) == 1:
        return 1
    optimum = value(m)
    total = 0
    for a in subvectors(m):
        b = minus(m, a)
        if max(value(a) / p0, value(b) / p1) != optimum:
            continue
        choices = 1
        for i in range(3):
            choices *= comb(m[i], a[i])
        total += choices * count_labeled_optima(a) * count_labeled_optima(b)
    return total

labels = (
    ("a0", "a1", "a2"),
    ("b0", "b1", "b2"),
    ("c0", "c1"),
)

def reconstruct(m, available, prefix=""):
    if sum(m) == 1:
        i = next(i for i, x in enumerate(m) if x)
        return {available[i][0]: prefix}
    optimum = value(m)
    candidates = []
    for a in subvectors(m):
        b = minus(m, a)
        if max(value(a) / p0, value(b) / p1) == optimum:
            candidates.append(a)
    a = min(candidates)
    b = minus(m, a)
    left = tuple(tuple(available[i][:a[i]]) for i in range(3))
    right = tuple(tuple(available[i][a[i]:]) for i in range(3))
    out = reconstruct(a, left, prefix + "0")
    out.update(reconstruct(b, right, prefix + "1"))
    return out

code = reconstruct(full, labels)
assert len(code) == 8
words = list(code.values())
assert all(not v.startswith(u) for i, u in enumerate(words) for j, v in enumerate(words) if i != j)

risk_by_label = {lab: risks[i] for i, group in enumerate(labels) for lab in group}
def survival(word):
    s = F(1)
    for bit in word:
        s *= p0 if bit == "0" else p1
    return s

max_risk = max(risk_by_label[lab] / survival(word) for lab, word in code.items())
assert max_risk == value(full) == F(1, 4)
assert count_labeled_optima(full) == 2304

print({
    "quotient_states": (full[0] + 1) * (full[1] + 1) * (full[2] + 1) - 1,
    "exact_optimum": str(value(full)),
    "labeled_optimal_codes": count_labeled_optima(full),
    "reconstructed_code": dict(sorted(code.items())),
})
