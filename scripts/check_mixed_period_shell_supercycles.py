#!/usr/bin/env python3
from fractions import Fraction
from math import lcm

E = {"A": (1, 0, 0), "B": (0, 1, 0), "C": (0, 0, 1)}
W1 = "AB"
W2 = "AAB"
L = lcm(len(W1), len(W2))
assert L == 6
TARGET = tuple(
    Fraction(sum(E[x][j] for x in W1), len(W1))
    + Fraction(sum(E[x][j] for x in W2), len(W2))
    for j in range(3)
)
assert TARGET == (Fraction(7, 6), Fraction(5, 6), Fraction(0))


def phase_record(p1, p2):
    cumulative = [Fraction(0), Fraction(0), Fraction(0)]
    minima = [Fraction(0), Fraction(0), Fraction(0)]
    word = []
    centered = []
    for t in range(L):
        a = W1[(t + p1) % len(W1)]
        b = W2[(t + p2) % len(W2)]
        word.append(a + b)
        service = tuple(E[a][j] + E[b][j] for j in range(3))
        increment = tuple(Fraction(service[j]) - TARGET[j] for j in range(3))
        centered.append(increment)
        for j in range(3):
            cumulative[j] += increment[j]
            minima[j] = min(minima[j], cumulative[j])
    assert cumulative == [0, 0, 0]
    buffer = tuple(-x for x in minima)
    return buffer, tuple(word), tuple(centered)


records = {}
for p1 in range(len(W1)):
    for p2 in range(len(W2)):
        records[(p1, p2)] = phase_record(p1, p2)

linf = {phase: max(buffer) for phase, (buffer, _, _) in records.items()}
assert sorted(linf.values()) == [Fraction(2, 3), Fraction(2, 3), Fraction(5, 6), Fraction(5, 6), Fraction(7, 6), Fraction(7, 6)]
best = sorted(phase for phase, value in linf.items() if value == min(linf.values()))
assert best == [(0, 2), (1, 0)]
phase = best[0]
buffer, word, centered = records[phase]
assert buffer == (Fraction(2, 3), Fraction(1, 2), Fraction(0))
assert word == ("AB", "BA", "AA", "BB", "AA", "BA")
assert sum(buffer) == Fraction(7, 6)

reserve = list(buffer)
for t in range(120):
    increment = centered[t % L]
    for j in range(3):
        reserve[j] += increment[j]
        assert reserve[j] >= 0

print({
    "phase_pairs_checked": len(records),
    "superperiod": L,
    "target": tuple(map(str, TARGET)),
    "optimal_phases": best,
    "minimum_linf_buffer": "2/3",
    "lexicographic_buffer": tuple(map(str, buffer)),
    "supercycle": word,
    "prefixes_checked": 120,
    "status": "passed",
})
