# Threshold-normal factorization and hidden residuals

`docs/551` bounds supplied threshold facets by a common discrepancy box.  To use
that adapter geometrically, every actual threshold inequality must be expressed
in the scheduled quotient coordinates.  This chapter gives the exact linear
criterion and records the current provenance gap.

Let `Q` map physical resource increments to quotient coordinates.  Let the rows
of `G` be the physical threshold normals.

## 1. Exact quotient-factorization criterion

### Theorem PP3cot -- PROVED / THRESHOLD NORMAL FACTORIZATION

The physical threshold family is completely controlled by quotient discrepancy
if and only if there is a rational matrix `Lambda` with

```text
G = Lambda Q.
```

For a quotient box with coordinate widths `w`, row `k` then has exact dual bound

```text
sum_j |Lambda_(k,j)| w_j.
```

#### Proof

Factorization gives `Gx=Lambda(Qx)`, so the box bound follows by the triangle
inequality and is sharp for an axis-aligned box.  Conversely, if a row of `G`
does not lie in the row space of `Q`, linear algebra gives a vector in `ker Q`
on which that row is nonzero.  Quotient discrepancy is then zero while the
physical threshold changes. ∎

## 2. Hidden-resource obstruction

### Theorem PP3cou -- PROVED / NONFACTORABLE NORMAL WITNESS

A nonfactorable threshold normal is a hidden resource.  It must either be added
to the quotient state or charged by an independent estimate; no common-box
certificate in the old quotient can control it.

#### Proof

Use the kernel witness from the converse of `PP3cot`.  Repetition scales the
physical threshold while leaving the quotient path unchanged, excluding every
finite quotient-only bound. ∎

## 3. Provenance status of the stored facets

### Theorem PP3cov -- PROVED / THRESHOLD NORMAL EXTRACTION GAP

The three facet rows in `docs/551` factor trivially through a two-coordinate
identity quotient and have maximum dual box loss `1/32`.  However, the stored
certificate contains neither a physical quotient map nor source identifiers for
the geometric inequalities.  Therefore it verifies the adapter arithmetic but
not extraction of the actual threshold-normal matrix.

#### Proof

The finite provenance record lists the three rows and no quotient map or source
inequality IDs.  The checker also embeds them as `(a,b,0)` in a three-coordinate
physical space and exhibits `(0,0,1)` as a nonfactorable hidden normal. ∎

## 4. Stored exact audit

The audit `scripts/check_threshold_normal_provenance.py` reconstructs the
`1/32` dual loss, verifies exact factorization of the supplied rows, and checks a
hidden-coordinate witness invisible to the quotient.

## 5. Prime-patching consequence

The threshold frontier is reduced to a concrete matrix-extraction problem:
write the complete physical normal matrix, write the quotient map, solve
`G=Lambda Q`, and explicitly account for every residual row.
