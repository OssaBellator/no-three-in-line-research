# Open bottlenecks and research roadmap

## Bottleneck 1: terminal repair needs ancestry

Exact four-endpoint traps exist. CMR143--CMR144 give a potential-one terminal
two-cycle at `N=4` even though a separate potential-zero saturated state exists.
Therefore no theorem depending only on normalized four-board type and current
triple potential can prove global descent.

The prime-field and prime-power routes both require inherited context, not
another purely local four-cell rule.

## Bottleneck 2: inherited parent escape

The composite branch now has the following reduction.

1. CMR123--CMR195 retain a fixed global baseline, contract positive target load,
   construct old-cell-clean parent banks, and attach every branch to a canonical
   envelope with finite expansion depth.
2. CMR196--CMR218 extract Hall walls, peel to a half-degree host, prove
   nonessentiality, and attach acyclic certificate-exchange ancestry.
3. CMR219--CMR359 localize frozen mass by primitive height and reduce sharp Hall
   blockers to universal line-clean banks, walls, secant stars, heavy prefix
   cells, or dispersed full tokens.
4. CMR360--CMR377 give deep-token batches, tunable heavy/dispersion thresholds,
   and exact target-specific completion of one intermediate-height band.
5. CMR378--CMR409 compute row-token and full-token reset costs, extend exact
   completion to harmonic packets, and partition all relevant dyadic bands into
   `O(log t)` exact packets.
6. CMR410--CMR417 erase exact selected-state cycles and prove that every sequence
   of distinct feasible states pays leaving-edge and full-token incidence mass.
7. CMR418--CMR421 prove that recreated selected conflicts meet entering edges,
   whose cardinality equals leaving-edge churn, and reduce first-dirty packet
   scheduling to that churn magnitude.
8. CMR422--CMR425 show that every lossy packet reset in a deletion pass pays a
   permanent deletion or one fully forced ancestry event, with at most
   `t(t-1)` permanent deletion responses.
9. CMR426--CMR428 prove essentiality persistence and show that the packet schedule
   either completes in polynomially many installations or reaches one terminal
   fully forced packet certificate in polynomially many installations.
10. CMR429--CMR432 show that all essential edges lie in one final matching core of
    size at most `t`, giving fewer than `t^3+t` distinct forced rank-`1/2/3`
    edge-set certificates and fewer than `3t^3` distinct ancestry links.
11. CMR433--CMR438 identify every first-essentiality layer with an acyclic
    directed exchange corridor and compress the entire pass to at most `t`
    historical batch exchange cycles.
12. CMR439--CMR443 lift every final essential edge to a common expanded final
    epoch by restoring at most `t` deleted edges. A minimum rollback set is a
    forced matching; large rollback cost gives exact lower-dimensional host
    factorization.
13. CMR444--CMR447 give exact full-token incidence for rollback and charge every
    conflict recreated from a previously clean packet family to a restored edge.

The inherited escape problem is no longer missing a local bank, packet
construction, packet termination statement, polynomial ancestry ledger,
exchange-cycle cover, or common-epoch avoiding matching. The principal
fixed-envelope obstruction is now **qualitative progress from a small restored-
edge footprint**, together with exchange-antichain geometry and the analogous
payment for repeated local ancestor resets.

## Bottleneck 3: selected-state, ancestry, and rollback dynamics

### One-pass aggregate bounds

A two-layer descending prefix pass has labelled full-token return mass at most

\[
\boxed{(p+1)t h(h-1)}.
\]

A complete harmonic-packet sweep has mass at most

\[
\boxed{(p+1)(h-1)P_\eta(t)t}.
\]

Therefore one prefix pass plus one packet sweep has

\[
\boxed{
(p+1)t(h-1)\bigl(h+P_\eta(t)\bigr)
=O_p(t\log^2t).
}
\]

This supersedes the earlier nonsharp `O_p(t^2 log t)` tokenwise union bounds.

### Distinct-state and packet payment

If `M` and `M'` are distinct feasible selected perfect matchings at a fixed
mask, both `M'\setminus M` and `M\setminus M'` have at least two edges. A
cycle-erased history with `L` selected states and labelled mass `I` satisfies

\[
\boxed{
L
\le
1+
\frac{I}{2(p+1)(h-1)}.
}
\]

If `M` is clean for a packet and `M'` recreates one of its triples, the triple
contains an entering edge of `M'\setminus M`; the leaving set
`M\setminus M'` has the same size. For packet weight `W`, the number of
recreated triples is at most

