# An aligned conservative threshold-layer benchmark

`docs/563` found that the source matrix in `docs/521` and the transient alphabet
in `docs/527` were different fixtures.  Here the observables are attached directly
to every permutation layer in an exact decomposition of the original conservative
matrix.  This removes the lineage mismatch for one benchmark data set.

Let

```text
M=((2,1,1,0),
   (0,2,1,1),
   (1,0,2,1),
   (1,1,0,2)).
```

For a permutation layer `pi`, record

```text
f(pi)=number of fixed points,
g(pi)=number of cyclic-forward edges i->i+1 mod 4.
```

## 1. Exact aligned decomposition census

### Theorem PP3cqd -- PROVED / SOURCE-MATRIX DECOMPOSITION ALIGNMENT

The matrix `M` has exactly 84 ordered decompositions into four permutation
layers.  Every layer observable `(f,g)` is computed from the same permutation
matrix that contributes to `M`; hence matrix totals, collision freedom, and
transient observables are aligned by construction.

#### Proof

Recursively subtract every supported permutation matrix from the current
nonnegative residual matrix.  Four subtraction levels exhaust all ordered
decompositions.  The observable is a deterministic function of the selected
permutation, so no independent layer alphabet is introduced. ∎

## 2. Sharp transient benchmark

### Theorem PP3cqe -- PROVED / ALIGNED PREFIX-DISCREPANCY OPTIMUM

Center the two observables within each four-layer decomposition.  The minimum
possible prefix `l_infinity` discrepancy among all 84 ordered decompositions is
one, attained by exactly sixteen decompositions.  The lexicographically first is

```text
(0,2,3,1), (0,1,2,3), (1,3,2,0), (2,1,0,3),
```

with observable vectors

```text
(1,2), (4,0), (1,2), (2,0)
```

and mean `(2,1)`.

#### Proof

Evaluate the exact centered prefix sums for all 84 decompositions.  Exhaustion
gives the optimum, multiplicity, and first witness. ∎

## 3. Exact normal-coverage oracle

### Theorem PP3cqf -- PROVED / ALIGNED LAYER NORMAL ROW SPACE

For the selected decomposition, adjoin the constant-total row to the two
observable rows.  The resulting quotient has rank three in four slot
coordinates.  Among the 1120 canonical primitive integer normals in `[-3,3]^4`,
145 lie in its row space and 975 do not.

#### Proof

Exact rational row reduction gives rank three.  For each bounded primitive
normal, append it to the quotient matrix and compare ranks.  Equality is
precisely row-space membership. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_aligned_threshold_decompositions.py
```

The audit reconstructs all 84 decompositions, all prefix discrepancies, the
sixteen optima, and the complete bounded normal census.

## 5. Prime-patching consequence

The threshold compiler now has a fully aligned benchmark using one source matrix,
one decomposition family, and observables derived from the actual layers.  The
remaining source gap is the list of residual prime-patching threshold normals.
Once supplied, `PP3cqf` either factors each one or returns an explicit hidden
normal requiring a separate ledger charge.
