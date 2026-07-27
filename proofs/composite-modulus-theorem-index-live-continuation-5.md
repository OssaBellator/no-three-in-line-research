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

The branch still does not prove the all-`n` conjecture.

## Current exact certificate surfaces

### Pareto-compressed background-height envelopes

For every host,

\[
M_r(G)=\sum_\ell\binom{\tau_G(\ell)}r,
\qquad r=1,2,3.
\]

For a uniform background height `H`,

\[
F_H(G)=\binom H2M_1(G)+HM_2(G)+M_3(G).
\]

The 740 raw hosts compress denominator-by-denominator to 69 Pareto triples, and
only 57 triples are ever maximal for an integer `H`.  Every side-four envelope is
terminal by `H=4`; every side-five envelope is terminal by `H=16`.

If the height cap depends on line length `L`, use

\[
\sum_L\left[
 \binom{H_L}{2}M_{1,L}(G)
 +H_LM_{2,L}(G)
 +M_{3,L}(G)
\right].
\]

The exact denominator-preserving length-stratified table has 20 side-four and 225
side-five Pareto signatures.

### Rank-three slack split

For every raw host, put

\[
S_3(G)=Z(G)-A_3(G).
\]

The exact split is:

| class | side four | side five | total |
|---|---:|---:|---:|
| `S_3>0` | 53 | 598 | 651 |
| `S_3=0` | 6 | 38 | 44 |
| `S_3<0` | 27 | 18 | 45 |

On a strict host, the exact residual scalar numerator budget after rank three is

\[
B\le S_3-1.
\]

Thus only 89 raw hosts require special rank-three correction or weighted routing;
the other 651 provide an explicit budget for shorter-line and return-selector
terms.

### Publication-grade labelled certificate

For integer state weights `X_j`, aggregate declared labelled coefficient numerators
before peeling.  Row `i` has sixfold outer score

\[
\Theta_i(e)=6q_i(e)+3j_{2,i}(e)+h_{3,i}(e).
\]

A manifest stores every inner and middle dual, one outer dual and a positive slack
`delta_i`.  The exact row check is

\[
U_{i,u}+V_{i,v}\ge\Theta_i((u,v))
\]

and

\[
\sum_uU_{i,u}+\sum_vV_{i,v}
\le
6D_iX_i-\delta_i.
\]

The standalone checker recomputes host extendability, validates all coefficient and
dual surfaces and accepts only complete recurrent blocks.  Passing every row gives
`AX<X` and a denominator-cleared integer certificate.

## Active frontier

1. Attach actual background-height, owner and provenance classes to the 740 raw
   hosts and map each class to an exact marginal, a 57-vector uniform envelope or
   a 245-signature line-length envelope.
2. Prioritize the 89 rank-three critical/excess hosts; on the other 651, spend the
   exact `S_3-1` residual budget on return, selector and shorter-line terms.
3. Populate the integer certificate manifest with the true labelled edge, pair and
   triple coefficients and generate all inner, middle and outer duals.
4. Produce strict row certificates for every surviving thin, fixed-interface and
   reused-support state.
5. Eliminate certified auxiliary modules through exact rational resolvents.
6. Certify the remaining collision/local-line SCCs, clear all denominators and
   publish the global integer quotient before CRT gluing.
