# Universal line-clean banks for sharp blocker families

CMR330 was stated for the common-ratio family extracted from a mixed fan, but
its proof uses only one geometric feature: the paid lines have distinct cells
on one fixed matching vertex.  The same construction therefore applies to
sharp singleton fans and to the canonical width-two and width-three Hall
families.  This chapter records that universal form and the resulting
low-height amplification.

Work in a target-specific parent board of size `t`.  Let

\[
z_*=(x_*,y_*)
\]

be the designated old endpoint to be omitted.  The source-side formulation
below has a coordinate-dual target-side version.

Let `\mathcal L` be a family of distinct nonaxis candidate-only certificate
lines.  Assume that every `L in \mathcal L` contains a distinguished available
cell

\[
f_L=(x_*,a_L),
\]

where the rows `a_L` are pairwise distinct and `a_L ne y_*`.  Choose one other
available cell `g_L` on `L` which is compatible with `f_L`, and put

\[
P_L=\{f_L,g_L\}.
\]

## 1. Universal fan-line criterion

### Theorem CMR347 — PROVED

For every `L`, fix a residual perfect matching containing all remaining
available cells of `L`, and complete `P_L` by a derangement of that matching as
in CMR330.  Then:

1. every completion omits `z_*`;
2. every completion contains `P_L` and no other cell of `L`;
3. every completion contains no candidate-only triple using both cells of
   `P_L`;
4. the cylinder for one line has exactly
   \[
   D_{t-2}
   \]
   states;
5. the cylinders for distinct lines are disjoint.

Consequently the universal line-clean bank has exact size

\[
\boxed{
|\mathcal L|D_{t-2}.
}
\]

### Proof

Containing `f_L` uses the source vertex `x_*` at a row different from `y_*`, so
`z_*` is omitted.  After deleting the two source and two target vertices used
by `P_L`, the remaining available cells of `L` form a partial matching.  Extend
it to a perfect matching and avoid that matching.  Relabelling it as the
identity gives exactly `D_{t-2}` derangements and removes every residual cell
of `L`.  Thus no third cell can complete the paid pair on `L`.

For distinct lines, the paid pairs contain different cells in the common
source column `x_*`.  One perfect matching cannot contain two such cells, so
the cylinders are disjoint.  This is exactly the proof of CMR330--CMR331, with
no ratio hypothesis. ∎

The target-side version fixes one common target row and interchanges the two
matching classes.

## 2. Sharp blocker instances

### Corollary CMR348 — PROVED

Every sharp target-specific blocker in the following classes supplies a
universal line-clean bank.

1. **Singleton fan.**  The sharp fan has
   \[
   \boxed{m=t-1}
   \]
   paid lines.
2. **Width two.**  CMR284 supplies at least
   \[
   \boxed{m=t-2}
   \]
   endpoint-disjoint full chords.  Either small Hall slice may be used as the
   common paid slice.
3. **Width three.**  For `t>=10`, CMR285 supplies at least
   \[
   \boxed{m=t-9}
   \]
   cell-disjoint full triples.  Any one of the three small Hall slices may be
   used as the common paid slice.
4. **Widths four through six.**  Whenever the CMR275 lower bound is positive,
   the full Hall transversals give the corresponding bank of size
   \[
   m\ge t-2-n(n-2).
   \]

### Proof

In every case the canonical lines have distinct available cells on each fixed
small-side Hall slice.  Choose one such slice and one further cell on each
certificate line, then apply CMR347. ∎

This includes mixed source/target singleton configurations once one of their
sharp fan sides is fixed.  The mixed-ratio extraction remains useful for its
additional algebraic signatures, but is not needed merely to construct the
paid bank.

## 3. Universal high-slice reserve

### Corollary CMR349 — PROVED

Fix any one paid line from a CMR348 bank.  For every odd

\[
t\ge2847,
\]

there is a completion which

1. omits the old target endpoint;
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

CMR337--CMR338 use only the paid-pair geometry and the residual forbidden
matching containing the remaining cells of its line.  CMR347 supplies exactly
those hypotheses. ∎

## 4. Quadratic line-signature amplification

Assume the current saturated state is a globally minimal positive-potential
state.  Suppose none of the line-clean banks under consideration improves and
none creates an anchored certificate.  For every paid line `L`, iterate CMR349
and choose a set `\mathcal N_L` of

\[
r=R_4(t)+1
\]

distinct low-height replacement-line signatures.  Every member has primitive
height below `ceil(21t/50)`.

### Theorem CMR350 — PROVED

Let

\[
I=m r,
\qquad
K=\left\lceil\sqrt I\right\rceil.
\]

At least one of the following holds.

1. The union of all replacement sets contains at least `K` distinct low-height
   line signatures.
2. One low-height real line belongs to at least `K` of the sets
   `\mathcal N_L`.

For a width-two or width-three bank with `t>=2847`, one may take

\[
\boxed{K\ge\left\lceil\frac{t}{32}\right\rceil.}
\]

The same bound holds for a singleton fan.

### Proof

There are at least `I` incidences `(L,M)` with `M in \mathcal N_L`.  If the
union contains fewer than `K` lines, it has at most `K-1` members.  Because

\[
I>(K-1)^2,
\]

one of those lines has incidence degree at least `K`.

For the three stated blocker classes, `m>=t-9` and

\[
r=\left\lfloor\frac{t}{1000}\right\rfloor+1\ge\frac{t}{1000}.
\]

For `t>=2847`,

\[
(t-9)\frac{t}{1000}\ge\frac{t^2}{32^2}.
\]

Taking square roots proves the explicit bound. ∎

Thus every frozen sharp blocker has a genuinely amplified low-height output:
either line-signature dispersion is linear in the parent size, or one
replacement line is recycled across linearly many different paid cylinders.
The latter is a concrete secant/carry concentration object, not an anonymous
failure of local descent.

No all-`n` theorem is claimed here.  The exact cylinder sizes, sharp-blocker
populations, and incidence amplification are checked in
[`scripts/verify_prime_power_universal_line_clean.py`](../scripts/verify_prime_power_universal_line_clean.py).
