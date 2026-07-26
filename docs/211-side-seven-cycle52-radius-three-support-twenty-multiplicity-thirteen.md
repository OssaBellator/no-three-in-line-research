# Exact `(5,2)` radius-three support-twenty multiplicity-13 obstruction

PX655--PX658 close multiplicity fourteen. This chapter closes the next nonempty top-signature tier in the exact `(5,2)` radius-three support-twenty cache. This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier

### Theorem PX659 -- PROVED FINITE

The exact support-twenty layer has forty-eight top signatures of multiplicity `13`, containing

\[
48\cdot13=\boxed{624}
\]

selectors.

The standalone verifier records and asserts the lexicographically ordered signature, clean-top order counts, clean-top search-node counts, and four orientation-specific bottom-CSP node counts for every one of the forty-eight classes.

### Theorem PX660 -- PROVED FINITE

The aggregate exact clean-top counts are:

- `2,365,929` concatenated orders;
- `1,208,891` interleaved orders;
- `19,068,192` concatenated top-search nodes;
- `10,861,516` interleaved top-search nodes.

The aggregate bottom-CSP counts by orientation are

\[
5{,}412{,}072,\quad 2{,}769{,}845,\quad
5{,}441{,}853,\quad 2{,}705{,}943.
\]

## 2. Exact infeasibility

### Theorem PX661 -- PROVED FINITE

All `624` multiplicity-13 selectors fail in every radix orientation after exactly

\[
5{,}412{,}072+2{,}769{,}845+5{,}441{,}853+2{,}705{,}943
=\boxed{16{,}329{,}713}
\]

shared bottom-CSP nodes. No clean top order and bottom-row permutation leaves an active selector.

### Proof

Regenerate the exact alternating-cycle radius layers around the canonical `(5,2)` centre. Their sizes are `364`, `26,550`, and `71,860`. Restrict the third layer to support twenty and group by the first seven row masks; the exact histogram contains forty-eight classes of size thirteen. For each class, enumerate both all-different top column orders, reject completed integer-collinear top triples, and search the bottom-row permutation while maintaining the exact active-selector bit mask. Every branch ends with mask zero. The verifier asserts each per-class and aggregate count. \(\square\)

## 3. Revised cache boundary

### Corollary PX662 -- PROVED REDUCTION

Adding multiplicity thirteen gives

\[
3{,}340+624=\boxed{3{,}964}
\]

certified-infeasible selectors and

\[
73{,}726{,}685+16{,}329{,}713=\boxed{90{,}056{,}398}
\]

cumulative shared bottom-CSP nodes. The active support-twenty count is

\[
71{,}860-3{,}964=\boxed{67{,}896}.
\]

The next nonempty tier is multiplicity `12`: one hundred twenty-eight signatures containing `1,536` selectors.

## 4. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity13.cpp \
  -o /tmp/m13

for case_index in $(seq 0 47); do
  for orientation in 0 1 2 3; do
    /tmp/m13 "$case_index" "$orientation"
  done
done
```

Each invocation regenerates the complete selector layer, verifies the forty-eight-class multiplicity-13 histogram, checks the selected thirteen-element group, and asserts exact integer-determinant search counts on `[14]^2`.
