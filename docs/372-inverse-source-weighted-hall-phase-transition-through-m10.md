# Exact inverse-source weighted-Hall phase transition through `m=10`

For a supported signed atomic flaw `f`, let

```text
s(f)     = number of compatible clean source cycles,
gamma(f) = exact optimal weighted-Hall charge.
```

`docs/370` proved `gamma(f)<4/s(f)` for every supported `m=10` flaw. This
chapter recomputes the support-normalized optimum for every complete audit from
`m=4` through `m=9` and combines it with the complete `m=10` ledger.

The result is finite. It does not prove a general inverse-source theorem.

## 1. Complete support-normalized ledger

Define

```text
A_m = max_f s(f) gamma(f),
```

where the maximum is over every supported signed flaw at size `m`.

### Theorem PP3bte -- VERIFIED FINITELY / EXACT INVERSE-SOURCE LEDGER

The complete exact values are:

| `m` | source-count range | `A_m` | decimal | maximizing source count | maximizing raw charge |
|---:|---:|---:|---:|---:|---:|
| 4 | `1--1` | `1/24` | `0.041666666667...` | 1 | `1/24` |
| 5 | `1--1` | `1/37` | `0.027027027027...` | 1 | `1/37` |
| 6 | `1--2` | `8/215` | `0.037209302326...` | 2 | `4/215` |
| 7 | `1--6` | `72/931` | `0.077336197637...` | 6 | `12/931` |
| 8 | `2--24` | `192/745` | `0.257718120805...` | 24 | `8/745` |
| 9 | `17--120` | `83040/96029` | `0.864738776828...` | 120 | `692/96029` |
| 10 | `106--720` | `3152400/791819` | `3.981212878196...` | 600 | `5254/791819` |

For `4<=m<=9`, the support-normalized maximizer uses the full factorial source
support

```text
s(f) = (m-4)!.
```

At `m=10`, the full three-arc support is `6!=720`, but the support-normalized
maximizer uses only 600 source cycles. Thus the extremal geometry changes before
the universal constant four is saturated.

#### Verification

For each `4<=m<=9`, the warning-clean compressed checker enumerates every
supported complement-reduced flaw, constructs its exact weighted transport
instance, solves the rational Dinkelbach/min-cut problem, and maximizes
`s(f)gamma(f)`. It also reproduces the published flaw counts, bottleneck counts,
source ranges, and global worst charges. The `m=10` row is read from the complete
47,512-instance audit. Exact witness identities are not regression-locked when
multiple tied flaws exist. ∎

## 2. Constant-one phase transition

### Corollary PP3btf -- PROVED / VERIFIED FINITELY / ONE-OVER-SUPPORT THROUGH `m=9`

Every supported signed flaw at every audited size `4<=m<=9` satisfies

```text
gamma(f) < 1/s(f).
```

The closest case is `m=9`, with exact margin

```text
1 - A_9
 = 1 - 83040/96029
 = 12989/96029
 > 0.
```

The constant one first fails at `m=10`, because

```text
A_10 = 3152400/791819 > 1.
```

This is a finite phase transition in support-normalized Hall charge. It does not
by itself identify the structural cause.

## 3. Uniform finite constant four

### Corollary PP3btg -- PROVED / VERIFIED FINITELY / FOUR-OVER-SUPPORT THROUGH `m=10`

Every supported signed flaw at every audited size `4<=m<=10` satisfies

```text
gamma(f) < 4/s(f).
```

The tightest audited margin is the `m=10` value

```text
4 - A_10
 = 14876/791819
 > 0.
```

Hence an asymptotic proof can be cleanly separated into two obligations:

1. establish an inverse-source Hall estimate `gamma(f) <= C/s(f)` with a uniform
   constant `C`;
2. prove a sufficiently large lower bound on compatible source support at the
   flaw scales that survive the geometric reductions.

If `s(f)>=c m^3`, these two statements immediately give

```text
gamma(f) <= (C/c)m^-3.
```

Neither asymptotic statement is proved here. The exact finite transition shows
that a proof with constant one cannot persist unchanged beyond `m=9`, while the
constant four remains compatible with every complete audit through `m=10`.

Compile the exact `m<=9` checker separately at each compile-time size:

```bash
for m in 4 5 6 7 8 9; do
  g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp -DMVAL="$m" \
    scripts/check_weighted_hall_inverse_source_through_m9.cpp \
    -o "/tmp/check_weighted_hall_inverse_source_m${m}"
  OMP_NUM_THREADS=8 "/tmp/check_weighted_hall_inverse_source_m${m}"
done

python scripts/verify_weighted_hall_inverse_source_through_m10.py .
```

The next theorem identifier after this chapter is `PP3bth`.
