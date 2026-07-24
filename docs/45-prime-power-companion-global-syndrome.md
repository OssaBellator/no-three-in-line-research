# Global line, energy, and syndrome bounds for the companion host

The completed-reciprocal companion pair is saturated and Hamiltonian, but its
full same-/cross-layer syndrome previously had no general quantitative bound.
The companion carry partition and the CMR31 direction cap give a first
unconditional estimate.

Let `N=p^k` with `p` odd. Write

\[
f=R_{\mathbf c},
\qquad
g=\sigma_p\circ f,
\qquad
\sigma_p(y)=[(1+p)y+1]_N,
\]

and let `S` be the union of the two permutation graphs. Thus `|S|=2N`.

For a real line of primitive direction height `H`, put

\[
A_{p,k}=(p+2)(2k+2),
\qquad
B_p=2\bigl((p+1)^2+1\bigr)\sqrt N.
\]

## 1. Direction-sensitive line cap for both layers

### Theorem CMR40 — PROVED

Every real line `L` of primitive direction height `H` satisfies

\[
|L\cap S|
\le
A_{p,k}+\frac{B_p}{H}.
\]

### Proof

Write the primitive line equation as

\[
Ax+Bz=C,
\qquad \gcd(A,B)=1,
\qquad H=\max(|A|,|B|).
\]

The first layer contributes at most

\[
2k+2+\frac{2\sqrt N}{H}
\]

points by CMR31.

For a first-layer row `y`, define its companion carry

\[
q(y)=\left\lfloor\frac{(1+p)y+1}{N}\right\rfloor.
\]

It takes at most `p+1` values, namely `0,...,p`. In one fixed carry cell the
companion line equation becomes

\[
Ax+B(1+p)y=C-B+BNq.
\]

After primitive reduction its direction height `H'` obeys

\[
H'\ge\frac{H}{p+1}.
\]

Indeed the new normal is `(A,(p+1)B)`, and its common divisor is
`gcd(A,p+1)<=p+1`. CMR31 therefore bounds one carry cell by

\[
2k+2+\frac{2(p+1)\sqrt N}{H}.
\]

Multiplying by the `p+1` carry values and adding the first layer gives the
stated constants. ∎

## 2. Harmonic energy of the two-layer host

Define

\[
\mathcal E(S)=\sum_{\{P,Q\}\subset S}\frac1{H(P,Q)}.
\]

### Theorem CMR41 — PROVED

For every integer `1<=K<N`,

\[
\mathcal E(S)
\le
4N(A_{p,k}-1)K
+4NB_p\sum_{H=1}^K\frac1H
+\frac1K\binom{2N}{2}.
\]

Consequently

\[
\mathcal E(S)
=O\bigl(p^2N^{3/2}\log N+pkN^{3/2}\bigr).
\]

### Proof

For one primitive direction of height `H`, its parallel lines partition the
`2N` points. CMR40 and

\[
\binom s2\le\frac{L_H-1}{2}s,
\qquad
L_H=A_{p,k}+B_p/H,
\]

show that the number of pairs in that direction is at most

\[
N(L_H-1).
\]

There are at most `4H` unoriented primitive directions of exact height `H`,
including the horizontal and vertical directions at height one. After division
by `H`, the energy at exact height `H` is at most `4N(L_H-1)`. Sum this for
`H<=K`; every remaining pair contributes at most `1/K`. Taking
`K=floor(sqrt(N))` proves the asymptotic estimate. ∎

## 3. Full same-/cross-layer syndrome

Let `T(S)` be the number of unordered real collinear triples in the saturated
union, including all layer patterns.

### Corollary CMR42 — PROVED

One has

\[
T(S)
\le
\frac{A_{p,k}-2}{3}\binom{2N}{2}
+\frac{B_p}{3}\mathcal E(S).
\]

In particular, for every fixed odd prime base `p`,

\[
T(S)=O_p(N^2\log N).
\]

More generally the displayed bounds give

\[
T(S)=O\bigl(p^4N^2\log N+p^3kN^2+pkN^2\bigr).
\]

### Proof

For every occupied real line, with occupancy `s` and direction height `H`,
CMR40 gives

\[
\binom s3
=\frac{s-2}{3}\binom s2
\le
\left(
\frac{A_{p,k}-2}{3}+\frac{B_p}{3H}
\right)\binom s2.
\]

Sum over all lines. The unweighted pair sum is `binom(2N,2)`, while the
height-weighted pair sum is exactly `mathcal E(S)`. Insert CMR41. ∎

This is still far above the near-linear syndrome sought by the recursive
repair programme. It does, however, close the absence of any full companion
bound and shows that the mixed-layer carry complexity is at most quadratic
polylogarithmic for each fixed prime base.

The exact finite checks are in
[`scripts/verify_prime_power_companion_global.py`](../scripts/verify_prime_power_companion_global.py).