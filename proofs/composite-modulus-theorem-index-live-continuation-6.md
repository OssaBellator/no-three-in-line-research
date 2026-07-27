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

The branch still does not prove the all-`n` conjecture.

## Exact finite background quotient

For side `s`, the absolute scalar background signature contains the grid point-pair
counts `p_B(q)` and the occupancies of the finite canonical response-line universe.
There are 23 such lines on side four and 83 on side five.

Every perfect response matching uses every row and every column once. Therefore the
rank-one grid weights are selector-equivalent modulo row and column potentials. With

\[
d_{ij}=p_{ij}-p_{i0}-p_{0j}+p_{00}\qquad(i,j>0),
\]

the exact reduced selector dimensions are

\[
\boxed{32\text{ on side four},\qquad99\text{ on side five}.}
\]

For every response `Q`,

\[
N_B(Q)=C_B+F_Q(\widehat\Sigma_s(B)),
\]

where `C_B` is common to all responses and `F_Q` is one affine integer row. Equal
reduced signatures give identical score differences and selectors, but do not prove
labelled or transition equivalence.

## Exact affine chambers

All 9,260 response occurrences use only 39 affine rows: six on side four and 33 on
side five. If host responses are lexicographically ordered `Q_0,...,Q_{Z-1}`, then
`Q_i` is selected exactly when

\[
F_{Q_i}<F_{Q_j}\quad(j<i),
\qquad
F_{Q_i}\le F_{Q_j}\quad(j>i).
\]

The complete catalogue has 125,448 ordered host comparisons but only 1,086 distinct
ordered affine-row pairs. These chambers are exact for the scalar selector only.

## Linked operation selector

A composed certificate now forces one source to agree on:

1. canonical host and fibre identity;
2. complete response family and denominator;
3. survivor background;
4. literal rank-one, rank-two and rank-three counts for every response;
5. destroyed-current-triple count `T`;
6. full selector and exact minimum delta; and
7. the response chosen by the declared parent policy.

Responsewise,

\[
\boxed{\Delta\Psi(Q)=N_B(Q)-T.}
\]

The full selector is strictly improving exactly when `N_B^*<T`. For the parent policy,

\[
\pi_{\rm pol}=N_B(Q_{\rm pol})-N_B^*\ge0
\]

is an exact policy penalty. It is not deletion credit, rollback distance, uniform
slack or labelled routing slack.

## Active frontier

1. Populate canonical linkage certificates for every actual owner/provenance fibre.
2. Populate true pre-response points, removal sets, survivor backgrounds, entry orders
   and rule-specific transition evidence.
3. Replace repeated geometric response enumeration by the certified reduced signature
   and 39-row affine library; record the chamber and exact full selector of every fibre.
4. Compose every genuine operation with the linked-operation selector and certify the
   actual destroyed threshold `T`.
5. Resolve the nine one-triple hard-core hosts by one proved payment, legal rollback,
   nonuniform weighting or sharper labelled routing.
6. Resolve the two four-triple one-response hosts by four units or structural
   replacement.
7. Close the remaining 78 exceptional rows with full background, return, selector,
   interface and labelled child terms.
8. Complete pool audits, domination, transfer and state-label semantics for every
   genuine operation.
9. Close every recurrent labelled row, eliminate certified auxiliaries and publish the
   denominator-cleared global CRT quotient.
