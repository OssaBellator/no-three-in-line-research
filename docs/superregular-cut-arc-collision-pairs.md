# Superregular cut-arc collision pairs

This note refines the canonical physical-source/witness-atom cut-pressure theorem at one fixed conditioned threshold. It converts every named positive-pressure arc into explicit pairs of separately payable burden units that both require that exact capacity.

## Contract

Let `C=A disjoint_union B` be the canonical split of a non-singleton irreducible burden core. Choose deterministic integral full flows for the two proper subsets, cancel directed cycles lexicographically, and decompose the remaining flows into ordered unit physical-source-to-burden paths. Every path retains its candidate, conditioned threshold, witness atom and all physical-source/atom arc addresses.

For a forward arc `e` of the canonical minimum cut with capacity `c_e`, put

`p_e=f_A(e)+f_B(e)-c_e>0`.

## SRR2dt--SRR2dx

1. The cycle-cancelled side flows have canonical unit-path decompositions, with exactly `f_A(e)` and `f_B(e)` burden paths through `e`.
2. Since each side separately respects capacity, `p_e<=min(f_A(e),f_B(e))`. Oppositely ordered allocation to the `c_e` unit slots gives exactly `p_e` doubly occupied slots.
3. Every such slot is an ordered pair of exact burden paths sharing the named physical-source or witness-atom arc. The least slot gives a canonical collision witness retaining both complete candidate/witness addresses.
4. If the colliding paths use `a_e` burden classes on side `A` and `b_e` classes on side `B`, one ordered class pair occurs at least `ceil(p_e/(a_e b_e))` times.
5. A geometric incidence argument excluding every retained cross-side pair, or bounding all class-pair collision multiplicities below the required total, excludes the core. Singleton burden cores remain direct shortages. Omitted witnesses or paths, merged atom capacity, uncancelled circulation, changed threshold/conditioning or independent capacity reuse is a reset.

## Consequence

The remaining SRR obstruction is one direct burden shortage or one exact pair of separately payable candidate paths colliding on a named physical-source/witness-atom capacity.

## Scope

This is conditional on the complete fixed conditioned network and deterministic integral flows. It does not construct the geometric tensor reference and does not prove SRR2, SRR4 or the no-three-in-line conjecture.