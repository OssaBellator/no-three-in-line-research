# Two-history reset for trajectory antichain children

PX294--PX314 reduce a genuinely trajectory-saturated terminal core to an
antichain child `Q`.  Inside `Q` no off-diagonal cell is currently allowed.
Every such cell is supplied either by the bounded base graph `F_0` or by one
unique releasable historical layer.

The path-forest depth bound of PX313 is useful, but it does not exploit the
simplest composite reset: opposite orientations of one unordered label pair
form a principal transposition.  If both orientations are historical, releasing
the one or two layers which contain them exposes that transposition.

This leaves only a base-sized antichain core.

## 1. Opposite historical arcs give a reset

Let `Q` have order `s`.  For distinct `u,v in Q`, call the unordered pair
`{u,v}` **doubly historical** when neither directed cell

\[
u\to v,\qquad v\to u
\]

belongs to `F_0`.  Since `Q` is an allowed antichain, both cells then belong to
unique historical layers.

### Theorem PX315 -- PROVED

If `{u,v}` is doubly historical, then releasing at most two ancestor layers
gives the principal transposition

\[
\boxed{u\leftrightarrow v.}
\]

If the two opposite arcs lie in one historical layer, that layer already
contains a directed two-cycle and PX311 gives a one-level reset.  Otherwise
releasing their two distinct layers gives a two-level reset.

### Proof

Historical edges are edge-disjoint after deleting their overlap with `F_0`.
Release every historical layer containing one of the two directed cells.
Neither cell is base-forbidden, so both become allowed.  They form the
fixed-point-free permutation of the principal set `{u,v}`. \(\square\)

## 2. No two-history reset forces a base orientation cover

### Theorem PX316 -- PROVED

If `Q` has no reset using at most two historical layers, then for every
unordered pair `{u,v}` at least one of `u->v` and `v->u` belongs to `F_0`.
Consequently

\[
\boxed{
\binom{s}{2}
\le
|F_0\cap(Q\times Q)|
\le
s\Delta_0
}
\]

and therefore

\[
\boxed{s\le2\Delta_0+1.}
\]

### Proof

If an unordered pair had neither orientation in `F_0`, PX315 would give a
reset.  Thus choosing one base orientation from every unordered pair gives at
least `binom(s,2)` distinct base cells.  The maximum row degree of `F_0` is at
most `Delta_0`, so it contributes at most `s Delta_0` cells inside
`Q times Q`.  Cancel `s/2` from

\[
s(s-1)/2\le s\Delta_0.
\]

\(\square\)

### Corollary PX317 -- PROVED

In the base-free case `Delta_0=0`, every nontrivial trajectory antichain child
has a reset using at most two historical layers.

### Proof

A nontrivial child has `s>=2`, contradicting PX316 unless a two-history reset
exists. \(\square\)

## 3. Constant-order residual terminal core

### Corollary PX318 -- PROVED

For fixed base degree `Delta_0`, every trajectory antichain child has one of
the following outcomes.

1. a one-history reset by PX294 or PX311;
2. a two-history principal transposition reset by PX315;
3. residual order

   \[
   \boxed{s\le2\Delta_0+1.}
   \]

The third outcome can be passed to the exact terminal optimizers PX273 and
PX290.  Its permutation state space is at most

\[
\boxed{(2\Delta_0+1)!}
\]

and is independent of the ambient side length `N`.

### Proof

Apply PX316.  Exact enumeration is PX273/PX290 with the displayed order
bound. \(\square\)

Thus long path-forest decompositions are not a large terminal obstruction.
Unless the bounded base graph orients at least one direction of every pair,
two ancestor levels already reset a principal pair.

## 4. Verification

Run

```bash
python scripts/verify_product_two_history_antichain_reset.py
```

The verifier exhausts all base/historical orientation patterns through order
five, checks the one/two-level transposition reset, and verifies the sharp
bound `s<=2Delta_0+1` in every no-reset pattern.
