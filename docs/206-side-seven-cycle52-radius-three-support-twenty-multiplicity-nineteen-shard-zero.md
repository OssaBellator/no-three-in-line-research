# Exact `(5,2)` radius-three support-twenty multiplicity-19 shard zero

PX633--PX636 close the multiplicity-20 tier.  The next nonempty tier has
forty-two top signatures of multiplicity nineteen.  This chapter closes the
lexicographically first seventeen signatures.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard

For a selector `F`, write

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6)
\]

for its first seven row masks.

### Theorem PX637 -- PROVED FINITE

The exact radius-three support-twenty layer contains forty-two top signatures
of multiplicity `19`, hence `798` selectors in that tier.  The first shard
consists of the following seventeen signatures and contains

\[
17\cdot19=\boxed{323}
\]

selectors.

| Case | Top signature |
|---:|---|
| `0` | `(3, 6, 520, 3072, 144, 8224, 4160)` |
| `1` | `(3, 6, 1536, 2056, 144, 8224, 4160)` |
| `2` | `(3, 260, 12, 3072, 144, 8224, 4160)` |
| `3` | `(3, 260, 1536, 24, 2176, 8224, 4160)` |
| `4` | `(3, 514, 12, 1040, 2176, 8224, 4160)` |
| `5` | `(3, 514, 1028, 24, 2176, 8224, 4160)` |
| `6` | `(3, 768, 12, 1040, 144, 8224, 4160)` |
| `7` | `(3, 768, 12, 3072, 17, 8224, 4160)` |
| `8` | `(3, 768, 12, 3072, 2176, 8224, 4160)` |
| `9` | `(3, 768, 520, 3072, 144, 8224, 4160)` |
| `10` | `(3, 768, 1028, 3072, 144, 8224, 4160)` |
| `11` | `(130, 260, 1536, 2056, 17, 8224, 4160)` |
| `12` | `(130, 514, 12, 3072, 17, 8224, 4160)` |
| `13` | `(130, 768, 12, 3072, 144, 8224, 4160)` |
| `14` | `(130, 768, 1028, 24, 2049, 8224, 4160)` |
| `15` | `(257, 6, 12, 1040, 2176, 8224, 4160)` |
| `16` | `(257, 6, 520, 1040, 144, 8224, 4160)` |

### Proof

Regenerate the exact alternating-cycle radius layers around the canonical
`(5,2)` centre.  Their sizes are `364`, `26,550`, and `71,860`.  Restrict the
third layer to support twenty and group by the first seven row masks.  The
histogram has exactly forty-two classes of size nineteen.  Sorting the keys
lexicographically gives the displayed first seventeen classes. \(\square\)

## 2. Exact clean-top searches

### Theorem PX638 -- PROVED FINITE

For each signature, the exact clean-top counts and top-search node counts are:

| Case | Concatenated orders | Interleaved orders | Concatenated nodes | Interleaved nodes |
|---:|---:|---:|---:|---:|
| `0` | 21,272 | 42,564 | 149,520 | 214,954 |
| `1` | 31,166 | 30,306 | 193,233 | 170,186 |
| `2` | 55,036 | 9,972 | 261,172 | 53,440 |
| `3` | 52,144 | 33,808 | 573,864 | 293,184 |
| `4` | 25,924 | 41,392 | 136,961 | 191,481 |
| `5` | 37,556 | 47,164 | 183,128 | 213,446 |
| `6` | 62,336 | 9,664 | 255,364 | 51,184 |
| `7` | 116,576 | 544 | 484,004 | 9,877 |
| `8` | 85,328 | 13,576 | 948,024 | 225,094 |
| `9` | 30,348 | 7,652 | 549,858 | 160,612 |
| `10` | 37,968 | 8,860 | 511,726 | 157,038 |
| `11` | 27,448 | 23,068 | 273,950 | 275,810 |
| `12` | 66,208 | 7,944 | 286,906 | 38,872 |
| `13` | 51,632 | 7,008 | 613,698 | 164,898 |
| `14` | 22,568 | 36,760 | 190,132 | 291,461 |
| `15` | 19,364 | 31,316 | 118,638 | 163,975 |
| `16` | 32,322 | 31,070 | 162,622 | 150,854 |
| **Total** | **775,196** | **382,668** | **5,892,800** | **2,826,366** |

