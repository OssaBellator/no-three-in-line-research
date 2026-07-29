# Prime-patching parity index supplement: `docs/495--500`

This supplement continues the cumulative parity index after `docs/494`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3chp--PP3chr | Rational marker policies factor through balanced binary mechanical routers, with depth discrepancy bounds and exact finite tree selection | PROVED | `docs/495-balanced-binary-routing-for-marker-controllers.md` |
| PP3chs--PP3chu | Hall-color list decoding admits sparse syndrome trellises, complementary half joins, reconstruction, and exact reverse-load certificates | PROVED | `docs/496-sparse-meet-in-the-middle-syndrome-trellises.md` |
| PP3chv--PP3chx | Nearest threshold designs form a finite rational projection atlas with exact breakpoint walks, prices, and localized basis audits | PROVED | `docs/497-parametric-regions-for-nearest-threshold-designs.md` |
| PP3chy--PP3cia | Unordered prefix-tree shapes have unique canonical encodings, isomorph-free augmentation, and exact optimal-orbit filtering | PROVED | `docs/498-canonical-augmentation-of-prefix-code-shapes.md` |
| PP3cib--PP3cid | Multiparametric shell attenuation has a finite rational chamber fan, circulation gradients, and exact chamber-walk certificates | PROVED | `docs/499-multiparametric-chambers-for-shell-attenuation.md` |
| PP3cie--PP3cig | Repeated interaction motifs compose through Pareto transfer matrices, exact semiring powers, and minimum-work reconstruction | PROVED | `docs/500-pareto-transfer-matrices-for-repeated-interactions.md` |

## Frontier update

### Boundary recleaning

A rational multi-action marker policy now factors through binary mechanical
routers.  A leaf at depth `d` has prefix discrepancy at most `d`, and arbitrary
interleavings of marker states inherit a summed observable bound.  The stored
policy `(1/2,1/3,1/6)` has six-step period `C,A,B,A,B,A` and exact leaf
discrepancies `1/2,2/3,5/6`.

### Localized Hall transport

Syndrome decoding now keeps only reachable states and joins two sparse halves by
complementary syndrome.  In the stored `[5,2,4]` code, the half supports have
sizes at most four and eight instead of 125 ambient syndromes.  Across 3,125
cyclic-pair observations, the list histogram is `2350,750,25` for sizes zero,
one, and two.

### Fractional direct-clean layers

Nearest threshold repair is now a parametric atlas.  The stored nominal path
`(t,t)` has exact projection regions separated at `1/2` and `3/5`; the repair
value slopes are `0,2,3`.  Active projection prices and coordinates are affine
inside each region.

### Support-chord repair words

Prefix-tree shapes are now generated without isomorphic duplicates.  The first
eight unordered full-binary shape counts are `1,1,1,2,3,6,11,23`.  Among six
six-leaf shapes, exactly two have minimum height three and equal-risk optimum
eight.

### Clean-macro shells

Several shell cycle targets may now vary simultaneously.  The stored
three-constraint attenuation value is `max(a,b,c,(a+b+c)/2)`, giving one central
and three dominant chambers.  A 1,331-point audit verifies the chamber formulas,
primal repairs, and circulation gradients.

### Integration

Repeated interaction motifs now compose by a Pareto transfer semiring.  The
stored length-eight chain compresses 128 direct start--end plans to 17 frontier
vectors.  Three matrix-squaring stages recover the exact frontier, and tolerance
`(4,4)` has the unique minimum-work plan `BDBDBDBD`.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_495_500.py
```

or individually with

```bash
python scripts/check_balanced_binary_marker_schedules.py
python scripts/check_sparse_mitm_hall_syndromes.py
python scripts/check_parametric_threshold_projection_regions.py
python scripts/check_canonical_prefix_tree_augmentation.py
python scripts/check_multiparametric_shell_chambers.py
python scripts/check_pareto_transfer_matrix_power.py
```

The local audits verify 961 marker-state interleavings, all 3,125 sparse Hall
observations, 101 projection samples, canonical tree shapes through eight leaves,
1,331 shell parameter triples, and exact direct-versus-powered interaction
frontiers.

The next available theorem identifier is `PP3cih`.
