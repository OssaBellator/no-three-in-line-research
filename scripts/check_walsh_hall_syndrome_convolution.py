#!/usr/bin/env python3
from functools import reduce
from operator import mul

RANK = 4
SIZE = 1 << RANK
A = {0, 1, 2, 4, 8, 15}
B = {0, 3, 5, 6, 9}
BLOCKS = [A, B, A, A, B, A, A, B, A, A, B, A]


def xor_convolve(vector, allowed):
    out = [0] * SIZE
    for syndrome, count in enumerate(vector):
        if count:
            for increment in allowed:
                out[syndrome ^ increment] += count
    return out


def walsh(vector):
    out = list(vector)
    step = 1
    while step < SIZE:
        for base in range(0, SIZE, 2 * step):
            for offset in range(step):
                i = base + offset
                j = i + step
                x, y = out[i], out[j]
                out[i], out[j] = x + y, x - y
        step *= 2
    return out

counts = [0] * SIZE
counts[0] = 1
for allowed in BLOCKS:
    counts = xor_convolve(counts, allowed)

spectrum = [1] * SIZE
for allowed in BLOCKS:
    indicator = [int(s in allowed) for s in range(SIZE)]
    transform = walsh(indicator)
    spectrum = [x * y for x, y in zip(spectrum, transform)]

inverse = walsh(spectrum)
assert all(value % SIZE == 0 for value in inverse)
walsh_counts = [value // SIZE for value in inverse]
assert walsh_counts == counts
assert sum(counts) == reduce(mul, (len(block) for block in BLOCKS), 1)
assert sum(counts) == 1_049_760_000
assert counts[0] == max(counts) == 65_622_784

prefix = [[0] * SIZE for _ in range(len(BLOCKS) + 1)]
prefix[0][0] = 1
for i, allowed in enumerate(BLOCKS):
    prefix[i + 1] = xor_convolve(prefix[i], allowed)

target = 7
assert prefix[-1][target] > 0
sequence = []
syndrome = target
for i in range(len(BLOCKS) - 1, -1, -1):
    for increment in sorted(BLOCKS[i]):
        previous = syndrome ^ increment
        if prefix[i][previous] > 0:
            sequence.append(increment)
            syndrome = previous
            break
    else:
        raise AssertionError("missing predecessor")
sequence.reverse()
assert reduce(lambda x, y: x ^ y, sequence, 0) == target

print({
    "rank": RANK,
    "blocks": len(BLOCKS),
    "ambient_syndromes": SIZE,
    "compatible_assignments": sum(counts),
    "zero_syndrome_count": counts[0],
    "maximum_count": max(counts),
    "reconstructed_target": target,
    "reconstructed_sequence": sequence,
})
