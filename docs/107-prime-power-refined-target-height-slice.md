# Refined target-specific cleaning above height `0.45t`

CMR231 bounded the top primitive-height slice by assigning at most `t` triples
to every direction and board vertex. A fixed matching vertex sees much less:
when the large component of the direction lies on that side of the board, only
one of the three positions in the primitive progression can occur. Keeping this
asymmetry lowers the exact target-specific cleaning threshold from `0.49t` to
`0.45t` and retains a linear forbidden-line reserve.

Work in the normalized parent board `[0,t-1]^2`, where `t` is odd. Fix one old
target cell `z_*`, and let the target-specific state space consist of all parent
permutations omitting `z_*`.

For a primitive unoriented nonaxis direction choose the representative

\[
(u,v),
\qquad
u>0,
\qquad
v\ne0,
\]

and put

\[
K=\max\{u,|v|\}.
\]

## 1. Refined vertex load in the three-point regime

### Theorem CMR252 — PROVED

Let

\[
\frac{t-1}{3}<H\le\frac{t-1}{2},
\]

and let `T_3(w)` be the number of compatible candidate-only collinear triples
incident with one fixed parent source row or target column `w` and having
primitive height at least `H`. Then

\[
\boxed{
T_3(w)
\le
\sum_{K=H}^{(t-1)/2}
2\varphi(K)(4t-7K).
}
\]

### Proof

Because `K>(t-1)/3`, every board line in the direction `(u,v)` contains at most
three grid points. Any candidate triple in that direction is therefore one
primitive progression

\[
P,
\qquad
P+(u,v),
\qquad
P+2(u,v).
\]

Fix first a source vertex, hence one vertical board slice `x=x_0`. Split the
primitive directions of height `K` into two classes.

### Horizontal component maximal

Let

\[
u=K,
\qquad
1\le |v|<K.
\]

Since `3K>t-1`, the validity intervals corresponding to the three possible
positions of `x_0` in the progression are disjoint. Thus at most one position is
possible. Once that position is fixed, there are at most

\[
t-2|v|
\]

vertical translates.

For every reduced residue `r` modulo `K` there are two signs of `v`, and

\[
\sum_{\substack{1\le r<K\\(r,K)=1}}r
=
\frac{K\varphi(K)}2.
\]

The total contribution of this class is therefore at most

\[
2\sum_{\substack{1\le r<K\\(r,K)=1}}(t-2r)
=
2\varphi(K)(t-K).
\]

### Vertical component maximal

Let

\[
|v|=K,
\qquad
1\le u<K.
\]

There are at most three possible positions of `x_0` in the progression. For
each position there are at most

\[
t-2K
\]

vertical translates. The two signs of `v` and the `\varphi(K)` reduced positive
values of `u` give total contribution at most

\[
6\varphi(K)(t-2K).
\]

Adding the two classes gives

\[
2\varphi(K)(t-K)+6\varphi(K)(t-2K)
=
2\varphi(K)(4t-7K).
\]

For a fixed target vertex, interchange the two coordinate roles. The same two
class totals occur in the opposite order, so the same bound holds. Summing over
`K` proves the theorem. ∎

## 2. An explicit `0.45t` matching-space threshold

Put

\[
H_0=\left\lceil\frac{9t}{20}\right\rceil,
\qquad
m_0=\frac{t-1}{2}.
\]

### Theorem CMR253 — PROVED

For every odd

