# Live composite-modulus theorem ledger continuation 5

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `composite-modulus-theorem-index-live-continuation-3.md` through CMR1629;
- `composite-modulus-theorem-index-live-continuation-4.md` through CMR1829; and
- this file from CMR1830 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR1830--1837 | Occupancy moments, uniform background-height compiler, exact height-layer identity, maximum line-occupancy distributions, third-moment distributions, denominator-specific side-four/five moment tables, and the occupancy-moment endpoint | PROVED; all 740 raw hosts, 89,664 host-line capacities, 1,188,144 response-line comparisons, 5,180 uniform-height bounds and 5,180 exact height-layer identities checked | `docs/332-prime-power-geometric-fibre-occupancy-moment-census.md` |
| CMR1838--1845 | Label linearization, weighted nested peeling, one weighted outer score, row Lyapunov criterion, simultaneous rational dual LP, rational/integer certificates, SCC/auxiliary assembly, and the labelled-LP endpoint | PROVED; 600 labelled systems, 4,645 response bounds, 4,645 label-linearization and outer-assignment checks, 600 rational duals and 600 denominator clearings checked | `docs/333-prime-power-label-weighted-unified-assignment-lp.md` |
| CMR1846--1853 | Full-length line classification, zero main-diagonal capacity, even and odd anti-diagonal laws, odd-side sharp construction, exact line-length occupancy census, side-four/five anti-diagonal distributions, and the diagonal-parity endpoint | PROVED; full-line classification through side twelve, parity checks through side eight, 28 odd-side constructions and all 89,664 raw host-line capacities checked | `docs/334-prime-power-diagonal-parity-line-occupancy-census.md` |
| CMR1854--1861 | Moment dominance, exact denominator-preserving Pareto compression, integer-height active envelopes, terminal phases, line-length-stratified moment bounds, exact signature counts, and the Pareto-envelope endpoint | PROVED; all 740 hosts and 89,664 line capacities, 740 moment-dominance checks, exact active phases and terminal certificates, and 740 length-signature dominance checks | `docs/335-prime-power-geometric-fibre-moment-pareto-envelopes.md` |
| CMR1862--1869 | Integer weighted coefficient aggregation, extendability-complete manifest surface, rank-two and rank-three dual checks, unified outer row check, global manifest theorem, gauge normalization, and the executable checker endpoint | PROVED; complete built-in labelled manifest accepted and twelve independently corrupted manifests rejected by exact integer arithmetic | `docs/336-prime-power-labelled-assignment-certificate-manifest.md` |
| CMR1870--1877 | Exact residual rank-three budget, side-four/five slack distributions, denominator-localized strict/critical/excess classes, automatic scalar elimination, exceptional-host localization, slack-aware outer score, and the rank-three slack endpoint | PROVED; all 740 raw hosts and 9,260 response occurrences classified, with exact residual-budget checks | `docs/337-prime-power-rank-three-fibre-slack-classification.md` |
| CMR1878--1885 | Exact response-averaged line moments, complete line-energy numerator, global pair/triple identities, rook-marginal equivalence, occupancy domination, exact uniform-height envelopes, Pareto/terminal census, and the averaged-line endpoint | PROVED; all 740 hosts, 89,664 host-line moment triples, 1,188,144 response-line occurrences, 537,984 exact line-height identities, 740 global identities, 103 Pareto triples and 48 active triples checked | `docs/338-prime-power-exact-response-averaged-line-moment-census.md` |
| CMR1886--1893 | Exact residual geometric numerator, strict rank-three line budget, line-budget allocation, one-line residual criterion, load-one and load-two censuses, weighted labelled allocation, and the line-budget endpoint | PROVED; all 740 hosts, 651 strict hosts, 80,602 strict host-line pairs and 106,810 exact active-line budget equivalences checked | `docs/339-prime-power-rank-three-slack-line-budget-allocation.md` |
| CMR1894--1901 | Primitive geometric witness sets, extendability-complete routing, rank-one/two/three route conservation, integer coefficient export, corrected-row fate requirement, and the executable routing-checker endpoint | PROVED; 500 deterministic random systems containing 6,063 primitive witnesses accepted and ten corrupted manifests rejected | `docs/340-prime-power-geometric-candidate-routing-manifest.md` |
| CMR1902--1909 | Unique absolute last-entering owner, exact owner partition, owner-preserving recurrent routes, owner-support closure, total witness fate partition, structural transfer surface, exact coefficient export, and the executable owner/fate endpoint | PROVED; 400 deterministic systems containing 5,586 witnesses accepted with exact fate counts, and eleven corrupted manifests rejected | `docs/341-prime-power-geometric-owner-fate-manifest.md` |
| CMR1910--1917 | Canonical source serialization, exact denominator inheritance, source/export coefficient equality, omission/addition exclusion, transparent domination multiplicity, source fingerprint linkage, composition with the assignment certificate, and the executable bundle endpoint | PROVED; 300 deterministic bundles containing 4,072 source witnesses, 3,125 exact bins and 4,138 exported coefficient units accepted, and ten corrupted bundles rejected | `docs/342-prime-power-geometric-assignment-bundle.md` |
| CMR1918--1925 | Exact destroyed-current-triple reconstruction, surviving-background linkage, unique deletion evidence, injective credit reservation, responsewise cancellation, unused destruction credit, strict average/uniform criteria, and the executable cancellation endpoint | PROVED; 300 deterministic systems containing 3,761 witnesses, 832 deleted witnesses, 1,304 destroyed triples, 472 unused credits and 2,310 responsewise inequalities checked; ten corrupted manifests rejected | `docs/343-prime-power-destroyed-triple-cancellation-manifest.md` |
| CMR1926--1933 | Common cancellation/coefficient source identity, exact exported response numerator, average and uniform destruction-credit slacks, strictness criteria, integration with exact/nested assignments, and the executable composed endpoint | PROVED; 300 deterministic systems containing 3,717 witnesses, 1,766 deleted witnesses, 1,881 unused credits and 4,557 exported numerator units checked; 129 average-strict and 105 uniform-strict systems; ten corruptions rejected | `docs/344-prime-power-cancellation-certified-assignment-bundle.md` |

