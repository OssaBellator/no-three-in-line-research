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
8. CMR422--CMR425 show that inside a certificate-directed deletion pass every
   lossy packet reset pays a permanent deletion or one fully forced ancestry
   event. Permanent deletion responses occur at most `t(t-1)` times.

The inherited escape problem is no longer missing a local bank, packet
construction, state-cycle lemma, recreation support theorem, or finite packet
loss response. The principal fixed-envelope obstruction is now the width of
fully forced exchange ancestry and the analogous payment for repeated local
ancestor resets.

## Bottleneck 3: selected-state dynamics

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

### Distinct-state payment

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

Thus factorial state space is no longer the quantitative endpoint.

### Correct packet recreation orientation

If `M` is clean for a packet and `M'` recreates one of its triples, the triple
contains an entering edge of `M'\setminus M`. The leaving set `M\setminus M'`
is returned to the complementary available host and has the same size. Hence
for packet weight `W`, the number of recreated triples is at most

\[
\boxed{2(t-1)^2W|M\setminus M'|}.
\]

The earlier numerical packet-recreation bounds remain correct; only the edge
orientation required correction.

### Deletion-or-ancestry response

Use the first-dirty packet order inside one certificate-directed deletion pass.
After a lossy reset, choose one lost packet and one recreated triple. CMR422
says:

1. a nonessential edge of that triple can be deleted while preserving a perfect
   matching; or
2. all three edges are essential, producing a fully forced CMR217 certificate
   with backward exchange ancestry.

If `P` is the packet count, `F` the number of fully forced packet events, and
`T` the number of packet installations, then

\[
\boxed{
T\le P\bigl(1+t(t-1)+F\bigr).
}
\]

If every earlier deletion certificate receives at most `w` incoming links from
fully forced packet events, then

\[
\boxed{
T\le P\bigl(1+(1+w)t(t-1)\bigr).
}
\]

Therefore packet scheduling no longer needs a separate global churn potential.
Its exact unresolved quantity is incoming ancestry width.

### Remaining theorem

A complete fixed-envelope prime-power termination theorem must now provide at
least one of:

- an incoming-width bound for CMR217 ancestry by full-token, primitive-height,
  quotient, or carry signature;
- a simultaneous alternating-cycle resampling theorem for several forced
  certificates;
- or a monotone payment which converts repeated local ancestor resets into
  deletion, envelope expansion, reserve depletion, or new bounded ancestry.

Another raw per-reset edge-count estimate will not close the argument; those
estimates are already exact at the required scales.

## Bottleneck 4: low primitive heights

Generic pair-codegree estimates remain too weak at low height. The branch has:

- common first-separation depth and projective direction;
- full-prefix heavy/dispersion alternatives;
- exact row-token and full-token inventories;
- exact token line universes and tunable deep-token batches;
- universal line-clean paid-pair banks;
- quotient and carry collateral ledgers.

The open task is to feed these local alternatives into the ancestry-width or
ancestor-reset payment rather than prove another isolated extraction lemma.

## Bottleneck 5: all side lengths

The prime-power programme now supplies nonlinear full channels at every odd
prime power, balanced recursive banks for every `p=1 mod 4` and every power of
seven, exact high-slice and harmonic-packet cleaning, and polynomial one-pass
dynamic accounting.

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
13. reduction of packet installation length to the incoming width of fully
    forced ancestry.

## Open lemmas in recommended order

1. **Forced-ancestry incoming width.** Bound how many fully forced packet or
   local certificates can point to one earlier deleted certificate at a fixed
   p-adic or primitive-height signature.
2. **Simultaneous exchange resampling.** Use edge-disjoint or low-overlap
   alternating cycles to eliminate several forced certificates at once.
3. **Repeated local ancestor-state payment.** Extend CMR422 to compatible prefix
   ancestor resets not arising from harmonic packet loss.
4. **Low-height carry integration.** Convert carry alternatives into the same
   ancestry or deletion budget.
5. **Prime-field transfer.** Rebuild the inherited-envelope and exact-covering
   endpoint for complementary-hyperbola carry cycles.
6. **Further balanced prime families.** Extend the prime-seven factorization or
   prove structural obstructions.
7. **Square-root divisor boundary.** Remove or sum the nearly singular terms in
   CMR61 and CMR64.
8. **CRT and arbitrary-size assembly.** Control mixed projections and patch
   between admissible side lengths.

## Computational priorities

- Enumerate incoming exchange-ancestry counts by full-token and primitive-height
  signature.
- Search for low-overlap families of CMR216 alternating cycles supporting
  simultaneous flips.
- Test local ancestor-reset potentials against the CMR350 exact return cycle.
- Search for packet states whose entering edges avoid earlier packet supports.
- Search for further non-reciprocal balanced grid factorizations.
- Continue the `N=14` and joint digital searches.

There is still no complete proof of the no-three-in-line conjecture.
