# Marked source-star credit diagnostic

Run

```text
python scripts/check_marked_source_star_credit.py \
  experiments/marked-source-star-credit-example.json
```

The stored instance has ambient size `Q=7`, marked subbank size `q=4`, and five
credit lines through the distinguished centre.  Each off-diagonal line trace is
a partial matching on the six noncentre endpoint indices.

The checker enumerates all marked four-subbanks and all derangements of each
subbank.  There are 180 states.  The exact average selected-credit
self-recapture is

```text
5/3,
```

while PP3agj gives the upper bound

```text
C(q-2)/(Q-2)=5*2/5=2.
```

The best state recreates one selected credit incidence.  With five units of
removal credit and zero foreign cost, its potential change is `-4`, so the
stored instance returns `paid_completion`.

The input field `foreign_cost_per_state` may be increased to exercise the
foreign-or-host obstruction branch.  The diagnostic is deliberately finite:
it tests the exact marked probability and credit arithmetic, not the asymptotic
source-valid host preparation in PP3agm.
