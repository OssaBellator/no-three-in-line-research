#!/usr/bin/env python3
from fractions import Fraction


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def inv(A):
    n = len(A)
    M = [row[:] + eye(n)[i] for i, row in enumerate(A)]
    for c in range(n):
        pivot = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[pivot] = M[pivot], M[c]
        z = M[c][c]
        M[c] = [x / z for x in M[c]]
        for r in range(n):
            if r == c:
                continue
            z = M[r][c]
            if z:
                M[r] = [M[r][j] - z * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def leq(A, B):
    return all(A[i][j] <= B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def main():
    a1, a2, a3 = Fraction(1, 4), Fraction(1, 3), Fraction(1, 5)
    k12, k13, k23 = Fraction(1, 10), Fraction(1, 20), Fraction(1, 8)
    A = [
        [a1, k12, k13],
        [0, a2, k23],
        [0, 0, a3],
    ]
    G = inv(sub(eye(3), A))
    R1, R2, R3 = 1 / (1 - a1), 1 / (1 - a2), 1 / (1 - a3)

    P = [
        [R1, R1 * k12 * R2, R1 * k13 * R3 + R1 * k12 * R2 * k23 * R3],
        [0, R2, R2 * k23 * R3],
        [0, 0, R3],
    ]
    assert G == P

    B11 = R1
    B12 = R2 * B11 * k12
    B13 = R3 * (B11 * k13 + B12 * k23)
    assert B12 == G[0][1] and B13 == G[0][2]

    lower = [Fraction(1), Fraction(1), Fraction(1)]
    upper = [R1 + Fraction(1, 100), R2 + Fraction(1, 100), R3 + Fraction(1, 100)]
    L = [
        [lower[0], lower[0] * k12 * lower[1], lower[0] * k13 * lower[2] + lower[0] * k12 * lower[1] * k23 * lower[2]],
        [0, lower[1], lower[1] * k23 * lower[2]],
        [0, 0, lower[2]],
    ]
    U = [
        [upper[0], upper[0] * k12 * upper[1], upper[0] * k13 * upper[2] + upper[0] * k12 * upper[1] * k23 * upper[2]],
        [0, upper[1], upper[1] * k23 * upper[2]],
        [0, 0, upper[2]],
    ]
    assert leq(L, G) and leq(G, U)

    print({
        "all_checks_passed": True,
        "global_resolvent": [[str(x) for x in row] for row in G],
        "path_1_to_3": str(B13),
        "interval_certified": True,
    })


if __name__ == "__main__":
    main()
