# Routing-skeleton changes have genuine square/asymmetric context ancestry

This chapter records CMR2900--CMR2919. CMR2888--CMR2899 define a typed
transition language for the local square/asymmetric context engine but leave its
owner, routing, factor and envelope labels unverified. The present chapter
installs the first construction-derived operation in that language.

The source operation is the factor-prefix routing change of CMR656--CMR676. A
balanced factor host is embedded as layer zero of an asymmetric context, with an
empty second layer. The checker reconstructs the canonical prime-power envelope,
the old and new routing skeletons, all changed vertices, exact entering and
leaving support, the complete routing-changing alternating-component union, and
the inherited full-token payment.

The executable checkers are:

```text
scripts/check_prime_power_routing_change_context_ancestry.py
scripts/check_prime_power_routing_change_history_payment.py
```

## CMR2900 — exact one-layer factor embedding

Let `p` be prime, `h>=1`, and `t=p^h`. Let `H` be a balanced factor host with
source set `X`, target set `Y`, and `|X|=|Y|=d>=2`. Any forbidden factor edges
form a deleted set `D`.

Embed this host in the asymmetric context

```text
ambient side: t
layer 0 rows: X
layer 0 columns: Y
layer 1 rows: empty
layer 1 columns: empty
deleted edges: {(0,x,y):(x,y) in D}
required edges: empty
```

Then the feasible asymmetric states are in exact bijection with the perfect
matchings of `H` avoiding `D`.

### Proof

Layer zero is precisely a perfect matching from `X` to `Y`; the empty second
layer contributes one empty matching and no physical-cell collisions. The
literal deleted-edge condition is the factor-host restriction. ∎

Thus the factor operation is represented by the established asymmetric context
class rather than a new host type.

## CMR2901 — canonical factor envelope is reconstructed

For a nonempty coordinate set `A`, let

\[
\delta(A)=\max\{s:\text{all members of }A\text{ are congruent modulo }p^s\}.
\]

The checker recomputes

\[
\beta=\min\{\delta(X),\delta(Y)\}.
\]

For `d>=2`, one has `beta<h`, and at least one of the source or target
projections occupies two next-digit classes. The factor-envelope record contains
exactly:

- `p`, `h`, `beta` and the envelope side `t/p^beta`;
- the common source and target residues modulo `p^beta`; and
- the occupied source and target next-digit labels.

This is the literal CMR656--CMR657 envelope data.

## CMR2902 — exact routing-skeleton reconstruction

For a factor matching `M`, the checker reconstructs both routing maps

\[
x\mapsto s(M(x)),
\qquad
y\mapsto r(M^{-1}(y)),
\]

and every nonempty cell `(X_rs(M),Y_rs(M))`. Corresponding source and target
routing cells have equal cardinality.

The resulting canonical digest is an exact label for `Gamma(M)` from CMR659.

## CMR2903 — routing-change equivalence

For two feasible factor matchings `M` and `N`, the typed operation is admitted
exactly when their reconstructed routing-skeleton digests differ.

This is equivalent to at least one source or target changing its child-routing
label, as in CMR671.

## CMR2904 — changed-vertex conservation

Define

\[
A_X(M,N)=\{x:s(M(x))\ne s(N(x))\},
\]

\[
A_Y(M,N)=\{y:r(M^{-1}(y))\ne r(N^{-1}(y))\}.
\]

Each changed set has cardinality zero or at least two. The checker rejects a
purported routing change with no changed vertex or a changed set of size one.

### Proof

The target-child margins and source-child margins are fixed. A single changed
vertex would remove one unit from one class and add one unit to another without a
compensating change. ∎

## CMR2905 — exact entering and leaving support

The checker reconstructs

\[
E^+_\Gamma(M,N)
=
\{(x,N(x)):x\in A_X\}
\cup
\{(N^{-1}(y),y):y\in A_Y\},
\]

and the analogous leaving set `E^-_Gamma(M,N)` using `M`.

It proves exactly:

\[
|E^+_\Gamma|\ge2,
\qquad
|E^-_\Gamma|\ge2,
\]

\[
E^+_\Gamma\subseteq N\setminus M,
\qquad
E^-_\Gamma\subseteq M\setminus N.
\]

These are the physical support statements of CMR672.

## CMR2906 — routing-changing alternating-component union

The symmetric difference `M triangle N` is decomposed into its bipartite
alternating components. A component is marked precisely when it contains a
changed source or target vertex.

Every entering support edge lies in the new matching part of the marked union,
and every leaving support edge lies in the old matching part of the marked
union. No assertion is made that one component contains all support.

The checker includes an explicit side-four witness consisting of two disjoint
alternating swaps, both of which change routing. This verifies the union scope
required by CMR673.

## CMR2907 — typed routing-skeleton-change transition

Every admitted pair `(M,N)` emits one typed transition record with:

```text
transition_kind = routing-skeleton-change
parent context = embedded factor context
child context = the same embedded factor context
parent state = M
child state = N
old and new routing skeletons
changed source and target vertices
entering and leaving routing support
all alternating components
```

The parent and child contexts are equal because a routing change rematches one
fixed factor host; it does not itself delete, require or contract an edge.

## CMR2908 — theorem-derived construction labels

The transition labels are no longer placeholders.

