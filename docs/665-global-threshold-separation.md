# Global threshold separation

The previous threshold chapters show that nearest legal targets have sign-coherent
drift and that balanced native factorizations still expose illegal intermediate
states. This chapter tests the entire legal four-layer endpoint catalogue rather
than only the eight nearest targets.

## PP3dbf — Complete legal endpoint catalogue

There are exactly eighteen no-three permutation layers on the `4 x 4` grid.
Taking unordered multisets of four such layers produces exactly 4,475 distinct
legal four-layer matrices.

The threshold source matrix

```text
2 1 1 0
0 2 1 1
1 0 2 1
1 1 0 2
```

is not one of those 4,475 matrices.

## PP3dbg — Exact integer separating functional

For a matrix `M`, define

```text
Phi(M) = M[0,3] + M[1,0] - M[1,1] - M[2,2]
         + M[3,0] + M[3,2].
```

The source has

```text
Phi(SOURCE) = -3.
```

Across all 4,475 legal endpoint matrices, the exact `Phi` distribution is

```text
0:495, 1:956, 2:1193, 3:1012, 4:590,
5:176, 6:44, 7:8, 8:1.
```

Therefore every legal endpoint satisfies

```text
Phi(M-SOURCE) >= 3.
```

The integer margin is sharp because 495 legal matrices attain equality.

## PP3dbh — Global no-compensation theorem

For any nonempty multiset of `k` legal four-layer endpoints
`M_1,...,M_k`, additivity gives

```text
Phi(sum_i(M_i-SOURCE)) >= 3k > 0.
```

Hence no nonempty finite collection of legal endpoints has zero aggregate
displacement from the source. Equivalently, the source is outside the convex hull
of the complete legal endpoint catalogue.

Thus no inverse pair, finite compensating cycle, or longer balanced endpoint
schedule can neutralize the threshold source while remaining inside the native
legal four-layer catalogue. A successful mechanism must change the source
interface, introduce a different endpoint catalogue, or use a protected operation
whose relevant conserved state is not this matrix average.

The exact enumeration and separation audit is
`scripts/check_threshold_global_separation.py`.

## Evidence boundary

This is a complete matrix-level impossibility theorem for the native endpoint
catalogue. It does not rule out a larger geometric state space, hidden-state
operations, or a different source primitive.
