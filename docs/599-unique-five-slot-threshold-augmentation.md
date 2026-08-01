# Unique five-slot threshold augmentation

The stored four-slot conservative matrix has no decomposition entirely into legal
no-three-in-line permutation layers.  Rather than moving existing mass, this
chapter adds one unit in every source row and action column and searches all
twenty-four possible augmentation permutations.

### Theorem PP3ctp -- PROVED / UNIQUE ONE-SLOT AUGMENTATION

Exactly one augmentation permutation works:

```text
(3,0,1,2).
```

It changes the source matrix to

```text
((2,1,1,1),
 (1,2,1,1),
 (1,1,2,1),
 (1,1,1,2)).
```

#### Proof

For each of the twenty-four permutations, add its permutation matrix to the
stored source matrix and recursively count decompositions into five of the
eighteen legal four-cell permutation layers.  Only the displayed augmentation
has positive count. ∎

### Theorem PP3ctq -- PROVED / EXACT LEGAL DECOMPOSITION COUNT

The augmented matrix has exactly `120` ordered decompositions into five legal
layers.

#### Proof

Memoized exact subtraction over the eighteen legal layers counts every ordered
decomposition and returns `120`. ∎

### Theorem PP3ctr -- PROVED / SOURCE-SLOT GAP

The augmentation permutation is itself geometrically illegal, even though the
augmented aggregate matrix admits legal decompositions.  Therefore the result is
an aggregate five-slot enlargement, not a physical extra layer.

#### Proof

The four points of `(3,0,1,2)` contain a collinear triple.  The legal
decompositions redistribute its added source mass across five different layers.
No repository inequality currently pays for that extra source slot. ∎

Run:

```bash
python scripts/check_threshold_unique_five_slot_augmentation.py
```
