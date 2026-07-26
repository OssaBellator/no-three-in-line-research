# Fixed-label blocker-fibre diagnostic

Run

```text
python scripts/check_fixed_label_blocker_fibre.py \
  experiments/fixed-label-blocker-fibre-example.json
```

The stored movement-label fibre has

```text
W=100,
R=100,000,
delta=0.30.
```

Its chosen blocker graph is the disjoint union of four copies of `K_(99,99)`.
Every bad entry has a unique controller resource disjoint from all blocker
vertices.  The exact output is

```text
W 100
R 100000
bad fixed-label entries 39204
delta R threshold 30000.0
maximum blocker degree 99
exact resource matching 396
greedy resource lower bound 129.3861386138614
one-layer endpoint bank 100
batch puncture ratio 0.001
outcome fixed_label_resource_bank
```

The blocker degree is below the star threshold `W`, so the diagnostic enters the
three-resource matching branch.  The exact matching remains large enough after
pigeonholing blocker endpoints between the two permutation layers to retain a
size-`W` endpoint bank.  Puncturing every selected endpoint in one macro would
cost only `W/R=0.001` of that macro's controller domain.

The checker verifies the fixed-label fibre threshold, blocker-star exclusion,
greedy three-resource lower bound, common-layer refinement, and batch-puncture
scale.
