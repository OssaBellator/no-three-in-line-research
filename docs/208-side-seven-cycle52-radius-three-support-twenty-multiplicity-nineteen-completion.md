# Exact `(5,2)` radius-three support-twenty multiplicity-19 completion

PX637--PX640 close the first seventeen multiplicity-19 signatures. This chapter closes the remaining twenty-five signatures and therefore the complete tier.

This is a finite obstruction result, not an infinite product theorem.

## 1. Remaining exact shard

### Theorem PX643 -- PROVED FINITE

The lexicographically final twenty-five multiplicity-19 signatures contain

\[
25\cdot19=\boxed{475}
\]

selectors. Together with the first shard, the complete tier contains forty-two signatures and `798` selectors.

| Global case | Top signature |
|---:|---|
| `17` | `(257,6,520,3072,17,8224,4160)` |
| `18` | `(257,6,520,3072,2176,8224,4160)` |
| `19` | `(257,6,1028,24,2176,8224,4160)` |
| `20` | `(257,6,1536,24,144,8224,4160)` |
| `21` | `(257,6,1536,2056,17,8224,4160)` |
| `22` | `(257,6,1536,2056,2176,8224,4160)` |
| `23` | `(257,260,520,3072,144,8224,4160)` |
| `24` | `(257,260,1536,2056,144,8224,4160)` |
| `25` | `(257,514,12,1040,2049,8224,4160)` |
| `26` | `(257,514,520,1040,2176,8224,4160)` |
| `27` | `(257,514,1028,24,2049,8224,4160)` |
| `28` | `(257,514,1536,24,2176,8224,4160)` |
| `29` | `(257,768,12,1040,2176,8224,4160)` |
| `30` | `(257,768,1028,24,2176,8224,4160)` |
| `31` | `(384,6,12,3072,17,8224,4160)` |
| `32` | `(384,6,520,3072,144,8224,4160)` |
| `33` | `(384,6,1536,24,2049,8224,4160)` |
| `34` | `(384,6,1536,2056,144,8224,4160)` |
| `35` | `(384,514,12,1040,17,8224,4160)` |
| `36` | `(384,514,12,1040,2176,8224,4160)` |
| `37` | `(384,514,12,2056,17,8224,4160)` |
| `38` | `(384,514,12,3072,2049,8224,4160)` |
| `39` | `(384,514,520,3072,17,8224,4160)` |
| `40` | `(384,514,1028,24,2176,8224,4160)` |
| `41` | `(384,768,12,3072,17,8224,4160)` |

### Proof

Regenerate the exact alternating-cycle radius layers around the canonical `(5,2)` centre. Their sizes are `364`, `26,550`, and `71,860`. Restrict the third layer to support twenty and group by the first seven row masks. The exact histogram has forty-two classes of size nineteen. Sorting those keys lexicographically gives PX637 shard zero followed by the displayed twenty-five classes. \(\square\)

## 2. Exact clean-top searches

### Theorem PX644 -- PROVED FINITE

For the second shard, the exact clean-top order and top-search node counts are:

| Global case | Concatenated orders | Interleaved orders | Concatenated nodes | Interleaved nodes |
|---:|---:|---:|---:|---:|
| `17` | 59,500 | 55,516 | 280,512 | 251,249 |
| `18` | 12,760 | 44,594 | 355,632 | 686,160 |
| `19` | 39,744 | 9,384 | 197,644 | 59,404 |
| `20` | 88,880 | 7,572 | 372,562 | 54,650 |
| `21` | 56,156 | 33,292 | 252,911 | 184,636 |
| `22` | 27,144 | 10,880 | 526,566 | 269,646 |
| `23` | 19,722 | 21,120 | 442,386 | 352,119 |
| `24` | 20,378 | 21,102 | 379,113 | 397,229 |
| `25` | 17,986 | 17,524 | 90,702 | 81,967 |
| `26` | 27,650 | 21,538 | 462,917 | 377,536 |
| `27` | 18,240 | 20,830 | 86,899 | 101,184 |
| `28` | 67,636 | 9,224 | 868,088 | 236,330 |
| `29` | 64,848 | 24,344 | 796,970 | 374,644 |
| `30` | 74,092 | 39,456 | 718,182 | 463,866 |
| `31` | 87,344 | 92,856 | 362,105 | 330,457 |
| `32` | 29,776 | 39,988 | 510,248 | 644,220 |
| `33` | 65,296 | 1,584 | 515,392 | 60,444 |
| `34` | 39,308 | 7,664 | 543,394 | 192,396 |
| `35` | 20,892 | 68,488 | 97,427 | 243,108 |
| `36` | 37,630 | 25,880 | 463,978 | 305,580 |
| `37` | 20,980 | 64,584 | 95,722 | 228,651 |
| `38` | 75,808 | 46,940 | 779,458 | 399,132 |
| `39` | 50,120 | 63,336 | 507,558 | 540,224 |
| `40` | 56,690 | 7,820 | 516,006 | 106,322 |
| `41` | 48,312 | 11,832 | 483,082 | 127,812 |
| **Total** | **1,126,892** | **767,348** | **10,705,454** | **7,068,966** |

