# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map records the active frontiers after PX1046. No item below is a proof of the classical no-three-in-line conjecture or an all-side product theorem.

## 1. Effective asymptotic repair path

**Status: effective for `N>=10^2874`; baseline divisor routes optimized or refuted.**

The paired repair path uses `d(N)<10^(2469/41) N^(6/41)` and closes every active inequality for `N>=10^2874`. The universal Euler-product exponent family cannot lower the integral cutoff. The Nicolas--Robin subexponential bound reaches only `10^14104` when inserted unchanged.

At `N=10^2873`, the optimal retained-order margin lies between `-0.093413` and `-0.093412`. A uniform 10% improvement in the ambient divisor cap suffices through the complete decimal-2873 slab, while 9% is insufficient.

**Frontier:** prove that 10% interval-specific improvement, reduce effective divisor loss, or build a structural extension or absorber chain below `10^2874`.

## 2. Finite side-seven full-selector census

**Status: exact through multiplicity-two case 639; cases 640--719 registered.**

All selectors of multiplicity at least three are classified: `37,600` are infeasible and one multiplicity-four selector is constructive. The first `640` multiplicity-two signatures add another `1,280` infeasible selectors.

Current committed boundary:

- `38,880` certified-infeasible selectors;
- one constructive selector;
- `32,979` unclassified selectors;
- `3,042,485,047` certified rejection-CSP nodes.

The unresolved cache is exactly:

- `3,200` multiplicity-two signatures containing `6,400` selectors;
- `26,579` multiplicity-one selectors.

An eight-shard workflow is registered for cases `640` through `719`. It is not counted until exact transcripts are promoted.

**Frontier:** continue canonical ten-signature proof units while replacing raw bottom DFS by compact cover-based master nogoods where possible.

## 3. Low-multiplicity certificate compression

**Status: seven-triple covers, semantic deletion, and actual-key deduplication proved for the dominant repeated support class.**

For case zero, orientation three, 128 selector/top obligations through 64 top orders all have seven-triple covers. A 55-triple dictionary and 93 cover lists encode all 896 entries.

The most frequent support mask `6975` occurs for both selectors at twelve top orders. Semantic deletion gives mask `6936` at eleven references and `6920` at one. Deduplicating actual partial assignments yields five keys. Their extension lists contain 40 occurrences but only 14 distinct clean top orders, with 26 overlaps and 403,200 exact bottom checks.

**Frontier:** extend semantic deletion to other support classes and orientations, deduplicate all assignments, and solve a compact set-cover problem against the complete clean-top family.

## 4. Recursive closure from produced bases

**Status: affine recursion closed at bases 8, 10, and 12; smallest non-affine double coset partly closed.**

At side ten, the complete opposite-pair coarse-row searches are infeasible:

- `cc`: 8,000 geometries and 152,056,230 nodes;
- `cf`: 8,000 geometries and 114,391,525 nodes.

The first 400 pair indices are also infeasible in each fine-row orientation:

- `fc`: 400 geometries and 2,168,727 nodes;
- `ff`: 400 geometries and 1,162,728 nodes.

A new exact matrix is registered for pair indices `400` through `799` in both fine orientations.

**Frontier:** finish the opposite-pair fine-row orientations in bounded replay intervals, then enumerate the two larger double cosets or prove a produced-base extension theorem.

## 5. Protected spread and global selection

**Status: exact cubic-entropy barrier established.**

The protected nonlinear problem is a sequential simultaneous-rainbow matching problem. At orders five and seven, the complete families have sizes `10` and `28`, uniformly before and after conditioning, with rank-three cylinder constants `6` and `15/2`. For any nonempty permutation family `F`, `K_3(F)>=(ell)_3/|F|`; therefore an absolute rank-three bound requires `Omega(ell^3)` family size.

**Frontier:** prove cubic common-rainbow abundance with rank-three completion multiplicity control and uniform conditional stability, then insert the resulting joint cylinder bounds into the local-load criterion.

## 6. Global product repair and carry coordination

**Status: exact bounded-uphill finite profile established.**

In the canonical side-six repair graph:

- all 546 states are within two unweighted cycle toggles of a solution;
- exactly ten one-defect states require any temporary defect increase;
- every required increase is exactly one;
- one state requires three moves to maintain the minimum barrier although every two-step route rises to defect at least three.

**Frontier:** prove a global bounded-barrier resampling theorem that permits controlled uphill collateral while preventing accumulation across many projection fibres. Shortest-path and monotone-potential formulations are both too rigid.

## 7. Hyperbola and bounded-denominator geometry

**Status: open after first-generation neutralization.**

Weighted quotient extraction, common-ratio conversion, secant-star carry dispersion, perfect-alignment arithmetic, wrap-center factorization, and alternating endpoint neutralization are proved.

**Frontier:** establish second-generation collateral concentration, alternating carry termination, or row-column-preserving absorbers for bounded-denominator chambers.

## 8. Operational priorities

1. Promote cases `640--719` and continue the finite census.
2. Promote side-ten fine intervals `400--799` and continue bounded recursion search.
3. Extend semantic-core generation to all support classes in the 64-top prefix.
4. Prove cubic protected-rainbow abundance and bounded rank-three completion counts.
5. Prove the 10% decimal-2873 arithmetic improvement or reduce divisor loss.
6. Develop bounded-barrier resampling and hyperbola/carry closure routes.

## Verification entry points

```bash
python scripts/verify_product_2873_divisor_improvement_target.py
python scripts/verify_product_protected_rainbow_cylinder_census.py
python scripts/verify_product_side_six_repair_barrier_profile.py
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_0_399.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..63}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
