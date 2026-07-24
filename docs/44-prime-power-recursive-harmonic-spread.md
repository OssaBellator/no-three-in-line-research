# Harmonic direction energy in the recursive prime-power bank

CMR32 reduced the completed-reciprocal syndrome to harmonic direction energy.
The recursive CMR27 bank has a provably near-linear polylogarithmic energy
marginal.

Let \(N=p^k\) with `p` odd. A recursive permutation chooses a base permutation
modulo `p` and then an independent uniform permutation of each new row-digit
fibre. Define

\[
\mathcal E(f)=
\sum_{0\le x<x'<N}
\frac{\gcd(|x'-x|,|f(x')-f(x)|)}
{\max(|x'-x|,|f(x')-f(x)|)}.
\]

## Exact pair law

Fix

\[
x'-x=p^tA,
\qquad p\nmid A,
\qquad M=p^{k-t}.
\]

### Theorem CMR38 — PROVED

Under the uniform recursive measure,

\[
f(x')-f(x)=p^tB,
\]

where

\[
\Pr(B=b)=\frac{M-|b|}{M^2(1-1/p)}
\]

for \(0<|b|<M\) and \(p\nmid b\), and is zero otherwise.

### Proof

The two columns share exactly their first `t` lower digits, and the recursive
permutation preserves that common prefix. At the first differing digit, a
uniform fibre permutation gives a uniform ordered pair of distinct row digits;
after separation, higher digits are independent. Deleting the common prefix
therefore gives a uniform ordered pair `(u,v)` in `[M]^2` with
\(p\nmid(v-u)\). There are \(M^2(1-1/p)\) such pairs and \(M-|b|\) with
`v-u=b`. ∎

## Expected harmonic energy

Put

\[
F(A)=\sum_{d\mid A}\frac{\varphi(d)}d,
\qquad
H_m=1+\frac12+\cdots+\frac1m.
\]

### Theorem CMR39 — PROVED

For the uniform recursive measure,

\[
\mathbb E\mathcal E(f)
\le4NkH_N(1+H_N)=O(N\log^3N).
\]

### Proof

CMR38 bounds the expected contribution of the fixed pair by

\[
\frac4{M^2}
\sum_{b=1}^{M-1}(M-b)
\frac{\gcd(A,b)}{\max(A,b)}.
\]

Using

\[
\gcd(A,b)=\sum_{d\mid A,\ d\mid b}\varphi(d)
\]

gives an upper bound

\[
\frac4M(1+H_M)F(A).
\]

At valuation `t`, the difference \(p^tA\) occurs for \(p^t(M-A)\) pairs, so
the total is at most

\[
4N(1+H_M)M^{-2}\sum_{A<M}(M-A)F(A).
\]

Finally,

\[
\sum_{A<M}F(A)
=
\sum_{d<M}\frac{\varphi(d)}d
\left\lfloor\frac{M-1}d\right\rfloor
\le MH_M.
\]

Sum the resulting \(4N(1+H_N)H_N\) over the `k` valuations. ∎

## No-three terminal base

Use the CMR35 terminal family at the base and uniform fibres above it.

### Theorem CMR40 — PROVED

For one recursive layer with the CMR35 base distribution,

\[
\mathbb E\mathcal E(f)
\le24NkH_N(1+H_N)=O(N\log^3N).
\]

Hence a deterministic recursive-bank state with this energy exists in each
layer of the saturated bank.

### Proof

Pairs with positive `p`-adic valuation use a higher uniform first-separating
fibre, so CMR38 is unchanged. At valuation zero, CMR36 bounds a prescribed
ordered base-row pair by \(4/(p-1)^2\), versus \(1/(p(p-1))\) under the
uniform base. The likelihood ratio is at most \(4p/(p-1)\le6\). Multiply
CMR39 by six and average. ∎

The checker is
[`scripts/verify_prime_power_recursive_harmonic.py`](../scripts/verify_prime_power_recursive_harmonic.py).
