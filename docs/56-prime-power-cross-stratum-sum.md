# Cross-stratum collision sums and a quadratic-order syndrome bound

CMR60 confines every cross-stratum divisor collision to one carry residue
class modulo `p`. The carry is fixed modulo the full valuation gap, and the
remaining quadratic discriminant has a uniform two-root form.

Retain

\[
N=p^k,
\qquad a=p^tA,
\qquad d\mid A,
\qquad M=p^{k-t}.
\]

First suppose the two endpoints are nonzero and their valuations are `t` and
\(r=t+h>t\). Put \(L=p^{k-r}=M/p^h\). The possible pair containing the
origin is treated separately.

## Full carry congruence

### Theorem CMR63 — PROVED

Every nonzero cross-stratum divisor collision satisfies

\[
dmA\equiv c_t\pmod {p^h}.
\]

Write

\[
z=\frac{dmA-c_t}{p^h}.
\]

For either orientation, the higher-valuation unit parameter `u` satisfies a
quadratic modulo `L` with discriminant

\[
\Delta_z=(z-p^hc_r)^2-4c_rc_t.
\]

A pair containing the origin satisfies

\[
dmA\equiv c_t\pmod M
\]

directly and contributes at most one collision for fixed `a,d`.

### Proof

Take \(x=p^ru\), \(x+a=p^tv\), so \(v=A+p^hu\). The reduced row equation is

\[
c_tv^{-1}-p^hc_ru^{-1}\equiv dm\pmod M.
\]

Multiplying by `uv` and expanding gives

\[
dmp^hu^2+(dmA-c_t+p^{2h}c_r)u+p^hc_rA\equiv0\pmod M.
\]

Reduction modulo \(p^h\) and cancellation of the unit `u` gives the carry
congruence. Divide by \(p^h\). The resulting quadratic modulo `L` is

\[
dm u^2+(z+p^hc_r)u+c_rA\equiv0.
\]

Its discriminant simplifies using \(dmA=c_t+p^hz\) to the displayed
\(\Delta_z\). The reverse orientation gives the same discriminant.

For the origin pair, the exact reduced row difference is congruent to
\(c_tA^{-1}\) modulo `M`; multiplication by `A` gives the stronger congruence.
∎

## Summing one nonzero cross stratum

### Theorem CMR64 — PROVED

For fixed \(r=t+h<k\), the total number of cross-stratum divisor collisions,
counting both orientations, is less than

\[
8+rac{16L}d+8\sqrt L.
\]

### Proof

The signed carry range is \(0<|m|<M/d\). CMR63 restricts `m` to one residue
class modulo \(p^h\), so the number `J` of carries is at most

\[
J\le1+rac{2M}{dp^h}=1+rac{2L}d.
\]

The corresponding values `z` form an arithmetic progression of length `J`
and unit step modulo `p`. For fixed `z`, the number of `u` values is the square
root count of \(\Delta_z\) modulo `L`.

For every `s`, the congruence

\[
(z-p^hc_r)^2\equiv4c_rc_t\pmod {p^{2s}}
\]

has zero or two residue classes. Each meets the `z` progression in at most
\(1+J/p^{2s}\) places. The valuation layer decomposition used in CMR61 gives
fewer than

\[
4J+4\sqrt L
\]

roots in one orientation. Double for the two orientations. ∎

## Total divisor collisions

### Corollary CMR65 — PROVED

Summing all nonzero higher valuations and the possible origin pair, the
cross-stratum collision count is less than

\[
\frac{8M}d+11\sqrt M+8k.
\]

Consequently

\[
C(a,d)<\frac{20N}d+13\sqrt N+8k.
\]

### Proof

Sum CMR64 over \(h=1,\ldots,k-t-1\). The geometric bounds

\[
\sum_{h\ge1}p^{k-t-h}<\frac{M}{p-1},
\qquad
\sum_{h\ge1}p^{(k-t-h)/2}<\frac{\sqrt M}{\sqrt p-1}
\]

control the `L/d` and square-root terms. The constants, including the origin
pair, are below `8k`. Add CMR62 and use `M<=N`. ∎

## Unconditional deterministic energy and syndrome

### Theorem CMR66 — PROVED

Every odd-prime completed-reciprocal channel satisfies

\[
\mathcal E(R_{\mathbf c})
\le20NkH_N^2+(N-1)(13\sqrt N+8k),
\]

so

\[
\mathcal E(R_{\mathbf c})=O(N^{3/2}+N\log^3N).
\]

Its real collinear triple count satisfies

\[
T(R_{\mathbf c})=O(N^2\log N).
\]

### Proof

Insert CMR65 into CMR56. The `20N/d` term sums as in CMR57 to
\(20NkH_N^2\). For the boundary term, use

\[
\sum_{d\mid A}\varphi(d)=A,
\]

so every positive column difference contributes at most
\(13\sqrt N+8k\). This proves the energy estimate. Apply CMR32: its unweighted
term is \(O(N^2\log N)\), while multiplying the energy by \(\sqrt N\) gives
\(O(N^2+N^{3/2}\log^3N)\). ∎

CMR66 removes a full factor \(\sqrt N\) from the previous general syndrome
bound. The remaining analytic gap is the square-root boundary in CMR65.

The checker is
[`scripts/verify_prime_power_cross_stratum_sum.py`](../scripts/verify_prime_power_cross_stratum_sum.py).
