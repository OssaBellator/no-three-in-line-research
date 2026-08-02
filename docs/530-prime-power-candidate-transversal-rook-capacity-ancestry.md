# Candidate-transversal, rook-owner and capacity ancestry is executable through CMR1453

This chapter records **CMR4086--CMR4101** and binds source **CMR1390--CMR1453**.

Canonical checker:

```text
scripts/check_prime_power_candidate_transversal_rook_capacity_ancestry.py
```

Contract:

```text
a590a41fb713c91904106d20d5eb31e18171a0761ce35a3908a29c8b87d547db
```

## CMR4086--CMR4089 — exact candidate transversals and Hall walls

Every response determines an equal-weight deletion transversal which preserves that response. Conversely, every surviving transversal bounds collateral by the exempt candidate weight. Thus minimum weighted collateral equals minimum surviving-transversal exemption weight.

A full surviving transversal gives a clean response and a subthreshold surviving transversal gives a strict response. A failed selector contains an inclusion-minimal perfect-matching blocker and therefore routes to the already installed deficiency-one unit-wall child descent.

The side-four equal-share obstruction remains explicit: equal fractional ownership does not prove strictness even when a clean response exists. The side-five clean response supplies an exact thirteen-edge surviving transversal.

## CMR4090--CMR4093 — fixed rook owners and matching preclusion

Every possible new triple has one least entering owner edge fixed before response sampling. Exact rook classes compute unconditional owner loads and one positive marginal division gives conditional owner weights.

In the extension-free target graph, the matching-preclusion number is exactly `n-2`; the only minimum blockers are the target row star and target column star. Canonical owner support is itself a candidate transversal. Small or nonexceptional owner support therefore guarantees a surviving response, while a positive minimum forces either a large owner tail, an exceptional star or a large fractional candidate packing.

## CMR4094--CMR4097 — exact rook probabilities and shared assignment

Residual forbidden boards have exact rook numbers and exact inclusion-exclusion completion counts. Rank-one through rank-three prescription probabilities and unavailable-edge marginals are exact rational values.

Every new credit is assigned once to its entering owner. Owner occurrence probabilities form a doubly stochastic matrix, so expected cross-line collateral is one bipartite assignment cost. Rational row-column potentials below destroyed load give a strict response; denominator clearing produces an independently checkable strict integer certificate.

The source ranges CMR1398--1405 and CMR1430--1437 describe one finalized rook-owner operation family. They are co-bound and are not double-counted in the registry.

## CMR4098--CMR4100 — harmonic and lattice-capacity owner envelopes

Primitive-height line populations are controlled by the inherited coordinate span, not merely the matching side. Conditional harmonic partner energy gives an owner envelope coupled by the same assignment dual.

The lattice-capacity coefficient

```text
max(floor(W_omega / h) - 1, 0)
```

is termwise no larger than the harmonic coefficient and vanishes for heights above half the inherited span. Exact dyadic capacity coefficients therefore give honest owner upper quotients for scattered residual factors.

## CMR4101 — executable consequence and honesty boundary

```text
candidate_transversal_rook_capacity_ancestry_proved = 1
candidate_transversal_identity_exact = 1
minimum_owner_blockers_classified = 1
rook_owner_rows_exact = 1
owner_support_tail_policy_exact = 1
extension_free_rook_probabilities_exact = 1
cross_line_assignment_dual_exact = 1
harmonic_owner_envelope_exact = 1
lattice_capacity_owner_envelope_exact = 1

uniform_cross_line_owner_policy_proved = 0
same_owner_diagonal_blocks_subcritical = 0
independent_line_kernel_sufficient = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The checker source and contract were validated locally. The complete seven-verifier consolidated execution has not been observed in the current environment, so no full execution or CI success is claimed.
