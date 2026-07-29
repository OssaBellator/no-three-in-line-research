#!/usr/bin/env python3
from fractions import Fraction

N = 5
R = [Fraction(6,5), Fraction(5,4), Fraction(4,3), Fraction(7,6), Fraction(9,8)]
B = [Fraction(1,5), Fraction(1,6), Fraction(0), Fraction(0), Fraction(0)]
C = [Fraction(0), Fraction(0), Fraction(1,10), Fraction(1,12), Fraction(1,4)]
A = {
    (0,1): Fraction(1,10),
    (0,2): Fraction(1,12),
    (1,3): Fraction(1,8),
    (2,3): Fraction(1,9),
    (1,4): Fraction(1,20),
    (3,4): Fraction(1,7),
}


def forward(Rv, Av):
    F = [Fraction(0) for _ in range(N)]
    U = [Fraction(0) for _ in range(N)]
    for j in range(N):
        U[j] = B[j] + sum(F[i] * Av.get((i,j), 0) for i in range(j))
        F[j] = U[j] * Rv[j]
    return U, F


def backward(Rv, Av):
    G = [Fraction(0) for _ in range(N)]
    V = [Fraction(0) for _ in range(N)]
    for i in reversed(range(N)):
        V[i] = C[i] + sum(Av.get((i,j), 0) * G[j] for j in range(i+1, N))
        G[i] = Rv[i] * V[i]
    return V, G


def correction(Rv, Av):
    _, F = forward(Rv, Av)
    return sum(F[i] * C[i] for i in range(N))

U, F = forward(R, A)
V, G = backward(R, A)
K = correction(R, A)
assert K == sum(B[i] * G[i] for i in range(N))

# Exact single-block sensitivities: every condensation path uses a block at most once.
for (u,v), value in A.items():
    delta = Fraction(1,1000)
    A2 = dict(A)
    A2[(u,v)] = value + delta
    exact_change = correction(R, A2) - K
    predicted = F[u] * delta * G[v]
    assert exact_change == predicted

for i in range(N):
    delta = Fraction(1,1000)
    R2 = list(R)
    R2[i] += delta
    exact_change = correction(R2, A) - K
    predicted = U[i] * delta * V[i]
    assert exact_change == predicted

# Simultaneous monotone perturbations are bounded by all-upper forward/backward prices.
dA = {(0,1): Fraction(1,200), (3,4): Fraction(1,300)}
dR = {2: Fraction(1,250)}
Aplus = dict(A)
for edge, delta in dA.items():
    Aplus[edge] += delta
Rplus = list(R)
for i, delta in dR.items():
    Rplus[i] += delta
Kplus = correction(Rplus, Aplus)
Uplus, Fplus = forward(Rplus, Aplus)
Vplus, Gplus = backward(Rplus, Aplus)
bound = sum(Fplus[u] * delta * Gplus[v] for (u,v), delta in dA.items())
bound += sum(Uplus[i] * delta * Vplus[i] for i, delta in dR.items())
assert Fraction(0) <= Kplus - K <= bound

print({
    "base_correction": str(K),
    "forward_prices": [str(x) for x in F],
    "backward_prices": [str(x) for x in G],
    "simultaneous_change": str(Kplus-K),
    "all_upper_bound": str(bound),
    "edge_sensitivities_checked": len(A),
    "resolvent_sensitivities_checked": N,
})
