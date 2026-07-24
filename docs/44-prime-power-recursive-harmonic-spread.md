# Harmonic direction energy in the recursive prime-power bank

CMR32 reduced the completed-reciprocal syndrome to harmonic direction energy.
The deterministic algebraic channel still requires a separate estimate, but
the recursive CMR27 bank itself has a provably near-linear polylogarithmic
energy marginal.

Let

\[
N=p^k
\]

with `p` odd. A recursive permutation is obtained by choosing a base
permutation modulo `p` and then, at every higher quotient level and every
column fibre, choosing an independent uniform permutation of the `p` new row
digits.

For a permutation `f`, define

\[
\mathcal E(f)
=
\sum_{0\le x<x'<N}
\frac{\gcd(|x'-x|,|f(x')-f(x)|)}
{\max(|x'-x|,|f(x')-f(x)|)}.
\]

This is the same harmonic direction energy as CMR32.

## 1. Exact pair law for a uniform p-adic isometry

First take the base permutation uniformly from all of `S_p`.

Fix two columns with

\[
x'-x=p^tA,
\qquad
p\nmid A,
\qquad
M=p^{k-t}.
\]

### Theorem CMR38 — PROVED

Under the uniform recursive measure,

\[
f(x')-f(x)=p^tB,
\]

where the signed integer `B` has distribution

\[
\Pr(B=b)
=
\frac{M-|b|}{M^2(1-1/p)}
\]

for

\[
0<|b|<M,
\qquad
p\nmid b,
\]

and probability zero otherwise.

### Proof

The recursive permutations preserve congruence modulo every power of `p`.
The two columns share exactly their first `t` lower base-`p` digits. Their row
images therefore share exactly `t` lower digits as well.

At the first differing digit, a uniform fibre permutation sends the two
distinct column digits to a uniform ordered pair of distinct row digits. Once
the paths separate, all higher row digits lie in independent uniform fibres.
Consequently, after deleting the common `t` lower digits, the ordered row pair
is uniform among all ordered pairs `(u,v)` in `[M]^2` with

\[
p\nmid(v-u).
\]

There are `M^2(1-1/p)` such pairs. For one fixed signed difference `b`, exactly
`M-|b|` ordered pairs satisfy `v-u=b`. ∎

## 2. Expected harmonic energy

For an integer `A` coprime to `p`, put

\[
F(A)=\sum_{d\mid A}\frac{\varphi(d)}d.
\]

Let

\[
H_m=1+\frac12+\cdots+\frac1m.
\]

### Theorem CMR39 — PROVED

For the uniform recursive measure,

\[
\mathbb E\mathcal E(f)
\le
4NkH_N(1+H_N).
\]

In particular,

\[
\mathbb E\mathcal E(f)=O(N\log^3N).
\]

### Proof

For the fixed column pair from CMR38, cancellation of the common power `p^t`
gives the reciprocal primitive height

\[
\frac{\gcd(A,|B|)}{\max(A,|B|)}.
\]

Using CMR38, dropping the restriction `p` not dividing `b`, and using
`1/(1-1/p)<=2`, its expectation is at most

\[
\frac4{M^2}
\sum_{b=1}^{M-1}
(M-b)
\frac{\gcd(A,b)}{\max(A,b)}.
\]

Split at `b=A`. The standard identity

\[
\gcd(A,b)=\sum_{d\mid A,\ d\mid b}\varphi(d)
\]

gives

\[
\frac1A\sum_{b\le A}\gcd(A,b)=F(A)
\]

and

\[
\sum_{b\le M}\frac{\gcd(A,b)}b
\le H_MF(A).
\]

Therefore the expected contribution of this pair is at most

\[
\frac4M(1+H_M)F(A).
\]

For one fixed valuation `t`, the positive column differences are
`p^t A`, with `1<=A<M` and `p` not dividing `A`; each occurs for

\[
N-p^tA=p^t(M-A)
\]

unordered column pairs. Hence the expected energy from this valuation is at
most

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

Thus each valuation contributes at most

\[
4N(1+H_M)H_M
\le
4N(1+H_N)H_N.
\]

Summing over the `k` possible valuations proves the theorem. ∎

## 3. The no-three terminal base costs only a constant factor

Now use the CMR35 terminal family as the base distribution and retain uniform
fibre permutations at every higher level.

### Theorem CMR40 — PROVED

For one layer of the recursive bank with the CMR35 base distribution,

\[
\mathbb E\mathcal E(f)
\le
24NkH_N(1+H_N)
=
O(N\log^3N).
\]

Consequently there exists a deterministic state in the recursive bank with
harmonic energy at most the displayed bound. The same assertion holds for
each layer of the two-layer saturated bank.

### Proof

For a pair of columns with positive `p`-adic valuation, the first differing row
digit is chosen in a higher uniform fibre, so the exact CMR38 pair law is
unchanged.

For valuation zero, CMR36 says that any prescribed ordered pair of distinct
base rows has probability at most

\[
1/h^2=4/(p-1)^2.
\]

Under the uniform base permutation its probability is

\[
1/(p(p-1)).
\]

The likelihood ratio is therefore at most

\[
\frac{4p}{p-1}\le6.
\]

All higher digits have the same conditional uniform law. Thus every pair-image
probability under the terminal distribution is at most six times its CMR38
value. Multiplying the CMR39 bound by six proves the result. The deterministic
existence statement follows by averaging. ∎

## 4. Significance and remaining gap

The repeated top-digit vectors from CMR14 do not force large harmonic energy
once the full recursive bank is used. A low-energy saturated state exists with
an explicit no-three terminal base.

This does not yet prove that the state itself is no-three: the algebraic
height-sensitive line cap CMR31 belongs to the original completed reciprocal
channel and is not automatically preserved by arbitrary fibre permutations.
The next decoder theorem must combine CMR40 with the first-separation carry
identity CMR28, rather than applying CMR32 directly after randomization.

The checker is
[`scripts/verify_prime_power_recursive_harmonic.py`](../scripts/verify_prime_power_recursive_harmonic.py).
