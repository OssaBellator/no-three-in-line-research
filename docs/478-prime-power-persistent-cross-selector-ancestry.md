# Persistent crosses, refined trace ancestry and fixed selector obstructions are exact

This chapter records **CMR3300--CMR3317** and installs CMR522--CMR551 as literal construction and scheduler ancestry.

Executable checker:

```text
scripts/check_prime_power_persistent_cross_selector_ancestry.py
```

## CMR3300 — maximum-allowed blocker criterion

For every side-three bipartite graph and every edge `e=uv`, the checker regenerates the maximum matching number and verifies

```text
e belongs to a maximum matching
iff
1 + nu(J-u-v) = nu(J).
```

## CMR3301 — exact two-endpoint deficiency

When the persistent edge is not maximum-allowed, the residual matching number is exactly two smaller. Every maximum matching saturates both endpoints with two distinct partner edges and omits the blocker.

The exhaustive census contains:

```text
511 nonempty side-three graphs
2,304 graph-edge cases
1,863 maximum-allowed cases
441 two-endpoint deficiency cases
1,152 deficiency partner incidences
```

## CMR3302 — persistent-aware trichotomy

The checker binds the literal CMR524 branches:

```text
paid-line trace contact
maximum-aware blocker absorption
two-endpoint absorption deficiency
```

The deficiency branch supplies a compatible row-arm/column-arm paid pair.

## CMR3303 — injective persistent-cross pair lines

For every side-five central cell and every partner type `(x,y)`, the row-arm and column-arm edges form a compatible pair. Distinct types determine distinct normalized real lines.

```text
25 central cells
400 cross-pair types
400 injective pair-line signatures
```

## CMR3304 — exact disjoint pair cylinders

Each partner type receives the universal residual side-three derangement cylinder of size `D_3=2`. Cylinders for distinct types are pairwise disjoint because a perfect matching determines its unique row-arm and column-arm choices.

```text
800 cylinder-state occurrences
3,000 pairwise disjoint-cylinder checks
```

## CMR3305 — partner support graph endpoint

All 511 nonempty support graphs on a `3 x 3` partner-type universe are exhausted at threshold two.

```text
478 two-arm bank profiles
33 one-arm line-star profiles
2,304 support-edge incidences
```

The first branch contains two partner types with distinct row and column arms. In the second branch all support is concentrated on one arm, attaining the exact König bound.

## CMR3306 — paid-pair selector surcharge

A fixed persistent-cross paid pair contributes a deterministic restoration surcharge in `{0,1,2}`. The CMR531 weighted selector remains valid with the surcharge included explicitly.

## CMR3307 — three-edge joint absence ledger

All five-time availability histories of one persistent blocker and its two partner edges are exhausted, together with every nonempty selected joint-absence subset.

```text
32,768 three-edge availability histories
26,281 selected joint-absence subsets
420 reintroduction endpoints
261 joint-persistent endpoints
```

The number of selected joint runs never exceeds one plus the total edge-reintroduction count.

## CMR3308 — canonical envelope-epoch clock

For sample root `t=2^3=8`, the exact nested epoch sides

```text
8, 4, 2, 1
```

exercise all four possible envelope epochs. Strict envelope change is registered separately from same-owner signature repetition.

## CMR3309 — exact pair and trace signature stocks

For that epoch chain, the checker evaluates the literal stocks

```text
pair signatures = 3,284
trace signatures = 1,000
```

and verifies their global CMR536 bounds.

## CMR3310 — refined rooted-trace stock

The exact sum of the theorem-level refined-signature bounds over the sample chain is

```text
406,048
```

with finite multiplicity bound `1,218,144` at recurrence threshold four.

## CMR3311 — fixed refined-trace selector

A refined rooted-trace record fixes the envelope epoch, rooted centre, paid partner, compatible pair, paid line, persistent blocker, trace cell and arm. Repetition therefore dispatches to one fixed weighted line-clean selector without declaring the trace cell unavailable.

## CMR3312 — failed-selector polarization

For residual side five and `q=4`, all integer triples `(V0,V1,|B|)` satisfying the exact failed-selector inequality are exhausted.

```text
33,207 failed integer profiles
28,161 unavailable-inventory profiles
5,046 collateral profiles
```

Every failure has either `S >= 11/120` or `|B| >= 4`.

## CMR3313 — collateral rank split

Every collateral profile has the CMR548 rank-zero or rank-one mass threshold.

```text
4,831 rank-zero profiles
215 rank-one profiles
```

## CMR3314 — exact obstruction atom stocks

For residual side five, the complete compatible-prescription stocks are

```text
rank-zero atoms = 600
rank-one atoms = 400
```

and the finite-history inequalities are regenerated from those exact universes.

## CMR3315 — paid-line separation of rank-one recurrence

All 882 compatible paid pairs in the side-seven grid are checked against every compatible rank-one collinear residual prescription avoiding the paid line.

```text
13,992 separated rank-one line atoms
```

Every recurrent rank-one atom lies on a fixed second line distinct from the paid line.

## CMR3316 — corruption rejection and contract

Eleven independently resealed report corruptions are rejected.

Contract:

```text
35bfc31201b5fffb46b37e9c36ffd4c1e9e01c6d1ccdb2b592818b9dc8bdcc80
```

## CMR3317 — exact consequence and honesty boundary

The checker reports:

```text
persistent_blocker_absorption_deficiency_ancestry_proved = 1
persistent_cross_pair_bank_ancestry_proved = 1
cross_signature_ancestry_exact = 1
refined_trace_fixed_selector_exact = 1
fixed_selector_obstruction_stock_exact = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The remaining recurrent endpoints are the fixed rank-zero target atom, the fixed paid-endpoint rank-one secant, and later selector/protected-core operations. No all-`n` theorem is claimed.
