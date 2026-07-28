# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map records the active frontiers after PX1032. No item below is a proof of
the classical no-three-in-line conjecture or an all-side product theorem.

## 1. Effective asymptotic repair path

**Status: effective for `N>=10^2874`; baseline divisor routes optimized or
refuted.**

The paired repair path uses

\[
\mathfrak d(N)<10^{2469/41}N^{6/41}
\]

and closes every active inequality for `N>=10^2874`. The universal
Euler-product exponent family cannot lower the integral cutoff. The classical
Nicolas--Robin subexponential bound reaches only `10^14104` when inserted
unchanged.

At `N=10^2873`, the optimal retained-order margin lies between `-0.093413` and
`-0.093412`. A uniform 10% improvement in the ambient divisor cap is sufficient
through the complete decimal-2873 slab, while 9% is insufficient.

**Frontier:** prove that 10% interval-specific improvement, reduce the effective
divisor loss in the retained-order inequality, or build a structural extension
or absorber chain below `10^2874`.

## 2. Finite side-seven full-selector census

**Status: exact through multiplicity-two case 559; cases 560--639 registered.**

All selectors of multiplicity at least three are classified: `37,600` are
infeasible and one multiplicity-four selector is constructive. The first `560`
multiplicity-two signatures add another `1,120` infeasible selectors.

Current committed boundary:

- `38,720` certified-infeasible selectors;
- one constructive selector;
- `33,139` unclassified selectors;
- `3,006,271,316` certified rejection-CSP nodes.

The unresolved cache is exactly:

- `3,280` multiplicity-two signatures containing `6,560` selectors;
- `26,579` multiplicity-one selectors.

An eight-shard workflow is registered for cases `560` through `639`. It is not
counted until exact transcripts are promoted.

**Frontier:** continue canonical ten-signature proof units while replacing raw
bottom DFS by compact cover-based master nogoods where possible.

## 3. Low-multiplicity certificate compression

**Status: seven-triple covers, semantic deletion, and actual-key deduplication
proved for the dominant repeated support class.**

For case zero, orientation three, 128 selector/top obligations through 64 top
orders all have seven-triple covers. A 55-triple dictionary and 93 cover lists
encode all 896 entries.

The most frequent syntactic support mask `6975` occurs for both selectors at
twelve top orders. Semantic deletion gives mask `6936` at eleven references and
mask `6920` at one. Deduplicating the actual partial assignments yields only five
keys:

- four assignments on mask `6936`;
- one assignment on mask `6920`.

Their extension lists contain 40 occurrences but only 14 distinct clean top
orders, with 26 overlaps and 403,200 exact bottom checks.

**Frontier:** extend semantic deletion to the other support classes and
orientations, deduplicate all actual assignments, and solve a compact set-cover
problem against the complete clean-top family.

## 4. Recursive closure from produced bases

**Status: affine recursion closed at bases 8, 10, and 12; smallest non-affine
double coset partly closed.**

Exact products include `2x3 -> 6`, `2x4 -> 8`, `2x5 -> 10`, and `2x6 -> 12`.
Every rectangle output lies in the all-transposition relative class.

At side ten, the three affine transposition double cosets have sizes `800`,
`800`, and `200`. The complete opposite-pair coarse-row searches are infeasible:

- `cc`: 8,000 geometries and 152,056,230 nodes;
- `cf`: 8,000 geometries and 114,391,525 nodes.

Any template in that double coset must use `fc` or `ff`.

**Frontier:** finish the opposite-pair fine-row orientations in bounded replay
intervals, then enumerate the two larger double cosets or prove a produced-base
extension theorem.

## 5. Global product repair and exact-cover selection

**Status: open.**

The full product host has exact SAT encodings, alternating-cycle connectivity,
carry bounds, and finite repair-barrier classifications. Triple-count and
pair-energy potentials are not monotone. Dense superregular hosts support spread
selections, but not yet the required negative-dependency or resampling theorem.

**Frontier:** prove a global repair/resampling theorem or an exact conflict-free
perfect-matching/cover theorem with the required local-load endpoint.

## 6. Hyperbola, carry, and bounded-denominator geometry

**Status: open after first-generation neutralization.**

Weighted quotient extraction, common-ratio conversion, secant-star carry
dispersion, perfect-alignment arithmetic, wrap-center factorization, and
alternating endpoint neutralization are proved.

**Frontier:** establish second-generation collateral concentration, a monotone
alternating carry-complexity potential, or row-column-preserving absorbers for
bounded-denominator chambers.

## 7. Operational priorities

1. Promote cases `560--639` and continue the finite census.
2. Extend semantic-core generation to all support classes in the 64-top prefix.
3. Prove the 10% decimal-2873 arithmetic improvement or reduce divisor loss.
4. Complete bounded side-ten `fc`/`ff` opposite-pair intervals.
5. Develop the global exact-cover/resampling and hyperbola/carry closure routes.

## Verification entry points

```bash
python scripts/verify_product_2873_divisor_improvement_target.py
python scripts/verify_product_nicolas_robin_divisor_baseline.py
python scripts/verify_product_transposition_double_coset_opposite_coarse_ten.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_repeated_semantic_cores.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..55}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
