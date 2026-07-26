# Exact shared-top obstruction for multiplicity thirty-eight

PX599--PX604 reject the top-signature tiers of multiplicities `46` and `40` in
the `(5,2)` radius-three support-twenty layer.  The next tier consists of three
signatures, each occurring `38` times.

The signatures are

```text
3   260 1536 2056 144  8224 4160
130 768 1028 2056 17   8224 4160
384 514 1028 24   2049 8224 4160
```

## 1. Exact coordinate ledgers

### Theorem PX605 -- PROVED FINITE

The exact clean top-order and shared bottom-CSP ledgers are:

| Signature | Concatenated top orders | Interleaved top orders | Orientation 0 nodes | Orientation 1 nodes | Orientation 2 nodes | Orientation 3 nodes |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 21,100 | 30,176 | 85,444 | 127,036 | 83,492 | 125,489 |
| 1 | 13,940 | 11,872 | 55,872 | 52,049 | 60,201 | 53,792 |
| 2 | 19,260 | 15,580 | 75,801 | 66,119 | 78,992 | 63,386 |

The exact top-search node pairs `(concatenated, interleaved)` are

```text
(314266, 335342)
(137462, 115592)
(163726, 149218)
```

### Theorem PX606 -- PROVED FINITE

None of the

\[
3\cdot38=\boxed{114}
\]

selectors in this tier has a no-three coordinate embedding in any radix
orientation.  The shared bottom-search total is

\[
421{,}461+221{,}914+284{,}298
=
\boxed{927{,}673}.
\]

## 2. Cumulative boundary

### Corollary PX607 -- PROVED REDUCTION

The shared-top cache has now rejected

\[
304+114=\boxed{418}
\]

support-twenty selectors after

\[
3{,}472{,}655+927{,}673
=
\boxed{4{,}400{,}328}
\]

shared bottom-CSP nodes.  The open support-twenty count is therefore

\[
71{,}860-418=\boxed{71{,}442}.
\]

### Corollary PX608 -- PROVED FINITE/REDUCTION

The next unprocessed multiplicity tier consists of exactly two top signatures,
each occurring `35` times:

```text
3   768 1028 24   2176 8224 4160
384 6   1536 2056 17   8224 4160
```

They form a 70-selector exact next target.  As before, no unproved scalar-grid
symmetry is used to identify the two cases.

This remains a finite local obstruction.  It does not prove that the remaining
support-twenty selectors, the `(5,2)` canonical class, universal
`2 x 7 -> 14`, or exact all-side closure are impossible.

## 3. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity38.cpp \
  -o /tmp/side7_c52_r3_s20_m38
```

Run every signature case `0..2` in every orientation `0..3`:

```bash
/tmp/side7_c52_r3_s20_m38 CASE ORIENTATION
```

The verifier regenerates the exact support-twenty layer and signature class,
checks the recorded top-order count and top-search node count, and asserts the
shared bottom-CSP total with exact integer collinearity.
