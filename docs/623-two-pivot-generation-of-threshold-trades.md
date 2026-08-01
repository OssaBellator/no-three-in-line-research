# Two-pivot generation of threshold three-cycle trades

`docs/617` classifies the eight nearest legal degree-four threshold matrices as
unit alternating three-cycle trades.  This chapter connects those targets to the
conservative residual-flow pivots of `docs/509` and records the exact geometric
atomicity obstruction.

## 1. Conservative two-pivot generation

### Theorem PP3cwj -- PROVED / COMPLETE TWO-PIVOT REACHABILITY

Every one of the eight nearest legal matrices is reachable from the stored source
matrix by exactly two allowed conservative `2x2` pivots.  No target is reachable
by one pivot.

Across the eight targets there are forty-eight ordered shortest paths, exactly
six per target, using twenty distinct intermediate matrices.

#### Proof

An allowed pivot subtracts one unit from one diagonal of a `2x2` rectangle and
adds one unit to the other diagonal without making an entry negative.  It is an
integral circulation and preserves all row and column margins.  Enumerate every
first pivot from the source and every second pivot, then compare the endpoints
with the 4,475 matrices decomposable into four legal no-three-in-line permutation
layers.  The exact counts are as stated.  ∎

## 2. Illegal intermediate obstruction

### Theorem PP3cwk -- PROVED / NO LEGAL VISIBLE FACTORIZATION

None of the twenty intermediate matrices on the forty-eight shortest paths is
decomposable into four legal no-three-in-line layers.

Consequently no target can be implemented as two temporally visible legal
threshold schedules, even though every matrix entry remains nonnegative and all
margins remain four.

#### Proof

Exact membership testing against the complete set of 4,475 legal degree-four
matrices rejects all twenty intermediates.  ∎

## 3. Candidate source path and atomicity obligation

### Theorem PP3cwl -- PROVED / MATRIX-LEVEL SOURCE PATH

The threshold candidate has a complete repository-native matrix-level source
path: every desired three-cycle replacement is a compound of two standard
conservative residual pivots.  This completes the fifth candidate threshold
field.

The remaining geometric obligation is sharper: realize the two pivots atomically,
or by a larger source edit whose exposed states never equal the illegal
intermediate.

#### Proof

Each pivot is the integral four-cycle circulation used by conservative matrix
rounding.  `PP3cwj` supplies a two-pivot path to every target, while `PP3cwk`
shows why the compound cannot be separated into two legal visible schedules.  ∎

No theorem currently maps the atomic compound to legal edits on actual prime-
patching source cells, so the actual threshold ledger row remains unpromoted.
