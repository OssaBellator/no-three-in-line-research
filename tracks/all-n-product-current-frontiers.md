# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map reconciles the finite selector census, the paired asymptotic repair
path, and the independent geometric and matching frontiers. It records what is
actually open after PX959.

No item below is a proof of the classical no-three-in-line conjecture unless it
is explicitly promoted to an all-side theorem; no such promotion has occurred.

## 1. Effective asymptotic repair path

**Status: proved reduction above an explicit cutoff.**

The paired rectangle-label path has audited entry, line-cap, packet, mixed,
terminal-return, recurrence, and causal-descent interfaces. The sharp rational
divisor certificate gives

\[
\mathfrak d(N)<10^{6425/109}N^{16/109}
\]

and verifies every active numerical hypothesis for

\[
\boxed{N\ge10^{2875}}.
\]

Within the same universal divisor framework, `10^2874` fails the
retained-order inequality. The substantive next step is therefore not another
small decimal optimization.

**Frontier:** cover every order below `10^2875` by a structural extension chain,
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
while searching for a two-candidate symmetry quotient or direct obstruction
certificate before starting multiplicity one.

## 3. Recursive closure from produced bases

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

## 4. Global product repair and exact-cover selection

**Status: open.**

The full product host has exact SAT encodings, alternating-cycle connectivity,
carry multiplicity bounds, and finite repair-barrier classifications. Natural
triple-count and pair-energy potentials are refuted as monotone objectives.
Dense superregular hosts support spread two-layer selections, but spread alone
does not supply the required negative-dependency or local resampling theorem.

**Frontier:** prove a global repair/resampling theorem coordinating many
projection fibres, or an exact conflict-free perfect-matching/cover theorem with
the required local-load endpoint.

## 5. Hyperbola, carry, and bounded-denominator geometry

**Status: open after first-generation neutralization.**

Weighted quotient extraction, common-ratio bank conversion, universal secant-star
carry dispersion, perfect-alignment arithmetic, wrap-center factorization, and
alternating endpoint neutralization are proved. One-colour carry-cycle dispersion
is refuted.

**Frontier:** establish second-generation collateral concentration, a monotone
alternating carry-complexity potential, or row-column-preserving absorbers for
bounded-denominator interpolation chambers.

## 6. Operational priorities

1. Promote durable side-seven multiplicity-two transcripts into replay verifiers
   and advance the finite boundary.
2. Seek a direct two-candidate certificate or symmetry reduction using repeated
   top-order and bottom-node profiles.
3. Build a finite-range bridge below `10^2875`; treat further universal cutoff
   compression as secondary.
4. Target recursive closure at side ten or twelve.
5. Develop the exact-cover/resampling theorem and the independent hyperbola
   termination/absorber routes.

## Verification entry points

```bash
python scripts/verify_product_sharp_rational_divisor_cutoff.py
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_splice_interface.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1,2,3,4,5,6,7}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
