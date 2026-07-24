# A global harmonic-energy bound from direction splitting

CMR31 gives a line cap that improves as the primitive direction height grows.
A low-/high-height decomposition converts that local estimate into a rigorous
global bound, without yet proving the conjectured near-linear energy.

Let `N=p^k` with `p` odd, and let `R_c` be a completed-reciprocal channel. For
a pair of channel points `P,Q`, write `H(P,Q)` for the height of their
unoriented primitive integer direction and

\[
\mathcal E=\sum_{\{P,Q\}}\frac1{H(P,Q)}.
\]

## 1. Pair count in one primitive direction

Fix one unoriented primitive direction of height `H`. The real lines parallel
to that direction partition the `N` channel points. If their occupancies are
`s_1,s_2,...`, then CMR31 gives

\[
s_i\le L_H:=2k+2+\frac{2\sqrt N}{H}.
\]

Consequently

\[
\sum_i\binom{s_i}{2}
\le
\frac{L_H-1}{2}\sum_i s_i
=
\frac{N(L_H-1)}2.
\]

There are at most `4H` unoriented primitive directions of exact height `H`.
This coarse count includes both signs of the slope and is sufficient below.

## 2. Global energy theorem

### Theorem CMR38 — PROVED

For every integer `1<=K<N`,

\[
\mathcal E
\le
2N(2k+1)K
+4N\sqrt N\sum_{H=1}^K\frac1H
+\frac1K\binom N2.
\]

In particular, choosing `K=floor(sqrt(N))` gives

\[
\mathcal E(R_c)=O(N^{3/2}\log N).
\]

### Proof

For directions of height at most `K`, the preceding one-direction estimate and
the `4H` direction count give, at exact height `H`,

\[
\sum_{\substack{\{P,Q\}:\\H(P,Q)=H}}
\frac1H
\le
4H\cdot\frac{N(L_H-1)}{2H}
=
2N\left(2k+1+\frac{2\sqrt N}{H}\right).
\]

Summing from `1` to `K` gives the first two terms.

Every remaining pair has height greater than `K`, hence contributes at most
`1/K`. There are at most `binom(N,2)` such pairs, giving the last term.

For `K=floor(sqrt(N))`, the harmonic sum is `O(log N)`, the first and last
terms are `O(N^(3/2) k)` and `O(N^(3/2))`, and `k<=log_3 N`. ∎

The theorem is intentionally robust: it uses only the direction-sensitive line
cap, not the detailed reciprocal displacement equation. A near-linear energy
theorem must exploit more arithmetic than this counting argument.

## 3. Improved one-channel syndrome

### Corollary CMR39 — PROVED

The number `T(R_c)` of unordered real collinear triples in one odd-prime
completed-reciprocal channel satisfies

\[
T(R_c)=O(N^2\log N).
\]

More explicitly, for every `K`, CMR32 and CMR38 give

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

Substitute the CMR38 energy estimate into the exact reduction of CMR32 and take
`K=floor(sqrt(N))`. ∎

This improves the earlier unconditional `O(N^(5/2)+N^2 log N)` estimate to a
quadratic polylogarithmic bound. It does not reach the near-linear syndrome
needed for a direct first-moment completion, but it removes a full factor of
`sqrt(N)` from the worst term.

The finite checker is
[`scripts/verify_prime_power_global_energy.py`](../scripts/verify_prime_power_global_energy.py).