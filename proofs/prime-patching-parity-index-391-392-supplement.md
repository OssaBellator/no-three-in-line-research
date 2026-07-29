# Prime-patching parity index supplement: `docs/391--392`

This supplement extends `proofs/prime-patching-parity-index.md` without replacing
its cumulative history.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bvj--PP3bvl | Joining two feasible boundary-constraint components has exact merge penalty zero for aligned majorities and `min(|I_R|,|I_S|)` for opposing majorities; forest recleaning cost telescopes as the sum of these penalties | PROVED | `docs/391-exact-component-merge-calculus-for-boundary-recleaning.md` |
| PP3bvm--PP3bvo | The thirteen violating `m=10` transition count maxima have an exact source-mass/capacity-deficit profile; nine microscopic witnesses have mean source mass 64 or 128, and their failure is exactly `Delta/V=A_s-1` | PROVED / VERIFIED FINITELY | `docs/392-exact-m10-hall-transition-count-maximizer-source-mass.md` |

## Frontier update

For component-local recleaning, the exact minimum cost can now be built edge by
edge. A feasible constraint joining two current components costs nothing when it
aligns their weighted majority phases, and otherwise costs exactly the smaller
absolute imbalance. The structural covering-rotation target is therefore to find
successors whose boundary forest has few majority-opposing merges, preferably
only against low-imbalance components.

For the `m=10` Hall transition count maxima, source-mass scale is narrow: every
maximizing subset has mean source mass in `[64,128]`, while subset size ranges
from one to 124. Among the nine microscopic witnesses with at most six sources,
eight have mean mass 128 and one has mean mass 64. The strongest microscopic
relative capacity deficit is `421/1563` at source count 248; the strongest overall
is `12769/38383` at source count 278. This reinforces capacity reuse and overlap
congestion, rather than source-mass scale, as the key obstruction.

The next available theorem identifier is `PP3bvp`.
