# Multiplicity-two case-zero orientation-three common semantic cover core

PX1010--PX1012 produce a seven-column two-selector master nogood from top order
35. The most frequent syntactic support mask in the 64-top prefix is `6975`; it
occurs for both selectors at top order zero. This chapter semantically minimizes
those two covers.

Both greedy covers contain seven triples and initially depend on the same ten
columns.

## 1. Identical selector-level minimization

### Theorem PX1013 -- PROVED FINITE

For each selector, columns zero, one, two, and five may be deleted successively
from syntactic mask `6975`. The resulting semantic mask is

\[
\boxed{6936}
\]

with exactly six fixed top columns.

The stored cover remains valid across all four clean top extensions of this
mask, giving `20,160` exact bottom checks per selector.

Every attempted deletion from mask `6936` fails for both selectors:

| Deleted column | Candidate size | Clean extensions | First failure after checked extensions |
|---:|---:|---:|---:|
| 3 | 5 | 20 | 1 |
| 4 | 5 | 6 | 5 |
| 8 | 5 | 12 | 3 |
| 9 | 5 | 12 | 3 |
| 11 | 5 | 10 | 5 |
| 12 | 5 | 12 | 3 |

Thus both fixed seven-triple covers have the same deletion-minimal semantic
support.

## 2. Common six-literal master nogood

### Theorem PX1014 -- PROVED FINITE

Because the selector masks coincide, their union incurs no additional literals:

\[
6936\mathbin{\mathrm{OR}}6936=\boxed{6936}.
\]

The common six-column assignment has four clean top extensions. Both selectors
are refuted on every extension, so the exact pair verification contains

\[
4\cdot2\cdot5040=\boxed{40{,}320}
\]

bottom checks.

The final deterministic transcript is:

```text
FINAL case=0 orientation=3 top_index=0 selector0_mask=6936 selector1_mask=6936 pair_mask=6936 pair_size=6 clean_extensions=4 top_nodes=128 tested_bottoms=40320 digest=7882978161453882300 PASS
```

## 3. Compression consequence

### Corollary PX1015 -- PROVED REDUCTION

One six-literal partial-top assignment, together with two seven-triple covers,
certifies simultaneous infeasibility of both selectors across four complete top
orders. The same assumption mask is inclusion-minimal for each stored cover
under single-literal deletion.

This improves the top-order-35 pilot from seven union literals to six and shows
that repeated syntactic support can correspond to a shared semantic core rather
than merely repeated storage structure.

The certificate is cover-relative; a different cover choice could conceivably
produce a smaller mask. No global lower bound on semantic support size is
claimed.

## 4. Next target

The mask `6975` occurs 28 times in the 64-top prefix. The next exact task is to
determine how many of those occurrences minimize to the same semantic mask
`6936`, and whether the resulting six-literal nogood vocabulary covers more than
four top orders once reference values are accounted for.

This is a finite proof-compression theorem. It does not advance the selector
classification boundary and does not prove an infinite product theorem.

## 5. Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core_top0.py
```

The verifier regenerates both covers, replays every successful and failed
literal deletion, checks the four clean extensions for both selectors, and
asserts the final ordered digest.
