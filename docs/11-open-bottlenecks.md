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
14. CMR448--CMR452 identify rollback number with minimum assignment cost, exclude
    negative alternating cycles, and cut out a canonical layered tight host
    containing exactly all minimum rollback states.

The inherited escape problem is no longer missing a local bank, packet
construction, packet termination statement, polynomial ancestry ledger,
exchange-cycle cover, common-epoch avoiding matching, or canonical minimum-cost
rollback class. The principal fixed-envelope obstruction is now **geometric
structure of the tight rollback host**, together with exchange-antichain geometry
and the analogous normalization of repeated local ancestor resets.

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

Let `E_*` be the final essential set. CMR429--CMR432 give

\[
|E_*|\le t,
\]

fewer than `t^3+t` distinct forced rank-`1/2/3` edge-set certificates, and fewer
than `3t^3` distinct CMR217 links.

Fix a perfect matching `M` before deleting `f=\ell_ur_v`. Contract its matching
edges and orient every nonmatching edge `\ell_jr_k` as `j\to k`.
CMR433--CMR438 give:

1. nonessential matching edges are exactly directed-cycle vertices;
2. newly essential edges are acyclic vertices on a directed `v`-to-`u` corridor;
3. reachability on one layer is a partial order;
4. every chain lies on one exchange cycle through `f`;
5. the exact cycle-cover number is the poset width;
6. a layer of size `n` has either a batch of size `ceil(sqrt(n))` or an antichain
   of that size;
7. all first-essentiality edges in the pass are covered at their valid times by
   at most
   \[
   \sum_iw_i\le |E_*|\le t
   \]
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

CMR439--CMR443 give

\[
\boxed{1\le\kappa(e)\le t.}
\]

If `R` is minimum, every edge of `R` is essential in `G+R-e`, and

\[
\boxed{
\operatorname{PM}(G+R-e)
\cong
\{R\}\times
\operatorname{PM}\bigl((G+R-e)-V(R)\bigr).
}
\]

For every threshold `q`, either `\kappa(e)<q`, or the avoiding problem factors
to side at most `t-q`. Every terminal rank-`1/2/3` certificate is destroyed by
applying this to one prescribed edge. Choosing one minimum rollback set for each
edge of `E_*` gives

\[
\boxed{
\sum_{e\in E_*}|R_e|\le t^2.
}
\]

### Exact rollback payment

CMR444--CMR447 give, for every restored set `R`,

\[
\boxed{
\mathcal I(R)
=(p+1)(h-1)|R|.
}
\]

If a candidate family was clean in `G`, every member appearing after rollback
uses a restored edge. For a clean harmonic packet of weight `W`, rollback
creates at most

\[
\boxed{2(t-1)^2W|R|}
\]

represented triples.

### Canonical optimal rollback face

Give every edge of `\Delta` unit cost and every final-host edge zero cost in
`G_0-e`. CMR448 identifies

\[
\boxed{
\kappa(e)
=
\min\{|M\cap\Delta|:M\in\operatorname{PM}(G_0-e)\}.
}
\]

Fix a minimum-cost matching

\[
M=\{m_j=\ell_jr_j\}.
\]

For every nonmatching edge `\ell_jr_k`, assign contraction-arc weight

\[
w(j,k)=c(\ell_jr_k)-c(m_k)\in\{-1,0,1\}.
\]

CMR449--CMR452 prove:

1. every directed alternating cycle has nonnegative total weight;
2. every other minimum rollback matching differs from `M` by zero-weight
   alternating cycles only;
3. shortest-path potentials give nonnegative reduced arc weights;
4. the base matching plus the zero-reduced-cost edges forms a **tight host**
   whose perfect matchings are exactly all minimum rollback states;
5. the potentials are integral and may be chosen in
   \[
   -(t-1)\le\phi(j)\le0;
   \]
6. every tight arc satisfies
   \[
   \phi(k)-\phi(j)=w(j,k)\in\{-1,0,1\}.
   \]

