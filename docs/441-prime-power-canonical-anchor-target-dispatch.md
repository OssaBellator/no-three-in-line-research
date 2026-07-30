# Canonical anchor-target dispatch

This chapter records CMR2818--CMR2827. It removes the last externally supplied
choice from the complete local T02 response rule. Given a supplied feasible
family, anchor and exact triple universe, the anchor itself canonically decides
whether the execution is terminal or which singleton target bank to use.

The executable checker is:

```text
scripts/check_prime_power_canonical_target_dispatch.py
```

## CMR2818 — exact anchor triple set

Let \(\mathcal F\) be a nonempty equal-cardinality family of finite labelled
states, let \(S\in\mathcal F\), and let \(\mathcal U\) be the supplied exact
triple universe. Define

\[
\mathcal T_{\mathcal U}(S)
=
\{T\in\mathcal U:T\subseteq S\}.
\]

This set is determined entirely by the supplied anchor and triple universe. No
user-supplied target list is used.

## CMR2819 — clean-anchor terminal

If

\[
\mathcal T_{\mathcal U}(S)=\varnothing,
\]

then \(S\) has no triple from the exact universe and is a clean terminal for the
local triple-potential problem.

The checker records:

```text
clean-anchor-terminal
```

and emits no candidate-response records, because no repair target is required.
This is a terminal statement only relative to the supplied exact triple
universe; proving that universe geometrically complete is still T05 work.

## CMR2820 — canonical dirty-anchor target

If \(\mathcal T_{\mathcal U}(S)\ne\varnothing\), order the exact triple universe
canonically and define

\[
T_*(S)=\min \mathcal T_{\mathcal U}(S).
\]

Then

\[
\mathcal Q_*(S)=\{T_*(S)\}
\]

is a canonical nonempty target bank. Thus a dirty anchor never needs an external
target-bank choice.

## CMR2821 — exact singleton-target contraction

A state preserves the canonical target precisely when it contains all three
cells of \(T_*(S)\). The preserving family is therefore

\[
\mathcal F_{T_*}
=
\{R\in\mathcal F:T_*(S)\subseteq R\}.
\]

Restriction gives the exact bijection

\[
\boxed{
\mathcal F_{T_*}
\cong
\{T_*(S)\}\times(\mathcal F_{T_*}/T_*(S)).
}
\]

Every residual state has cardinality three less than its original state. The
checker verifies injectivity of this contraction.

## CMR2822 — canonical anchor dispatch

Every supplied anchor now has exactly one dispatch mode:

```text
anchor has no exact triples
  -> clean terminal

anchor has at least one exact triple
  -> choose the least anchor triple T_*
  -> apply the complete local response rule to {T_*}
```

Hence

```text
canonical_target_bank_external_choice_required = 0
local_anchor_dispatch_complete = 1
```

relative to the supplied family, anchor and exact triple universe.

## CMR2823 — exact dirty-anchor candidate response

For every alternative \(R\ne S\) under a dirty anchor, exactly one of the
following occurs:

1. **Canonical target preserved.**  Then \(T_*(S)\subseteq R\), and \(R\) lies
   in the exact singleton-target contraction branch.
2. **Canonical target destroyed with lower potential.**  Then
   \(\Phi(R)<\Phi(S)\), giving a strict improvement.
3. **Canonical target destroyed without lower potential.**  The CMR698 identity
   forces at least one genuinely new triple in \(R\). Choose the least new
   triple and apply the duplicate-free first-missing partition.

These predicates are pairwise disjoint and exhaustive.

## CMR2824 — duplicate-free nonimproving branch

For the canonical new triple \(C_R=(f_0,f_1,f_2)\), the exact response is:

```text
0: omit f0
1: contain f0 and omit f1
2: contain f0,f1 and omit f2
3: contain f0,f1,f2 and contract the forced triple
```

Every feasible state occurs in exactly one branch. The rejected candidate occurs
only in branch 3, whose residual states have cardinality three less.

## CMR2825 — exhaustive hypergraph census

The checker exhausts every triple hypergraph on a five-cell universe and every
four-cell anchor in the complete five-state family:

```text
5,120 hypergraph/anchor scenarios
320 clean-anchor terminals
4,800 dirty-anchor canonical targets
19,200 classified dirty-anchor alternatives
4,800 target-preserving alternatives
5,880 strict improvements
8,520 nonimproving new-triple alternatives
```

Every dirty-anchor alternative receives exactly one action.

## CMR2826 — subfamily and corruption regression

The checker also exhausts every subfamily of the five four-cell states containing
its anchor against every triple hypergraph:

```text
81,920 subfamily scenarios
5,120 clean-anchor scenarios
76,800 dirty-anchor scenarios
12 rejected corruptions
```

The corruptions include missing anchors, duplicate or unequal-cardinality family
states, duplicate triples, an incorrect canonical target, a false clean dispatch,
a corrupted category or new-triple witness, missing candidate data, a damaged
contraction, an honesty flip and a bad seal.

The contract digest is:

```text
634318242ece5cab549b9394ba33e116d7c1b01b4c74d5a02e276004fe1e8444
```

The exhaustive finite censuses are regression evidence. CMR2818--CMR2824 are
exact finite set-family and triple-counting statements.

## CMR2827 — T02 consequence and honesty boundary

The local T02 rule no longer requires a separately supplied target bank. Once a
feasible family, anchor and exact triple universe are supplied, the checker has a
complete deterministic local dispatch:

```text
clean anchor -> terminal

dirty anchor -> least singleton target
             -> preservation contraction,
                strict improvement,
                or canonical new-triple partition
```

It still does not supply or prove:

- global generation of every feasible parent family;
- geometric completeness of the supplied triple universe;
- correctness of the anchor chosen by the construction;
- complete coverage of closure-envelope and parent-state types;
- every finite parameter domain and exclusion;
- genuine expected hosts or T03/T04 populations;
- termination of repeated local dispatches; or
- the all-`n` implication.

The checker permanently records:

```text
canonical_target_bank_external_choice_required = 0
local_anchor_dispatch_complete = 1
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The no-three-in-line conjecture remains open.
