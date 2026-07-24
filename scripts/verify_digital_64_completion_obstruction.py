#!/usr/bin/env python3
"""Verify the exact CMR44 covering certificate."""
from __future__ import annotations

from itertools import combinations
from math import gcd

SCALE = 500
MASKS = (25, 8, 2, 11, 52, 28)

X_WEIGHTS = {0: 427, 1: 283, 2: 394, 3: 427, 4: 338, 5: 286, 6: 144, 7: 349, 8: 312, 9: 209, 10: 210, 11: 280, 12: 158, 13: 146, 14: 120, 15: 47, 16: 82, 17: 65, 18: 114, 19: 321, 21: 69, 23: 114, 24: 8, 25: 151, 26: 218, 27: 280, 28: 47, 29: 218, 30: 22, 31: 47, 32: 47, 33: 22, 34: 218, 35: 47, 36: 280, 37: 218, 38: 151, 39: 8, 40: 114, 42: 69, 44: 321, 45: 114, 46: 65, 47: 82, 48: 47, 49: 120, 50: 146, 51: 158, 52: 280, 53: 210, 54: 209, 55: 312, 56: 349, 57: 144, 58: 286, 59: 338, 60: 427, 61: 394, 62: 283, 63: 427}

Y_WEIGHTS = {0: 343, 1: 454, 2: 381, 3: 356, 4: 349, 5: 283, 6: 355, 7: 299, 8: 283, 9: 125, 10: 221, 11: 107, 12: 232, 14: 107, 15: 221, 16: 46, 17: 74, 18: 157, 19: 61, 20: 56, 21: 74, 22: 74, 23: 292, 24: 126, 26: 215, 27: 268, 28: 107, 29: 190, 30: 23, 31: 107, 32: 107, 33: 23, 34: 190, 35: 107, 36: 268, 37: 215, 39: 126, 40: 292, 41: 74, 42: 74, 43: 56, 44: 61, 45: 157, 46: 74, 47: 46, 48: 221, 49: 107, 51: 232, 52: 107, 53: 221, 54: 125, 55: 283, 56: 299, 57: 355, 58: 283, 59: 349, 60: 356, 61: 381, 62: 454, 63: 343}

LINE_WEIGHTS = {
    (1, -1, -10): 56,
    (1, -1, -13): 74,
    (2, -1, -17): 45,
    (1, -2, -40): 18,
    (1, 2, 64): 93,
    (1, 9, 324): 59,
    (1, 1, 43): 103,
    (1, 2, 86): 35,
    (1, -1, -43): 25,
    (1, 1, 47): 29,
    (7, -1, -4): 56,
    (14, -15, -511): 112,
    (2, 1, 44): 42,
    (1, 1, 53): 130,
    (1, 1, 27): 128,
    (1, -1, -25): 56,
    (3, 5, 171): 52,
    (1, 1, 35): 33,
    (1, 1, 44): 34,
    (1, 1, 45): 51,
    (2, 3, 136): 47,
    (1, 1, 61): 8,
    (1, -2, -23): 18,
    (1, -2, -31): 91,
    (2, -1, -19): 18,
    (1, 1, 65): 8,
    (3, 5, 242): 89,
    (3, 5, 262): 89,
    (1, 3, 154): 74,
    (3, 7, 232): 35,
    (1, 3, 98): 74,
    (1, -1, -39): 26,
    (1, 1, 49): 39,
    (1, -6, -259): 91,
    (4, -1, 1): 48,
    (2, 1, 60): 137,
    (1, -1, -16): 16,
    (7, -2, -11): 19,
    (3, -1, -9): 18,
    (1, -3, -110): 28,
    (1, 1, 57): 198,
    (3, -1, 15): 65,
    (5, -2, 0): 3,
    (3, -1, 4): 39,
    (1, -2, -32): 91,
    (1, 1, 70): 217,
    (3, 7, 209): 3,
    (1, 3, 120): 41,
    (1, -5, -45): 94,
    (1, -6, -56): 91,
    (3, 2, 122): 1,
    (1, 1, 56): 217,
    (2, 3, 179): 47,
    (1, 1, 71): 108,
    (2, 1, 81): 134,
    (3, 5, 333): 52,
    (1, 1, 73): 130,
    (1, 1, 51): 218,
    (1, -7, -373): 33,
    (3, 7, 421): 3,
    (3, 1, 97): 73,
    (1, -1, 13): 74,
    (1, 1, 69): 198,
    (1, 2, 125): 93,
    (1, 1, 55): 108,
    (9, 10, 695): 48,
    (2, 1, 92): 63,
    (1, 1, 77): 39,
    (4, 1, 122): 99,
    (1, 1, 39): 125,
    (1, 1, 79): 29,
    (1, 3, 89): 169,
    (1, 4, 233): 14,
    (9, 10, 502): 48,
    (1, -5, -207): 94,
    (1, 1, 75): 218,
    (1, -1, 10): 56,
    (1, 2, 103): 35,
    (2, 1, 97): 63,
    (9, -2, 181): 77,
    (3, -1, 59): 7,
    (1, 1, 81): 51,
    (1, 1, 82): 34,
    (1, 1, 83): 103,
    (2, 15, 809): 75,
    (26, 17, 1626): 8,
    (3, -1, 67): 7,
    (3, 7, 398): 35,
    (2, 1, 108): 134,
    (3, 2, 193): 1,
    (26, 17, 1083): 8,
    (1, 1, 87): 125,
    (6, -1, 142): 60,
    (1, 3, 163): 169,
    (1, -3, -16): 28,
    (2, 15, 262): 75,
    (1, 4, 82): 14,
    (1, -1, 25): 56,
    (9, -2, 260): 77,
    (1, -7, -5): 33,
    (14, -15, 448): 112,
    (1, 1, 91): 33,
    (3, 1, 155): 73,
    (4, 1, 193): 99,
    (2, 1, 129): 137,
    (6, -1, 173): 60,
    (1, 1, 99): 128,
    (1, -1, 39): 26,
    (5, -2, 189): 3,
    (2, -1, 80): 45,
    (3, -1, 122): 39,
    (3, -1, 111): 65,
    (2, -1, 82): 18,
    (1, -1, 16): 16,
    (1, 3, 132): 41,
    (1, 9, 306): 59,
    (1, -1, 43): 25,
    (3, -1, 135): 18,
    (4, -1, 188): 48,
    (7, -2, 326): 19,
    (2, 1, 145): 42,
    (7, -1, 382): 56,
}


