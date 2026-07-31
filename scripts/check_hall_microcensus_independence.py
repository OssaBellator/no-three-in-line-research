#!/usr/bin/env python3
import json
from itertools import product
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "certificates" / "prime-patching-provenance-audit-555-560.json"
record = json.loads(DATA.read_text())["frontiers"]["hall"]
KERNELS = tuple(tuple(tuple(row) for row in kernel) for kernel in record["quotient_kernels"])
FIBRES = tuple(tuple(fibre) for fibre in record["syndrome_partition"])

assert record["evidence_level"] == "fixture_derived"
assert record["independent_geometric_source"] is None
assert record["microscopic_construction"].startswith("balanced")


def balanced_block(k):
    hi = (k + 1) // 2
    lo = k // 2
    return ((hi, lo), (lo, hi))


def diagonal_block(k):
    return ((k, 0), (0, k))


def lift(kernel, block_builder):
    matrix = [[0] * 6 for _ in range(6)]
    for i in range(3):
        for j in range(3):
            block = block_builder(kernel[i][j])
            for u in range(2):
                for v in range(2):
                    matrix[2 * i + u][2 * j + v] = block[u][v]
    return tuple(tuple(row) for row in matrix)


def check_lumpability(kernel, micro):
    assert all(sum(row) == 4 for row in micro)
    assert all(sum(micro[i][j] for i in range(6)) == 4 for j in range(6))
    for syndrome, fibre in enumerate(FIBRES):
        for state in fibre:
            for target, target_fibre in enumerate(FIBRES):
                assert sum(micro[state][u] for u in target_fibre) == kernel[syndrome][target]


def multiply(vector, matrix):
    return [sum(vector[i] * matrix[i][j] for i in range(len(vector))) for j in range(len(matrix[0]))]


def aggregate(vector):
    return [sum(vector[state] for state in fibre) for fibre in FIBRES]

balanced = tuple(lift(kernel, balanced_block) for kernel in KERNELS)
diagonal = tuple(lift(kernel, diagonal_block) for kernel in KERNELS)
assert balanced != diagonal
for kernel, first, second in zip(KERNELS, balanced, diagonal):
    check_lumpability(kernel, first)
    check_lumpability(kernel, second)

# The two genuinely different microcensuses have identical quotient evolution.
words_checked = 0
for length in range(8):
    for word in product(range(2), repeat=length):
        for start in range(6):
            quotient = [0, 0, 0]
            quotient[start // 2] = 1
            vectors = []
            for family in (balanced, diagonal):
                vector = [0] * 6
                vector[start] = 1
                for symbol in word:
                    vector = multiply(vector, family[symbol])
                vectors.append(aggregate(vector))
            for symbol in word:
                quotient = multiply(quotient, KERNELS[symbol])
            assert vectors[0] == quotient == vectors[1]
        words_checked += 1

assert len(record["required_for_promotion"]) == 5
print({
    "quotient_kernels": len(KERNELS),
    "distinct_strongly_lumpable_microcensuses": 2,
    "microcensus_rows": 6,
    "switch_words_compared": words_checked,
    "quotient_does_not_identify_microgeometry": True,
    "independent_census_present": False,
    "status": "passed",
})
