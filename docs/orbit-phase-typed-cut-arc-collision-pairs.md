# Orbit-phase typed cut-arc collision pairs

This note refines the typed shared-source cut-pressure theorem. It converts every named positive-pressure arc into explicit residual/edit path pairs that both require that exact unit-sensitive source capacity.

## Contract

Let `C=A disjoint_union B` be the canonical split of a non-singleton irreducible typed residual/edit core. Choose deterministic integral full flows for the two proper subsets, cancel directed cycles lexicographically, and decompose the remaining flows into ordered unit source-to-demand paths. Every path retains residual-or-edit type, unit class, valuation, holonomy and complete source addresses.

For a forward arc `e` of the canonical shared-source cut with capacity `c_e`, put

`p_e=f_A(e)+f_B(e)-c_e>0`.

## OP4ej--OP4en

1. The cycle-cancelled side flows have canonical unit-path decompositions, with exactly `f_A(e)` and `f_B(e)` typed paths through `e`.
2. Since each side separately respects capacity, `p_e<=min(f_A(e),f_B(e))`. Oppositely ordered allocation to the `c_e` unit slots gives exactly `p_e` doubly occupied slots.
3. Every such slot is an ordered pair of exact typed demand paths sharing the named unit-sensitive source arc. The least slot gives a canonical collision witness retaining both complete path addresses.
4. If the colliding paths use `a_e` typed terminal classes on side `A` and `b_e` classes on side `B`, one ordered typed class pair occurs at least `ceil(p_e/(a_e b_e))` times. Residual/edit type and unit class remain explicit.
5. An arithmetic or holonomy argument excluding every retained cross-side pair, or bounding all typed class-pair collision multiplicities below the required total, excludes the core. Singleton typed cores remain direct shortages. Omitted unit fields or path arcs, merged sources, uncancelled circulation, changed quotient state or independent capacity reuse is a reset.

## Consequence

The remaining OP obstruction is one direct residual/edit shortage or one exact pair of separately payable typed paths colliding on a named unit-sensitive source capacity.

## Scope

This is conditional on the complete fixed typed network and deterministic integral flows. It does not construct the physical source graph and does not prove OP5 or the no-three-in-line conjecture.