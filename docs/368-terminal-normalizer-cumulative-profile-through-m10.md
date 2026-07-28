# Terminal normalizer cumulative profiles through `m=10`

For the fibre-capacity-weighted terminal policy, each incoming labelled move
from a terminal source state `x` has positive capacity normalizer

```text
Z(x) = sum_(closing labels T available at x) F(eta_T),
```

and contributes `1/Z(x)` to its regenerated target column. `docs/365` rewrites
the column load using the cumulative profile

```text
C_eta(t) = number of incoming labelled moves to eta with Z(x) <= t.
```

This chapter computes that profile exactly through `m=10` and tests the
square-root instance of the layer-cake criterion.

No asymptotic cumulative-profile estimate is claimed.

## 1. Complete cumulative-profile census

### Theorem PP3bsv -- VERIFIED FINITELY / TERMINAL NORMALIZER PROFILE

The exact terminal incidence data are

| `m` | terminal states | incoming signed labels | targets hit | normalizer range | maximum labels into one target |
|---:|---:|---:|---:|---:|---:|
| 8 | 33,624 | 1,136,332 | 2,614 | `1096--7056` | 1,744 |
| 9 | 478,040 | 28,101,044 | 22,138 | `2976--28160` | 8,574 |
| 10 | 535,072 | 55,091,040 | 65,420 | `9872--85248` | 8,960 |

The maxima of `C_eta(t)` at the relevant dyadic thresholds are

| `m` | exact dyadic cumulative maxima |
|---:|---|
| 8 | `C(2048)<=96`, `C(4096)<=688`, `C(8192)<=1744` |
| 9 | `C(4096)<=32`, `C(8192)<=616`, `C(16384)<=5632`, `C(32768)<=8574` |
| 10 | `C(16384)<=128`, `C(32768)<=1344`, `C(65536)<=6656`, `C(131072)<=8960` |

Here each displayed maximum is taken over every predecessor-shell target cycle.

#### Verification

The checker reconstructs the exact root-cube clean-macro shells. For each
terminal signed source state it computes every closing predecessor label and
its integer normalizer `Z(x)`. It then forms the complete incoming normalizer
multiset for every target cycle, sorts it, and audits every jump of `C_eta(t)`.
The Hamilton counts, clean-state counts, terminal counts, normalizer ranges,
dyadic maxima, and extremal profile values are hard-coded regression data. ∎

## 2. Exact square-root envelopes

For a fixed size define

```text
R_m = sup_(eta,t) C_eta(t)^2/t.
```

The exact extrema are

| `m` | maximizing `(C,t)` | exact `R_m` | ties |
|---:|---:|---:|---:|
| 8 | `(1744,6384)` | `190096/399` | 2 |
| 9 | `(8574,23584)` | `18378369/5896` | 2 |
| 10 | `(8960,85248)` | `313600/333` | 2 |

Consequently `C_eta(t) <= sqrt(R_m t)` for every audited target and threshold.

### Theorem PP3bsw -- PROVED / VERIFIED FINITELY / SQUARE-ROOT COUNTING CERTIFICATE AT `m=10`

At `m=10`, the square-root cumulative estimate alone certifies terminal
contraction:

```text
kappa_F(eta)
 <= 2 sqrt(R_10) / sqrt(z_min)
 = sqrt(78400/205461)
 < 5/8.
```

#### Proof

Apply the cumulative-capacity criterion `PP3bso` with `delta=1/2`,
`A=sqrt(R_10)`, and the exact minimum normalizer `z_min=9872`. Squaring the
result gives

```text
4 R_10/z_min
 = 4*(313600/333)/9872
 = 78400/205461.
```

Finally,

```text
64*78400 = 5,017,600
< 5,136,525 = 25*205461,
```

so the unsquared bound is below `5/8`. ∎

The analogous squared bounds are

```text
m=8:  95048/54663  > 1,
m=9:  6126123/1462208 > 1,
m=10: 78400/205461 < 1.
```

Thus this deliberately coarse square-root route becomes contractive at
`m=10`, although it does not certify the smaller earlier sizes. That failure is
only a failure of the coarse cumulative envelope; the exact capacity-weighted
policy itself is contractive at all three sizes by `docs/361`.

Compile and run the exact audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_terminal_normalizer_cumulative_profile.cpp \
  -o /tmp/check_terminal_normalizer_cumulative_profile

for m in 8 9 10; do
  OMP_NUM_THREADS=8 /tmp/check_terminal_normalizer_cumulative_profile "$m"
done
```

The next theorem identifier after this chapter is `PP3bsx`.
