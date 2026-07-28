# Rational-inverse typed cut-arc collision pairs

This note refines the typed physical/collateral cut-pressure theorem. It converts every named positive-pressure arc into explicit owner/charge path pairs that both require that exact collateral capacity.

## Contract

Let `C=A disjoint_union B` be the canonical split of a non-singleton irreducible typed owner/charge core. Choose deterministic integral full flows for the two proper subsets, cancel directed cycles lexicographically, and decompose the remaining flows into ordered unit physical-source-to-demand paths. Every path retains its owner-or-charge type, terminal profile, host, context, coherence and all physical-source/collateral arc addresses.

For a forward arc `e` of the canonical minimum cut with capacity `c_e`, put

`p_e=f_A(e)+f_B(e)-c_e>0`.

## RI5fd--RI5fh

1. The cycle-cancelled side flows have canonical unit-path decompositions, with exactly `f_A(e)` and `f_B(e)` typed paths through `e`.
2. Since each side separately respects `c_e`, `p_e<=min(f_A(e),f_B(e))`. Oppositely ordered use of the `c_e` unit slots gives exactly `p_e` doubly occupied slots.
3. Every such slot is an ordered pair of exact typed demand paths sharing the named physical-source or collateral arc; the least slot is canonical and retains both complete arithmetic addresses.
4. If the colliding paths use `a_e` typed terminal classes on side `A` and `b_e` classes on side `B`, one ordered typed class pair occurs at least `ceil(p_e/(a_e b_e))` times. Owner/charge type is never suppressed.
5. An arithmetic argument excluding every retained cross-side typed pair, or bounding all typed class-pair multiplicities below the required total, excludes the core. Singleton typed cores remain direct shortages. Omitted type fields or path arcs, merged collateral, uncancelled circulation, changed arithmetic state or independent capacity reuse is a reset.

## Consequence

The remaining RI obstruction is one direct owner/charge shortage or one exact pair of separately payable typed paths colliding on a named physical-source/collateral capacity.

## Scope

This is conditional on the complete fixed typed network and deterministic integral flows. It does not construct the arithmetic compatibility graph and does not prove RI6 or the no-three-in-line conjecture.