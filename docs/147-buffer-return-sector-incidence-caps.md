# Incidence caps for buffer-return sectors

PX356--PX363 turn every nonimproving terminal bank into a weighted one-point
child or a large same-type endpoint block.  The return theorem is purely
combinatorial.  The exact buffer geometries impose additional incidence caps
on two of the four PX354 sectors.

A shared-core directed-path blocker is an incidence between one of `n`
distinct candidate secant lines and a fixed selected point.  Szemeredi--Trotter
therefore limits the whole family to `O(n^(4/3))`.  A mixed cross-buffer
blocker has one cell depending on `a`, one depending on `b`, and one fixed
selected anchor.  For each fixed anchor, line uniqueness makes the relation
between `a` and `b` a partial matching, so the whole family has size at most
`2n^2`.

These caps show that directed-path return cannot carry large designated weight,
and a mixed cross-buffer sector cannot repeat after its first linear-weight
one-point return.

## 1. Distinct directed-path lines

Fix distinct core labels `u,v`.  For every admissible first-buffer label `a`,
put

\[
P_a=(x_u,y_a),
\qquad
Q_a=(x_a,y_v),
\]

and let `L_a` be the real line through `P_a,Q_a`.

### Theorem PX364 -- PROVED

The lines `L_a` are pairwise distinct.

### Proof

Every `L_a` meets the fixed row `x=x_u` at `P_a`.  For distinct labels
`a,a'`, the columns `y_a,y_(a')` are distinct, so `P_a` and `P_(a')` are
distinct points of that row.  A nonhorizontal line has only one intersection
with the row.  The line `L_a` is nonhorizontal because `x_a!=x_u`.  Hence
`L_a=L_(a')` would force `P_a=P_(a')`, impossible. \(\square\)

Let `Z` be the fixed selected background.  Saturation gives `|Z|<=2n`.
A directed-path blocker is exactly a pair `(a,z)` with `z in Z cap L_a`.

### Theorem PX365 -- PROVED USING SZEMEREDI--TROTTER

The number `M_path` of shared-core directed-path blocker certificates satisfies

\[
\boxed{
M_{\rm path}=O(n^{4/3}).
}
\]

The implicit constant is absolute.

### Proof

PX364 gives at most `n` distinct lines, and the fixed selected background has
at most `2n` points.  Apply the standard point--line incidence bound

\[
I(P,L)=O(|P|^{2/3}|L|^{2/3}+|P|+|L|).
\]

With `|P|<=2n` and `|L|<=n`, the result is `O(n^(4/3))`. \(\square\)

This is the same published incidence input already used in PX189, but here it
acts on the much smaller line family of one exact buffer-return type.

### Corollary PX366 -- PROVED REDUCTION

Suppose a terminal bank with designated destruction `D` returns through one
exact directed-path type.  Then

\[
\boxed{D=O(n^{1/3}).}
\]

### Proof

PX357 supplies at least `Dn/48` blockers of the exact type.  PX365 bounds this
by `O(n^(4/3))`.  Divide by `n`. \(\square\)

Thus a weighted one-point child whose designated destruction is
`omega(n^(1/3))` cannot return through the shared-core directed-path sector.

## 2. Mixed cross-buffer fibres are partial matchings

Fix one of the four cross-buffer types in PX353.  Write its two candidate-cell
families as

\[
f_a,
\qquad
g_b.
\]

Each `f_a` varies on one fixed grid row or one fixed grid column, and each
`g_b` varies on another fixed row or column.  The two coordinate lines are
chosen so that no `f_a` lies on the coordinate line containing all `g_b`, and
symmetrically.

For a fixed selected anchor `z`, put an edge `a b` when `f_a,g_b,z` are
collinear.

### Theorem PX367 -- PROVED

For every fixed anchor `z`, the relation

\[
\{(a,b):f_a,g_b,z\text{ are collinear}\}
\]

is a partial matching between the `a`-labels and `b`-labels.  In particular it
has at most `n` edges.

### Proof

Fix `a`.  The line through `f_a` and `z` is not the coordinate line containing
all `g_b`, by the displayed nondegeneracy of the four PX353 cross types.  It
therefore meets that coordinate line in at most one point, determining at most
one `b`.  The same argument with `a,b` reversed gives degree at most one on the
other side. \(\square\)

### Corollary PX368 -- PROVED

The total number `M_mix` of blocker certificates of one exact mixed
cross-buffer type satisfies

\[
\boxed{M_{\rm mix}\le 2n^2.}
\]

If such a type is the weighted two-variable outcome of PX357 for a bank of
designated destruction `D`, then

\[
\boxed{D\le64.}
\]

### Proof

There are at most `2n` fixed selected anchors.  PX367 gives at most `n`
blockers per anchor, proving the first display.

PX357 gives `M_mix>=Dn^2/32`.  Combining with `2n^2` gives `D<=64`.
\(\square\)

### Corollary PX369 -- PROVED REDUCTION

Starting from an original terminal core with `D>=1`, a mixed two-variable
outcome produces by PX361 a one-point child with designated destruction at
least

\[
\frac{Dn}{64}.
\]

For all sufficiently large `n`, that child has destruction greater than `64`.
Consequently its next nonimproving terminal cover cannot return through a
mixed cross-buffer type.

Thus the mixed-shadow return is nonrecurrent: it can occur at most once along
one weighted terminal-return chain.

## 3. Coordinate rank-one degeneracy

Consider a one-variable coordinate family of candidate cells `f_a` lying on a
fixed grid row or fixed grid column.  A rank-one blocker consists of `f_a` and
two fixed selected points `z,z'`.

### Theorem PX370 -- PROVED REDUCTION

For a fixed selected pair `{z,z'}`, exactly one of the following holds.

1. The line `zz'` is the coordinate line containing the whole family.  Then
   every blocker using that pair is suppressed by moving either `z` or `z'`,
   and the pair is a loaded coordinate-line child.
2. The line `zz'` meets the coordinate family in at most one candidate cell.

Consequently every nondegenerate coordinate rank-one blocker family is a
simple graph on fixed selected pairs, while every repeated pair is already a
loaded-line child.

### Proof

Two distinct lines meet in at most one point.  If `zz'` is not the coordinate
line of the family, it therefore contains at most one `f_a`.  If it is that
coordinate line, both selected points lie on the same row or column and moving
either destroys every blocker using the pair. \(\square\)

PX364--PX370 sharpen the return frontier as follows.

- Directed paths are limited to designated weight `O(n^(1/3))`.
- Mixed cross-buffer shadows cannot recur after their first return.
- Repeated coordinate rank-one support is already a loaded-line child.
- The genuinely persistent return sectors are therefore nondegenerate
  coordinate rank one and generic two-variable rank one.

## 4. Verification

Run

```bash
python scripts/verify_product_buffer_return_sector_caps.py
```

The verifier checks distinct directed-path lines on exact integer grids,
verifies every mixed anchor fibre is a partial matching in all four cross
shapes, confirms the `D<=64` consequence, and tests the coordinate-line
degeneracy dichotomy.