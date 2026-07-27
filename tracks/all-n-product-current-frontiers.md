# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map reconciles the finite selector census, the paired asymptotic repair
path, and the independent geometric and matching frontiers. It records what is
actually open after PX965.

No item below is a proof of the classical no-three-in-line conjecture unless it
is explicitly promoted to an all-side theorem; no such promotion has occurred.

## 1. Effective asymptotic repair path

**Status: proved reduction above an explicit cutoff.**

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

For this fixed `3/41` witness, `10^2873` fails the retained-order inequality.
The substantive next step is therefore a new witness or inequality, but more
importantly a structural finite-range bridge.

**Frontier:** cover every order below `10^2874` by a structural extension chain,
interval-specific arithmetic, exact absorbers, or finite classification.

## 2. Finite side-seven full-selector census

**Status: exact through multiplicity-two case 79.**

All selectors of multiplicity at least three are classified: `37,600` are
infeasible and one multiplicity-four selector is constructive. The first eighty
multiplicity-two signatures add another `160` infeasible selectors.

Current exact boundary:

- `37,760` certified-infeasible selectors;
- one constructive selector;
- `34,099` unclassified selectors;
- `2,797,478,913` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `3,760` multiplicity-two signatures, containing `7,520` selectors;
- `26,579` multiplicity-one signatures/selectors.

**Frontier:** continue fixed ten-signature proof shards from global case `80`,
while replacing raw DFS where possible by explicit bottom-permutation triple
covers and assumption-minimized top nogoods.

## 3. Low-multiplicity certificate compression

**Status: exact reduction implemented; finite measurements pending.**

For a fixed clean top order, selector `F` is bottom-infeasible exactly when the
coverage sets of its collinear abstract triples cover all `5,040` bottom
permutations. The selector-family subproblem is infeasible exactly when every
selector has such a cover.

Two generic tools now compare:

- first-bad-triple dictionary compression;
- deterministic greedy triple-subcover compression.

**Frontier:** measure case zero in all orientations, deduplicate repeated covers
across top orders and selector pairs, then combine them with minimized top
assumption cores. Promote only independently replayed stored covers.

## 4. Recursive closure from produced bases

**Status: open.**

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

The arbitrary-map one-inner-layer family is completely classified through base
eight and cannot simply iterate the side-four template. Full side-six selector
classes are solved, but no theorem recursively closes sides ten or twelve.

**Frontier:** prove a produced-base iteration theorem, find larger successful
cycle-type templates, or construct an extension mechanism compatible with the
paired repair path.

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

1. Promote durable side-seven multiplicity-two transcripts into replay verifiers
   and advance the finite boundary.
2. Measure and minimize bottom triple covers, then add top assumption learning.
3. Build a finite-range bridge below `10^2874`; treat further universal cutoff
   compression as secondary.
4. Target recursive closure at side ten or twelve.
5. Develop the exact-cover/resampling theorem and the independent hyperbola
   termination/absorber routes.

## Verification entry points

```bash
python scripts/verify_product_three_forty_first_divisor_cutoff.py
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_splice_interface.py

g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_bottom_certificate_dictionary.cpp \
  -o /tmp/m2-dictionary

g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_bottom_triple_cover.cpp \
  -o /tmp/m2-cover

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1,2,3,4,5,6,7}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
