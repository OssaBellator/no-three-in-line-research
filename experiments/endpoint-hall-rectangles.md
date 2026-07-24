# Endpoint Hall rectangle diagnostics

This experiment accompanies
[`docs/97-zero-unary-shadow-hall-rectangles.md`](../docs/97-zero-unary-shadow-hall-rectangles.md)
and
[`scripts/analyze_endpoint_hall_rectangles.py`](../scripts/analyze_endpoint_hall_rectangles.py).

Run

```bash
python scripts/analyze_endpoint_hall_rectangles.py \
  certificates/prime-patching-small.json
```

The current finite corpus supplies only the source-unary part of the future
zero-shadow host.  Recapture and insertion-shadow supports require a prepared
resource bank and are therefore not present in these whole-layer diagnostics.

## Full endpoint-safe hosts

For sides `3` through `10`, every full endpoint-safe host has a perfect matching
except side `9`, layer `0`.  The exact Hall witness there is

```text
X = {0,1,2,3,4,5,6,7,8},
N(X) = {0,2,3,4,5,6,7,8},
Y = {1}.
```

Thus

```text
|X| = 9,
|N(X)| = 8,
|Y| = 1,
|X|+|Y| = 10 > 9.
```

The forbidden rectangle is the complete `9 by 1` fibre

```text
X times Y.
```

This is the near-complete-fibre alternative of PP3ka, not a macroscopic balanced
rectangle.

At side `2`, both hosts are empty because the diagonal is forbidden and every
off-diagonal cell is occupied by the opposite matching layer.  The Hall witness
is the complete `2 by 2` forbidden rectangle.

## PP3is-pruned hosts

The deterministic PP3is pruning preserves a perfect matching on every stored
host except side `2` and side `5`, layer `0`.

For side `5`, layer `0`, the retained active index set has size three and the
exact witness is

```text
X = {1,4},
N(X) = {0},
Y = {1,4}.
```

Hence

```text
|X| = 2,
|N(X)| = 1,
|Y| = 2,
|X|+|Y| = 4 > 3,
rectangle area = 4.
```

The obstruction is an exact `2 by 2` forbidden rectangle in the induced
three-index endpoint host.

## Interpretation

The finite failures already show both Hall-rectangle regimes of PP3ka:

- an almost-complete single fibre (`9 by 1`);
- a balanced small forbidden rectangle (`2 by 2`).

The diagnostic therefore returns substantially more structural information than
a maximum-matching size alone.  These examples are finite source-unary stress
tests, not asymptotic obstructions to the controller-shadow conversion theorem.
