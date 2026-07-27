# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map reconciles the finite selector census, the paired asymptotic repair
path, recursive produced-base searches, and the independent geometric and
matching frontiers. It records what is actually open after PX1012.

No item below is a proof of the classical no-three-in-line conjecture unless it
is explicitly promoted to an all-side theorem; no such promotion has occurred.

## 1. Effective asymptotic repair path

**Status: proved reduction above an explicit, family-optimal cutoff.**

The paired rectangle-label path is effective for every

\[
\boxed{N\ge10^{2874}}
\]

using

\[
\mathfrak d(N)<10^{2469/41}N^{6/41}.
\]

PX966--PX969 optimize the complete universal Euler-product exponent family and
show that it cannot lower the integral decimal cutoff. PX994--PX996 audit the
classical Nicolas--Robin subexponential divisor bound; inserted unchanged, it
reaches only `N>=10^14104`.

**Frontier:** cover the interval below `10^2874` using interval-specific
arithmetic, a retained-order inequality with less ambient-divisor loss,
structural extension chains, exact absorbers, or recursive produced-base
closure. The two baseline universal divisor routes are closed.

## 2. Finite side-seven full-selector census

**Status: exact through multiplicity-two case 399; cases 400--479 running.**

All selectors of multiplicity at least three are classified: `37,600` are
infeasible and one multiplicity-four selector is constructive. The first `400`
multiplicity-two signatures add another `800` infeasible selectors.

Current committed boundary:

- `38,400` certified-infeasible selectors;
- one constructive selector;
- `33,459` unclassified selectors;
- `2,922,421,260` certified rejection-CSP nodes.

The unresolved cache is exactly:

- `3,440` multiplicity-two signatures containing `6,880` selectors;
- `26,579` multiplicity-one selectors.

A durable eight-shard matrix covers cases `400` through `479`. It is not counted
until its exact transcripts are promoted.

**Frontier:** continue canonical ten-signature proof units while replacing raw
bottom DFS where possible by compact cover-based master nogoods.

## 3. Low-multiplicity certificate compression

**Status: bottom-cover compression and semantic two-selector learning proved.**

For one fixed top order, bottom infeasibility is equivalent to covering all
`5,040` bottom permutations by collinear abstract triples.

For multiplicity-two case zero, orientation three:

- 128 selector/top obligations through 64 top orders all have seven-triple
  covers;
- 55 triples and 93 cover lists encode 896 cover entries;
- only 37 syntactic top-support masks occur;
- every support fixes at most 11 of 14 top columns.

At top order `35`, semantic deletion shrinks the selector supports to sizes six
and five. Their seven-column union mask `11546` refutes both selectors across
four clean top extensions and 40,320 exact bottom checks. This is an
inclusion-minimal master nogood for the stored cover pair.

**Frontier:** minimize repeated cover/support classes across the 64-top prefix,
measure master-nogood coverage of the complete top-order family, and construct a
small replay vocabulary before multiplicity one.

## 4. Recursive closure from produced bases

**Status: affine-column recursion ruled out at bases 8, 10, and 12; the smallest
non-affine double coset is partly closed.**

Exact factor-independent products include

\[
2\times3\to6,
\quad
2\times4\to8,
\quad
2\times5\to10,
\quad
2\times6\to12.
\]

Every rectangle output lies in the all-transposition relative class. At side
ten, transpositions split into affine double cosets of sizes `800`, `800`, and
`200`. The complete opposite-pair coarse-row searches are infeasible:

- `cc`: `8,000` geometries and `152,056,230` nodes;
- `cf`: `8,000` geometries and `114,391,525` nodes.

Thus any template in that double coset must use `fc` or `ff`. Those fine-row
families and both larger double cosets remain open.

**Frontier:** finish the opposite-pair fine-row orientations in bounded replay
intervals, then enumerate the two 800-map double cosets or prove a produced-base
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

Weighted quotient extraction, common-ratio bank conversion, universal
secant-star carry dispersion, perfect-alignment arithmetic, wrap-center
factorization, and alternating endpoint neutralization are proved. One-colour
carry-cycle dispersion is refuted.

**Frontier:** establish second-generation collateral concentration, a monotone
alternating carry-complexity potential, or row-column-preserving absorbers for
bounded-denominator interpolation chambers.

## 7. Operational priorities

1. Promote the `400--479` side-seven transcripts and continue the finite census.
2. Extend semantic cover minimization from one master nogood to a reusable
   vocabulary over the 64-top prefix.
3. Seek interval-specific arithmetic or reduced divisor loss below `10^2874`.
4. Complete the side-ten opposite-pair fine-row double-coset searches.
5. Develop the global exact-cover/resampling theorem and independent
   hyperbola/carry termination routes.

## Verification entry points

```bash
python scripts/verify_product_three_forty_first_divisor_cutoff.py
python scripts/verify_product_universal_divisor_cutoff_optimality.py
python scripts/verify_product_nicolas_robin_divisor_baseline.py
python scripts/verify_product_transposition_double_coset_opposite_coarse_ten.py
python scripts/verify_product_side_seven_multiplicity2_case0_bottom_cover8.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_bottom_cover64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_cover_support64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..39}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
