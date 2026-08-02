# Scaling mechanisms evidence gate

This chapter integrates `docs/639--643` without converting finite or conditional
progress into unsupported global evidence.

## 1. Candidate ledger

### Theorem PP3cyu — PROVED / CANDIDATE TOTAL UNCHANGED

The candidate field completion remains

```text
boundary    4/5
Hall        4/5
threshold   5/5
prefix      5/5
shell       5/5
integration 2/5
----------------
total      25/30.
```

The corrected twelfth transition, source-centre pruning, seven-cell threshold
batch, thirteen-pair reservoir, and shell amortization law refine existing
candidate fields but do not add a new completed field.

## 2. Fixture arithmetic

### Theorem PP3cyv — PROVED / FIXED POINT UNCHANGED

The fixture fixed-point total remains

```text
705466760524005697 / 3623878655999606784,
```

with positive slack below one quarter

```text
200502903475895999 / 3623878655999606784.
```

#### Proof

`scripts/check_scaling_mechanisms_gate.py` re-evaluates the stored exact rational
coordinates and candidate ledger. ∎

## 3. Evidence gate

### Theorem PP3cyw — PROVED / ZERO GLOBAL PROMOTIONS

All six actual ledger rows remain `fixture_derived`. No row is promoted to
`geometrically_verified`; geometric closure is false and the all-`n` theorem
remains open.

#### Proof

Boundary remains a bounded corrected path; Hall lacks asymptotic bad-centre and
degree bounds; threshold lacks a legal seven-cell or primitive six-cell source
edit; prefix lacks a uniform anchor-preserving family; shell lacks an actual
macro cost and collateral audit. ∎
