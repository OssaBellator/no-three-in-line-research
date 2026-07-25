# Cross-block supervariable regression

This experiment accompanies
[`docs/131-credit-poor-cross-block-supervariables.md`](../docs/131-credit-poor-cross-block-supervariables.md),
[`scripts/check_cross_block_supervariable.py`](../scripts/check_cross_block_supervariable.py),
and
[`cross-block-supervariable-example.json`](cross-block-supervariable-example.json).

Run

```bash
python scripts/check_cross_block_supervariable.py \
  experiments/cross-block-supervariable-example.json
```

## Unique safe state

The first fixture has four formal cross-block matchings.  One direct-recapture
cell is forbidden in each distinguished owner column.  Two additional unary
cells force the opposite bijections.

Exactly one state is both credit-preserving and source-safe:

```text
s0 -> T1
s1 -> T0
t0 -> S0
t1 -> S1
```

Thus the fixture verifies:

```text
cross-block states          = 4
credit-preserving states    = 1
source-safe states          = 1
```

## Exact Hall failure

The second fixture again has one formally credit-preserving state before general
unary pruning.  The cells

```text
u1 -> V0
u1 -> V1
```

are then both forbidden, so `u1` is isolated in the forward `2 by 2` host.  The
checker returns the Hall witness

```text
left set     = {u1}
neighborhood = empty
deficiency   = 1
```

and reports no source-safe cross-block state.

These finite fixtures validate the four-state enumeration, designated-credit
exclusions, and exact small Hall obstruction.  They do not establish that a
positive fraction of an asymptotic geometric rectangle bank has matchable
cross-block hosts.
