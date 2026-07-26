# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

The collision-free theorem ledger is split across

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` from CMR870.

## Established prime-power structure

- Closure envelopes form at most `h+1` nested epochs with at most `h` strict
  expansions.
- Protected/free, child-routing, essential-core, exchange-SCC, and unit-wall
  matching products are exact.
- Physical restoration is defined in absolute parent coordinates and is not
  duplicated by owner relabelling.
- Returned structural deletions form a forward acyclic ancestry forest.
- A recurrent target edge deletes while nonessential; essential return produces a
  deficiency-one Hall wall and exact lower-side factorisation.
- Historical protected-line targets are neutralised through stored labelled
  pairs, with reuse counted by physical cell--absence-run slots.
- A recurrent physical target has at most six labelled same-layer pair types. A
  recurrent type deletes one nonessential pair edge or contracts two essential
  pair edges.

## Completeness correction and branch compression

The anchor-preserving complete-entering-batch deletion of CMR785--CMR821 is a
rigorous **aggressive subbranch**, but it may remove other untested states. Its
forcing and contraction conclusions are branch-local.

Completeness is restored by exact single-edge child unions and by the
rank-three prescription split. Every nonimproving target-destroying candidate
has at most three deletion children plus one conditioned forced-triple branch.
Every state survives in at least one branch.

The split can be made disjoint by assigning each state to the first prescription
edge it omits. Every internal step fixes or deletes a previously undecided edge,
so the disjoint target-resolution tree has depth at most `2n^2`.

Terminal leaves forced by the same physical target may be unioned as set
families. Splitting by the eight layer assignments of that target gives at most

\[
8\binom{n^2}{3}
\]

fixed labelled-triple classes at one resolution stage. These unions are not
assumed to be the perfect-matching family of one common host when their inherited
masks differ.

Along one stable-owner path, canonical new triples have support matching number at
most

\[
B_n=2n^2-2n+\left\lfloor\frac{2n}{3}\right\rfloor.
\]

A maximal support packing gives a cover of size at most `9B_n`. Long paths
therefore concentrate on one physical cell or labelled matching vertex. One exact
labelled edge then batches many candidates through a binary delete/condition
split, with rank-two transfer in the conditioned branch.

## Minimum-anchor proof mode

A proof which analyses an actual minimum-potential state does not need to retain
an unknown improving witness. If `S` minimises the current finite state family,
any restriction preserving `S` preserves one minimum.

For a chosen target of `S`, every target-destroying alternative supplies a
canonical new triple containing an edge outside `S`. Deleting one such edge
rejects the alternative and preserves the minimum. After at most

\[
2n^2-2n
\]

outside-anchor deletions, the chosen physical target—and then any chosen labelled
anchor prescription—becomes fixed in the surviving minimum branch.

Exact contraction preserves minimum status for the induced objective

\[
\Phi_P(R')=\Phi(P\cup R').
\]

Thus completeness-tree width is not an obstruction in minimum-anchor mode. The
remaining issue there is dynamic restoration, anchor loss, and structural owner
change.

## Minimum-face edge dichotomy

Let `\mathcal M` be the complete face of minimum-potential states at one owner.
Every labelled physical edge has exactly one response:

1. some minimum state omits it, so the edge can be deleted while preserving the
   minimum value; or
2. every minimum state contains it, so it belongs to the common minimum core and
   contracts exactly.

Contracting the complete minimum core leaves a residual minimum family with empty
common core. Strict core growth occurs at most `2n` times for a saturated
side-`n` two-layer state.

Repeated restoration of a noncore edge is pure paid reopening: it is deleted
again against an avoiding minimum and carries exact full-token incidence.

## Physical-edge lineage budget

One labelled physical edge has at most

\[
L_{\mathrm{edge}}(N,h)
=
(h+1)\left(1+\sum_{m=1}^{N}(2m^2+m+1)\right)
\]

structural owner slots along a closure branch.

Each owner slot receives at most one uncharged first closure of that edge. If the
edge has `J` active appearances and does not contract, then the genuine
restoration count satisfies

\[
R\ge J-L_{\mathrm{edge}}(N,h),
\]

with labelled nonroot token incidence at least

\[
\max\{0,J-L_{\mathrm{edge}}(N,h)\}(p+1)(h-1).
\]

For every threshold `\lambda>=2`, either one fixed owner sees `\lambda`
restorations or

\[
J\le\lambda L_{\mathrm{edge}}(N,h).
\]

Consequently the former fixed-owner, fixed-edge recurrence now has finite owner
stock, minimum-preserving deletion, exact minimum-core contraction, or explicit
full-token payment.

## Corrections retained

- Naive sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines are not simultaneous target families.
- One edge return may serve several neutralisations in one absence run.
- Removing one essential edge produces Hall deficiency exactly one.
- Owner relabelling does not itself create physical restoration.
- Aggressive batch deletion is branch-local; completeness uses viable child
  unions or disjoint prescription partitions.
- A union of differently masked terminal leaves is a valid set family but is not
  silently treated as one matching host.

## Current open frontier

1. **Owner-transition minimum faces.** Control how the minimum face and its common
   core change when the host, routing skeleton, factor, unit wall, or closure
   envelope changes.
2. **Full-token return capacity.** Convert accumulated genuine restorations into
   an unconditional target-load decrease, protected-reserve exhaustion, or strict
   global potential improvement.
3. **Host representability.** Reconnect set-family minimum-core contraction and
   terminal-leaf unions with the geometric matching-host selectors when masks
   differ.
4. **Prime-field and arbitrary-length transfer.** Rebuild the endpoint for prime
   fields, thin quotient/carry regimes, and every positive integer side length.

## Bottom line

There is no complete proof. Through **CMR925**, local completeness has disjoint
polynomial certificate compression, minimum-anchor analysis avoids branch width,
and every fixed-owner edge deletes against the minimum face or contracts. The
remaining prime-power problem is dynamic owner-transition and full-token capacity,
not another local fixed-edge classification.
