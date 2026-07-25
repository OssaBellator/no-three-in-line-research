# Exact cross-half obstruction profile for four side-seven selectors

PX505 proves that none of the four centre abstract selectors has a complete
no-three coordinate embedding.  This chapter locates that failure more
precisely.  For most coordinate pairs which make the top seven scalar rows
no-three, there is also a bottom-row ordering which makes the bottom seven rows
no-three in isolation.  The unavoidable obstruction is therefore a triple
meeting both halves.

Throughout, fix one of the four abstract selectors from PX505.  For a radix
orientation and column permutations `A_0,A_1`, let `U(A_0,A_1)` be the fourteen
selected points in the top seven scalar rows.  For a bottom-row permutation
`R`, let `L(A_0,A_1,R)` be the fourteen selected points in the bottom seven
rows.

## 1. Clean top-half embeddings

### Theorem PX508 -- PROVED FINITE

The number of ordered column-permutation pairs

\[
(A_0,A_1)\in S_7^2
\]

for which `U(A_0,A_1)` has no real-collinear triple is:

| Relative type | `cc` | `cf` | `fc` | `ff` | Total |
|---|---:|---:|---:|---:|---:|
| `(7)` | 30,972 | 55,312 | 30,972 | 55,312 | 172,568 |
| `(5,2)` | 16,644 | 17,170 | 16,644 | 17,170 | 67,628 |
| `(4,3)` | 22,264 | 88,712 | 22,264 | 88,712 | 221,952 |
| `(3,2,2)` | 142,224 | 90,128 | 142,224 | 90,128 | 464,704 |
| **Total** |  |  |  |  | **926,852** |

### Proof

Enumerate all `7!^2` ordered pairs in each class and orientation.  The top row
order is gauge-fixed, so every top point is determined by `A_0,A_1`.  Test all
`binom(14,3)=364` triples by exact integer determinant.  The verifier asserts
the sixteen displayed counts. \(\square\)

The equality between `cc` and `fc`, and between `cf` and `ff`, is expected:
the first orientation letter only changes the unused bottom-row embedding when
the top half is considered alone.

## 2. Separately clean bottom halves

For a top-clean pair `(A_0,A_1)`, call it **half-compatible** if there exists at
least one `R in S_7` such that `L(A_0,A_1,R)` is no-three in isolation.

### Theorem PX509 -- PROVED FINITE

The exact half-compatible counts are:

| Relative type | `cc` | `cf` | `fc` | `ff` | Total |
|---|---:|---:|---:|---:|---:|
| `(7)` | 23,743 | 43,448 | 23,743 | 43,448 | 134,382 |
| `(5,2)` | 14,928 | 14,797 | 14,928 | 14,797 | 59,450 |
| `(4,3)` | 20,804 | 80,614 | 20,804 | 80,614 | 202,836 |
| `(3,2,2)` | 125,184 | 79,756 | 125,184 | 79,756 | 409,880 |
| **Total** |  |  |  |  | **806,548** |

Thus more than

\[
\frac{806{,}548}{926{,}852}>0.87
\]

of the top-clean column pairs admit a separately clean bottom half.

### Proof

For every pair counted by PX508, expose the seven bottom abstract rows.  Branch
on the unused value of `R(z)` and reject immediately when either new bottom
point completes a bottom-only collinear triple.  This exhausts `S_7` with
exact determinant pruning and records whether at least one bottom-clean
ordering exists.  The sixteen counts are asserted by the verifier. \(\square\)

## 3. The obstruction is cross-half

### Corollary PX510 -- PROVED FINITE

For every one of the 806,548 half-compatible column pairs, choose any bottom-row
permutation `R` for which the bottom half is no-three.  Then the complete
28-point state contains a collinear triple meeting both the top and bottom
halves.

Equivalently, the failure of these coordinate assignments is neither a top-only
nor a bottom-only defect.

### Proof

PX508 and PX509 make the two halves separately no-three.  PX505 proves that no
choice of `A_0,A_1,R` gives a complete no-three embedding of the fixed selector.
Therefore every such union has a bad triple, and that triple must meet both
halves. \(\square\)

### Corollary PX511 -- PROVED REDUCTION

For the four centre selectors, improving the separate geometry of either half
cannot close the side-seven problem.  The remaining obstruction is an exact
cross-half hitting problem over triples of one of the two forms

\[
2\text{ top}+1\text{ bottom},
\qquad
1\text{ top}+2\text{ bottom}.
\]

The next selector move must alter the incidence pattern of these mixed triples,
not merely reorder a fixed selector's coordinates.

This is still a statement about four selectors, not all 9,991,170 abstract
spanning degree-two selectors in the four relative classes.

## Verification

Compile and run the four cases independently:

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_cross_half_profile.cpp -o /tmp/side7_cross_half
/tmp/side7_cross_half cycle7
/tmp/side7_cross_half cycle52
/tmp/side7_cross_half cycle43
/tmp/side7_cross_half cycle322
```

The verifier asserts all top-clean and half-compatible counts using integer
determinants.  Complete nonembeddability is independently checked by
`verify_product_side_seven_selector_coordinate_csp.cpp`.