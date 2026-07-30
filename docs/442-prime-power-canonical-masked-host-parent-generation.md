# Canonical masked-host parent generation

This chapter records CMR2828--CMR2839. It removes the remaining locally supplied
family, triple universe and anchor from the T02 dispatcher. The input is now only
a side length and a monotone labelled-edge deletion mask.

The executable checker is:

```text
scripts/check_prime_power_masked_host_parent_generation.py
```

## CMR2828 — labelled two-layer host

For side \(n\), let

\[
H_n=\{0,1\}\times[n]\times[n].
\]

An edge \((\lambda,r,c)\) records layer, row and column. A saturated labelled
state contains exactly one edge in every row and column of each layer, and the
two layers may not occupy the same physical cell \((r,c)\).

Equivalently, a state is determined by two permutations
\(\sigma_0,\sigma_1\in S_n\) satisfying

\[
\sigma_0(r)\ne\sigma_1(r)\qquad\text{for every }r.
\]

The corresponding state is

\[
S(\sigma_0,\sigma_1)
=
\{(0,r,\sigma_0(r)),(1,r,\sigma_1(r)):r\in[n]\}.
\]

## CMR2829 — exact permutation-state bijection

The map above is a bijection between:

1. ordered pairs of permutations with pointwise-distinct values; and
2. saturated, layer-disjoint labelled two-layer states.

### Proof

Every permutation pair produces one edge in every row and column of each layer.
Pointwise distinctness is exactly physical-cell disjointness. Conversely, the
unique column selected in row \(r\) of each layer reconstructs the two
permutations. ∎

## CMR2830 — exact masked feasible family

Let \(D\subseteq H_n\) be a monotone deleted-edge mask. Define

\[
\mathcal F(n,D)
=
\{S(\sigma_0,\sigma_1):D\cap S(\sigma_0,\sigma_1)=\varnothing\}.
\]

This is the exact family of saturated labelled two-layer states admitted by the
host and mask. The generator is duplicate-free because the permutation-state
map is injective.

Thus, relative to \((n,D)\), the feasible family is reconstructed rather than
supplied.

## CMR2831 — infeasible-mask terminal

If

\[
\mathcal F(n,D)=\varnothing,
\]

then the mask has no saturated completion. The local branch is an exact
infeasible terminal and emits no anchor or candidate records.

This is a dead recurrence branch, not a no-three-in-line solution.

## CMR2832 — exact realizable triple universe

For every generated state, inspect all three-edge subsets. A labelled triple is
admitted exactly when:

1. its three physical cells are distinct;
2. their determinant is zero; and
3. it occurs in at least one state of \(\mathcal F(n,D)\).

Let the resulting union be \(\mathcal U(n,D)\). Then

\[
\boxed{
\mathcal U(n,D)
=
\bigcup_{S\in\mathcal F(n,D)}
\{T\subseteq S:|T|=3,\ T\text{ is physically collinear}\}.
}
\]

Hence every listed triple is realizable, and every realizable collinear triple
is listed. No externally supplied triple universe is used.

## CMR2833 — exact single-edge mask extension

For \(f\notin D\),

\[
\boxed{
\mathcal F(n,D\cup\{f\})
=
\{S\in\mathcal F(n,D):f\notin S\}.
}
\]

### Proof

Both sides are exactly the saturated states avoiding every edge in \(D\) and
also avoiding \(f\). ∎

This identifies the generated child family with the CMR830 single-edge
restriction \(\mathcal F-f\), so the abstract completeness branch is realized
by literal mask extension.

## CMR2834 — monotonicity of realizable triples

The mask-extension identity implies

\[
\boxed{
\mathcal U(n,D\cup\{f\})
\subseteq
\mathcal U(n,D).
}
\]

### Proof

Every child state is a parent state. Every triple realizable in a child state is
therefore realizable in a parent state. ∎

Deletion cannot create a previously unrealizable labelled triple universe,
although the selected anchor and its potential may change.

## CMR2835 — canonical feasible anchor

When \(\mathcal F(n,D)\ne\varnothing\), order labelled states
lexicographically and choose

\[
S_*(n,D)=\min\mathcal F(n,D).
\]

The anchor is now generated deterministically from the host and mask. No
external anchor choice remains in the local masked-host rule.

## CMR2836 — exhaustive mask dispatch

Exactly one of the following occurs:

```text
F(n,D) is empty
  -> infeasible-mask terminal

F(n,D) is nonempty and S_* has no triple in U(n,D)
  -> clean-anchor terminal

F(n,D) is nonempty and S_* has a triple in U(n,D)
  -> dirty-anchor canonical target dispatch
```

The three conditions are mutually exclusive and exhaustive.

For a dirty anchor, choose its least realizable triple and apply
CMR2818--CMR2827. Every alternative then receives exactly one of:

```text
canonical target preserved
  -> singleton-target contraction

canonical target destroyed with lower potential
  -> strict improvement

canonical target destroyed without lower potential
  -> least new triple and duplicate-free first-missing partition
```

## CMR2837 — local masked-parent rule

Relative to only a side length and deletion mask, the checker reconstructs:

- the complete feasible family;
- the exact realizable collinear-triple universe;
- the canonical anchor;
- the empty/clean/dirty dispatch;
- the canonical dirty-anchor target;
- every candidate action; and
- every new-triple child partition.

It records:

```text
masked_host_family_generated = 1
family_generation_duplicate_free = 1
triple_universe_generated_from_family = 1
single_edge_mask_extension_exact = 1
child_triple_universe_monotone = 1
canonical_target_bank_external_choice_required = 0
local_masked_parent_dispatch_complete = 1
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## CMR2838 — exhaustive finite regression

The checker exhausts every deletion mask on the complete side-two labelled host:

```text
256 masks
31 feasible masks
225 infeasible masks
31 clean anchors
0 dirty anchors
32 feasible-state occurrences
1,024 single-edge mask-extension checks
```

It also exhausts every side-three mask of size zero, one or two:

```text
172 masks
172 feasible masks
43 clean anchors
129 dirty anchors
588 dirty-anchor candidate records
324 single-edge mask-extension checks
```

Twelve independent corruptions are rejected, including malformed masks,
family/triple-universe drift, wrong anchor or dispatch, wrong canonical target,
candidate-category drift, an honesty flip and a bad seal.

The contract digest is:

```text
0cdc1914c11c79e1c9f3274f025263597c8eec5a7ed9c7e60d8cc24d66f817e7
```

The finite censuses are regression evidence. CMR2828--CMR2837 are exact
finite combinatorial statements.

## CMR2839 — T02 consequence and honesty boundary

The local T02 rule now needs only a side length and a labelled deletion mask.
The feasible family, realizable triple universe, anchor, target and response are
all canonical consequences.

The remaining global work is not another local choice convention. It is to
prove that the actual prime-power construction generates exactly the required
sequence of hosts and masks, including:

- every factor, owner, routing and closure-envelope context;
- every initial and inherited deletion mask;
- every contraction and relabelling map;
- every non-mask restriction, if any;
- every finite parameter domain and exclusion;
- recurrence exhaustiveness across all generated contexts; and
- termination or successful descent of every genuine branch.

The checker does not prove those statements or the all-\(n\) conjecture.
