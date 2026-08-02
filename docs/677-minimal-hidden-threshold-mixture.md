# Minimal hidden threshold mixture

`docs/671` proves that any same-transportation-space compensation needs hidden
weight at least `3/8`. This chapter proves that the lower bound is algebraically
sharp and identifies the smallest equal-weight batch attaining it.

Let `S` be the threshold source matrix and let `H=4I_4`, the unique transportation
matrix of separator score `-8`.

## PP3dcp — Explicit five-state facet average

The following five legal score-zero four-layer matrices lie on the separating
facet:

```text
L1 = ((0,0,4,0),(0,0,0,4),(4,0,0,0),(0,4,0,0)),
L2 = ((0,0,4,0),(0,4,0,0),(0,0,0,4),(4,0,0,0)),
L3 = ((0,4,0,0),(0,0,0,4),(0,0,4,0),(4,0,0,0)),
L4 = ((0,4,0,0),(0,0,4,0),(4,0,0,0),(0,0,0,4)),
L5 = ((4,0,0,0),(0,0,4,0),(0,0,0,4),(0,4,0,0)).
```

They satisfy the exact integer identity

```text
3H + L1 + L2 + L3 + L4 + L5 = 8S.
```

Thus an equal-weight eight-state algebraic batch with three hidden states and five
legal facet states averages exactly to the source.

## PP3dcq — The hidden-mass lower bound is sharp

The witness has hidden weight `3/8`, exactly matching the separator lower bound.
Therefore the bound from `docs/671` is sharp within the convex algebra of integer
row-and-column-sum-four transportation states.

Equality forces every exposed legal state to have separator score zero and every
hidden state to have minimum score `-8`. Since the latter state is uniquely `4I_4`,
the witness also identifies the only hidden matrix that can attain equality.

## PP3dcr — Eight is the minimum equal-weight batch size

For an equal-weight batch of `N` states with `K` hidden states, equality in the
score bound gives

```text
-3N = -8K.
```

Hence `8` divides `N` and `K=3N/8`. The smallest positive possibility is

```text
N=8, K=3,
```

and the explicit identity above realizes it. Therefore eight is the exact minimum
equal-weight batch size attaining the `3/8` hidden-mass law.

## Verification

`scripts/check_threshold_minimal_hidden_mixture.py` reconstructs all eighteen legal
permutation layers, all 4,475 legal four-layer matrices, and the 495-matrix facet.
It verifies that each `Li` is legal and score zero, checks the eight-state matrix
identity exactly, and confirms the divisibility obstruction for equal-weight
batches.

## Evidence boundary

This is an algebraic compensation certificate, not an exposed legal schedule.
`4I_4` consists of four copies of the collinear identity layer and cannot appear as
a legal exposed endpoint. No geometric hidden-state primitive realizes the
three-hidden/five-legal batch or provides a recurrent threshold construction.
