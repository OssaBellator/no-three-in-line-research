# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This branch is independent of the other all-`n` strategies. It assumes a
saturated no-three-in-line theorem is eventually proved on `(p-1)x(p-1)` grids
for all sufficiently large primes `p`, and asks how to extend such a
construction to nearby side lengths.

Prime-gap information alone is not sufficient: embedding a `2m`-point solution
into an `n x n` grid leaves `2(n-m)` missing points. The essential theorem is an
exact extension absorber.

Detailed statements and proofs are in:

- [`docs/27-all-n-prime-patching.md`](../docs/27-all-n-prime-patching.md);
- [`docs/28-one-strip-and-pair-aware-patching.md`](../docs/28-one-strip-and-pair-aware-patching.md);
- [`docs/29-general-reservoir-patching.md`](../docs/29-general-reservoir-patching.md);
- [`docs/30-deletion-aware-row-lift-banks.md`](../docs/30-deletion-aware-row-lift-banks.md);
- [`docs/31-sequential-row-lift-local-lemma.md`](../docs/31-sequential-row-lift-local-lemma.md);
- [`docs/32-row-lift-pruning-barriers.md`](../docs/32-row-lift-pruning-barriers.md);
- [`docs/33-off-diagonal-reservoir-obstruction.md`](../docs/33-off-diagonal-reservoir-obstruction.md);
- [`docs/34-projection-triple-lower-bounds.md`](../docs/34-projection-triple-lower-bounds.md);
- [`docs/35-component-clean-row-lift-banks.md`](../docs/35-component-clean-row-lift-banks.md);
- [`docs/36-monotone-parabolic-reservoirs.md`](../docs/36-monotone-parabolic-reservoirs.md);
- [`docs/37-variable-reservoir-patch-banks.md`](../docs/37-variable-reservoir-patch-banks.md);
- [`docs/38-parabolic-rung-budget.md`](../docs/38-parabolic-rung-budget.md);
- [`docs/39-matching-reservoir-cycle-factorization.md`](../docs/39-matching-reservoir-cycle-factorization.md);
- [`docs/40-cycle-reservoir-2sat.md`](../docs/40-cycle-reservoir-2sat.md);
- [`docs/41-sheared-parabolic-banks.md`](../docs/41-sheared-parabolic-banks.md);
- [`docs/42-width-two-matching-patches.md`](../docs/42-width-two-matching-patches.md);
- [`docs/43-one-rectangle-patch-repair.md`](../docs/43-one-rectangle-patch-repair.md).

Finite computations are recorded in:

- [`experiments/prime-patching-small.md`](../experiments/prime-patching-small.md);
- [`experiments/general-reservoir-loads.md`](../experiments/general-reservoir-loads.md);
- [`experiments/row-lift-static-pruning.md`](../experiments/row-lift-static-pruning.md);
- [`experiments/row-lift-projections.md`](../experiments/row-lift-projections.md);
- [`experiments/component-clean-row-lift.md`](../experiments/component-clean-row-lift.md);
- [`experiments/parabolic-matching-reservoirs.md`](../experiments/parabolic-matching-reservoirs.md);
- [`experiments/parabolic-parameter-sweep.md`](../experiments/parabolic-parameter-sweep.md);
- [`experiments/sheared-parabolic-parameters.md`](../experiments/sheared-parabolic-parameters.md);
- [`experiments/matching-reservoir-cycles.md`](../experiments/matching-reservoir-cycles.md);
- [`experiments/cycle-reservoir-2sat.md`](../experiments/cycle-reservoir-2sat.md);
- [`experiments/variable-reservoir-banks.md`](../experiments/variable-reservoir-banks.md);
- [`experiments/width-two-rectangle-repairs.md`](../experiments/width-two-rectangle-repairs.md).

## PP1 — Boundary extension interface

### Status: PROVED for saturation; geometry separated into PP2

The row-column bookkeeping is exact:

- for `t>=2`, two edge-disjoint permutation graphs on the new `t x t` corner
  add exactly `2t` points without changing the old core;
- for `t=1`, every boundary-only degree state is either a one-point corner splice
  or a two-edge strip switch;
- the complete `t=1` list has only `2m^2-m` forced candidates;
- geometric validity is exactly the avoidance of old-pair secants,
  old-anchor/new-pair triples, and internal new-point triples.

## PP2 — Secant-shadow patching lemma

### Status: OPEN, with exact fixed- and variable-reservoir endpoints

There should be functions `w(m)` and `f(t)` such that, whenever `t<=w(m)`, one
can prepare a reservoir in `S_m` that supports an exact row-column-preserving
completion without creating any triple.

The exact selection step is closed in several forms:

