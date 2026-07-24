# Prime-power displacement signatures and one-channel syndrome

This chapter continues the valuation-completed reciprocal analysis from
[`docs/28-prime-power-completed-reciprocals.md`](28-prime-power-completed-reciprocals.md).
It supplies an exact same-channel displacement filter and the first general
real-triple syndrome bound for a nonlinear full composite channel.

Let \(N=p^k\), and let \(R_{\mathbf c}\) be the completed reciprocal
permutation.  For a nonzero integer \(z\), write \(v_p(z)\) for its
\(p\)-adic valuation.

## 1. Every secant is p-adically diagonal

Take two distinct channel points

\[
P=(x,R_{\mathbf c}(x)),
\qquad
P'=(x',R_{\mathbf c}(x')),
\]

and write their exact lifted displacement as

\[
(a,b)=(x'-x,R_{\mathbf c}(x')-R_{\mathbf c}(x)).
\]

### Theorem CMR6 — PROVED

Every completed-reciprocal secant satisfies

\[
v_p(a)=v_p(b).
\]

Consequently, a displacement vector whose two coordinates have unequal
\(p\)-adic valuation has multiplicity zero inside one channel.  After removing
the common power of \(p\), both coordinates of every primitive secant
direction are units modulo \(p\).

### Proof

Let \(r=v_p(x)\) and \(s=v_p(x')\), with the convention that the origin has
valuation \(k\).

If \(r\ne s\), then

\[
v_p(x'-x)=\min(r,s).
\]

The channel preserves valuation pointwise, so the two row values have
valuations \(r,s\), and their difference has the same valuation
\(\min(r,s)\).

Now suppose \(r=s<k\).  Write

\[
x=p^r u,
\qquad x'=p^r v,
\]

with \(u,v\) units modulo \(p^{k-r}\).  On this stratum,

\[
R_{\mathbf c}(x)=p^r c_r u^{-1},
\qquad
R_{\mathbf c}(x')=p^r c_r v^{-1}
\pmod {p^k}.
\]

Therefore

\[
R_{\mathbf c}(x')-R_{\mathbf c}(x)
\equiv
-p^r c_r\frac{v-u}{uv}
\pmod {p^k}.
\]

The factors \(c_r,u,v\) are units, so the modular row difference and the
column difference \(p^r(v-u)\) have the same valuation below \(k\).  Their
standard lifted differences are nonzero integers of absolute value below
\(p^k\), so adding a multiple of \(p^k\) cannot change that valuation. ∎

This closes an exact displacement-signature subtask of CM3.  It is not yet a
constant multiplicity bound.

## 2. Exact same-stratum secant product

Suppose the two endpoints in CMR6 have the same valuation \(r\).  Put

\[
t=v_p(a)=v_p(b),
\qquad
\alpha=a/p^t,
\qquad
\beta=b/p^t.
\]

Then \(r\le t<k\), and \(\alpha,\beta\) are units modulo \(p\).

### Theorem CMR7 — PROVED

With \(x=p^r u\) and \(x'=p^r v\), one has the exact reduced secant signature

\[
uv\equiv-c_r\alpha\beta^{-1}
\pmod {p^{k-t}}.
\]

Equivalently, the first endpoint parameter obeys

\[
u\bigl(u+p^{t-r}\alpha\bigr)
\equiv-c_r\alpha\beta^{-1}
\pmod {p^{k-t}}.
\]

For odd \(p\), candidate same-stratum secants with fixed displacement are
therefore controlled by one explicit square-root congruence.  If

\[
D_{r,t}
=
\bigl(p^{t-r}\alpha\bigr)^2
+4c_r\alpha\beta^{-1},
\]

then the number of residue classes for \(u\pmod {p^{k-t}}\) is exactly the
number of square roots of \(D_{r,t}\) modulo \(p^{k-t}\), and is bounded by

\[
2p^{\lfloor(k-t)/2\rfloor}.
\]

### Proof

The reciprocal difference identity on the common stratum is

\[
\frac b{p^r}
\equiv
-c_r\frac{a/p^r}{uv}
\pmod {p^{k-r}}.
\]

Both sides are divisible by \(p^{t-r}\).  Dividing by this power reduces the
modulus to \(p^{k-t}\) and gives

\[
\beta\equiv-c_r\alpha(uv)^{-1}
\pmod {p^{k-t}}.
\]

This is the first displayed congruence.  Since
\(v-u=a/p^r=p^{t-r}\alpha\), substitution gives the quadratic in \(u\).
For odd \(p\), completing the square gives

\[
\bigl(2u+p^{t-r}\alpha\bigr)^2
\equiv D_{r,t}
\pmod {p^{k-t}}.
\]

The square-root count is the one classified in Theorem CMR3. ∎

The missing multiplicity upgrade is now precise: one must control lifts from
these reduced residue classes together with the cross-stratum cases
\(v_p(x)\ne v_p(x')\).

## 3. A general one-channel syndrome bound

Let \(T(R_{\mathbf c})\) denote the number of unordered real collinear triples
inside one completed-reciprocal channel.  Theorem CMR3 gives the coarse line
cap

\[
L_{p,k}=2k+2p^{\lfloor k/2\rfloor}+1.
\]

### Theorem CMR8 — PROVED

For every odd prime power \(N=p^k\),

\[
T(R_{\mathbf c})
\le
\frac{L_{p,k}-2}{3}\binom N2.
\]

In particular,

\[
T(R_{\mathbf c})
=
O\!\left(N^{5/2}+N^2\log N\right).
\]

### Proof

For each real line \(\ell\), let \(s_\ell\) be its channel occupancy.  Every
unordered pair of channel points determines exactly one real line, so

\[
\sum_\ell\binom{s_\ell}{2}=\binom N2.
\]

For every \(3\le s\le L_{p,k}\),

\[
\binom s3
=
\frac{s-2}{3}\binom s2
\le
\frac{L_{p,k}-2}{3}\binom s2.
\]

Summing over the lines proves the claim. ∎

This is far above the desired \(O(N\log^C N)\) endpoint, but it is a rigorous
finite syndrome bound for a nonlinear full channel over every odd prime
power.  The tangent-cell classification and CMR7 identify exactly where a
sharper count must be proved.

## 4. Computational evidence and next target

For the uniform choice \(c_r=1\), exact checks give:

| \(p^k\) | maximum real line | real collinear triples |
|---:|---:|---:|
| 9 | 5 | 10 |
| 27 | 7 | 93 |
| 81 | 9 | 580 |
| 243 | 12 | 3303 |
| 25 | 5 | 30 |
| 125 | 8 | 809 |

These values are finite observations, not asymptotic claims.  They are much
smaller than the worst-case CMR8 bound and suggest the next concrete theorem:
prove a divisor-sensitive count for exact real points inside one
Hensel-tangent cell, rather than counting every modular square root as a real
line point.

The checks are implemented in
[`scripts/verify_prime_power_displacement.py`](../scripts/verify_prime_power_displacement.py).
