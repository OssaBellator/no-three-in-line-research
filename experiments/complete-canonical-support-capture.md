# Complete canonical support-capture diagnostic

Run

```text
python scripts/check_complete_canonical_support_capture.py \
  experiments/complete-canonical-support-capture-example.json
```

The stored state has six endpoint indices.  The checker enumerates every directed
single cycle with the marked centre fixed first.  The exact output is

```text
cycle size 6
directed single cycles 120
diagonal arc occurrences 0
transposition occurrences 0
nonzero canonical classes 9
maximum helper rank 5
residual support edges 4
independent helper block [2, 4]
selected residual supports 0
source-invalid count 0
insertion cost 0
outcome zero_insertion_support_independent_state
```

The cycle count is `(6-1)!=120`.  No cycle contains a diagonal arc or a directed
2-cycle, verifying the deterministic disappearance of `A_1` and `B_2`.

The nine remaining canonical classes have helper ranks

```text
source: 1,2,3,3,4,5
Xi:     1,2,3.
```

The stored residual support hypergraph is

```text
{1}, {2,3}, {4,5}, {1,2,4}.
```

The helper set `{2,4}` contains none of these supports.  Therefore every canonical
source-invalid and positive insertion signature is absent, illustrating the exact
zero-insertion conclusion PP3aof--PP3aog.
