# Exact `(5,2)` radius-three support-eighteen obstruction

PX586--PX588 close support sixteen in the exact `(5,2)` radius-three selector
layer.  The next stratum contains `18,336` selectors at symmetric-difference
support eighteen.

## 1. Complete coordinate census

### Theorem PX589 -- PROVED FINITE

Every `(5,2)` radius-three selector satisfying

\[
|F\triangle F_0|=18
\]

fails the exact coordinate CSP in all four radix orientations.

The lexicographically ordered layer is split into eighteen 1,000-selector
intervals and one final 336-selector interval:

| Selector interval | CSP nodes |
|---:|---:|
| 1--1,000 | 565,781,650 |
| 1,001--2,000 | 673,515,968 |
| 2,001--3,000 | 732,521,201 |
| 3,001--4,000 | 803,681,136 |
| 4,001--5,000 | 578,943,304 |
| 5,001--6,000 | 576,485,631 |
| 6,001--7,000 | 493,101,924 |
| 7,001--8,000 | 786,032,048 |
| 8,001--9,000 | 848,103,393 |
| 9,001--10,000 | 614,200,631 |
| 10,001--11,000 | 664,692,958 |
| 11,001--12,000 | 987,641,609 |
| 12,001--13,000 | 975,243,375 |
| 13,001--14,000 | 1,091,607,602 |
| 14,001--15,000 | 851,948,118 |
| 15,001--16,000 | 882,518,590 |
| 16,001--17,000 | 800,847,607 |
| 17,001--18,000 | 1,210,432,179 |
| 18,001--18,336 | 444,347,727 |
| **Total** | **14,581,646,651** |

No interval returns a complete coordinate assignment.

### Proof

Regenerate the exact first three selector layers and retain the support-eighteen
stratum from PX577.  Apply the PX515 dangerous-point coordinate CSP to every
selector and each of the four radix orientations.  The nineteen deterministic
intervals partition all `18,336` selectors; each exhausts its exact search tree
and returns no feasible embedding.  Summing their node totals gives the value
above. \(\square\)

### Corollary PX590 -- PROVED REDUCTION

Any coordinate-embeddable `(5,2)` selector at alternating-cycle distance three
has

\[
|F\triangle F_0|\ge20.
\]

### Corollary PX591 -- PROVED REDUCTION

The first open `(5,2)` radius-three stratum is support twenty and contains
exactly

\[
\boxed{71{,}860}
\]

selectors.  This is too large for another independent-selector census at the
current branching cost.  The next implementation target is shared coordinate
state caching among selectors with common radius-two parents, common row masks,
or common completed-point dangerous masks.

This remains a finite obstruction around the certified centre, not a proof that
the `(5,2)` canonical host problem is globally infeasible.

## 2. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_three_support.cpp \
  -o /tmp/side7_radius3_range
```

and run class `cycle52`, support `18`, on the nineteen displayed intervals.