\[
t\ge169,
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
`H_0`.

### Proof

Use `\varphi(K)\le K` in CMR252 and put

\[
f_t(x)=2x(4t-7x).
\]

On the interval beginning at `9t/20-1`, this function is positive and decreasing
for the present values of `t`. Hence

\[
T_3(w)
\le
\sum_{K=H_0}^{m_0}f_t(K)
\le
\int_{9t/20-1}^{(t-1)/2}f_t(x)\,dx.
\]

The integral is

\[
\frac{383}{12000}t^3
+
\frac{103}{200}t^2
+
\frac{31}{20}t
-
\frac{49}{12}.
\]

After inserting this bound, the difference between `1/24` and the displayed
vertex load is at least

\[
\frac{
117t^3-19680t^2+18400t+25000
}{
12000t(t-1)(t-2)
}.
\]

The numerator is positive at `t=169` and increasing for every `t>=169`. This
proves the claim. ∎

## 3. Exact target-specific high-slice cleaning

### Corollary CMR254 — PROVED

For every odd parent block with

\[
t\ge169,
\qquad
H\ge\left\lceil\frac{9t}{20}\right\rceil,
\]

there is a complete parent permutation which

1. omits the designated old target cell `z_*`;
2. contains no compatible candidate-only collinear triple of primitive height
   at least `H`;
3. preserves saturation and inherited layer disjointness.

### Proof

Apply the target-specific matching-space local lemma CMR249. Use the singleton
bad event for `z_*` and the rank-three events from the indicated height slice.
CMR253 bounds the total probability load at every board vertex by less than
`1/24`. ∎

The conclusion concerns candidate-only board triples. It does not claim to
exclude rank-one or rank-two triples using fixed outside points.

## 4. A linear forbidden-line reserve at height `0.45t`

### Theorem CMR255 — PROVED

Let `t` be odd with

\[
t\ge343,
\]

and put

\[
R(t)=\left\lfloor\frac t{200}\right\rfloor.
\]

Fix any at most `R(t)` distinct nonaxis real lines. There is a complete
parent permutation which

1. omits `z_*`;
2. avoids every available parent-board cell on each fixed line;
3. avoids every candidate-only triple of primitive height at least
   `ceil(9t/20)`.

### Proof

A nonaxis line cuts the matching board in a partial matching. Consequently its
available cells contribute at most one singleton event at each source or target
vertex. The chosen line family therefore contributes vertex load at most

\[
\frac{R(t)}t\le\frac1{200}.
\]

The target cell contributes at most `1/t`, and CMR252 gives the high-slice
rank-three load. The calculation in CMR253 now yields

\[
\frac1{200}+
\frac1t+
\frac{T_3(w)}{(t)_3}
<
\frac1{24},
\]

because the remaining margin is at least

\[
\frac{
57t^3-19500t^2+18280t+25000
}{
12000t(t-1)(t-2)
}.
\]

Its numerator is positive at `t=343` and increasing thereafter. CMR249 applied
to the target event, the fixed-line singleton events, and the high-slice
rank-three events supplies the required permutation. ∎

## 5. Frozen-parent lower-height reserve

### Corollary CMR256 — PROVED

Let a globally minimal positive-potential inherited parent block have odd size
`t>=343`, and fix one endpoint `z_*` of an old target triple. At least one of the
following holds.

1. A target-specific parent state creates a rank-one or rank-two triple, giving
   an anchored alternating continuation.
2. There are

   \[
   R(t)+1
   \]

   distinct candidate-only real-line signatures, all of primitive height below

   \[
   \left\lceil\frac{9t}{20}\right\rceil,
   \]

   and one target-specific parent permutation simultaneously avoids the first
   `R(t)` lines and every candidate-only triple at or above that height.

### Proof

Apply CMR255 first with no fixed line. The resulting permutation moves `z_*` and
contains no high-slice candidate-only triple. Global minimality requires a new
covering certificate. If it is rank one or two, the first alternative holds.
Otherwise it supplies one lower-height candidate-only line.

Repeat, adding every discovered line to the fixed reserve. Until `R(t)` lines
have been accumulated, CMR255 remains applicable. Every later candidate-only
certificate lies on a new line because every available cell of the earlier
lines is forbidden. Applying CMR255 once more with all `R(t)` earlier lines
produces either an anchored certificate or the `(R(t)+1)`-st distinct
lower-height line. ∎

## 6. Revised height endpoint

The exact candidate-only cleaning threshold has moved from `0.49t` to `0.45t`
for target-specific parent escape. A linear line reserve survives at the same
threshold. The remaining intermediate-height problem now begins below

\[
0.45t,
\]

while anchored rank-one and rank-two certificates remain delegated to the
alternating continuation machinery.

No all-`n` theorem is claimed here. The direction-class count, both polynomial
margins, and small-grid triple loads are checked in
[`scripts/verify_prime_power_refined_target_height.py`](../scripts/verify_prime_power_refined_target_height.py).
