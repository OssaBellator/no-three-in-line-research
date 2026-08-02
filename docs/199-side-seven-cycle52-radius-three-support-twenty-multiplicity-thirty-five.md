# Exact `(5,2)` radius-three support-twenty multiplicity-35 obstruction

PX592--PX608 develop the exact shared-state cache for the `71,860` selectors in
the `(5,2)` radius-three support-twenty layer and exhaust the top-signature
tiers of multiplicity `46`, `40`, and `38`.  This chapter closes the next tier.

## 1. Exact multiplicity-35 signatures

For a selector `F`, write its top half-signature as

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6),
\]

where each `F_i` is the fourteen-bit row mask of selected abstract columns.

### Theorem PX609 -- PROVED FINITE

Exactly two top signatures occur with multiplicity `35` in the exact
radius-three support-twenty layer.  In lexicographic order they are

\[
\begin{aligned}
\sigma_0&=(3,768,1028,24,2176,8224,4160),\\
\sigma_1&=(384,6,1536,2056,17,8224,4160).
\end{aligned}
\]

They contain exactly

\[
2\cdot35=\boxed{70}
\]

selectors.

### Proof

Regenerate the exact radius-zero, radius-one, radius-two, and radius-three
layers, retain support twenty, and group its `71,860` selectors by the first
seven row masks.  The PX592 half-signature histogram has exactly two classes of
size `35`, and their sorted masks are the two displayed tuples. \(\square\)

## 2. Shared-top coordinate census

For one fixed top signature, the selected top abstract cells are common to all
selectors in the group.  The cache therefore enumerates each no-three top
column ordering `(A_0,A_1)` once.  For each such ordering it searches the bottom
row permutation `R` while retaining a bitset of still-feasible selectors.
Whenever a bottom row becomes complete, a selector is deleted exactly when it
contains all three cells of a newly completed collinear host-cell triple.

This is the exact PX595 shared-top recursion: no selector is deleted without an
integer zero determinant, and every completed bad triple deletes every selector
containing its three cells.

### Theorem PX610 -- PROVED FINITE

The clean top-order counts and top-search node counts are:

| Signature | Concatenated top orders | Interleaved top orders | Concatenated top nodes | Interleaved top nodes |
|---|---:|---:|---:|---:|
| `sigma_0` | 67,312 | 73,184 | 560,622 | 596,164 |
| `sigma_1` | 59,216 | 25,200 | 446,832 | 325,044 |

The two scalar row orientations sharing one column radix use the same clean
`(A_0,A_1)` list, so these lists cover all four radix orientations.

### Theorem PX611 -- PROVED FINITE

Neither multiplicity-35 group has a coordinate embedding in any radix
orientation.  The exact shared bottom-CSP node counts are:

| Signature | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---|---:|---:|---:|---:|---:|
| `sigma_0` | 278,151 | 298,358 | 264,468 | 331,833 | 1,172,810 |
| `sigma_1` | 265,812 | 106,524 | 248,665 | 125,655 | 746,656 |
| **Total** | **543,963** | **404,882** | **513,133** | **457,488** | **1,919,466** |

No top ordering and no bottom-row permutation leaves an active selector.

### Proof

For each displayed signature, regenerate its exact 35-selector group.  For each
of the two column-radix modes, enumerate every clean top ordering and assert the
recorded top-order and top-node counts.  Run the active-selector bottom recursion
for both scalar row orientations.  Every search exhausts its exact tree and
returns no active selector; summing the recorded node totals gives
`1,919,466`. \(\square\)

## 3. Revised support-twenty boundary

### Corollary PX612 -- PROVED REDUCTION

The previously certified cache tiers contain `418` selectors.  Adding the
multiplicity-35 tier gives

\[
418+70=\boxed{488}
\]

certified-infeasible support-twenty selectors.  Hence the active count becomes

\[
71{,}860-488=\boxed{71{,}372}.
\]

The next top-signature tier has multiplicity `32`: exactly three signatures and
`96` selectors.

This is a finite cache obstruction, not a proof that the `(5,2)` canonical host
problem or universal side-seven doubling is globally infeasible.

## 4. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity35.cpp \
  -o /tmp/side7_c52_s20_m35
```

Run the eight exact cases:

```bash
for case_index in 0 1; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m35 "$case_index" "$orientation"
  done
done
```

Each case regenerates the complete selector layer, asserts the signature group,
checks the exact clean-top list, and verifies the recorded shared bottom-CSP
node total using integer determinants on `[14]^2`.