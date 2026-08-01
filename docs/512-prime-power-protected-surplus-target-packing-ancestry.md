# Protected robust surplus and minimum-target packing have exact executable ancestry

This chapter records **CMR3798--CMR3817** and installs source theorems CMR1006--CMR1093.

Canonical checker:

```text
scripts/check_prime_power_protected_surplus_target_packing_ancestry.py
```

Contract:

```text
5e90f91f2c8a8679bdeb3fc78ab7b0ed71c2f8d3e09de41b8ad9fc18865bddd8
```

## CMR3798--CMR3801 — entry-rank and layer polarization

All 46,656 ordered transitions between the 216 side-four saturated states are generated. New triples split exactly by physical entry rank. Rank-one triples decompose into secants through one entering cell; higher-rank triples concentrate on one entering pair and its unique loaded line. Every simultaneous secant-star bank is partitioned by actual layer labels into compatible common-layer outside pairs or cross-layer rooted endpoint banks.

```text
31,104 rank-one new-triple incidences
46,656 higher-rank incidences
24,064 cell-disjoint secant-star banks
14,976 common-layer simultaneous banks
9,216 cross-layer simultaneous banks
39,744 entering-pair loaded lines
```

## CMR3802--CMR3805 — loaded lines and simultaneous star absorption

Every selected side-four line profile is polarized to a majority layer. All protected submatchings are tested against the `2k` protected-touch bound. Free line cells form an absorbable matching; zero growth implies the stated large-core threshold. Direct common-layer star and one-side cross-layer growth/core formulas are checked over 9,792 symbolic parameter profiles.

## CMR3806--CMR3809 — minimum-target hypergraph packing

Every dirty side-four state supplies its complete target hypergraph. Maximum vertex-disjoint target banks and their complementary small covers are generated. Rooted line decompositions are exact. Seventy-two states with disjoint target pairs admit the majority-layer representative matching and a degree-two Hall rematching that destroys every target in the chosen subbank.

```text
176 dirty target hypergraphs
72 disjoint-target packing cases
280 small-cover cases
864 rooted line decompositions
72 simultaneous target-escape banks
200 degree-two rematching candidates
```

## CMR3810--CMR3813 — large-core and protected capacity

Selected-skeleton interface arithmetic, target-contraction rank budgets, owner-stage capacities, strict path aggregation, unit-wall tree aggregation and closure-envelope aggregation are checked through side twelve, envelope depth four and routing thresholds two through five.

## CMR3814--CMR3816 — exact endpoints

The finite bank validates the literal alternatives for robust episode protected execution, loaded old-line destruction, simultaneous common/cross-star absorption, disjoint target contraction or escape, large-core coordinate descent and post-capacity zero-growth dispatch.

## CMR3817 — honesty boundary

```text
robust_surplus_entry_rank_exact = 1
secant_star_layer_polarization_exact = 1
entering_pair_line_absorption_exact = 1
robust_surplus_protected_execution_exact = 1
large_protected_core_minimum_descent_exact = 1
loaded_target_line_minimum_absorption_exact = 1
simultaneous_star_direct_absorption_exact = 1
simultaneous_cross_star_absorption_exact = 1
minimum_target_hypergraph_packing_exact = 1
disjoint_target_simultaneous_escape_exact = 1
global_protected_owner_capacity_exact = 1
protected_surplus_target_packing_ancestry_proved = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The checker installs CMR1006--CMR1093 only. It does not prove that selected-routing, later rollback/blocker, Hall-wall or scheduler operations are exhausted.
