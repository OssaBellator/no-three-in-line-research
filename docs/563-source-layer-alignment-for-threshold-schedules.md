# Source-layer alignment for threshold schedules

The threshold chain `docs/521`, `docs/527`, `docs/533`, and `docs/551` uses
several finite layer fixtures.  `docs/557` showed that a quotient controls only
factorable physical normals.  This chapter first checks whether the source
matrix and the later transient layer alphabet are even the same physical
schedule.

The conservative matrix from `docs/521` is

```text
M=((2,1,1,0),
   (0,2,1,1),
   (1,0,2,1),
   (1,1,0,2)).
```

Its stored lexicographic decomposition is

```text
0123, 0123, 1230, 2301.
```

The transient fixture in `docs/527` instead uses

```text
0123, 1230, 2301, 3012.
```

## 1. Layer-sum invariance

### Theorem PP3cpl -- PROVED / PHYSICAL LAYER-SUM CERTIFICATE

The sum of permutation layers is invariant under every reordering.  Therefore a
transient sequencing theorem may be attached to a conservative source matrix
only after the selected layer multiset is proved to sum to that matrix.

#### Proof

Reordering changes only the order of addition, not the entrywise sum of the
permutation matrices. ∎

## 2. Stored lineage mismatch

### Theorem PP3cpm -- REFUTED / DIRECT `DOCS/521`-TO-`DOCS/527` LAYER IDENTITY

The `docs/521` layers sum to `M`, whereas the four distinct cyclic layers of
`docs/527` sum to the all-ones matrix `J`.  Their difference is

```text
M-J=(( 1, 0, 0,-1),
     (-1, 1, 0, 0),
     ( 0,-1, 1, 0),
     ( 0, 0,-1, 1)).
```

Consequently no reordering of the `docs/527` layer alphabet realizes the stored
`docs/521` source matrix.

#### Proof

Entrywise summation gives the two displayed matrices.  `PP3cpl` excludes repair
by reordering. ∎

## 3. Quotient-normal coverage census

### Theorem PP3cpn -- PROVED / BOUNDED PHYSICAL-NORMAL COVERAGE ORACLE

Attach to the four `docs/527` layers the observable columns

```text
(3,0), (0,3), (2,1), (1,2).
```

The resulting quotient map has row rank two.  Among the `1120` canonical
primitive integer normals on the four layer-count coordinates with coefficients
in `[-3,3]`, exactly six lie in its row space and `1114` are hidden.  In
particular,

```text
(3,-3,1,-1)
```

is controlled, while

```text
(1,-1,-1,1)
```

is not.

#### Proof

Exact rational Gaussian elimination decides row-space membership.  Exhausting
the finite coefficient box gives the counts and witnesses. ∎

## 4. Stored exact audit

Run

```bash
python scripts/check_threshold_source_layer_alignment.py
```

The checker reconstructs both layer sums and exhausts the bounded primitive
normal census.

## 5. Prime-patching consequence

The current threshold row cannot be promoted by linking the existing source and
transient fixtures: their physical layer multisets differ.  A successful
extraction must choose one actual conservative matrix, one decomposition of that
matrix, and one complete normal list on those same layers before applying a
quotient discrepancy bound.
