# Exact `m=10` Hall phase profile by compatible-source count

For a supported signed atomic flaw `f`, write

```text
s(f)     = number of compatible clean source cycles,
gamma(f) = exact optimal weighted-Hall charge.
```

For every nonempty source count `s`, define the count-resolved extremum

```text
A_s = max_{f: s(f)=s} s gamma(f).
```

`docs/372` records only the maximum of `A_s` over all source counts. This
chapter resolves the complete `m=10` profile by exact source count.

The result is finite. It does not prove an asymptotic inverse-source theorem or
that every flaw at a source count with `A_s>1` violates the constant-one bound.

## 1. Complete count-resolved profile

### Theorem PP3bth -- VERIFIED FINITELY / ALL NONEMPTY SOURCE COUNTS

The complete `m=10` transport census has exactly 479 nonempty compatible-source
counts in the range `106--720`. The count-resolved ledgers cover all 47,512
supported signed flaws, and for every nonempty count they record exactly:

1. the number of signed flaws;
2. the maximum Hall charge;
3. the support-normalized maximum `A_s`;
4. a maximizing Hall-subset size, supply, and capacity.

The ledgers split into the already natural computational ranges

```text
106--399,
400--575,
576--649,
650--719,
720.
```

Every recorded flaw has a proper Hall bottleneck. The profile maximum remains

```text
A_600 = 600 * 5254/791819
      = 3152400/791819
      = 3.981212878196... < 4.
```

#### Verification

The warning-clean Dinic and gap-push-relabel workers solve the exact
Dinkelbach/min-cut instance for every flaw in one requested source interval.
The resumable orchestration script asks them to solve one exact source count at
a time and stores every completed JSON row. The aggregate Python verifier
combines those outputs with the previously committed exact high-source and
full-support ledgers, checks unique count coverage, reconstructs every
`A_s=s*gamma_s`, and verifies the total of 47,512 flaws. ∎

## 2. Onset, intermittent window, and permanent count-max violation

### Theorem PP3bti -- VERIFIED FINITELY / CONSTANT-ONE SUPPORT PHASE

The exact count-resolved profile has three regimes.

### Subcritical count range

For every one of the 25 nonempty source counts in `106--208`,

```text
A_s < 1.
```

These levels contain 152 signed flaws. Consequently every flaw at each of these
source counts satisfies `gamma(f)<1/s(f)`.

### Intermittent transition window

The constant-one envelope first fails at source count 209:

```text
A_209 = 45980/45691
      = 1 + 289/45691
      = 1.006325... .
```

Within `209--287`, there are 43 nonempty source counts. Exactly 13 have
`A_s>1`, while 30 still have `A_s<1`. Thus the transition is not monotone in
source count.

The closest nonviolation to one occurs at source count 279:

```text
A_279 = 29574/29677
      = 1 - 103/29677.
```

The last later nonviolation occurs at source count 287:

```text
A_287 = 861/1133
      = 1 - 272/1133.
```

### Permanent count-max violation range

For every one of the 411 nonempty source counts in `288--720`,

```text
A_s > 1.
```

These levels contain 47,076 signed flaws. The smallest count-resolved maximum in
this range is attained at source count 305:

```text
A_305 = 685640/632751
      = 1 + 52889/632751
      = 1.083588... .
```

Here `A_s>1` means that at least one flaw with exactly `s` compatible source
cycles violates the constant-one inverse-support bound. It does not assert that
all flaws at that count violate it. ∎

## 3. Structural interpretation

### Corollary PP3btj -- PROVED / VERIFIED FINITELY / TWO-THRESHOLD TRANSITION

At `m=10`, the support-normalized Hall obstruction has two exact thresholds:

```text
onset of failure:                 s=209,
last later count with A_s<1:      s=287,
all later nonempty counts:        A_s>1.
```

Thus the jump beyond the constant-one theorem is not caused only by nearly full
three-arc support. It begins at less than one third of the factorial support
`720`, passes through an intermittent geometry-dependent window, and becomes a
persistent count-resolved obstruction well before the median source count 612.

The asymptotic inverse-source problem should therefore not be reduced to source
count alone. A uniform theorem with constant below four must also distinguish
the weighted neighbourhood geometry responsible for the transition window and
the permanent high-support obstruction.

Reproduce the low and middle profiles resumably with

```bash
python scripts/check_m10_hall_support_count_phase.py . \
  --lo 106 --hi 399 \
  --cache /tmp/m10-hall-106-399 \
  --output /tmp/m10-hall-profile-106-399.json

python scripts/check_m10_hall_support_count_phase.py . \
  --lo 400 --hi 575 \
  --cache /tmp/m10-hall-400-575 \
  --output /tmp/m10-hall-profile-400-575.json

python scripts/verify_m10_hall_support_count_phase.py .
```

The next theorem identifier after this chapter is `PP3btk`.
