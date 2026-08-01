# Atomic two-swap generation of threshold trades

`docs/617` classifies the eight nearest legal degree-four threshold matrices as
unit alternating three-cycle trades.  This chapter connects those targets to the
conservative residual-flow pivots of `docs/509` and records the exact atomicity
obstruction.

## 1. Complete two-swap generation

### Theorem PP3cwj -- PROVED / TWO-SWAP SOURCE PATHS

Every one of the eight nearest legal matrices is reachable from the stored source
matrix by exactly two allowed conservative `2x2` swaps.  No target is reachable
by one swap.

Across the eight targets there are forty-eight ordered shortest paths, exactly
six per target, using twenty distinct intermediate matrices.

#### Proof

An allowed swap subtracts one unit from one diagonal of a `2x2` rectangle and
adds one unit to the other diagonal without making an entry negative.  It
preserves all row and column margins.  Enumerate every first swap from the source
and every second swap, then compare the endpoints with the 4,475 matrices
decomposable into four legal no-three-in-line permutation layers.  ∎

## 2. Illegal intermediate obstruction

### Theorem PP3cwk -- PROVED / NO LEGAL VISIBLE FACTORIZATION

None of the twenty intermediate matrices on the forty-eight shortest paths is
decomposable into four legal no-three-in-line layers.

Consequently no target can be implemented as two temporally visible legal
threshold schedules, although every intermediate is nonnegative and has all
margins equal to four.

#### Proof

Exact membership testing against the complete set of 4,475 legal degree-four
matrices rejects all twenty intermediates.  ∎

## 3. Candidate source path and atomicity obligation

### Theorem PP3cwl -- PROVED / MATRIX-LEVEL SOURCE GENERATION

Every desired three-cycle replacement is a compound of two repository-native
conservative residual swaps.  This completes the fifth candidate threshold
field and raises total candidate coverage by one.

The remaining geometric obligation is to realize the pair atomically, or by a
larger source edit whose exposed states never equal the illegal intermediate.

#### Proof

Each swap is an integral four-cycle circulation of the conservative matrix
kernel.  `PP3cwj` supplies a path to every target, while `PP3cwk` proves that the
compound cannot be separated into two visible legal schedules.  ∎

No theorem currently maps the atomic compound to legal edits on actual prime-
patching source cells, so the actual threshold row remains unpromoted.
