# Sparse rollback levels, colour factors and mixed cycles are exact construction operations

This chapter records CMR3122--CMR3137 and installs CMR462--CMR476 as literal ancestry.

Executable checker:

```text
scripts/check_prime_power_rollback_level_colour_cycle_ancestry.py
```

## CMR3122 — literal binary-cost rollback face

For every side-three final matchable host and essential final edge, the complete ancestor-minus-edge matching family is regenerated. Deleted final-host edges are the exact marked restoration set. The canonical minimum-cost face, base matching, tight potential and optimal-allowed core are reconstructed from literal edges.

## CMR3123 — exact level-cut conservation

For every optimum and every adjacent potential cut, upward and downward permutation arrows are counted and checked equal. No aggregate balance is inferred without checking each cut.

## CMR3124 — sparse cross-level skeleton

Every upward arrow is a marked edge replacing an unmarked base edge. Hence upward and downward counts are equal and at most the minimum rollback cost `k`; every cross-level skeleton is even and has size at most `2k`.

## CMR3125 — balanced residual levels

At every potential level, outgoing and incoming cross-level endpoint counts are equal. Removing them leaves one literal source and target residual of equal size.

## CMR3126 — exact conditional level product

For every observed skeleton, each residual same-level host is generated from the optimal-allowed core. The Cartesian product of its perfect-matching families, together with the fixed skeleton, is checked to equal exactly the global optimum states carrying that skeleton.

## CMR3127 — finite skeleton identity

Skeletons are stored as canonical ordered cross-level edge tuples. The side-three census contains 835 distinct skeleton occurrences across the 513 rollback pairs. The general theorem bound `(k+1)t^(4k)` is retained as the owner-witness stock.

## CMR3128 — right-endpoint cost polarization

Inside every residual same-level host, every edge entering one residual right endpoint has the cost of that endpoint's base edge. Thus all local perfect matchings have one fixed marked cost.

## CMR3129 — exact source-split product

Local states are partitioned by the source set sent to marked right endpoints. For each source set, the checker regenerates the marked-column and unmarked-column factor families and verifies their exact Cartesian product.

## CMR3130 — mixed-colour cycle criterion

Relative to the first local matching, the contraction digraph is generated. The marked-source split is unique exactly when every strongly connected component is colour-homogeneous. A mixed component yields a literal zero-cost mixed-colour cycle.

## CMR3131 — cyclic boundary arcs

Every cyclic arc crossing the two endpoint colours receives one canonical shortest return path and one simple mixed witness cycle. The witness family is indexed exactly by boundary arcs.

## CMR3132 — packing or concentration

At threshold three, canonical witnesses either concentrate at one contraction vertex or greedily yield the theorem-mandated vertex-disjoint packing. Both alternatives occur in the finite regression.

## CMR3133 — simultaneous zero-cost batch

Pairwise vertex-disjoint witness cycles are flipped independently. Every subset gives a distinct perfect matching and a distinct marked-source split.

## CMR3134 — sparse-tail deletion

The tails of cyclic boundary arcs are deleted as matching pairs. The residual contraction digraph is regenerated and checked to contain no mixed-colour cycle; its matching family therefore has the colour-separated product.

## CMR3135 — exhaustive finite census

```text
247 matchable final hosts
513 essential rollback pairs
1,116 optimum-state incidences
835 sparse level skeletons
644 cross-level edge incidences
1,481 residual level hosts
1,286 colour-separated residual hosts
195 mixed-colour residual hosts
412 cyclic boundary arcs and witness cycles
173 packed cycle witnesses
22 concentration hosts
390 sparse-tail matching-pair deletions
```

## CMR3136 — corruption rejection

Eight independently resealed mutations are rejected, including contract substitution, altered rollback-pair census, negative skeleton count, false theorem flags, an all-`n` flag and broken boundary/witness equality.

Contract digest:

```text
b97b2553cf5548cfc32a022172d2e011bc60952021d87178ae0e0fdc673ecc23
```

## CMR3137 — T02 consequence and honesty boundary

Installed kinds:

```text
rollback-level-skeleton-restriction
rollback-residual-level-factorization
same-level-colour-source-split
colour-separated-level-factorization
mixed-colour-cycle-batch-flip
mixed-cycle-sparse-tail-deletion
```

Exact flags:

```text
rollback_level_skeleton_ancestry_proved = 1
same_level_colour_split_ancestry_proved = 1
mixed_cycle_packing_ancestry_proved = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Boundary-fan, rooted-conflict, line-clean and unavailable-edge operations remain open. No all-`n` theorem is claimed.
