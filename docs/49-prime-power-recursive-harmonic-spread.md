# Harmonic direction energy in the recursive prime-power bank

CMR32 reduced the completed-reciprocal syndrome to harmonic direction energy.
The deterministic algebraic channel has separate estimates, while the recursive
CMR27 bank has a provably near-linear polylogarithmic energy marginal.

Let \(N=p^k\) with `p` odd. A recursive permutation is obtained by choosing a
base permutation modulo `p` and then, at every higher quotient level and every
column fibre, choosing an independent uniform permutation of the `p` new row
digits. Define

\[
\mathcal E(f)
=
\sum_{0\le x<x'<N}
\frac{\gcd(|x'-x|,|f(x')-f(x)|)}
{\max(|x'-x|,|f(x')-f(x)|)}.
\]

## 1. Exact pair law for a uniform p-adic isometry

Fix two columns with

\[
x'-x=p^tA,
\qquad p\nmid A,
\qquad M=p^{k-t}.
\]

### Theorem CMR50 — PROVED

Under the uniform recursive measure,

\[
f(x')-f(x)=p^tB,
\]

where the signed integer `B` has distribution

\[
\Pr(B=b)=\frac{M-|b|}{M^2(1-1/p)}
\]

for \(0<|b|<M\) and \(p\nmid b\), and probability zero otherwise.

### Proof

The recursive permutations preserve congruence modulo every power of `p`.
The two columns share exactly their first `t` lower base-`p` digits, so their
row images share exactly `t` lower digits. At the first differing digit, a
uniform fibre permutation sends the two distinct column digits to a uniform
ordered pair of distinct row digits. After the paths separate, all higher row
digits lie in independent uniform fibres.

After deleting the common `t` digits, the ordered row pair is therefore uniform
among all `(u,v)` in `[M]^2` with \(p\nmid(v-u)\). There are
\(M^2(1-1/p)\) such pairs, and exactly \(M-|b|\) have `v-u=b`. ∎

## 2. Expected harmonic energy

For `A` coprime to `p`, put

\[
F(A)=\sum_{d\mid A}\frac{\varphi(d)}d,
\qquad
H_m=1+\frac12+\cdots+\frac1m.
\]

### Theorem CMR51 — PROVED

For the uniform recursive measure,

\[
\mathbb E\mathcal E(f)
\le4NkH_N(1+H_N)=O(N\log^3N).
\]

### Proof

For the fixed pair from CMR50, cancellation of the common power `p^t` gives
harmonic weight

\[
\frac{\gcd(A,|B|)}{\max(A,|B|)}.
\]

Using CMR50, dropping the restriction \(p\nmid b\), and using
\(1/(1-1/p)\le2\), its expectation is at most

\[
\frac4{M^2}
\sum_{b=1}^{M-1}(M-b)
\frac{\gcd(A,b)}{\max(A,b)}.
\]

The identity

\[
\gcd(A,b)=\sum_{d\mid A,\ d\mid b}\varphi(d)
\]

implies

\[
\frac1A\sum_{b\le A}\gcd(A,b)=F(A),
\qquad
\sum_{b\le M}\frac{\gcd(A,b)}b\le H_MF(A).
\]

Hence the expected contribution of this pair is at most

\[
\frac4M(1+H_M)F(A).
\]

For fixed valuation `t`, the difference \(p^tA\) occurs for
\(p^t(M-A)\) unordered pairs. Therefore that valuation contributes at most

\[
4N(1+H_M)\frac1{M^2}
\sum_{A<M}(M-A)F(A).
\]

Finally,

\[
\sum_{A<M}F(A)
=
\sum_{d<M}\frac{\varphi(d)}d
\left\lfloor\frac{M-1}d\right\rfloor
\le MH_M.
\]

Each valuation contributes at most \(4N(1+H_N)H_N\); summing the `k`
valuations proves the theorem. ∎

## 3. The no-three terminal base costs only a constant factor

Use the CMR35 terminal family as the base distribution and retain uniform fibre
permutations at every higher level.

### Theorem CMR52 — PROVED

For one layer of the recursive bank with the CMR35 base distribution,

\[
\mathbb E\mathcal E(f)
\le24NkH_N(1+H_N)=O(N\log^3N).
\]

Consequently a deterministic recursive-bank state exists with harmonic energy
at most this bound, and the same assertion holds for each layer of the
saturated two-layer bank.

### Proof

For a pair with positive `p`-adic valuation, the first differing row digit is
chosen in a higher uniform fibre, so CMR50 is unchanged. For valuation zero,
CMR36 bounds any prescribed ordered pair of distinct base rows by
\(1/h^2=4/(p-1)^2\), while the uniform base probability is
\(1/(p(p-1))\). The likelihood ratio is at most

\[
\frac{4p}{p-1}\le6.
\]

All higher digits have the same conditional law. Multiplying CMR51 by six and
averaging proves the claim. ∎

The repeated top-digit vectors from CMR14 therefore do not force large
harmonic energy in the recursive bank. This does not itself prove a no-three
state, because the deterministic line cap CMR31 is not preserved by arbitrary
fibre permutations. The remaining decoder must combine this dispersion with
the first-separation identity CMR28.

The checker is
[`scripts/verify_prime_power_recursive_harmonic.py`](../scripts/verify_prime_power_recursive_harmonic.py).
