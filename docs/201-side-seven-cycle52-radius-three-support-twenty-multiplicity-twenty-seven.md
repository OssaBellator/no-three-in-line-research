# Exact `(5,2)` radius-three support-twenty multiplicity-27 obstruction

PX613--PX616 close the three multiplicity-32 top-signature classes in the exact
`(5,2)` radius-three support-twenty layer. This chapter closes the next tier.

## 1. Exact multiplicity-27 signatures

For a selector `F`, let

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6)
\]

be its top half-signature.

### Theorem PX617 -- PROVED FINITE

Exactly six top signatures have multiplicity `27`:

\[
\begin{aligned}
\sigma_0&=(3,260,1028,2056,144,8224,4160),\\
\sigma_1&=(3,768,1536,2056,144,8224,4160),\\
\sigma_2&=(257,6,520,2056,144,8224,4160),\\
\sigma_3&=(257,514,1028,1040,2176,8224,4160),\\
\sigma_4&=(384,514,1028,24,17,8224,4160),\\
\sigma_5&=(384,514,1028,2056,2049,8224,4160).
\end{aligned}
\]

They contain

\[
6\cdot27=\boxed{162}
\]

selectors.

### Proof

Regenerate the exact radius-three support-twenty layer and group its `71,860`
selectors by their first seven row masks. The exact half-signature histogram
contains six and only six classes of size `27`; sorting their keys gives the
displayed tuples. \(\square\)

## 2. Exact shared-top search

The PX595 shared-top recursion enumerates every clean top column ordering once
per signature and then searches bottom row orders while retaining a bitset of
active selectors. A selector is removed exactly when it contains all cells of
a newly completed integer-collinear host triple.

### Theorem PX618 -- PROVED FINITE

The exact clean-top counts are:

| Signature | Concatenated top orders | Interleaved top orders | Concatenated top nodes | Interleaved top nodes |
|---|---:|---:|---:|---:|
| `sigma_0` | 31,274 | 26,546 | 163,792 | 134,476 |
| `sigma_1` | 25,584 | 30,758 | 427,366 | 424,094 |
| `sigma_2` | 35,692 | 32,214 | 183,834 | 165,022 |
| `sigma_3` | 33,226 | 29,406 | 434,895 | 361,174 |
| `sigma_4` | 11,410 | 53,404 | 55,598 | 216,746 |
| `sigma_5` | 32,020 | 31,082 | 384,624 | 316,697 |

## 3. Exact infeasibility

### Theorem PX619 -- PROVED FINITE

All `162` selectors fail in every radix orientation. The exact shared
bottom-CSP node totals are:

| Signature | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---|---:|---:|---:|---:|---:|
| `sigma_0` | 90,698 | 80,652 | 90,973 | 77,237 | 339,560 |
| `sigma_1` | 69,440 | 94,072 | 76,673 | 89,729 | 329,914 |
| `sigma_2` | 105,592 | 103,293 | 116,743 | 91,975 | 417,603 |
| `sigma_3` | 96,453 | 90,592 | 108,737 | 82,563 | 378,345 |
| `sigma_4` | 32,878 | 165,930 | 35,023 | 133,296 | 367,127 |
| `sigma_5` | 98,312 | 102,568 | 93,107 | 85,488 | 379,475 |
| **Total** | **493,373** | **637,107** | **521,256** | **560,288** | **2,212,024** |

No clean top order and bottom-row permutation leaves an active selector.

### Proof

For each signature, regenerate its exact `27`-selector group. Enumerate and
assert the clean-top order and node counts in both column-radix modes. For each
of the four orientations, run the active-selector bottom recursion over every
clean top ordering. Every exact tree is exhausted without a survivor, and the
node totals sum to `2,212,024`. \(\square\)

## 4. Revised cache boundary

### Corollary PX620 -- PROVED REDUCTION

The cache tiers through multiplicity `32` contain `584` selectors. Adding the
multiplicity-27 tier gives

\[
584+162=\boxed{746}
\]

certified-infeasible support-twenty selectors, using cumulatively

\[
7{,}695{,}368+2{,}212{,}024
=\boxed{9{,}907{,}392}
\]

shared bottom-CSP nodes. The active count is therefore

\[
71{,}860-746=\boxed{71{,}114}.
\]

The next tier has multiplicity `26`: six signatures and `156` selectors.

This remains a finite cache obstruction, not a global infeasibility theorem.

## 5. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity27.cpp \
  -o /tmp/side7_c52_s20_m27
```

and run all twenty-four exact cases:

```bash
for case_index in 0 1 2 3 4 5; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m27 "$case_index" "$orientation"
  done
done
```

Every case regenerates the complete selector layer, verifies that the
multiplicity-27 histogram consists of exactly six signatures, checks the
selected signature group, and asserts the exact top and bottom search counts
using integer determinants on `[14]^2`.
