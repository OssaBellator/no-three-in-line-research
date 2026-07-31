# Source-cell normal census for threshold layers

`docs/569` aligns one conservative source matrix with its exact permutation
decomposition and two derived observables.  This chapter tests the most direct
source-derived threshold normals: occupancy of each positive source-action
cell across the four selected layers.

## 1. Cell occupancy normals

For source `i` and action `j`, let

```text
g_ij(t)=1
```

when layer `t` uses cell `(i,j)`, and zero otherwise.  The four-entry vector
`g_ij` is an exact normal on the layer-count coordinates.

### Theorem PP3cqv -- PROVED / SOURCE-CELL NORMAL EXTRACTION

The selected decomposition has twelve positive source cells and four absent
cells.  Their complete occupancy-normal table is computable directly from the
permutations, with no separately chosen geometric coefficients.

#### Proof

Each layer is an explicit permutation.  Evaluating its cell indicator in all
four positions gives the normal.  A cell absent from the conservative matrix
has the zero normal in every valid decomposition. ∎

## 2. Exact quotient factorization census

Let `Q` have rows

```text
constant total,
fixed-point count,
cyclic-forward count.
```

### Theorem PP3cqw -- PROVED / FOUR CONTROLLED, EIGHT HIDDEN

Of the twelve positive source-cell normals, exactly four lie in the row space of
`Q` and eight do not.  For example,

```text
g_(0,2)=(0,0,0,1)
       =2 Q_0-(1/2)Q_1-(3/4)Q_2,
```

while

```text
g_(0,0)=(1,1,0,0)
```

is not in that row space.

#### Proof

Exact rational row reduction tests all twelve vectors.  The checker stores a
factorization for every controlled vector and a rank-increase certificate for
every hidden one. ∎

## 3. Threshold consequence

### Theorem PP3cqx -- PROVED / SOURCE GRANULARITY OBSTRUCTION

Any threshold system that separately constrains all positive source-action
cells cannot be certified by the current constant/fixed/forward quotient alone.
At least one additional observable is required, and in this fixture eight cell
constraints are presently hidden.

#### Proof

A hidden normal varies on the kernel of the quotient map.  Therefore no bound on
the quotient coordinates can control that cell occupancy without a separate
charge or a refined quotient. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_threshold_source_cell_normals.py
```

## 5. Prime-patching consequence

The missing normal list is no longer merely hypothetical: even the canonical
source-cell constraints expose eight hidden directions.  The next threshold
step should derive the actual geometric inequalities and enlarge the quotient
only along directions they genuinely use.
