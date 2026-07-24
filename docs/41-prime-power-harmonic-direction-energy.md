# Harmonic direction energy and the prime-power syndrome

CMR30 turns the worst tangent multiplicity into a direction-height-sensitive
line cap. Summing that cap against pair counts yields a sharper structural
endpoint for the one-channel syndrome.

Let \(N=p^k\) with `p` odd, and let \(R_{\mathbf c}\) be a completed reciprocal
channel. For two distinct channel points `P,Q`, let

\[
\operatorname{prim}(Q-P)=(r,s)
\]

be the unoriented primitive integer direction, and put

\[
H(P,Q)=\max(|r|,|s|).
\]

Define the **harmonic direction energy**

\[
\mathcal E(R_{\mathbf c})
=
\sum_{\{P,Q\}}
\frac1{H(P,Q)}.
\]

## 1. Direction-sensitive line cap

### Lemma CMR31 — PROVED

Every real line `L` of primitive direction height `H` satisfies

\[
|L\cap R_{\mathbf c}|
\le
2k+2+rac{2\sqrt N}{H}.
\]

### Proof

The lower valuation strata contribute at most `2h≤2k`. In a two-branch top
cell, CMR30 gives at most

\[
2\left(1+\frac{p^t}{H}\right)
\]

points, with \(t\le m/2\), so \(p^t\le\sqrt{p^m}\le\sqrt N\). The
zero-discriminant case is smaller, and nonsingular cases have at most two top
points. ∎

## 2. Exact energy reduction

Let \(T(R_{\mathbf c})\) be the number of unordered real collinear triples in
the channel.

### Theorem CMR32 — PROVED

One has

\[
T(R_{\mathbf c})
\le
\frac{2k}{3}\binom N2
+
\frac{2\sqrt N}{3}\mathcal E(R_{\mathbf c}).
\]

Consequently, the harmonic-energy hypothesis

\[
\mathcal E(R_{\mathbf c})
=O(N\log^C N)
\]

would imply

\[
T(R_{\mathbf c})
=O(N^2\log N+N^{3/2}\log^C N)
=O(N^2\log^{\max(1,C)}N).
\]

### Proof

For a real line `L`, write \(s_L=|L\cap R_{\mathbf c}|\) and let `H_L` be its
primitive direction height. By CMR31,

\[
s_L-2
\le
2k+rac{2\sqrt N}{H_L}.
\]

Therefore

\[
\binom{s_L}{3}
=
\frac{s_L-2}{3}\binom{s_L}{2}
\le
\left(
\frac{2k}{3}+rac{2\sqrt N}{3H_L}
\right)
\binom{s_L}{2}.
\]

Sum over all real lines. Every unordered channel pair lies on exactly one
line, giving

\[
\sum_L\binom{s_L}{2}=\binom N2.
\]

The height-weighted pair sum is exactly

\[
\sum_L\frac1{H_L}\binom{s_L}{2}
=
\mathcal E(R_{\mathbf c}).
\]

Substitution proves the theorem. ∎

This improves the previous endpoint conceptually: the square-root line cap is
paid only on low-height pairs, rather than on all \(\binom N2\) pairs.

## 3. Finite data

For the uniform parameters \(c_r=1\), exact computations give:

| \(N\) | \(\mathcal E\) | \(\mathcal E/N\) | \(\mathcal E/(N\log N)\) |
|---:|---:|---:|---:|
| 9 | 21.086 | 2.343 | 1.066 |
| 25 | 97.081 | 3.883 | 1.206 |
| 27 | 114.162 | 4.228 | 1.283 |
| 81 | 567.143 | 7.002 | 1.593 |
| 125 | 949.950 | 7.600 | 1.574 |
| 243 | 2383.090 | 9.807 | 1.785 |

These values are observations, not an asymptotic theorem. They suggest

\[
\mathcal E(R_{\mathbf 1})=O(N\log^C N)
\]

with small `C`, despite the linear repeated displacements from CMR14.

## 4. Revised analytic bottleneck

The one-channel syndrome problem is now reduced to:

> prove a near-linear harmonic direction-energy bound for completed
> reciprocals, preferably after contracting the CMR19 top-digit blocks.

The repeated top-digit vectors contribute only `O_p(N)` to this energy because
they lie inside `N/p` blocks of bounded size for fixed `p`. The unresolved
mass comes from cross-block directions.

The exact computations and the CMR32 inequality are checked in
[`scripts/verify_prime_power_harmonic_energy.py`](../scripts/verify_prime_power_harmonic_energy.py).
