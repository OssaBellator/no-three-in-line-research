# Pool-compatible paired secant-switch diagnostic

Run

```text
python scripts/check_pool_compatible_paired_secant_switch.py \
  experiments/pool-compatible-paired-secant-switch-example.json
```

The stored model has twelve secant records.  Their tentative pivots are arcs of one
12-cycle and their witness pivots are arcs of a second 12-cycle with step five.

Two records conflict when their tentative arcs or witness arcs are adjacent.  The
conflict graph has maximum degree four.  A greedy matching in its complement pairs all
twelve records:

```text
[(0,2),(1,3),(4,6),(5,7),(8,10),(9,11)].
```

For the sample pair `(0,2)`, the tentative-block switch is

```text
{0->1,2->3}  to  {0->3,2->1},
```

and the witness-block switch is

```text
{0->5,2->7}  to  {0->7,2->5}.
```

Each switch preserves its own row and column resource sets, every crossed arc remains
off diagonal, and all four original pivots are omitted.

The expected output is

```text
secant records 12
tentative cycle step 1
witness cycle step 5
conflict maximum degree 4
paired switches 6
unpaired records []
record pairs [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11]]
sample tentative diagonal [[0, 1], [2, 3]]
sample tentative cross [[0, 3], [2, 1]]
sample witness diagonal [[0, 5], [2, 7]]
sample witness cross [[0, 7], [2, 5]]
tentative resources preserved True
witness resources preserved True
all four pivots omitted True
outcome pool_compatible_paired_secant_switch
```

This checks PP3azk--PP3azm in a tight two-cycle model and demonstrates why the paired
product, unlike a direct cross-pool diagonal, preserves both permanent blocks.
