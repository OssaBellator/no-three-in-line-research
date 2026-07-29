# Prime-patching parity index supplement: `docs/513--518`

This supplement continues the cumulative parity index after `docs/512`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cjr--PP3cjt | Periodic marker flows admit finite residue correctors, reduced-cost residue oracles, and exact all-length schedules | PROVED | `docs/513-residue-corrected-marker-flow-schedules.md` |
| PP3cju--PP3cjw | Q-ary Hall syndrome blocks admit finite-abelian Fourier powers, exponential mixing bounds, and exact reverse-load horizons | PROVED | `docs/514-q-ary-fourier-mixing-for-hall-syndromes.md` |
| PP3cjx--PP3cjz | Conservative threshold matrices admit binary-router orderings with rowwise and global prefix-load discrepancy certificates | PROVED | `docs/515-prefix-balanced-conservative-threshold-schedules.md` |
| PP3cka--PP3ckc | Regular prefix codes admit threshold generating polynomials, coefficient feasibility/counting certificates, and exact optimum extraction | PROVED | `docs/516-threshold-generating-functions-for-regular-prefix-codes.md` |
| PP3ckd--PP3ckf | Periodic shell controls admit finite prefix-deficit tables, minimum startup buffers, and all-prefix feasibility with vanishing overhead | PROVED | `docs/517-buffered-periodic-shell-schedules.md` |
| PP3ckg--PP3cki | Critical interaction cycles admit scalar residue periodicity and complete vector Pareto corrector frontiers | PROVED | `docs/518-vector-residue-frontiers-for-interactions.md` |

## Frontier update

### Boundary recleaning

A periodic marker controller now works at every sufficiently large attainable
length. A finite reduced-cost residue graph supplies exact correction walks. In
the stored period-three fixture, the optimum cost is `N+(N mod 3)` and the action
rate error is at most `2/N` for every length through 120.

### Localized Hall transport

Hall syndrome mixing now extends from binary Walsh analysis to arbitrary finite
abelian groups. The stored ternary rank-two block has Fourier magnitudes
`7,4,1`; seven blocks are necessary and sufficient for one-percent uniformity,
and the exact degree-18 load is `32929/4941258`.

### Fractional direct-clean layers

A conservative rounded threshold matrix now has a deterministic transient
ordering. The stored three-source rows are `CBAA`, `DBBA`, and `DCCA`; exact
source and global action totals are preserved, while the attained row and global
prefix discrepancies are one and two.

### Support-chord repair words

Regular-language prefix-code optimization now has a threshold generating
function. The target coefficient for multiplicities `(3,2,1)` first becomes
nonzero at `243/1024`, where it equals one; the infeasible threshold `3/16` has
coefficient zero.

### Clean-macro shells

A periodic shell schedule now carries a finite prefix-deficit table and one
minimum startup buffer. The stored twenty-slot word has deficits `(0,0,2/5)`;
buffer `(2/5,0,0)` is optimal and gives all-prefix feasibility with average
overhead `2/(5N)`.

### Integration

Minimum-work interaction schedules now retain every secondary vector tradeoff in
each length residue. The stored period-two system has one even-length frontier
point and two incomparable odd-length points, with exact minimum work
`5 floor(N/2)+3(N mod 2)`.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_513_518.py
```

or individually with

```bash
python scripts/check_marker_residue_correctors.py
python scripts/check_qary_hall_fourier_mixing.py
python scripts/check_prefix_balanced_threshold_schedules.py
python scripts/check_regular_prefix_code_generating_function.py
python scripts/check_buffered_shell_periodic_schedule.py
python scripts/check_vector_interaction_residue_frontiers.py
```

The local audits verify 120 marker lengths, twelve ternary convolution powers,
every threshold prefix, the complete truncated generating polynomial, every
shell prefix through length 100, and every interaction length through 128.

The next available theorem identifier is `PP3ckj`.
