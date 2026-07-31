# Evidence-closed coupled ledger audit

`docs/554` proves arithmetic closure for supplied direct rows and coupling
coefficients.  Arithmetic feasibility and geometric evidence are separate
properties.  This chapter adds a provenance meet to the coupled ledger and
computes the exact minimal fixed point of the stored cyclic coupling system.

## 1. Evidence-meet composition

### Theorem PP3cpc -- PROVED / COUPLED EVIDENCE STATUS

Order evidence levels as

```text
assumed < fixture_derived < independently_enumerated < geometric_verified.
```

The evidence level of a composed certificate is at most the minimum level of
all inputs it consumes.  In particular, an exact rational supersolution cannot
promote a fixture-derived row to geometric verification.

#### Proof

The composition logically implies every consumed premise.  Its evidence can be
no stronger than its weakest unverified premise; otherwise the composition
would certify that premise without supplying new evidence for it. ∎

## 2. Exact minimal cyclic fixed point

### Theorem PP3cpd -- PROVED / SIX-ROW COUPLING FIXED POINT

For the stored nonnegative coupling matrix `C`, the minimal nonnegative solution
of

```text
x=b+Cx
```

is `(I-C)^(-1)b`.  The product of the six cyclic edge weights is

```text
1/9216000000000 < 1,
```

so the inverse exists and is the convergent nonnegative geometric series.  Its
row sum is approximately `0.194671739175`, below the simple supersolution sum
`99/500`.

#### Proof

The only directed cycle has the displayed product.  Therefore the spectral
radius is below one, `sum_(k>=0) C^k` converges entrywise, and multiplying by `b`
gives the least fixed point.  Exact Gaussian elimination reconstructs it. ∎

## 3. Current evidence closure status

### Theorem PP3cpe -- PROVED / GEOMETRIC CLOSURE REFUSAL CERTIFICATE

All six current provenance rows are marked `fixture_derived` and have no
independent geometric source.  Thus the stored system is arithmetically feasible
with positive margin but has zero geometrically verified rows.  It cannot be
reported as an all-`n` prime-patching closure.

#### Proof

The machine-readable record contains six fixture-derived levels and six null
source fields.  `PP3cpc` keeps the composed evidence at that level, while
`PP3cpd` and `docs/554` establish only arithmetic feasibility. ∎

## 4. Stored exact audit

The audit `scripts/check_integration_evidence_closure.py` verifies the supplied
supersolution, solves the exact fixed-point system, checks the cyclic product,
and refuses evidence closure because the number of geometric rows is zero.  The
group runner `scripts/check_frontier_555_560.py` first executes the complete
`docs/549--554` audit.

## 5. Prime-patching consequence

The branch now has an automatic guard against a serious category error:
compatible fixture arithmetic cannot be mistaken for geometric realization.
Each future extracted row can be promoted independently, after which the same
checker recomputes both the arithmetic fixed point and the evidence meet.
