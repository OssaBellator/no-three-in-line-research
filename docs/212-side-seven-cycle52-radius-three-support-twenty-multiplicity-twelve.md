# Exact `(5,2)` radius-three support-twenty multiplicity-12 obstruction

PX659--PX662 close multiplicity thirteen. This chapter closes the next nonempty top-signature tier in the exact `(5,2)` radius-three support-twenty cache. This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier

### Theorem PX663 -- PROVED FINITE

The exact support-twenty layer has one hundred twenty-eight top signatures of multiplicity `12`, containing

\[
128\cdot12=\boxed{1{,}536}
\]

selectors.

The standalone verifier records and asserts the lexicographically ordered signature, clean-top order counts, clean-top search-node counts, and four orientation-specific bottom-CSP node counts for every class.

### Theorem PX664 -- PROVED FINITE

The aggregate exact clean-top counts are:

- `5,066,246` concatenated orders;
- `3,953,042` interleaved orders;
- `39,315,962` concatenated top-search nodes;
- `31,378,820` interleaved top-search nodes.

The aggregate bottom-CSP counts by orientation are

\[
10{,}846{,}582,\quad 8{,}787{,}671,\quad
11{,}012{,}223,\quad 8{,}225{,}462.
\]

## 2. Exact infeasibility

### Theorem PX665 -- PROVED FINITE

All `1,536` multiplicity-12 selectors fail in every radix orientation after exactly

\[
10{,}846{,}582+8{,}787{,}671+11{,}012{,}223+8{,}225{,}462
=\boxed{38{,}871{,}938}
\]

shared bottom-CSP nodes. No clean top order and bottom-row permutation leaves an active selector.

### Proof

Regenerate the exact alternating-cycle radius layers around the canonical `(5,2)` centre. Their sizes are `364`, `26,550`, and `71,860`. Restrict the third layer to support twenty and group by the first seven row masks; the exact histogram contains one hundred twenty-eight classes of size twelve. For each class, enumerate both all-different top column orders, reject completed integer-collinear top triples, and search the bottom-row permutation while maintaining the exact active-selector bit mask. Every branch ends with mask zero. The verifier asserts each per-class and aggregate count. \(\square\)

## 3. Reusable exact engine

The common radius-layer generation, clean-top enumeration, hoisted incidence masks, scalar point tables, active-selector propagation, and count assertions now live in

`scripts/product_side_seven_cache_engine.hpp`.

Each later tier needs only a `CaseData` table and a call to `verify_tier`. This refactor preserves the exact search and published count semantics while eliminating duplicated solver implementations across new tier scripts.

## 4. Revised cache boundary

### Corollary PX666 -- PROVED REDUCTION

Adding multiplicity twelve gives

\[
3{,}964+1{,}536=\boxed{5{,}500}
\]

certified-infeasible selectors and

\[
90{,}056{,}398+38{,}871{,}938=\boxed{128{,}928{,}336}
\]

cumulative shared bottom-CSP nodes. The active support-twenty count is

\[
71{,}860-5{,}500=\boxed{66{,}360}.
\]

There is no multiplicity-11 class. The next nonempty tier is multiplicity `10`: one hundred sixty-four signatures containing `1,640` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity12.cpp \
  -o /tmp/m12

for case_index in $(seq 0 127); do
  for orientation in 0 1 2 3; do
    /tmp/m12 "$case_index" "$orientation"
  done
done
```

Each invocation regenerates the complete selector layer, verifies the 128-class multiplicity-12 histogram, checks the selected twelve-element group, and asserts exact integer-determinant search counts on `[14]^2`.
