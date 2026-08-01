# Nearest legal conservative threshold matrix

`docs/581` proved that the stored conservative matrix cannot be decomposed into
four no-three-in-line permutation layers.  This chapter searches the complete
nearby replacement space before attaching any quotient observables.

Let

```text
M = ((2,1,1,0),
     (0,2,1,1),
     (1,0,2,1),
     (1,1,0,2)).
```

Every sum of four permutation matrices has all row and column sums equal to four.
We restrict the layers to the eighteen legal permutations of the four-by-four
grid.

## 1. Sharp replacement distance

### Theorem PP3csf -- PROVED / NEAREST LEGAL MATRIX DISTANCE

Among all multisets of four legal permutation layers, the minimum entrywise
`l_1` distance from `M` is six.  Exactly eight resulting conservative matrices
attain this distance.

#### Proof

There are eighteen legal layers and

```text
C(18+4-1,4)=5985
```

four-layer multisets.  Exact enumeration forms each matrix and compares all
sixteen entries with `M`.  The minimum is six and has eight witnesses. ∎

### Theorem PP3csg -- PROVED / CANONICAL LEGAL REPLACEMENT

The lexicographically first nearest matrix is

```text
M' = ((1,1,1,1),
      (0,2,1,1),
      (2,0,1,1),
      (1,1,1,1)),
```

with legal layer multiset

```text
(0,1,3,2),
(1,2,0,3),
(2,3,0,1),
(3,1,2,0).
```

Thus geometric legality can be restored without changing the row or column
margins, but only after moving three units of mass and therefore changing six
matrix entries in `l_1` distance.

#### Proof

Direct summation gives `M'`, and each listed layer passes the exact collinearity
test.  `PP3csf` proves optimality. ∎

## 2. Transient ordering after geometric legality

### Theorem PP3csh -- PROVED / LEGAL PREFIX ORDERING

For the fixed-point and cyclic-forward layer observables, the canonical
replacement admits an ordering with maximum centered prefix discrepancy one.
Exactly eight of its twenty-four orderings attain this value.

#### Proof

The checker evaluates both observable prefixes for every ordering using exact
rational arithmetic. ∎

## 3. Exact audit

Run

```bash
python scripts/check_nearest_legal_threshold_matrix.py
```

## 4. Frontier consequence

The four-slot geometric obstruction has a sharp nearest replacement.  This does
not identify the correct prime-patching matrix: the six units of entrywise
change must be justified by the actual threshold inequalities or paid as a
separate repair.  Observables are attached only after legality, avoiding the
lineage error isolated in `docs/563`.
