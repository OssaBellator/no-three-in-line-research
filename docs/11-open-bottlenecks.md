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

The inherited escape problem is no longer missing a local bank, packet
construction, packet termination statement, or polynomial ancestry-width bound.
The principal fixed-envelope obstruction is geometric use of the polynomial
exchange-link family and the analogous payment for repeated local ancestor
resets.

## Bottleneck 3: selected-state and ancestry dynamics

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

### Polynomial essential-core ledger

Let `E_*` be the final essential set of the deletion pass. CMR429--CMR432 give

\[
|E_*|\le t,
\]

and after identifying certificates with the same prescribed edge set,

\[
\#\{\text{forced rank-}1/2/3\text{ certificates}\}
\le
\binom t1+\binom t2+\binom t3
<t^3+t,
\]

while the total number of distinct CMR217 links is below

\[
\binom t1+2\binom t2+3\binom t3
<3t^3.
\]

Thus raw ancestry width and factorial certificate proliferation are closed.

### Remaining theorem

A complete fixed-envelope prime-power termination theorem must now provide at
least one of:

- a low-overlap extraction theorem for the polynomial CMR216 exchange-cycle
  family, followed by simultaneous flips;
- a high-overlap theorem forcing concentration on one p-adic, primitive-height,
  quotient, or carry signature;
- a theorem that concentrated exchange ancestry forces strict host
  decomposition or envelope expansion;
- or a monotone payment converting repeated local ancestor resets into deletion,
  reserve depletion, envelope expansion, or new geometric structure.

Another raw node, link, or per-reset count will not close the argument; those
counts are already polynomial and exact at the required level.

## Bottleneck 4: low primitive heights

Generic pair-codegree estimates remain too weak at low height. The branch has:

- common first-separation depth and projective direction;
- full-prefix heavy/dispersion alternatives;
- exact row-token and full-token inventories;
- exact token line universes and tunable deep-token batches;
- universal line-clean paid-pair banks;
- quotient and carry collateral ledgers.

The open task is to feed these local alternatives into exchange-cycle overlap or
repeated-ancestor payment rather than prove another isolated extraction lemma.

## Bottleneck 5: all side lengths

The prime-power programme now supplies nonlinear full channels at every odd
prime power, balanced recursive banks for every `p=1 mod 4` and every power of
seven, exact high-slice and harmonic-packet cleaning, and polynomial dynamic
accounting through the ancestry ledger.

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
    ledger.

## Open lemmas in recommended order

1. **Exchange-cycle overlap dichotomy.** Extract many low-overlap CMR216 cycles
   or force concentration on a bounded geometric/p-adic signature.
2. **Simultaneous exchange resampling.** Turn a low-overlap cycle family into one
   executable move eliminating several forced certificates.
3. **Concentrated-ancestry conversion.** Turn high overlap into prefix repair,
   line-clean continuation, host decomposition, or envelope expansion.
4. **Repeated local ancestor-state payment.** Extend the packet deletion/
   ancestry mechanism to compatible prefix ancestor resets.
5. **Low-height carry integration.** Convert carry alternatives into the same
   exchange, deletion, or envelope budget.
6. **Prime-field transfer.** Rebuild the inherited-envelope and exact-covering
   endpoint for complementary-hyperbola carry cycles.
7. **Further balanced prime families.** Extend the prime-seven factorization or
   prove structural obstructions.
8. **Square-root divisor boundary.** Remove or sum the nearly singular terms in
   CMR61 and CMR64.
9. **CRT and arbitrary-size assembly.** Control mixed projections and patch
   between admissible side lengths.

## Computational priorities

- Enumerate CMR216 cycle overlaps by full-token and primitive-height signature.
- Search for large edge-disjoint or bounded-overlap exchange-cycle families.
- Test concentrated-cycle signatures against prefix and envelope continuations.
- Test local ancestor-reset potentials against the CMR350 exact return cycle.
- Search for further non-reciprocal balanced grid factorizations.
- Continue the `N=14` and joint digital searches.

There is still no complete proof of the no-three-in-line conjecture.
