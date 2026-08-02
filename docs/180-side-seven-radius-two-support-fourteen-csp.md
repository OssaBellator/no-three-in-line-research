# Exact side-seven radius-two support-fourteen obstruction

PX531 leaves two possible locations for a side-seven certificate: selector
distance at least three, or distance two with symmetric-difference support at
least fourteen.  The support-fourteen distance-two stratum contains `9312`
selectors.  This chapter exhausts it in all four radix orientations.

## 1. Exact support-fourteen census

### Theorem PX533 -- PROVED FINITE

Every radius-two selector satisfying

\[
|F\triangle F_0|=14
\]

fails the 21-variable coordinate CSP.

The exact class totals are:

| Relative class | Selectors | CSP nodes | Feasible selectors |
|---|---:|---:|---:|
| `(7)` | 4,424 | 2,961,462,605 | 0 |
| `(5,2)` | 1,768 | 1,225,466,432 | 0 |
| `(4,3)` | 2,132 | 1,886,418,924 | 0 |
| `(3,2,2)` | 988 | 639,620,973 | 0 |
| **Total** | **9,312** | **6,712,968,934** | **0** |

### Proof

Regenerate the exact radius-two layer from PX519, retain the support-fourteen
stratum in the PX521 histogram, and run the PX515 dangerous-point coordinate
CSP for every selector and orientation.  The search is split into twenty
contiguous deterministic shards.  Every shard asserts its selector interval and
exact node total; none returns a complete coordinate assignment. \(\square\)

### Corollary PX534 -- PROVED FINITE

No side-seven full-selector certificate occurs at alternating-cycle distance two
and symmetric-difference support fourteen.

## 2. Revised distance-two boundary

### Corollary PX535 -- PROVED REDUCTION

If a side-seven full-selector template exists, then either:

1. its selector lies at distance two and
   
   \[
   |F\triangle F_0|\ge16;
   \]

2. or its selector has alternating-cycle distance at least three.

The radius-two support-sixteen stratum has class counts

\[
18{,}878,\qquad5{,}315,\qquad2{,}013,\qquad478,
\]

and total

\[
\boxed{26{,}684}.
\]

### Corollary PX536 -- PROVED REDUCTION

Cumulative distance-two failure through support fourteen covers

\[
2{,}236+1{,}864+7{,}396+9{,}312
=
\boxed{20{,}808}
\]

selectors and

\[
1{,}594{,}005{,}329
+1{,}326{,}750{,}836
+5{,}461{,}931{,}168
+6{,}712{,}968{,}934
=
\boxed{15{,}095{,}656{,}267}
\]

coordinate-CSP nodes.

The immediate exact target is the support-sixteen stratum.  Because its size is
26,684, the next implementation priority is shared coordinate-state caching by
radius-one parent or by common selector row masks, rather than independent CSP
runs.

This remains a finite obstruction around four certified centres, not a proof
that universal side-seven doubling fails.

## 3. Verification

The shared sharded verifier

```bash
scripts/verify_product_side_seven_radius_two_support_csp.cpp
```

accepts support `14`.  Compile it and run all embedded class shards.  Each shard
regenerates the selector layer and asserts its exact node total using integer
collinearity tests on `[14]^2`.
