# Inherited-coordinate diagonal blocks have executable owner, quotient and cross-line ancestry

This chapter records **CMR4038--CMR4053** and binds source **CMR1318--CMR1389**.

Canonical checker:

```text
scripts/check_prime_power_inherited_coordinate_diagonal_block_ancestry.py
```

Contract:

```text
bff27495eef9188b3d90e5f36ee66ed889b0606c7fa92f8b3391a3114e03d826
```

## CMR4038--CMR4041 — structural owners and upper triangularity

Every live physical credit has one persistent last-entering structural owner. One-coordinate product moves create credits only at the active factor, restrictions and contractions do not relabel surviving credits, and strict child, wall, normalized-host and envelope exits form a finite forward owner DAG.

The global reproduction matrix is therefore block upper triangular after topological ordering. Same-owner response dynamics remain inside diagonal blocks; strict structural exits contribute only to later blocks. Rational diagonal certificates glue by backward scaling.

## CMR4042--CMR4045 — exact credit classes and honest upper quotients

Complete state-target pairs give finite exact credit classes and exact rational same-owner offspring rows. Arbitrary geometric class maps define exact coarse fibre sums. Componentwise worst-fibre rows give an honest upper quotient, and one strict coarse certificate lifts to every exact row and every dominated host.

Once a weight vector is fixed, deterministic row selection suffices. Rational rows and weights clear to strict integer inequalities.

## CMR4046--CMR4049 — line profiles, pair moments and extension-free cylinders

Collateral candidates admit exact nonaxis line profiles, dyadic rank/profile classes and exact pair-moment tail envelopes. The extension-free response bank has explicit permanent and derangement denominators, sharp rank-one marginals and exact higher-rank cylinder counts.

Exact row-column incidence types compute both created-credit and destroyed-credit expectations. These are exact rational rows, not merely universal factor-four upper bounds.

## CMR4050--CMR4052 — cross-line assignment

Candidate triples can be assigned to one residual response edge. For any selector, true collateral is dominated by an edge-weighted perfect-matching cost. Joint selector/matching optimization is exact, and the equivalent fractional form pays each candidate through its least-loaded residual edge.

A fractional profile below the guaranteed old-credit loss yields a deterministic strict response. If the response host has no perfect matching, the branch continues through the exact deficiency-one unit-wall descent.

## CMR4053 — preserved obstruction and honesty boundary

The realizable side-five line-composition example remains an explicit obstruction to independent linewise domination, while a deterministic cross-line response has zero new collateral and destroys both old targets.

```text
inherited_coordinate_diagonal_block_ancestry_proved = 1
owner_dag_upper_triangular = 1
upper_quotient_lifting_exact = 1
line_profile_pair_moment_envelopes_exact = 1
extension_free_permanent_and_marginals_exact = 1
exact_cylinder_rows_available = 1
cross_line_assignment_normal_form_exact = 1

same_owner_diagonal_blocks_subcritical = 0
independent_line_kernel_sufficient = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The checker source and contract were validated locally. The complete nine-verifier consolidated execution has not been observed in the current environment, so no full execution or CI success is claimed.
