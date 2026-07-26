# Local atom two-step cancellation diagnostic

Run

```text
python scripts/check_local_atom_two_step_cancellation.py \
  experiments/local-atom-two-step-cancellation-example.json
```

The stored first trade has removal credit `100`, one selected local atom of weight
`1000`, and other insertion cost `20`.  Its one-step potential change is therefore

```text
1000+20-100=920.
```

A second marked trade moves one inserted endpoint belonging to every selected atom
incidence.  It recreates `5` units of the atom and has foreign cost `30`, so its
change is

```text
5+30-1000=-965.
```

For each of `A2`, `B3`, and `B4`, the expected output is

```text
atom weight 1000
first-step change 920
second-step change -965
composite change -45
```

The reduced composite formula is

```text
20+5+30-100=-45.
```

Thus the complete atom weight cancels exactly.  Only first-step nonatom cost,
second-step self-recapture, and second-step foreign cost remain against the
original first-step removal credit.
