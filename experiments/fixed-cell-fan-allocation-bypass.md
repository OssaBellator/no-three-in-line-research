# Fixed-cell fan allocation-domain diagnostic

Run

```text
python scripts/check_fixed_cell_fan_allocation_bypass.py \
  experiments/fixed-cell-fan-allocation-bypass-example.json
```

The stored instance fixes one endpoint centre and eight compatible partner cells.
The partner cells form a matching and determine eight distinct nonaxis lines
through the centre.  Candidate intersections are tested against six movement
labels and six refill labels in an identity controller layer split among three
macros.

The exact output is:

```text
residual matching size          8
movement candidate entries      7
refill candidate entries        7
maximum movement-label load     4
maximum refill-label load       4
maximum movement-controller load 2
maximum refill-controller load   2
trace degree bound              8
maximum one-domain loss         3
general domain-loss bound       16
base domain size                60
post-fan lower bound            57
allocation threshold            40
outcome                         direct_allocation_bypass
```

The example deliberately contains both movement and refill candidate entries.
The maximum loss from any one macro domain is only three, while PP3agw permits
`2n=16`.  The stored margin satisfies

```text
2n=16 <= xi R=20,
```

and the post-fan domain lower bound `57` remains above `gamma R=40`.

The diagnostic checks simple candidate-entry support, not weighted `Xi`
multiplicity.  This is the point of the theorem: arbitrarily many candidate
incidences may lie on one selected secant line, but that line still removes at
most one movement entry at a prescribed movement label and at most one refill
entry at a prescribed refill label.
