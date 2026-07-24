# Critical cells in completed-reciprocal divisor collisions

CMR45 reduces deterministic harmonic energy to the counts `C(a,d)`. This
chapter proves that all regular valuation cells already satisfy the desired
`O(N/d)` scale. The unresolved mass is confined to two explicit carry residue
classes.

Let

\[
N=p^k,
\qquad
f=R_{\mathbf c},
\qquad
a=p^tA,
\qquad p\nmid A.
\]

Fix a divisor `d` of `A`. If a pair at columns `x,x+a` contributes to
`C(a,d)`, write its exact row difference as

\[
f(x+a)-f(x)=p^t d m.
\]

CMR6 implies

\[
p\nmid m,
\qquad
0<|m|<\frac{p^{k-t}}d.
\]

Put

\[
M=p^{k-t}.
\]

## 1. Same-stratum pairs

Suppose

\[
v_p(x)=v_p(x+a)=r\le t.
\]

Write

\[
x=p^ru,
\qquad
x+a=p^rv,
\qquad
v=u+p^{t-r}A,
\]

with `u,v` units.

### Theorem CMR47 — PROVED

Every such divisor collision satisfies

\[
dmuv+Ac_r\equiv0\pmod M.
\]

For fixed `m`, the possible residues `u` modulo `M` are roots of

\[
dm\,u(u+p^{t-r}A)+Ac_r\equiv0\pmod M.
\]

1. If `r<t`, this quadratic has at most two roots modulo `M`.
2. If `r=t`, it has at most two roots unless
   \[
   dmA\equiv4c_t\pmod p.
   \]

### Proof

Write the two unit row coordinates in the stratum as `w,w'`, so

\[
f(x)=p^rw,
\qquad
f(x+a)=p^rw',
\qquad
w'-w=p^{t-r}dm.
\]

The reciprocal equations are

\[
uw\equiv c_r,
\qquad
vw'\equiv c_r
\pmod {p^{k-r}}.
\]

Substitute the row difference into the second equation, subtract the first,
divide by `p^(t-r)`, and multiply by `u`. This gives the displayed congruence
modulo `M`.

After division by the unit `dm`, the quadratic discriminant is

\[
\Delta_{r,m}
=
(p^{t-r}A)^2-4Ac_r(dm)^{-1}
\pmod M.
\]

If `r<t`, its reduction modulo `p` is nonzero, so every root is simple and
there are at most two. If `r=t`, the discriminant vanishes modulo `p` exactly
when

\[
A^2dm-4Ac_t\equiv0\pmod p,
\]

which is the stated condition. ∎

## 2. Regular same-stratum mass

### Corollary CMR48 — PROVED

For a fixed stratum `r<t`, the number of divisor collisions is less than

\[
\frac{4p^{k-r}}d.
\]

The nonsingular part of the critical stratum `r=t` is less than

\[
\frac{4M}d.
\]

Summing the regular strata `r<t` gives less than

\[
\frac{4N}{d}\sum_{r=0}^{t-1}p^{-r}
<
\frac{6N}d
\]

for odd `p`.

### Proof

There are fewer than `2M/d` possible signed nonzero values of `m`. Each simple
quadratic has at most two roots modulo `M`.

For `r<t`, one root modulo `M` has exactly `p^(t-r)` lifts to a unit parameter
modulo `p^(k-r)`. Thus the count is less than

\[
2\cdot\frac{2M}d\cdot p^{t-r}
=
\frac{4p^{k-r}}d.
\]

For `r=t`, there is no lift factor. The geometric sum proves the last bound. ∎

## 3. Cross-stratum pairs

Suppose the endpoint valuations are different. CMR6 and

\[
v_p((x+a)-x)=t
\]

force the smaller endpoint valuation to equal `t`. Let the other valuation be
`r>t`.

### Theorem CMR49 — PROVED

Every cross-stratum divisor collision satisfies the single carry condition

\[
dmA\equiv c_t\pmod p,
\]

where `c_t` is the completed-reciprocal parameter of the lower-valuation
endpoint. The same condition holds in either orientation of the two endpoints.

### Proof

First suppose `x=p^ru` and `x+a=p^tv`, so

\[
v=A+p^{r-t}u.
\]

After dividing the exact row difference by `p^t`, the reciprocal equations give

\[
c_t v^{-1}-p^{r-t}c_ru^{-1}\equiv dm\pmod M.
\]

Multiply by `uv` and reduce modulo `p`. Since `v` is congruent to `A`, the
terms containing `p^(r-t)` disappear and one obtains

\[
c_tu\equiv dmAu\pmod p.
\]

Cancel the unit `u`.

In the reverse orientation, `v` is congruent to `-A` modulo `p`, and both signs
reverse; the same condition results. ∎

## 4. Revised deterministic endpoint

CMR48 proves the desired divisor-collision scale for every same-stratum cell
strictly below the displacement valuation and for the nonsingular part of the
critical stratum. All remaining mass lies in only two explicit carry classes:

\[
dmA\equiv4c_t\pmod p
\]

for singular same-stratum pairs, and

\[
dmA\equiv c_t\pmod p
\]

for cross-stratum pairs.

Thus CMR46 no longer requires a uniform analysis over all carries. It is
enough to prove an `O(polylog(N) N/d)` bound for these two critical classes, or
to absorb them using the recursive top-digit blocks.

The finite checker is
[`scripts/verify_prime_power_critical_collisions.py`](../scripts/verify_prime_power_critical_collisions.py).
