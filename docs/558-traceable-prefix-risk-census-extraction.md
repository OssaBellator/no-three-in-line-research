# Traceable prefix-risk census extraction

`docs/552` proves deterministic existence from exact profile size and aggregate
risk totals.  The profile count is derived from the legal-tree series, whereas
the stored risk totals are fixture multiples of that count.  This chapter
separates the valid union-bound interface from the missing geometric census.

## 1. Exact census compression

### Theorem PP3cow -- PROVED / PROFILE RISK-SUM SUFFICIENCY

For a finite profile family `F` and nonnegative integer risks `r_k(T)`, the data

```text
|F|,  R_k=sum_(T in F) r_k(T)
```

are sufficient to certify an object with `r_k(T)<tau_k` for all `k` whenever

```text
sum_k floor(R_k/tau_k) < |F|.
```

#### Proof

At most `floor(R_k/tau_k)` objects violate coordinate `k`.  The union bound leaves
at least the displayed positive number outside every violating set. ∎

## 2. Traceability requirement

### Theorem PP3cox -- PROVED / AGGREGATE-RISK RECONSTRUCTION CONTRACT

To promote aggregate totals to geometric evidence, a certificate must provide a
canonical object index or coefficient dynamic program, the integer risk rule for
each coordinate, and a reconstruction of every `R_k`.  Aggregate totals alone do
not identify a witness object.

#### Proof

Different assignments can have identical totals and different good-object sets.
Thus totals prove existence by `PP3cow` but cannot reconstruct a witness without
additional trace data.  A deterministic enumerator or sufficient-statistic
recurrence supplies exactly that data. ∎

## 3. Status of the stored profile fixture

### Theorem PP3coy -- PROVED / PREFIX RISK PROVENANCE GAP

For 30 leaves and nine binary nodes, the exact family size is
`168212023980`.  The stored totals `(3,2,1,1)|F|` and thresholds
`(10,10,8,16)` certify at least `52566257495` acceptable objects and row `1/40`.
No risk enumerator or geometric risk definition is recorded, so the existence
calculation remains fixture-backed.

#### Proof

The profile coefficient is the exact factorial formula.  Dividing the four
stored totals by their thresholds and applying `PP3cow` gives the stated lower
bound.  The provenance record has a null risk-enumerator field. ∎

## 4. Stored exact audit

The audit `scripts/check_prefix_risk_census_provenance.py` reconstructs the
profile coefficient, all four violation caps, the good-family lower bound, and
the normalized row.  A toy pair of equal-total censuses verifies that aggregate
totals do not identify the same witness set.

## 5. Prime-patching consequence

The prefix frontier now has a precise extraction target: implement the actual
support/source/geometric risk recurrence on one central profile and output both
the aggregate totals and a deterministic surviving object.
