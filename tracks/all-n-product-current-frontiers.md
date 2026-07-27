# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map reconciles the finite selector census, the paired asymptotic repair
path, recursive produced-base searches, and the independent geometric and
matching frontiers. It records what is actually open after PX999.

No item below is a proof of the classical no-three-in-line conjecture unless it
is explicitly promoted to an all-side theorem; no such promotion has occurred.

## 1. Effective asymptotic repair path

**Status: proved reduction above an explicit, family-optimal cutoff.**

The paired rectangle-label path has audited entry, line-cap, packet, mixed,
terminal-return, recurrence, and causal-descent interfaces. The current rational
divisor certificate gives

\[
\mathfrak d(N)<10^{2469/41}N^{6/41}
\]

and verifies every active numerical hypothesis for

\[
\boxed{N\ge10^{2874}}.
\]

PX966--PX969 optimize the entire universal Euler-product exponent family. At
decimal order `2873`, the concave cutoff margin is globally maximized at
`log(2)/log(13033)` but remains below `-0.0934`. Further tuning of that same
universal family cannot lower the integral decimal cutoff.

PX994--PX996 audit the classical Nicolas--Robin subexponential divisor estimate.
Inserted unchanged, it reaches only `N>=10^14104`; it is therefore substantially
weaker than the active power-law certificate in the relevant range.

**Frontier:** cover every order below `10^2874` by a structural extension chain,
interval-specific arithmetic, exact absorbers, or a stronger retained-order
inequality with less ambient-divisor loss. Neither universal exponent tuning nor
the baseline Nicolas--Robin estimate improves the current cutoff.

## 2. Finite side-seven full-selector census

**Status: exact through multiplicity-two case 319; cases 320--399 launched.**

All selectors of multiplicity at least three are classified: `37,600` are
infeasible and one multiplicity-four selector is constructive. The first `320`
multiplicity-two signatures add another `640` infeasible selectors.

Current committed exact boundary:

- `38,240` certified-infeasible selectors;
- one constructive selector;
- `33,619` unclassified selectors;
- `2,899,564,230` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `3,520` multiplicity-two signatures, containing `7,040` selectors;
- `26,579` multiplicity-one signatures/selectors.

A durable eight-shard matrix covers multiplicity-two cases `320` through `399`.
It is not counted until exact transcripts are promoted to replay verifiers.

**Frontier:** continue fixed ten-signature proof shards from global case `320`,
while replacing raw DFS where possible by explicit bottom-permutation triple
covers and assumption-minimized top nogoods.

## 3. Low-multiplicity certificate compression

**Status: exact reduction, generic generators, and first comparative theorem.**

For a fixed clean top order, selector `F` is bottom-infeasible exactly when the
coverage sets of its collinear abstract triples cover all `5,040` bottom
permutations. The selector-family subproblem is infeasible exactly when every
selector has such a cover.

PX997--PX999 measure the first eight top orders of multiplicity-two case zero in
all four orientations. Across 64 selector/top obligations, every greedy cover is
explicitly checked. Orientation three is exceptional:

- every obligation has a seven-triple cover;
- all 112 cover entries use only 19 unique triples;
- only ten distinct covers are needed for sixteen obligations.

The other orientations require 57--60 unique triples and have little or no
complete-cover reuse on this prefix. A 64-top orientation-three saturation
experiment is running.

**Frontier:** measure dictionary growth over wider prefixes, deduplicate repeated
covers across top orders and selector pairs, combine stored covers with minimized
top-assumption cores, and promote only independently replayed proof objects.

## 4. Recursive closure from produced bases

**Status: affine-column recursion ruled out at bases 8, 10, and 12; the smallest
non-affine double coset is partly closed.**

Exact factor-independent products currently include

\[
2\times3\to6,
\qquad
2\times4\to8,
\qquad
2\times5\to10,
\qquad
2\times6\to12.
\]

Every rectangle output belongs to the all-transposition relative class. Exact
row-pattern searches absorb arbitrary `P` and arbitrary spanning degree-two
selection. They rule out affine column pairs at sides eight, ten, and twelve.

At side ten, transpositions split into affine double cosets of sizes `800`,
`800`, and `200`. The smallest, opposite-pair double coset contains `8,000`
geometries per orientation. Its complete coarse-row searches are infeasible:

- `cc`: `152,056,230` nodes;
- `cf`: `114,391,525` nodes.

Thus any template in that double coset must use `fc` or `ff`. Those fine-row
families, and both larger double cosets, remain open. A deterministic exact sample
of 1,000 arbitrary non-affine pairs also finds no witness, but is only evidence.

**Frontier:** finish the opposite-pair fine-row orientations with bounded replay
intervals, then enumerate the two 800-map double cosets or find a produced-base
extension theorem. Representative left cosets are not complete double cosets.

## 5. Global product repair and exact-cover selection

**Status: open.**

The full product host has exact SAT encodings, alternating-cycle connectivity,
carry multiplicity bounds, and finite repair-barrier classifications. Natural
triple-count and pair-energy potentials are refuted as monotone objectives.
Dense superregular hosts support spread two-layer selections, but spread alone
does not supply the required negative-dependency or local resampling theorem.

**Frontier:** prove a global repair/resampling theorem coordinating many
projection fibres, or an exact conflict-free perfect-matching/cover theorem with
the required local-load endpoint.

## 6. Hyperbola, carry, and bounded-denominator geometry

**Status: open after first-generation neutralization.**

Weighted quotient extraction, common-ratio bank conversion, universal secant-star
carry dispersion, perfect-alignment arithmetic, wrap-center factorization, and
alternating endpoint neutralization are proved. One-colour carry-cycle dispersion
is refuted.

**Frontier:** establish second-generation collateral concentration, a monotone
alternating carry-complexity potential, or row-column-preserving absorbers for
bounded-denominator interpolation chambers.

## 7. Operational priorities

1. Promote the `320--399` side-seven transcripts and continue the multiplicity-two
   census.
2. Complete the 64-top orientation-three cover saturation experiment and add
   top-assumption learning.
3. Seek interval-specific divisor bounds or reduced divisor loss below
   `10^2874`; the two baseline universal routes are closed.
4. Complete the side-ten opposite-pair fine-row double-coset searches.
5. Develop the exact-cover/resampling theorem and the independent hyperbola
   termination/absorber routes.

## Verification entry points

```bash
python scripts/verify_product_three_forty_first_divisor_cutoff.py
python scripts/verify_product_universal_divisor_cutoff_optimality.py
python scripts/verify_product_nicolas_robin_divisor_baseline.py
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_splice_interface.py
python scripts/verify_product_transposition_class_ten.py
python scripts/verify_product_transposition_class_twelve.py
python scripts/verify_product_transposition_double_coset_ten.py
python scripts/verify_product_transposition_double_coset_opposite_coarse_ten.py
python scripts/verify_product_side_seven_multiplicity2_case0_bottom_cover8.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..31}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
