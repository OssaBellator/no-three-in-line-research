#!/usr/bin/env python3
from fractions import Fraction
import json

F = Fraction
A = [[F(1,4), F(1,10)], [F(1,5), F(1,4)]]
B = [[F(1,10)], [F(1,20)]]
C = [[F(1,8), F(1,10)]]
D = [[F(1,3)]]

def matmul(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

def matadd(X, Y):
    return [[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def matsub(X, Y):
    return [[X[i][j]-Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def inv2(M):
    det = M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert det != 0
    return [[M[1][1]/det, -M[0][1]/det], [-M[1][0]/det, M[0][0]/det]]

def mv(M, v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]

RA = inv2(matsub(eye(2), A))
S = matadd(D, matmul(matmul(C, RA), B))
s = S[0][0]
assert s < 1

aX = [F(1), F(1)]
aY = [F(1)]
qX = max(mv(A, aX))
b = max(mv(B, aY))
c = mv(C, aX)[0]
d = D[0][0]
scalar_bound = d + b*c/(1-qX)
assert qX == F(9,20)
assert scalar_bound < 1

base = mv(RA, mv(B, aY))
eps = F(1,10)
x = [z + eps for z in base]
full = [A[0] + B[0], A[1] + B[1], C[0] + D[0]]
vec = x + aY
image = mv(full, vec)
assert all(image[i] < vec[i] for i in range(3))

T = 4
At = eye(2)
partial = D
for _ in range(T):
    partial = matadd(partial, matmul(matmul(C, At), B))
    At = matmul(At, A)
tail_exact = s - partial[0][0]
tail_bound = b*c*(qX**T)/(1-qX)
assert tail_exact >= 0 and tail_exact <= tail_bound
eta = 1 - partial[0][0]
assert tail_bound < eta

print(json.dumps({
    "all_checks_passed": True,
    "resolvent_A": [[str(z) for z in row] for row in RA],
    "schur_complement": str(s),
    "transient_q": str(qX),
    "scalar_core_bound": str(scalar_bound),
    "strict_supersolution": [str(z) for z in vec],
    "truncation_depth": T,
    "exact_tail": str(tail_exact),
    "tail_bound": str(tail_bound),
    "remaining_margin": str(eta),
}, indent=2))
