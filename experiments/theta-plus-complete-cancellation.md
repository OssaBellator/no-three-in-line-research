# Complete Theta-plus insertion-cancellation diagnostic

Run

```text
python scripts/check_theta_plus_complete_cancellation.py \
  experiments/theta-plus-complete-cancellation-example.json
```

The stored first package inserts six points split across three post-trade blocks:

```text
E0={d0,d3},
E1={d1,d4},
Q ={d2,d5}.
```

Its new current incidences have total multiplicities

```text
Xi_cell 21,
Xi_old  15,
Lambda  15,
```

for complete first insertion cost 51.  The original removal credit is 14, so the first
step alone changes the enlarged potential by `+37`.

Assign every new incidence to the first block deleting one of its inserted supports.
The removal totals are

```text
E0 25,
E1 17,
Q   9,
```

which sum to the complete first insertion table.  When the three blockwise second
cycles have zero current insertion, their change is `-51`, and the composite change is
exactly `-14`.

The expected output is

```text
inserted points 6
block order ['E0', 'E1', 'Q']
first insertion by table {'Lambda': 15, 'Xi_cell': 21, 'Xi_old': 15}
complete first insertion 51
first removal credit 14
first-step change 37
later removal by block {'E0': 25, 'E1': 17, 'Q': 9}
complete later removal 51
later zero-insertion change -51
composite change -14
assigned records 30
outcome theta_plus_complete_insertion_cancellation
```

The example includes singleton and cross-block binary records in both fixed pair
potentials, together with anchor records supported by new anchors, new controller
edges, or both.  It checks the first-deletion assignment used in PP3azs--PP3azw.
