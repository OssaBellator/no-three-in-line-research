# Composite historical-cycle reset and the transitive split core

PX315--PX329 analyze resets using one or two historical levels and reduce the
remaining antichain child to a bounded base-tournament core.  A principal reset
does not require all released arcs to lie in one or two layers.  It only
requires a directed cycle in the union of the releasable historical arcs.

This gives a sharper final reduction.  Either a historical cycle resets the
child, using at most one ancestor level per cycle edge, or the historical union
is acyclic.  A topological endpoint of an acyclic historical union forces an
entire half-tournament of base positions and reduces the child order to
`Delta_0+1`.

## 1. Historical union cycles are composite resets

Let

\[
\mathcal H
=
\bigcup_{j=1}^d \widehat H_j[Q]
\]

be the directed union of all releasable historical cells inside the antichain
child `Q`.

### Theorem PX330 -- PROVED

If `mathcal H` contains a directed cycle of length `ell`, then releasing at
most `ell` ancestor levels gives an executable principal cyclic rematching on
the vertices of that cycle.

### Proof

Every arc of the cycle belongs to one unique releasable historical layer.
Release all distinct layers represented on the cycle.  None of its arcs belongs
to `F_0`, and historical edge-disjointness prevents any unreleased historical
layer from still forbidding it.  All cycle arcs therefore become allowed and
give the principal cyclic permutation.  The number of released levels is at
most the number of cycle edges. \(\square\)

PX311 and PX315 are the one- and two-level special cases.

## 2. Acyclic historical union forces order `Delta_0+1`

### Theorem PX331 -- PROVED

If no composite historical-cycle reset exists, then

\[
\boxed{s\le\Delta_0+1.}
\]

### Proof

By PX330, the historical union `mathcal H` is acyclic.  Choose a topological
order

\[
v_1,\ldots,v_s
\]

in which every historical arc points forward.

For the last label `v_s`, every backward cell

\[
v_s\to v_i,\qquad i<s,
\]

is forbidden inside the antichain but cannot be historical, because it points
backward in the topological order.  Hence all `s-1` such cells belong to
`F_0`.  The base row-degree bound gives

\[
s-1\le\Delta_0.
\]

\(\square\)

The symmetric argument at `v_1` uses the base column-degree bound.

Thus allowing a bounded composite release improves the two-history residual
bound from `2Delta_0+1` to `Delta_0+1`.

## 3. Sharp acyclic template

### Theorem PX332 -- PROVED

Assume `s=Delta_0+1` and the historical union is acyclic.  In every topological
order `v_1,...,v_s`:

1. all backward arcs `v_j->v_i` with `j>i` are base-forbidden;
2. the last row and first column have base degree exactly `Delta_0`.

If the base obstruction is edge-minimal subject to the absence of a historical
cycle, then the base graph is exactly the backward transitive tournament and
the historical union is exactly the forward transitive tournament.

### Proof

The first statement is the proof of PX331 applied to every backward pair.
At equality, row `v_s` and column `v_1` contain exactly `s-1=Delta_0` forced
base cells.

For an edge-minimal obstruction, no forward arc may also be base-forbidden:
deleting such an extra base cell leaves every backward pair base-covered and
does not create a historical cycle.  Hence every forward arc is historical,
while every backward arc is base. \(\square\)

Call this equality case the **transitive split core**.

## 4. Final trajectory terminal bound

### Corollary PX333 -- PROVED

For fixed base degree `Delta_0`, every trajectory antichain child has one of
the following outcomes.

1. a principal reset obtained by releasing at most `s<=2Delta_0+1` historical
   levels;
2. an acyclic residual child of order

   \[
   \boxed{s\le\Delta_0+1.}
   \]

The second outcome has at most

\[
\boxed{(\Delta_0+1)!}
\]

principal permutation states and is handled exactly by PX273/PX290.

For `Delta_0=2`, a genuinely no-reset trajectory child has order at most three;
the sharp edge-minimal template is the three-label transitive split core.

### Proof

If the historical union contains a cycle, apply PX330 and use PX316 for the
pre-existing order bound.  Otherwise apply PX331 and the exact terminal
enumerator.  PX332 gives the equality template. \(\square\)

The remaining trajectory frontier is therefore not a path-forest family of
logarithmic-logarithmic order.  It is the exact absorption or contradiction of
a fixed base-sized transitive split core.

## 5. Verification

Run

```bash
python scripts/verify_product_composite_history_reset.py
```

The verifier exhausts base/historical arc patterns through order five, checks
cycle-release correctness, verifies `s<=Delta_0+1` in every acyclic historical
union, and confirms the sharp transitive split template.
