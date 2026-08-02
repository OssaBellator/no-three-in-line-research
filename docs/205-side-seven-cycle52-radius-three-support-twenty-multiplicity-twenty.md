# Exact `(5,2)` radius-three support-twenty multiplicity-20 obstruction

PX629--PX632 close the ten multiplicity-23 top-signature classes in the exact
`(5,2)` radius-three support-twenty layer. There are no multiplicity-22 or
multiplicity-21 classes. This chapter closes the next nonempty tier.

## 1. Exact multiplicity-20 signature

For a selector `F`, let

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6)
\]

be its top half-signature.

### Theorem PX633 -- PROVED FINITE

Exactly one top signature has multiplicity `20`:

\[
\boxed{(257,514,1028,2056,144,8224,4160)}.
\]

It contains exactly `20` selectors.

### Proof

Regenerate the exact radius-three support-twenty layer and group its `71,860`
selectors by their first seven row masks. The exact half-signature histogram
contains one and only one class of size `20`, with the displayed key. \(\square\)

## 2. Exact shared-top search

### Theorem PX634 -- PROVED FINITE

The exact clean-top counts are:

| Column-radix mode | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 16,644 | 193,092 |
| Interleaved | 17,170 | 191,228 |

## 3. Exact infeasibility

### Theorem PX635 -- PROVED FINITE

All `20` selectors fail in every radix orientation. The exact shared
bottom-CSP node totals are:

| Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---:|---:|---:|---:|---:|
| 47,979 | 51,334 | 50,510 | 50,225 | **200,048** |

No clean top order and bottom-row permutation leaves an active selector.

### Proof

Regenerate the exact `20`-selector group. Enumerate and assert the clean-top
order and node counts in both column-radix modes. For each of the four
orientations, run the active-selector bottom recursion over every clean top
ordering. Every exact tree is exhausted without a survivor, and the node totals
sum to `200,048`. \(\square\)

## 4. Revised cache boundary

### Corollary PX636 -- PROVED REDUCTION

The cache tiers through multiplicity `23` contain `1,324` selectors. Adding the
multiplicity-20 tier gives

\[
1{,}324+20=\boxed{1{,}344}
\]

certified-infeasible support-twenty selectors, using cumulatively

\[
20{,}487{,}804+200{,}048
=\boxed{20{,}687{,}852}
\]

shared bottom-CSP nodes. The active count is therefore

\[
71{,}860-1{,}344=\boxed{70{,}516}.
\]

The next tier has multiplicity `19`: forty-two signatures containing `798`
selectors.

This remains a finite cache obstruction, not a global infeasibility theorem.

## 5. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity20.cpp \
  -o /tmp/side7_c52_s20_m20
```

and run the four exact cases:

```bash
for orientation in 0 1 2 3; do
  /tmp/side7_c52_s20_m20 "$orientation"
done
```

Every case regenerates the complete selector layer, verifies that the
multiplicity-20 histogram consists of exactly one signature, checks its group,
and asserts the exact top and bottom search counts using integer determinants
on `[14]^2`.
