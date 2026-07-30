# Complete local target-trigger response partition

This chapter records CMR2806--CMR2817. It combines the target-destruction identity of CMR698, the canonical new-triple trigger of CMR866, and the duplicate-free prescription rule of CMR2794--CMR2805 into one complete local response theorem relative to a supplied feasible family, anchor state, triple universe and nonempty designated target bank.

The executable checker is:

```text
scripts/check_prime_power_target_trigger_response_partition.py
```

## CMR2806 — designated target core

Let \(\mathcal F\) be a nonempty equal-cardinality family of finite labelled states, let \(S\in\mathcal F\) be the anchor, and let \(\mathcal Q\) be a nonempty family of designated triples contained in \(S\).

Define the target core

\[
K(\mathcal Q)=\bigcup_{T\in\mathcal Q}T.
\]

The core is a compatible fixed partial state because it is contained in the anchor.

## CMR2807 — target preservation equals core containment

For every \(R\in\mathcal F\), the following are equivalent:

1. every target in \(\mathcal Q\) is contained in \(R\);
2. \(K(\mathcal Q)\subseteq R\).

### Proof

If every target is contained, then every cell appearing in their union is contained. Conversely, every target is a subset of the union. ∎

Thus the target-preserving family is exactly the conditioned family

\[
\mathcal F_{K}=\{R\in\mathcal F:K\subseteq R\}.
\]

## CMR2808 — exact target-core contraction

Restriction gives the bijection

\[
\boxed{
\mathcal F_K\cong\{K\}\times(\mathcal F_K/K).
}
\]

If every state has cardinality \(k\), every residual state has cardinality \(k-|K|\). The residual map is injective because adjoining the fixed core reconstructs the original state.

This supplies a genuine conditional T02 operation:

```text
target-preserving-core-contraction
```

## CMR2809 — exact candidate trichotomy

For an alternative state \(R\ne S\), let

\[
D(R)=|\{T\in\mathcal Q:T\nsubseteq R\}|
\]

and let

\[
\Delta\Phi(R)=\Phi(R)-\Phi(S),
\]

where \(\Phi\) counts triples from the supplied exact triple universe.

Exactly one of the following occurs:

1. \(D(R)=0\): target-preserving core contraction;
2. \(D(R)>0\) and \(\Delta\Phi(R)<0\): strict potential improvement;
3. \(D(R)>0\) and \(\Delta\Phi(R)\ge0\): nonimproving target destruction.

The three predicates are pairwise disjoint and exhaustive.

## CMR2810 — strict-improvement action

The second class already supplies the desired local progress:

```text
target-destroying-strict-improvement
```

No prescription split is needed because the candidate has strictly smaller triple potential than the anchor.

## CMR2811 — new-triple surplus

For a candidate in the third class, put

\[
\mathcal N(R,S)=\mathcal T(R)\setminus\mathcal T(S).
\]

CMR698 gives

\[
\Phi(R)-\Phi(S)=|\mathcal N(R,S)|-|\mathcal L(S,R)|.
\]

Every destroyed designated target belongs to \(\mathcal L(S,R)\). Hence

\[
\boxed{|\mathcal N(R,S)|\ge D(R)\ge1.}
\]

Therefore every nonimproving target-destroying candidate contains at least one genuinely new triple.

## CMR2812 — canonical new-triple witness

Order the exact triple universe canonically and choose the least member of \(\mathcal N(R,S)\). This gives a deterministic labelled prescription \(C_R\subseteq R\), independent of user-supplied witness choices.

The checker publishes the complete lost-target list, new-triple list, potential difference and canonical witness for every candidate.

## CMR2813 — duplicate-free response to the third class

Apply CMR2794--CMR2805 to \(C_R=(f_0,f_1,f_2)\). The full feasible family is partitioned into:

```text
0: omit f0
1: contain f0 and omit f1
2: contain f0,f1 and omit f2
3: contain f0,f1,f2 and contract the forced triple
```

The branches are pairwise disjoint, cover every state exactly once, isolate the rejected candidate in the conditioned branch and reduce conditioned cardinality by three.

## CMR2814 — complete local response rule

Relative to the supplied target bank, every alternative now has an exact action:

```text
target-preserving             -> contract the complete target core
target-destroying, improving  -> accept strict potential improvement
target-destroying, nonimproving -> canonical new-triple first-missing partition
```

Thus

```text
exact_candidate_trigger_partition = 1
target_preserving_core_contraction = 1
strict_improvement_action = 1
nonimproving_new_triple_action = 1
local_target_response_rule_ready = 1
```

This closes the local trigger complement that remained after CMR2805.

## CMR2815 — exhaustive hypergraph regression

The checker exhausts every triple hypergraph on a five-cell universe, every four-cell anchor, and every nonempty target subbank contained in that anchor. It checks:

```text
20,800 hypergraph/anchor/target scenarios
83,200 alternative-candidate records
10,240 target-preserving candidates
42,240 target-destroying strict improvements
30,720 target-destroying nonimproving candidates
```

Every nonimproving candidate satisfies the exact new-triple inequality and receives a canonical duplicate-free prescription partition.

## CMR2816 — subfamily and corruption regression

The checker also exhausts every subfamily of the five canonical four-cell states containing its anchor:

```text
1,200 subfamily scenarios
2,400 subfamily candidate records
```

Twelve independent corruptions are rejected, including malformed families, missing anchors, duplicate triples, invalid target banks, core corruption, category corruption, a false new-triple witness, missing candidate records, an honesty flip and a bad manifest seal.

The contract digest is:

```text
c7239521fb73e0347783e76ebfde83d96e968712376745542b5a93888312c0ef
```

The exhaustive finite censuses are regression evidence. CMR2806--CMR2814 are exact finite set-family and triple-counting statements.

## CMR2817 — T02 consequence and honesty boundary

The branch now contains a complete local candidate-response rule relative to a supplied feasible family, anchor, exact triple universe and nonempty designated target bank.

It still does not supply or prove:

- the global generation of every feasible parent family;
- the choice and existence of the designated target bank at every parent;
- exhaustion of all parent-state types and closure-envelope situations;
- every finite parameter axis and exclusion;
- genuine expected hosts and T03 populations;
- termination of repeated local responses; or
- the all-\(n\) implication.

The checker permanently records:

```text
local_target_response_rule_ready = 1
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The no-three-in-line conjecture remains open.
