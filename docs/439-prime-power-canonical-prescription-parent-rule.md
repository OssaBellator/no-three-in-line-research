# Canonical duplicate-free prescription parent rule

This chapter records CMR2794--CMR2805.  It strengthens the exact prescription
union of CMR862--CMR869 into a canonical disjoint parent-rule clause.

The checker is:

```text
scripts/check_prime_power_canonical_prescription_partition.py
```

## CMR2794 — first-missing index

Let \(\mathcal F\) be a nonempty equal-cardinality family of labelled states.
Let

\[
C=(f_0,\ldots,f_{r-1})\subseteq Q\in\mathcal F
\]

be an ordered labelled prescription.  For \(R\in\mathcal F\), define

\[
\iota_C(R)=\min\{i:f_i\notin R\},
\]

with \(\iota_C(R)=r\) when \(C\subseteq R\).

This index is defined for every state and is unique.

## CMR2795 — canonical disjoint partition

For \(0\le i<r\), put

\[
\mathcal B_i=
\{R\in\mathcal F:
f_0,\ldots,f_{i-1}\in R,\ f_i\notin R\},
\]

and put

\[
\mathcal B_r=\mathcal F_C
=\{R\in\mathcal F:C\subseteq R\}.
\]

Then

\[
\boxed{
\mathcal F=\bigsqcup_{i=0}^{r}\mathcal B_i.
}
\]

### Proof

Every state has exactly one first-missing index.  Two distinct indices cannot
both be first.  The value \(r\) is exactly the condition \(C\subseteq R\). ∎

This is stronger than the union in CMR862: the older deletion children may
overlap, while the first-missing children are pairwise disjoint.

## CMR2796 — exact counting identity

The partition gives

\[
\boxed{
|\mathcal F|=\sum_{i=0}^{r}|\mathcal B_i|.
}
\]

More strongly, every state occurs in exactly one branch record.  No
inclusion--exclusion correction or duplicate-state reconciliation is required.

## CMR2797 — nonempty-child pruning

Deleting empty \(\mathcal B_i\) leaves an exact disjoint cover.  Thus an
executable rule emits only nonempty operation slots without changing the
represented feasible family.

## CMR2798 — rejected-candidate localisation

Because \(C\subseteq Q\), the rejected state \(Q\) lies only in
\(\mathcal B_r\).  It occurs in no first-missing deletion branch.

Consequently the side branches preserve all states assigned to them without
silently retaining the rejected candidate, while the conditioned branch is the
unique branch that must process \(Q\).

## CMR2799 — exact conditioned contraction

On the final branch, restriction is the exact bijection

\[
\mathcal B_r
\cong
\{C\}\times(\mathcal B_r/C).
\]

If every state in \(\mathcal F\) has cardinality \(k\), every residual state has
cardinality \(k-r\).  The checker verifies injectivity of the residual-state
map.

## CMR2800 — labelled-triple arity

For the canonical new triple \(C_Q=(f_0,f_1,f_2)\) supplied by CMR866, the
complete rule has at most four nonempty branches:

```text
0: omit f0
1: contain f0 and omit f1
2: contain f0,f1 and omit f2
3: contain f0,f1,f2 and contract/hand off the forced triple
```

Hence the CMR867 constant-arity response can be made duplicate-free without
increasing its arity.

## CMR2801 — canonical operation-slot keys

Every nonempty branch publishes a source-independent operation key containing:

- clause ID `canonical-first-missing-prescription-v1`;
- branch index and branch ID;
- operation kind;
- the required prescription prefix; and
- the omitted prescription edge, or null on the conditioned branch.

Deletion branches use
`prescription-first-missing-deletion`.  The final branch uses
`prescription-conditioned-contraction`.

The operation-slot key is canonically hashed.

## CMR2802 — compatibility with the proved new-triple trigger

CMR866 proves that every nonimproving target-destroying candidate supplies a
new labelled triple.  Applying CMR2795 to that triple gives a genuine
conditional parent-rule clause for precisely that situation.

No new geometric trigger is assumed: the clause begins only after the CMR866
hypotheses and prescription have been established.

## CMR2803 — completeness and duplicate freedom

The clause simultaneously has:

```text
exact_union = 1
pairwise_disjoint = 1
duplicate_free_child_assignment = 1
rejected_candidate_only_in_conditioned_branch = 1
conditioned_cardinality_drop = 3
```

This removes one concrete obstruction to placing the CMR862--CMR869 response
inside the T02 operation-slot system.

## CMR2804 — exhaustive regression and corruption rejection

The checker exhausts every equal-cardinality family of three-subsets of a
five-edge universe that contains the prescribed triple:

```text
512 families
2,816 state occurrences
1,824 nonempty branch occurrences
315 families with all four branches nonempty
11 rejected corruptions
```

The corruptions include duplicate prescription edges, missing rejected state,
a prescription not contained in the rejected state, unequal state
cardinalities, missing or duplicated branch members, wrong operation kind,
wrong prefix, corrupted contraction residuals, an honesty flip and a bad seal.

The contract digest is:

```text
dca487a954f03f5aaebf09394ab427ef5b338f0e107adf6581146d84863ce39c
```

The exhaustive finite census is regression evidence.  CMR2794--CMR2803 are
exact set-family statements.

## CMR2805 — T02 consequence and honesty boundary

The branch now contains one non-synthetic, duplicate-free conditional
parent-rule clause: the canonical response to a CMR866 new labelled triple.

It still does not provide:

- an exhaustive classification of every global parent state;
- proof that every parent reaches the CMR866 trigger or another listed clause;
- the complete finite parameter domains and exclusions;
- genuine expected host IDs for every global parent;
- complete T03 populations; or
- any all-\(n\) implication.

The checker permanently records:

```text
conditional_parent_rule_clause_ready = 1
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The no-three-in-line conjecture remains open.
