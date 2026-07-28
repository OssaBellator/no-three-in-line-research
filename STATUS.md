# Status and honesty ledger

**Last updated:** 28 July 2026

## External status

The classical no-three-in-line problem remains unresolved: no side length is
known for which the maximum is strictly below `2n`. Exact `2n` configurations
are known for every `2 <= n <= 66`, and also for `n=68` and `n=70`.

The analogous no-`(k+1)`-in-line problem is resolved for every fixed `k>=3` and
sufficiently large `n`; this does not settle the exceptional `k=2` case studied
here.

## What this branch genuinely proves

Detailed theorem statements and locations are maintained in `proofs/` and the
track ledgers. Principal endpoints include:

1. **Exact product encodings.** Saturated states decompose into two permutation
   layers; fixed-phase and full-selector existence reduce to exact finite
   CSP/SAT systems.
2. **Small factor-independent products.** The branch proves `2x3 -> 6`,
   `2x4 -> 8`, `2x5 -> 10`, and `2x6 -> 12` for every saturated no-three factor
   of the indicated inner side.
3. **Low-syndrome doubling seed.** Every saturated side-`n` factor has a
   factor-compatible side-`2n` state with `O(n log n)` bad triples.
4. **Paired asymptotic repair.** The audited repair path is effective for every
   `N >= 10^2874`.
5. **Finite-range arithmetic targets and barriers.** The universal
   Euler-product exponent family cannot lower the integral cutoff. The baseline
   Nicolas--Robin estimate reaches only `10^14104`. At `10^2873`, a uniform 10%
   improvement of the optimal ambient-divisor cap is sufficient through the
   missing decimal slab, while 9% is insufficient.
6. **Finite side-seven census.** All selectors of multiplicity at least three
   are classified. Multiplicity-two cases `0` through `559` add `1,120` exact
   rejections. The committed cache contains:
   - `38,720` certified-infeasible selectors;
   - one constructive selector;
   - `33,139` unclassified selectors;
   - `3,006,271,316` certified rejection-CSP nodes.
7. **Bottom-cover compression.** Fixed-top infeasibility is equivalent to
   covering all `5,040` bottom permutations by collinear triples. In case zero,
   orientation three, 128 obligations through 64 top orders all have
   seven-triple covers; 55 triples and 93 covers encode 896 entries.
8. **Semantic top-master learning.** Twelve repeated-support references collapse
   to five actual partial assignments: four use mask `6936`, one uses mask
   `6920`. Their extension lists contain 40 occurrences but only 14 distinct
   clean top orders, with 403,200 exact bottom checks.
9. **Produced-base recursion barriers.** Affine-column all-transposition
   templates are impossible at bases 8, 10, and 12. At side ten, the complete
   opposite-pair double coset is infeasible in orientations `cc` and `cf`,
   covering 16,000 geometries and 266,447,755 nodes.
10. **Global matching, hyperbola/carry, and terminal repair endpoints.** Dense
    hosts have spread-selection theorems; the hyperbola path has exact extraction
    and first-generation neutralization; Hall-core and trajectory-reset
    interfaces are integrated into the paired repair tree.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors. The committed
classification is:

- `38,720` certified infeasible;
- `1` constructive;
- `33,139` unclassified.

The unresolved set is exactly:

- `3,280` multiplicity-two signatures containing `6,560` selectors;
- `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `560`. An eight-shard workflow for
cases `560` through `639` is registered but is not counted until its exact
transcripts are promoted.

## What remains conditional or open

- A structural or arithmetic bridge covering every order below `10^2874`.
- A 10% interval-specific divisor-cap improvement on the decimal-2873 slab, or
  an equivalent reduction in effective divisor loss.
- Infinite exact product closure or arithmetic coverage of every side length.
- Completion of the side-ten opposite-pair `fc` and `ff` double-coset searches,
  followed by the two larger transposition double cosets.
- Semantic cores for the remaining support classes and measurement of their
  coverage of the complete top-order family.
- A global repair/resampling theorem or conflict-free exact-cover theorem with
  the required local-load endpoint.
- Second-generation collateral concentration, monotone alternating carry
  complexity, or a bounded-denominator chamber absorber.
- Completion of multiplicity two and multiplicity one in the side-seven census.

## Important barriers

- Bounded line occupancy and bounded pair codegree alone do not imply private
  repair expansion.
- Triple-count and natural pair-energy objectives are not monotone on the
  alternating-cycle state space.
- Global radix choices, identity/reversal maps, and affine block maps are not
  universal constructions beyond the proved small templates.
- Representative left cosets are not complete double-coset obstructions.
- The current universal divisor family is exhausted at `10^2874`; the classical
  subexponential baseline is weaker in the active range.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no
all-side product theorem. The branch contains exact finite classifications,
small factor-independent products, an effective asymptotic repair reduction,
compact semantic master nogoods, and replayable recursion barriers. The active
fronts are the case-`560` census, finite-range coverage, broader semantic
vocabulary coverage, genuinely non-affine recursion, global resampling, and
hyperbola/carry termination or absorption.
