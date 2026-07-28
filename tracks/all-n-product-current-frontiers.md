# All-n product construction: current frontier map

**Branch:** `research/all-n-product-construction`

This map records the active frontiers after PX1057. No item below proves the classical no-three-in-line conjecture or an all-side product theorem.

## 1. Effective asymptotic repair

The paired repair path is effective for every `N>=10^2874` using `d(N)<10^(2469/41)N^(6/41)`. Universal exponent tuning cannot lower the integral cutoff, and the Nicolas--Robin baseline reaches only `10^14104`.

At `10^2873`, a uniform 10% improvement in the ambient divisor cap suffices through the complete decimal slab; 9% does not.

**Frontier:** prove that interval-specific improvement, reduce effective divisor loss, or build a structural extension/absorber chain below `10^2874`.

## 2. Side-seven finite census

**Status: exact through multiplicity-two case 719; cases 720--799 registered.**

Committed boundary:

- `39,040` certified-infeasible selectors;
- one constructive selector;
- `32,819` unclassified selectors;
- `3,073,826,508` certified rejection-CSP nodes.

The unresolved cache is exactly `3,120` multiplicity-two signatures (`6,240` selectors) plus `26,579` multiplicity-one selectors.

**Frontier:** continue canonical ten-signature proof units and replace raw bottom DFS with compact cover-based master nogoods where possible.

## 3. Low-multiplicity certificate compression

Every case-zero orientation-three obligation through 64 top orders has a seven-triple cover. Thirty references in six repeated paired-equal support groups have now been semantically minimized:

- first group: twelve references, five actual keys, fourteen covered top orders;
- second group: eighteen references, sixteen actual keys, forty-seven covered top orders.

Both selectors have the same minimized mask at every measured reference. A combined 21-key census is measuring the exact cross-group top-order union.

**Frontier:** finish that union, extend to unequal-support and singleton groups, and solve a compact set-cover problem over the complete clean-top family.

## 4. Produced-base recursion

The complete opposite-pair double coset is infeasible in coarse-row orientations:

- `cc`: 8,000 geometries, 152,056,230 nodes;
- `cf`: 8,000 geometries, 114,391,525 nodes.

Pair indices `0` through `799` are infeasible in both fine-row orientations:

- `fc`: 800 geometries, 4,076,728 nodes;
- `ff`: 800 geometries, 2,659,076 nodes.

An exact matrix is registered for pair indices `800` through `1199` in both fine orientations.

**Frontier:** finish the opposite-pair fine-row orientations, then enumerate the two larger double cosets or prove a produced-base extension theorem.

## 5. Protected spread

Complete order-five and order-seven simultaneous-rainbow families have sizes `10` and `28`, with rank-three cylinder constants `6` and `15/2`. Any absolute rank-three bound requires `Omega(ell^3)` family size.

**Frontier:** prove cubic common-rainbow abundance with controlled rank-three completion multiplicity, uniformly after conditioning.

## 6. Global repair and carry coordination

In the canonical side-six repair graph, all 546 states are within two unweighted moves of a solution. Exactly ten states require any temporary defect increase, and each requires only one. One state requires three moves to preserve the minimum barrier although every two-step route rises higher.

**Frontier:** prove a global bounded-barrier resampling theorem that permits controlled uphill collateral without accumulation across fibres.

## 7. Hyperbola and bounded-denominator geometry

Weighted quotient extraction, common-ratio conversion, secant-star carry dispersion, perfect-alignment arithmetic, wrap-center factorization, and alternating endpoint neutralization are proved.

**Frontier:** establish second-generation collateral concentration, alternating carry termination, or row-column-preserving absorbers.

## Operational priorities

1. Promote side-seven cases `720--799`.
2. Promote side-ten fine intervals `800--1199`.
3. Complete the combined semantic vocabulary union and extend to remaining support classes.
4. Prove cubic protected-rainbow abundance.
5. Prove the decimal-2873 arithmetic improvement or reduce divisor loss.
6. Develop bounded-barrier resampling and hyperbola/carry closure.

## Verification entry points

```bash
python scripts/verify_product_2873_divisor_improvement_target.py
python scripts/verify_product_protected_rainbow_cylinder_census.py
python scripts/verify_product_side_six_repair_barrier_profile.py
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_0_399.py
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_400_799.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_next_equal.py
```
