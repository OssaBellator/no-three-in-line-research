# Fieldwise evidence gate after independent extraction

`docs/560` separated arithmetic feasibility from geometric evidence.  The five
new extraction attempts improve several source fields without realizing a full
prime-patching row.  This chapter records progress field by field and prevents a
partially completed candidate model from being promoted as geometric closure.

## 1. Candidate-field completion vector

### Theorem PP3cpu -- PROVED / EXTRACTION-FIELD COMPLETION CERTIFICATE

Against the promotion requirements recorded in
`certificates/prime-patching-provenance-audit-555-560.json`, the independent
attempts complete the following numbers of source fields:

```text
boundary    3/5,
Hall        4/5,
threshold   4/5,
prefix      5/5,
shell       5/5,
integration 1/5.
```

Thus `22` of `30` candidate fields are now represented by an exact finite
construction or obstruction.  Only the corrected structural prefix model and
the benchmark shell model are internally complete; neither is linked to the
actual prime-patching geometry.

#### Proof

Each completed field has a source definition and checker in `docs/561--565`.
Each missing field is listed explicitly in the new machine-readable certificate.
Summation gives `22/30`. ∎

## 2. Exact arithmetic fixed point remains feasible

### Theorem PP3cpv -- PROVED / COUPLED FIXED-POINT RECOMPUTATION

For the fixture-derived base vector and coupling matrix of `docs/554`, the exact
minimal nonnegative solution of

```text
y=b+Cy
```

has total

```text
705466760524005697 / 3623878655999606784
 = 0.194671739175... .
```

The exact remaining arithmetic slack below `1/4` is

```text
200502903475895999 / 3623878655999606784 > 0.
```

#### Proof

Exact rational Gaussian elimination solves `(I-C)y=b`.  Substitution verifies
every coordinate equation, and summation gives the displayed values. ∎

## 3. Evidence-gated nonclosure

### Theorem PP3cpw -- PROVED / NO-PROMOTION GATE

No global row is promoted by `docs/561--565`.  All six direct rows in the coupled
ledger remain `fixture_derived`, so the geometric evidence meet is below
`geometric_verified`.  Positive arithmetic slack therefore does not imply
prime-patching closure.

#### Proof

The boundary attempt ends in a seam obstruction; the Hall microcensus lacks a
geometric decoder; the threshold source and transient fixtures disagree; the
prefix risk is structural rather than geometric; and the shell incidence is a
benchmark definition.  Hence every actual global row retains at least one
missing geometric source field.  The closure rule requires both arithmetic
feasibility and geometric verification of every row, so it remains false. ∎

## 4. Machine-readable evidence record

The complete record is

```text
certificates/prime-patching-independent-extraction-561-566.json
```

and is checked by

```bash
python scripts/check_independent_extraction_evidence_gate.py
```

The group runner is

```bash
python scripts/check_frontier_561_566.py
```

## 5. Prime-patching consequence

The new tranche makes progress without manufacturing a theorem from benchmarks.
The next work is sharply localized: a non-diagonal boundary seam mechanism, a
geometric decoder for the Hall cylinder states, one aligned threshold source
matrix and normal list, the actual geometric prefix risks, the true shell
incidence map, and source-derived coupling coefficients.
