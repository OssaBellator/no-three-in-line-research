# Hamilton targeted-switching drift census

Run:

```bash
python scripts/check_hamilton_targeted_switching_drift.py \
  experiments/hamilton-targeted-switching-drift-audit.json
```

The checker exhausts every signed Hamilton state for pair sizes `m=4,5,6` and
every occurrence of a collinear triple supported on three distinct orbit owners.
For each occurrence it performs the unique three-edge successor rotation and all
eight choices of the new orientation bits.

Four potentials are audited:

1. total collinear triples;
2. number of occupied lines with at least three selected cells;
3. total line excess `sum_L max(0,|L cap P|-2)`; and
4. targetable collinear triples with three distinct orbit owners.

For total collinear triples the exact occurrence-weighted mean drifts under
uniform fresh signs are

```text
m=4: -28/13
m=5: -567/118
m=6: -2057/494.
```

Thus targeted switching has negative average finite drift in this range.
However the drift is not pointwise.  At `m=5` there is a state and targeted
source triple with four old collinear triples for which the eight outputs have

```text
24,20,24,20,20,20,24,24
```

triples.  At `m=6` an eight-triple state has output counts

```text
48,48,48,48,48,44,48,44.
```

Even the best sign choice therefore increases the potential by `16` and `36`,
respectively.

The state-level greedy census also finds many nonvalid local minima.  For total
triple count:

| `m` | signed Hamilton states | valid | improvable | local minima | defective with no targetable triple |
|---:|---:|---:|---:|---:|---:|
| 4 | 96 | 16 | 44 | 36 | 0 |
| 5 | 768 | 16 | 532 | 188 | 32 |
| 6 | 7,680 | 0 | 6,600 | 1,048 | 32 |

Analogous local minima occur for bad-line count, line excess, and targetable
triple count.  The support-three kernel is therefore a useful stochastic repair
primitive but none of these four raw potentials supplies monotone termination.
The census is finite evidence and a finite obstruction only; it does not decide
asymptotic drift after geometric weighting or multi-step scheduling.
