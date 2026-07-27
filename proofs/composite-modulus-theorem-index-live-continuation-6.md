# Live composite-modulus theorem ledger continuation 6

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `composite-modulus-theorem-index-live-continuation-3.md` through CMR1629;
- `composite-modulus-theorem-index-live-continuation-4.md` through CMR1829;
- `composite-modulus-theorem-index-live-continuation-5.md` through CMR1997; and
- this file from CMR1998 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR1998--2005 | Exact side-four base response table, zero-response blocker criterion, three inclusion-minimal transversals, complete eleven-host blocker census, surviving positive-response classification, exact hard-core equivalence, and executable blocker endpoint | PROVED; six base responses split four zero and two positive; three minimal blockers generate exactly eleven canonical hosts with size distribution 3/6/2 and minimum distribution 9/2; ten corruptions rejected | `docs/353-prime-power-rank-three-zero-response-blockers.md` |
| CMR2006--2013 | Two selected hard-core responses, exact line support, selected-response occurrence-deletion minimum, 17-unit deterministic burden, 44-unit uniform comparison, 27-unit policy difference, two-host irreducible raw geometry, and executable correction endpoint | PROVED; eleven hosts split nine one-triple and two four-triple selectors on two exact lines; deterministic/uniform totals 17/44; ten corruptions rejected | `docs/354-prime-power-rank-three-hard-core-correction.md` |
| CMR2014--2021 | Injective allowed-edge host identification, host-ID and record-digest linkage, complete response-list equality, policy-separated response selection, mandatory parent label tuple, source/fibre identity, exact linkage claims, and executable fibre-linkage endpoint | PROVED; 300 linked fibres containing 3,815 response records and 4,096 witnesses accepted, split 150 canonical and 150 declared policies; twelve corruptions rejected | `docs/355-prime-power-raw-host-fibre-linkage.md` |
| CMR2022--2029 | Finite hard-core rollback, exact 10/1 distance split, unique distance-two host, 21 minimum options, restored zero-response and uniform-slack census, exact 12-unit independent rollback distance, policy separation from occurrence correction, and executable rollback endpoint | PROVED; ten hosts need one rollback edge and one needs two; 21 minimum options land in 13 restored hosts; restored slacks are 19 at -2 and 2 at -1; ten corruptions rejected | `docs/356-prime-power-rank-three-hard-core-rollback.md` |
| CMR2030--2037 | Canonical response-line records, exact rank-two and rank-three kernels, rank-one point kernel, complete line-incidence census, seven occupancy profiles, exact background response score, and executable kernel endpoint | PROVED; all 740 hosts and 9,260 responses produce 79,736 line records, 6,485 rank-three occurrences, 39 coordinate-labelled response geometries and seven profiles; ten corruptions rejected | `docs/357-prime-power-response-line-incidence-kernel.md` |
| CMR2038--2045 | Direct/kernel rank agreement, post-response identity, minimizer independence from removed prehistory, deterministic full selector, exact raw-selector penalty, instability criterion, deterministic stress census, and executable background-selector endpoint | PROVED; 400 systems with 5,077 responses and 1,260 background points checked; raw selector changes in 166 cases, has positive penalty in 160, total penalty 239; twelve corruptions rejected | `docs/358-prime-power-background-response-selector.md` |
| CMR2046--2053 | Finite response-line universe, absolute survivor-background signature, perfect-matching row/column gauge, reduced selector signature, exact rank-one reconstruction, exact affine score factorization, scalar signature equivalence, and executable signature endpoint | PROVED; side line universes 23/83, full dimensions 39/108, reduced selector dimensions 32/99; 500 systems, 6,166 response scores and 1,706 background points checked; twelve corruptions rejected | `docs/359-prime-power-survivor-background-signature.md` |
| CMR2054--2061 | Affine response rows, 39-row global library, exact host chamber criterion, integer polyhedral selector chambers, complete comparison census, exact selector reconstruction, deterministic chamber stress test, and executable chamber endpoint | PROVED; six side-four and 33 side-five rows, 125,448 host comparisons and 1,086 unique ordered row pairs; 5,876 chamber inequalities checked; twelve corruptions rejected | `docs/360-prime-power-affine-selector-chambers.md` |
| CMR2062--2069 | Exact source identity, survivor-background identity, responsewise operation composition, minimizer agreement, strict destroyed-threshold criterion, declared-policy penalty, deterministic composed suite, and executable linked-operation endpoint | PROVED; 240 linked operations, 2,944 responsewise identities, 3,363 witnesses, 589 destroyed triples and 230 strict full selectors checked; fourteen corruptions rejected | `docs/361-prime-power-linked-operation-selector.md` |
| CMR2070--2077 | Tracked-line pair partition, nonnegative residual realizability inequalities, Vandermonde line-cluster identity, exact residual score factorization, residual row/column gauge, residual signature equivalence, deterministic regression, and executable residual endpoint | PROVED; selector dimensions remain 32/99; 500 host/background systems check residual nonnegativity and responsewise equality; twelve corruptions rejected | `docs/362-prime-power-background-residual-signature.md` |
| CMR2078--2085 | Exact labelled response vectors, scalar coordinate-sum identity, duplicate-vector quotient, componentwise dominance pruning, strictly-positive weighted Pareto theorem, deterministic weighted selector, scalar/labelled policy separation, and executable Pareto endpoint | PROVED; 300 accepted owner/fate systems exercise exact vectors, duplicate quotients and positive-weight selectors; twelve corruptions rejected | `docs/363-prime-power-labelled-response-pareto.md` |
| CMR2086--2093 | Exact three-certificate entry linkage, canonical operation records, unique fibre ordering, reconstructed aggregate censuses, explicit expected-ID coverage, undeclared incompleteness, reloadable batch digest, and executable real-fibre batch endpoint | PROVED as an interface; 120 distinct accepted synthetic operations check incomplete and declared-complete modes; twelve corruptions rejected; no genuine population claimed | `docs/364-prime-power-real-fibre-batch-manifest.md` |

