# Weighted slot-mass endpoint regression

This experiment validates the rational checker for PP3fi.

Run

```bash
python scripts/check_weighted_slot_mass.py \
  experiments/weighted-slot-mass-example.json
```

The fixture has four slots, six rank-two events of probability `1/100`, and four
rank-three events of probability `1/200`.

Every slot belongs to three pair events and three triple events, so its exact
incident probability mass is

\[
 3\cdot\frac1{100}+3\cdot\frac1{200}
 =
 \frac9{200}
 =0.045.
\]

Thus

```text
maximum event probability             1/100
maximum incident probability mass     9/200
PP3fi simple criterion                 true
```

The checker also evaluates the exact asymmetric-LLL inequalities with activities
`x_E=2 Pr(E)`.

For a pair event, the neighbor activity sum is `3/25`; for a triple event it is
`3/20`.  Both are below the proof threshold `1/2`, and every exact activity
inequality holds.

The fixture is intentionally small.  Its role is to distinguish the weighted
criterion from raw occurrence: changing one event into many lower-probability
events can leave the incident mass unchanged even though the event count grows.
