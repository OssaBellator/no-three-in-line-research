# Prime-patching parity index supplement: `docs/525--530`

This supplement continues the cumulative parity index after `docs/524`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3clb--PP3cld | Tied marker cycles admit critical-graph min-plus quasiperiodicity, a critical action-rate polytope, and finite residue certificates | PROVED | `docs/525-min-plus-critical-graphs-for-marker-schedules.md` |
| PP3cle--PP3clg | Noncommuting periodic Hall transfers admit exact matrix products, spectral mixing tails, and reverse-load horizons | PROVED | `docs/526-noncommuting-transfer-products-for-hall-transport.md` |
| PP3clh--PP3clj | Collision-free threshold permutation layers admit exact transient sequencing, additive-potential quotienting, and prefix-load certificates | PROVED | `docs/527-transient-ordering-of-threshold-permutation-layers.md` |
| PP3clk--PP3clm | Regular prefix-tree automata admit algebraic elimination, exact Lagrange coefficients, and singularity-derived entropy asymptotics | PROVED | `docs/528-singularity-analysis-of-regular-prefix-tree-series.md` |
| PP3cln--PP3clp | Shell service multisets admit exact word buffers, Pareto order optimization, and all-length reserve-overhead certificates | PROVED | `docs/529-order-optimized-shell-service-periods.md` |
| PP3clq--PP3cls | Multiple critical interaction blocks admit scalar residue stabilization, Minkowski-power vector frontiers, and critical-polytope limits | PROVED | `docs/530-multicritical-vector-cones-for-interactions.md` |

## Frontier update

### Boundary recleaning

Marker schedules no longer require one uniquely preferred periodic block. The
stored tied-critical catalogue has mean one, cyclicity two, and exact cost

```text
F(N)=N for even N, F(N)=N+1 for odd N.
```

Its limiting action rates fill `conv((1,0),(0,1))`, with finite mesh at most
`4/N`.

### Localized Hall transport

Periodic Hall gadgets may now act by noncommuting transfer matrices. The stored
period product has eigenvalues `9,3,-3`; its exact deviation is `2/3^(m+1)`, so
four periods, or eight blocks, are the sharp one-percent horizon. Degree twelve
gives exact load `83/2916`.

### Fractional direct-clean layers

Permutation layers can now be ordered to control transient geometric resources.
Among all 24 orders of the stored four layers, exactly two attain the minimum
`l_infinity` prefix discrepancy one. Additive source-plus-action potentials
cancel before sequencing.

### Support-chord repair words

For leaf words avoiding `000`, the legal ordered-tree series satisfies

```text
T=z+zT+zT^2.
```

The exact coefficient formula implies

```text
[z^n]T ~ (sqrt(3)/(2 sqrt(pi))) 3^n n^(-3/2).
```

Thus the constrained schedule family has exponential growth constant three.

### Clean-macro shells

The shell service multiset itself can now be reordered to minimize startup
reserve. For `A,A,B,B,C` with target `(2/5,2/5,1/5)`, all 30 words are audited;
ten attain minimum `l_1` buffer `6/5`. The lexicographic optimum `ABABC` uses
buffer `(0,2/5,4/5)`.

### Integration

Several interaction blocks may tie for critical mean work. The stored system
has scalar work `N` on even lengths and `N+1` on odd lengths, but its secondary
frontier has `floor(N/2)+1` points. Exact finite frontiers are residue correctors
plus Minkowski powers, and their normalized limit is
`conv((1,0),(0,1))`.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_525_530.py
```

or individually with

```bash
python scripts/check_multicritical_marker_minplus.py
python scripts/check_noncommuting_hall_transfer_products.py
python scripts/check_steinitz_threshold_layer_ordering.py
python scripts/check_regular_prefix_singularity.py
python scripts/check_order_optimized_shell_periods.py
python scripts/check_multicritical_interaction_cones.py
```

The local audits verify 400 marker lengths, twelve noncommuting Hall periods, all
24 threshold-layer orders, 100 legal-tree coefficients, all 30 shell words and
200 repeated prefixes, and every multi-critical interaction length through 200.

The next available theorem identifier is `PP3clt`.