The branch still does not prove the all-`n` conjecture.

## Residual realizability structure

For each grid point `q`, let

\[
t_B(q)=\sum_{L\in L_s:q\in L}\binom{h_B(L)}2,
\qquad
u_B(q)=p_B(q)-t_B(q).
\]

Every genuine background satisfies `u_B(q)>=0`.  For every response,

\[
\boxed{
N_B(Q)=
\sum_{q\in Q}u_B(q)+
\sum_{L\in L_s}
\left[
\binom{h_B(L)+r_Q(L)}3-\binom{h_B(L)}3
\right].
}
\]

The residual grid weights have the same perfect-matching row/column gauge, so the
selector dimensions remain 32 and 99.  These inequalities are necessary realizability
conditions, not a complete characterization of all possible signatures.

## Labelled response frontier

For one accepted coefficient table, every response has exact nonnegative child vector

\[
v(Q)=(v_c(Q))_{c\in C}.
\]

Its coordinate sum is the exported all-ones scalar score.  Duplicate vectors are
weight-indistinguishable.  If one vector is componentwise no larger and is strictly
smaller somewhere, the dominated response cannot minimize any strictly positive child
weighting.  Thus every positive-weight minimizer lies on the exact Pareto frontier.

The full real-triple selector, all-ones exported selector and weighted labelled selector
are different policies.  Unlabelled destroyed-triple credit still requires an explicit
labelled routing theorem.

## Canonical population batch

Each operation entry now composes:

1. linked literal operation geometry and the full scalar selector;
2. the residual survivor-background signature; and
3. the labelled vector/Pareto certificate.

A batch record fixes the fibre, host, source, background, selector, threshold, policy,
residual and labelled-vector data and protects them by digest.  Batch completeness is
recognized only relative to an explicit sorted expected fibre-ID registry.  Without
that registry, every batch remains incomplete regardless of size.

## Active frontier

1. Derive and publish the exact expected fibre-ID registry from the actual parent
   operation rule; no sample may substitute for this registry.
2. Populate one canonical batch entry for every expected owner/provenance fibre,
   including true point, removal, survivor, entry-order and state-label data.
3. Validate the residual realizability inequalities and exact scalar selector on every
   genuine background.
4. Publish each fibre's labelled response vectors, duplicate quotient, Pareto frontier
   and any proposed positive child weights.
5. Compose every genuine operation with the destroyed threshold `T`, pool audit and
   exact policy penalty.
6. Resolve the nine one-triple hard-core hosts by one proved payment, legal rollback,
   nonuniform weighting or sharper labelled routing.
7. Resolve the two four-triple one-response hosts by four units or structural
   replacement.
8. Close the remaining 78 exceptional rows with full background, return, selector,
   interface and labelled child terms.
9. Prove every deletion, domination, transfer and state-label semantic assertion;
   close every recurrent labelled row, eliminate certified auxiliaries and publish the
   denominator-cleared global CRT quotient.
