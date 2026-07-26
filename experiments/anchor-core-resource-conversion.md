# Anchor-core energy resource-conversion diagnostic

Run

```text
python scripts/check_anchor_core_resource_conversion.py \
  experiments/anchor-core-resource-conversion-example.json
```

The stored abstract core uses

```text
W=100,
D_m=5,
R=1,000,000.
```

Its physical controller--anchor graph is the disjoint union of four copies of
`K_(99,99)`.  Every physical pair is counted with the maximum permitted
slot/divisor multiplicity

```text
W D_m=500.
```

The exact output is

```text
W 100
D_m 5
distinct pair count 39204
slot-expanded energy 19602000
core threshold 10000000
pair lower bound 39204.0
maximum source degree 99
exact matching size 396
matching lower bound 196.02
one-layer anchor bank 100
post-puncture domain lower bound 549900
puncture/domain ratio 0.0001
outcome batch_punctured_anchor_endpoint_bank
```

The maximum source degree is below the star threshold `W`, while the exact
endpoint-disjoint matching is large enough that pigeonholing the anchor endpoints
between the two permutation layers still leaves a target-size bank.  Puncturing
all selected anchors costs at most `W` values in any one macro, which is negligible
compared with `R`.

The checker verifies the physical-pair multiplicity cap, the energy threshold
`2D_mW^3`, the graph-matching lower bound, the one-layer refinement, and the
cumulative batch-puncture domain cost.
