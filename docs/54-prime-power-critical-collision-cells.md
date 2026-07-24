# Critical cells in completed-reciprocal divisor collisions

CMR56 reduces deterministic harmonic energy to the counts `C(a,d)`. All
regular valuation cells satisfy the desired `O(N/d)` scale; the unresolved
mass is confined to explicit carry classes.

Let

\[
N=p^k,
\qquad f=R_{\mathbf c},
\qquad a=p^tA,
\qquad p\nmid A,
\]

and fix a divisor `d` of `A`. If the pair at columns `x,x+a` contributes to
`C(a,d)`, write

\[
f(x+a)-f(x)=p^tdm,
\qquad
M=p^{k-t}.
\]

Then \(p\nmid m\) and \(0<|m|<M/d\).

## Same-stratum pairs

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
v=u+p^{t-r}A.
\]

### Theorem CMR58 — PROVED

Every such collision satisfies

\[
dmuv+Ac_r\equiv0\pmod M.
\]

For fixed `m`, the parameter `u` is a root of

\[
dm\,u(u+p^{t-r}A)+Ac_r\equiv0\pmod M.
\]

If `r<t`, this quadratic has at most two roots. If `r=t`, it has at most two
roots unless

\[
dmA\equiv4c_t\pmod p.
\]

### Proof

Write \(f(x)=p^rw\), \(f(x+a)=p^rw'\), so
\(w'-w=p^{t-r}dm\). The reciprocal equations are

\[
uw\equiv c_r,
\qquad
vw'\equiv c_r
\pmod {p^{k-r}}.
\]

Substitute the row difference, subtract, divide by \(p^{t-r}\), and multiply by
`u`. This gives the displayed congruence modulo `M`.

After division by the unit `dm`, the discriminant is

\[
(p^{t-r}A)^2-4Ac_r(dm)^{-1}.
\]

For `r<t` its reduction modulo `p` is nonzero. For `r=t` it vanishes exactly
under the displayed carry condition. ∎

### Corollary CMR59 — PROVED

For fixed `r<t`, the number of divisor collisions is less than

\[
\frac{4p^{k-r}}d.
\]

The nonsingular part of `r=t` is less than \(4M/d\). Summing all regular
strata `r<t` gives less than \(6N/d\) for odd `p`.

### Proof

There are fewer than `2M/d` signed nonzero carries. Each simple quadratic has
at most two roots modulo `M`. For `r<t`, one root has \(p^{t-r}\) lifts to the
full stratum parameter. Sum the resulting geometric series. ∎

## Cross-stratum pairs

If the endpoint valuations differ, CMR6 forces the smaller valuation to equal
`t`.

### Theorem CMR60 — PROVED

Every cross-stratum divisor collision satisfies

\[
dmA\equiv c_t\pmod p,
\]

in either orientation of the endpoints.

### Proof

Suppose \(x=p^ru\), \(x+a=p^tv\) with `r>t`, so
\(v=A+p^{r-t}u\). The reduced row equation is

\[
c_tv^{-1}-p^{r-t}c_ru^{-1}\equiv dm\pmod M.
\]

Multiply by `uv` and reduce modulo `p`. Terms containing \(p^{r-t}\) vanish,
and \(v\equiv A\), giving \(c_tu\equiv dmAu\). Cancel `u`. The reverse
orientation gives the same condition. ∎

Thus every unresolved collision lies either in the singular same-stratum class
\(dmA\equiv4c_t\pmod p\) or the cross-stratum class
\(dmA\equiv c_t\pmod p\). The following chapters sum both.

The checker is
[`scripts/verify_prime_power_critical_collisions.py`](../scripts/verify_prime_power_critical_collisions.py).
