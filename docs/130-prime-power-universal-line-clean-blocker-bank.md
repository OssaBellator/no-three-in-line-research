# Universal line-clean banks for sharp blocker families

The line-clean construction first used for a mixed-ratio fan needs only one
geometric feature: the paid lines have distinct available cells on one fixed
matching vertex. It therefore applies to singleton fans and to the canonical
width-two and width-three Hall families as well.

Work in a target-specific parent board of size `t`. Let

\[
z_*=(x_*,y_*)
\]

be the designated old endpoint. Let `\mathcal L` be a family of distinct
nonaxis candidate-only certificate lines. Assume every `L\in\mathcal L`
contains a distinguished available cell

\[
f_L=(x_*,a_L),
\]

where the rows `a_L` are pairwise distinct and `a_L\ne y_*`. Choose one other
available cell `g_L` on `L`, compatible with `f_L`, and put

\[
P_L=\{f_L,g_L\}.
\]

The target-side form is obtained by interchanging the two matching classes.

## 1. Universal fan-line criterion

### Theorem CMR360 — PROVED

For every `L`, extend the remaining available cells of `L` to a perfect
matching of the residual `(t-2)\times(t-2)` board and complete `P_L` by a
derangement of that matching. Then:

1. every completion omits `z_*`;
2. every completion contains `P_L` and no other cell of `L`;
3. no completion contains a candidate-only triple using both cells of `P_L`;
4. the cylinder for one line has exactly `D_{t-2}` states;
5. cylinders belonging to distinct lines are disjoint.

Consequently the universal line-clean bank has exact size

\[
\boxed{|\mathcal L|D_{t-2}}.
\]

### Proof

Containing `f_L` uses source `x_*` at a row different from `y_*`, so `z_*` is
omitted. After deleting the two sources and two rows used by `P_L`, the
remaining available cells of `L` form a partial matching. Extend it to a
perfect matching `F_L`. Relabel `F_L` as the identity; the completions avoiding
it are exactly the `D_{t-2}` derangements. They avoid every residual cell of
`L`, so the paid pair cannot be completed to a triple on `L`.

Distinct paid pairs prescribe distinct cells in the common source column
`x_*`, hence no perfect matching belongs to two cylinders. ∎

## 2. Sharp-blocker instances

### Corollary CMR361 — PROVED

Each of the following sharp blocker classes supplies a CMR360 bank.

1. A singleton fan supplies `m=t-1` paid lines.
2. A width-two Hall blocker supplies at least `m=t-2` endpoint-disjoint full
   chords by CMR284.
3. A width-three Hall blocker with `t\ge10` supplies at least `m=t-9`
   cell-disjoint full triples by CMR285.
4. For widths `4\le n\le6`, the CMR275 full transversals supply
   \[
   m\ge t-2-n(n-2)
   \]
   paid lines whenever this bound is positive.

### Proof

In each class, choose one small-side Hall slice. The canonical lines meet that
slice in pairwise distinct available cells. Choose one further compatible cell
on each line and apply CMR360. ∎

This includes mixed source/target configurations once one sharp fan side is
fixed. The ratio extraction remains useful for algebraic signatures, but is
not required merely to construct the paid bank.

## 3. Universal high-slice reserve

### Corollary CMR362 — PROVED

Fix one paid line from a CMR361 bank. For every odd `t\ge2847`, there is a
completion which

1. omits `z_*`;
2. contains the paid pair and no other cell of its line;
3. avoids every candidate-only triple of primitive height at least
   \[
   \left\lceil\frac{21t}{50}\right\rceil;
   \]
4. simultaneously avoids all available cells on any prescribed family of at
   most
   \[
   R_4(t)=\left\lfloor\frac{t}{1000}\right\rfloor
   \]
   additional nonaxis lines.

### Proof

CMR337–CMR338 use only the paid-pair geometry and the residual forbidden
matching containing the other cells of its line. CMR360 supplies precisely
those hypotheses. ∎

## 4. Quadratic line-signature amplification

Assume the current saturated state is a globally minimal positive-potential
state. Suppose none of the line-clean banks improves and none creates an
anchored certificate. For every paid line `L`, iterate CMR362 and choose

\[
r=R_4(t)+1
\]

distinct low-height replacement-line signatures; call the set `\mathcal N_L`.

### Theorem CMR363 — PROVED

Let

\[
I=mr,
\qquad
K=\left\lceil\sqrt I\right\rceil.
\]

At least one of the following holds.

1. The union of the replacement sets contains at least `K` distinct low-height
   line signatures.
2. One low-height real line belongs to at least `K` sets `\mathcal N_L`.

For a singleton, width-two, or width-three bank with `t\ge2847`, one may take

\[
\boxed{K\ge\left\lceil\frac{t}{32}\right\rceil}.
\]

### Proof

There are at least `I` incidences `(L,M)` with `M\in\mathcal N_L`. If the
union has at most `K-1` lines, one line has incidence degree at least `K`
because `I>(K-1)^2`.

For the stated blocker classes, `m\ge t-9` and

\[
r=\left\lfloor\frac{t}{1000}\right\rfloor+1\ge\frac{t}{1000}.
\]

For `t\ge2847`,

\[
(t-9)\frac{t}{1000}\ge\frac{t^2}{32^2}.
\]

Taking square roots proves the explicit bound. ∎

Thus every frozen sharp blocker has an amplified low-height output: either
line-signature dispersion is linear in the parent size, or one replacement
line is recycled across linearly many paid cylinders.

No all-`n` theorem is claimed here. Exact cylinder sizes, blocker populations,
and the incidence amplification are checked in
[`scripts/verify_prime_power_universal_line_clean.py`](../scripts/verify_prime_power_universal_line_clean.py).
