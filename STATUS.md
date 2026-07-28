# Status and honesty ledger

**Last updated:** 28 July 2026

## External status

The classical no-three-in-line problem remains unresolved: no side length is known for which the maximum is strictly below `2n`. Exact `2n` configurations are known for every `2 <= n <= 66`, and also for `n=68` and `n=70`.

The analogous no-`(k+1)`-in-line problem is resolved for every fixed `k>=3` and sufficiently large `n`; this does not settle the exceptional `k=2` case studied here.

## What this branch genuinely proves

1. **Exact product encodings.** Saturated states decompose into two permutation layers; fixed-phase and full-selector existence reduce to exact finite CSP/SAT systems.
2. **Small factor-independent products.** The branch proves `2x3 -> 6`, `2x4 -> 8`, `2x5 -> 10`, and `2x6 -> 12` for every saturated no-three factor of the indicated inner side.
3. **Low-syndrome doubling seed.** Every saturated side-`n` factor has a factor-compatible side-`2n` state with `O(n log n)` bad triples.
4. **Paired asymptotic repair.** The audited repair path is effective for every `N >= 10^2874`.
5. **Finite-range arithmetic targets and barriers.** The universal Euler-product exponent family cannot lower the integral cutoff. The Nicolas--Robin baseline reaches only `10^14104`. At `10^2873`, a uniform 10% improvement of the optimal ambient-divisor cap suffices through the missing decimal slab, while 9% is insufficient.
6. **Finite side-seven census.** All selectors of multiplicity at least three are classified. Multiplicity-two cases `0` through `639` add `1,280` exact rejections. The committed cache contains:
   - `38,880` certified-infeasible selectors;
   - one constructive selector;
   - `32,979` unclassified selectors;
   - `3,042,485,047` certified rejection-CSP nodes.
7. **Bottom-cover and semantic compression.** For case zero, orientation three, 128 obligations through 64 top orders have seven-triple covers. The dominant repeated support class collapses from twelve references to five actual partial assignments covering fourteen distinct clean top orders.
8. **Produced-base recursion barriers.** Affine-column templates are impossible at bases 8, 10, and 12. At side ten, the complete opposite-pair double coset is infeasible in `cc` and `cf`; the first 400 pair indices are also infeasible in each of `fc` and `ff`.
9. **Protected-spread entropy barrier.** Exact order-five and order-seven simultaneous-rainbow censuses have rank-three cylinder constants `6` and `15/2`. Any absolute rank-three bound requires at least cubic family size.
10. **Bounded-uphill repair profile.** In the canonical side-six repair graph, every state is within two unweighted cycle toggles of a solution. Exactly ten states require any defect increase, never more than one; one state needs three moves to preserve the minimum barrier.
11. **Global matching, hyperbola/carry, and terminal endpoints.** Dense hosts have spread-selection theorems; the hyperbola path has exact extraction and first-generation neutralization; Hall-core and trajectory-reset interfaces are integrated into the paired repair tree.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors:

- `38,880` certified infeasible;
- `1` constructive;
- `32,979` unclassified.

The unresolved set is exactly:

- `3,200` multiplicity-two signatures containing `6,400` selectors;
- `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `640`. An eight-shard workflow for cases `640` through `719` is registered but is not counted until its exact transcripts are promoted.

## What remains conditional or open

- A structural or arithmetic bridge covering every order below `10^2874`.
- A 10% interval-specific divisor-cap improvement on the decimal-2873 slab, or an equivalent reduction in effective divisor loss.
- Infinite exact product closure or arithmetic coverage of every side length.
- Completion of the side-ten opposite-pair `fc` and `ff` searches beyond pair index `399`, followed by the two larger double cosets.
- Semantic cores for the remaining support classes and their complete top-family coverage.
- Cubic simultaneous-rainbow abundance with controlled rank-three multiplicities, uniformly after conditioning.
- A global bounded-barrier repair/resampling theorem coordinating many product fibres.
- Second-generation collateral concentration, alternating carry termination, or a bounded-denominator chamber absorber.
- Completion of multiplicity two and multiplicity one in the side-seven census.

## Important barriers

- Bounded line occupancy and pair codegree alone do not imply private repair expansion.
- Triple-count and natural pair-energy objectives are not monotone on the alternating-cycle state space.
- Shortest repair paths need not minimize peak defect.
- Existence or merely quadratic abundance of protected rainbow matchings cannot yield constant rank-three spread.
- Global radix choices, identity/reversal maps, and affine block maps are not universal constructions beyond the proved small templates.
- Representative left cosets are not complete double-coset obstructions.
- The current universal divisor family is exhausted at `10^2874`; the classical subexponential baseline is weaker in the active range.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no all-side product theorem. The active fronts are the case-`640` census, finite-range coverage, broader semantic vocabulary coverage, non-affine recursion, cubic protected entropy, bounded-barrier resampling, and hyperbola/carry termination or absorption.
