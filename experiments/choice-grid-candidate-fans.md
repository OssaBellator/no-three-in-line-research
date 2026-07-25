# Choice-grid candidate-fan diagnostic

This check accompanies
`docs/192-choice-grid-candidate-fan-localization.md`.

Run:

```bash
python scripts/check_choice_grid_candidate_fans.py \
  experiments/choice-grid-candidate-fans-example.json
```

The stored instance is a complete `5 x 5` choice grid. Every state receives two
candidate colours

```text
0:(a+b mod 5),  1:(a+b mod 5).
```

Each of the ten candidate colour classes is a perfect matching, so the matching
condition PP3afh is exact. There are 25 states and 50 candidate incidences.
Every row and every column has five distinct partners and ten distinct candidates.
Thus the best fixed-cell fan has

```text
partner support:       5
candidate incidences: 10
```

which attains the weighted average bound `50/5=10`. With removal credit two,
this is the model equality `R_* q=10` in PP3afk.

The diagnostic checks matching-colour injectivity and weighted fan extraction.
It does not pay the conditional residual host after the fan centre is fixed.
