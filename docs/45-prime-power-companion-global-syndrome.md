# Global line, energy, and syndrome bounds for the companion host

Let `N=p^k` with `p` odd,

\[
f=R_{\mathbf c},
\qquad
g=\sigma_p\circ f,
\qquad
\sigma_p(y)=[(1+p)y+1]_N,
\]

and let `S` be the union of the two permutation graphs. Put

\[
A_{p,k}=(p+2)(2k+2),
\qquad
B_p=2\bigl((p+1)^2+1\bigr)\sqrt N.
\]

## 1. Full direction-sensitive line cap

### Theorem CMR40 — PROVED

Every real line of primitive direction height `H` satisfies

\[
|L\cap S|\le A_{p,k}+\frac{B_p}{H}.
\]

### Proof

Write the primitive line equation as `Ax+Bz=C`. The first layer contributes at
most

\[
2k+2+\frac{2\sqrt N}{H}
\]

points by CMR31. For a first-layer row `y`, define

\[
q(y)=\left\lfloor\frac{(1+p)y+1}{N}\right\rfloor.
\]

This carry takes at most `p+1` values. In one fixed carry cell, companion points
on the line correspond to first-layer points on

\[
Ax+B(1+p)y=C-B+BNq.
\]

After primitive reduction, the new direction height is at least `H/(p+1)`,
because the common divisor of `A` and `(p+1)B` divides `p+1`. CMR31 bounds one
cell by

\[
2k+2+\frac{2(p+1)\sqrt N}{H}.
\]

Sum the `p+1` companion cells and the first layer. ∎

## 2. Harmonic energy

Define

\[
\mathcal E(S)=\sum_{\{P,Q\}\subset S}\frac1{H(P,Q)}.
\]

### Theorem CMR41 — PROVED

For every `1<=K<N`,

\[
\mathcal E(S)
\le
4N(A_{p,k}-1)K
+4NB_p\sum_{H=1}^K\frac1H
+\frac1K\binom{2N}{2}.
\]

Hence

\[
\mathcal E(S)
=O\bigl(p^2N^{3/2}\log N+pkN^{3/2}\bigr).
\]

### Proof

For one primitive direction, its parallel lines partition the `2N` points.
CMR40 implies at most `N(L_H-1)` pairs in that direction, where
`L_H=A_{p,k}+B_p/H`. There are at most `4H` directions of exact height `H`, so
the weighted energy at height `H` is at most `4N(L_H-1)`. Sum through `K`; the
remaining pairs each have weight at most `1/K`. Take `K=floor(sqrt(N))`. ∎

## 3. Full companion syndrome

### Corollary CMR42 — PROVED

The number of unordered real triples in the saturated union satisfies

\[
T(S)
\le
\frac{A_{p,k}-2}{3}\binom{2N}{2}
+\frac{B_p}{3}\mathcal E(S).
\]

For every fixed odd prime base,

\[
T(S)=O_p(N^2\log N).
\]

### Proof

On a line of occupancy `s` and height `H`, CMR40 gives

\[
\binom s3
\le
\left(\frac{A_{p,k}-2}{3}+\frac{B_p}{3H}\right)\binom s2.
\]

Summing uses the total pair count `binom(2N,2)` and the definition of harmonic
energy. ∎

The exact checks are in
[`scripts/verify_prime_power_companion_global.py`](../scripts/verify_prime_power_companion_global.py).
