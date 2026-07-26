# Exact `(5,2)` radius-three support-twenty multiplicity-26 obstruction

PX617--PX620 close the six multiplicity-27 top-signature classes in the exact
`(5,2)` radius-three support-twenty layer. This chapter closes the next tier.

## 1. Exact multiplicity-26 signatures

For a selector `F`, let

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6)
\]

be its top half-signature.

### Theorem PX621 -- PROVED FINITE

Exactly six top signatures have multiplicity `26`:

\[
\begin{aligned}
\sigma_0&=(3,260,520,3072,144,8224,4160),\\
\sigma_1&=(3,768,12,1040,2176,8224,4160),\\
\sigma_2&=(130,768,12,3072,17,8224,4160),\\
\sigma_3&=(257,6,520,1040,2176,8224,4160),\\
\sigma_4&=(384,6,520,3072,17,8224,4160),\\
\sigma_5&=(384,514,12,1040,2049,8224,4160).
\end{aligned}
\]

They contain

\[
6\cdot26=\boxed{156}
\]

selectors.

### Proof

Regenerate the exact radius-three support-twenty layer and group its `71,860`
selectors by their first seven row masks. The exact half-signature histogram
contains six and only six classes of size `26`; sorting their keys gives the
displayed tuples. \(\square\)

## 2. Exact shared-top search

### Theorem PX622 -- PROVED FINITE

The exact clean-top counts are:

| Signature | Concatenated top orders | Interleaved top orders | Concatenated top nodes | Interleaved top nodes |
|---|---:|---:|---:|---:|
| `sigma_0` | 19,260 | 15,580 | 292,664 | 184,330 |
| `sigma_1` | 59,216 | 25,200 | 514,288 | 272,702 |
| `sigma_2` | 60,976 | 1,792 | 462,542 | 30,224 |
| `sigma_3` | 13,940 | 11,872 | 241,259 | 193,612 |
| `sigma_4` | 67,312 | 73,184 | 561,806 | 627,318 |
| `sigma_5` | 21,100 | 30,176 | 201,992 | 251,256 |

## 3. Exact infeasibility

### Theorem PX623 -- PROVED FINITE

All `156` selectors fail in every radix orientation. The exact shared
bottom-CSP node totals are:

| Signature | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---|---:|---:|---:|---:|---:|
| `sigma_0` | 64,725 | 55,690 | 67,268 | 54,599 | 242,282 |
| `sigma_1` | 236,345 | 97,461 | 227,240 | 111,101 | 672,147 |
| `sigma_2` | 220,331 | 7,520 | 256,239 | 9,443 | 493,533 |
| `sigma_3` | 50,293 | 46,838 | 52,645 | 47,190 | 196,966 |
| `sigma_4` | 248,093 | 270,765 | 242,528 | 294,320 | 1,055,706 |
| `sigma_5` | 72,872 | 110,350 | 70,774 | 106,494 | 360,490 |
| **Total** | **892,659** | **588,624** | **916,694** | **623,147** | **3,021,124** |

No clean top order and bottom-row permutation leaves an active selector.

### Proof

For each signature, regenerate its exact `26`-selector group. Enumerate and
assert the clean-top order and node counts in both column-radix modes. For each
of the four orientations, run the active-selector bottom recursion over every
clean top ordering. Every exact tree is exhausted without a survivor, and the
node totals sum to `3,021,124`. \(\square\)

## 4. Revised cache boundary

### Corollary PX624 -- PROVED REDUCTION

The cache tiers through multiplicity `27` contain `746` selectors. Adding the
multiplicity-26 tier gives

\[
746+156=\boxed{902}
\]

certified-infeasible support-twenty selectors, using cumulatively

\[
9{,}907{,}392+3{,}021{,}124
=\boxed{12{,}928{,}516}
\]

shared bottom-CSP nodes. The active count is therefore

\[
71{,}860-902=\boxed{70{,}958}.
\]

There is no multiplicity-25 tier. The next tier has multiplicity `24`: eight
signatures and `192` selectors.

This remains a finite cache obstruction, not a global infeasibility theorem.

## 5. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity26.cpp \
  -o /tmp/side7_c52_s20_m26
```

and run all twenty-four exact cases:

```bash
for case_index in 0 1 2 3 4 5; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m26 "$case_index" "$orientation"
  done
done
```

Every case regenerates the complete selector layer, verifies that the
multiplicity-26 histogram consists of exactly six signatures, checks the
selected signature group, and asserts the exact top and bottom search counts
using integer determinants on `[14]^2`.
