# Prime-patching parity index supplement: `docs/519--524`

This supplement continues the cumulative parity index after `docs/518`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ckj--PP3ckl | Finite based marker blocks have eventual residue quasipolynomials, reduced-cost residue oracles, and deterministic `O(1/N)` rate certificates | PROVED | `docs/519-eventual-quasipolynomials-for-marker-schedules.md` |
| PP3ckm--PP3cko | Heterogeneous finite-abelian Hall blocks admit exact characterwise products, nonstationary spectral tails, and reverse-load horizons | PROVED | `docs/520-heterogeneous-fourier-products-for-hall-transport.md` |
| PP3ckp--PP3ckr | Integral conservative threshold matrices decompose into collision-free permutation layers with finite matching certificates | PROVED | `docs/521-permutation-layer-realization-of-threshold-matrices.md` |
| PP3cks--PP3cku | Regular prefix-tree families have depth-truncated algebraic recurrences, coefficient stabilization, and multivariate legal-code series | PROVED | `docs/522-coefficientwise-stable-series-for-regular-prefix-trees.md` |
| PP3ckv--PP3ckx | Periodic shell controls admit exact phase buffers, finite Pareto phase optimization, and all-length truncation certificates | PROVED | `docs/523-phase-optimized-startup-buffers-for-shell-periods.md` |
| PP3cky--PP3cla | Strictly critical interaction blocks have eventual scalar quasipolynomials and translated vector residue frontiers | PROVED | `docs/524-eventual-vector-quasiperiodicity-for-interactions.md` |

## Frontier update

### Boundary recleaning

Minimum marker cost is now eventually affine on every attainable length residue.
The stored length-two/length-three catalogue has critical mean `4/3` and exact
formulas

```text
F(3k)=4k, F(3k+1)=4k+2, F(3k+2)=4k+3.
```

The residue excesses are `0,2/3,1/3`, and deterministic action rates have
`l_1` error at most `8/N`.

### Localized Hall transport

Hall blocks may now vary from layer to layer.  Exact Fourier coefficients multiply
characterwise, while the nonstationary ambiguity tail is the product of the
individual spectral radii.  The stored alternating ternary kernels have power-seven
counts `(274685,274429,274429)`; seven blocks are the sharp `1/4000` horizon, and
degree 18 gives exact load `274685/14823774`.

### Fractional direct-clean layers

An integral conservative threshold matrix now compiles into collision-free
permutation slots.  The stored `4 x 4` margin-four matrix has 84 ordered
permutation decompositions.  Its lexicographically first four layers reproduce
every entry exactly while using each source and each action channel once per slot.

### Support-chord repair words

Regular prefix legality now has a coefficientwise-stable algebraic generating
series.  For leaf words avoiding `000`, the ordered legal-tree counts for one
through ten leaves are

```text
1,1,2,4,9,21,51,127,323,835.
```

The coefficient for `K` leaves stabilizes by depth `K-1`.

### Clean-macro shells

A shell period can now choose its cyclic phase to minimize startup reserves.  For
three coordinate service actions with target `(1/3,1/3,1/3)`, the phase buffers
are the three permutations of `(0,1/3,2/3)`.  Minimum `l_1` buffer is one, no
zero-buffer phase exists, and every truncation remains feasible.

### Integration

Minimum-work interaction frontiers are now eventually periodic up to vector
translation.  The stored period-three system has work

```text
6 floor(N/3)+{0,3,5}[N mod 3],
```

with residue frontier sizes one, two, and two.  Every frontier through length 180
is the finite residue corrector set translated by copies of the critical block.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_519_524.py
```

or individually with

```bash
python scripts/check_eventual_marker_quasipolynomial.py
python scripts/check_heterogeneous_hall_fourier_products.py
python scripts/check_birkhoff_threshold_layers.py
python scripts/check_regular_prefix_shape_series.py
python scripts/check_phase_optimized_shell_buffers.py
python scripts/check_eventual_vector_interaction_frontiers.py
```

The local audits verify 301 marker lengths, twelve heterogeneous Fourier products,
all 84 ordered threshold decompositions, stable legal-tree coefficients through
ten leaves, every phase prefix through length 100, and every interaction length
through 180.

The next available theorem identifier is `PP3clb`.
