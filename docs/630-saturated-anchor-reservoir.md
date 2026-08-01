# Saturated retained-source anchor reservoir

`docs/624` realizes unary-run anchors on an external parabola source. This
chapter replaces that source by an explicit finite two-per-row/two-per-column
no-three-in-line reservoir large enough for all eleven maximal unary runs.

## Theorem PP3cxe — explicit saturated 11 by 11 source

Let the two permutations be

```text
P=(4,1,3,9,8,0,2,10,5,7,6),
Q=(6,3,1,8,5,10,0,2,7,9,4).
```

Their union contains twenty-two cells in an `11x11` grid, has degree two in every
row and column, and contains no collinear triple.

## Theorem PP3cxf — eleven disjoint anchor pairs

Pair the `P` cell in row `r` with the `Q` cell in row

```text
(1,0,3,2,5,4,8,6,7,10,9)[r].
```

The eleven pairs partition all twenty-two source cells. Every pair uses distinct
rows and columns, and no two pairs determine the same support line because the
source itself is no-three-in-line.

## Theorem PP3cxg — complete unary-run embedding census

For every one of the `2^10=1024` ordered compositions of eleven unary nodes,
assign one anchor pair to each maximal run and greedily choose the required
integer insertion cells on its support line. The construction keeps all
insertion rows and columns distinct and creates no collinear triple involving
more than one run.

All 1024 compositions pass exact determinant checking; the maximum coordinate
magnitude is `110`.

This closes the finite saturated-reservoir identification for the size-thirty
profile. It does not provide an asymptotic saturated source family compatible
with every prime-patching scale.
