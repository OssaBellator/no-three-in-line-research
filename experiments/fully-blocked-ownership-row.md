# Fully blocked ownership-row diagnostic

Run

```text
python scripts/check_fully_blocked_ownership_row.py \
  experiments/fully-blocked-ownership-row-example.json
```

The stored dead movement row uses

```text
W=100,
R=10,000,
T=1,000,
delta=0.5.
```

The exact mass identity requires more than

```text
delta R T=5,000,000
```

combined units of macro refill-cell defect and same-slot anchor row mass.  The
stored values split this as `4,000,000+1,500,000`, so the macro refill-defect
branch is forced.

The exact output is

```text
W 100
R 10000
T 1000
required combined mass 5000000.0
macro refill defect mass 4000000
anchor row mass 1500000
resource threshold W*T 100000
greedy bank lower bound 10.0
star partner lower bound 99.0
outcome fixed_macro_refill_resource_conversion
```

The resource threshold `WT` gives the exact dichotomy used in PP3alo.  A source
resource above that threshold yields approximately `W` distinct blocker partners;
otherwise the four-resource greedy matching has target order `Omega(W)`.

The checker verifies the dead-row mass identity, its two-way split, the fixed-
macro resource threshold, and the star/matching lower bounds.
