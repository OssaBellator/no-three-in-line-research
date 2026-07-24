# Parabolic matching reservoir experiments

These computations use
[`scripts/analyze_parabolic_matching_reservoir.py`](../scripts/analyze_parabolic_matching_reservoir.py)
and the construction in
[`docs/36-monotone-parabolic-reservoirs.md`](../docs/36-monotone-parabolic-reservoirs.md).
All geometry uses exact integer determinants.

## Width-two scan on the stored certificate corpus

The command

```bash
python scripts/analyze_parabolic_matching_reservoir.py \
  certificates/prime-patching-small.json --widths 2
```

uses the smallest monotone parameters `L=2,d=1`.  For `t=2`, each old
coordinate set is a translated copy of

```text
{0,1,2,3}.
```

A candidate reservoir is a four-edge matching between one translated row set
and one translated column set.  The deterministic replacement inserts eight
points and extends side `n` to side `n+2`.

| Source `n` | Matching reservoirs | Minimum blocked-cell triples | Minimum retained-anchor triples at the same candidate | Minimum total triples | Clean patches |
|---:|---:|---:|---:|---:|---:|
| 2 | 0 | -- | -- | -- | 0 |
| 3 | 0 | -- | -- | -- | 0 |
| 4 | 4 | 0 | 3 | 3 | 0 |
| 5 | 4 | 1 | 3 | 4 | 0 |
| 6 | 2 | 2 | 1 | 3 | 0 |
| 7 | 1 | 9 | 6 | 15 | 0 |
| 8 | 3 | 8 | 5 | 13 | 0 |
| 9 | 0 | -- | -- | -- | 0 |
| 10 | 0 | -- | -- | -- | 0 |

For `n=2,3`, the four-coordinate pattern does not fit.  For `n=9,10`, it fits
but the stored certificate contains no matching between any feasible translated
row and column patterns.

## Internal-geometry check

Every enumerated candidate has exactly zero internal patch triples.  This is an
independent finite regression check of PP3ac--PP3ae:

- each movement component is a translated monotone double parabola;
- each refill component is its transpose;
- every movement--refill line has negative slope, while every nonaxis secant
  inside either component has positive slope.

Thus all residual defects in the table are genuinely external.  They split
between:

1. one inserted point on a secant of two retained points;
2. two inserted points collinear with one retained anchor.

## Best finite candidates

The two minimum-three cases are:

```text
n=4, column offset 1, row offset 1
blocked-cell triples: 0
retained-anchor triples: 3

delete:
(1,3), (2,4), (3,2), (4,1)
```

and

```text
n=6, column offset 3, row offset 1
blocked-cell triples: 2
retained-anchor triples: 1

delete:
(3,2), (4,1), (5,4), (6,3)
```

Neither is a valid extension, but they demonstrate that the matching-reservoir
condition occurs naturally in small saturated configurations and that the
construction removes the entire internal-triple obstruction exactly.

## Interpretation

The parabolic ladder solves a different part of PP3 than the full row-lift
bank.  It supplies one deterministic internally clean state at square-root
width, rather than a large spread state space.  The finite failures therefore
do not come from candidate-only triples or movement/refill interaction.  The
remaining target is to prepare many such matching reservoirs with low retained
secant and retained-anchor incidence, or to combine the construction with the
variable-reservoir selection machinery.
