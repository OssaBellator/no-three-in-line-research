# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This branch is independent of the other all-`n` strategies. It assumes a saturated no-three-in-line theorem is eventually proved on `(p-1)x(p-1)` grids for all sufficiently large primes `p`, and asks how to extend such a construction to nearby side lengths.

Prime-gap information alone is not sufficient: embedding a `2m`-point solution into an `n x n` grid leaves `2(n-m)` missing points. The essential theorem is an exact extension absorber.

## PP1 — Boundary extension interface

### Target statement

Let `S_m` be a saturated no-three-in-line configuration on `[m]^2`. For `t>=1`, define the enlarged grid `[m+t]^2`. Construct a set of admissible states on the new rows and columns that adds exactly `2t` points while preserving exactly two points in every old and new row and column.

The construction may modify `O(f(t))` old points near a designated reservoir, but must preserve the total point count `2(m+t)`.

## PP2 — Secant-shadow patching lemma

### Target statement

There are functions `w(m)` and `f(t)` such that, whenever `t<=w(m)`, one can choose or prepare a reservoir in `S_m` with the following property:

- delete at most `f(t)` reservoir blocks;
- insert a row-column-preserving completion involving the `t` new rows and `t` new columns;
- create no collinear triple with retained old points;
- internally avoid all triples among new and replacement points.

The desired width should be at least polylogarithmic in `m`; an `m^theta` width would also be useful if matched by a proven prime-gap theorem.

## PP3 — Robust seed preparation

### Target statement

Prove that the prime-minus-one construction can be chosen with a boundary or distributed absorber reservoir satisfying PP2, rather than as an arbitrary saturated configuration. The reservoir should have:

- low secant shadow into future rows and columns;
- many interchangeable row-column states;
- bounded interaction with the core construction;
- compatibility with deleting a variable number `t` of blocks.

This may require reserving rows and columns before the main prime-grid repair process.

## PP4 — Prime-gap transfer theorem

### Target statement

Let `P` be a set of solved side lengths, for example `P={p-1:p prime}`. If every sufficiently large `n` has some `m in P` with

\[
0\le n-m\le w(m),
\]

then PP1–PP3 imply `D(n)=2n` for every sufficiently large `n`.

State the exact unconditional or conditional prime-gap input needed for the proved width `w(m)`.

No conjectural prime-gap assertion should be described as completing the proof unless the extension theorem and the gap theorem are both available.

## PP5 — Finite exceptions

### Target statement

Once PP4 covers all `n>=n_0`, provide exact constructions or certified computational solutions for every `n<n_0` not already covered.

The finite verification must include machine-checkable coordinates and exact integer determinant checks.

## Candidate absorber designs

- boundary ladders using alternating cycles in the row-column graph;
- subgroup-coset blocks reserved across several outer strips;
- recursive two-row/two-column extension gadgets;
- Hall-type completion in a near-complete new-row/new-column host;
- tomographic trades that free selected old rows and columns before extension.

## Falsification programme

- test whether a saturated core can block every cell in one new row by old secants;
- enumerate minimal extension obstructions for small `t`;
- search for configurations requiring changes far from the boundary;
- verify that proposed recursive gadgets do not create long-slope triples with the old core.

## Completion criterion

This branch is complete when PP1–PP5 provide an exact theorem transferring the prime-minus-one result to every sufficiently large `n`, followed by finite verification of the remaining sizes.