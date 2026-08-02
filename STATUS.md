# Status and honesty ledger

**Last updated:** 2 August 2026

## External status

The classical no-three-in-line problem remains unresolved. The analogous no-`(k+1)`-in-line problem is resolved for each fixed `k>=3` and sufficiently large `n`; that does not settle the exceptional `k=2` case studied here.

## What this branch genuinely proves

1. Saturated states decompose into two permutation layers, and product existence has exact finite CSP/SAT encodings.
2. The branch proves factor-independent products `2x3 -> 6`, `2x4 -> 8`, `2x5 -> 10`, and `2x6 -> 12`.
3. Every saturated side-`n` factor has a factor-compatible side-`2n` state with `O(n log n)` bad triples.
4. The audited paired repair path is effective for every `N >= 10^2874`.
5. At decimal order `2873`, the unchanged divisor-improvement threshold satisfies `1.0979139 < rho_* < 1.0979151`. A 9% improvement is insufficient through exponent `2873.0585` and sufficient from `2873.0616` onward.
6. All side-seven support-twenty selectors of multiplicity at least three are classified. Multiplicity-two cases `0--1389` are also classified with witness-aware exact replay.
7. The classified multiplicity-two prefix contains `2,780` selectors: `2,779` infeasible and one constructive selector at case `1287`, selector zero, orientation zero.
8. Across support twenty, the exact cache contains `40,379` certified-infeasible selectors, two constructive selectors, `31,479` unclassified selectors, and `3,278,927,685` certified rejection-CSP nodes.
9. For multiplicity-two case zero, orientation three, 192 references reduce to 150 relaxed semantic keys. A 115-key irredundant basis covers 204 of 35,112 clean top orders, with exact digest `12529763722981785837`; `34,908` clean top orders remain outside that union.
10. At side ten, the opposite-pair double coset is completely obstructed in `cc` and `cf`. Fine-row pair indices `0--4799` are obstructed in both `fc` and `ff`, with no constructive witness in those 9,600 geometries.
11. Protected-spread, repair, and carry diagnostics include the first tested genuinely cubic common-rainbow family at order 13, the exact canonical side-six repair-path profile, and complete side-two through side-five carry-level profiles.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors:

- `40,379` certified infeasible;
- `2` constructive;
- `31,479` unclassified.

The unresolved set is exactly:

- `2,450` multiplicity-two signatures containing `4,900` selectors;
- `26,579` multiplicity-one selectors.

The next certified multiplicity-two case is `1390`. Cases `1390--1399` are registered for exact computation but are not counted until every transcript is promoted and replayed.

For the side-ten opposite-pair fine-row search:

- `fc`: indices `0--4799`, `171,920,043` nodes, maximum `1,877,339`;
- `ff`: indices `0--4799`, `100,441,668` nodes, maximum `909,040`.

Indices `4800--5199` are registered but uncounted.

## Active frontiers

- Complete multiplicity two from case `1390`, then classify multiplicity one.
- Continue side-ten fine-row obstruction from pair index `4800`, then address the larger double cosets.
- Expand the semantic union from the `34,908` uncovered clean top orders.
- Determine whether the case-`1287` construction has a symmetry orbit or reusable local template.
- Prove the decimal-2873 interval-specific improvement on the first 6.16% of the logarithmic slab, or reduce effective divisor loss.
- Prove cubic protected residual entropy and bounded rank-three completion multiplicity.
- Prove a global bounded-barrier repair/resampling theorem.
- Prove second-generation collateral concentration, monotone carry termination, or bounded-denominator absorbers.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no infinite all-side product theorem. The repository contains exact finite classifications, verified constructions, computational obstructions, and conditional reductions. Registered workloads do not advance the certified boundary until their outputs are independently replayed and committed.
