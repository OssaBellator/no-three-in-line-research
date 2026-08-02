# Exact `(5,2)` radius-three support-twenty multiplicity-24 obstruction

PX621--PX624 close the six multiplicity-26 top-signature classes in the exact
`(5,2)` radius-three support-twenty layer. This chapter closes the next tier.

## 1. Exact multiplicity-24 signatures

For a selector `F`, let

\[
\sigma^+(F)=(F_0,F_1,\ldots,F_6)
\]

be its top half-signature.

### Theorem PX625 -- PROVED FINITE

Exactly eight top signatures have multiplicity `24`:

\[
\begin{aligned}
\sigma_0&=(3,514,12,3072,144,8224,4160),\\
\sigma_1&=(257,6,12,3072,144,8224,4160),\\
\sigma_2&=(257,514,12,1040,144,8224,4160),\\
\sigma_3&=(257,514,12,3072,17,8224,4160),\\
\sigma_4&=(257,514,12,3072,2176,8224,4160),\\
\sigma_5&=(257,514,520,3072,144,8224,4160),\\
\sigma_6&=(257,768,12,3072,144,8224,4160),\\
\sigma_7&=(384,514,12,3072,144,8224,4160).
\end{aligned}
\]

They contain

\[
8\cdot24=\boxed{192}
\]

selectors.

### Proof

Regenerate the exact radius-three support-twenty layer and group its `71,860`
selectors by their first seven row masks. The exact half-signature histogram
contains eight and only eight classes of size `24`; sorting their keys gives the
displayed tuples. \(\square\)

## 2. Exact shared-top search

### Theorem PX626 -- PROVED FINITE

The exact clean-top counts are:

| Signature | Concatenated top orders | Interleaved top orders | Concatenated top nodes | Interleaved top nodes |
|---|---:|---:|---:|---:|
| `sigma_0` | 46,840 | 8,180 | 225,599 | 45,484 |
| `sigma_1` | 42,928 | 45,502 | 219,278 | 207,729 |
| `sigma_2` | 33,226 | 29,406 | 151,745 | 134,252 |
| `sigma_3` | 59,556 | 8,636 | 257,314 | 40,607 |
| `sigma_4` | 45,248 | 38,240 | 597,856 | 470,356 |
| `sigma_5` | 29,724 | 28,890 | 473,244 | 370,472 |
| `sigma_6` | 57,204 | 5,780 | 745,474 | 130,448 |
| `sigma_7` | 48,388 | 39,952 | 566,176 | 510,608 |

## 3. Exact infeasibility

### Theorem PX627 -- PROVED FINITE

All `192` selectors fail in every radix orientation. The exact shared
bottom-CSP node totals are:

| Signature | Orientation 0 | Orientation 1 | Orientation 2 | Orientation 3 | Total |
|---|---:|---:|---:|---:|---:|
| `sigma_0` | 132,228 | 23,431 | 153,912 | 24,908 | 334,479 |
| `sigma_1` | 122,194 | 130,542 | 139,907 | 130,968 | 523,611 |
| `sigma_2` | 91,087 | 86,477 | 101,642 | 76,965 | 356,171 |
| `sigma_3` | 172,705 | 27,363 | 170,090 | 22,384 | 392,542 |
| `sigma_4` | 138,832 | 119,708 | 142,311 | 113,014 | 513,865 |
| `sigma_5` | 77,886 | 84,061 | 86,417 | 79,071 | 327,435 |
| `sigma_6` | 157,379 | 18,581 | 185,286 | 18,417 | 379,663 |
| `sigma_7` | 134,752 | 128,162 | 135,243 | 105,325 | 503,482 |
| **Total** | **1,027,063** | **618,325** | **1,114,808** | **571,052** | **3,331,248** |

No clean top order and bottom-row permutation leaves an active selector.

### Proof

For each signature, regenerate its exact `24`-selector group. Enumerate and
assert the clean-top order and node counts in both column-radix modes. For each
of the four orientations, run the active-selector bottom recursion over every
clean top ordering. Every exact tree is exhausted without a survivor, and the
node totals sum to `3,331,248`. \(\square\)

## 4. Revised cache boundary

### Corollary PX628 -- PROVED REDUCTION

The cache tiers through multiplicity `26` contain `902` selectors. Adding the
multiplicity-24 tier gives

\[
902+192=\boxed{1{,}094}
\]

certified-infeasible support-twenty selectors, using cumulatively

\[
12{,}928{,}516+3{,}331{,}248
=\boxed{16{,}259{,}764}
\]

shared bottom-CSP nodes. The active count is therefore

\[
71{,}860-1{,}094=\boxed{70{,}766}.
\]

The next tier has multiplicity `23`: ten signatures and `230` selectors.

This remains a finite cache obstruction, not a global infeasibility theorem.

## 5. Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity24.cpp \
  -o /tmp/side7_c52_s20_m24
```

and run all thirty-two exact cases:

```bash
for case_index in 0 1 2 3 4 5 6 7; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m24 "$case_index" "$orientation"
  done
done
```

Every case regenerates the complete selector layer, verifies that the
multiplicity-24 histogram consists of exactly eight signatures, checks the
selected signature group, and asserts the exact top and bottom search counts
using integer determinants on `[14]^2`.
