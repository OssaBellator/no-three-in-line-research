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
6. All side-seven support-twenty selectors of multiplicity at least three are classified. Multiplicity-two cases `0--1399` are also classified with witness-aware exact replay.
7. The classified multiplicity-two prefix contains `2,800` selectors: `2,799` infeasible and one constructive selector at case `1287`, selector zero, orientation zero.
8. Across support twenty, the exact cache contains `40,399` certified-infeasible selectors, two constructive selectors, `31,459` unclassified selectors, and `3,285,616,695` certified rejection-CSP nodes.
9. For multiplicity-two case zero, orientation three, the first 192 references reduce to 150 relaxed semantic keys. A 115-key irredundant basis covers 204 of 35,112 clean top orders, with exact digest `12529763722981785837`. The first 16 references selected from outside that union add 15 distinct keys and expand exact coverage to 221 clean top orders; `34,891` remain uncovered. The expansion digest is `16150749401146711547`.
10. At side ten, the opposite-pair double coset is completely obstructed in `cc` and `cf`. Fine-row pair indices `0--5199` are obstructed in both `fc` and `ff`, with no constructive witness in those 10,400 geometries.
11. Protected-spread, repair, and carry diagnostics include the first tested genuinely cubic common-rainbow family at order 13, the exact canonical side-six repair-path profile, and complete side-two through side-five carry-level profiles.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors:

- `40,399` certified infeasible;
- `2` constructive;
- `31,459` unclassified.

The unresolved set is exactly:

- `2,440` multiplicity-two signatures containing `4,880` selectors;
- `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1400`. Cases `1400--1409` are registered for exact computation but are not counted until every transcript is promoted and replayed.

For the side-ten opposite-pair fine-row search:

- `fc`: indices `0--5199`, `184,338,885` nodes, maximum `1,877,339`;
- `ff`: indices `0--5199`, `112,022,029` nodes, maximum `909,040`.

Indices `5200--5599` are registered but uncounted.

## Active frontiers

- Complete multiplicity two from case `1400`, then classify multiplicity one.
- Continue side-ten fine-row obstruction from pair index `5200`, then address the larger double cosets.
- Continue semantic-union expansion from the `34,891` uncovered clean top orders and recompute a compact basis for the 221-top expanded union.
- Determine whether the case-`1287` construction has a symmetry orbit or reusable local template.
- Prove the decimal-2873 interval-specific improvement on the first 6.16% of the logarithmic slab, or reduce effective divisor loss.
- Prove cubic protected residual entropy and bounded rank-three completion multiplicity.
- Prove a global bounded-barrier repair/resampling theorem.
- Prove second-generation collateral concentration, monotone carry termination, or bounded-denominator absorbers.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no infinite all-side product theorem. The repository contains exact finite classifications, verified constructions, computational obstructions, and conditional reductions. Registered workloads do not advance the certified boundary until their outputs are independently replayed and committed.
