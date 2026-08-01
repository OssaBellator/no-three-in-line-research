# SCC branching, support compression and minimum-face lineage have exact executable ancestry

This chapter records **CMR3702--CMR3721** and installs source theorems CMR854--CMR925.

Canonical checker:

```text
scripts/check_prime_power_scc_branch_minimum_face_ancestry.py
```

Contract:

```text
3ec89baac0450290c3dbe3a340af76aaea95bf7f4c84342a9aac8f7c31862498
```

## CMR3702--CMR3705 — generic exchange-SCC normal form

Every matchable side-three bipartite host and every perfect matching node are regenerated. A nonmatching edge is usable exactly when its exchange arc lies on a directed cycle, equivalently when the arc endpoints lie in one strongly connected component. Removing cross-SCC inactive edges preserves the perfect-matching family. The family factors exactly over SCC blocks, and local distinguishing widths add.

## CMR3706 — componentwise minimum branch cover

Minimum local feedback-vertex sets assemble one exact global distinguishing cover. Every child deletion is confined to one SCC block and leaves the other exact product factors unchanged.

## CMR3707--CMR3709 — exact constant-arity prescription split

For every nonempty prescription of rank at most three, the family is the exact union of its single-edge deletion children and its conditioned child. Ordered prescriptions give a disjoint first-missing partition. A conditioned prescription contracts exactly and transfers its residual rank.

## CMR3710 — canonical new-triple response

Every nonimproving target-destroying candidate in the finite joint-state bank supplies a genuinely new labelled collinear triple containing an edge outside the current minimum anchor. Its complete response has at most three deletion children and one conditioned forced-triple child.

## CMR3711--CMR3713 — support packing and edge batching

Every canonical triple has exactly nine support atoms: three physical cells and six labelled matching endpoints. Distinct signatures either pack support-disjointly or admit a bounded support cover. Concentration on a cell or matching vertex stabilises one exact labelled edge, whose binary split batches all associated signatures. Conditioning on that edge contracts it and converts every associated triple to a rank-two residual pair.

## CMR3714--CMR3715 — path budgets and terminal compression

Distinct support-disjoint signatures consume finite deletion or rank-three contraction stock. The target-resolution tree fixes or deletes an undecided edge at every step. Its leaves partition the positive-potential family and compress first by physical target and then by one of eight layer assignments into fixed labelled-triple classes.

## CMR3716--CMR3718 — minimum-anchor path

An actual minimum state survives every deletion of an edge outside it. The checker repeatedly deletes canonical new-triple edges outside the minimum anchor, forces one physical target and then its chosen labelled assignment, and contracts the common prescription while preserving minimality for the induced residual objective.

## CMR3719 — minimum-face edge dichotomy

For every labelled ambient edge, either some minimum state omits it and authorises minimum-preserving deletion, or every minimum state contains it and it lies in the complete minimum core. Contracting the complete minimum core leaves a residual minimum family with empty common core.

## CMR3720 — branch-wide physical-edge lineage budget

One uncharged first closure is allowed per structural owner slot. Every later active appearance of the same edge requires a genuine restoration unless the edge enters the minimum core and contracts. The owner-slot, restoration, token-incidence and total active-edge bounds are checked through side twelve and envelope depth four.

## CMR3721 — finite census and honesty boundary

```text
247 matchable side-three hosts
384 matching nodes
2,304 usable-edge checks
384 exact SCC product checks
384 SCC width/FVS checks
384 componentwise branch covers
12 labelled saturated joint states
4,095 nonempty joint-state families
1,007,616 exact prescription splits
1,007,616 ordered disjoint partitions
73,710 minimum-face edge dichotomies
444 canonical new-triple witnesses
450 minimum-anchor forcing deletions
7 target-resolution tree nodes
5 terminal leaves
4 fixed labelled-target classes
192 path-budget parameter checks
9 rejected contract corruptions
```

Exact flags:

```text
generic_exchange_scc_width_exact = 1
new_triple_constant_arity_split_exact = 1
new_triple_support_packing_exact = 1
constant_arity_path_budget_exact = 1
support_atom_edge_batching_exact = 1
disjoint_leaf_certificate_compression_exact = 1
minimum_anchor_preserving_path_exact = 1
minimum_face_edge_dichotomy_exact = 1
minimum_face_edge_lineage_budget_exact = 1
scc_branch_minimum_face_ancestry_proved = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

This checker installs the literal CMR854--CMR925 operations only. It does not prove that every later owner transition is installed, that the full operation bank is globally exhaustive, or that every construction branch terminates.
