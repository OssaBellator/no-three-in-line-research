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
   of distinct feasible states pays returned-edge and full-token incidence mass.
7. CMR418--CMR421 prove that every recreated old-packet conflict contains a
   returned edge and reduce the first-dirty packet schedule to cumulative churn.

The inherited escape problem is no longer missing a local bank, packet
construction, state-cycle lemma, or recreation support theorem. It is a global
churn and forced-ancestry problem.

## Bottleneck 3: the global churn variable

For a full token

\[
\tau=(b,a,c,\theta),
\]

one recursive ancestor reset returns at most `t/p^b` token edges, and one
one-layer whole-parent reset has the same bound. Exact incidence accounting gives
much sharper aggregate estimates than tokenwise summation.

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
mask, the returned set is exactly `M\setminus M'` and has at least two edges.
Consequently a cycle-erased history with `L` selected states and labelled mass
`I` satisfies

\[
\boxed{
L
\le
1+rac{I}{2(p+1)(h-1)}.
}
\]

Thus factorial state space is no longer the quantitative endpoint.

### Packet recreation payment

If a host is clean for a packet and a reset returns `R`, every recreated packet
triple contains an edge of `R`. For packet weight `W`, the number of recreated
triples is at most

\[
\boxed{2(t-1)^2W|R|}.
\]

For packets with total harmonic weight `W_*`, cumulative churn

\[
C=\sum_j|R_j|
\]

and a first-dirty schedule of length `T`,

\[
\boxed{
T
\le
P+2(t-1)^2W_*C.
}
\]

Exact cycles, distinct-state expansion, and packet loss are therefore paid by
one common variable: cumulative returned-edge churn.

### The remaining theorem

A complete prime-power termination theorem must now provide at least one of:

- a global upper bound on `C` from destroyed target load;
- a reserve or envelope potential which decreases whenever churn is created;
- a protected-packet rule restricting the old edges vacated by later resets;
- or a theorem converting excess churn into bounded-width fully forced exchange
  ancestry and simultaneous resampling.

Another raw per-reset estimate will not close the argument; those estimates are
already exact at the required scales.

## Bottleneck 4: low primitive heights

Generic pair-codegree estimates remain too weak at low height. The branch has:

- common first-separation depth and projective direction;
- full-prefix heavy/dispersion alternatives;
- exact row-token and full-token inventories;
- exact token line universes and tunable deep-token batches;
- universal line-clean paid-pair banks;
- quotient and carry collateral ledgers.

The open task is to feed these local alternatives into the global churn or
ancestry potential rather than prove another isolated extraction lemma.

## Bottleneck 5: all side lengths

The prime-power programme now supplies nonlinear full channels at every odd
prime power, balanced recursive banks for every `p=1 mod 4` and every power of
seven, exact high-slice and harmonic-packet cleaning, and polynomial one-sweep
dynamic accounting.

Arbitrary `n` still requires a separate coverage mechanism: further balanced
prime factorizations, controlled products, CRT absorption, or patching between
nearby admissible sizes.

## Current proved endpoint

The following broad pieces are closed:

1. generic recursive first-separation summation;
2. prefix and joint-parent collateral;
3. global-baseline contraction and exact root escapes;
4. Hall-wall peeling and exchange ancestry;
5. exact high-slice cleaning and universal sharp-blocker line-clean banks;
6. deep-token batching and tunable heavy/dispersion thresholds;
7. exact harmonic-packet completion of all relevant intermediate bands;
8. exact one-pass prefix, packet, whole-parent, and joint-parent return costs;
9. exact selected-state cycle erasure;
10. polynomial returned-edge payment for distinct-state expansion;
11. returned-edge support and harmonic degree bounds for packet recreation;
12. reduction of first-dirty packet scheduling to cumulative churn.

## Open lemmas in recommended order

1. **Global churn potential.** Charge cumulative returned-edge churn to target
   load, envelope depth, or protected reserve depletion.
2. **Forced-ancestry conversion.** Show that excess churn forces bounded-width
   exchange ancestry or permits simultaneous cycle resampling.
3. **Protected-packet selection.** Incorporate restrictions on vacated old edges
   into the duplicated-row exact-covering theorem.
4. **Low-height carry integration.** Convert the carry alternatives into the same
   global churn/ancestry budget.
5. **Prime-field transfer.** Rebuild the inherited-envelope and exact-covering
   endpoint for complementary-hyperbola carry cycles.
6. **Further balanced prime families.** Extend the prime-seven factorization or
   prove structural obstructions.
7. **Square-root divisor boundary.** Remove or sum the nearly singular terms in
   CMR61 and CMR64.
8. **CRT and arbitrary-size assembly.** Control mixed projections and patch
   between admissible side lengths.

## Computational priorities

- Measure cumulative churn and packet-loss matrices for exact packet states.
- Test target-load, reserve, and envelope potentials against the CMR350 return
  cycle.
- Enumerate exchange-ancestry descendant counts by full-token signature.
- Search for exact packet coverings whose vacated old edges avoid earlier packet
  supports.
- Search for further non-reciprocal balanced grid factorizations.
- Continue the `N=14` and joint digital searches.

There is still no complete proof of the no-three-in-line conjecture.
