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
6. All side-seven support-twenty selectors of multiplicity at least three are classified. Multiplicity-two cases `0` through `1039` add `2,080` exact rejections. The committed cache contains:
   - `39,680` certified-infeasible selectors;
   - one constructive selector;
   - `32,179` unclassified selectors;
   - `3,165,594,500` certified rejection-CSP nodes.
7. Case-zero orientation-three bottom covers compress 128 obligations into 55 triples and 93 cover lists. The complete first-64 semantic census reduces 64 reference cores to 49 actual partial-assignment keys covering 92 distinct clean top orders, verified by 1,703,520 exact bottom checks.
8. At side ten, the complete opposite-pair double coset is infeasible in `cc` and `cf`. Pair indices `0` through `2399` are also infeasible in each of `fc` and `ff`, using 40,119,413 and 41,948,761 nodes respectively.
9. Exact protected-rainbow censuses show that an absolute rank-three cylinder bound requires at least cubic family size.
10. In the canonical side-six repair graph, every state is within two unweighted moves of a solution; exactly ten states require a temporary defect increase, never more than one.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors:

- `39,680` certified infeasible;
- `1` constructive;
- `32,179` unclassified.

The unresolved set is exactly:

- `2,800` multiplicity-two signatures containing `5,600` selectors;
- `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1040`.

## Active frontiers

- Cover every order below `10^2874`, either by a 10% decimal-2873 divisor improvement, reduced divisor loss, or a structural extension/absorber chain.
- Continue the side-ten `fc` and `ff` search from pair index `2400`, then address the two larger double cosets.
- Complete the semantic vocabulary census through top index 127, measure reuse of the established 49 keys, and solve a compact set-cover problem over the complete clean-top family.
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

There is no complete proof of the classical no-three-in-line conjecture and no all-side product theorem. The complete semantic census through top index 127 is active but excluded until promoted; the next finite side-seven case is `1040` and the next side-ten pair index is `2400`.
