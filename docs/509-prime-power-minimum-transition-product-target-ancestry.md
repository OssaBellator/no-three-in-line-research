# Minimum transitions, induced products and robust target signatures have exact executable ancestry

This chapter records **CMR3750--CMR3769** and installs source theorems CMR926--CMR1005.

Canonical checker:

```text
scripts/check_prime_power_minimum_transition_product_target_ancestry.py
```

Contract:

```text
dcdd3c27f46f64757c999621de5a67ff4868a355fc0e5fab7ac0953b8cf62086
```

## CMR3750--CMR3753 — minimum-face owner transitions

Five deterministic objective banks are evaluated on every nonempty rank-three state family over a six-edge universe. Restriction and expansion minimum faces, intersection factorisation, canonical lost/added witnesses and minimum-core monotonicity are checked over 8,820 arbitrary host-transition pairs.

## CMR3754--CMR3756 — expansion rollback and lowering contraction

Every same-value expansion rolls back exactly. A lowering expansion has an added-edge transversal; avoidable added edges peel while preserving the lower minimum until one added edge becomes common and contracts. The same procedure works when the intersection host is infeasible.

Observed finite cases:

```text
639 exact same-value rollbacks
526 lowering-expansion contractions
5,350 infeasible-intersection contractions
5,538 canonical minimum-change witnesses
840 fixed-vertex execution bounds
```

## CMR3757 — complete host-transition normal form

Every same-vertex-set transition factors through its intersection. The expansion factor rolls back, contracts one added edge or yields strict improvement. Between contractions, normalized hosts form a nested decreasing restriction chain.

## CMR3758--CMR3760 — induced product potential transport

Exact product fixtures split triples into fixed-core constants, pure factor conflicts and low-rank coupling atoms. Every coupling occurrence is one Cartesian box. Conditioning and contraction transport each triple to its exact residual prescription, and coordinate fibres inherit the selected global minimum.

## CMR3761--CMR3763 — host-representable minimum-core contraction

All 247 matchable side-three hosts are regenerated. For every matching and compatible prescription of rank one or two, conditioning and endpoint deletion give exactly the residual perfect-matching family. The joint two-layer conditioned cylinders preserve opposite-layer physical exclusions, and factorwise conditioning respects exact products.

Finite census:

```text
247 representable matching hosts
2,304 one-layer conditioned cylinders
21 joint conditioned cylinders
23 induced contraction checks
19 coupling boxes
6 coordinate-fibre checks
```

## CMR3764--CMR3766 — physical minimum-target handoff

Across all 4,095 nonempty families of the twelve side-three joint states, a minimum target omitted by another minimum is removed by deleting both layer labels of one physical cell. The minimum face is restricted exactly and no surviving state contains the target.

```text
225 minimum-face physical target handoffs
4 distinct cut cells
```

## CMR3767--CMR3768 — robust surplus and absolute signatures

Every state pair satisfies the exact gained/lost triple identity. New triples have entering-edge support. A synthetic positive-gap fixture checks the strict surplus branch. Basic signatures split into at most four exact residual labelled-pair types, with one disjoint assignment partition and exact fixed-class rank-two transfer.

```text
144 state-pair energy checks
64 entering-edge/new-triple incidences
12 basic signatures
12 augmented signatures
12 residual pair assignment classes
70 surplus-bound parameter checks
```

## CMR3769 — finite consequence and honesty boundary

```text
minimum_face_owner_transition_exact = 1
minimum_expansion_rollback_exact = 1
lowering_expansion_core_contraction_exact = 1
complete_host_transition_normalization_exact = 1
induced_product_potential_transport_exact = 1
minimum_coordinate_fibre_descent_exact = 1
minimum_core_host_representability_exact = 1
minimum_face_target_handoff_exact = 1
minimum_robust_target_surplus_exact = 1
absolute_signature_pair_stabilization_exact = 1
minimum_transition_product_target_ancestry_proved = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The checker installs CMR926--CMR1005 only. It does not prove that later rank-two, star, protected-core and envelope operations are exhausted or that the global branch terminates.
