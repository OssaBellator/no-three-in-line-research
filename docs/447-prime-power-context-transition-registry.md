# Exact square/asymmetric context-transition registry

This chapter records CMR2888--CMR2899. CMR2852--CMR2887 close the local
square/asymmetric context class and its complete candidate-response rule. The
present chapter adds the first typed transition layer between those local
contexts. It traces the genuine CMR830 deletion and CMR862/CMR2794
first-missing operations to literal generated children.

The executable checker is:

```text
scripts/check_prime_power_context_transition_registry.py
```

## CMR2888 — canonical sealed context identity

For an asymmetric context

\[
(n;R_0,K_0,R_1,K_1;D,P),
\]

the checker records the literal ambient side, layer row and column domains,
deleted edges and required edges. It also binds:

- the exact feasible-state count;
- the exact realizable-triple count;
- the SHA-256 of the generated feasible family; and
- the SHA-256 of the generated exact triple universe.

The resulting `context_sha256` is a canonical identity for the complete local
context semantics, not merely for its name or parameter tuple.

## CMR2889 — typed transition record

A context transition record contains exactly:

```text
operation kind
source theorem identifiers
construction labels
literal parent context
literal child context
operation payload
exact family semantics
```

The construction labels are:

```text
operation_slot
owner
routing
factor
envelope
```

They are bound as nonempty identifiers. Their truth as labels of the actual
prime-power construction is not inferred from the transition checker.

## CMR2890 — exact single-edge deletion transition

For an unclassified edge `f` of an asymmetric context, the child obtained by
adding `f` to the deleted mask satisfies

\[
\boxed{
\mathcal F(D\cup\{f\},P)
=
\{S\in\mathcal F(D,P):f\notin S\}.
}
\]

The transition record binds the parent and child context identities and records
CMR830, CMR2843 and CMR2868 as its theorem ancestry. The child triple universe
is contained in the parent universe.

## CMR2891 — exact required-edge conditioning transition

For an unclassified compatible edge `f`, the child obtained by adding `f` to
the required set satisfies

\[
\boxed{
\mathcal F(D,P\cup\{f\})
=
\{S\in\mathcal F(D,P):f\in S\}.
}
\]

The transition record binds CMR862, CMR2844 and CMR2869. Again the child triple
universe is contained in the parent universe.

## CMR2892 — exact forced-set contraction transition

Let `C` be a nonempty compatible subset of the required set. The generated
forced-set child from CMR2870--CMR2872 is installed as the literal transition
child. The record binds:

- the forced edges;
- exact opposite-layer blockers;
- parent and child state counts;
- the restriction/adjoin bijection;
- the transported deleted and required sets; and
- the exact transported triple universe.

The child family and triple-universe hashes are recomputed from the child
context and must equal the contraction manifest hashes.

## CMR2893 — exact contradiction terminal

A first-missing branch can formally require and delete the same edge when that
edge was already required by the parent context. Such a branch is not treated as
an malformed ordinary context. It has a canonical

```text
required-deleted-contradiction-terminal
```

identity with empty feasible family and empty triple universe.

This records the exact empty branch without weakening deleted/required
disjointness for genuine contexts.

## CMR2894 — genuine CMR830 operation trace

Let `Q` be a feasible rejected state and choose an edge `f in Q`. The CMR830
trace installs the exact deletion transition for `f`.

The generated child:

1. excludes `Q`;
2. preserves every parent state omitting `f`; and
3. equals the complete single-edge deletion child.

Thus the abstract CMR830 state-exclusion operation is now attached to a literal
square/asymmetric parent and child context.

This is a genuine theorem trace. It is not yet a trace of a particular owner,
routing, factor or envelope step from the full construction.

## CMR2895 — genuine CMR862 first-missing trace

Let `C=(f_0,f_1,f_2)` be a compatible prescription contained in a rejected
state. The trace emits four typed transition records:

```text
branch 0: delete f0
branch 1: require f0, delete f1
branch 2: require f0,f1, delete f2
branch 3: require f0,f1,f2, then contract C
```

The branch records use CMR862, CMR2794, CMR2847, CMR2882 and CMR2883 as their
exact theorem ancestry.

The four child families are pairwise disjoint and exhaustive. The rejected state
occurs only in branch three, whose literal child is the exact asymmetric
forced-set contraction.

## CMR2896 — transition-family semantic closure

Every admitted transition kind now carries an executable family statement:

| Transition kind | Exact child semantics |
|---|---|
| `single-edge-deletion` | parent states omitting one edge |
| `required-edge-conditioning` | parent states containing one edge |
| `forced-set-contraction` | exact forced-set restriction |
| `first-missing-deletion` | exact first-missing side branch or contradiction terminal |
| `first-missing-conditioned-contraction` | exact contraction of the full-prescription branch |

No transition is accepted merely because its parent and child identifiers are
well formed.

## CMR2897 — construction-label honesty boundary

The transition record binds owner, routing, factor and envelope strings, but the
checker does not derive those strings from the actual construction. It records:

```text
construction_labels_bound = 1
actual_construction_ancestry_proved = 0
```

A later construction theorem must supply the real labels and prove that every
actual operation produces the recorded parent and child contexts.

## CMR2898 — finite transition regression

On the complete side-three square context the checker records:

```text
12 parent states
18 single-edge deletion transitions
18 required-edge conditioning transitions
72 CMR830 rejected-state/edge traces
4 realizable labelled triples
4 forced-set contraction transitions
8 CMR862 triple/state first-missing bundles
32 first-missing branch transitions
8 rejected malformed or corrupted cases
```

Every child family is regenerated from its literal context and checked against
the direct operation definition.

The contract digest is:

```text
ace68b33d5c7111a5d623cb5a1db128ccc86bb193601404a5ede4713571b241d
```

The finite census is regression evidence. CMR2888--CMR2897 are exact finite
context and set-family statements.

## CMR2899 — T02 consequence and honesty boundary

The branch now has a typed, executable transition language for the local
operations that are already genuinely proved:

```text
CMR830 single-edge deletion
CMR862/CMR2794 first-missing conditioning
exact forced-set contraction
```

The checker records:

```text
canonical_context_identity_sealed = 1
single_edge_deletion_transition_exact = 1
required_edge_conditioning_transition_exact = 1
forced_set_contraction_transition_exact = 1
cmr830_single_edge_trace_exact = 1
cmr862_first_missing_trace_exact = 1
transition_child_context_generated = 1
transition_family_semantics_exact = 1
construction_labels_bound = 1
actual_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The next genuine theorem is no longer a schema theorem. It must trace one actual
owner, routing, factor or closure-envelope operation from its original
construction statement to a transition record and prove the supplied labels and
child context from first principles. The complete transition-kind bank,
termination, genuine T03/T04 population and the all-`n` implication remain open.