- The operation slot is `CMR671-CMR676-routing-skeleton-change`.
- The factor and owner labels are canonical digests of the ambient side,
  source/target sets and deleted factor edges.
- The routing label is the ordered old-to-new routing-skeleton digest pair.
- The envelope label is the canonical CMR656--CMR657 envelope digest.

Hence

```text
construction_labels_theorem_derived = 1
routing_change_construction_ancestry_proved = 1
```

for this operation kind.

## CMR2909 — exact same-context state semantics

Both endpoint states are members of the same generated factor family. The
transition changes only the selected matching state and preserves the complete
factor context and its feasible-family digest.

Thus the operation is an exact state transition inside one canonical asymmetric
context, not an inferred relation between anonymous histories.

## CMR2910 — finite transition regression

The ancestry checker exhausts nontrivial factor hosts with matching size at most
three for:

```text
p=2, h=2
p=3, h=1
```

It records:

```text
62 factor hosts with routing changes
284 routing-change transitions
638 entering support incidences
638 leaving support incidences
245 distinct ordered routing-skeleton pairs
1 explicit multi-component routing-change witness
9 rejected malformed or corrupted cases
```

Every transition recomputes the factor envelope and both routing skeletons from
literal coordinates and matchings.

The contract digest is:

```text
b2de334dedbde2a865704f3d08cc9f590e74e14b7e8d813c329e59cc97636360
```

## CMR2911 — per-transition ancestry honesty boundary

CMR2900--CMR2910 prove actual construction ancestry for the
`routing-skeleton-change` operation kind only. They do not prove ancestry for
owner changes, factor creation, child handoffs, closure-envelope changes,
restorations, returned-edge operations, target-bank handoffs or scheduler steps.

Therefore the checker records:

```text
routing_change_construction_ancestry_proved = 1
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

## CMR2912 — fixed factor-owner-envelope history

Consider a simple sequence of distinct factor matchings in which every
consecutive pair changes routing. Applying CMR2907 to each pair gives a sequence
of typed transitions.

The history checker requires the factor, owner and envelope labels to be
identical across the sequence. Only the routing label and endpoint states vary.

This is the literal fixed-owner/factor/envelope scope of CMR674--CMR676.

## CMR2913 — exact history support incidence

For `R` routing-changing transitions, let `C^+` and `C^-` be the total entering
and leaving routing-support incidences with multiplicity. Then

\[
C^+\ge2R,
\qquad
C^-\ge2R.
\]

The checker stores the exact multiplicity of every labelled entering and leaving
factor edge.

## CMR2914 — exact full-token payment

CMR413 assigns exactly `(p+1)(h-1)` labelled nonroot full-token incidences to
every physical parent edge. Hence the history carries exactly

\[
(p+1)(h-1)C^+
\]

entering incidences and the analogous leaving total.

The checker recomputes these totals from the typed transition support rather
than accepting a supplied payment value.

## CMR2915 — recurrent entering edge or finite history

Fix `lambda>=2`. If no entering routing-support edge occurs in `lambda`
transitions, then every host edge occurs at most `lambda-1` times. Since every
transition contributes at least two incidences,

\[
\boxed{
R\le
\left\lfloor
\frac{(\lambda-1)|E(H)|}{2}
\right\rfloor.
}
\]

Otherwise one exact entering edge is recurrent with multiplicity at least
`lambda`. The checker verifies this dichotomy from the literal support
multiplicities.

## CMR2916 — recurrent leaving edge or finite history

The identical statement holds for leaving routing-support edges. The checker
maintains separate entering and leaving multiplicity tables and validates both
bounds.

## CMR2917 — routing-history endpoint

Every supplied simple fixed-factor routing-change history reaches both an
entering and a leaving alternative:

1. an exact recurrent physical routing edge; or
2. the CMR674 finite-history bound.

The full-token totals of CMR2914 attach exact payment to the same labelled edge
records. Repeated occurrences are retained with multiplicity and are not called
fresh.

## CMR2918 — finite history regression

The history checker constructs greedy simple routing-change histories on the
side-four binary factor and the side-three ternary factor. Across thresholds
`lambda=2,3,4`, it records:

```text
78 routing histories
867 routing transitions inside those histories
56 recurrent-entering-edge cases
22 finite-history cases
5,814 labelled entering full-token incidences
8 rejected malformed or corrupted cases
```

Both sides of the CMR674 alternative occur in the regression.

The history contract digest is:

```text
b7c4efe585e6fa70cf6556e4eb86969e685c542d8192326b3c29169c8f9b2259
```

## CMR2919 — T02 consequence and global honesty boundary

The typed transition layer now contains its first theorem-derived construction
operation. Routing-skeleton changes have exact:

- factor-context embedding;
- envelope and routing labels;
- state-to-state semantics;
- entering and leaving support;
- alternating-component scope;
- full-token payment; and
- recurrent-edge or finite-history endpoint.

The remaining T02 work is no longer to invent labels for routing changes. It is
to install the other genuine construction operation kinds, prove that their bank
is exhaustive, and combine their individual descent or finite-stock alternatives
into one global termination theorem.

The permanent boundary is:

```text
routing_change_construction_ancestry_proved = 1
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

No T01 source bank, genuine T03/T04 population, exceptional chamber, final
premise, handoff, review, dossier or all-`n` theorem is supplied here.
