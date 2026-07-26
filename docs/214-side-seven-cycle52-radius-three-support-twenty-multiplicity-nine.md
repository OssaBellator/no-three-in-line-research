# Exact `(5,2)` radius-three support-twenty multiplicity-9 obstruction

PX667--PX670 close multiplicity ten. This chapter closes the next nonempty top-signature tier in the exact `(5,2)` radius-three support-twenty cache. This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier

### Theorem PX671 -- PROVED FINITE

The exact support-twenty layer has sixty-four top signatures of multiplicity `9`, containing

\[
64\cdot9=\boxed{576}
\]

selectors.

The standalone verifier records and asserts the lexicographically ordered signature, clean-top order counts, clean-top search-node counts, and four orientation-specific bottom-CSP node counts for every class. Its data are split into two include files and executed by the shared exact engine.

### Theorem PX672 -- PROVED FINITE

The aggregate exact clean-top counts are:

- `1,797,736` concatenated orders;
- `1,992,555` interleaved orders;
- `14,812,380` concatenated top-search nodes;
- `15,387,412` interleaved top-search nodes.

The aggregate bottom-CSP counts by orientation are

\[
3{,}675{,}568,\quad 4{,}090{,}822,\quad
3{,}440{,}689,\quad 3{,}904{,}096.
\]

## 2. Exact infeasibility

### Theorem PX673 -- PROVED FINITE

All `576` multiplicity-9 selectors fail in every radix orientation after exactly

\[
3{,}675{,}568+4{,}090{,}822+3{,}440{,}689+3{,}904{,}096
=\boxed{15{,}111{,}175}
\]

shared bottom-CSP nodes. No clean top order and bottom-row permutation leaves an active selector.

### Proof

Regenerate the exact alternating-cycle radius layers around the canonical `(5,2)` centre. Their sizes are `364`, `26,550`, and `71,860`. Restrict the third layer to support twenty and group by the first seven row masks; the exact histogram contains sixty-four classes of size nine. For each class, enumerate both all-different top column orders, reject completed integer-collinear top triples, and search the bottom-row permutation while maintaining the exact active-selector bit mask. Every branch ends with mask zero. The verifier asserts each per-class and aggregate count. \(\square\)

## 3. Revised cache boundary

### Corollary PX674 -- PROVED REDUCTION

Adding multiplicity nine gives

\[
7{,}140+576=\boxed{7{,}716}
\]

certified-infeasible selectors and

\[
190{,}606{,}879+15{,}111{,}175=\boxed{205{,}718{,}054}
\]

cumulative shared bottom-CSP nodes. The active support-twenty count is

\[
71{,}860-7{,}716=\boxed{64{,}144}.
\]

The next nonempty tier is multiplicity `8`: two hundred seventy-seven signatures containing `2,216` selectors.

## 4. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity9.cpp \
  -o /tmp/m9

for case_index in $(seq 0 63); do
  for orientation in 0 1 2 3; do
    /tmp/m9 "$case_index" "$orientation"
  done
done
```

Each invocation regenerates the complete selector layer, verifies the 64-class multiplicity-9 histogram, checks the selected nine-element group, and asserts exact integer-determinant search counts on `[14]^2`.
