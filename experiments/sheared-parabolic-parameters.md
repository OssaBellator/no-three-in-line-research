# Sheared parabolic parameter sweep

This experiment uses
[`scripts/search_sheared_parabolic_parameters.py`](../scripts/search_sheared_parabolic_parameters.py)
and the internally clean bank from
[`docs/41-sheared-parabolic-banks.md`](../docs/41-sheared-parabolic-banks.md).

The exact command was

```bash
python scripts/search_sheared_parabolic_parameters.py \
  certificates/prime-patching-small.json \
  --widths 2,3 --max-scale 10 --shear-min -5 --shear-max 10
```

Movement and refill components were allowed independent scale, branch-gap,
shear, and offset parameters.  Every candidate was checked with exact integer
determinants.  Internal patch triples were identically zero, as predicted by
PP3aq and PP3ad.

## Results

| Source `n` | Width `t` | Component patterns | Parameter tuples with matchings | Matching-reservoir states | Minimum external triples | Clean states |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 6 | 36 | 144 | 3 | 0 |
| 5 | 2 | 19 | 361 | 361 | 3 | 0 |
| 6 | 2 | 46 | 875 | 875 | 1 | 0 |
| 7 | 2 | 89 | 1,513 | 1,672 | 5 | 0 |
| 8 | 2 | 155 | 3,253 | 3,253 | 6 | 0 |
| 9 | 2 | 245 | 4,820 | 4,820 | 7 | 0 |
| 10 | 2 | 365 | 7,691 | 7,691 | 7 | 0 |

There are no feasible width-two patterns for `n<=3`.  At width three, the
specified parameter range produces only one geometrically feasible component
pattern, at `n=10`, and no movement/refill parameter pair has a matching
reservoir in the stored source certificate.

Across the searched width-two cases there are `18,816` matching-reservoir
states and no clean patch.  The minimum is attained at `n=6`: the best state
has no old-pair blocked inserted cell and exactly one retained-anchor triple.

## Interpretation

The shear parameter succeeds at its intended combinatorial task:

- it enlarges the matching-admissible parameter family from the unsheared
  `40` states in the earlier parameter sweep to `18,816` states;
- every inserted state remains internally no-three;
- the best finite external obstruction falls from three triples to one.

It does not by itself solve seed preparation.  The remaining single-triple
examples show that the decisive issue is now the correlation between matching
deletions and retained-anchor or retained-pair geometry.  The natural next
steps are the exact PP2l joint expectation, cycle-reservoir 2-SAT, or a
prepared source construction that forces the final certificate anchor into the
deletion reservoir.
