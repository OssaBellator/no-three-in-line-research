# Exact avoidance of the top primitive-height slice

CMR223--CMR226 treat a dyadic height band as a bounded conflict system and
obtain an almost-perfect conflict-free matching. At the very top of the
primitive-height range, the matching-space local-load theorem CMR219 is already
strong enough to give an exact parent permutation.

Work in one normalized nonroot parent board of odd size `t`. For a primitive
nonaxis direction `(u,v)`, put

\[
K=\max\{|u|,|v|\}.
\]

A compatible triple can occur only when

\[
K\le\frac{t-1}{2}.
\]

## 1. Exact direction count and vertex load

### Theorem CMR231 — PROVED

Let

\[
\frac{t-1}{3}<H\le\frac{t-1}{2},
\]

and let `\mathcal C_{\ge H}` be the family of compatible candidate-only
collinear triples whose primitive direction height satisfies

\[
H\le K\le\frac{t-1}{2}.
\]

For every parent source row or target column `w`, the number `T_3(w)` of such
triples incident with `w` satisfies

\[
\boxed{
T_3(w)
\le
4t\sum_{K=H}^{(t-1)/2}\varphi(K)
\le
2t\left(
\frac{t^2-1}{4}-H(H-1)
\right).
}
\]

### Proof

For every integer `K>=2`, the number of primitive unoriented nonaxis integer
directions with maximum coordinate `K` is exactly

\[
4\varphi(K).
\]

Indeed, the primitive points on the boundary of the square `[-K,K]^2` number
`8\varphi(K)`, and identifying opposite directions divides this by two.

Fix one such direction and one board cell incident with `w`. Since

\[
K>\frac{t-1}{3},
\]

the integer parameter interval of the line contains at most three board
points. Consequently at most one triple of this direction contains the fixed
cell. There are at most `t` cells incident with `w`, so this direction
contributes at most `t` triples.

Summing the `4\varphi(K)` directions gives the first bound. Finally use
`\varphi(K)\le K` and, because `t` is odd,

\[
\sum_{K=H}^{(t-1)/2}K
=
\frac12\left(
\frac{t^2-1}{4}-H(H-1)
\right).
\]

Compatibility and the missing old diagonal only reduce the count. ∎

## 2. The matching-space threshold

### Theorem CMR232 — PROVED

Let

\[
c>\sqrt{\frac{11}{48}}.
\]

For every sufficiently large odd `t`, if

\[
H\ge ct,
\]

then every parent board vertex satisfies

\[
\boxed{
\frac1t+
\frac{T_3(w)}{(t)_3}<\frac1{24}.
}
\]

An explicit finite version is

\[
\boxed{
 t\ge95,
 \qquad
 H\ge\left\lceil\frac{49t}{100}\right\rceil
}
\]

which implies the same inequality.

### Proof

CMR231 gives

\[
\frac{T_3(w)}{(t)_3}
\le
\frac{
2\left((t^2-1)/4-H(H-1)\right)
}{(t-1)(t-2)}.
\]

If `H\ge ct`, the right side has limit superior

\[
2\left(\frac14-c^2\right)
=
\frac12-2c^2
<
\frac1{24}.
\]

The additional diagonal load `1/t` tends to zero, proving the asymptotic
statement.

For the explicit claim, use `H\ge49t/100`. It is enough to check

\[
\frac1t+
\frac{
2\left((t^2-1)/4-(49t/100)(49t/100-1)\right)
}{(t-1)(t-2)}
\le
\frac1{24}.
\]

After clearing positive denominators, this is

\[
328t^3-31575t^2+53750t-30000\ge0.
\]

The cubic is increasing and positive for every `t\ge95`; the companion checker
verifies the exact integer boundary. ∎

## 3. Exact top-slice cleaning

### Corollary CMR233 — PROVED

For every odd parent block with

\[
t\ge95,
\qquad
H\ge\left\lceil\frac{49t}{100}\right\rceil,
\]

there is a parent permutation which

1. avoids every old diagonal cell;
2. contains no compatible collinear triple whose primitive height is at least
   `H`;
3. preserves saturation and inherited layer disjointness.

### Proof

Apply CMR219 with the old diagonal singleton events and with
`\mathcal F_3=\mathcal C_{\ge H}`. There are no rank-one or rank-two events in
this band-only application. CMR232 verifies the local-load hypothesis at every
board vertex, so the matching-space lopsided local lemma supplies a perfect
matching avoiding all bad events. ∎

The conclusion is exact, unlike CMR226. It does not yet clean lower primitive
heights, and a permutation chosen for this slice may create triples in those
lower bands.

## 4. Revised height programme

The top `1/50` of the possible primitive-height interval is now removable by
one exact parent move for every sufficiently large odd block. More generally,
CMR232 identifies the natural local-load boundary

\[
c=\sqrt{11/48}\approx0.4787.
\]

The remaining exact-band task starts below this constant-height threshold. It
may be attacked by combining

- the half-line deletion resilience CMR228--CMR230;
- the almost-perfect bounded-conflict matching CMR226;
- and a reserve or switching completion for the intermediate-height bands.

No all-`n` theorem is claimed here. Primitive-direction counts and the explicit
`49/100`, `t\ge95` inequality are checked in
[`scripts/verify_prime_power_exact_top_slice.py`](../scripts/verify_prime_power_exact_top_slice.py).
