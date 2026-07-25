# Packet losses reduce to deletion or exchange ancestry

CMR418--CMR421 charge packet recreation to selected-state churn, but cumulative
churn can still be large if many distinct packet states are installed. Inside a
certificate-directed deletion pass there is a sharper response. A recreated
packet triple is realized by the current selected perfect matching. Either one
of its edges is deletable, giving permanent mask progress, or all three edges
are essential and CMR217 attaches the triple to earlier deletions through
alternating exchange ancestry.

This chapter removes cumulative churn as an independent packet-scheduling term
inside one deletion pass. The unresolved packet term becomes exactly the width
of the fully forced ancestry DAG.

Let

\[
G_0\supset G_1\supset\cdots\supset G_d,
\qquad
G_i=G_{i-1}-f_i,
\]

be a certificate-directed deletion pass on a balanced parent matching host with
`t` vertices on each side. Assume every `G_i` has a perfect matching and `G_0`
is the half-degree host of CMR208, so CMR212 gives no essential edge initially.
At any intermediate time, a packet installation chooses a perfect matching
`M'` of the current residual host.

A **lossy reset** is a selected-state transition after which at least one packet
which was previously clean is dirty.

## 1. One lossy reset

### Theorem CMR422 — PROVED

Consider one lossy reset from selected perfect matching `M` to selected perfect
matching `M'` in the current residual host `G`. Choose one lost packet and one
of its recreated candidate-only triples

\[
Q\subseteq M'.
\]

Then exactly one of the following responses is available.

1. **Deletion response.** Some prescribed edge `e\in Q` is nonessential in `G`.
   Then
   \[
   G-e
   \]
   has a perfect matching. Deleting `e` permanently destroys `Q` and strictly
   enlarges the monotone forbidden mask.
2. **Fully forced response.** Every edge of `Q` is essential in `G`. Then `Q` is
   a fully forced rank-three certificate. Each of its edges has a
   first-essentiality time and an alternating exchange link to an earlier
   certificate deletion, as in CMR217. The resulting ancestry links point
   strictly backward in the deletion pass.

Moreover, because the packet was clean before the reset, `Q` contains an
entering edge of `M'\setminus M` by CMR418.

### Proof

The selected matching `M'` realizes `Q`, so every edge of `Q` belongs to the
current residual host `G`. If one edge is nonessential, deleting it preserves a
perfect matching by definition and eliminates every realization containing
that edge, including `Q`.

Otherwise every prescribed edge is essential in `G`. The deletion pass began
with no essential edge, so CMR217 applies to each edge of `Q` and supplies its
first-essentiality deletion and alternating exchange cycle. CMR218 orients all
such links strictly backward. The entering-edge assertion is CMR418. ∎

The theorem does not assert that one deletion restores every lost packet. It
asserts that every lossy reset has an immediate monotone deletion response
unless it exposes a fully forced ancestry certificate.

## 2. Exact deletion budget

### Theorem CMR423 — PROVED

The total number `d` of successful edge deletions in the pass satisfies

\[
\boxed{
 d\le |E(G_0)|-t\le t(t-1).
}
\]

Consequently, the deletion response in CMR422 can occur at most `t(t-1)` times.

### Proof

All deleted edges are distinct because the residual hosts are nested. The final
host `G_d` contains a perfect matching and therefore at least `t` edges. Hence

\[
d=|E(G_0)|-|E(G_d)|\le |E(G_0)|-t.
\]

Finally `|E(G_0)|\le t^2`. ∎

This bound is deliberately independent of how much selected-state churn occurs
between deletions.

## 3. First-dirty packet schedule

Fix `P` harmonic packets and use the first-dirty installation rule of CMR421.
After every lossy reset, immediately choose one lost packet and apply CMR422.
If the deletion response is available, perform that deletion before the next
packet installation. Otherwise record one fully forced packet event.

Let

- `B` be the number of lossy reset batches;
- `L` be the total number of packet losses, counted with multiplicity;
- `T` be the number of packet installations;
- `m` be the number of deletion responses used by this policy;
- `F` be the number of fully forced packet events.

### Theorem CMR424 — PROVED

One has

\[
\boxed{B\le m+F}
\]

and

\[
\boxed{
L\le P(m+F).
}
\]

Consequently,

\[
\boxed{
T
\le
P+L
\le
P\bigl(1+m+F\bigr)
\le
P\bigl(1+t(t-1)+F\bigr).
}
\]

### Proof

Every lossy reset is processed once. If its chosen recreated triple has a
nonessential edge, the policy performs a new permanent deletion. Distinct such
responses use distinct deleted edges, so the number of deletion-answered
batches is at most `m`. Every remaining batch contributes one fully forced
event, proving `B\le m+F`.

At most `P` previously clean packets can be lost in one reset, so `L\le PB`.
CMR421 gives `T\le P+L`. Apply CMR423 to `m`. ∎

Thus packet scheduling is polynomial inside one deletion pass as soon as the
number of fully forced packet events is polynomially bounded.

## 4. Conditional closure from ancestry width

For every fully forced packet event, count its CMR217 ancestry links with
multiplicity. Let `A` be the total number of such links. Every forced event has
at least one link, so

\[
F\le A.
\]

Assume that each earlier deleted certificate receives at most `w` incoming
links from fully forced packet events during the pass.

### Corollary CMR425 — PROVED UNDER THE ANCESTRY-WIDTH HYPOTHESIS

Under the preceding incoming-width bound,

\[
\boxed{
F\le A\le wd
}
\]

and therefore

\[
\boxed{
T
\le
P\bigl(1+(1+w)d\bigr)
\le
P\bigl(1+(1+w)t(t-1)\bigr).
}
\]

### Proof

There are `d` earlier deletion certificates and each receives at most `w`
incoming links, so `A\le wd`. Since every fully forced packet event supplies at
least one ancestry link, `F\le A`. Substitute in CMR424 and use CMR423. ∎

CMR425 is a genuine termination reduction for the packet schedule. It does not
assume a bound on cumulative selected-state churn and does not use the
factorial number of parent permutations. The remaining packet obstruction is
precisely a quantitative incoming-width bound for fully forced exchange
ancestry.

## 5. Revised frontier

Inside one certificate-directed deletion pass:

1. exact selected-state cycles are erasable by CMR410;
2. distinct selected states pay edge churn by CMR413--CMR417;
3. packet recreation is supported by entering edges and paid by equal leaving
   churn through CMR418--CMR421;
4. every lossy reset now pays a permanent deletion or a fully forced ancestry
   event by CMR422;
5. permanent deletion responses occur at most `t(t-1)` times by CMR423.

Therefore cumulative churn is no longer the essential packet-scheduling
unknown. The live fixed-envelope target is the incoming width of the CMR217
ancestry DAG, together with the analogous treatment of repeated local ancestor
resets not arising from packet loss.

No all-`n` theorem is claimed here. Matching-difference identities, deletion
budgets, lossy-batch accounting, and the conditional width closure are checked
in
[`scripts/verify_prime_power_packet_loss_ancestry.py`](../scripts/verify_prime_power_packet_loss_ancestry.py).
