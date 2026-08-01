# Minimum rollback faces restrict and factor exactly

This chapter records CMR3084--CMR3097. It installs the CMR448--CMR461 minimum-cost rollback face, tight-host restriction, SCC factorization and marked ancestor-reset normalization as literal construction operations.

The executable checker is:

```text
scripts/check_prime_power_rollback_optimal_face_scc_ancestry.py
```

## CMR3084 — binary-cost rollback context

For a final host `G`, complete deletion-pass ancestor and essential edge `e`, every ancestor edge outside `G` has cost one and every final-host edge has cost zero. The feasible family is the exact perfect-matching family of the ancestor with `e` removed.

## CMR3085 — rollback number as exact minimum cost

The checker enumerates every feasible matching, computes its marked-edge cost and verifies that the minimum equals the canonical rollback number from the restoration checker.

## CMR3086 — canonical optimum matching

The lexicographically first minimum-cost matching is selected as the base state. Its restored-edge set is a minimum rollback footprint.

## CMR3087 — no-negative-cycle invariant

Every nonmatching ancestor edge generates one contraction arc with weight equal to entering cost minus replaced matching-edge cost. Bellman--Ford relaxation from an auxiliary zero source verifies that no directed alternating cycle has negative total weight.

## CMR3088 — exact shortest-path potential

Integral shortest-path potentials are computed and every reduced arc weight is checked nonnegative. The potential range satisfies

\[
-k\le\phi\le0,
\]

where `k` is the minimum rollback cost.

## CMR3089 — exact tight-host restriction

The tight host consists of the base matching plus every zero-reduced-cost nonmatching edge. Its perfect-matching family is regenerated and checked to equal exactly the complete minimum-cost rollback family.

## CMR3090 — zero-cycle connectivity

Every minimum rollback state differs from the base by zero-cost alternating cycles contained in the tight host. Positive-cost excursions are excluded from the canonical operation.

## CMR3091 — optimal-allowed core

The tight contraction digraph is decomposed into strongly connected components. The union of all minimum rollback states is exactly the base matching plus tight edges whose arc endpoints lie in the same component.

Cross-component tight edges are rejected as unusable dual-tight edges.

## CMR3092 — exact SCC product

The minimum rollback family factors exactly over the induced strongly connected blocks. The checker forms the Cartesian product of all local block matching families and verifies equality with the global optimum family.

## CMR3093 — additive local rollback cost

Every local perfect matching in a component has the same marked-edge cost as the base restriction. Local costs sum exactly to the global minimum rollback cost.

## CMR3094 — active block and level bounds

At most `k` SCC blocks are rollback-active. Active vertices occupy at most `k + number_of_active_blocks <= 2k` component-level cells, and the exact concentration lower bound is verified.

## CMR3095 — threshold endpoint

At threshold two, every exhaustive rollback face reaches exactly one selected endpoint:

```text
large rollback-free component
strict factorization into singleton blocks
rollback-active same-level concentration
```

The side-three rollback census exercises the last two endpoints.

## CMR3096 — marked ancestor-reset normalization

The same optimal-face and SCC construction is applied to all 512 binary marked-edge profiles of the complete side-three host. This validates the CMR461 transfer from deleted edges to arbitrary marked return edges.

The exhaustive regression records:

```text
247 matchable final hosts
513 essential rollback pairs
450 minimum cost-one pairs
63 minimum cost-two pairs
1,116 minimum rollback state incidences
3,276 tight-edge incidences
909 SCC factor blocks
513 rollback-active blocks
369 active-level concentration endpoints
144 strict small-block endpoints
512 marked ancestor-reset profiles
10 rejected corruptions
```

The contract digest is:

```text
1281001711d4312dd98b8434e20dffb226b0608a893ffe5cf13f8b8e13940feb
```

## CMR3097 — T02 consequence and honesty boundary

The installed operation kinds are:

```text
rollback-minimum-cost-face-restriction
rollback-tight-host-restriction
rollback-optimal-scc-factor-split
marked-ancestor-reset-optimal-face
```

The checker reports:

```text
rollback_minimum_cost_face_ancestry_proved = 1
rollback_tight_host_exact = 1
rollback_optimal_scc_factorization_exact = 1
marked_ancestor_reset_optimal_face_exact = 1
all_owner_operations_proved = 0
all_scheduler_operations_proved = 0
all_restoration_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Rollback level-skeleton, colour-split, line-clean and unavailable-edge operations remain to be installed. No all-`n` theorem is claimed.
