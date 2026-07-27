# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map reconciles the finite selector census, the paired asymptotic repair
path, recursive produced-base searches, and the independent geometric and
matching frontiers. It records what is actually open after PX979.

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
`log(2)/log(13033)` but remains below `-0.0934`. Therefore further tuning of the
same universal divisor family cannot lower the integral decimal cutoff.

**Frontier:** cover every order below `10^2874` by a structural extension chain,
interval-specific arithmetic, exact absorbers, stronger retained-order
inequalities, or finite classification.

## 2. Finite side-seven full-selector census

**Status: exact through multiplicity-two case 159.**

All selectors of multiplicity at least three are classified: `37,600` are
infeasible and one multiplicity-four selector is constructive. The first 160
multiplicity-two signatures add another `320` infeasible selectors.

Current committed exact boundary:

- `37,920` certified-infeasible selectors;
- one constructive selector;
- `33,939` unclassified selectors;
- `2,829,870,112` certified rejection-CSP nodes.

The unresolved committed cache consists exactly of:

- `3,680` multiplicity-two signatures, containing `7,360` selectors;
- `26,579` multiplicity-one signatures/selectors.

**Frontier:** continue fixed ten-signature proof shards from global case `160`,
while replacing raw DFS where possible by explicit bottom-permutation triple
covers and assumption-minimized top nogoods.

## 3. Low-multiplicity certificate compression

**Status: exact reduction and generic generators implemented.**

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

**Status: affine-column recursion ruled out at bases 8, 10, and 12.**

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
selection. They now rule out affine column pairs `(T,Q)` at:

- side eight: `4,096` geometries;
- side ten: `6,400` geometries and `165,874,408` nodes;
- side twelve: `9,216` geometries and `175,715,546` nodes.

A deterministic exact side-ten experiment also tests 1,000 genuinely non-affine
column pairs with no witness. This is evidence, not an obstruction theorem.

Thus neither produced base ten nor twelve iterates by keeping both column
labelings affine and hiding all nonlinearity in row assignment or selector
choice.

**Frontier:** enumerate complete non-affine affine-double-coset families or larger
map groups, prove a produced-base extension mechanism, or use the general
low-syndrome repair/resampling path instead of a fixed template. Representative
left cosets must not be confused with complete double cosets.

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

1. Continue side-seven multiplicity-two classification from case `160` and
   promote every transcript into a replay verifier.
2. Measure and minimize bottom triple covers, then add top assumption learning.
3. Build a finite-range bridge below `10^2874`; universal exponent tuning is now
   closed at integral decimal scale.
4. Enumerate complete non-affine column double cosets for produced-base recursion,
   rather than repeating affine or representative-left-coset searches.
5. Develop the exact-cover/resampling theorem and the independent hyperbola
   termination/absorber routes.

## Verification entry points

```bash
python scripts/verify_product_three_forty_first_divisor_cutoff.py
python scripts/verify_product_universal_divisor_cutoff_optimality.py
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_splice_interface.py
python scripts/verify_product_transposition_class_ten.py
python scripts/verify_product_transposition_class_twelve.py
python scripts/verify_product_transposition_nonaffine_sample_ten.py

g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_bottom_certificate_dictionary.cpp \
  -o /tmp/m2-dictionary

g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_bottom_triple_cover.cpp \
  -o /tmp/m2-cover

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