## 3. Exact infeasibility

### Theorem PX645 -- PROVED FINITE

Every one of the `475` selectors fails in every radix orientation. The exact shared bottom-CSP node counts are:

| Global case | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---:|---:|---:|---:|---:|---:|
| `17` | 158,814 | 178,654 | 160,405 | 135,033 | 632,906 |
| `18` | 37,018 | 125,572 | 35,913 | 121,229 | 319,732 |
| `19` | 107,024 | 32,116 | 136,516 | 30,832 | 306,488 |
| `20` | 254,120 | 26,449 | 290,333 | 25,070 | 595,972 |
| `21` | 155,871 | 107,017 | 156,446 | 94,948 | 514,282 |
| `22` | 84,197 | 33,436 | 82,609 | 32,969 | 233,211 |
| `23` | 49,034 | 58,023 | 54,452 | 53,843 | 215,352 |
| `24` | 54,398 | 58,618 | 58,779 | 57,778 | 229,573 |
| `25` | 48,273 | 47,363 | 47,929 | 40,009 | 183,574 |
| `26` | 68,437 | 60,547 | 75,551 | 55,248 | 259,783 |
| `27` | 48,728 | 59,002 | 49,194 | 48,832 | 205,756 |
| `28` | 186,670 | 27,259 | 205,101 | 26,898 | 445,928 |
| `29` | 172,380 | 73,803 | 188,267 | 74,280 | 508,730 |
| `30` | 199,864 | 116,657 | 217,658 | 119,655 | 653,834 |
| `31` | 229,194 | 258,861 | 250,609 | 251,773 | 990,437 |
| `32` | 81,076 | 109,369 | 76,048 | 103,014 | 369,507 |
| `33` | 244,747 | 5,786 | 248,124 | 7,551 | 506,208 |
| `34` | 118,662 | 22,880 | 105,520 | 20,748 | 267,810 |
| `35` | 56,185 | 194,095 | 56,897 | 166,752 | 473,929 |
| `36` | 100,696 | 84,740 | 97,267 | 69,465 | 352,168 |
| `37` | 60,509 | 184,938 | 60,999 | 167,868 | 474,314 |
| `38` | 220,916 | 151,979 | 217,631 | 132,674 | 723,200 |
| `39` | 137,694 | 184,256 | 147,347 | 170,973 | 640,270 |
| `40` | 166,297 | 25,533 | 153,159 | 21,323 | 366,312 |
| `41` | 133,519 | 40,423 | 157,074 | 35,289 | 366,305 |
| **Total** | **3,174,323** | **2,267,376** | **3,329,828** | **2,064,054** | **10,835,581** |

No clean top order and bottom-row permutation leaves an active selector.

### Proof

For each signature, retain a nineteen-bit active-selector mask. The top search enforces the two all-different column permutations and rejects partial assignments containing a completed integer-collinear top triple. For every clean top order, the bottom search assigns the remaining row permutation by minimum remaining values and clears exactly the selector bits containing each newly completed collinear triple. All exact trees terminate with the active mask zero. The standalone verifier asserts every top count and every orientation count. \(\square\)

## 4. Complete multiplicity-19 tier

### Corollary PX646 -- PROVED REDUCTION

Combining both shards, all `798` multiplicity-19 selectors are certified infeasible. The complete tier uses

\[
6{,}921{,}276+10{,}835{,}581=\boxed{17{,}756{,}857}
\]

shared bottom-CSP nodes. Its complete clean-top totals are:

- `1,902,088` concatenated orders and `1,150,016` interleaved orders;
- `16,598,254` concatenated top-search nodes and `9,895,332` interleaved top-search nodes.

The cumulative cache therefore contains

\[
1{,}667+475=\boxed{2{,}142}
\]

certified-infeasible support-twenty selectors after

\[
27{,}609{,}128+10{,}835{,}581=\boxed{38{,}444{,}709}
\]

shared bottom-CSP nodes. The active count is

\[
71{,}860-2{,}142=\boxed{69{,}718}.
\]

There are no multiplicity-18 or multiplicity-17 classes. The next nonempty tier has multiplicity `16`: thirty-eight signatures containing `608` selectors.

## 5. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity19_shard1.cpp \
  -o /tmp/side7_c52_s20_m19_s1
```

Run cases independently:

```bash
for case_index in $(seq 0 24); do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m19_s1 "$case_index" "$orientation"
  done
done
```

Each invocation regenerates the complete selector layer, verifies the forty-two-class multiplicity-19 histogram, checks the selected nineteen-element group, and asserts exact integer-determinant search counts on `[14]^2`.
