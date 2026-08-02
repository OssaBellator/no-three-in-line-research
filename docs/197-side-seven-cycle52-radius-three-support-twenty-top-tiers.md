# Exact shared-top obstruction for the largest support-twenty signature tiers

PX592--PX598 introduce the exact shared-top cache and reject one top-signature
class of multiplicity `46`.  The support-twenty multiplicity histogram contains
four top signatures of multiplicity `46` and three of multiplicity `40`.  This
chapter exhausts all seven classes.

## 1. Multiplicity forty-six

The four signatures, in lexicographic order, are:

```text
3   768  12   3072 144  8224 4160
257 6    520  3072 144  8224 4160
257 514  12   1040 2176 8224 4160
384 514  12   3072 17   8224 4160
```

### Theorem PX599 -- PROVED FINITE

Their exact clean top-order and shared bottom-search ledgers are:

| Signature | Concatenated top orders | Interleaved top orders | Orientation 0 nodes | Orientation 1 nodes | Orientation 2 nodes | Orientation 3 nodes |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 65,296 | 1,584 | 291,211 | 6,842 | 293,813 | 9,539 |
| 1 | 22,568 | 36,760 | 96,550 | 152,589 | 94,773 | 161,139 |
| 2 | 27,448 | 23,068 | 117,557 | 97,658 | 119,345 | 104,242 |
| 3 | 52,144 | 33,808 | 228,092 | 155,693 | 224,792 | 150,020 |

The corresponding exact top-search node pairs `(concatenated, interleaved)` are

```text
(576716, 39556)
(331714, 420464)
(286467, 265038)
(413174, 202572)
```

### Theorem PX600 -- PROVED FINITE

None of the

\[
4\cdot46=\boxed{184}
\]

selectors in these four classes has a no-three coordinate embedding in any
radix orientation.  Their shared bottom-row recursions visit exactly

\[
601{,}405+505{,}051+438{,}802+758{,}597
=
\boxed{2{,}303{,}855}
\]

nodes.

## 2. Multiplicity forty

The three signatures are:

```text
3   768 1028 2056 144 8224 4160
257 514 12   3072 144 8224 4160
384 514 1028 2056 17  8224 4160
```

### Theorem PX601 -- PROVED FINITE

Their exact ledgers are:

| Signature | Concatenated top orders | Interleaved top orders | Orientation 0 nodes | Orientation 1 nodes | Orientation 2 nodes | Orientation 3 nodes |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 26,364 | 12,620 | 103,599 | 48,299 | 98,432 | 55,778 |
| 1 | 40,392 | 15,248 | 155,054 | 59,694 | 167,938 | 67,590 |
| 2 | 13,624 | 40,276 | 52,378 | 159,792 | 52,825 | 147,421 |

The exact top-search node pairs are

```text
(280846, 152594)
(390380, 166320)
(140786, 331240)
```

### Theorem PX602 -- PROVED FINITE

None of the

\[
3\cdot40=\boxed{120}
\]

selectors in the multiplicity-forty tier embeds.  The shared bottom-search total
is

\[
306{,}108+450{,}276+412{,}416
=
\boxed{1{,}168{,}800}.
\]

## 3. Cumulative support-twenty boundary

### Corollary PX603 -- PROVED REDUCTION

The shared-top cache has now rejected

\[
184+120=\boxed{304}
\]

support-twenty selectors after

\[
2{,}303{,}855+1{,}168{,}800
=
\boxed{3{,}472{,}655}
\]

shared bottom-CSP nodes.  The open `(5,2)` radius-three support-twenty count is
therefore

\[
71{,}860-304=\boxed{71{,}556}.
\]

### Corollary PX604 -- PROVED FINITE/REDUCTION

The next unprocessed multiplicity tier consists of exactly three top signatures,
each occurring `38` times:

```text
3   260 1536 2056 144  8224 4160
130 768 1028 2056 17   8224 4160
384 514 1028 24   2049 8224 4160
```

They form a 114-selector exact next target.  No symmetry identification between
these signatures is assumed, because an abstract host automorphism need not
preserve the fixed scalar top-row geometry.

This remains a finite local obstruction.  It does not prove that the remaining
support-twenty selectors, the `(5,2)` canonical class, universal
`2 x 7 -> 14`, or exact all-side closure are impossible.

## 4. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_top_tiers.cpp \
  -o /tmp/side7_c52_r3_s20_tiers
```

For each case `0..6`, orientation `0..3`, and every embedded shard index, run

```bash
/tmp/side7_c52_r3_s20_tiers CASE ORIENTATION SHARD
```

Cases `0..3` are the multiplicity-46 signatures and cases `4..6` are the
multiplicity-40 signatures.  The verifier regenerates the exact radius-three
support-twenty layer, extracts the recorded signature class, regenerates its
clean top-order list, and asserts the deterministic shared bottom-CSP node
total using integer collinearity on `[14]^2`.
