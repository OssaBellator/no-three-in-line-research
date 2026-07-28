# Bounded-denominator cut-arc collision pairs

This note refines the canonical primitive-potential cut-pressure theorem on the same complete physical/source/restoration network. It turns a named positive-pressure arc into explicit pairs of separately payable restoration units that both require that exact arithmetic capacity.

## Contract

Let `C=A disjoint_union B` be the canonical split of a non-singleton irreducible restoration core. Choose deterministic integral full flows for the two proper subsets, cancel directed cycles lexicographically, and decompose the remaining flows into ordered unit source-to-restoration paths. Every path retains its restoration address, primitive weight, gain fields and every physical/source-potential compatibility arc.

For a forward arc `e` of the canonical arithmetic minimum cut with capacity `c_e`, put

`p_e=f_A(e)+f_B(e)-c_e>0`.

## BDA5fm--BDA5fq

1. The cycle-cancelled side flows have canonical unit-path decompositions, with exactly `f_A(e)` and `f_B(e)` paths through `e`.
2. Because each side separately respects capacity, `p_e<=min(f_A(e),f_B(e))`. Oppositely ordered allocation to the `c_e` unit capacity slots gives exactly `p_e` doubly occupied slots.
3. Every doubly occupied slot is an ordered pair of exact restoration paths sharing the named physical- or source-potential arc. The least slot is a canonical arithmetic collision witness.
4. If the colliding paths use `a_e` restoration classes on side `A` and `b_e` classes on side `B`, one ordered class pair occurs at least `ceil(p_e/(a_e b_e))` times.
5. An arithmetic estimate excluding every such cross-side pair, or bounding all retained class-pair collision multiplicities below the required total, excludes the core. Singleton cores remain direct shortages. Omitted gains or paths, merged potential sources, uncancelled circulation, changed denominator state or independent capacity reuse is a reset.

## Consequence

The remaining BDA obstruction is one direct restoration shortage or one exact pair of separately payable primitive-potential paths colliding on a named physical/source arc.

## Scope

This is conditional on the complete fixed arithmetic network and deterministic integral flows. It does not construct the physical weights or prove BDA6 or the no-three-in-line conjecture.