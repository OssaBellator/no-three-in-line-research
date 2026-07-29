#!/usr/bin/env python3
from fractions import Fraction


def mat_identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]

def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mat_inverse(A):
    n = len(A)
    aug = [A[i][:] + mat_identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor:
                aug[r] = [aug[r][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]

n = 5
diag = [Fraction(1, 5), Fraction(1, 4), Fraction(1, 6), Fraction(1, 3), Fraction(1, 7)]
A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
for i, x in enumerate(diag):
    A[i][i] = x
for i, j, x in [
    (0, 1, Fraction(1, 10)), (0, 2, Fraction(1, 12)),
    (1, 3, Fraction(1, 9)), (2, 3, Fraction(1, 8)),
    (1, 4, Fraction(1, 14)), (3, 4, Fraction(1, 11)),
]:
    A[i][j] = x
R = [1 / (1 - diag[i]) for i in range(n)]
Inv = mat_inverse(mat_sub(mat_identity(n), A))

# Transfer recurrence from every possible start.
for s in range(n):
    T = [Fraction(0) for _ in range(n)]
    T[s] = R[s]
    for j in range(s + 1, n):
        T[j] = sum(T[i] * A[i][j] for i in range(s, j)) * R[j]
    for j in range(n):
        expected = Inv[s][j] if j >= s else 0
        assert T[j] == expected

B = [Fraction(1, 13), Fraction(1, 17), Fraction(0), Fraction(1, 19), Fraction(0)]
C = [Fraction(0), Fraction(1, 23), Fraction(1, 29), Fraction(0), Fraction(1, 31)]
U = [Fraction(0) for _ in range(n)]
for j in range(n):
    U[j] = (B[j] + sum(U[i] * A[i][j] for i in range(j))) * R[j]
correction = sum(U[j] * C[j] for j in range(n))
direct = sum(B[i] * Inv[i][j] * C[j] for i in range(n) for j in range(n))
assert correction == direct

# Scalar interval propagation.
Rminus = [r - Fraction(1, 100) for r in R]
Rplus = [r + Fraction(1, 100) for r in R]
Aminus = [[max(Fraction(0), A[i][j] - Fraction(1, 1000)) for j in range(n)] for i in range(n)]
Aplus = [[A[i][j] + (Fraction(1, 1000) if i < j and A[i][j] else 0) for j in range(n)] for i in range(n)]

def core_dp(Rdata, Adata):
    V = [Fraction(0) for _ in range(n)]
    for j in range(n):
        V[j] = (B[j] + sum(V[i] * Adata[i][j] for i in range(j))) * Rdata[j]
    return sum(V[j] * C[j] for j in range(n))

lower = core_dp(Rminus, Aminus)
upper = core_dp(Rplus, Aplus)
assert lower <= correction <= upper
print({
    "components": n,
    "exact_core_correction": str(correction),
    "interval_lower": str(lower),
    "interval_upper": str(upper),
    "direct_inverse_match": True,
})
