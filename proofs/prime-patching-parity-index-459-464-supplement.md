# Prime-patching parity index supplement: `docs/459--464`

This supplement continues the cumulative parity index after `docs/458`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cdl--PP3cdn | Candidate marker moves admit a statewise multipotential controller LP, sparse randomized policies, and localized rational separating witnesses | PROVED | `docs/459-multipotential-marker-controller-synthesis.md` |
| PP3cdo--PP3cdq | Hall color tags obey the Singleton erasure bound; Reed--Solomon evaluation tags attain it and have exact post-budget list ambiguity | PROVED | `docs/460-optimal-erasure-tags-for-hall-colors.md` |
| PP3cdr--PP3cdt | Threshold-basis regions are affine rational cells; exact facet times and one-pivot continuations traverse parametric right-hand-side paths | PROVED | `docs/461-exact-pivot-paths-between-threshold-basis-regions.md` |
| PP3cdu--PP3cdw | Generalized Kraft bounds give safe split pruning, bottom-up branch-and-bound proof trees, and an exact memoized subset oracle | PROVED | `docs/462-branch-and-bound-certificates-for-unequal-symbol-codes.md` |
| PP3cdx--PP3cdz | Allowed motion on a multicritical shell face is an exact rational descent LP with convex-cycle dual obstructions and strict-descent persistence | PROVED | `docs/463-descent-linear-programs-on-multicritical-shell-faces.md` |
| PP3cea--PP3cec | Interaction automata admit exact adaptive path-frontier remainders, potential envelopes, and a finitely terminating hybrid truncation procedure | PROVED | `docs/464-adaptive-frontier-truncation-for-interaction-automata.md` |

## Frontier update

### Boundary recleaning

The marker automaton is now a synthesis problem rather than only a verification
problem.  For several positive observables, the controller constraints split by
state into small rational linear programs.  Extreme policies use at most one
more action than the number of protected observables, and failure returns one
statewise nonnegative separator.  The stored root genuinely requires the mixed
policy `(1/2,1/2)`.

### Localized Hall transport

A field-coordinate tag for `p^k` proper Hall colors that survives `e` erasures
must have length at least `k+e`.  Reed--Solomon evaluation attains that length
when `k+e<=p`.  Beyond the protected budget, exactly `p^(r-e)` colors remain
possible after `r>e` erasures, so the reverse-load degradation is explicit.

### Fractional direct-clean layers

Parametric threshold certificates can now be followed across their region
walls.  Inside one basis cell the optimum is affine.  Along a rational parameter
path, the first wall time is an exact ratio of basic coordinates, and a
nondegenerate continuation is one exact simplex pivot.  The stored path pivots
at `t=1/2`.

### Support-chord repair words

The generalized survival-Kraft bound is now used inside an exact
branch-and-bound proof.  Every skipped subset split carries a lower bound at
least the current incumbent.  The seven-bank fixture proves optimum `27/64`
while visiting 76 of 127 subsets and pruning 236 split candidates.

### Clean-macro shells

At a multicritical tie, allowed local changes can be optimized by a finite LP
on the active cycle incidences.  Its dual is a convex combination of critical
cycles proving the absence of a better direction.  The stored face has exact
strict descent `-1/4` in direction `(1/2,-1,1/2)`.

### Integration

Uniform interaction order is replaced by an exact adaptive path frontier.  A
frontier atom is priced by the resolvent continuation `H=(I-J)^(-1)C`, and its
sum is the exact omitted output.  Potential prices provide a cheaper envelope
and a uniform-depth fallback.  The stored audit reaches the same `1/100` error
budget with four expansions instead of seven.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_459_464.py
```

or individually with

```bash
python scripts/check_marker_controller_synthesis.py
python scripts/check_optimal_erasure_hall_tags.py
python scripts/check_threshold_basis_path_traversal.py
python scripts/check_branch_and_bound_unequal_codes.py
python scripts/check_multicritical_descent_lp.py
python scripts/check_adaptive_interaction_truncation.py
```

The local audits verify a unique mixed marker controller and rational separator,
all erasure fibers of an optimal 25-color tag, 101 exact basis-path points, a
seven-bank branch-and-bound certificate, 217 exact multicritical directions,
and an exact two-output adaptive interaction frontier.

The next available theorem identifier is `PP3ced`.
