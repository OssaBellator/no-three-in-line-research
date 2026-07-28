# Disjoint normalizer-bin envelopes for terminal descent

`docs/365` expresses the fibre-capacity-weighted terminal load at a target cycle
`eta` as

```text
kappa_F(eta) = sum_(incoming labelled moves i to eta) 1/Z_i,
```

where every capacity normalizer `Z_i` is a positive integer.  `docs/368`
controls this sum by a single square-root cumulative profile.  This chapter
keeps the normalizer scales separate.

No asymptotic bin-population estimate is claimed.

## 1. A discrete scale-separation lemma

Fix disjoint integer intervals

```text
I_j = [L_j,U_j]
```

covering all possible incoming normalizers.  Let

```text
B_j = sup_eta #{incoming labels i to eta with Z_i in I_j}.
```

### Proposition PP3bsx -- PROVED / DISJOINT NORMALIZER-BIN ENVELOPE

For every target cycle `eta`,

```text
kappa_F(eta) <= sum_j B_j/L_j.
```

#### Proof

Every label in `I_j` has `Z_i >= L_j`, hence contributes at most `1/L_j`.
There are at most `B_j` such labels into any fixed target.  Summing over the
disjoint bins gives the result. ∎

Unlike a cumulative bound, the maxima `B_j` may be proved independently at
each scale.  The price is that the maximizing targets for different bins need
not coincide, so the resulting envelope can be conservative.

## 2. Exact terminal bin populations through `m=10`

The checker uses powers of two as upper edges and the exact integer successor as
the next lower edge.

### Theorem PP3bsy -- VERIFIED FINITELY / EXACT BIN ENVELOPES

The exact maximum target populations and resulting envelopes are:

### `m=8`

| normalizer bin | maximum labels into one target |
|---:|---:|
| `1096--2048` | 96 |
| `2049--4096` | 672 |
| `4097--8192` | 1,344 |

Thus

```text
kappa_F(eta)
 <= 96/1096 + 672/2049 + 1344/4097
 = 285067172/383360387
 = 0.743601012694...
 < 3/4.
```

The exact margin below `3/4` is

```text
9812473/1533441548.
```

### `m=9`

| normalizer bin | maximum labels into one target |
|---:|---:|
| `2976--4096` | 32 |
| `4097--8192` | 616 |
| `8193--16384` | 5,376 |
| `16385--32768` | 4,864 |

The independent-bin envelope is

```text
18995653877059/17049712431135
 = 1.114133388102... > 1.
```

This does not contradict the exact capacity-weighted maximum
`0.573551848419...`; it shows only that independent maxima at these four scales
lose too much correlation at `m=9`.

### `m=10`

| normalizer bin | maximum labels into one target |
|---:|---:|
| `9872--16384` | 128 |
| `16385--32768` | 1,344 |
| `32769--65536` | 6,656 |
| `65537--131072` | 6,144 |

Therefore

```text
kappa_F(eta)
 <= 8507693248751944/21711076395041385
 = 0.391859578675...
 < 2/5.
```

The exact margin below `2/5` is

```text
35347461852922/4342215279008277.
```

#### Verification

The warning-clean checker reconstructs the complete terminal shells and every
closing labelled move.  For each move it computes the integer normalizer,
places it in the unique bin, and increments the target-bin population.  It then
maximizes each bin population over all predecessor-shell targets and verifies
the displayed rational sums exactly.  The previously audited exact
capacity-weighted maxima are also hard-coded as independent regressions. ∎

## 3. Structural consequence

The terminal counting problem can now be attacked scale by scale.  A uniform
asymptotic theorem need not fit a global power law to `C_eta(t)`; it is enough to
choose bins with lower edges `L_j` and prove

```text
sum_j B_j/L_j < 1-epsilon.
```

The finite `m=10` ledger shows substantial room with a four-bin proof.  The
`m=9` failure identifies the missing ingredient precisely: either finer bins or
correlation between populations at different scales.

Compile and run with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_terminal_normalizer_bin_envelope.cpp \
  -o /tmp/check_terminal_normalizer_bin_envelope

for m in 8 9 10; do
  OMP_NUM_THREADS=8 /tmp/check_terminal_normalizer_bin_envelope "$m"
done
```

The next theorem identifier after this chapter is `PP3bsz`.