The branch still does not prove the all-`n` conjecture.

## Current exact certificate surfaces

### Exact response-averaged line moments

For every host and nonaxis line,

\[
z_r(G,\ell)
=
\sum_{Q\in\operatorname{PM}(G)}
\binom{|Q\cap\ell|}{r},
\qquad r=1,2,3.
\]

For background line loads `h_ell`, the exact uniform-response numerator is

\[
A_G(B)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
 +z_3(G,\ell)
\right].
\]

The identities

\[
\sum_\ell z_2(G,\ell)=Z(G)\binom d2,
\qquad
\sum_\ell z_3(G,\ell)=A_3(G)
\]

fix the total rank-two and rank-three moments.

### Rank-three slack

On a rank-three-strict host,

\[
S_3(G)=Z(G)-A_3(G)>0,
\]

and the retained background-dependent geometric numerator is strict whenever

\[
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)+h_\ell z_2(G,\ell)
\right]
\le S_3(G)-1.
\]

There are 651 strict hosts, 44 critical hosts and 45 excess hosts.

### Primitive witnesses, owners and total fates

The raw source reconstructs every rank-one, rank-two and rank-three primitive
witness. A strict total order on extendable response edges gives

\[
\operatorname{own}(w)=\max_\prec P(w).
\]

Every witness has exactly one fate: retained, deleted, transferred or dominated.
Recurrent retained/dominated routes preserve the exact owner. The source exports
one labelled integer table `c^(r)_j(P)`, and the downstream coefficient bundle must
equal this table exactly.

### Destroyed-triple cancellation

Let `P` be the exact pre-response point set and `R` the removed subset. The exact
current triples destroyed by removal are

\[
\mathcal D(P,R)
=
\{T\in\binom P3:T\text{ collinear and }T\cap R\ne\varnothing\}.
\]

An accepted cancellation manifest injects every deleted primitive witness into a
distinct member of `\mathcal D(P,R)`. If `C` is the reserved image, put

\[
U=|\mathcal D(P,R)|-|C|.
\]

For every response,

\[
\boxed{N_{\rm raw}(Q)-|\mathcal D(P,R)|\le B(Q)-U,}
\]

where `B(Q)` is the accepted nondeleted/dominated export score.

With

\[
A_B=\sum_QB(Q),
\qquad M_B=\max_QB(Q),
\]

the exact strict criteria are

\[
\boxed{A_B<ZU}
\]

for existence of an improving response, and

\[
\boxed{M_B<U}
\]

for every response to improve. Any proved numerator upper bound `L` may replace
`A_B`; in nested assignment currency it is enough that

\[
6l_1+3l_2+l_3<6ZU.
\]

### Publication-grade labelled certificate

After geometric source, fate evidence, cancellation and coefficient handoff are
verified, the downstream integer assignment manifest stores all labelled
coefficients, contracted duals, one unified outer dual and positive row slacks.
Passing every recurrent row proves `AX<X` for the declared exact or honest upper
table.

## Active frontier

1. Generate the actual pre-response point sets, removed subsets, surviving
   backgrounds and strict entry orders for the 740 raw hosts.
2. Reconstruct the true destroyed-current-triple sets and use injective cancellation
   for every deletion fate that is genuinely paid by potential destruction.
3. Attach and verify owner, collision, local-line, interface, root, thin and CRT
   semantics for every nondeleted witness.
4. On the 651 rank-three-strict hosts, combine `S_3-1` and any unused destruction
   credit `U` with exact averaged line, return and selector coefficients.
5. On the 89 critical/excess hosts, build explicit corrected fate maps, nonuniform
   child weights, finer state splits or certified off-diagonal/auxiliary transfers.
6. Export accepted cancellation-certified bundles to the integer assignment checker,
   solve all recurrent rows, eliminate certified auxiliaries and publish the global
   integer quotient before CRT gluing.