def digital_permutation() -> list[int]:
    return [
        sum((((x & mask).bit_count() & 1) << i) for i, mask in enumerate(MASKS))
        for x in range(64)
    ]


def determinant(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def line_key(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int, int]:
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1
    common = gcd(gcd(abs(A), abs(B)), abs(C))
    if common:
        A //= common
        B //= common
        C //= common
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def has_perfect_matching(candidates: list[tuple[int, int]]) -> bool:
    neighbours = [[] for _ in range(64)]
    for x, y in candidates:
        neighbours[x].append(y)

    matched_x = [-1] * 64

    def augment(x: int, seen: set[int]) -> bool:
        for y in neighbours[x]:
            if y in seen:
                continue
            seen.add(y)
            if matched_x[y] == -1 or augment(matched_x[y], seen):
                matched_x[y] = x
                return True
        return False

    return all(augment(x, set()) for x in range(64))


def main() -> None:
    values = digital_permutation()
    assert sorted(values) == list(range(64))
    fixed = [(x, values[x]) for x in range(64)]
    assert all(determinant(*triple) != 0 for triple in combinations(fixed, 3))

    fixed_secants = {line_key(a, b) for a, b in combinations(fixed, 2)}
    candidates = []
    for x in range(64):
        for y in range(64):
            if y == values[x]:
                continue
            if any(A * x + B * y == C for A, B, C in fixed_secants):
                continue
            candidates.append((x, y))

    assert len(candidates) == 390
    counts_by_x = [sum(1 for cx, _ in candidates if cx == x) for x in range(64)]
    assert min(counts_by_x) == 3 and max(counts_by_x) == 13
    assert has_perfect_matching(candidates)

    for line in LINE_WEIGHTS:
        A, B, C = line
        fixed_count = sum(1 for x, y in fixed if A * x + B * y == C)
        candidate_count = sum(1 for x, y in candidates if A * x + B * y == C)
        assert fixed_count == 1
        assert candidate_count >= 2
        assert line_key(
            next(point for point in candidates if A * point[0] + B * point[1] == C),
            next(
                point
                for point in reversed(candidates)
                if A * point[0] + B * point[1] == C
            ),
        ) == line

    minimum_coverage = 10**9
    for x, y in candidates:
        coverage = X_WEIGHTS.get(x, 0) + Y_WEIGHTS.get(y, 0)
        coverage += sum(
            weight
            for (A, B, C), weight in LINE_WEIGHTS.items()
            if A * x + B * y == C
        )
        minimum_coverage = min(minimum_coverage, coverage)
        assert coverage >= SCALE

    capacity = sum(X_WEIGHTS.values()) + sum(Y_WEIGHTS.values()) + sum(LINE_WEIGHTS.values())
    assert minimum_coverage == 501
    assert capacity == 31718
    assert capacity < 64 * SCALE

    print(
        f"verified CMR44: candidates={len(candidates)}, lines={len(LINE_WEIGHTS)}, "
        f"minimum-coverage={minimum_coverage}, capacity={capacity}, "
        f"required={64 * SCALE}"
    )


if __name__ == "__main__":
    main()
