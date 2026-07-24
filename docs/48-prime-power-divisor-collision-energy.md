# Divisor-collision reduction for deterministic harmonic energy

CMR32 reduces the deterministic completed-reciprocal syndrome to harmonic
direction energy. This chapter converts that energy into one exact family of
integer divisibility counts.

Let

\[
N=p^k
\]

with `p` odd, and let `f=R_c` be a completed-reciprocal permutation. For a
positive column difference `a`, write

\[
a=p^tA,
\qquad
p\nmid A.
\]

For every `0<=x<N-a`, CMR6 gives

\[
f(x+a)-f(x)=p^t b_x
\]

with `b_x` a nonzero integer not divisible by `p`. Put

\[
B_x=|b_x|.
\]

For a divisor `d` of `A`, define the **divisor-collision count**

\[
C(a,d)
=
\#\{0\le x<N-a:d\mid B_x\}.
\]

## 1. Exact energy reduction

### Theorem CMR45 — PROVED

The harmonic direction energy satisfies

\[
\mathcal E(f)
\le
\sum_{a=1}^{N-1}
\frac1A
\sum_{d\mid A}
\varphi(d)C(a,d),
\]

where `A=a/p^v_p(a)`.

### Proof

For the pair of graph points at columns `x` and `x+a`, cancellation of the
common power `p^t` shows that its primitive direction height is

\[
\frac{\max(A,B_x)}{\gcd(A,B_x)}.
\]

Its harmonic weight is therefore

\[
\frac{\gcd(A,B_x)}{\max(A,B_x)}
\le
\frac{\gcd(A,B_x)}A.
\]

Use the divisor identity

\[
\gcd(A,B_x)
=
\sum_{d\mid A,\ d\mid B_x}\varphi(d)
\]

and sum first over `x` and then over `a`. ∎

## 2. A quantified endpoint

### Theorem CMR46 — PROVED UNDER HYPOTHESES

Suppose that for some `K>=1`, every positive column difference `a` and every
divisor `d` of its reduced part `A` satisfy

\[
C(a,d)
\le
K\frac Nd.
\]

Then

\[
\mathcal E(f)
\le
KNkH_N^2
=
O(KN\log^3N).
\]

Consequently CMR32 gives

\[
T(f)
=
O\left(N^2\log N+K N^{3/2}\log^3N\right).
\]

### Proof

Insert the assumed collision bound into CMR45:

\[
\mathcal E(f)
\le
KN
\sum_{a=1}^{N-1}
\frac1A
\sum_{d\mid A}\frac{\varphi(d)}d.
\]

Group `a=p^tA` by `0<=t<k`. For one fixed `t`, put
`X=N/p^t`. Dropping the restriction that `A` is not divisible by `p`,

\[
\begin{aligned}
\sum_{A<X}
\frac1A
\sum_{d\mid A}\frac{\varphi(d)}d
&=
\sum_{d<X}
\frac{\varphi(d)}{d^2}
H_{\lfloor(X-1)/d\rfloor}\\
&\le
H_X\sum_{d<X}\frac1d
\le H_N^2.
\end{aligned}
\]

There are `k` valuation levels. This proves the energy bound, and CMR32 gives
the triple bound. ∎

## 3. Exact finite data

For the uniform parameters `c_r=1`, exhaustive checks give the following
smallest valid constants

\[
K_N
=
\max_{a,d\mid A}
\frac{dC(a,d)}N.
\]

| `N` | `K_N` | harmonic energy | CMR45 divisor bound |
|---:|---:|---:|---:|
| 9 | 1.111 | 21.086 | 27.293 |
| 25 | 2.200 | 97.081 | 144.302 |
| 27 | 1.704 | 114.162 | 172.982 |
| 49 | 1.959 | 237.357 | 405.147 |
| 81 | 1.975 | 567.143 | 978.665 |
| 121 | 2.198 | 746.717 | 1430.140 |
| 125 | 3.904 | 949.950 | 1682.855 |
| 243 | 4.099 | 2383.090 | 4689.184 |

These are observations, not an asymptotic theorem. They suggest that a
polylogarithmic divisor-collision constant may be plausible even though the
raw displacement multiplicity is linear by CMR14.

The deterministic harmonic bottleneck is now the explicit statement

> prove `K_N=O(log^C N)` for a suitable completed-reciprocal parameter family,
> or prove the weighted CMR45 sum directly without a uniform maximum bound.

The checker is
[`scripts/verify_prime_power_divisor_collisions.py`](../scripts/verify_prime_power_divisor_collisions.py).