\[
\boxed{2(t-1)^2W|M\setminus M'|}.
\]

### Completion or terminal ancestry

Inside one certificate-directed deletion pass, every lossy packet reset either
removes a nonessential edge or exposes a fully forced CMR217 certificate.
Essentiality is monotone, so a fully forced packet triple is terminal for that
pass.

If `P` is the packet count and `T` the number of packet installations, CMR428
gives:

1. packet completion with
   \[
   \boxed{T\le P\bigl(1+t(t-1)\bigr)};
   \]
2. or one terminal forced certificate with
   \[
   \boxed{T\le P\bigl(2+t(t-1)\bigr)}.
   \]

### Essential core and exchange corridors

Let `E_*` be the final essential set of the deletion pass. CMR429--CMR432 give

\[
|E_*|\le t,
\]

fewer than `t^3+t` distinct forced rank-`1/2/3` edge-set certificates, and fewer
than `3t^3` distinct CMR217 ancestry links.

Fix a perfect matching `M` before deleting one edge `f=\ell_ur_v`. Contract the
matching edges and orient every nonmatching edge `\ell_jr_k` as `j\to k`.
CMR433--CMR436 show:

1. a matching edge is nonessential exactly when its contracted vertex lies on a
   directed cycle;
2. an edge newly essential after deleting `f` is an acyclic vertex on a directed
   `v`-to-`u` corridor;
3. reachability on the new essential vertices is a partial order;
4. every reachability chain lies on one exchange cycle through `f` and can be
   traded in one batch;
5. the minimum number of exchange cycles through `f` covering the layer equals
   the poset width.

For a layer of size `n`, CMR437 gives:

- one exchange cycle batches at least `ceil(sqrt(n))` newly essential edges; or
- there is an antichain of that size which no one exchange cycle through `f`
  can address twice.

Finally CMR438 gives

\[
\boxed{
\sum_iw_i
\le
\sum_i|E_i|
=|E_*|
\le t,
}
\]

so all first-essentiality edges are covered at their valid times by at most `t`
historical exchange cycles.

### Sparse common-epoch rollback

Let `G` be the final host and

\[
\Delta=E(G_0)\setminus E(G).
\]

For `e\in\operatorname{Ess}(G)`, define

\[
\kappa(e)
=
\min\{|R|:R\subseteq\Delta,\ \operatorname{PM}(G+R-e)\ne\varnothing\}.
\]

CMR439--CMR443 give:

\[
\boxed{1\le\kappa(e)\le t.}
\]

If `R` is minimum, every edge of `R` is essential in `G+R-e`, so

\[
\boxed{
\operatorname{PM}(G+R-e)
\cong
\{R\}\times
\operatorname{PM}\bigl((G+R-e)-V(R)\bigr).
}
\]

For every threshold `q`, either:

1. `\kappa(e)<q`, giving a cheap common-epoch rollback; or
2. `\kappa(e)\ge q`, and the avoiding problem factors to side at most `t-q`.

Every terminal rank-`1/2/3` certificate is destroyed by applying this to any one
prescribed edge. Choosing one minimum rollback set for each edge of `E_*` gives

\[
\boxed{
\sum_{e\in E_*}|R_e|\le t^2.
}
\]

The rollback footprints also satisfy a disjoint-packing versus common-deleted-
edge concentration dichotomy.

### Exact rollback payment

CMR444 gives, for every restored set `R`,

\[
\boxed{
\mathcal I(R)
=(p+1)(h-1)|R|.
}
\]

Hence a cheap rollback with `|R|<q` has labelled full-token cost below

\[
(p+1)(h-1)q,
\]

and all chosen minimum rollback footprints for `E_*` have total labelled cost at
most

\[
\boxed{(p+1)(h-1)t^2}.
\]

If a candidate family was clean in `G`, every member appearing after rollback
uses a restored edge. For a clean harmonic packet of weight `W`, rollback
creates at most

\[
\boxed{2(t-1)^2W|R|}
\]

represented triples.

Common-epoch existence and the numerical token/packet price are closed. Large
rollback is already strict host decomposition. The live temporal obstruction is
therefore qualitative conversion of the **cheap** restored-edge support.

### Remaining theorem

A complete fixed-envelope prime-power termination theorem must now provide at
least one of:

- a theorem converting a small rollback footprint into destroyed target load or
  protected-reserve depletion;
- a prefix, line-clean, Hall, or envelope continuation forced by concentration
  of many minimum rollback footprints on one deleted edge;
- a theorem converting a large reachability antichain into Hall decomposition,
  p-adic/carry concentration, or envelope expansion;
- or a canonical monotone payment converting repeated local ancestor resets into
  deletion, rollback, reserve depletion, or new geometric structure.

Another raw state, edge, link, cycle, or rollback-count estimate will not close
the argument; those quantities are already polynomial or linear, and expensive
rollback already factors the host.

## Bottleneck 4: low primitive heights

Generic pair-codegree estimates remain too weak at low height. The branch has:

- common first-separation depth and projective direction;
- full-prefix heavy/dispersion alternatives;
- exact row-token and full-token inventories;
- exact token line universes and tunable deep-token batches;
- universal line-clean paid-pair banks;
- quotient and carry collateral ledgers.

The open task is to feed these local alternatives into rollback-support or
exchange-antichain geometry rather than prove another isolated extraction lemma.

## Bottleneck 5: all side lengths

The prime-power programme now supplies nonlinear full channels at every odd
prime power, balanced recursive banks for every `p=1 mod 4` and every power of
seven, exact high-slice and harmonic-packet cleaning, and polynomial dynamic
accounting through sparse rollback.

Arbitrary `n` still requires a separate coverage mechanism: further balanced
prime factorizations, controlled products, CRT absorption, or patching between
nearby admissible sizes.

## Current proved endpoint

The following broad pieces are closed:

1. generic recursive first-separation summation;
2. prefix and joint-parent collateral;
3. global-baseline contraction and exact root escapes;
4. Hall-wall peeling and acyclic exchange ancestry;
5. exact high-slice cleaning and universal sharp-blocker line-clean banks;
6. deep-token batching and tunable heavy/dispersion thresholds;
7. exact harmonic-packet completion of all relevant intermediate bands;
8. exact one-pass prefix, packet, whole-parent, and joint-parent return costs;
9. exact selected-state cycle erasure;
10. polynomial edge-incidence payment for distinct-state expansion;
11. corrected entering-edge support and harmonic bounds for packet recreation;
12. deletion-or-forced-ancestry response for every lossy packet reset;
13. essentiality persistence and polynomial completion-or-terminal-ancestry
    packet scheduling;
14. polynomial distinct node and link bounds for the essential-core ancestry
    ledger;
15. exact directed exchange corridors, Dilworth batch-cycle covers, and linear
    temporal cycle compression;
16. sparse common-epoch rollback for every final essential edge;
17. minimum rollback essential-core factorization and threshold
    cost-or-dimension reduction;
18. exact rollback full-token and harmonic-packet payment.

## Open lemmas in recommended order

1. **Cheap rollback conversion.** Use the restored matching support to force
   target-load destruction, reserve depletion, prefix/line-clean repair, Hall
   decomposition, or envelope expansion.
2. **Rollback concentration conversion.** If many minimum rollback footprints
   use one deleted edge, exploit the associated earlier deletion certificate and
   its p-adic/carry signature.
3. **Exchange-antichain conversion.** Turn a large CMR437 antichain into Hall
   decomposition, prefix/carry concentration, or envelope expansion.
4. **Repeated local ancestor-state payment.** Attach a canonical rollback or
   deletion class to compatible prefix ancestor resets.
5. **Low-height carry integration.** Convert carry alternatives into the same
   rollback, exchange, deletion, or envelope budget.
6. **Prime-field transfer.** Rebuild the inherited-envelope and exact-covering
   endpoint for complementary-hyperbola carry cycles.
7. **Further balanced prime families.** Extend the prime-seven factorization or
   prove structural obstructions.
8. **Square-root divisor boundary.** Remove or sum the nearly singular terms in
   CMR61 and CMR64.
9. **CRT and arbitrary-size assembly.** Control mixed projections and patch
   between admissible side lengths.

## Computational priorities

- Enumerate minimum rollback footprints for exact terminal hosts and classify
  their full-token, primitive-height, quotient, and carry signatures.
- Test whether rollback footprints concentrated on one deleted edge reproduce a
  Hall wall, line-clean bank, or envelope-expansion certificate.
- Enumerate CMR216 corridor antichains by the same signatures.
- Test local ancestor-reset potentials against the CMR350 exact return cycle.
- Search for further non-reciprocal balanced grid factorizations.
- Continue the `N=14` and joint digital searches.

There is still no complete proof of the no-three-in-line conjecture.
