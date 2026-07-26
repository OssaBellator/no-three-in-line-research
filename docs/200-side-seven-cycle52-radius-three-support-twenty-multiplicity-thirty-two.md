# Exact `(5,2)` radius-three support-twenty multiplicity-32 obstruction

PX609--PX612 close the two multiplicity-35 top-signature classes in the exact
`(5,2)` radius-three support-twenty layer.  This chapter closes the next tier.

## 1. Exact multiplicity-32 signatures

For a selector `F`, let

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6)
\]

be its top half-signature.

### Theorem PX613 -- PROVED FINITE

Exactly three top signatures have multiplicity `32`:

\[
\begin{aligned}
\sigma_0&=(257,6,1536,24,2176,8224,4160),\\
\sigma_1&=(257,6,1536,2056,144,8224,4160),\\
\sigma_2&=(257,514,1028,24,2176,8224,4160).
\end{aligned}
\]

They contain

\[
3\cdot32=\boxed{96}
\]

selectors.

### Proof

Regenerate the exact radius-three support-twenty layer and group its `71,860`
selectors by their first seven row masks.  The exact half-signature histogram
contains three and only three classes of size `32`; sorting their keys gives the
displayed tuples. \(\square\)

## 2. Exact shared-top search

The PX595 shared-top recursion enumerates every clean top column ordering once
per signature and then searches bottom row orders while retaining a bitset of
active selectors.  A selector is removed exactly when it contains all cells of
a newly completed integer-collinear host triple.

### Theorem PX614 -- PROVED FINITE

The exact clean-top counts are:

| Signature | Concatenated top orders | Interleaved top orders | Concatenated top nodes | Interleaved top nodes |
|---|---:|---:|---:|---:|
| `sigma_0` | 60,976 | 1,792 | 647,984 | 72,614 |
| `sigma_1` | 32,028 | 14,076 | 386,563 | 217,668 |
| `sigma_2` | 40,392 | 15,248 | 353,504 | 161,844 |

### Theorem PX615 -- PROVED FINITE

All 96 selectors fail in every radix orientation.  The exact shared bottom-CSP
node totals are:

| Signature | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---|---:|---:|---:|---:|---:|
| `sigma_0` | 257,180 | 9,042 | 291,770 | 10,563 | 568,555 |
| `sigma_1` | 128,632 | 52,616 | 125,609 | 64,029 | 370,886 |
| `sigma_2` | 149,482 | 61,989 | 160,376 | 64,286 | 436,133 |
| **Total** | **535,294** | **123,647** | **577,755** | **138,878** | **1,375,574** |

No clean top order and bottom-row permutation leaves an active selector.

### Proof

For each signature, regenerate its exact 32-selector group.  Enumerate and
assert the clean-top order and node counts in both column-radix modes.  For each
of the four orientations, run the active-selector bottom recursion over every
clean top ordering.  Every exact tree is exhausted without a survivor, and the
node totals sum to `1,375,574`. \(\square\)

## 3. Revised cache boundary

### Corollary PX616 -- PROVED REDUCTION

The cache tiers through multiplicity 35 contain `488` selectors.  Adding the
multiplicity-32 tier gives

\[
488+96=\boxed{584}
\]

certified-infeasible support-twenty selectors, using cumulatively

\[
4{,}400{,}328+1{,}919{,}466+1{,}375{,}574
=\boxed{7{,}695{,}368}
\]

shared bottom-CSP nodes.  The active count is therefore

\[
71{,}860-584=\boxed{71{,}276}.
\]

The next tier has multiplicity `27`: six signatures and `162` selectors.

This remains a finite cache obstruction, not a global infeasibility theorem.

## 4. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity32.cpp \
  -o /tmp/side7_c52_s20_m32
```

and run all twelve exact cases:

```bash
for case_index in 0 1 2; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m32 "$case_index" "$orientation"
  done
done
```

Every case regenerates the complete selector layer, verifies its signature
group, and asserts the exact top and bottom search counts using integer
determinants on `[14]^2`.