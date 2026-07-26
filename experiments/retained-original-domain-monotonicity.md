# Retained-original controller-domain monotonicity diagnostic

Run

```text
python scripts/check_retained_original_domain_monotonicity.py \
  experiments/retained-original-domain-monotonicity-example.json
```

The stored source has seven row/column-disjoint points, three retained controller
edges, and 36 movement/refill label pairs per controller.  Deleting the one
noncontroller source point `(2,2)` gives the exact output summary

```text
source size                    7
retained size                  6
deleted size                   1
controller count               3
label-pair count              36
original domain sizes      19,18,12
retained domain sizes      24,18,16
original gamma-good            0
retained gamma-good            1
monotonicity verified       true
outcome retained_original_domains_expand
```

For controller `(0,4)`, five refill-label pairs become safe after the deletion:

```text
(7,10), (8,10), (10,10), (11,10), (12,10).
```

For controller `(4,1)`, four pairs become safe:

```text
(10,9), (10,10), (10,11), (10,12).
```

No originally safe pair becomes unsafe.  The threshold `gamma_count=20` is not
met by any original controller, while one retained-original domain crosses it.
The checker verifies the inclusion for every controller and label pair rather
than only comparing total sizes.
