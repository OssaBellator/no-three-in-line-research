# Status and honesty ledger

**Last updated:** 28 July 2026

## External status

The classical no-three-in-line problem remains unresolved. The analogous no-`(k+1)`-in-line problem is resolved for each fixed `k>=3` and sufficiently large `n`; that does not settle the exceptional `k=2` case studied here.

## What this branch genuinely proves

1. Saturated states decompose into two permutation layers, and product existence has exact finite CSP/SAT encodings.
2. The branch proves factor-independent products `2x3 -> 6`, `2x4 -> 8`, `2x5 -> 10`, and `2x6 -> 12`.
3. Every saturated side-`n` factor has a factor-compatible side-`2n` state with `O(n log n)` bad triples.
4. The audited paired repair path is effective for every `N >= 10^2874`.
5. Universal divisor-exponent tuning cannot lower that integral cutoff. The Nicolas--Robin baseline reaches only `10^14104`; at `10^2873`, a uniform 10% divisor-cap improvement suffices while 9% does not.
6. All side-seven support-twenty selectors of multiplicity at least three are classified. Multiplicity-two cases `0` through `719` add `1,440` exact rejections. The committed cache contains:
   - `39,040` certified-infeasible selectors;
   - one constructive selector;
   - `32,819` unclassified selectors;
   - `3,073,826,508` certified rejection-CSP nodes.
7. Case-zero orientation-three bottom covers compress 128 obligations into 55 triples and 93 cover lists. Thirty semantically minimized references in six repeated support groups reduce to 21 actual partial assignments; their two groupwise extension unions have sizes 14 and 47. A combined cross-group union measurement is active.
8. At side ten, the complete opposite-pair double coset is infeasible in `cc` and `cf`. Pair indices `0` through `799` are also infeasible in each of `fc` and `ff`.
9. Exact protected-rainbow censuses show that an absolute rank-three cylinder bound requires at least cubic family size.
10. In the canonical side-six repair graph, every state is within two unweighted moves of a solution; exactly ten states require a temporary defect increase, never more than one.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors:

- `39,040` certified infeasible;
- `1` constructive;
- `32,819` unclassified.

The unresolved set is exactly:

- `3,120` multiplicity-two signatures containing `6,240` selectors;
- `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `720`. An eight-shard workflow for cases `720` through `799` is registered but not counted until its transcripts are promoted.

## Active frontiers

- Cover every order below `10^2874`, either by a 10% decimal-2873 divisor improvement, reduced divisor loss, or a structural extension/absorber chain.
- Complete the side-ten `fc` and `ff` searches beyond pair index `799`, then address the two larger double cosets.
- Extend semantic cores to the unequal-support and singleton classes and compute the combined top-order union.
- Prove cubic simultaneous-rainbow abundance with controlled rank-three completion multiplicities.
- Prove a global bounded-barrier repair/resampling theorem.
- Establish second-generation hyperbola/carry concentration, termination, or bounded-denominator absorbers.
- Complete multiplicity two and multiplicity one in the side-seven census.

## Important barriers

- Strict triple-count and natural pair-energy descent are not monotone.
- Shortest repair paths need not minimize peak defect.
- Existence or quadratic abundance of protected rainbow matchings cannot yield constant rank-three spread.
- Representative left cosets are not complete double-coset obstructions.
- The current universal divisor family is exhausted at `10^2874`.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no all-side product theorem. The active exact computations are side-seven cases `720--799`, side-ten fine-row indices `800--1199`, and the combined semantic vocabulary census.
