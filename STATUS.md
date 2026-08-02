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
6. All side-seven support-twenty selectors of multiplicity at least three are classified. Multiplicity-two cases `0--1439` are also classified with witness-aware exact replay.
7. The classified multiplicity-two prefix contains `2,880` selectors: `2,879` infeasible and one constructive selector at case `1287`, selector zero, orientation zero.
8. Across support twenty, the exact cache contains `40,479` certified-infeasible selectors, two constructive selectors, `31,379` unclassified selectors, and `3,297,611,555` certified rejection-CSP nodes.
9. The semantic-compression frontier has 208 references, 165 relaxed keys, 221 covered clean top orders, and `34,891` uncovered clean top orders. The basis digest is `12529763722981785837`; the expansion digest is `16150749401146711547`.
10. At side ten, fine-row pair indices `0--6799` are obstructed in both `fc` and `ff`, with no constructive witness in those 13,600 geometries.
11. Protected-spread, repair, and carry diagnostics include the first tested genuinely cubic common-rainbow family at order 13, the exact canonical side-six repair-path profile, and complete side-two through side-five carry-level profiles.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors:

- `40,479` certified infeasible;
- `2` constructive;
- `31,379` unclassified.

The unresolved set is exactly `2,400` multiplicity-two signatures containing `4,800` selectors plus `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `1440`. Cases `1440--1449` are registered but uncounted.

For side ten:

- `fc`: indices `0--6799`, `232,466,543` nodes, maximum `1,877,339`;
- `ff`: indices `0--6799`, `150,194,835` nodes, maximum `909,040`.

Indices `6800--7199` are registered but uncounted.

## Active frontiers

- Continue multiplicity two from case `1440`, then classify multiplicity one.
- Continue side-ten fine-row obstruction from pair index `6800`, then address larger double cosets.
- Continue semantic-union expansion from the `34,891` uncovered clean top orders and recompute a compact basis for the 221-top union.
- Determine whether the case-`1287` construction has a symmetry orbit or reusable local template.
- Advance the decimal-2873 arithmetic, protected-spread, global repair, and carry/absorber frontiers without upgrading conditional statements.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no infinite all-side product theorem. Registered workloads do not advance the certified boundary until their outputs are independently replayed and committed.
