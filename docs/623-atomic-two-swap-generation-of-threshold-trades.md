# Atomic two-swap generation of threshold trades

`docs/617` identifies eight nearest legal degree-four matrices, each differing
from the stored source matrix by one alternating three-cycle.  This chapter
locates those targets in the conservative `2x2` trade graph.

## 1. Exact two-swap generation

### Theorem PP3cwj -- PROVED / TWO-SWAP GENERATION

Every one of the eight nearest legal matrices is reachable from the stored source
matrix by exactly two elementary conservative `2x2` swaps.  No target is
reachable by one swap.

Across all targets there are forty-eight ordered length-two paths, exactly six
per target, using twenty distinct intermediate matrices.

#### Proof

An elementary swap subtracts one unit from one diagonal of a `2x2` submatrix and
adds one unit to the other diagonal, whenever the subtracted entries are
positive.  Enumerate all such first swaps from the source and all legal second
swaps.  Compare the endpoints with the 4,475 matrices decomposable into four
legal no-three-in-line permutation layers.  The exact counts are as stated.  ∎

## 2. Illegal intermediate obstruction

### Theorem PP3cwk -- PROVED / NO LEGAL TWO-SWAP FACTORIZATION

None of the twenty intermediate matrices on the forty-eight generation paths is
decomposable into four legal no-three-in-line layers.

Consequently the three-cycle replacement cannot be implemented as two temporally
visible threshold schedules while keeping every intermediate schedule legal.

#### Proof

The complete multiset enumeration of four legal layers contains 4,475 distinct
matrices.  Exact membership testing rejects all twenty intermediates.  ∎

## 3. Atomic source-operation obligation

### Theorem PP3cwl -- PROVED AS A FINITE REDUCTION / COMPOUND TRADE TARGET

At the conservative matrix level, the threshold source-generation problem is
closed: each desired replacement is a compound of two elementary margin-
preserving swaps.  The remaining geometric obligation is to realize the pair
atomically, or through a larger source move whose exposed states never equal the
illegal intermediate.

This does not identify a prime-patching source operation.  It replaces the vague
three-cycle request by an exact two-swap atomicity requirement.
