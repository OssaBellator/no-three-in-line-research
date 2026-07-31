# Complete target dispatch on asymmetric contexts

This chapter records CMR2876--CMR2887. CMR2864--CMR2875 generate arbitrary
asymmetric contexts and prove closure under restrictions and contractions. The
present chapter transfers the complete local target-response theorem to that
enlarged host class.

The executable checker is:

```text
scripts/check_prime_power_asymmetric_target_dispatch.py
```

## CMR2876 — canonical asymmetric target core

Let an asymmetric context have feasible family `F`, exact realizable triple
universe `U`, and least anchor `S`. If `S` is dirty, let

\[
T_*=\min\{T\in\mathcal U:T\subseteq S\}.
\]

The target-preserving family is generated exactly by requiring the three edges
of `T_*`:

\[
\boxed{
\mathcal F_{T_*}
=
\{R\in\mathcal F:T_*\subseteq R\}.
}
\]

No external target bank or preserving subfamily is supplied.

## CMR2877 — exact asymmetric target contraction

Inside `F_T*`, the target is a compatible forced set. Apply CMR2870. Removing
`T_*` generates a canonical asymmetric child context with:

- layer-specific surviving row and column domains;
- inherited deleted and required edges;
- exact opposite-layer blockers;
- an inverse restriction/adjoin bijection; and
- the exact transported triple universe.

Thus target preservation is an exact contraction action on every asymmetric
context.

## CMR2878 — exhaustive asymmetric candidate trichotomy

For each alternative candidate `Q != S`, exactly one of the following holds:

1. `T_*` is preserved;
2. `T_*` is destroyed and `Phi(Q) < Phi(S)`; or
3. `T_*` is destroyed and `Phi(Q) >= Phi(S)`.

The conditions are pairwise disjoint and exhaustive.

## CMR2879 — strict-improvement action

In case 2, retain `Q` as an exact strict potential improvement. No branching or
contraction is needed to certify the local decrease.

The checker records the exact anchor and candidate triple counts and the negative
potential delta.

## CMR2880 — new triple under nonimproving destruction

In case 3, at least one labelled collinear triple occurs in `Q` but not in `S`:

\[
\boxed{
\mathcal T(Q)\setminus\mathcal T(S)\ne\varnothing.
}
\]

### Proof

Destroying `T_*` loses at least one anchor triple. If no genuinely new triple
appeared, the candidate triple count would be strictly smaller than the anchor
count, contradicting the nonimproving hypothesis. This is the exact finite-set
form of CMR698 and CMR866. ∎

## CMR2881 — canonical asymmetric new-triple witness

Order the exact triple universe canonically and choose the least member of

\[
\mathcal T(Q)\setminus\mathcal T(S).
\]

Call it `C_Q=(f0,f1,f2)`. It is a compatible labelled prescription because it is
contained in `Q`.

## CMR2882 — generated asymmetric first-missing children

For `i=0,1,2`, require the prefix `f0,...,f_{i-1}` and delete `f_i`. For branch
three, require the full triple `C_Q`.

Every child is generated from the same asymmetric layer domains by a literal
deleted/required extension. If the omitted edge was already required, that
branch is the exact required/deleted contradiction terminal.

For `i<3`, the generated family is exactly

\[
\{R\in\mathcal F:
 f_0,\ldots,f_{i-1}\in R,\ f_i\notin R\}.
\]

The branch-three family is exactly

\[
\{R\in\mathcal F:C_Q\subseteq R\}.
\]

## CMR2883 — disjoint partition and conditioned contraction

The four generated first-missing branches are pairwise disjoint and their union
is the full parent family. The rejected candidate occurs only in branch three.

Branch three contracts `C_Q` through CMR2870 to another canonical asymmetric
context. Every child triple universe is contained in the parent universe before
contraction, and the contracted universe is the exact disjoint restriction.

## CMR2884 — complete local asymmetric response

Every dirty asymmetric anchor and every alternative candidate receive exactly
one canonical action:

```text
target preserved
  -> exact asymmetric forced-triple contraction

target destroyed with lower potential
  -> strict improvement

target destroyed without lower potential
  -> least new triple
  -> disjoint first-missing asymmetric contexts
  -> exact conditioned contraction in branch 3
```

Therefore

```text
local_asymmetric_candidate_response_complete = 1
```

relative to the supplied asymmetric context.

## CMR2885 — exhaustive side-three domain census

The checker exhausts all 400 asymmetric domain hosts on ambient side three:

```text
44 dirty anchor dispatches
148 classified alternative candidates
1 target-preserving candidate
108 strict-improvement candidates
39 nonimproving new-triple candidates
39 first-missing response scenarios
156 branch records
111 nonempty branch records
```

Every candidate receives exactly one action and every nonimproving response is a
disjoint exhaustive generated partition.

## CMR2886 — side-four census and corruption rejection

On the complete side-four context, the checker records:

```text
216 feasible states
215 alternative candidates
8 target-preserving candidates
172 strict-improvement candidates
35 nonimproving new-triple candidates
35 first-missing response scenarios
140 branch records
140 nonempty branch records
```

Ten malformed inputs or corrupted manifests are rejected. The contract digest
is:

```text
5e982b03f24ce4cd1230ede70563b49e3ac67976b0a84e038ae27b463e39fa83
```

The finite censuses are regression evidence. CMR2876--CMR2884 are exact finite
set-family and triple-counting statements.

## CMR2887 — T02 consequence and honesty boundary

The complete local response rule now applies uniformly before and after forced
contractions. Square contexts enter the asymmetric class after one conditioned
triple, and every later asymmetric context has canonical:

- feasible-family generation;
- triple-universe generation;
- least-anchor and least-target selection;
- target-preserving contraction;
- strict-improvement retention;
- new-triple witness selection;
- first-missing child generation; and
- conditioned contraction.

The checker records:

```text
asymmetric_target_preserving_contraction_exact = 1
asymmetric_strict_improvement_action_exact = 1
asymmetric_nonimproving_new_triple_response_exact = 1
asymmetric_first_missing_contexts_generated = 1
asymmetric_first_missing_partition_exact = 1
asymmetric_conditioned_contraction_exact = 1
local_asymmetric_candidate_response_complete = 1
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The remaining T02 problem is now genuinely global: prove that every owner,
routing, factor and closure-envelope transition of the actual construction is
represented by the square/asymmetric context model; prove the global trigger
bank exhaustive; and prove every resulting branch terminates or reaches a
successful descent. Genuine T03/T04 population, arbitrary-`n` semantic coverage,
all exceptional chambers and the all-`n` implication remain open.
