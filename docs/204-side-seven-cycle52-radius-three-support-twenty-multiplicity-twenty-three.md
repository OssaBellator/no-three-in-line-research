# Exact `(5,2)` radius-three support-twenty multiplicity-23 obstruction

PX625--PX628 close the eight multiplicity-24 top-signature classes in the exact
`(5,2)` radius-three support-twenty layer. This chapter closes the next tier.

## 1. Exact multiplicity-23 signatures

For a selector `F`, let

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6)
\]

be its top half-signature.

### Theorem PX629 -- PROVED FINITE

Exactly ten top signatures have multiplicity `23`:

\[
\begin{aligned}
\sigma_0&=(3,768,12,2056,144,8224,4160),\\
\sigma_1&=(3,768,1028,24,144,8224,4160),\\
\sigma_2&=(3,768,1028,2056,17,8224,4160),\\
\sigma_3&=(3,768,1028,2056,2176,8224,4160),\\
\sigma_4&=(130,514,1028,2056,17,8224,4160),\\
\sigma_5&=(130,768,1028,2056,144,8224,4160),\\
\sigma_6&=(384,6,1028,2056,17,8224,4160),\\
\sigma_7&=(384,514,1028,3072,17,8224,4160),\\
\sigma_8&=(384,514,1536,2056,17,8224,4160),\\
\sigma_9&=(384,768,1028,2056,17,8224,4160).
\end{aligned}
\]

They contain

\[
10\cdot23=\boxed{230}
\]

selectors.

### Proof

Regenerate the exact radius-three support-twenty layer and group its `71,860`
selectors by their first seven row masks. The exact half-signature histogram
contains ten and only ten classes of size `23`; sorting their keys gives the
displayed tuples. \(\square\)

## 2. Exact shared-top search

### Theorem PX630 -- PROVED FINITE

The exact clean-top counts are:

| Signature | Concatenated top orders | Interleaved top orders | Concatenated top nodes | Interleaved top nodes |
|---|---:|---:|---:|---:|
| `sigma_0` | 62,984 | 8,044 | 252,322 | 44,882 |
| `sigma_1` | 49,904 | 54,940 | 208,776 | 231,368 |
| `sigma_2` | 24,924 | 5,144 | 119,531 | 33,295 |
| `sigma_3` | 51,408 | 58,392 | 612,490 | 607,628 |
| `sigma_4` | 18,558 | 16,388 | 88,736 | 79,005 |
| `sigma_5` | 17,716 | 20,802 | 262,452 | 322,809 |
| `sigma_6` | 35,452 | 44,968 | 156,332 | 199,678 |
| `sigma_7` | 53,884 | 60,084 | 534,432 | 490,688 |
| `sigma_8` | 30,972 | 55,312 | 308,770 | 631,100 |
| `sigma_9` | 9,576 | 42,788 | 131,306 | 391,446 |

## 3. Exact infeasibility

### Theorem PX631 -- PROVED FINITE

All `230` selectors fail in every radix orientation. The exact shared
bottom-CSP node totals are:

| Signature | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---|---:|---:|---:|---:|---:|
| `sigma_0` | 189,222 | 22,160 | 190,535 | 28,644 | 430,561 |
| `sigma_1` | 144,788 | 169,221 | 138,762 | 168,853 | 621,624 |
| `sigma_2` | 72,433 | 15,741 | 68,225 | 14,850 | 171,249 |
| `sigma_3` | 149,391 | 184,363 | 149,440 | 166,031 | 649,225 |
| `sigma_4` | 49,110 | 49,117 | 52,976 | 44,016 | 195,219 |
| `sigma_5` | 48,712 | 64,260 | 49,375 | 51,862 | 214,209 |
| `sigma_6` | 91,837 | 130,271 | 98,041 | 126,902 | 447,051 |
| `sigma_7` | 156,287 | 191,739 | 161,827 | 168,621 | 678,474 |
| `sigma_8` | 90,223 | 163,336 | 101,404 | 157,072 | 512,035 |
| `sigma_9` | 27,210 | 133,895 | 32,130 | 115,158 | 308,393 |
| **Total** | **1,019,213** | **1,124,103** | **1,042,715** | **1,042,009** | **4,228,040** |

No clean top order and bottom-row permutation leaves an active selector.

### Proof

For each signature, regenerate its exact `23`-selector group. Enumerate and
assert the clean-top order and node counts in both column-radix modes. For each
of the four orientations, run the active-selector bottom recursion over every
clean top ordering. Every exact tree is exhausted without a survivor, and the
node totals sum to `4,228,040`. \(\square\)

## 4. Revised cache boundary

### Corollary PX632 -- PROVED REDUCTION

The cache tiers through multiplicity `24` contain `1,094` selectors. Adding the
multiplicity-23 tier gives

\[
1{,}094+230=\boxed{1{,}324}
\]

certified-infeasible support-twenty selectors, using cumulatively

\[
16{,}259{,}764+4{,}228{,}040
=\boxed{20{,}487{,}804}
\]

shared bottom-CSP nodes. The active count is therefore

\[
71{,}860-1{,}324=\boxed{70{,}536}.
\]

There are no multiplicity-22 or multiplicity-21 tiers. The next tier has
multiplicity `20`: one signature containing `20` selectors.

This remains a finite cache obstruction, not a global infeasibility theorem.

## 5. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity23.cpp \
  -o /tmp/side7_c52_s20_m23
```

and run all forty exact cases:

```bash
for case_index in 0 1 2 3 4 5 6 7 8 9; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m23 "$case_index" "$orientation"
  done
done
```

Every case regenerates the complete selector layer, verifies that the
multiplicity-23 histogram consists of exactly ten signatures, checks the
selected signature group, and asserts the exact top and bottom search counts
using integer determinants on `[14]^2`.
