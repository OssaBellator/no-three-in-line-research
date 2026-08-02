# Legal-convex threshold separation

The earlier threshold chapters eliminate transient-buffer reuse and exposure
imbalance, but their native intermediate matrices remain illegal. This chapter
shows that endpoint-only compensation inside the present legal four-layer matrix
catalogue is impossible at every batch length.

## PP3dbf — An exact integer separator

For a `4 x 4` matrix `M`, define

```text
Phi(M) = -M[0,0]
         +M[1,0]+M[1,2]
         +M[2,1]
         +M[3,2]-M[3,3].
```

The threshold source matrix

```text
2 1 1 0
0 2 1 1
1 0 2 1
1 1 0 2
```

has

```text
Phi(SOURCE) = -3.
```

Among all 4,475 matrices formed from four no-three-in-line permutation layers,
`Phi` is always nonnegative. The exact legal score histogram is

```text
0:495, 1:956, 2:1193, 3:1012, 4:590,
5:176, 6:44, 7:8, 8:1.
```

Thus the hyperplane `Phi=0` strictly separates the source from the entire legal
catalogue.

## PP3dbg — No legal endpoint-only compensating batch

Every convex combination of legal four-layer matrices has nonnegative `Phi`, as
does every finite average or normalized multiset sum. Since the source has score
`-3`, no finite collection of legal endpoint matrices can have average equal to
the source.

Equivalently, there is no positive integer `k` and no legal matrices
`M_1,...,M_k` satisfying

```text
M_1 + ... + M_k = k*SOURCE.
```

Therefore a compensating walk cannot be achieved merely by choosing more legal
endpoints from the present catalogue, regardless of length or ordering.

## PP3dbh — Sharp supporting face at distance six

The minimum `L1` distance from the source to a legal four-layer matrix is six.
There are exactly eight nearest legal targets, and every one lies on the
supporting face

```text
Phi(M)=0.
```

Hence the separator is sharp: the existing eight target operations reach the
closest possible legal face, but no combination of points on that face can cancel
the three-unit separator deficit of the source.

## Verification

`scripts/check_threshold_legal_convex_separation.py` reconstructs the eighteen
legal permutation layers, all 4,475 four-layer matrices, the complete score
histogram, and the eight nearest targets.

## Evidence boundary

This is a global obstruction for the current matrix catalogue. Endpoint
compensation requires a hidden-state operation, a source state outside this
catalogue, a different layer model, or a primitive whose legality is not captured
by exposed endpoint matrices alone.
