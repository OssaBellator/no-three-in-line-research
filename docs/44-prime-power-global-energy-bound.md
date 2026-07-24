# A global harmonic-energy bound from direction splitting

CMR31 gives a line cap that improves as the primitive direction height grows.
A low-/high-height decomposition converts that local estimate into a rigorous
global bound.

Let `N=p^k` with `p` odd, let `R_c` be a completed-reciprocal channel, and put

\[
\mathcal E(R_c)=\sum_{\{P,Q\}}\frac1{H(P,Q)}.
\]

## 1. Pair count in one primitive direction

Fix one unoriented primitive direction of height `H`. Its parallel real lines
partition the `N` channel points. If their occupancies are `s_i`, CMR31 gives

\[
s_i\le L_H:=2k+2+\frac{2\sqrt N}{H}.
\]

Therefore

\[
\sum_i\binom{s_i}{2}
\le
\frac{L_H-1}{2}\sum_i s_i
=
\frac{N(L_H-1)}2.
\]

There are at most `4H` unoriented primitive directions of exact height `H`.

## 2. Global energy theorem

### Theorem CMR38 — PROVED

For every integer `1<=K<N`,

\[
\mathcal E(R_c)
\le
2N(2k+1)K
+4N\sqrt N\sum_{H=1}^K\frac1H
+\frac1K\binom N2.
\]

Choosing `K=floor(sqrt(N))` yields

\[
\mathcal E(R_c)=O(N^{3/2}\log N).
\]

### Proof

At exact height `H<=K`, the preceding direction count and pair bound give
weighted energy at most

\[
4H\cdot\frac{N(L_H-1)}{2H}
=
2N\left(2k+1+\frac{2\sqrt N}{H}\right).
\]

Sum over `H<=K`. Every remaining pair has height greater than `K` and hence
weight at most `1/K`. Taking `K=floor(sqrt(N))` and using `k=O(log N)` proves
the asymptotic estimate. ∎

## 3. Improved one-channel syndrome

### Corollary CMR39 — PROVED

The one-channel real triple count satisfies

\[
T(R_c)=O(N^2\log N).
\]

More explicitly, CMR32 and CMR38 give

\[
\begin{aligned}
T(R_c)
\le{}&\frac{2k}{3}\binom N2\\
&+\frac{2\sqrt N}{3}
\left(
2N(2k+1)K
+4N\sqrt N\sum_{H=1}^K\frac1H
+\frac1K\binom N2
\right).
\end{aligned}
\]

### Proof

Substitute CMR38 into CMR32 and take `K=floor(sqrt(N))`. ∎

Later divisor-collision work sharpens the energy estimate, but this chapter is
the first unconditional quadratic-order syndrome reduction.
