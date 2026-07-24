# The local-arc obstruction in saturated CRT assembly

CMCRT4--CMCRT5 are valid under a local modular-arc hypothesis, but saturated
prime-field factors cannot satisfy that premise.

## 1. Saturated prime pairs are not modular arcs

### Theorem CMCRT6 — PROVED

Let `p>=3` be prime. A union of two pointwise-disjoint permutation graphs in
`F_p^2` contains three distinct collinear points.

### Proof

Fix one selected point `P`. If no three selected points are collinear, every one
of the `p+1` affine directions through `P` contains at most one further selected
point. Thus any modular arc has size at most `p+2`. A disjoint permutation pair
has `2p>p+2` points. ∎

## 2. Projection taxonomy

### Proposition CMCRT7 — PROVED

Every real triple in a synchronized two-factor CRT lift has one of four local
projection patterns:

- collision / collision;
- collision / distinct-point local line;
- distinct-point local line / collision;
- distinct-point local line / distinct-point local line.

In the collision/collision case, the collision edge cannot be the same in both
factors unless two global points coincide. Distinct collision edges share a
vertex, and CMCRT3 gives the mixed-direction factorization.

### Proof

The real determinant vanishes modulo each factor. In one factor, either two
projected points coincide or all three are distinct and collinear. This gives
the four cases. A pair coinciding in both coprime factors is equal globally by
CRT. ∎

Thus direct saturated CRT assembly must retain local-line directions and their
integer carries rather than demand that local triples disappear. CMCRT8--9 in
[`docs/52-crt-slope-carry-signatures.md`](52-crt-slope-carry-signatures.md)
provide that refined signature.
