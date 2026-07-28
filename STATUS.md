# Status and honesty ledger

**Last updated:** 28 July 2026

## External status

The classical no-three-in-line problem remains unresolved. The analogous no-`(k+1)`-in-line problem is resolved for each fixed `k>=3` and sufficiently large `n`; that does not settle the exceptional `k=2` case studied here.

## What this branch genuinely proves

1. Saturated states decompose into two permutation layers, and product existence has exact finite CSP/SAT encodings.
2. The branch proves factor-independent products `2x3 -> 6`, `2x4 -> 8`, `2x5 -> 10`, and `2x6 -> 12`.
3. Every saturated side-`n` factor has a factor-compatible side-`2n` state with `O(n log n)` bad triples.
4. The audited paired repair path is effective for every `N >= 10^2874`.
5. At decimal order `2873`, the unchanged divisor-improvement threshold lies between `1.0979139` and `1.0979151`; factor `1.097913` is insufficient and `1.097916` is sufficient.
6. All side-seven support-twenty selectors of multiplicity at least three are classified. Multiplicity-two cases `0` through `1199` add `2,400` exact rejections. The committed cache contains:
   - `40,000` certified-infeasible selectors;
   - one constructive selector;
   - `31,859` unclassified selectors;
   - `3,215,626,032` certified rejection-CSP nodes.
7. For case zero, orientation three, the first 128 semantic reference cores reduce to 102 actual partial-assignment keys. Their 316 extension occurrences cover 164 distinct clean top orders, verified by 3,185,280 exact bottom checks. Three selector-zero references require twelve-triple rather than seven-triple greedy covers.
8. At side ten, the complete opposite-pair double coset is infeasible in `cc` and `cf`. Pair indices `0` through `3199` are also infeasible in each of `fc` and `ff`, using 91,512,849 and 64,396,059 nodes respectively.
9. Protected-rainbow cylinder bounds require cubic entropy in every nonempty slice conditioned on at most three edges; the exact order-five and order-seven families collapse to singleton slices after two compatible edges.
10. In the canonical side-six repair graph, every state is within two unweighted moves of a solution. Exactly 102 nonsolutions have a forced minimax-optimal first move, while every bounded-uphill state has at least three optimal exits.
11. Exact carry multiplicity at sides two through five is at most three-fifths of the general cap, with sharp maxima 12, 36, 48, and 72.

## Current exact finite boundary

The side-seven support-twenty cache contains `71,860` selectors:

- `40,000` certified infeasible;
- `1` constructive;
- `31,859` unclassified.

The unresolved set is exactly:

- `2,640` multiplicity-two signatures containing `5,280` selectors;
- `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1200`. Cases `1200` through `1279` are registered but are not counted until their transcripts are promoted.

## Active frontiers

- Prove the approximately `9.7914%` interval-specific decimal-2873 divisor improvement, reduce effective divisor loss, or construct a structural extension below `10^2874`.
- Promote side-ten pair indices `3200` through `3599`, then continue the opposite-pair coset and address the two larger double cosets.
- Extend semantic master learning beyond top index 127 and compute a compact set-cover basis from the 102-key vocabulary.
- Prove cubic simultaneous-rainbow abundance with cubic residual entropy after every rank-at-most-three conditioning.
- Prove a global bounded-barrier repair/resampling theorem that coordinates forced states and the multiple exits at uphill states.
- Improve carry multiplicity asymptotically or prove second-generation collateral concentration, termination, or bounded-denominator absorbers.
- Complete multiplicity two and multiplicity one in the side-seven census.

## Bottom line

There is no complete proof of the classical no-three-in-line conjecture and no all-side product theorem. The active exact matrices are side-seven cases `1200--1279` and side-ten fine-row indices `3200--3599`; both are excluded from the certified boundary until promoted.
