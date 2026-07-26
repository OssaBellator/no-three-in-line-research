# Layerwise complete insertion-cancellation diagnostic

Run

```text
python scripts/check_layerwise_complete_cancellation.py \
  experiments/layerwise-complete-cancellation-example.json
```

The stored first trade inserts twelve cells split across two permutation layers:

```text
layer sizes [7, 5].
```

Its insertion table has total multiplicity `1,000`:

- `420` incidences use only layer zero;
- `330` use only layer one;
- `250` use cells from both layers.

The first layerwise zero-cost trade removes `670` units, including every cross-layer
incidence.  The second removes the remaining `330`.  Thus each first-step incidence
is removed exactly once.

The square-root helper demand is

```text
7^2+5^2=74 <= 12^2=144.
```

The exact expected output is

```text
layer sizes [7, 5]
total marked size 12
layer helper square volume 74
global square budget 144
first insertion cost 1000
layerwise removed insertion [670, 330]
second insertion costs [0, 0]
first removal credit 12
composite change -12
composite upper bound -12
outcome layerwise_complete_insertion_cancellation
```

This verifies PP3asm--PP3aso: layerwise helper demand remains within the global
square budget, and sequential zero-cost trades cancel the complete first insertion
table, including cross-layer incidences.