Thus positive-cost rollback excursions can be discarded. The cheap branch is a
layered optimal matching face with at most `t` integer levels.

### Remaining theorem

A complete fixed-envelope prime-power termination theorem must now provide at
least one of:

- a theorem converting a large tight potential level or dense zero-cost
  component into target-load destruction, reserve depletion, prefix/line-clean
  continuation, Hall decomposition, or envelope expansion;
- a theorem that many unit level changes consume enough restored-edge or token
  budget to force progress;
- a conversion of rollback-footprint concentration on one deleted edge into the
  earlier certificate's p-adic/carry geometry;
- a conversion of a large reachability antichain into Hall decomposition,
  p-adic/carry concentration, or envelope expansion;
- or the same minimum-cost/tight-face normalization for repeated local ancestor
  resets.

Another raw state, edge, link, cycle, or rollback-count estimate will not close
the argument; those quantities are already polynomial or linear, expensive
rollback factors the host, and minimum rollback states already form one exact
optimal face.

## Bottleneck 4: low primitive heights

Generic pair-codegree estimates remain too weak at low height. The branch has:

- common first-separation depth and projective direction;
- full-prefix heavy/dispersion alternatives;
- exact row-token and full-token inventories;
- exact token line universes and tunable deep-token batches;
- universal line-clean paid-pair banks;
- quotient and carry collateral ledgers.

The open task is to feed these alternatives into tight-host level geometry,
rollback concentration, or exchange-antichain structure.

## Bottleneck 5: all side lengths

The prime-power programme now supplies nonlinear full channels at every odd
prime power, balanced recursive banks for every `p=1 mod 4` and every power of
seven, exact high-slice and harmonic-packet cleaning, and polynomial dynamic
accounting through a canonical optimal rollback face.

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
14. polynomial essential-core ancestry ledger;
15. exact directed exchange corridors and linear temporal cycle compression;
16. sparse common-epoch rollback for every final essential edge;
17. minimum rollback factorization and threshold cost-or-dimension reduction;
18. exact rollback full-token and harmonic-packet payment;
19. minimum-cost rollback characterization, no-negative-cycle optimality, exact
    tight-host equality, and integer rollback levels.

## Open lemmas in recommended order

1. **Tight-level geometry.** Classify large potential levels and zero-cost
   strongly connected components by full token, primitive height, quotient, and
   carry signature.
2. **Tight-host conversion.** Turn that classification into prefix/line-clean
   repair, Hall decomposition, reserve depletion, or envelope expansion.
3. **Rollback concentration conversion.** If many minimum footprints use one
   deleted edge, exploit its earlier deletion certificate.
4. **Exchange-antichain conversion.** Turn a large CMR437 antichain into Hall or
   p-adic/carry structure.
5. **Repeated ancestor normalization.** Define the corresponding binary edge cost
   and tight optimal face for compatible prefix ancestor resets.
6. **Low-height carry integration.** Convert carry alternatives into the same
   rollback, exchange, deletion, or envelope budget.
7. **Prime-field transfer.** Rebuild the inherited-envelope and exact-covering
   endpoint for complementary-hyperbola carry cycles.
8. **Further balanced prime families.** Extend the prime-seven factorization or
   prove structural obstructions.
9. **Square-root divisor boundary.** Remove or sum the nearly singular terms in
   CMR61 and CMR64.
10. **CRT and arbitrary-size assembly.** Control mixed projections and patch
    between admissible side lengths.

## Computational priorities

- Enumerate tight rollback hosts and potential levels for exact terminal hosts.
- Classify zero-cost components by full-token, primitive-height, quotient, and
  carry data.
- Test whether level concentration reproduces a Hall wall, line-clean bank, or
  envelope-expansion certificate.
- Apply the binary rollback-cost normalization to CMR350-style ancestor-return
  cycles.
- Search for further non-reciprocal balanced grid factorizations.
- Continue the `N=14` and joint digital searches.

There is still no complete proof of the no-three-in-line conjecture.
