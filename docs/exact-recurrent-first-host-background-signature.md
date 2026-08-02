# Lossless background signature for the first-host response menu

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact finite score interface proved; no physical fibre populated.

The first residual host has two unreopened responses and three local reopening
responses:

```text
3012 3210 2031 2310 3201
```

Previous audits showed that intrinsic scores alone are not background-stable.
This chapter replaces the missing background by a finite exact signature that is
sufficient to recover the complete new-triple score of all five responses.

## Signature coordinates

Let `B` be any finite background disjoint from the response being evaluated.
For a response `Q`, let `k_Q(l)` be the number of response points on line `l`.

Across the five-response menu there are exactly:

```text
20 distinct response-secant lines
11 distinct response points
31 signature coordinates in total
```

The coordinates are:

1. `h_B(l)=|B intersect l|` for each of the 20 response-secant lines;
2. `pair_B(q)`, the number of unordered background pairs whose line passes
   through response point `q`, for each of the 11 response points.

## ERL-S4.10 — lossless score identity

For every candidate response `Q` and every finite disjoint background `B`, the
number of new collinear triples containing at least one response point is

```text
score(Q;B)
 = intrinsic(Q)
 + sum_l C(k_Q(l),2) h_B(l)
 + sum_{q in Q} pair_B(q),
```

where the first sum runs over the response-secant lines of `Q`.

### Proof

Partition every new triple by the number of response points it contains.

- Three response points contribute `intrinsic(Q)`.
- Two response points determine one response-secant line `l`; the third point
  can be any of the `h_B(l)` background points on that line. This gives
  `C(k_Q(l),2)h_B(l)`.
- One response point `q` is completed by any background pair collinear with
  `q`, giving `pair_B(q)`.

The cases are disjoint and exhaustive. No assumption that the background is
triple-free is needed because background-only triples are not counted. ∎

## Exact coefficient matrix

The committed manifest stores the full `5 x 31` integer coefficient matrix.
Its exact rational row rank is five. Relative to response `3012`, the four
selector-difference rows have rank four.

Thus the five score functionals are independent on the installed signature, and
no response score is an affine consequence of the other four on arbitrary
background signatures.

## Implementation audit

The checker independently compares the compressed formula with direct triple
enumeration for every background of size at most three drawn from the padded
coordinate domain

```text
{-1,0,1,2,3,4} x {-1,0,1,2,3,4}
```

after removing the eleven candidate response points. This gives exactly

```text
25 available background points
2626 background subsets
13130 response/background score comparisons
```

All comparisons agree. The finite audit is an implementation check; the theorem
itself follows from the triple partition above and applies to every finite
background.

## Why this advances the physical fibre

The first-host background obligation is no longer “store an unspecified
background.” It is enough, for response-score purposes, to populate the exact
31-coordinate signature.

This compression is deliberately limited:

- it determines geometric new-triple scores;
- it does not identify physical owners or deletion causes;
- it does not determine whether restoring `02` or `20` is legal;
- it does not enumerate collateral children or their Lyapunov weights.

A physical-fibre manifest can now be rejected concretely if it omits any
signature coordinate used by a candidate response row.

## Next certificate target

For each physically realizable occurrence of
`s4-75b04c45c1c8eac2`, populate:

```text
20 exact secant-line loads
11 exact background-pair-through-point counts
causes and owners of deletions 02 and 20
installed legal operations
resulting labelled children
parent budget or destroyed load
```

The geometric score vector then follows by exact integer matrix multiplication.
The remaining work is physical provenance and payment, not further local score
ambiguity.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_background_signature.py \
  --check data/exact_recurrent_first_host_background_signature.json
```

The checker rebuilds the coordinate set and coefficient matrix, verifies the two
matrix ranks, performs the 2626-background audit, and rejects eleven mutation
classes. Actual signatures, legal operations, recurrent rows, strict Lyapunov
descent and the all-`n` conclusion remain unproved.
