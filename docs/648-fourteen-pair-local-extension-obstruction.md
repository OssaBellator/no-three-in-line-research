# Local obstruction to fourteen-pair source extension

`docs/642` gives a saturated thirteen-pair source.  This chapter tests the most
direct extension mechanism: insert one new row and column into each permutation,
then repair by a small number of layer transpositions.

## 1. Complete insertion-plus-one-swap neighbourhood

### Theorem PP3czg — PROVED / 23,273 EXTENSIONS REJECTED

Starting from the canonical thirteen-pair witness, perform every insertion of
the new column into each of the two permutations, placing the displaced entries
in the new row.  Then either make no further change or transpose two entries in
one layer.

After excluding row collisions between the two layers, there are 23,273 valid
candidates.  None is no-three-in-line.

#### Proof

`scripts/check_prefix_13_to_14_neighbourhood.cpp` enumerates the complete stated
neighbourhood and checks all triples exactly. ∎

## 2. Unique minimum-defect candidate

### Theorem PP3czh — PROVED / THREE-TRIPLE MINIMUM

The minimum number of collinear triples in the preceding neighbourhood is three,
attained by exactly one candidate:

```text
P=(9,4,7,13,0,1,12,8,11,10,2,6,5,3)
Q=(7,12,9,11,4,3,8,13,2,1,5,10,6,0).
```

The defect histogram begins

```text
3:1, 4:5, 5:26, 6:183, 7:488.
```

#### Proof

The exhaustive checker records the complete defect histogram and unique
minimizer. ∎

## 3. Two-transposition local obstruction

### Theorem PP3czi — PROVED / NO SECOND-NEIGHBOURHOOD REPAIR

From the unique three-triple candidate, all 25,229 valid ordered move sequences
of length at most two, where each move is a transposition in either layer, still
have at least three collinear triples.

#### Proof

`scripts/check_prefix_14_two_swap_neighbourhood.cpp` exhausts the stated move
sequences and returns the same minimum candidate and defect value. ∎

## Consequence

The canonical thirteen-pair source cannot be extended by the natural insertion
operation plus local permutation repair.  A fourteen-pair source requires a
nonlocal rearrangement or a different uniform family; the result is not an
impossibility theorem for all `14 x 14` saturated sources.
