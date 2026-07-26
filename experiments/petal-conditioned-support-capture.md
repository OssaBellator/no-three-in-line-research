# Petal-conditioned complete-support diagnostic

Run

```text
python scripts/check_petal_conditioned_support_capture.py \
  experiments/petal-conditioned-support-capture-example.json
```

The first stored petal is the directed path

```text
0->1->2
```

inside a six-index single cycle.  Its three selected helpers form an independent
set in the residual helper-support hypergraph.  The second petal consists of two
disjoint fixed arcs

```text
0->1,
2->3.
```

The exact output is

```text
path cycle size 6
path fixed arcs 2
path conditional cycles 6
path formula count 6
path selected residual supports 0
path local arcs [(0, 1), (1, 2)]
path deterministic local cost 7
path removal credit 10
path outcome zero_residual_paid_path
fan cycle size 6
fan fixed arcs 2
fan conditional cycles 6
fan formula count 6
fan selected residual supports 0
fan local bridge 1->2 count 2
fan local bridge 3->0 count 2
fan expected local core cost 2.333333333333
fan outcome finite_local_core_only
outcome petal_conditioned_complete_support_capture
```

Both conditional cycle counts equal

```text
(6-2-1)!=6.
```

For the spanning path, the only selected arcs with both endpoints in the fixed
three-vertex core are the two prescribed path arcs.  All helper-supported source
and insertion patterns are absent, so the stored deterministic cost `7` is paid
by credit `10`.

For the disconnected partner petal, the only weighted local bridges in the stored
table are `1->2` and `3->0`.  Each occurs in two of the six completions, giving
expected local-core cost

```text
(2*3+2*4)/6=7/3.
```

Every nonlocal residual pattern is excluded by the independent helper set.
