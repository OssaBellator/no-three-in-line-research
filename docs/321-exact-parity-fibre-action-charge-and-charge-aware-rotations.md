# Exact parity-fibre action charge and charge-aware rotations

`docs/320` gives exact uniform regeneration inside a clean orientation fibre.
This chapter computes the resulting labelled action charge and audits a
charge-aware clean-rotation choice through `m=9`.

The result does not yet give an unlabelled global flaw-walk criterion: different
rotation labels may merge into the same output column.

## 1. Exact predecessor multiplicity inside one source fibre

Fix an atomic three-owner flaw `A`, a parity-clean source Hamilton cycle `rho`,
and a labelled owner-intersecting successor rotation on source triple `T` whose
target cycle `rho'` is parity satisfiable.  Let

```text
c  = number of components of the source parity graph,
c' = number of components of the target parity graph,
r  = number of source components meeting the three owners of A.
```

The labelled fibre action applies the rotation and then outputs a uniformly
random clean orientation of `rho'`.

### Proposition PP3bmj -- PROVED / EXACT LABELLED CHARGE

For every clean output orientation on `rho'`, the total transition mass from
parity-clean source states on `rho` containing `A` is exactly

```text
2^(c-r-c').
```

Equivalently, the labelled column mass is

```text
2^(-Delta),
Delta = r+c'-c.
```

#### Proof

The atomic flaw records the signed assignments of its three owners and therefore
fixes the three corresponding orientation bits.  In the source parity solution
space, fixing one bit in a connected component fixes that component's root
choice.  Because `A` is present in at least one clean source state, the fixed
bits are mutually compatible.  They fix exactly the `r` component roots touched
by the owners and leave the other `c-r` roots free.  Thus exactly

```text
2^(c-r)
```

clean source orientations on `rho` contain `A`.

For the fixed labelled rotation and fixed target cycle, every such source state
outputs each of the `2^c'` clean target orientations with probability `2^-c'`.
Multiplication gives `2^(c-r-c')`. ∎

The inverse successor rotation makes the predecessor cycle unique once the
output cycle and label `T` are fixed, so no second source cycle contributes to
this labelled column.

## 2. Forest-regime formula

### Corollary PP3bmk -- PROVED

If both source and target parity graphs are forests with `q` and `q'` parity
edges, then

```text
Delta = r+q-q',
labelled column mass = 2^(q'-q-r).
```

#### Proof

By PP3bme, forest fibres satisfy `c=m-q` and `c'=m-q'`. Substitute in PP3bmj. ∎

Thus a clean rotation is charge-favourable when it touches many distinct source
components and does not increase the parity-edge count.

## 3. Charge-aware clean rotations through `m=9`

For one clean source cycle and one owner triple `S`, examine every clean
successor rotation whose source triple intersects `S` and maximize

```text
Delta = r(S)+c'-c.
```

### Theorem PP3bml -- VERIFIED FINITELY

For every `4<=m<=9`, every parity-satisfiable Hamilton cycle, and every
three-owner set, there is a clean owner-intersecting rotation with

```text
Delta >= 3.
```

Consequently every audited owner triple admits a labelled fibre-regenerated
macro action whose column mass is at most

```text
1/8.
```

The exact best-exponent distributions are:

| `m` | distribution of best `Delta` over clean-cycle/owner-triple pairs |
|---:|---|
| 4 | `3:20, 4:4` |
| 5 | `3:88, 4:100, 5:32` |
| 6 | `3:728, 4:890, 5:532, 6:90` |
| 7 | `3:5,242, 4:9,042, 5:7,134, 6:1,722, 7:100` |
| 8 | `3:43,134, 4:78,402, 5:56,592, 6:17,922, 7:2,252, 8:50` |
| 9 | `3:495,222, 4:950,218, 5:797,738, 6:341,198, 7:70,986, 8:6,322, 9:108` |

#### Verification

Run

```bash
python scripts/check_hamilton_parity_fibre_charge.py \
  experiments/hamilton-parity-fibre-charge-audit.json
```

The checker reconstructs every clean parity graph, labels its components,
enumerates every clean owner-intersecting rotation, and compares the exact
best-exponent distributions against the stored ledger. ∎

The lower endpoint `Delta=3` persists at every audited size; finite data do not
show a growing guaranteed exponent.

## 4. Relation to immediate and mixed charges

### Corollary PP3bmm -- PROVED / FRONTIER REFINED

Exact fibre regeneration can preserve the immediate three-owner charge scale
`1/8` while making the target orientation conditionally uniform.  It does not by
itself reach the stationary atomic scale `Theta(n^-3)`.

The remaining charge loss is therefore localized to two issues:

1. **cycle-coordinate concentration:** the target Hamilton cycle is not mixed;
2. **label merging:** if several admissible rotation labels are combined into one
   action, their predecessor masses may accumulate in one output column.

A useful next theorem would choose or weight labels so that the merged column
sum remains close to the best labelled bound while the cycle coordinate spreads
through the logarithmic trajectory window of `docs/317`.

The exact `1/8` labelled bound through `m=9` is finite evidence, not an
asymptotic action-charge theorem.
