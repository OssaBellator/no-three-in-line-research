# Sparse rollback is an exact restoration-or-contraction construction bank

This chapter records CMR3048--CMR3059. It installs the literal CMR439--CMR447 rollback operation relative to a deletion-pass ancestor.

The executable checker is:

```text
scripts/check_prime_power_sparse_rollback_restoration_ancestry.py
```

## CMR3048 — exact deletion-pass endpoint

The final matchable host `G` is represented by its literal edge set inside the complete ancestor host. Deleted ancestor edges form the exact restoration universe `Delta`.

## CMR3049 — minimum rollback restoration

For every essential final edge `e`, the checker searches rollback subsets in increasing size and lexicographic order. The first set `R` satisfying

\[
\operatorname{PM}(G+R-e)\ne\varnothing
\]

is the canonical minimum rollback. It verifies

\[
1\le |R|\le t.
\]

## CMR3050 — restored edges form a forced matching core

Every edge of a minimum rollback set is checked to belong to every perfect matching of `G+R-e`. The restored set is therefore a matching and a literal forced core.

## CMR3051 — exact residual factorization

Removing the endpoints of `R` produces a residual host whose matching family satisfies

\[
\operatorname{PM}(G+R-e)
=
\{R\}\times\operatorname{PM}((G+R-e)-V(R)).
\]

The residual side is exactly `t-|R|`.

## CMR3052 — cheap restoration or strict contraction

At threshold `q=2`, every exhaustive side-three case is classified as either:

```text
|R| = 1  -> cheap rollback restoration
|R| >= 2 -> forced-core contraction by at least two rows and columns
```

The same code accepts arbitrary thresholds.

## CMR3053 — forced-certificate escape

Every forced compatible collinear certificate containing the selected essential edge is absent from every rollback avoiding matching.

## CMR3054 — finite rollback incidence or concentration

For one minimum rollback footprint per final essential edge, total incidence is checked against `t^2`. The finite regression also verifies the CMR443 alternative: either one deleted edge occurs in two rollback footprints or a greedy disjoint subfamily meets the required packing bound.

## CMR3055 — exact full-token restoration incidence

Every restored edge contributes exactly `(p+1)(h-1)` labelled nonroot incidences. The side-three census is evaluated with the sample multiplier for `p=2,h=3`, giving six labelled incidences per restored edge.

## CMR3056 — restored-edge support for recreated conflicts

Every compatible collinear triple present after restoration but absent before restoration is checked to contain at least one restored edge. The recreated conflict count is bounded by rollback size times the exact restored-edge conflict degree.

## CMR3057 — exhaustive side-three regression

The checker records:

```text
247 matchable final hosts
513 final essential-edge pairs
450 minimum rollbacks of size one
63 minimum rollbacks of size two
576 restored-edge incidences
3,456 sample full-token incidences
192 recreated conflicts with restored support
150 forced certificates escaped
150 concentration hosts
63 disjoint-packing hosts
```

The size-two cases are genuine strict forced-core contractions, not synthetic arithmetic examples.

## CMR3058 — corruption rejection

Eight independent mutations are rejected, including a false essential edge, empty rollback, corrupted restored host, missing avoiding family, false residual vertices, unsupported recreated conflict, corrupted owner and broken seal.

The contract digest is:

```text
35fc36f758016a3de0dba687950e4d6f0d1b17caece487ef21af3e9967f32267
```

## CMR3059 — T02 consequence and honesty boundary

The installed rollback operations are:

```text
minimum-rollback-restoration
cheap-rollback-certificate-escape
rollback-forced-core-contraction
rollback-recreated-conflict-support
```

The checker reports:

```text
sparse_rollback_restoration_ancestry_proved = 1
minimum_rollback_forced_core_exact = 1
rollback_token_incidence_exact = 1
rollback_recreated_conflict_support_exact = 1
all_owner_operations_proved = 0
all_scheduler_operations_proved = 0
all_restoration_operations_proved = 0
all_returned_edge_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The zero restoration flag is intentional: later rollback optimal-face, line-clean, unavailable-edge and ancestor-reset operations remain to be audited. No all-`n` theorem is claimed.
