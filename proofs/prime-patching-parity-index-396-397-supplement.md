# Prime-patching parity index supplement: `docs/396--397`

This supplement extends `proofs/prime-patching-parity-index.md` and the
`docs/391--395` supplement without replacing their cumulative history.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bvy--PP3bwb | Exact recleaning cost is within additive three of weighted boundary minority mass; minority mass is equivalent within factor two to opposite-phase pair energy; every conflict has a parity-odd path witness of length at most six | PROVED | `docs/396-boundary-phase-impurity-and-conflict-energy.md` |
| PP3bwc--PP3bwe | Boundary minority is the exact weighted cover and fractional packing value of the complete phase-conflict graph; bounded component size turns large impurity into a large complete bipartite bank of six-edge witnesses | PROVED | `docs/397-boundary-conflict-covers-and-biclique-localization.md` |

## Frontier update

The recleaning obstruction is now separated from the three owner bits. If `Q`
is the total minority mass of boundary-component phases, then

```text
Q <= c_min <= Q+3.
```

Writing `E_R` for the weighted opposite-phase pair energy in a graph component,

```text
sum_R E_R/B_R <= Q <= 2 sum_R E_R/B_R.
```

Thus a low expected pair-conflict energy over covering rotations gives a low-cost
rotation by averaging. Conversely, large cost gives an exact weighted conflict
packing, and under a boundary-component size cap it gives a complete two-sided
bank of bounded parity-odd path witnesses. The next geometric task is to bound
that witness-bank mass or convert a dense bank into another improving rotation.

The exact finite identities are checked by

```bash
python scripts/check_boundary_phase_impurity.py \
  experiments/boundary-phase-impurity-example.json
```

The next available theorem identifier is `PP3bwf`.
