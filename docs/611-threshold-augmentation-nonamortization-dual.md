# Threshold augmentation non-amortization dual

`docs/599` finds the unique one-layer augmentation that turns the stored
four-slot threshold matrix into a legal five-layer matrix.  `docs/605` records
its new degree-five margins.  A possible escape would be to share one fifth
layer across several source periods.  An integer dual certificate rules this out
exactly.

Let

```text
S = ((2,1,1,0),
     (0,2,1,1),
     (1,0,2,1),
     (1,1,0,2))
```

and define the cell-weight matrix

```text
W = (( 3, 1, 2, 0),
     ( 0, 0, 0,-1),
     (-1,-3,-1,-3),
     ( 1, 0, 0, 0)).
```

## 1. Exact separating dual

### Theorem PP3cuz -- PROVED / INTEGER LEGAL-LAYER SEPARATOR

Every legal no-three-in-line permutation layer has `W`-score at most zero.
Every permutation layer, legal or illegal, has score at least minus three.  The
source matrix has score three.

#### Proof

The checker enumerates all twenty-four permutation layers.  Eighteen are legal.
Their scores lie in `{0,-1,-2}`.  All permutation scores are at least `-3`, while
an exact cellwise sum gives

```text
<W,S> = 3.
```

The unique augmentation `(3,0,1,2)` has score `-3`. ∎

## 2. No residue amortization

### Theorem PP3cva -- PROVED / ONE AUGMENTATION PER SOURCE PERIOD

Suppose `k` copies of `S`, together with `t` arbitrary permutation augmentation
layers, decompose into legal permutation layers.  Then

```text
t >= k.
```

#### Proof

The legal decomposition has total `W`-score at most zero.  The source contribution
has score `3k`, and the `t` augmentations contribute at least `-3t`.  Therefore

```text
0 >= 3k-3t,
```

which gives `t>=k`. ∎

## 3. Sharpness and cost

### Theorem PP3cvb -- PROVED / SHARP UNDILUTED FIFTH-LAYER DENSITY

The bound in `PP3cva` is sharp for every `k`: repeat the augmentation
`(3,0,1,2)` exactly `k` times and repeat its stored five-layer legal
decomposition.  Thus the exact augmentation density remains

```text
1 augmentation per source period,
1/5 of the augmented schedule,
1/4 relative slot-count increase.
```

#### Proof

The checker verifies the cellwise identity between `S` plus the augmentation and
the five legal layers

```text
(0,1,3,2), (0,2,1,3), (1,0,2,3), (2,3,0,1), (3,1,2,0).
```

All five have dual score zero.  Repetition gives equality for every `k`. ∎

## 4. Prime-patching consequence

The fifth layer cannot be paid by a bounded residue corrector or diluted over
many source periods.  Any source realization must supply degree-five margins at
positive density, or replace the current threshold matrix by different geometry.
