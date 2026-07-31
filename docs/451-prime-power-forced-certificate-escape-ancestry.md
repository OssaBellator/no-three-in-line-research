# Forced mixed certificates have exact deletion, skeleton and restoration escape ancestry

This chapter records CMR2944--CMR2955. CMR2932--CMR2943 generate the canonical
mixed-child deletion procedure and isolate a terminal forced mixed certificate.
The present chapter installs the CMR643--CMR648 escape bank as literal typed
product-context transitions.

The executable checker is:

```text
scripts/check_prime_power_forced_certificate_escape_ancestry.py
```

## CMR2944 — literal forced-product context

Fix one owner-labelled product with factor contexts `I` and `J`, one host of
cross-skeleton edges, one selected skeleton, and a typed three-edge certificate

\[
T=T_I\sqcup T_J\sqcup T_S.
\]

Each factor context records its exact source and target domains, allowed and
deleted edges, complete feasible matching family and essential-edge set. The
skeleton context records both host-available cross edges and the currently
selected skeleton.

The certificate validator requires:

1. every edge of `T_I` to be essential in factor `I`;
2. every edge of `T_J` to be essential in factor `J`; and
3. every edge of `T_S` to belong to the selected skeleton.

Thus every parent product state contains the complete certificate.

## CMR2945 — persistent certificate endpoint

Given a later literal product context and later factor matchings, the checker
first tests whether all three certificate edges still occur in the later state.
If so, it emits

```text
transition_kind = persistent-forced-certificate
```

and no escape witness.

This is the persistent forced-class endpoint of CMR648.

## CMR2946 — exact certificate-edge deletion transition

Assume the later state omits the certificate. The first escape test asks whether
some certificate edge is absent from its later literal host.

For factor edges this means absence from the factor's allowed edge set. For a
skeleton edge it means absence from the cross-skeleton host, not merely absence
from the selected skeleton.

The canonical witness is the least missing typed certificate edge. The checker
emits

```text
transition_kind = certificate-edge-deletion
witness_kind = deletion
```

with complete parent and later factor/skeleton contexts.

This is the first branch of CMR645 and the deletion/reintroduction endpoint of
CMR647--CMR648.

## CMR2947 — host availability versus selected skeleton

The skeleton model separates:

```text
host_edges      = cross edges physically available
selected_edges  = the current protected/free cross skeleton
```

This distinction is necessary. A certificate skeleton edge may remain physically
available while a later selected skeleton omits it. Such an event is skeleton
churn, not certificate-edge deletion.

## CMR2948 — exact selected-skeleton churn transition

If every certificate edge remains host-available but the selected skeleton
changes, the checker emits

```text
transition_kind = selected-skeleton-churn
witness_kind = skeleton
```

The witness is the least physical edge in the symmetric difference of the old
and new selected skeletons. The complete symmetric difference is sealed in the
transition record.

This is the second branch of CMR645. It is compatible with the existing
cross-interface churn ledger but does not identify all possible skeleton
operations with the factor-routing operation of CMR671--CMR676.

## CMR2949 — factor restoration set

Suppose the certificate is absent from the later state, every certificate edge
remains host-available, and the selected skeleton is unchanged. Then some old
essential factor certificate edge is omitted by a later factor matching.

For each affected factor define the genuinely entering edge set

