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

The global identities

\[
\sum_\ell z_2(G,\ell)=Z(G)\binom d2,
\qquad
\sum_\ell z_3(G,\ell)=A_3(G)
\]

fix the total rank-two and rank-three moments.  Only the rank-one incidence
numerator varies freely.

### Rank-three slack as an exact line budget

On a rank-three-strict host,

\[
S_3(G)=Z(G)-A_3(G)>0.
\]

The remaining geometric numerator

\[
R_G(h)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
\right]
\]

is strict exactly when

\[
\boxed{R_G(h)\le S_3(G)-1.}
\]

There are 651 strict hosts, 44 critical hosts and 45 excess hosts.

### Primitive witnesses and absolute owners

The raw candidate source reconstructs every primitive witness:

- rank one: a response edge and one collinear unordered background pair;
- rank two: a compatible response pair and one collinear background point;
- rank three: one collinear response triple.

A strict total order on extendable response edges gives the unique owner

\[
\operatorname{own}(w)=\max_\prec P(w).
\]

The owner/fate manifest requires every raw witness exactly once and assigns one
explicit fate:

1. retained in the same recurrent owner class;
2. deleted with a correction-evidence identifier;
3. transferred to a lower-stratum off-diagonal or auxiliary child; or
4. dominated by an explicit positive upper multiplicity in the same owner class.

No accepted manifest can silently omit a witness.  The checker validates owner and
fate syntax, but rule-specific verifiers must prove deletion, domination and
auxiliary-transfer evidence.

### Exact geometric-to-assignment handoff

The owner/fate source exports one integer table

\[
c^{(r)}_j(P).
\]

A downstream bundle carries the source inline, its canonical SHA-256 fingerprint,
the exact denominator

\[
D=|\operatorname{PM}(G)|,
\]

and the labelled edge, pair and triple table.  Acceptance requires exact equality
with the recomputed source export.  Thus there is no unchecked coefficient
conversion between primitive geometry and the assignment LP.

### Publication-grade labelled certificate

After source and fate evidence are verified, the downstream integer assignment
manifest retains state weights, all labelled coefficients, complete contracted
dual families, one unified outer dual and one positive integer row slack.  Passing
every row proves `AX<X` for the declared exact or componentwise upper table.

## Active frontier

1. Generate the actual 740-host background-point manifests and strict entry orders.
2. Attach the correct owner, collision, local-line, interface, root, thin and CRT
   state semantics to every primitive witness.
3. Prove every nonretained fate using rule-specific correction, domination,
   structural-transition or auxiliary-module verifiers.
4. On the 651 rank-three-strict hosts, allocate `S_3-1` across all retained line,
   return and selector coefficients using exact response-averaged moments.
5. On the 89 critical/excess hosts, construct explicit corrected fate maps,
   nonuniform child weights, finer state splits or certified off-diagonal transfers.
6. Export accepted owner/fate bundles to the integer assignment checker, solve all
   recurrent rows, eliminate certified auxiliaries and publish the global integer
   quotient before CRT gluing.
