# Cross-stratum collision sums and a quadratic-order syndrome bound

CMR49 confines every cross-stratum divisor collision to one carry residue
class modulo `p`. In fact the carry is fixed modulo the full valuation gap, and
the remaining quadratic discriminant has a uniform two-root form.

Retain

\[
N=p^k,
\qquad
a=p^tA,
\qquad d\mid A,
\qquad M=p^{k-t}.
\]

First suppose the two endpoints are nonzero and their valuations are `t` and

\[
r=t+h>t.
\]

Put

\[
L=p^{k-r}=M/p^h.
\]

The possible pair containing the origin is treated separately below.

## 1. Full carry congruence

### Theorem CMR52 — PROVED

Every nonzero cross-stratum divisor collision satisfies

\[
dmA\equiv c_t\pmod {p^h}.
\]

Write

\[
z=\frac{dmA-c_t}{p^h}.
\]

For either orientation of the two endpoint valuations, the higher-valuation
unit parameter `u` satisfies a quadratic congruence modulo `L` whose
discriminant is

\[
\Delta_z
=
(z-p^hc_r)^2-4c_rc_t.
\]

A pair containing the origin satisfies the stronger congruence

\[
dmA\equiv c_t\pmod M
\]

directly and contributes at most one collision for fixed `a,d`.

### Proof

First take

\[
x=p^ru,
\qquad
x+a=p^tv,
\qquad
v=A+p^hu.
\]

The reduced row-difference equation is

\[
c_tv^{-1}-p^hc_ru^{-1}\equiv dm\pmod M.
\]

After multiplication by `uv` and expansion of `v`, this becomes

\[
dmp^hu^2
+(dmA-c_t+p^{2h}c_r)u
+p^hc_rA
\equiv0\pmod M.
\]

Reduction modulo `p^h` gives

\[
(dmA-c_t)u\equiv0\pmod {p^h}.
\]

Since `u` is a unit, the full carry congruence follows. Divide the quadratic by
`p^h`; modulo `L` it is

\[
dm u^2+(z+p^hc_r)u+c_rA\equiv0.
\]

Its discriminant is

\[
(z+p^hc_r)^2-4dm c_rA.
\]

Using `dmA=c_t+p^hz` simplifies this to the displayed `Delta_z`.

In the reverse orientation the middle coefficient changes sign before
squaring, and the same discriminant results.

For the origin pair, `x=0` and `x+a=p^tA`. The exact reduced row difference is
congruent to `c_t A^{-1}` modulo `M`. Since it equals `dm`, multiplication by
`A` gives the stated congruence. There is only one origin pair for a fixed
positive difference `a`. ∎

## 2. Summing one nonzero cross stratum

### Theorem CMR53 — PROVED

For a fixed nonzero higher valuation `r=t+h<k`, the total number of
cross-stratum divisor collisions, counting both endpoint orientations, is less
than

\[
8+
\frac{16L}d
+
8\sqrt L.
\]

### Proof

The signed carry range is

\[
0<|m|<M/d.
\]

CMR52 restricts `m` to one residue class modulo `p^h`. Hence the number `J` of
possible carries is at most

\[
J\le1+rac{2M}{dp^h}
=1+rac{2L}d.
\]

As these carries run through their arithmetic progression, the corresponding
values `z` form an arithmetic progression of length `J` and unit step modulo
`p`.

For a fixed `z`, the number of possible `u` values is the square-root count of
`Delta_z` modulo `L`. Put

\[
E=\lfloor\log_p(L)/2\rfloor.
\]

The right side `4c_rc_t` is a unit. Therefore the congruence

\[
(z-p^hc_r)^2\equiv4c_rc_t\pmod {p^{2s}}
\]

has either zero or two residue classes modulo `p^(2s)`. Each class meets the
`z` progression in at most

\[
1+J/p^{2s}
\]

places.

Applying the same valuation layer decomposition as in CMR50 gives a total root
count in one orientation of less than

\[
4J+4\sqrt L
\le
4+
\frac{8L}d
+
4\sqrt L.
\]

There are two endpoint orientations. ∎

## 3. Total cross-stratum and divisor-collision bounds

### Corollary CMR54 — PROVED

Summing all nonzero higher valuations `t<r<k` and the possible origin pair, the
cross-stratum divisor-collision count is less than

\[
\frac{8M}d+11\sqrt M+8k.
\]

Consequently the complete divisor-collision count satisfies

\[
C(a,d)
<
\frac{20N}d+13\sqrt N+8k.
\]

### Proof

Sum CMR53 over `h=1,...,k-t-1`. The geometric estimates

\[
\sum_{h\ge1}p^{k-t-h}
<
\frac{M}{p-1},
\]

and

\[
\sum_{h\ge1}p^{(k-t-h)/2}
<
\frac{\sqrt M}{\sqrt p-1}
\]

show that the `L/d` contribution is less than `8M/d` for odd `p`, while the
square-root contribution is less than `11 sqrt(M)`. The constant terms from
the nonzero strata, together with the at-most-one origin pair, are less than
`8k`.

Add the same-stratum bound CMR51 and use `M<=N`. ∎

## 4. Unconditional deterministic energy and syndrome

### Theorem CMR55 — PROVED

Every odd-prime completed-reciprocal channel satisfies

\[
\mathcal E(R_{\mathbf c})
\le
20NkH_N^2
+(N-1)(13\sqrt N+8k).
\]

In particular,

\[
\mathcal E(R_{\mathbf c})
=
O(N^{3/2}+N\log^3N).
\]

Its number of real collinear triples satisfies

\[
T(R_{\mathbf c})
=
O(N^2\log N+N^{3/2}\log^3N)
=
O(N^2\log N).
\]

### Proof

Insert CMR54 into the divisor reduction CMR45. The `20N/d` term is summed as in
CMR46 and contributes at most

\[
20NkH_N^2.
\]

For the remaining term, use

\[
\sum_{d\mid A}\varphi(d)=A.
\]

Thus every positive column difference contributes at most

\[
13\sqrt N+8k
\]

from the boundary term, giving the displayed energy estimate.

Finally apply CMR32. The first part contributes `O(N^2 log N)`, and multiplying
the energy estimate by `sqrt(N)` contributes

\[
O(N^2+N^{3/2}\log^3N).
\]

This proves the syndrome bound. ∎

## 5. Remaining analytic target

CMR55 improves the previous `O(N^(5/2)+N^2 log N)` syndrome to quadratic order
up to a logarithm. The remaining gap to the desired repair regime is the
square-root boundary term in CMR54. Removing it requires a sharper count of
the rare carries where the discriminant vanishes to nearly the full modulus,
or a bank that absorbs those carries recursively.

The finite checker is
[`scripts/verify_prime_power_cross_stratum_sum.py`](../scripts/verify_prime_power_cross_stratum_sum.py).
