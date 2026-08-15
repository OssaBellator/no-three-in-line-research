# First-host minimizer-face cost dominance

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional comparison of the thirty-two background-sensitive minimizer-face scalar covers with the fourteen ordinary menu-projectable covers. No physical occurrence, face partition, route cost, route admissibility, or recurrent row is imported.

## Two canonical completions

A background-sensitive cover assigns different directions to at least one of

```text
B--D3 versus B--D4
C--D3 versus C--D4,
```

where `D3` is the 24-background restore-both face and `D4` is the 8-background restore-both face.

For every such cover `S`, form two menu-projectable completions:

```text
C_D3: copy every D3 direction onto D4
C_D4: copy every D4 direction onto D3.
```

Both completions are acyclic strict scalar covers and belong to the existing fourteen menu-cover registry.

## Exact convex identity

At the occurrence level, the restore-both classes have weights

```text
D3: 24/32 = 3/4
D4:  8/32 = 1/4.
```

For both paid and externally routed directed-edge count vectors,

```text
4 S = 3 C_D3 + C_D4.
```

This equality is componentwise over the eight directed menu edges.

Therefore, for every real additive per-occurrence cost that depends only on the directed menu edge and does not distinguish `D3` from `D4`,

```text
cost(S) = 3/4 cost(C_D3) + 1/4 cost(C_D4).
```

At least one ordinary completion is no more expensive than `S`. Thus none of the thirty-two sensitive covers can strictly improve a class-blind linear route or payment objective.

## Class-blind feasibility

The same conclusion holds for route admissibility, without assigning numerical costs.

If a sensitive cover is feasible using route predicates that depend only on the directed menu edge, then every direction used separately on `D3` and `D4` is class-blind admissible. Copying either class across the other therefore leaves an admissible ordinary completion. In fact both ordinary completions are feasible.

Hence background sensitivity adds no new cover under class-blind route feasibility.

## Completion graph

The exact completion registry is

```text
sensitive covers                         32
ordered completion maps                  32
unordered ordinary completion pairs      16
sensitive mixtures per unordered pair     2
ordinary covers                          14.
```

The sixteen completion-pair edges have ordinary-cover degree distribution

```text
degree 2: 10 covers
degree 3:  4 covers.
```

## Source-ingestion comparison

An ordinary menu cover requires four directed menu-route domains.

The sensitive covers require:

```text
one split restore-both family: 24 covers, 5 route domains
two split restore-both families: 8 covers, 6 route domains.
```

They still leave four external occurrence edges per background. The additional domains are not a reduction; they encode the class-sensitive choice.

A claimed strict advantage requires all eight fields:

```text
physical_occurrence_domain_ref
restore_both_face_partition_ref
d3_domain_completeness_ref
d4_domain_completeness_ref
split_pair_route_cost_ref
split_pair_route_admissibility_ref
class_sensitive_benefit_theorem_ref
realization_status.
```

Current populated fields: **0 of 8**. Accepted `D3/D4`-sensitive advantage theorems: **0**.

The exact score-face split alone does not prove that the physical operation, owner, child row, payment, capacity, or route cost differs between `D3` and `D4`.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_minimizer_face_cost_dominance.py \
  --check data/exact_recurrent_first_host_minimizer_face_cost_dominance.json \
  --self-test
```

The checker joins the face-scalar registry, closure-route source gate, and transition-domain source audit; reconstructs all thirty-two completion maps; validates the componentwise convex identities; and pins the completion registry by stable IDs and a digest.

Physical occurrence coverage, physical face classification, legal transitions, persistent owner identity, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.
