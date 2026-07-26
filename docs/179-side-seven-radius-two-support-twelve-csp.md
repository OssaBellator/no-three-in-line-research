# Exact side-seven radius-two support-twelve obstruction

PX527 leaves two possible locations for a side-seven certificate: selector
distance at least three, or distance two with symmetric-difference support at
least twelve.  The support-twelve distance-two stratum contains `7396`
selectors.  This chapter exhausts it.

## 1. Exact support-twelve census

### Theorem PX529 -- PROVED FINITE

Every radius-two selector satisfying

\[
|F\triangle F_0|=12
\]

fails the 21-variable coordinate CSP in every radix orientation.

The exact class totals are:

| Relative class | Selectors | CSP nodes | Feasible selectors |
|---|---:|---:|---:|
| `(7)` | 3,606 | 2,735,202,607 | 0 |
| `(5,2)` | 1,584 | 1,103,440,538 | 0 |
| `(4,3)` | 1,004 | 915,236,711 | 0 |
| `(3,2,2)` | 1,202 | 708,051,312 | 0 |
| **Total** | **7,396** | **5,461,931,168** | **0** |

### Proof

Regenerate the exact radius-two layer from PX519, retain the support-twelve
histogram stratum from PX521, and apply the dangerous-point coordinate recursion
of PX515 to every selector and orientation.  The search is split into twenty
deterministic shards.  Each shard asserts its selector interval and exact node
total; no shard returns a complete coordinate assignment. \(\square\)

### Corollary PX530 -- PROVED FINITE

No side-seven full-selector certificate occurs at alternating-cycle distance two
and symmetric-difference support twelve.

## 2. Revised distance-two boundary

### Corollary PX531 -- PROVED REDUCTION

If a side-seven full-selector template exists, then either:

1. its selector lies at distance two and
   
   \[
   |F\triangle F_0|\ge14;
   \]

2. or its selector has alternating-cycle distance at least three.

The radius-two support-fourteen stratum has class counts

\[
4424,\qquad1768,\qquad2132,\qquad988,
\]

and total

\[
\boxed{9312}.
\]

### Corollary PX532 -- PROVED REDUCTION

The immediate exact coordinate target is the 9,312-selector support-fourteen
stratum.  Cumulative failure through support twelve covers

\[
2236+1864+7396
=
\boxed{11496}
\]

distance-two selectors.

This remains a finite obstruction around four centres, not a proof that the
full selector classes are geometrically infeasible.

## 3. Verification

The sharded verifier

```bash
scripts/verify_product_side_seven_radius_two_support_csp.cpp
```

accepts support `12` in addition to supports `8` and `10`.  Compile it and run
all embedded class shards.  The expected node totals are part of the executable
certificate.
