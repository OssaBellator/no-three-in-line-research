#!/usr/bin/env python3
from fractions import Fraction

MATRIX = (
    (2, 1, 1, 0),
    (1, 2, 0, 1),
    (1, 0, 2, 1),
)
M = 4

# Fixed balanced binary router tree: {0,1}|{2,3}, then split each pair.
def mechanical_word(left: int, right: int):
    total = left + right
    if total == 0:
        return []
    out = []
    sent_left = 0
    for t in range(1, total + 1):
        # Send left exactly when the floor count increases.
        want = (t * left) // total
        if want > sent_left:
            out.append(0)
            sent_left += 1
        else:
            out.append(1)
    assert out.count(0) == left and out.count(1) == right
    return out

def route_row(counts):
    left_total = counts[0] + counts[1]
    right_total = counts[2] + counts[3]
    root = mechanical_word(left_total, right_total)
    left = iter(mechanical_word(counts[0], counts[1]))
    right = iter(mechanical_word(counts[2], counts[3]))
    word = []
    for side in root:
        local = next(left) if side == 0 else next(right)
        word.append(local if side == 0 else 2 + local)
    return word

words = [route_row(row) for row in MATRIX]
for i, word in enumerate(words):
    assert tuple(word.count(j) for j in range(4)) == MATRIX[i]

row_max = Fraction(0)
global_max = Fraction(0)
for t in range(1, M + 1):
    for i, word in enumerate(words):
        for j in range(4):
            actual = sum(x == j for x in word[:t])
            ideal = Fraction(t * MATRIX[i][j], M)
            row_max = max(row_max, abs(actual - ideal))
    for j in range(4):
        actual = sum(sum(x == j for x in word[:t]) for word in words)
        total_j = sum(row[j] for row in MATRIX)
        ideal = Fraction(t * total_j, M)
        global_max = max(global_max, abs(actual - ideal))

assert row_max <= 2  # router depth
assert global_max <= 6  # three rows times depth two
assert tuple(sum(row[j] for row in MATRIX) for j in range(4)) == (4, 3, 3, 2)

print({
    "rows": tuple("".join("ABCD"[x] for x in w) for w in words),
    "row_prefix_discrepancy": str(row_max),
    "global_prefix_discrepancy": str(global_max),
    "row_totals": (4, 4, 4),
    "column_totals": (4, 3, 3, 2),
})
