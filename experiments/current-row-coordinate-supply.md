# Current-row coordinate-supply diagnostic

This diagnostic exercises the finite reservation inequality behind
`docs/271-current-row-coordinate-cover-elimination.md`.

Run:

```bash
python scripts/check_current_row_coordinate_supply.py \
  experiments/current-row-coordinate-supply-example.json
```

The checker computes the permanent slab reservation, subtracts the additional
internal reservation census, and verifies that every marked block has more than
`C h^2` available coordinates.  It also checks the aggregate
sum-of-squares helper requirement.

The stored finite instance is illustrative.  The asymptotic theorem uses the
slab inequalities `MR=(ab+o(1))m` with `ab<1` and
`W^2=Theta(R)=o(m)`.
