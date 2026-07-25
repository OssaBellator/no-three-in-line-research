# Placement-count cleaning above height `0.44t`

CMR252 treats the class with maximal vertical direction component by allowing
three positions for every reduced horizontal step. Those positions overlap
strongly when the board vertex is fixed. Summing their exact validity intervals
before discarding coprimality gives a better uniform vertex load and lowers the
exact target-specific candidate-only threshold to `0.44t`.

Retain the notation of CMR252. Thus `t` is odd, `w` is one fixed parent source
row or target column, and `T_3(w)` counts compatible candidate-only triples in
the primitive three-point regime.

## 1. Summed placement bound

### Theorem CMR261 — PROVED

Let

\[
\frac{t-1}{3}<H\le\frac{t-1}{2}.
\]

Then every parent board vertex satisfies

\[
\boxed{
T_3(w)
\le
\sum_{K=H}^{(t-1)/2}
\left[
2\varphi(K)(t-K)
+
2(t-1)(t-2K)
\right].
}
\]

### Proof

Fix a source vertex `x=x_0`. As in CMR252, directions with horizontal component
`u=K` contribute at most

\[
2\varphi(K)(t-K).
\]

Now consider directions with vertical component `|v|=K` and reduced horizontal
step `u`. Let `n_u(x_0)` be the number of positions in which `x_0` can occur in

\[
x,
\qquad
x+u,
\qquad
x+2u.
\]

The three positions are valid respectively under

\[
2u\le x_0,
\qquad
u\le x_0\le t-1-u,
\qquad
2u\le t-1-x_0.
\]

Therefore, even before the coprimality restriction is imposed,

\[
\sum_{\substack{1\le u<K\\(u,K)=1}}n_u(x_0)
\le
\left\lfloor\frac{x_0}{2}\right\rfloor
+
\min\{x_0,t-1-x_0\}
+
\left\lfloor\frac{t-1-x_0}{2}\right\rfloor
\le t-1.
\]

Each valid placement has at most `t-2K` vertical translates, and the two signs
of `v` give contribution at most

\[
2(t-1)(t-2K).
\]

Adding the two direction classes proves the source-vertex bound. Interchanging
coordinates proves the same statement for a target vertex. ∎

## 2. Explicit `0.44t` threshold

Put

\[
H_1=\left\lceil\frac{11t}{25}\right\rceil.
\]

### Theorem CMR262 — PROVED

For every odd

\[
t\ge347,
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
`H_1`.

### Proof

Use `\varphi(K)\le K` in CMR261 and define

\[
g_t(x)
=
2x(t-x)+2(t-1)(t-2x).
\]

The function is positive and decreasing on the relevant interval. Hence

\[
T_3(w)
\le
\int_{11t/25-1}^{(t-1)/2}g_t(x)\,dx.
\]

The integral equals

\[
\frac{579}{15625}t^3
+
\frac{1189}{2500}t^2
+
\frac{57}{50}t
-
\frac{25}{12}.
\]

The remaining margin below `1/24` is at least

\[
\frac{
1729t^3-600225t^2+728750t+31250
}{
375000t(t-1)(t-2)
}.
\]

The numerator is positive at `t=347`; its derivative is positive and increasing
from that point onward. ∎

### Corollary CMR263 — PROVED

For every odd parent block with

\[
t\ge347,
\qquad
H\ge\left\lceil\frac{11t}{25}\right\rceil,
\]

there is a complete target-specific parent permutation which omits `z_*` and
contains no compatible candidate-only triple of primitive height at least `H`.

### Proof

Apply CMR249 with the target singleton event and the indicated rank-three
candidate events. CMR262 verifies the local-load hypothesis. ∎

## 3. Protected-line reserve

### Theorem CMR264 — PROVED

Let `t` be odd with

\[
t\ge611,
\]

and put

\[
R_1(t)=\left\lfloor\frac t{500}\right\rfloor.
\]

For every family of at most `R_1(t)` distinct nonaxis real lines, there is a
complete parent permutation which

1. omits `z_*`;
2. avoids every available cell on the protected lines;
3. avoids every candidate-only triple of primitive height at least
   `ceil(11t/25)`.

### Proof

The protected lines contribute singleton-event load at most

\[
\frac{R_1(t)}t\le\frac1{500}
\]

at every board vertex. Using the integral from CMR262, the remaining margin is
at least

\[
\frac{
979t^3-597975t^2+727250t+31250
}{
375000t(t-1)(t-2)
}.
\]

The numerator is positive at `t=611`, and its derivative is positive and
increasing thereafter. The target-specific matching-space local lemma CMR249
now supplies the required permutation. ∎

### Corollary CMR265 — PROVED

Let a globally minimal positive-potential inherited parent block have odd size
`t>=611`, and fix one endpoint `z_*` of an old target triple. Then either

1. a target-specific state creates a rank-one or rank-two certificate and hence
   exposes an anchored alternating continuation; or
2. there are `R_1(t)+1` distinct candidate-only real-line signatures, all of
   primitive height below `ceil(11t/25)`, and one target-specific state avoids
   the first `R_1(t)` lines together with the entire higher slice.

### Proof

Iterate CMR264 exactly as in CMR256. Every candidate-only replacement line is
new because all available cells on the protected lines are forbidden, and it is
below the threshold because the whole higher slice is avoided. ∎

## 4. Revised intermediate-height endpoint

The exact target-specific candidate-only cleaning boundary is now

\[
0.44t,
\]

with a simultaneous linear protected-line reserve. The remaining height problem
is confined below this threshold. Further improvement requires either a sharper
uniform count of reduced placements or an exact completion theorem for a
bounded-conflict intermediate band.

No all-`n` theorem is claimed here. The placement bound, polynomial thresholds,
and exact small-board loads are checked in
[`scripts/verify_prime_power_role_count_height.py`](../scripts/verify_prime_power_role_count_height.py).
