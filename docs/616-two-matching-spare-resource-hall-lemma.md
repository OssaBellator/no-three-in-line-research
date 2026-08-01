# Two-matching spare-resource Hall lemma

The five-resource fixture of `docs/604` leaves a residual `K_3,3`.  One
matching-shaped partner fibre is harmless there, but a second source-exclusion
family can destroy robustness.  This chapter adds one further spare resource on
each side and audits the exact `K_4,4` residual problem.

## 1. Partial-matching catalogue

### Theorem PP3cvo — PROVED / TWO MATCHING-SHAPED FORBIDDEN FAMILIES

A `4 x 4` bipartite host has 209 partial matchings.  There are 43,681 ordered
pairs `(F,S)` of partial matchings, representing a restricted partner fibre and a
restricted source-exclusion family.  Their unions give 7,343 distinct forbidden
edge sets.

#### Proof

Enumerate every edge subset with distinct left and right endpoints, then every
ordered pair and union. ∎

## 2. Robust completion

### Theorem PP3cvp — PROVED / ONE-EXCLUSION ROBUSTNESS

For every union `F union S` in the preceding catalogue, `K_4,4-(F union S)` has
at least two perfect matchings.  After deletion of any one further allowed cell,
at least one perfect matching remains.

#### Proof

The checker enumerates all twenty-four perfect matchings.  Across the 7,343
unions, the pre-exclusion matching count ranges from two to twenty-four.  It then
deletes every remaining edge in turn and verifies a surviving matching. ∎

## 3. Quantitative source condition

### Theorem PP3cvq — PROVED UNDER AN EXPLICIT HOST CONDITION

A conditional Hall choice is safe against one additional residual-cell exclusion
whenever, after selecting its two local resources:

1. four unused resources remain on each side;
2. the restricted partner fibre is a partial matching;
3. the restricted source-exclusion family is a partial matching.

#### Proof

Under these hypotheses the residual graph is exactly a graph covered by
`PP3cvp`. ∎

## Remaining source obligation

The asymptotic PP3 host has not been proved to provide six total resources for
each local choice while simultaneously making both real forbidden families
matching-shaped.  The theorem is a sharp finite completion interface, not an
asymptotic Hall conversion.
