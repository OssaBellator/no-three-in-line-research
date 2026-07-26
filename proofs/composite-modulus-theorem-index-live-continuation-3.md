# Live composite-modulus theorem ledger continuation 3

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `composite-modulus-theorem-index-live-continuation-2.md` through CMR1197; and
- this file from CMR1198 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR1198--1205 | Fixed-target collateral expectation and one-bank improvement criterion | PROVED | `docs/254-prime-power-degree-two-bank-collateral-expectation.md` |
| CMR1206--1213 | Restricted-host penalty and target aggregation | PROVED | `docs/255-prime-power-restricted-bank-target-collateral-selection.md` |
| CMR1214--1221 | Absolute last-entering collateral ownership | PROVED | `docs/256-prime-power-last-entering-edge-collateral-ownership.md` |
| CMR1222--1229 | Corrected rank-one/two/three line energy | PROVED; old matching subsets subtracted | `docs/257-prime-power-degree-two-bank-line-energy.md` |
| CMR1230--1237 | Rank-one marginal and assignment refinement | PROVED | `docs/258-prime-power-rank-one-bank-marginal-refinement.md` |
| CMR1238--1245 | Full local collateral envelopes and matching assignment | PROVED | `docs/259-prime-power-full-collateral-local-envelope.md` |
| CMR1246--1253 | Optimized target-cell envelope aggregation | PROVED | `docs/260-prime-power-optimized-envelope-target-aggregation.md` |
| CMR1254--1261 | Last-creation live-credit ledger | PROVED | `docs/261-prime-power-last-creation-collateral-credit-ledger.md` |
| CMR1262--1269 | Offspring matrices and spectral-radius reduction | PROVED as a reduction; subcritical matrix remains OPEN | `docs/262-prime-power-collateral-reproduction-matrix.md` |
| CMR1270--1277 | Rational and integer Lyapunov certificates | PROVED | `docs/263-prime-power-rational-spectral-certificate.md` |
| CMR1278--1285 | Side-three full-grid strict responses | PROVED only for standard/verified affine full grids | `docs/264-prime-power-side-three-strict-target-improvement.md` |
| CMR1286--1293 | Side-four full-grid improvement policy | PROVED only for standard/verified affine full grids | `docs/265-prime-power-side-four-finite-improvement.md` |
| CMR1294--1301 | Side-five full-grid improvement policy | PROVED only for standard/verified affine full grids | `docs/266-prime-power-side-five-finite-improvement.md` |
| CMR1302--1309 | Extension-free target response family | PROVED | `docs/267-prime-power-extension-free-target-response-family.md` |
| CMR1310--1317 | Side-six response traps and two-layer escape | PROVED only for standard/verified affine full grids | `docs/268-prime-power-side-six-target-response-traps.md` |
| CMR1318--1325 | Last-entering owner DAG and exact block triangularity | PROVED | `docs/269-prime-power-last-entering-owner-triangularity.md` |
| CMR1326--1333 | Exact credit classes and honest upper quotients | PROVED | `docs/270-prime-power-exact-credit-classes-upper-quotients.md` |
| CMR1334--1341 | Corrected exact/dyadic line profiles | PROVED; `B_n=2+floor(log_2 n)` | `docs/271-prime-power-degree-two-bank-line-profile-classes.md` |
| CMR1342--1349 | Exact pair moments and profile envelopes | PROVED | `docs/272-prime-power-line-profile-pair-moment-envelopes.md` |
| CMR1350--1357 | Extension-free permanent bound and scaling | PROVED | `docs/273-prime-power-extension-free-bank-permanent-bound.md` |
| CMR1358--1365 | Exact derangement bank size and sharp marginals | PROVED | `docs/274-prime-power-extension-free-derangement-marginals.md` |
| CMR1366--1373 | Exact all-target line kernel and independent-line obstruction | PROVED | `docs/275-prime-power-extension-free-line-composition-kernel.md` |
| CMR1374--1381 | Exact extension-free cylinder types | PROVED | `docs/276-prime-power-extension-free-exact-cylinder-types.md` |
| CMR1382--1389 | Cross-line selector and fractional matching normal form | PROVED; side-five witness checked completely | `docs/277-prime-power-cross-line-edge-assignment-normal-form.md` |
| CMR1390--1397 | Candidate transversals, Hall witnesses and clean deletion criterion | PROVED | `docs/278-prime-power-candidate-transversal-hall-wall.md` |
| CMR1398--1405 | Fixed pre-sampling owners and exact rook owner loads | PROVED | `docs/278-prime-power-rook-owner-edge-weights.md` |
| CMR1406--1413 | Matching preclusion, minimum star blockers and owner-support tails | PROVED | `docs/279-prime-power-owner-support-matching-preclusion.md` |
| CMR1414--1421 | Exact residual rook numbers, prescription probabilities and host penalties | PROVED; reindexed after concurrent collision | `docs/280-prime-power-extension-free-rook-probabilities.md` |
| CMR1422--1429 | Exact owner-line loads, doubly stochastic assignment and integer dual certificate | PROVED | `docs/281-prime-power-cross-line-owner-assignment.md` |
| CMR1430--1437 | Closed owner/rook class weights and geometric refinements | PROVED | `docs/282-prime-power-rook-owner-edge-weights.md` |
| CMR1438--1445 | Harmonic conditional owner stars with inherited coordinate span | PROVED | `docs/283-prime-power-cross-line-harmonic-owner-bound.md` |
| CMR1446--1453 | Inherited lattice-capacity owner envelope and exact height cutoff | PROVED | `docs/284-prime-power-cross-line-lattice-capacity-owner.md` |
| CMR1454--1461 | Eligible prime-power signatures with separate matching, envelope and span parameters | PROVED | `docs/285-prime-power-eligible-owner-signature-fans.md` |
| CMR1462--1469 | Fractional packed-signature identity, owner/pair dispersion, primitive-direction concentration and exact-displacement translation banks | PROVED; inherited-coordinate parameters corrected before endpoint snapshot | `docs/286-prime-power-fractional-packed-signature-fans.md` |

The branch still does not prove the all-`n` conjecture.

The complete selected owner matrix is block upper triangular, so only
same-owner diagonal blocks require subcritical certificates.  Exact rook
classes give prescription probabilities; canonical owner fibres give one
doubly stochastic edge-assignment cost; and inherited lattice capacity reduces
owner load to finite first-separation/projective-direction/height classes.

For a response matching side `d` inside envelope `p^k` with ambient coordinate
span `W_omega`, a positive-minimum fractional obstruction contains a signature
of packed incidence mass at least

\[
\frac{d-2}{3k(p+1)B_\omega},
\qquad
B_\omega=1+\lfloor\log_2\max\{1,W_\omega\}\rfloor.
\]

It further contains an exact-displacement translation class of mass at least

\[
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)},
\]

where

\[
S_{\omega,p}(s,H)=\left\lfloor\frac{W_\omega}{p^sH}\right\rfloor.
\]

The active frontier is:

1. pay the CMR1469 exact-displacement bank through prefix return,
   quotient/carry collision or protected reserve;
2. compare that global payment with the one-owner loaded-line gain of
   CMR1458--CMR1461;
3. encode the comparison as a host-uniform rational/integer certificate
   `Av<v`;
4. prove analogous diagonal certificates for prime-field and thin owners; and
5. glue them through owner triangularity and complete balanced/CRT assembly.
