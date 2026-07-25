# Dynamic candidate-cell shadow diagnostics

This experiment accompanies
[`docs/101-dynamic-pool-excess-shadow-potential.md`](../docs/101-dynamic-pool-excess-shadow-potential.md)
and
[`scripts/analyze_dynamic_cell_shadow.py`](../scripts/analyze_dynamic_cell_shadow.py).

Run

```bash
python scripts/analyze_dynamic_cell_shadow.py \
  certificates/prime-patching-small.json \
  --labels 12
```

For each deterministic matching layer, the whole layer is used as one controller
pool.  There are twelve movement labels and twelve refill labels, hence `24n`
candidate cells at side `n`.

## Exact results

| Side | Candidate cells | Bad cell entries | Excess potential `Xi` | Maximum excess at one cell |
|---:|---:|---:|---:|---:|
| 2 | 48 | 0 | 0 | 0 |
| 3 | 72 | 6 | 6 | 1 |
| 4 | 96 | 11 | 13 | 2 |
| 5 | 120 | 31 | 36 | 3 |
| 6 | 144 | 51 | 66 | 2 |
| 7 | 168 | 98 | 128 | 3 |
| 8 | 192 | 122 | 168 | 3 |
| 9 | 216 | 148 | 237 | 4 |
| 10 | 240 | 172 | 276 | 3 |

The two deterministic matching layers give identical rows in this table.

For every one of the `2,592` tested layer-labelled candidate cells, the program
verified all of the following exactly.

1. There is exactly one horizontal or vertical blocker pair.
2. That axis pair contains the current controller point.
3. Every other blocker pair is nonaxis.
4. No nonaxis blocker pair contains the controller point.
5. The number of nonaxis blocker pairs equals `blocker_pair_count-1`.
6. The number of bad candidate cells is at most `Xi`.

## Interpretation

The experiment confirms that controller-aware cell safety depends only on the
excess nonaxis blocker shadow, not on the current pairing of old columns and rows
inside the matching pool.  This is the invariant used by PP3ku--PP3kz to permit
within-pool controller permutations while keeping the candidate-cell universe
fixed.

The finite values are not asymptotic evidence for small shadow: at sides seven
through ten most labelled cells are bad.  Their role is to validate the exact
axis subtraction and the pairing-invariance of the potential.
