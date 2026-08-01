# Heavy-line, secant-star and protected-interface histories have exact execution ancestry

This chapter records **CMR3470--CMR3489** and installs CMR605--CMR628.

Executable checker:

```text
scripts/check_prime_power_protected_interface_execution_ancestry.py
```

## CMR3470--3474 — heavy-line execution

For every side-five protected matching and nonaxis line, the checker regenerates the protected-touching and free line cells. It verifies:

```text
protected-touching cells <= 2k
free cells >= max(0,r-2k)
P union free cells is a partial matching
```

All free cells enter one canonical protected extension. Post-absorption rank-zero and rank-one line atoms obey the exact `binom(2k,3)` and `binom(2k,2)` caps. The monotone growth budget is checked at every protected size and threshold.

## CMR3475--3479 — secant-star execution

Physical side-five star arms are grouped by their matching-vertex degrees. Each star reaches either a matching-vertex wall or a matching-compatible arm family. For every protected matching, at most `2k` extracted arms touch the protected vertices. The remaining outside pairs form one compatible partial matching and are absorbed in one batch, with two protected edges per free arm.

## CMR3480--3484 — protected/free interface factorization

Every side-five derangement and every protected index subset are exhaustively classified by their cross skeleton. The checker verifies:

```text
I-to-J flow = J-to-I flow
interface size = 2c <= 2u
exact product = {skeleton} x PM(H_I) x PM(H_J)
```

The exact skeleton formula and coarse `(u+1)n^(4u)` bound are checked for all 32 protected subsets.

## CMR3485--3487 — protected-skeleton history

Skeleton classes are regenerated for every nontrivial protected size. A repeated skeleton satisfies the exact protected/free factor-diversity bounds. Consecutive distinct protected-factor restrictions have at least two entering and two leaving edges. Skeleton-changing transitions have even symmetric difference at least two and exact physical cross-edge churn.

## CMR3488 — finite census and corruption rejection

```text
34,012 protected-line profiles
15,466 free line-cell incidences
41,742 star bulk-absorption profiles
1,022 exact product-factorization checks
1,408 protected-interface state incidences
118 protected-skeleton history classes
158 skeleton-changing transitions
458 physical cross-edge churn incidences
29 protected-factor paid transitions
6 rejected corruptions
```

Contract:

```text
59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f
```

## CMR3489 — T02 consequence and honesty boundary

```text
heavy_line_protected_absorption_proved = 1
secant_star_protected_absorption_proved = 1
protected_core_interface_factorization_exact = 1
protected_skeleton_history_exact = 1
protected_interface_execution_ancestry_proved = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Product-conflict and essential-prescription operations beginning at CMR629 remain to be installed. No all-`n` theorem is claimed.