The search uses the exact two-permutation all-different constraints and rejects
a partial top assignment immediately when its completed top points contain an
integer-collinear triple.

## 3. Exact shared bottom CSP

### Theorem PX639 -- PROVED FINITE

Every one of the `323` selectors fails in every radix orientation.  The shared
active-selector bottom-CSP node counts are:

| Case | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---:|---:|---:|---:|---:|---:|
| `0` | 56,952 | 124,843 | 63,773 | 112,559 | 358,127 |
| `1` | 87,205 | 94,509 | 92,258 | 90,231 | 364,203 |
| `2` | 153,133 | 25,972 | 170,103 | 30,441 | 379,649 |
| `3` | 191,948 | 129,694 | 192,464 | 126,010 | 640,116 |
| `4` | 73,238 | 113,035 | 78,764 | 108,292 | 373,329 |
| `5` | 98,899 | 141,939 | 110,661 | 127,132 | 478,631 |
| `6` | 177,311 | 28,868 | 178,942 | 30,291 | 415,412 |
| `7` | 339,224 | 1,843 | 328,017 | 1,676 | 670,760 |
| `8` | 252,796 | 44,194 | 259,904 | 44,912 | 601,806 |
| `9` | 74,758 | 23,104 | 83,321 | 24,473 | 205,656 |
| `10` | 105,637 | 29,840 | 114,220 | 27,695 | 277,392 |
| `11` | 94,865 | 79,638 | 98,836 | 84,119 | 357,458 |
| `12` | 171,316 | 23,290 | 199,147 | 22,604 | 416,357 |
| `13` | 136,457 | 20,504 | 142,988 | 20,739 | 320,688 |
| `14` | 77,691 | 124,670 | 77,368 | 128,751 | 408,480 |
| `15` | 53,243 | 88,408 | 61,444 | 87,809 | 290,904 |
| `16` | 91,366 | 100,975 | 90,784 | 79,183 | 362,308 |
| **Total** | **2,236,039** | **1,195,326** | **2,342,994** | **1,146,917** | **6,921,276** |

### Proof

For one top signature, all nineteen selectors have the same top edges.  For
each clean top order, retain a nineteen-bit active-selector mask.  Assign the
bottom row permutation by minimum remaining values.  Whenever a bottom row is
positioned, check every newly completed integer triple and clear exactly the
selector bits containing all three abstract edges.  A branch terminates when
its active mask is zero.  Every exact tree is exhausted without a surviving
bit, and the asserted node counts sum to `6,921,276`. \(\square\)

## 4. Hoisted incidence implementation

The verifier improves the earlier tier scripts without changing their search
tree.  Selector-to-edge incidence masks and the four host edges of each bottom
abstract row are constructed once per signature, not once per clean top order.
For each top order it then constructs fixed scalar point tables; recursive
nodes use stack arrays rather than dynamic vectors.

This is an implementation optimization, not a pruning assumption.  The active
mask after every partial bottom assignment is still exactly the set of
selectors containing no completed collinear triple.  The multiplicity-20 case
was used as a regression test: the optimized engine reproduces all published
top counts and all four published bottom-node counts exactly.

## 5. Revised cache boundary

### Corollary PX640 -- PROVED REDUCTION

The previous cache rejected `1,344` selectors in `20,687,852` shared bottom-CSP
nodes.  Adding this shard gives

\[
1{,}344+323=\boxed{1{,}667}
\]

certified-infeasible support-twenty selectors and

\[
20{,}687{,}852+6{,}921{,}276
=\boxed{27{,}609{,}128}
\]

shared bottom-CSP nodes.  The active support-twenty count is therefore

\[
71{,}860-1{,}667=\boxed{70{,}193}.
\]

Twenty-five multiplicity-19 signatures containing `475` selectors remain in
this tier.

## 6. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity19_shard0.cpp \
  -o /tmp/side7_c52_s20_m19_s0
```

Run cases independently:

```bash
for case_index in $(seq 0 16); do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m19_s0 "$case_index" "$orientation"
  done
done
```

Each invocation regenerates the complete selector layer, verifies that the
multiplicity-19 histogram contains exactly forty-two signatures, checks the
selected nineteen-element group, and asserts the exact top and bottom search
counts using integer determinants on `[14]^2`.