# Universal bounds for higher-rank prefix collateral

CMR78 leaves two normalized higher-rank terms in the prefix-block repair:

\[
\sum_{a,\ell}
\frac{T_2(A_{s,a,\ell})}{(t)_2}
\qquad\text{and}\qquad
\sum_{a,\ell}
\frac{T_3(A_{s,a,\ell})}{(t)_3}.
\]

They admit geometry-free quadratic bounds. Retain

\[
N=p^k,
\qquad 1\le s<k,
\qquad m=p^s,
\qquad t=N/m,
\]

and one saturated two-layer state `S`.

For a layer-prefix block `A`, let `U(A)` be its allowed replacement cells and
let

\[
Z(A)=S\setminus A.
\]

The forbidden identity matching gives

\[
|U(A)|\le t(t-1),
\]

while

\[
|Z(A)|=2N-t.
\]

## 1. Rank-two certificates

### Theorem CMR90 — PROVED

At every nontrivial quotient scale,

\[
\sum_{a,\ell}
\frac{T_2(A_{s,a,\ell})}{(t)_2}
\le
m(2N-t)(t-1)
<
2N^2.
\]

### Proof

Fix one block `A`. A rank-two certificate consists of one fixed selected point
`P` in `Z(A)` and two compatible allowed cells `z_1,z_2` on one real line.

Choose `P` and an ordered first cell `z_1`. The real line through them meets the
`t`-column by `t`-row block rectangle in at most `t` grid points. One is `z_1`,
so there are at most `t-1` possibilities for `z_2`, even before compatibility
and forbidden-position restrictions are imposed.

Every unordered certificate is counted twice by the ordered choice of its two
block cells. Therefore

\[
T_2(A)
\le
\frac{|Z(A)|\,|U(A)|\,(t-1)}2
\le
\frac{(2N-t)t(t-1)^2}{2}.
\]

Divide by

\[
(t)_2=t(t-1)
\]

to obtain

\[
\frac{T_2(A)}{(t)_2}
\le
\frac{(2N-t)(t-1)}2.
\]

There are exactly `2m` layer-prefix blocks. Summing gives the displayed bound,
and

\[
m(2N-t)(t-1)<2mNt=2N^2.
\]

∎

## 2. Rank-three certificates

### Theorem CMR91 — PROVED

At every nontrivial quotient scale,

\[
\sum_{a,\ell}
\frac{T_3(A_{s,a,\ell})}{(t)_3}
\le
\frac{m(t-1)^2}{3}
<
\frac{Nt}{3}
\le
\frac{N^2}{3p}.
\]

### Proof

Fix one block `A`. Choose an ordered first allowed cell `z_1`. A compatible
second cell must use a different column and row, so there are at most

\[
(t-1)^2
\]

choices for `z_2`. The line through `z_1,z_2` contains at most `t` block grid
points, and hence at most `t-2` further cells after the first two are removed.

Every unordered three-cell certificate is counted six times by its ordered first
and second cells. Thus

\[
T_3(A)
\le
\frac{|U(A)|(t-1)^2(t-2)}6
\le
\frac{t(t-1)^3(t-2)}6.
\]

After division by

\[
(t)_3=t(t-1)(t-2),
\]

one block contributes at most `(t-1)^2/6`. There are `2m` blocks, giving

\[
\sum_{a,\ell}\frac{T_3(A_{s,a,\ell})}{(t)_3}
\le
\frac{m(t-1)^2}{3}.
\]

Finally `mt=N` and `m>=p`. ∎

## 3. The remaining prefix-repair obstruction

Put

\[
\mathcal H_s(S)
=
\sum_{a,\ell}
\left(
\frac{T_2(A_{s,a,\ell})}{(t)_2}
+
\frac{T_3(A_{s,a,\ell})}{(t)_3}
\right).
\]

### Corollary CMR92 — PROVED

For every saturated state and every nontrivial quotient scale,

\[
\mathcal H_s(S)
<
\left(2+\frac1{3p}\right)N^2.
\]

Consequently, if no scale-`s` prefix block improves the triple potential, then
CMR78 and CMR85 give

\[
B_s
<
128\left(
\mathcal M_s(S)
+
\mathcal C_s(S)-|E_s^{\rm coll}|
+
\left(2+\frac1{3p}\right)N^2
\right).
\]

For the corrected balanced recursive bank, CMR88 then yields the expected
one-scale obstruction

\[
O_p(sN^2).
\]

The normalized rank-two and rank-three terms are therefore no longer open.
Below the quadratic-logarithmic level, the sole remaining prefix-repair loss is
the modular quotient syndrome inside `M_s`, together with any attempt to make
the repair iteration stable after arbitrary block rematchings.

The finite exact checks are in
[`scripts/verify_prime_power_higher_rank_prefix.py`](../scripts/verify_prime_power_higher_rank_prefix.py).
