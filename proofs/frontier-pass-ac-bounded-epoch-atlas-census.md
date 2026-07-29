# Frontier pass: AC bounded-epoch atlas census

## Active branch

`agent/ac-bounded-epoch-atlas-census`

Parent: `agent/ac-kernel-coverage-atlas` at `6f97f7fa0fc0f8e9c250ff72590211aee4bd7ed4`.

Only AC is active. Historical AC, RI, BDA, GC, OP, SRR, SAS and all-n branches remain immutable source libraries.

## New theorem block

- **AC5in:** canonical bounded-epoch pair/state/edge incidence matrix and first malformed prerequisite, object record, capacity record or unknown-object witness.
- **AC5io:** deterministic marginal-gain atlas construction, reverse deletion and private-object/dependency-critical irredundancy witnesses.
- **AC5ip:** exact minimum prerequisite-closed atlas under the objective `(total construction weight, number of templates, lexicographic template list)`.
- **AC5iq:** candidate-neighbourhood bottleneck packing lower bound and exact zero-neighbourhood frontier witness.
- **AC5ir:** selected-atlas union certificate and finite episode bound using only globally deduplicated capacities referenced by the exact minimum atlas.

## Logical gain

The preceding coverage atlas measured missing pairs, states and edges, but did not determine which historical templates should be retained or whether a smaller complete atlas existed.

For a bounded physical epoch `U=Omega sqcup V sqcup E`, the new census compiles the candidate incidence matrix `M_(x,i)`. Every greedy insertion lowers the exact uncovered count

\[
U(A)=|\mathcal U\setminus\bigcup_{i\in A}C_i|
\]

by its measured marginal gain. Reverse deletion leaves an irredundant closed atlas in which every template has either a private physical object or a dependency-critical selected template.

The exact optimizer then computes

\[
A_{\min}
=\arg\min_A
\left(
\sum_{i\in A}w_i,
|A|,
\operatorname{lex}(A)
\right)
\]

over all complete, consistent, prerequisite-closed atlases.

For every physical object `x`, the candidate neighbourhood `N(x)` records every template capable of covering it. A family of objects with pairwise disjoint candidate neighbourhoods gives a certified atlas-size lower bound. `N(x)=empty` is the exact next construction target.

The selected-atlas episode bound is

\[
E_{\min}
\le
(C_{\rm reset}^{\min}+1)\Psi_*
+U^{\min}W_{\rm dist}^{\min}
+C_{\rm pay}^{\min}
+C_{\rm ticket}^{\min},
\]

with every physical capacity alias counted once.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_bounded_epoch_atlas_census.py` checks 2,500 bounded epoch systems:

- 500 complete valid censuses;
- 500 exact uncovered-object routes;
- 500 object-overlap conflict routes;
- 500 malformed-prerequisite routes;
- 500 capacity-alias conflict routes.

The 500 valid censuses contain:

- 7,596 physical pair/state/edge objects;
- 4,214 candidate templates;
- 2,025 templates in the irredundant greedy atlases;
- 1,951 templates in the exact minimum atlases;
- greedy construction weight 7,756;
- exact minimum construction weight 6,862;
- 1,859 private physical-object witnesses;
- 166 dependency-critical witnesses;
- bottleneck-packing lower-bound total 1,567;
- raw selected capacity amount 11,975;
- globally unique selected capacity amount 7,092;
- 4,883 units removed as alias double counting;
- aggregate selected-atlas episode bound 110,691.

All assertions pass.

## Remaining AC frontier

1. Serialize the first actual bounded physical AC epoch into `Omega sqcup V sqcup E`.
2. Generate historical template candidates with exact prerequisites and construction weights.
3. Run AC5in and remove malformed candidates.
4. Compute the exact minimum physical atlas with AC5ip.
5. Use zero- and low-neighbourhood objects from AC5iq as the next construction queue.
6. Certify the selected union graph, bridges and physical capacity quotient.
7. Run AC5ir on the selected physical atlas.
8. Enlarge the epoch or discharge its first exact returned object.

AC6 and the global no-three-in-line conjecture remain open.
