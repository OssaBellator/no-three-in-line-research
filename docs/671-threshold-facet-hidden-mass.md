# Threshold facet and hidden-state mass

The separating functional from `docs/665` excludes compensation by the present
catalogue of exposed legal four-layer endpoints. This chapter identifies the
separator as a facet and quantifies the minimum hidden-state mass required by any
enlargement within the same transportation space.

Let

```text
Phi(M) = -M[0,0] + M[1,0] + M[1,2] + M[2,1] + M[3,2] - M[3,3].
```

The source matrix has `Phi=-3`.

## PP3dbx — The score-zero legal set is a facet

The 4,475 legal four-layer matrices have affine hull dimension nine inside the
row-and-column-sum-four transportation space. Exactly 495 have `Phi=0`, and those
495 matrices have affine hull dimension eight.

Therefore

```text
conv(legal matrices) intersect {Phi=0}
```

is a facet of the legal convex hull. The separator is not an accidental inequality
visible only at the eight nearest targets; it supports a full codimension-one face.

All eight nearest legal matrices, at `L1` distance six from the source, lie on
this facet.

## PP3dby — Exact transportation-space score floor

There are exactly 10,147 nonnegative integer `4 x 4` matrices with every row and
column sum equal to four. Across that complete transportation catalogue, the
minimum score is `-8`, attained uniquely by

```text
4 I_4 =
(4,0,0,0)
(0,4,0,0)
(0,0,4,0)
(0,0,0,4).
```

Thus any hidden state that remains in the same integer transportation space has
score at least `-8`.

## PP3dbz — Necessary hidden-state mass

Consider a convex compensation whose average matrix is the source. Give total
weight `h` to hidden transportation states and weight `1-h` to exposed legal
states. Legal states have score at least zero, while hidden transportation states
have score at least `-8`. Hence the average score is at least `-8h`.

Since the source score is `-3`, necessarily

```text
h >= 3/8.
```

For an equal-weight batch of `N` endpoint states, at least

```text
ceil(3N/8)
```

must therefore be hidden or outside the current legal catalogue.

This is a necessary bound only. It does not assert that the source is representable
when the bound is met.

## Verification

`scripts/check_threshold_facet_hidden_mass.py` reconstructs all eighteen legal
permutation layers, all 4,475 legal four-layer matrices, the 495-vertex facet, and
all 10,147 integer transportation matrices. It computes both affine dimensions by
exact rational elimination and verifies the unique score-minus-eight state.

## Evidence boundary

Any successful threshold mechanism must expose fewer states than its algebraic
endpoint count suggests, introduce a substantial hidden-state phase, or leave the
present transportation model. No such geometric primitive or recurrence is yet
known.
