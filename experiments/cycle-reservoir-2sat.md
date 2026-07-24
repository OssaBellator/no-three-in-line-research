# Cycle-reservoir 2-SAT experiments

These checks use
[`scripts/solve_matching_reservoir_2sat.py`](../scripts/solve_matching_reservoir_2sat.py)
and the exact reduction in
[`docs/40-cycle-reservoir-2sat.md`](../docs/40-cycle-reservoir-2sat.md).

## Side-four parabolic reservoir

Run:

```bash
python scripts/solve_matching_reservoir_2sat.py \
  certificates/prime-patching-small.json \
  experiments/parabolic-variable-bank-n4.json \
  --n 4 --t 2 \
  --columns 1,2,3,4 --rows 1,2,3,4
```

The induced reservoir graph has two four-cycles and therefore two Boolean
variables.  The fixed internally clean parabolic patch creates 19 external
geometric certificates before deletion choices are applied:

```text
14 retained-pair / inserted-cell certificates
5 retained-anchor / inserted-pair certificates
```

Eight certificate assignments are impossible automatically because their old
points lie in opposite alternating classes on one cycle.  The remaining
certificates reduce, after deduplication, to:

| Clause type | Count |
|---|---:|
| Unary | 4 |
| Binary | 2 |
| Total | 6 |

The four unary clauses include both values of each cycle variable.  Equivalently,
the implication graph places all four literals in one strongly connected
component.  The formula is therefore unsatisfiable.

The six distinct clauses, using variables `x0,x1`, are:

```text
not x0
x0
not x1
x1
(not x0 or x1)
(x0 or x1)
```

The exact choice of Boolean labels depends on the alternating-class convention;
unsatisfiability does not.

## Interpretation

The 2-SAT reduction is strictly sharper than expectation.  The uniform
variable-reservoir average is `17/4`, but that value alone does not explain why
all four states fail.  The implication graph gives the complete reason: each
cycle is independently forced to both alternating classes by unary external
certificates.

A positive geometry-aligned cycle construction must prevent this unary
contradiction first.  Binary clauses are not inherently fatal; a dense binary
constraint graph can remain satisfiable when its implication components avoid a
variable and its negation.  Thus the next finite and asymptotic target is to
install reservoir cycles for which:

1. no cycle receives conflicting unary requirements;
2. binary certificate clauses have a satisfiable parity/implication structure.
