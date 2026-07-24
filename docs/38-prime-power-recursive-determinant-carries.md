# Recursive determinant carries for prime-power lifts

CMR25–CMR27 give a recursive state space. This chapter gives the matching
recursive collinearity signature.

Let

\[
N=p^k,
\qquad a=p^{k-1},
\]

and write three standard grid points uniquely as

\[
P_i=(x_i,y_i)
=(\bar x_i+a\xi_i,\bar y_i+a\eta_i),
\]

where

\[
0\le \bar x_i,\bar y_i<a,
\qquad
0\le \xi_i,\eta_i<p.
\]

Put

\[
D_0
=
\Delta((\bar x_i,\bar y_i)_{i=1}^3),
\]

\[
D_1
=
(\xi_2-\xi_1)(\eta_3-\eta_1)
-(\xi_3-\xi_1)(\eta_2-\eta_1),
\]

and define the mixed digit term

\[
\begin{aligned}
M={}&
(\xi_2-\xi_1)(\bar y_3-\bar y_1)
+(\bar x_2-\bar x_1)(\eta_3-\eta_1)\\
&-(\xi_3-\xi_1)(\bar y_2-\bar y_1)
-(\bar x_3-\bar x_1)(\eta_2-\eta_1).
\end{aligned}
\]

## 1. Exact determinant recurrence

### Theorem CMR28 — PROVED

The exact integer determinant satisfies

\[
\Delta(P_1,P_2,P_3)
=
D_0+aM+a^2D_1.
\]

If the lifted points are real collinear, then

\[
D_0\equiv0\pmod a.
\]

Writing

\[
q=D_0/a,
\]

the real-collinearity condition is exactly

\[
q+M+aD_1=0.
\]

### Proof

Expand each coordinate difference into its lower part plus `a` times its top
digit. The degree-zero terms give `D_0`, the terms with one top digit give
`aM`, and the terms with two top digits give `a^2D_1`.

If the full determinant is zero, its reduction modulo `a` is `D_0`, proving
the divisibility. Division by `a` gives the final identity. ∎

The integer `q` is the **quotient determinant carry**. It records exactly why
a projected modular triple need not be a real triple.

## 2. First-separation signatures

### Corollary CMR29 — PROVED

Every real triple in a recursively lifted state has, at each quotient level,
a signature

\[
(q,M,D_1)
\]

satisfying

\[
q+M+aD_1=0.
\]

If the three projected points are real collinear, then `q=0`; otherwise the
nonzero carry `q` is cancelled by the mixed and top-digit terms. Repeating the
decomposition on the projected coordinates produces a finite sequence of
such signatures down to modulus `p`.

At the first level where the projected determinant is nonzero, the triple is
therefore certified by an explicit nonzero quotient carry rather than merely
by modular incidence.

### Proof

Apply CMR28 at the current exponent and then recursively to the projected
points. The process terminates because the exponent decreases by one at every
step. ∎

## 3. Coarse ranges

The components have explicit deterministic ranges:

\[
|D_1|\le2(p-1)^2,
\]

\[
|M|\le4(p-1)(a-1),
\]

and

\[
|q|<2a.
\]

The last inequality follows from
\(|D_0|<2a^2\). These bounds are coarse, but they show that each quotient level
has only `O(p^2a)` possible mixed-carry values and `O(p^2)` top-digit areas.
Sharper counts can exploit the permutation-block constraints.

## 4. Decoder endpoint

The recursive bank and the recursive determinant now match exactly. A
multiscale certificate potential may charge every real triple at its first
nonzero quotient carry and weight it by the cylinder probability of the digit
assignments that satisfy

\[
q+M+aD_1=0.
\]

The missing theorem is a concentration bound for these first-separation
signatures under the recursive CMR27 measure. Unlike a flat first moment, this
potential separates terminal internal triples, quotient-real triples, and
modular false positives.

The identity is checked in
[`scripts/verify_prime_power_recursive_determinant.py`](../scripts/verify_prime_power_recursive_determinant.py).
