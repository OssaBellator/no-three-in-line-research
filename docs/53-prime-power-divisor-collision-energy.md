# Divisor-collision reduction for deterministic harmonic energy

CMR32 reduces the deterministic completed-reciprocal syndrome to harmonic
direction energy. This chapter converts that energy into explicit integer
divisibility counts.

Let \(N=p^k\) with `p` odd, and let \(f=R_{\mathbf c}\). For a positive column
difference `a`, write

\[
a=p^tA,
\qquad p\nmid A.
\]

For every \(0\le x<N-a\), CMR6 gives

\[
f(x+a)-f(x)=p^tb_x
\]

with nonzero \(p\nmid b_x\). Put \(B_x=|b_x|\). For a divisor `d` of `A`,
define

\[
C(a,d)=\#\{0\le x<N-a:d\mid B_x\}.
\]

## Exact energy reduction

### Theorem CMR56 — PROVED

The harmonic direction energy satisfies

\[
\mathcal E(f)
\le
\sum_{a=1}^{N-1}
\frac1A
\sum_{d\mid A}\varphi(d)C(a,d),
\]

where \(A=a/p^{v_p(a)}\).

### Proof

For the pair at columns `x,x+a`, cancel the common power \(p^t\). Its harmonic
weight is

\[
\frac{\gcd(A,B_x)}{\max(A,B_x)}
\le
\frac{\gcd(A,B_x)}A.
\]

Use

\[
\gcd(A,B_x)=\sum_{d\mid A,\ d\mid B_x}\varphi(d)
\]

and sum over `x` and then `a`. ∎

## Quantified endpoint

### Theorem CMR57 — PROVED UNDER HYPOTHESES

Suppose that for some \(K\ge1\), every positive difference `a` and every divisor
`d` of its reduced part `A` satisfy

\[
C(a,d)\le K\frac Nd.
\]

Then

\[
\mathcal E(f)\le KNkH_N^2=O(KN\log^3N),
\]

and CMR32 gives

\[
T(f)=O\left(N^2\log N+KN^{3/2}\log^3N\right).
\]

### Proof

Insert the collision bound into CMR56. Group \(a=p^tA\). For fixed `t`,
put \(X=N/p^t\). Then

\[
\begin{aligned}
\sum_{A<X}\frac1A
\sum_{d\mid A}\frac{\varphi(d)}d
&=
\sum_{d<X}\frac{\varphi(d)}{d^2}
H_{\lfloor(X-1)/d\rfloor}\\
&\le H_N^2.
\end{aligned}
\]

There are `k` valuation levels. Apply CMR32 for the triple bound. ∎

The remaining chapters prove unconditional collision estimates by splitting
same-stratum, singular, and cross-stratum cells.

The checker is
[`scripts/verify_prime_power_divisor_collisions.py`](../scripts/verify_prime_power_divisor_collisions.py).
