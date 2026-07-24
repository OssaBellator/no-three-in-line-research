# The local-arc obstruction in saturated CRT assembly

CMCRT4--CMCRT5 give a valid direction-separation criterion under the hypothesis
that each local projection contains no modular triple of distinct points. For
saturated prime-field factors, that premise is impossible. This chapter records
the obstruction and the corrected projection taxonomy.

## 1. A saturated prime-field pair cannot be a modular arc

### Theorem CMCRT6 — PROVED

Let `p>=3` be prime. A union of two pointwise-disjoint permutation graphs in
`F_p^2` contains three distinct collinear points. In particular, no saturated
`2p`-point local pair can satisfy the modular-arc hypothesis of CMCRT4.

### Proof

More generally, let `S` be a set in `F_p^2` with no three collinear and fix a
point `P` in `S`. Every other point of `S` must determine a different direction
through `P`; two points in the same direction would be collinear with `P`.
There are only `p+1` affine directions. Hence

\[
|S|-1\le p+1,
\qquad
|S|\le p+2.
\]

A pointwise-disjoint pair of permutation graphs has `2p` distinct points. For
`p>=3`,

\[
2p>p+2,
\]

so such a pair necessarily has a modular triple. ∎

The argument is deliberately elementary. Stronger finite-geometry arc bounds
are unnecessary for the obstruction.

## 2. The four local projection patterns

Consider a real collinear triple in a synchronized CRT lift for coprime factors
`u,v`. Its determinant vanishes modulo both factors. In either local projection,
one of two events occurs:

1. **collision:** at least two projected points coincide;
2. **local line:** all three projected points are distinct and collinear.

### Proposition CMCRT7 — PROVED

Every global real triple has one of the following factor-pattern types:

- collision / collision;
- collision / local line;
- local line / collision;
- local line / local line.

In the collision/collision case, the collision edge cannot be the same in both
factors unless two global points are equal. Therefore distinct collision edges
share one vertex, and CMCRT3 gives the mixed-direction factorization

\[
\Delta=N\det(A,B).
\]

### Proof

Reduction of the real determinant modulo each factor gives local modular
collinearity. If a local projection does not contain a repeated point, it is a
local line of three distinct points. This gives the four cases.

If one pair coincides in both factors, CRT makes that pair equal globally.
Thus a triple of distinct global points cannot use the same collision edge in
both factors. Two different edges of a three-vertex set share a vertex, giving
the CMCRT3 normalization. ∎

## 3. Corrected CRT target

CMCRT5 remains a useful theorem for local sets that genuinely are modular arcs,
but CMCRT6 shows that it cannot directly assemble saturated odd-prime local
pairs. A viable saturated CRT theorem must attach signatures to the unavoidable
local-line cases as well as to collision vectors.

The corrected construction target is therefore:

1. label every local modular triple by its primitive line direction and carry;
2. label every local collision by its scaled collision direction;
3. prove that no compatible pair of labels from the two factors can cancel to
   exact global determinant zero, or install an absorber for the compatible
   label classes.

This replaces the impossible requirement "eliminate all local triples" by the
quantitative requirement "separate or absorb all local triple signatures."