- a pair-aware corner clone-space local lemma;
- an arbitrary deleted-reservoir clone-space theorem allowing old-old and
  mixed old/new replacement cells;
- explicit normalized cell, anchored-pair, and internal-triple load bounds;
- an internally no-three spread-bank endpoint using only retained-core cell and
  pair expectations;
- a component-clean row-lift endpoint that factors movement and refill banks and
  pays only retained-core and cross-component certificates;
- the deletion-aware variable-reservoir theorem PP2l, which permits different
  states to delete different old points and uses the exact joint survival and
  insertion probabilities.

For active clone size `N>=200`, the arbitrary-reservoir bounds

```text
u_* <= N/200,
pi_* <= N^2/1600,
tau_* <= N^3/3200
```

suffice. Failure forces one of the three local loads to be large.

The missing work is geometric preparation, not exact degree selection.

## PP3 — Robust seed preparation

### Status: OPEN, with an internally clean square-root patch and exact repair interfaces

A prepared reservoir should have low old-pair shadow, low old-anchor pair load,
controlled internal directions, interchangeable row-column states, and a
variable deletion budget.

### Completed positive components

- The exact one-strip degree states and deletion-aware surviving-certificate
  average are proved. The corrected average detects the valid `2 -> 3` state.
- Deleting all points in `t` old rows gives an explicit row-lift bank with exact
  saturation and fixed-rank spread.
- Four row-lift permutation layers can be selected by a prefix-aware sequential
  local lemma under maximum activated assignment load `1/24`.
- Prefix enumeration can be replaced by the static terminal-load test PP3p.
- Collision constraints can be conditioned out, giving the threshold-one
  activated-mass theorem PP3q and static test PP3r.
- Projection dispersion gives a fast necessary support screen and exact lower
  bounds on triples forced by under-dispersed parallel-line families.
- Internally clean movement and refill component banks have an exact independent
  expectation endpoint PP3z and spread form PP3aa. Any fixed clean component pair
  has only `O(t^2)` cross triples.
- The monotone parabolic matching construction gives a deterministic internally
  no-three patch of width `Theta(sqrt(m))`; only the two retained-core certificate
  classes remain.
- A linear shear preserves the parabolic no-three proof and yields an internally
  clean parameter bank with cell probability `O(1/m)` and nonaxis pair
  probability as small as `O(t/m^2)`, conditional on a positive-density family
  of matching-admissible parameter tuples.
- Variable matching reservoirs factor exactly into forced paths and independent
  alternating cycles. For one fixed patch, selecting cycle parities to clear all
  external triples is exactly a 2-SAT problem.
- Cross-only width-two matching patches have a complete 36-state degree
  classification for each four-column/four-row matching reservoir.
- A near-miss patch can be repaired by one alternating rectangle switch under
  the exact criterion PP3ay. The stored corpus contains three such repaired
  extensions: `4 -> 6`, `5 -> 7`, and `6 -> 8`.

### Quantitative prime-gap-scale ladder target

One parabolic rung has square-root width. If `K` disjoint rungs of widths `t_i`
are packed into old-coordinate intervals, then

\[
\sum_i t_i
\le
K+\sqrt{K(m-K)/2}.
\]

A total width `m^theta` with `theta>1/2` therefore needs and permits
`K=Theta(m^(2theta-1))` equal-scale rungs at the coordinate-budget level. For
the published exponent `theta=0.525`, the target is only about `m^0.05`
mutually compatible rungs.

No multi-rung compatibility theorem is yet proved.

### Refuted or blocked shortcuts

- Universal recursive boundary-only one-strip extension dies before side five.
- The original unconditioned PP3b boundary-shadow average is universally
  vacuous because every future boundary cell has an automatic axis blocker.
- The unrestricted full row-lift bank is not automatically clean; exhaustive
  searches over every two- and three-row reservoir in the stored `2<=n<=10`
  corpus find no clean state.
- The full-support PP3j first-moment route cannot scale: one refill rectangle
  already contributes `Omega(t^4 log t)` compatible candidate triples.
- Deleting an aligned contiguous square and refilling only its two off-diagonal
  blocks is impossible for every `t`: `4t` points occupy only `2t-1` slope-`-1`
  diagonals.
- Projection equality analysis shows that this aligned slope-`-1` placement is
  the unique primitive-direction failure at the minimal `2t-1` level threshold.
- Conditioning the full small banks to internally clean components leaves no
  clean pair at fully deleted widths `3,4,5`; the clean families are too small
  and concentrated.
- Across the stored `2<=n<=10` corpus, the unsheared parabolic parameter sweep
  finds 40 matching states and the sheared sweep finds 18,816 matching states,
  but neither contains an externally clean patch.
