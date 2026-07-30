# Prime-patching parity index supplement: `docs/531--536`

This supplement continues the cumulative parity index after `docs/530`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3clt--PP3clv | Mixed-length critical marker blocks admit numerical-semigroup conductors, residue cost formulas, and deterministic critical rate polytopes | PROVED | `docs/531-affine-semigroup-saturation-for-marker-cycles.md` |
| PP3clw--PP3cly | Arbitrarily switched Hall transfers admit common Dobrushin contraction, sharp finite horizons, and switch-robust reverse-load bounds | PROVED | `docs/532-arbitrary-switching-contraction-for-hall-transfers.md` |
| PP3clz--PP3cmb | Threshold permutation layers admit exact cyclic-window discrepancy, finite cyclic sequencing, and phase-independent repeated execution | PROVED | `docs/533-cyclic-discrepancy-of-threshold-permutation-layers.md` |
| PP3cmc--PP3cme | Regular prefix trees admit exact bivariate profile coefficients, entropy maximization, and finite profile-count certificates | PROVED | `docs/534-bivariate-entropy-profiles-for-regular-prefix-trees.md` |
| PP3cmf--PP3cmh | Mixed-period shell controls admit exact supercycle buffers, finite phase-torus optimization, and all-length truncation certificates | PROVED | `docs/535-mixed-period-supercycles-for-shell-controls.md` |
| PP3cmi--PP3cmk | Multi-critical interactions admit Hilbert-basis normality, exact lattice-slice frontiers, and Ehrhart/mesh certificates | PROVED | `docs/536-hilbert-basis-compression-of-interaction-cones.md` |

## Frontier update

### Boundary recleaning

Mixed critical marker lengths now close through a numerical semigroup rather than
a common period. The stored lengths two and three have conductor two; minimum
cost is `2` at length one and exactly `N` at every length `N>=2`. The complete
critical rate mesh lies in `conv((1,0),(0,1))` with `l_1` covering radius at most
`8/N`.

### Localized Hall transport

Hall gadgets may now switch arbitrarily among noncommuting kernels. The stored
pair has common Dobrushin coefficient `3/4`. Across all switch words, seven
blocks fail the target `1/40` while eight blocks attain worst deviation
`2401/98304`; degree sixteen gives exact load `11723/524288`.

### Fractional direct-clean layers

Threshold permutation layers now have a cyclic all-window certificate. Among
all 720 orders of the stored six quotient vectors, 48 linear orders—or eight
cyclic classes—attain minimum `l_infinity` discrepancy two. Repeating the
lexicographic cycle `ABCDEF` preserves the same bound on every interval.

### Support-chord repair words

The legal prefix-tree series now records unary and binary node profiles. The
exact coefficient is `(n-1)!/(a!j!(j+1)!)` when `a+2j=n-1`. At 30 leaves the two
peak branching counts are nine and ten, each of size `168212023980`; the entropy
profile is uniquely maximized at branching density `1/3`.

### Clean-macro shells

Independent shell components of periods two and three now synchronize through a
six-slot supercycle. Of six phase pairs, two minimize `l_infinity` startup
reserve at `2/3`. The lexicographic phase has buffer `(2/3,1/2,0)` and supercycle
`AB,BA,AA,BB,AA,BA`.

### Integration

A Hilbert-basis normality certificate now compresses repeated critical Minkowski
sums into lattice slices. The stored mixed-length critical semigroup has minimum
work `N`, exact frontier

```text
{(N-2b,2b):0<=b<=floor(N/2)},
```

count `floor(N/2)+1`, rational generating function `1/((1-z)(1-z^2))`, and
normalized mesh at most `2/N`.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_531_536.py
```

or individually with

```bash
python scripts/check_mixed_length_marker_semigroups.py
python scripts/check_switched_hall_dobrushin.py
python scripts/check_cyclic_threshold_layer_discrepancy.py
python scripts/check_regular_prefix_entropy_profile.py
python scripts/check_mixed_period_shell_supercycles.py
python scripts/check_normal_interaction_semigroups.py
```

The local audits verify 500 marker lengths, 8,190 switched Hall products, all 720
threshold orders and repeated windows, 100 exact profile coefficients, all six
shell phase pairs with 120 prefixes, and every normal interaction slice through
length 300.

The next available theorem identifier is `PP3cml`.
