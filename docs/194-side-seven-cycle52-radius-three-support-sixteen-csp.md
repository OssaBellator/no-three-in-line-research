# Exact `(5,2)` radius-three support-sixteen obstruction

PX583--PX585 close support fourteen in the exact `(5,2)` radius-three selector
layer.  The next stratum contains `19,352` selectors at symmetric-difference
support sixteen.

## 1. Complete coordinate census

### Theorem PX586 -- PROVED FINITE

Every `(5,2)` radius-three selector satisfying

\[
|F\triangle F_0|=16
\]

fails the exact coordinate CSP in all four radix orientations.

The lexicographically ordered layer is split into nineteen 1,000-selector
intervals and one final 352-selector interval:

| Selector interval | CSP nodes |
|---:|---:|
| 1--1,000 | 585,067,681 |
| 1,001--2,000 | 468,784,112 |
| 2,001--3,000 | 728,681,313 |
| 3,001--4,000 | 941,494,170 |
| 4,001--5,000 | 622,100,851 |
| 5,001--6,000 | 644,069,749 |
| 6,001--7,000 | 431,652,930 |
| 7,001--8,000 | 786,174,015 |
| 8,001--9,000 | 944,855,043 |
| 9,001--10,000 | 584,547,327 |
| 10,001--11,000 | 529,964,943 |
| 11,001--12,000 | 569,529,910 |
| 12,001--13,000 | 1,233,017,632 |
| 13,001--14,000 | 1,106,320,767 |
| 14,001--15,000 | 1,027,677,881 |
| 15,001--16,000 | 759,818,614 |
| 16,001--17,000 | 1,006,032,277 |
| 17,001--18,000 | 702,211,176 |
| 18,001--19,000 | 1,358,763,137 |
| 19,001--19,352 | 446,410,026 |
| **Total** | **15,477,173,554** |

No interval returns a complete coordinate assignment.

### Proof

Regenerate the exact first three selector layers and retain the support-sixteen
stratum from PX577.  For every selector and each of the four orientations, run
the PX515 dangerous-point coordinate recursion.  The twenty deterministic
intervals partition all `19,352` selectors; each records the exact node total
above and returns no feasible embedding.  Summation gives the displayed total.
\(\square\)

### Corollary PX587 -- PROVED REDUCTION

Any coordinate-embeddable `(5,2)` selector at alternating-cycle distance three
has

\[
|F\triangle F_0|\ge18.
\]

### Corollary PX588 -- PROVED REDUCTION

The first open `(5,2)` radius-three stratum is support eighteen and contains
exactly

\[
\boxed{18{,}336}
\]

selectors.  This remains a finite obstruction around the certified centre, not
a proof that the `(5,2)` canonical host problem is globally infeasible.

## 2. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/search_product_side_seven_radius_three_support.cpp \
  -o /tmp/side7_radius3_range
```

and run class `cycle52`, support `16`, on the twenty displayed intervals.  The
search regenerates the exact radius-three layer and uses integer determinant
tests on `[14]^2`.