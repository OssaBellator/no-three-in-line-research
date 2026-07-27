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

The branch still does not prove the all-`n` conjecture.

## Current exact certificate surfaces

### Exact response-averaged line moments

For every host and nonaxis line, define

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

The global identities are

\[
\sum_\ell z_2(G,\ell)=Z(G)\binom d2,
\qquad
\sum_\ell z_3(G,\ell)=A_3(G).
\]

Thus the global pair moment is fixed by side and denominator, while the triple
moment is the completed rank-three census.  Exact line moments are always at most
the corresponding occupancy-capacity numerators.

For a uniform height cap `H`, exact averaged moment triples compress to 13 Pareto
triples on side four and 90 on side five.  Only 48 are active for an integer `H`.
Every exact averaged side-four envelope is terminal by `H=2`, and every side-five
envelope is terminal by `H=4`.

### Rank-three slack as an exact line budget

On a rank-three-strict host,

\[
S_3(G)=Z(G)-A_3(G)>0.
\]

The remaining exact geometric numerator is

\[
R_G(h)
=
\sum_\ell
\left[
 \binom{h_\ell}{2}z_1(G,\ell)
 +h_\ell z_2(G,\ell)
\right],
\]

and the complete scalar geometric row is strict exactly when

\[
\boxed{R_G(h)\le S_3(G)-1.}
\]

Equivalently, each line may receive a nonnegative integer budget and the budget
total must not exceed `S_3-1`.

Across the 651 strict hosts:

| profile | active host-line pairs | individually fitting `S_3-1` | hosts with at least one fitting active line | hosts whose every active line fits |
|---|---:|---:|---:|---:|
| load one | 34,618 | 27,192 | 594 | 26 |
| load two | 72,192 | 16,838 | 492 | 0 |

Individual fits become complete row certificates only when all other retained
line contributions are separately budgeted, corrected or routed away.

### Geometric candidate-source manifest

For each extendable prescription, the raw geometric checker enumerates primitive
witnesses rather than only aggregate multiplicities:

- rank one: every unordered background pair collinear with the response edge;
- rank two: every background point collinear with the response pair;
- rank three: the unique primitive witness for every collinear response triple.

Every witness must occur exactly once with a declared child label.  Aggregation by
`(rank,child,prescription)` exports the exact geometric coefficient table for the
integer assignment manifest.

`scripts/check_geometric_candidate_routing_manifest.py` recomputes response
matchings, extendability, collinearity and witness conservation.  It validates raw
candidate completeness but does not prove that a declared child-label string has
the correct owner, collision, interface or CRT semantics.

### Publication-grade labelled certificate

The downstream integer manifest retains state weights, all labelled edge/pair/
triple coefficients, complete contracted dual families, one unified outer dual
and one positive integer row slack.  Passing every row proves `AX<X` relative to
the declared exact or componentwise upper table.

A corrected or upper offspring table must provide an explicit fate for every raw
geometric witness: retained, deleted by a verified rule, transferred to a
separately certified state, or honestly dominated.  Silent deletion is invalid.

## Active frontier

1. Generate the actual background-point, owner and provenance routing manifests
   for the 740 raw hosts and verify raw witness conservation.
2. Use exact response-averaged line moments in place of occupancy maxima whenever
   the response law is uniform; retain occupancy capacities only as a fallback.
3. On the 651 rank-three-strict hosts, allocate the exact `S_3-1` budget across
   return, selector and all retained line coefficients.
4. On the 89 critical/excess hosts, record an explicit correction, nonuniform
   child-weight route, finer state split or certified off-diagonal transfer for
   every raw witness.
5. Export the routed coefficients to the integer assignment manifest and generate
   all inner, middle and unified outer duals.
6. Certify thin, fixed-interface and reused-support modules, eliminate them through
   exact resolvents, then finish the collision/local-line SCCs and publish the
   global integer quotient before CRT gluing.
