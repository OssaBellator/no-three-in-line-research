# Parity-sieved target cleaning above height `0.43t`

CMR261 isolates the only totient-weighted part of the high-direction vertex
load. Even direction heights satisfy a uniform factor-two totient saving. A
monotone pairing of consecutive heights transfers this saving to at least half
of the weighted height mass, modulo one endpoint term. This lowers the exact
target-specific candidate-only threshold from `0.44t` to `0.43t`.

Retain the normalized odd parent board and target-specific notation from
CMR261. Put

\[
m=\frac{t-1}{2}.
\]

## 1. Parity-sieved vertex load

### Theorem CMR266 — PROVED

Let

\[
\frac{t-1}{3}<H\le m.
\]

Define

\[
S(H)=\sum_{K=H}^{m}K(t-K),
\qquad
R(H)=\sum_{K=H}^{m}(t-2K).
\]

Then every parent board vertex satisfies

\[
\boxed{
T_3(w)
\le
\frac32 S(H)
+
\frac12 m(t-m)
+
2(t-1)R(H).
}
\]

### Proof

CMR261 gives

\[
T_3(w)
\le
2\sum_{K=H}^{m}\varphi(K)(t-K)
+
2(t-1)R(H).
\]

Put

\[
h(K)=K(t-K).
\]

For every `K`, `\varphi(K)\le K`, while for even `K`,

\[
\varphi(K)\le\frac K2.
\]

Let

\[
E(H)=\sum_{\substack{H\le K\le m\\K\text{ even}}}h(K).
\]

Therefore

\[
\sum_{K=H}^{m}\varphi(K)(t-K)
\le
S(H)-\frac12E(H).
\]

The function `h(K)` is increasing on the integer interval up to `m`. Pair each
odd height with the following even height. Every paired even term is at least
its odd partner. An initial unpaired even term only helps; the only possible
unpaired adverse term is the final odd height, whose mass is at most `h(m)`.
Consequently

\[
E(H)
\ge
\frac{S(H)-h(m)}2.
\]

It follows that

\[
2\sum_{K=H}^{m}\varphi(K)(t-K)
\le
\frac32S(H)+\frac12h(m).
\]

Substitution into CMR261 proves the theorem. ∎

## 2. Explicit `0.43t` threshold

Put

\[
H_2=\left\lceil\frac{43t}{100}\right\rceil.
\]

### Theorem CMR267 — PROVED

For every odd

\[
t\ge295,
\]

every parent board vertex satisfies

\[
\boxed{
\frac1t+
\frac{T_3(w)}{(t)_3}
<
\frac1{24}
}
\]

when `T_3(w)` counts only candidate-only triples of primitive height at least
`H_2`.

### Proof

The function `x(t-x)` is increasing through the relevant integer interval and
symmetric about `t/2`. Hence

\[
S(H_2)
\le
\int_{43t/100}^{(t+1)/2}x(t-x)\,dx.
\]

The function `t-2x` is decreasing, so

\[
R(H_2)
\le
\int_{43t/100-1}^{(t-1)/2}(t-2x)\,dx.
\]

Also

\[
m(t-m)\le\frac{t^2}{4}.
\]

After inserting these three bounds into CMR266, one obtains

\[
T_3(w)
\le
\frac{71757}{2000000}t^3
+
\frac{5827}{10000}t^2
+
\frac{61}{50}t
-
\frac{25}{16}.
\]

The remaining margin below `1/24` is at least

\[
\frac{
34729t^3-10246200t^2+11180000t-2625000
}{
6000000t(t-1)(t-2)
}.
\]

The numerator is positive at `t=295`, and its derivative is positive and
increasing from that point onward. ∎

### Corollary CMR268 — PROVED

For every odd parent block with

\[
t\ge295,
\qquad
H\ge\left\lceil\frac{43t}{100}\right\rceil,
\]

there is a complete target-specific parent permutation which omits `z_*` and
contains no compatible candidate-only collinear triple of primitive height at
least `H`.

### Proof

Apply CMR249 using the target singleton event and the indicated high-slice
rank-three events. CMR267 verifies the matching-space local-load condition. ∎

## 3. Protected-line reserve

### Theorem CMR269 — PROVED

Let `t` be odd with

\[
t\ge449,
\]

and put

\[
R_2(t)=\left\lfloor\frac t{500}\right\rfloor.
\]

For every family of at most `R_2(t)` distinct nonaxis real lines, there is a
complete parent permutation which

1. omits `z_*`;
2. avoids every available cell on the protected lines;
3. avoids every candidate-only triple of primitive height at least
   `ceil(43t/100)`.

### Proof

The protected lines contribute matching-vertex singleton load at most `1/500`.
Using the CMR267 estimate, the remaining margin is at least

\[
\frac{
22729t^3-10210200t^2+11156000t-2625000
}{
6000000t(t-1)(t-2)
}.
\]

Its numerator is positive at `t=449`, and its derivative is positive and
increasing thereafter. CMR249 gives the required permutation. ∎

### Corollary CMR270 — PROVED

Let a globally minimal positive-potential inherited parent block have odd size
`t>=449`, and fix one endpoint `z_*` of an old target triple. Then either

1. a target-specific state creates a rank-one or rank-two certificate and hence
   exposes an anchored alternating continuation; or
2. there are `R_2(t)+1` distinct candidate-only real-line signatures, all of
   primitive height below `ceil(43t/100)`, and one target-specific state avoids
   the first `R_2(t)` lines together with the entire higher slice.

### Proof

Iterate CMR269 as in CMR256 and CMR265. Every candidate-only replacement line is
new and lies below the protected height threshold. ∎

## 4. Revised intermediate-height endpoint

The exact target-specific candidate-only cleaning boundary is now

\[
0.43t,
\]

using only elementary parity information about Euler's totient function. A
linear protected-line reserve survives at the same threshold. The remaining
height problem is confined below `0.43t`, together with anchored triples and the
mixed/nontrivial sharp blocker geometries from CMR260.

No all-`n` theorem is claimed here. The parity-pair inequality, polynomial
thresholds, and exact small-board loads are checked in
[`scripts/verify_prime_power_parity_height.py`](../scripts/verify_prime_power_parity_height.py).
