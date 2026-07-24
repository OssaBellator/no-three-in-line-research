# Multistate trade-bank regression

This experiment validates the exact finite-state CSP in
[`docs/46-multistate-trade-banks.md`](../docs/46-multistate-trade-banks.md).

The fixture
[`four-state-trade-bank-n4.json`](four-state-trade-bank-n4.json)
groups the two independent rectangle variables from the side-six regression
into one four-state equal-margin variable.

The command is

```bash
python scripts/solve_multistate_trade_bank.py \
  experiments/four-state-trade-bank-n4.json
```

The exact output has the following key values:

```text
variable_count                         1
state_counts                           [4]
candidate_collinear_triples            18
locally_impossible_triples             10
distinct_bad_box_count                 4
distinct_bad_box_rank_histogram        {1: 4}
uniform_bad_box_expectation            3/2
maximum_bad_box_probability            1/2
maximum_dependency_degree              3
symmetric LLL exact left side          6
satisfiable                             true
selected state                         3
```

The selected state produces the saturated no-three configuration

```text
(1,1), (1,3), (2,4), (2,5),
(3,2), (3,6), (4,1), (4,2),
(5,5), (5,6), (6,3), (6,4).
```

This is a useful separation of roles.  The first-moment and conservative
bounded-dependency criteria are sufficient but not necessary, while the exact
forbidden-box solver still finds the clean state.  In an asymptotic sheared-rung
bank, the large state sets are intended to reduce the bad-box probabilities
until PP3bj or PP3bk becomes effective.