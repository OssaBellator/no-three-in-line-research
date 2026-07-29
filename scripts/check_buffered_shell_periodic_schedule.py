#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

COUNTS = (5, 7, 3, 5)  # x1,x2,x3,idle in a period of 20
TARGETS = (Fraction(3, 5), Fraction(1, 2), Fraction(2, 5))
SYMS = "123I"

@lru_cache(None)
def solve(state):
    if state == COUNTS:
        return Fraction(0), ""
    t = sum(state)
    best = None
    for j in range(4):
        if state[j] == COUNTS[j]:
            continue
        ns = list(state)
        ns[j] += 1
        ns = tuple(ns)
        future, suffix = solve(ns)
        nt = t + 1
        deficits = (
            TARGETS[0] * nt - (ns[0] + ns[1]),
            TARGETS[1] * nt - (ns[1] + ns[2]),
            TARGETS[2] * nt - (ns[2] + ns[0]),
        )
        current = max(Fraction(0), *deficits)
        candidate = (max(current, future), SYMS[j] + suffix)
        if best is None or candidate < best:
            best = candidate
    return best

max_deficit, word = solve((0, 0, 0, 0))
assert word == "213121212122233IIIII"
assert max_deficit == Fraction(2, 5)

used = [0, 0, 0]
component_max = [Fraction(0), Fraction(0), Fraction(0)]
for t, symbol in enumerate(word, 1):
    if symbol != "I":
        used[int(symbol) - 1] += 1
    deficits = (
        TARGETS[0] * t - (used[0] + used[1]),
        TARGETS[1] * t - (used[1] + used[2]),
        TARGETS[2] * t - (used[2] + used[0]),
    )
    component_max = [max(component_max[i], deficits[i]) for i in range(3)]

assert tuple(component_max) == (0, 0, Fraction(2, 5))
# Buffer b=(2/5,0,0) covers all cycle deficits and is optimal because at t=1
# one of the three pair constraints must miss by at least 2/5.
buffer = (Fraction(2, 5), Fraction(0), Fraction(0))
for n in range(1, 101):
    used = [0, 0, 0]
    for t in range(1, n + 1):
        symbol = word[(t - 1) % len(word)]
        if symbol != "I":
            used[int(symbol) - 1] += 1
        assert buffer[0] + buffer[1] + used[0] + used[1] >= TARGETS[0] * t
        assert buffer[1] + buffer[2] + used[1] + used[2] >= TARGETS[1] * t
        assert buffer[2] + buffer[0] + used[2] + used[0] >= TARGETS[2] * t

print({
    "period": 20,
    "word": word,
    "attenuation_counts": COUNTS[:3],
    "idle_slots": COUNTS[3],
    "cycle_prefix_deficits": tuple(str(x) for x in component_max),
    "minimum_startup_buffer": tuple(str(x) for x in buffer),
    "average_overhead": "2/(5N)",
})
