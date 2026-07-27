# Exact `(5,2)` radius-three support-twenty signature histogram and low-multiplicity frontier

The multiplicity-four and higher tiers were completed in PX799, leaving multiplicity three as the next exact frontier. PX936--PX939 now close that tier. This chapter records the complete top-signature histogram and identifies the exact residual cache.

This is a finite classification statement for one side-seven product host. It is not an infinite product theorem and not a proof of the no-three-in-line conjecture.

## 1. Exact signature histogram

### Theorem PX940 -- PROVED FINITE

The radius-three support-twenty layer contains exactly `71,860` selectors grouped into `38,553` top signatures with the following multiplicities.

| Multiplicity | Signatures | Selectors |
|---:|---:|---:|
| 1 | 26,579 | 26,579 |
| 2 | 3,840 | 7,680 |
| 3 | 3,544 | 10,632 |
| 4 | 2,392 | 9,568 |
| 5 | 725 | 3,625 |
| 6 | 524 | 3,144 |
| 7 | 100 | 700 |
| 8 | 277 | 2,216 |
| 9 | 64 | 576 |
| 10 | 164 | 1,640 |
| 12 | 128 | 1,536 |
| 13 | 48 | 624 |
| 14 | 40 | 560 |
| 15 | 2 | 30 |
| 16 | 38 | 608 |
| 19 | 42 | 798 |
| 20 | 1 | 20 |
| 23 | 10 | 230 |
| 24 | 8 | 192 |
| 26 | 6 | 156 |
| 27 | 6 | 162 |
| 32 | 3 | 96 |
| 35 | 2 | 70 |
| 38 | 3 | 114 |
| 40 | 3 | 120 |
| 46 | 4 | 184 |
| **Total** | **38,553** | **71,860** |

The verifier regenerates the exact layer from the canonical centre state, groups states by their seven-row top signature, asserts every histogram entry, and checks both totals.

## 2. Complete classification above multiplicity two

### Corollary PX941 -- PROVED CLASSIFICATION

The selectors of multiplicity at least three total

\[
71{,}860-(26{,}579+7{,}680)=\boxed{37{,}601}.
\]

PX799 classified multiplicity four and every higher tier, with one constructive multiplicity-four selector and all other selectors infeasible. PX936--PX939 classify all `10,632` multiplicity-three selectors as infeasible. Therefore every selector of multiplicity at least three is classified:

- `37,600` are certified infeasible in every radix orientation;
- one multiplicity-four selector is constructively feasible.

No selector of multiplicity at least three remains open.

## 3. Exact residual cache

### Corollary PX942 -- PROVED REDUCTION

The unresolved cache consists exactly of:

| Tier | Signatures | Selectors |
|---:|---:|---:|
| Multiplicity one | 26,579 | 26,579 |
| Multiplicity two | 3,840 | 7,680 |
| **Total** | **30,419** | **34,259** |

Thus the arithmetic remainder from PX939 is not merely a count: it is precisely the union of the multiplicity-one and multiplicity-two tiers.

## 4. Low-multiplicity solver reduction

### Corollary PX943 -- PROVED REDUCTION

For every remaining top signature, the shared bottom solver starts with an active selector mask of size one or two. Consequently the remaining finite classification no longer needs a large same-signature selector cache:

- multiplicity one is a direct coordinate-feasibility problem for one candidate selector;
- multiplicity two is a two-candidate shared coordinate-feasibility problem;
- the generic tier-shard engine already supports both tiers by setting the multiplicity parameter to `1` or `2`.

This reduction does not make the total computation small: multiplicity one contains `26,579` separate signatures. It does identify the exact next executable target, namely a multiplicity-two pilot followed by a cost audit before committing to the much larger multiplicity-one census.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_signature_histogram.cpp \
  -o /tmp/side-seven-histogram

/tmp/side-seven-histogram
```

To measure a low-multiplicity shard independently:

```bash
g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_tier_shard.cpp \
  -o /tmp/measure-tier

/tmp/measure-tier 0 100 2
/tmp/measure-tier 0 100 1
```

The first command targets multiplicity two; the second targets multiplicity one. A successful run emits exact aggregate counts and a deterministic transcript digest, while any feasible selector terminates the run immediately.
