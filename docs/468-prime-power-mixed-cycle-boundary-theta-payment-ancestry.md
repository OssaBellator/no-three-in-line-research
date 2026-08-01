# Mixed-cycle concentration has exact boundary-fan, cut and private-edge operations

This chapter records CMR3162--CMR3177 and installs CMR477--CMR486 as literal ancestry.

Executable checker:

```text
scripts/check_prime_power_mixed_cycle_boundary_theta_payment.py
```

## CMR3162 — literal coloured contraction host

Every loopless side-three contraction digraph and every nonconstant binary right-endpoint colouring are generated. Cyclic colour-boundary arcs are reconstructed from strongly connected components.

## CMR3163 — vertex-to-boundary incidence

Canonical shortest-return cycles are indexed by boundary arcs. For every contraction vertex, labelled-witness multiplicity, distinct underlying cycles and boundary-edge incidence are checked against CMR477.

## CMR3164 — exact return-path representation

For each cyclic boundary arc `a=u->w`, all simple paths from `w` to `u` in `D-a` are generated. Adding `a` gives every simple mixed cycle through `a`, and removing `a` recovers the path.

## CMR3165 — directed edge-Menger equality

The checker brute-forces the largest edge-disjoint return-path family and the smallest return-edge cut and verifies equality for every boundary arc.

## CMR3166 — theta-fan branch

At threshold two, two edge-disjoint return routes generate two literal zero-cost cycle-flip states sharing the boundary arc.

## CMR3167 — small-cut branch

When two edge-disjoint routes do not exist, a nonempty cut of size below two meets every return route.

## CMR3168 — two-edge bottleneck

Every small-cut profile counts return paths through its cut edges and verifies the CMR480 concentration lower bound for one second fixed edge.

## CMR3169 — private entering-edge code

For a theta pair, the entering-edge sets intersect exactly in the common boundary edge. Removing it leaves nonempty pairwise disjoint private route-edge sets.

## CMR3170 — blocker resilience

Every noncore blocker with fewer edges than theta states misses the complete entering set of at least one state.

## CMR3171 — rooted-or-private conflict split

Every clean candidate pair recreated in a theta state is either contained in the base matching plus the boundary edge or contains a private entering edge.

## CMR3172 — aggregate private support

Nonrooted recreated conflicts are assigned to private route edges. The complete incidence is bounded by maximum conflict degree times total private-edge count.

## CMR3173 — exact full-token payment

With sample `p=2,h=3`, every distinct private edge contributes six labelled nonroot full-token incidences.

## CMR3174 — exhaustive finite census

```text
378 coloured digraph profiles
192 mixed profiles
480 cyclic boundary arcs and canonical cycles
576 return-path incidences
96 theta-fan profiles
384 small-cut profiles
384 two-edge bottleneck incidences
288 private route-edge incidences
96 rooted conflict occurrences
480 nonrooted private-supported conflict occurrences
1,728 sample full-token incidences
```

## CMR3175 — both structural endpoints exercised

The finite regression contains genuine theta fans and genuine small return cuts; neither branch is represented only by symbolic arithmetic.

## CMR3176 — corruption rejection

Eight independently resealed mutations are rejected, including contract substitution, false theorem flags, removed endpoint coverage, removed rooted-conflict coverage, an all-`n` flag and broken record seal.

Contract digest:

```text
7089d93aa893b506e3e9d183d29869961c5e4fc59a25547d1a0c7e5607f084be
```

## CMR3177 — T02 consequence and honesty boundary

Installed kinds:

```text
mixed-cycle-boundary-fan-extraction
mixed-cycle-small-return-cut
mixed-cycle-two-edge-bottleneck
theta-fan-cycle-flip
theta-fan-private-edge-payment
theta-fan-rooted-conflict-dispatch
```

Exact flags:

```text
mixed_cycle_boundary_fan_ancestry_proved = 1
theta_fan_private_edge_payment_proved = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Rooted-star, pair-cylinder, line-clean and unavailable-edge operations remain open.
