# Complete state exclusion and distinguishing rank have exact executable ancestry

This chapter records **CMR3658--CMR3677** and installs source theorems CMR830--CMR853.

Canonical checker:

```text
scripts/check_prime_power_complete_branch_distinguishing_rank.py
```

Contract:

```text
d59d5eb82d388c12ba4551c377054d8bdce91b7d10098ebc32c78c56025727cc
```

## CMR3658--CMR3662 — exact complete state exclusion

All 4,095 nonempty families of the twelve labelled side-three saturated two-layer states are generated. At each of 24,576 rejected-state nodes, the viable single-edge children have union exactly equal to the original family minus the rejected state. Viability is equivalent to nonmembership in the complete common core.

## CMR3663--CMR3666 — complete-core branch normal form

The full compatible state-family core contracts exactly. Every residual family has empty core, core rank plus viable child count equals the six-edge state cardinality, singleton nodes are detected exactly, and compressed child covers are verified.

## CMR3667--CMR3669 — distinguishing transversals

For every state-exclusion node, the minimum subset of rejected-state edges hitting every alternative-support set is computed. That subset gives an exact minimum child cover; all 24,576 compressed covers are regenerated.

## CMR3670 — product additivity

Eighteen exact product-family fixtures verify that distinguishing rank adds across disjoint factors.

## CMR3671--CMR3675 — exchange digraph

All 247 matchable side-three bipartite hosts and 384 perfect-matching nodes are generated. Alternative matchings induce directed exchange cycles. The distinguishing rank equals the exact directed feedback-vertex number, and an edge is nonessential exactly when its source vertex lies on a directed cycle.

## CMR3676 — finite census and corruption rejection

```text
4,095 equal-cardinality families
24,576 state-exclusion nodes
147,456 viability/core checks
24,576 compressed branch covers
247 matchable bipartite hosts
384 matching exchange nodes
384 FVS equality checks
1,152 essential-cycle checks
9 rejected contract corruptions
```

## CMR3677 — consequence and honesty boundary

```text
complete_state_exclusion_branching_exact = 1
viable_branch_essential_core_exact = 1
distinguishing_rank_exchange_digraph_exact = 1
complete_branch_distinguishing_rank_proved = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The checker corrects the completeness scope of aggressive anchor normalization. It does not control arbitrary branch-tree width or prove the global theorem.
