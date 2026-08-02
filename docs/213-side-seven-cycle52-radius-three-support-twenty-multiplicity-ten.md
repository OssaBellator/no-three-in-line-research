# Exact `(5,2)` radius-three support-twenty multiplicity-10 obstruction

PX663--PX666 close multiplicity twelve; there is no multiplicity-eleven class. This chapter closes the next nonempty top-signature tier in the exact `(5,2)` radius-three support-twenty cache. This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier

### Theorem PX667 -- PROVED FINITE

The exact support-twenty layer has one hundred sixty-four top signatures of multiplicity `10`, containing

\[
164\cdot10=\boxed{1{,}640}
\]

selectors.

The standalone verifier records and asserts the lexicographically ordered signature, clean-top order counts, clean-top search-node counts, and four orientation-specific bottom-CSP node counts for every class. The case data are split into four include files so the proof data remain reviewable and the executable uses the shared exact engine.

### Theorem PX668 -- PROVED FINITE

The aggregate exact clean-top counts are:

- `8,140,864` concatenated orders;
- `5,304,038` interleaved orders;
- `62,411,264` concatenated top-search nodes;
- `43,424,113` interleaved top-search nodes.

The aggregate bottom-CSP counts by orientation are

\[
19{,}374{,}191,\quad 12{,}381{,}914,\quad
18{,}412{,}588,\quad 11{,}509{,}850.
\]

## 2. Exact infeasibility

### Theorem PX669 -- PROVED FINITE

All `1,640` multiplicity-10 selectors fail in every radix orientation after exactly

\[
19{,}374{,}191+12{,}381{,}914+18{,}412{,}588+11{,}509{,}850
=\boxed{61{,}678{,}543}
\]

shared bottom-CSP nodes. No clean top order and bottom-row permutation leaves an active selector.

### Proof

Regenerate the exact alternating-cycle radius layers around the canonical `(5,2)` centre. Their sizes are `364`, `26,550`, and `71,860`. Restrict the third layer to support twenty and group by the first seven row masks; the exact histogram contains one hundred sixty-four classes of size ten. For each class, enumerate both all-different top column orders, reject completed integer-collinear top triples, and search the bottom-row permutation while maintaining the exact active-selector bit mask. Every branch ends with mask zero. The verifier asserts each per-class and aggregate count. \(\square\)

## 3. Revised cache boundary

### Corollary PX670 -- PROVED REDUCTION

Adding multiplicity ten gives

\[
5{,}500+1{,}640=\boxed{7{,}140}
\]

certified-infeasible selectors and

\[
128{,}928{,}336+61{,}678{,}543=\boxed{190{,}606{,}879}
\]

cumulative shared bottom-CSP nodes. The active support-twenty count is

\[
71{,}860-7{,}140=\boxed{64{,}720}.
\]

The next nonempty tier is multiplicity `9`: sixty-four signatures containing `576` selectors.

## 4. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity10.cpp \
  -o /tmp/m10

for case_index in $(seq 0 163); do
  for orientation in 0 1 2 3; do
    /tmp/m10 "$case_index" "$orientation"
  done
done
```

Each invocation regenerates the complete selector layer, verifies the 164-class multiplicity-10 histogram, checks the selected ten-element group, and asserts exact integer-determinant search counts on `[14]^2`.
