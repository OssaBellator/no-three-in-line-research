# ERL minimizer-face cost-dominance review gate

This gate applies to any claim that a background-sensitive `D3/D4` minimizer-face scalar is preferable to an ordinary menu-state scalar.

## Exact checked facts

- [x] All 32 background-sensitive covers have two canonical menu-projectable completions.
- [x] Both completions are acyclic and belong to the existing 14-cover menu registry.
- [x] Paid and external occurrence vectors satisfy `4*S = 3*C_D3 + C_D4` componentwise.
- [x] Every class-blind additive cost is therefore weakly improved by at least one ordinary completion.
- [x] Class-blind route admissibility makes both ordinary completions feasible whenever the sensitive cover is feasible.
- [x] The completion graph has 14 vertices, 16 unordered edges, and degree distribution `10 x 2, 4 x 3`.
- [x] Twenty-four sensitive covers require five source route domains; eight require six; an ordinary menu cover requires four.
- [x] Every cover still leaves four external occurrence edges per background.

## Reject unless explicitly proved

Reject any argument that treats one of the following as a `D3/D4`-sensitive advantage:

- the formal 24/8 face census alone;
- a class-blind directed-edge cost;
- a class-blind route predicate;
- equal selected response or equal next-gap value;
- an operation-score signature without physical owner, child, payment, and route semantics;
- a sensitive cover whose ordinary completion comparison is omitted.

## Required advantage contract

A strict sensitive-cover advantage requires all of:

```text
physical_occurrence_domain_ref
restore_both_face_partition_ref
d3_domain_completeness_ref
d4_domain_completeness_ref
split_pair_route_cost_ref
split_pair_route_admissibility_ref
class_sensitive_benefit_theorem_ref
realization_status
```

It must additionally compare the proposed cover against both canonical ordinary completions on the same physical occurrence domain.

Current status:

```text
populated advantage fields                 0 of 8
accepted D3/D4-sensitive advantage theorems 0
source-admissible edge-route cells          0
physical directed edges                     0
promotion to recurrent closure              0
```

Physical occurrence coverage, legal transitions, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.
