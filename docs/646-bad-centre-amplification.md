# Bad-centre amplification for source-star motifs

`docs/640` classifies the stored four-centre source motif: three centres are
matching-shaped and one is bad.  This chapter gives the exact amplification and
corruption tolerance when several resource-disjoint motifs are available.

## 1. Exact motif amplification

### Theorem PP3cza — PROVED / GOOD-CENTRE COUNT

For `t` disjoint copies of the four-centre source motif and `e` additional
corruptions among the otherwise good centres, the guaranteed number of usable
centres is

```text
3t - e.
```

The mixed-degree Hall pipeline has its required twenty-eight good centre
resources exactly when

```text
3t - e >= 28.
```

#### Proof

Each motif contributes three source-typed matching-shaped centres before
additional corruption.  The extra corruptions remove at most one usable centre
each. ∎

## 2. Sharp finite thresholds

### Theorem PP3czb — PROVED / TEN-MOTIF BASE THRESHOLD

Without additional corruption, ten motifs are necessary and sufficient:
nine supply twenty-seven good centres, while ten supply thirty.

Ten motifs tolerate exactly two additional corruptions and still supply
twenty-eight good centres; a third corruption forces an eleventh motif.

#### Proof

Substitute `e=0,2,3` into `PP3cza`.  The integer threshold is

```text
ceil((28+e)/3).
```

The exact values are checked in
`scripts/check_hall_bad_centre_amplification.py`. ∎

## 3. Corruption-rate interface

### Theorem PP3czc — PROVED / LINEAR BAD-CENTRE BUDGET

If the number of additional corruptions is at most `rho t`, with `rho<3`, then
it suffices that

```text
t >= ceil(28/(3-rho)).
```

For corruption rates `0, 1/4, 1/2, 1, 2`, the minimum motif counts are
respectively

```text
10, 11, 12, 14, 28.
```

#### Proof

Use `3t-rho t >= 28` and round to the least integer motif count. ∎

## Remaining source obligation

The count interface is exact.  The large geometric host must still produce
resource-disjoint copies, control cross-copy conflicts, and prove the degree-two
source and host-defect conditions after the resulting centre selection.
