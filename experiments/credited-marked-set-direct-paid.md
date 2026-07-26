# Credited marked-set direct-paid diagnostic

Run

```text
python scripts/check_credited_marked_set_direct_paid.py \
  experiments/credited-marked-set-direct-paid-example.json
```

The stored credited marked set has ten current source cells split between two
permutation layers as `6+4`.  Its designated credit consists of eighteen and twelve
within-layer incidences plus seven cross-layer incidences, for total credit

```text
37.
```

The first zero-cost layer cycle removes its eighteen local units and all seven
cross-layer units.  The second removes the remaining twelve.  Every designated
incidence is therefore removed exactly once, and the direct package has potential
change

```text
0-(25+12)=-37.
```

The layerwise helper-square demand is `6^2+4^2=52<=100`.  Even if all selected
marked/helper indices are controllers, only twenty values are punctured, a ratio of
`0.002` to `R=10,000`.

The exact output is

```text
layer marked sizes [6, 4]
total marked size 10
within-layer designated credit [18, 12]
cross-layer designated credit 7
total designated credit 37
layerwise removals [25, 12]
layerwise insertion costs [0, 0]
composite change -37
layerwise square demand 52
global square budget 100
selected controller punctures 20
puncture to R ratio 0.002
outcome credited_marked_set_direct_paid_trade
```

This verifies PP3auc--PP3aue in a finite two-layer model with cross-layer credit.
