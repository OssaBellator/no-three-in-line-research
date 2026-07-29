#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

q = 3
outer = [(a, b, (a + b) % q) for a in range(q) for b in range(q)]

def weighted_distance(c, d, lengths):
    return sum(lengths[j] for j in range(3) if c[j] != d[j])

def minimum_weighted_distance(lengths):
    return min(
        weighted_distance(c, d, lengths)
        for i, c in enumerate(outer)
        for d in outer[i + 1 :]
    )

allocations = []
for l0 in range(1, 9):
    for l1 in range(1, 9):
        for l2 in range(1, 9):
            if l0 + l1 + l2 <= 8:
                lengths = (l0, l1, l2)
                allocations.append((lengths, minimum_weighted_distance(lengths)))

optimum = max(d for _, d in allocations)
optimal_allocations = sorted(lengths for lengths, d in allocations if d == optimum)
assert len(allocations) == 56
assert optimum == 5
assert optimal_allocations == [(2, 3, 3), (3, 2, 3), (3, 3, 2)]

lengths = optimal_allocations[0]

def concatenate(word):
    out = []
    for symbol, length in zip(word, lengths):
        out.extend([symbol] * length)
    return tuple(out)

code = [concatenate(c) for c in outer]
assert min(
    sum(x != y for x, y in zip(c, d))
    for i, c in enumerate(code)
    for d in code[i + 1 :]
) == 5

observations = set()
for word in code:
    for error_position in range(8):
        for replacement in range(q):
            if replacement == word[error_position]:
                continue
            remaining = [i for i in range(8) if i != error_position]
            for erased in combinations(remaining, 2):
                received = list(word)
                received[error_position] = replacement
                for i in erased:
                    received[i] = None
                observations.add(tuple(received))
    for erased in combinations(range(8), 4):
        received = list(word)
        for i in erased:
            received[i] = None
        observations.add(tuple(received))

def compatible(received, word):
    erasures = sum(x is None for x in received)
    errors = sum(
        x is not None and x != word[i] for i, x in enumerate(received)
    )
    return 2 * errors + erasures < optimum

list_sizes = Counter(
    sum(compatible(received, word) for word in code)
    for received in observations
)
assert len(observations) == 3654
assert list_sizes == Counter({1: 3654})

print({
    "outer_colors": len(outer),
    "allocation_candidates": len(allocations),
    "optimal_weighted_distance": optimum,
    "optimal_inner_lengths": optimal_allocations,
    "chosen_concatenated_length": sum(lengths),
    "checked_observations": len(observations),
    "compatibility_histogram": dict(list_sizes),
})
