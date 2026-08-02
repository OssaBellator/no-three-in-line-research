# Exact `(5,2)` radius-three support-twenty multiplicity-eight tier

PX671--PX674 close multiplicity nine. The next nonempty tier has 277 top
signatures of multiplicity eight, hence 2,216 selectors. This chapter closes
the complete tier.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact tier census

### Theorem PX675 -- PROVED FINITE

The exact radius-three support-twenty layer contains exactly 277
lexicographically ordered top signatures of multiplicity eight. Therefore the
tier contains

\[
277\cdot 8=\boxed{2{,}216}
\]

selectors.

The verifier regenerates the radius layers of sizes `364`, `26,550`, and
`71,860`, groups the final support-twenty layer by the first seven row masks,
and asserts the complete multiplicity histogram.

## 2. Exact clean-top census

### Theorem PX676 -- PROVED FINITE

Across all 277 signatures, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 11,957,408 | 80,982,232 |
| Interleaved | 10,852,546 | 75,065,004 |
| **Total** | **22,809,954** | **156,047,236** |

For compact independent verification, the executable prints the complete
per-signature transcript and mixes each signature, both top-order counts, both
top-node counts, and all four bottom-node counts into the deterministic
64-bit transcript digest

`5710772046139185874` (`0x4f40bceb435b5ad2`).

Changing any recorded per-signature count changes the asserted digest.

## 3. Exact shared bottom CSP

### Theorem PX677 -- PROVED FINITE

Every one of the 2,216 selectors fails in every radix orientation. The exact
shared active-selector bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 22,373,701 |
| 1 | 20,809,483 |
| 2 | 22,353,455 |
| 3 | 19,251,567 |
| **Total** | **84,788,206** |

For each clean top order, the solver retains an eight-bit active-selector mask.
Assigning one bottom row position checks every newly completed integer triple
and clears precisely the selector bits containing all three abstract edges.
Every exact tree terminates with the active mask empty.

## 4. Revised cache boundary

### Corollary PX678 -- PROVED REDUCTION

Before this tier the cache had rejected 7,716 selectors in 205,718,054 shared
bottom-CSP nodes. Adding multiplicity eight gives

\[
7{,}716+2{,}216=\boxed{9{,}932}
\]

certified-infeasible selectors and

\[
205{,}718{,}054+84{,}788{,}206
=\boxed{290{,}506{,}260}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-9{,}932=\boxed{61{,}928}
\]

support-twenty selectors remain active.

The next nonempty tier has multiplicity seven: 100 signatures containing 700
selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity8.cpp \
  -o /tmp/m8

# Full transcript, aggregate assertions, and transcript digest.
/tmp/m8

# Optional independently reproducible single cases/orientations.
/tmp/m8 34 0
/tmp/m8 174 3
```

The full run asserts the radius-layer sizes, the 277-signature histogram, exact
aggregate top and bottom counts, absence of every candidate embedding, and the
complete transcript digest.
