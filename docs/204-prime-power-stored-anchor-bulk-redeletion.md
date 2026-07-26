# A surviving anchor re-closes every restored private batch at once

CMR793--CMR799 attach pairwise disjoint private deletion batches to rejected
nonimproving states. A later reset may restore edges from many batches. The
stored anchor gives a simultaneous response: if the anchor remains feasible,
all restored private edges can be deleted again in one operation. If the anchor
does not remain feasible, one of its own labelled edges has been lost. Thus bulk
reopening reduces to either bulk redeletion or one canonical anchor-loss witness.

Fix one anchor pass on two labelled layer hosts of side `n`. Let

\[
S
\]

be the stored anchor and let

\[
D=A_1\sqcup\cdots\sqcup A_B
\]

be the union of its private entering batches. By construction,

\[
D\cap S=\varnothing.
\]

Consider a later same-vertex-set host family `H` in which some edges of `D` have
been restored.

## 1. Surviving anchor gives simultaneous redeletion

### Theorem CMR800 -- PROVED

If every labelled edge of `S` remains feasible in `H`, then every currently
restored edge of `D` may be deleted simultaneously while preserving the anchor.
More precisely, with

\[
R=D\cap E(H),
\]

one has

\[
\boxed{S\in\mathcal F(H-R).}
\]

Every private batch reopened by `R` is closed again.

### Proof

The anchor is feasible in `H` by hypothesis and is disjoint from `D`, hence from
`R`. Deleting `R` therefore leaves every anchor edge present and preserves the
same ordered saturated state. Every reopened batch meets `R`; removing all of
`R` closes those restored batch edges simultaneously. ∎

The operation may delete many restored edges, but it uses one explicit avoiding
state rather than separate matching arguments.

## 2. Failure of bulk redeletion exposes an anchor edge

### Theorem CMR801 -- PROVED

If the stored anchor is not feasible in the later same-vertex-set host, then

\[
\boxed{S\setminus E(H)\ne\varnothing.}
\]

Choose the first missing labelled edge

\[
f\in S\setminus E(H).
\]

The witness stock has size at most

\[
\boxed{|S|=2n.}
\]

### Proof

A joint anchor state is feasible whenever all of its labelled layer edges remain
available; its layer-disjointness and saturation are intrinsic to `S`. Hence
infeasibility implies at least one missing anchor edge. The state contains `n`
edges in each of two layers. ∎

This is the joint-state analogue of the stored avoiding matching witness in
CMR721.

## 3. Every anchor-loss witness begins after the anchor was stored

### Theorem CMR802 -- PROVED

Every canonical witness `f` from CMR801 was present when the anchor pass began and
became absent later. Its first loss after anchor storage is exactly one of:

1. a selected-state or routing transition with entering/leaving support;
2. a matching-preserving structural deletion;
3. contraction of an endpoint;
4. owner or envelope transition.

In the structural-deletion branch, `f` belongs to a forward deletion generation
of CMR778--CMR779.

### Proof

The edge belongs to the stored feasible anchor, so it was initially present.
Trace its first later present-to-absent transition and classify that transition
as in CMR778. ∎

No owner relabelling alone can create the witness by CMR777.

## 4. Anchor replacement is finite in one monotone segment

Consider a same-vertex-set segment with no physical edge restoration and a
monotone forbidden mask. Whenever the current anchor loses an edge, choose the
first surviving feasible state as the next anchor.

### Theorem CMR803 -- PROVED

The number of anchor replacements in such a segment is at most

\[
\boxed{2n^2-2n.}
\]

More sharply, it is at most the number of distinct labelled edges deleted after
the first anchor was chosen.

### Proof

Every anchor replacement has a canonical missing anchor edge. Under a monotone
mask with no restoration, that edge is newly absent and can never be the cause
of a later first loss again. The two layer hosts contain at most `2n^2` labelled
edges, while every surviving anchor contains `2n` edges, so at most
`2n^2-2n` distinct deletions can occur while preserving feasibility. ∎

A reset which restores an old witness ends the monotone segment and pays the
global restoration ledger instead of receiving another finite-deletion charge.

## 5. Repeated batch reopening has an exact dichotomy

### Theorem CMR804 -- PROVED

For every later reopening of one or more private batches, at least one of the
following occurs.

1. The stored anchor survives and CMR800 re-closes all restored private edges in
   one simultaneous redeletion.
2. One of at most `2n` anchor edges is absent and enters CMR801--CMR803.
3. The reopening transition itself restores at least one private edge and pays
   CMR795--CMR797.
4. An endpoint contracts or the owner/envelope changes.

### Proof

Every reopening contains a genuine private-edge restoration by CMR794. Test the
stored anchor. If it survives, use CMR800. Otherwise use CMR801 and classify its
missing edge by CMR802. Contraction and owner change are the remaining exits. ∎

Branches 1 and 3 can occur together: the restoration is paid and then immediately
removed again.

## 6. Finite anchor epochs or recurrent restoration

### Theorem CMR805 -- PROVED

Fix integers `lambda>=2`. In one fixed labelled vertex universe, a history of
anchor passes and private-batch reopenings reaches at least one of:

1. at most `2n^2-2n` anchor replacements in every monotone no-restoration segment;
2. one exact labelled physical edge restored in at least `lambda` segments;
3. at most
   \[
   \boxed{(\lambda-1)2n^2}
   \]
   physical restoration events without such recurrence;
4. simultaneous bulk redeletion of all currently restored private edges;
5. strict contraction or owner transition.

### Proof

CMR803 bounds anchor replacements within each no-restoration segment. Between
segments there is at least one genuine restoration. Apply the pigeonhole
principle to the `2n^2` labelled physical edges: if none is restored `lambda`
times, there are at most `(lambda-1)2n^2` restoration events. CMR800 gives the
bulk response and CMR802 gives structural exits. ∎

Every restoration event carries exact full-token incidence by CMR413.

## 7. Stored-anchor reopening endpoint

### Corollary CMR806 -- PROVED

Private entering-batch progress cannot be erased anonymously. Every later attempt
to reuse rejected candidates reaches at least one of:

1. simultaneous bulk redeletion using the stored anchor;
2. permanent anchor-edge deletion and finite anchor replacement;
3. one recurrent restored physical edge with exact token payment;
4. forward deletion ancestry for a missing anchor edge;
5. pair contraction, unit-wall factorisation, owner change, or envelope expansion;
6. strict target-potential improvement.

Thus the unresolved global branch is no longer arbitrary reopening of large
private batches. It is recurrence of one exact physical restoration after all
available bulk redeletions and finite anchor losses have been charged.

### Proof

Combine CMR800--CMR805 with the anchor-batch ledger CMR793--CMR799 and the global
return forest CMR777--CMR784. ∎

No all-`n` theorem is claimed. Bulk redeletion, anchor-loss witnesses, monotone
anchor replacement, and restoration thresholds are checked in
[`scripts/verify_prime_power_stored_anchor_bulk_redeletion.py`](../scripts/verify_prime_power_stored_anchor_bulk_redeletion.py).
