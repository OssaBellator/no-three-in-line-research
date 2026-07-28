# Sparse typed cut-arc collision pairs

This note refines the typed neutral-source/move cut-pressure theorem. It converts every named positive-pressure arc into explicit pair/completion path pairs that both require that exact boundary-neutral capacity.

## Contract

Let `C=A disjoint_union B` be the canonical split of a non-singleton irreducible typed pair/completion core. Choose deterministic integral full flows for the two proper subsets, cancel directed cycles lexicographically, and decompose the remaining flows into ordered unit neutral-source-to-demand paths. Every path retains pair-or-completion type, sign, boundary profile and complete neutral-source/move addresses.

For a forward arc `e` of the canonical neutral cut with capacity `c_e`, put

`p_e=f_A(e)+f_B(e)-c_e>0`.

## SAS5lj--SAS5ln

1. The cycle-cancelled side flows have canonical unit-path decompositions, with exactly `f_A(e)` and `f_B(e)` typed paths through `e`.
2. Since each side separately respects capacity, `p_e<=min(f_A(e),f_B(e))`. Oppositely ordered allocation to the `c_e` unit slots gives exactly `p_e` doubly occupied slots.
3. Every such slot is an ordered pair of exact typed demand paths sharing the named neutral-source or move arc. The least slot gives a canonical collision witness retaining both complete boundary-neutral path addresses.
4. If the colliding paths use `a_e` typed terminal classes on side `A` and `b_e` classes on side `B`, one ordered typed class pair occurs at least `ceil(p_e/(a_e b_e))` times. Pair/completion type and sign data remain explicit.
5. A shareability or boundary argument excluding every retained cross-side pair, or bounding all typed class-pair collision multiplicities below the required total, excludes the core. Singleton typed cores remain direct shortages. Omitted legality fields or paths, merged moves, uncancelled circulation, changed boundary state or independent neutral-capacity reuse is a reset.

## Consequence

The remaining SAS obstruction is one direct pair/completion shortage or one exact pair of separately payable typed paths colliding on a named neutral-source/move capacity.

## Scope

This is conditional on the complete fixed typed network and deterministic integral flows. It does not construct the physical neutral-source graph and does not prove SAS6 or the no-three-in-line conjecture.