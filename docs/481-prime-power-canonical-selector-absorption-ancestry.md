# Canonical selector, collateral geometry and protected absorption are exact operations

This chapter records **CMR3342--CMR3359** and installs CMR552--CMR576 as literal construction and scheduler ancestry.

Executable checker:

```text
scripts/check_prime_power_canonical_selector_absorption_ancestry.py
```

## CMR3342 — canonical forbidden matching

For every compatible paid pair in the side-seven grid, the residual paid-line trace is extended deterministically by the order-preserving matching of unused rows and columns.

```text
882 compatible paid pairs
1,002 paid-line trace incidences
```

## CMR3343 — exact canonical cylinder

Relabelling the canonical forbidden matching as the identity gives the exact side-five derangement cylinder of size `D_5=44`.

```text
38,808 canonical cylinder-state occurrences
194,040 paid-line avoidance checks
```

Every state avoids the complete forbidden matching and every residual paid-line cell.

## CMR3344 — time-independent profile

For all 882 selector signatures, repeated regeneration returns the identical forbidden matching and identical rank-zero/rank-one collinearity profile.

```text
882 fixed-profile repeat checks
```

## CMR3345 — static selector classification

All physical side-seven selector profiles satisfy the static collateral threshold at `q=4`.

```text
882 static physical profiles
880 rank-zero mass profiles
2 one-endpoint rank-one mass profiles
```

The separate dynamic ledger is exercised on a fixed canonical side-four allowed universe with zero static collateral.

## CMR3346 — exact line decomposition

Every physical collateral atom is assigned to its unique normalized supporting line.

```text
1,764 exact line-decomposition checks
2,646 factorial-energy checks
```

The line atom counts never exceed their binomial cell capacities.

## CMR3347 — heavy line and low-height checks

```text
1,222 heavy rank-zero lines
1,504 heavy rank-one lines
2,726 primitive-height checks
```

Every heavy line satisfies the exact bound `K <= (m-1)/(r-1)`.

## CMR3348 — line-bank endpoints

When no rank-zero line is heavy at threshold two, the checker searches the exact cell-disjoint-bank or repeated-cell-star alternative.

```text
172 rank-zero disjoint-bank endpoints
```

Rank-one nonheavy lines through one paid endpoint are checked to have pairwise disjoint residual arms.

## CMR3349 — dyadic line localization

Every physical static profile is partitioned by primitive-height dyadic band. Some band carries at least a `1/ceil(log2 m)` fraction of the selected line mass.

```text
882 dyadic localizations
```

## CMR3350 — exact dynamic selector universe

A canonical side-four derangement universe has exactly twelve allowed edges. All `2^12=4,096` availability profiles are exhausted.

```text
2,510 failed profiles
1,586 successful profiles
threshold H = 6
```

Every failed profile contains at least six unavailable allowed edges.

## CMR3351 — finite dynamic stock or recurrence

At recurrence threshold three, the exact finite bound is four failed occurrences when no allowed edge appears three times. The checker exercises both a four-occurrence finite history and a five-occurrence recurrent history.

## CMR3352 — global selector-signature stock

For sample `p=2,h=3,t=8`, the canonical selector ancestry bound is evaluated exactly as

```text
1,618,176 selector signatures
```

## CMR3353 — canonical protected extension

All partial matchings of `K_4,4` are exhausted.

```text
209 protected partial matchings
1,881 protected cylinder-state occurrences
```

Each protected matching has the canonical order-preserving perfect extension and a cylinder of size `D_4=9`.

## CMR3354 — exact edge-absorption criterion

For every protected state and every nonforbidden residual edge, absorption is possible exactly when the edge is disjoint from the protected matching.

```text
252 absorbable edge cases
2,256 blocked edge cases
```

## CMR3355 — protected contact signatures

Every blocked edge is assigned to its exact source and/or target contact with one protected edge.

```text
3,264 contact signatures
208 protected-cover checks
```

The blocked inventory obeys the exact `ceil(|B|/(2|P|))` heavy-contact bound.

## CMR3356 — finite absorption chase

Lexicographic absorption strictly enlarges the protected matching.

```text
292 successful growth steps
maximum chase depth = 4
```

For every initial partial matching the number of steps is exactly `4-|P|`.

## CMR3357 — corruption rejection

Ten independently resealed report corruptions are rejected.

## CMR3358 — contract

```text
15fdb4ac2e639dd23b89dae3ce302356ee4790a2183e7768315aed8b881e6d5e
```

## CMR3359 — exact consequence and honesty boundary

```text
canonical_selector_ledger_exact = 1
canonical_collateral_line_decomposition_exact = 1
canonical_collateral_carry_splice_exact = 1
canonical_selector_absorption_chase_exact = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The next unpaid operation is repeated protected-core contact and the reuse of fixed line/prefix/carry certificates. No all-`n` theorem is claimed.