\[
A=E(H')\setminus E(H).
\]

In deleted-mask language, `A` is exactly the set of old deleted edges restored
in the later factor context. The later context may simultaneously delete other
old edges.

The checker requires `A` to be nonempty whenever an old essential edge is
omitted. This is the executable CMR643 statement.

## CMR2950 — exact alternating-component decomposition

Choose an old factor matching and the later matching. Their symmetric difference
is decomposed into its disjoint even alternating components.

For every component meeting an omitted essential certificate edge, the checker
requires at least one later-matching edge in `A`. It records:

```text
omitted essential edges
all entering edges on the component
canonical entering witness
complete old/new alternating component
```

Therefore every affected component receives a distinct entering-edge witness,
and

\[
\chi(R;M,N)\le |N\cap A|.
\]

This is the exact CMR644 component payment. Several omitted essential edges may
share one witness only when they lie on the same alternating component.

## CMR2951 — typed essentiality-loss restoration transition

The third escape branch emits

```text
transition_kind = factor-essentiality-loss-entering-edge
witness_kind = entering
```

with literal old and later factor masks, endpoint matchings, every affected
alternating component and the canonical first entering witness.

This proves a genuine restoration transition for the precise operation in which
a restored factor edge makes an old essential certificate edge avoidable:

```text
factor_restoration_essentiality_loss_transition_exact = 1
```

It does not prove all restoration operations.

## CMR2952 — first-applicable escape partition

For any validated forced certificate and later endpoint, exactly one canonical
category is emitted:

```text
certificate still present
  -> persistent-forced-certificate

first certificate edge absent from later host
  -> certificate-edge-deletion

all certificate edges host-available, selected skeleton changed
  -> selected-skeleton-churn

same selected skeleton, factor certificate edge omitted
  -> factor-essentiality-loss-entering-edge
```

The ordering implements the canonical witness rule of CMR646. Internal matching
variation in unchanged hosts and skeleton cannot create another category.

## CMR2953 — owner-labelled witness stock and token payment

Every genuine escape event receives one witness key

```text
(witness kind, physical parent-board edge)
```

with witness kind in

```text
deletion
skeleton
entering
```

At one owner and ambient side `n`, the witness universe has size at most

\[
3n^2.
\]

For recurrence threshold `lambda>=2`, a history of `J` escape events therefore
has either a witness occurring at least `lambda` times or

\[
J\le 3(\lambda-1)n^2.
\]

For parent side `n=p^g`, each event contributes exactly

\[
(p+1)(g-1)
\]

nonroot full-token incidences under CMR413, counted with multiplicity. This is
the executable CMR646--CMR647 payment.

## CMR2954 — finite regression and corruption rejection

The checker records all four canonical categories and exhausts all balanced
`2 x 2` old/later factor hosts for essentiality-loss events. The census is:

```text
4 canonical persistence/escape scenarios
24 two-by-two essentiality-loss transitions
24 affected alternating components
32 entering-edge incidences on affected components
1 explicit two-component essentiality-loss witness
2 escape-history scenarios
1 finite-history branch
1 recurrent-witness branch
6 history escape events
18 labelled nonroot token incidences
8 rejected malformed or corrupted cases
```

The two-component witness uses two disjoint alternating swaps, verifying that
payment is componentwise rather than one witness per omitted essential edge.

The contract digest is:

```text
dc3c472d258d7cfbbfbf5dd45f68f19a5999c5f4a1818a6945dd460eb1c82253
```

The finite census is regression evidence. CMR2944--CMR2953 are exact finite
matching, context and counting statements.

## CMR2955 — T02 consequence and honesty boundary

The fixed-routing product execution now has exact construction ancestry through:

```text
routing-skeleton change and payment
fixed-routing child-product split
mixed-atom nonessential-edge deletion
mixed-clean strict-child handoff
forced-certificate persistence
forced-certificate edge deletion
selected-skeleton churn
factor restoration with essentiality-loss entering support
```

In particular:

```text
forced_mixed_certificate_escape_proved = 1
factor_restoration_essentiality_loss_transition_exact = 1
```

The permanent boundary remains:

```text
all_restoration_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Owner changes, general closure-envelope transitions, general restoration and
returned-edge operations, target-bank handoffs and scheduler transitions remain
uninstalled. The separate local stocks and strict descents have not yet been
combined into one exhaustive global termination theorem. No all-`n` theorem,
genuine T03/T04 population, chamber proof or final implication is claimed.