- Exhausting all 80,731 internally clean cross-only width-two matching states
  finds no raw patch. One rectangle switch repairs exactly three of them and no
  others in the stored corpus.
- Deletion-cycle entropy alone does not dilute a fixed certificate: optional
  old points have survival probabilities bounded away from zero. Useful cycles
  must be geometrically aligned so their alternating choices anticorrelate the
  relevant blockers.

### Current exact target

The strongest concrete route is now a **parabolic patch-plus-trade ladder**.
A prime-gap-scale PP3 construction may succeed by providing:

1. `Theta(m^0.05)` mutually compatible square-root-scale parabolic rungs for the
   published prime-gap exponent;
2. a positive-density family of matching-admissible sheared parameter tuples;
3. cycle parities satisfying the exact 2-SAT external-certificate formula, or
   PP2l joint expectation below one;
4. protected alternating rectangles whose removed diagonals cover residual
   blockers and whose added diagonals have controlled collateral;
5. compatibility between the inserted points and trades of different rungs.

The older row-lift alternatives remain valid: a sparse algebraic bank passing
PP3p/PP3r, a prefix-structured bank passing PP3l/PP3q, or an arbitrary-reservoir
host passing the PP2 cell/pair/triple endpoint.

## PP4 — Prime-gap transfer theorem

### Status: PROVED UNDER PP2–PP3

If every sufficiently large `n` has a solved size `m` with

\[
0\le n-m\le w(m),
\]

then the prepared-seed extension theorem implies `D(n)=2n` for every sufficiently
large `n`.

For solved sizes `m=p-1`, a prime in `[x-x^theta,x]` is matched by any proved
width `w(m)>=C m^theta` with fixed `C>1`. Consequently:

- the published Baker–Harman–Pintz exponent `theta=0.525` requires
  `w(m)>=C m^0.525`, or more simply `m^(0.525+epsilon)`;
- Runbo Li's arXiv preprint claims `theta=0.52`, usable only as a preprint input;
- a merely polylogarithmic width does not currently give an unconditional
  all-`n` transfer.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; CERTIFICATES VERIFIED FOR `2<=n<=10`

The exact verifier checks integer determinants, bounds, distinctness, point
count, and two points in every row and column. The missing PP5 work is the
eventual threshold and the complete certificate set below it.

## Computational tools

- `scripts/search_boundary_extension.py`: general prescribed-degree extension
  CSP with `found`, `exhausted`, and `cutoff` outcomes;
- `scripts/analyze_deletion_aware_one_strip.py`: exact deletion-aware `t=1`
  certificate average;
- `scripts/analyze_reservoir_patch_loads.py`: exact arbitrary-reservoir clone and
  coordinate loads;
- `scripts/analyze_row_lift_bank.py`: exact small full-bank enumeration;
- `scripts/analyze_row_lift_sequential_loads.py`: prefix-aware four-layer loads;
- `scripts/analyze_row_lift_static_pruning.py`: static PP3p and PP3r screens;
- `scripts/analyze_row_lift_projections.py`: primitive-direction projection and
  forced-triple lower bounds;
- `scripts/analyze_component_clean_row_lift.py`: PP3z/PP3aa component-clean
  analysis;
- `scripts/analyze_parabolic_matching_reservoir.py`: exact parabolic matching
  reservoir search;
- `scripts/search_parabolic_parameters.py`: unsheared parameter sweep;
- `scripts/search_sheared_parabolic_parameters.py`: independent movement/refill
  scale, gap, shear, and offset sweep;
- `scripts/analyze_variable_reservoir_bank.py`: exact PP2l finite bank verifier;
- `scripts/analyze_matching_reservoir_cycles.py`: degree-two path/cycle
  factorization and deletion marginals;
- `scripts/solve_matching_reservoir_2sat.py`: exact implication-graph solver for
  fixed-patch cycle reservoirs;
- `scripts/search_width_two_matching_patches.py`: complete cross-only width-two
  matching-patch enumeration;
- `scripts/search_width_two_rectangle_repairs.py`: exhaustive one-switch repair
  search;
- `scripts/search_row_lift_reservoirs.py`: exhaustive small reservoir-row search;
- `scripts/verify_no_three_certificate.py`: exact finite certificate verifier.

## Completion criterion

This branch is complete only when PP2 and PP3 provide a width large enough for
PP4, followed by verified PP5 coverage below the resulting threshold. The branch
now closes the exact extension interfaces, fixed- and variable-reservoir
selection endpoints, one-strip rigidity, row-lift and parabolic internally clean
banks, sequential/static/2-SAT selection criteria, projection obstructions, and
one-rectangle repair. It still lacks the asymptotic seed-preparation and
multi-rung compatibility theorem and does not prove the no-three-in-line
conjecture.
