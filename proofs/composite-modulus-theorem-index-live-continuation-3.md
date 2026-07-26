# Live composite-modulus theorem ledger continuation 3

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `composite-modulus-theorem-index-live-continuation-2.md` through CMR1197; and
- this file from CMR1198 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR1198--1205 | Disjoint target extensions, van der Waerden response-bank lower bound, rank-one/two/three cylinder probabilities, exact physical collateral classes, expected collateral, destroyed target load, one-bank strict-improvement criterion, and the positive-minimum collateral barrier | PROVED | `docs/254-prime-power-degree-two-bank-collateral-expectation.md` |
| CMR1206--1213 | Expected unavailable-edge use, feasibility penalty, restricted-host improvement, target-incidence identity, edge-averaged bank inequality, forbidden-extension optimization, and the restricted-bank barrier | PROVED | `docs/255-prime-power-restricted-bank-target-collateral-selection.md` |
| CMR1214--1221 | Entering-edge support of every created triple, canonical absolute owner, exact owner partition, fixed-core no-duplication, unique product ownership, contraction/lifting invariance, edge-local bank scores, and the collateral-owner endpoint | PROVED | `docs/256-prime-power-last-entering-edge-collateral-ownership.md` |
| CMR1222--1229 | Corrected rank-one/two/three line-energy identities, surviving-old-edge subtraction, exact compatible-pair stocks, corrected line-cap bounds, line-local owner scores, and the line-energy endpoint | PROVED; corrected before indexing to subtract old matching edges and triples | `docs/257-prime-power-degree-two-bank-line-energy.md` |
| CMR1230--1237 | Corrected rank-one edge weights, doubly-stochastic response marginals, row/column assignment bounds, refined collateral expectation, restricted improvement, heavy genuinely-new edge concentration, and loaded-line/secant-star alternatives | PROVED; old response edges have zero new-collateral weight | `docs/258-prime-power-rank-one-bank-marginal-refinement.md` |
| CMR1238--1245 | Edge extendability in regular bipartite response graphs, exact local rank-two/three incidence, full local collateral envelopes, row/column pointwise bounds, target improvement or wall blockage, rank-two assignment representation, and local line/star consequences | PROVED | `docs/259-prime-power-full-collateral-local-envelope.md` |
| CMR1246--1253 | Feasible-extension decision, optimized full-collateral envelope, global target-incidence barrier, concentrated entering edge, quantitative rank split, explicit line/star scales, extension-law averaging, and the optimized aggregation endpoint | PROVED | `docs/260-prime-power-optimized-envelope-target-aggregation.md` |
| CMR1254--1261 | Last creation times, physical owner credits, exact live-credit partition, transition update, owner-load bound, owner-cell retirement, layer-reassignment invariance, and the collateral-credit endpoint | PROVED | `docs/261-prime-power-last-creation-collateral-credit-ledger.md` |
| CMR1262--1269 | Expected offspring matrix, weighted live-credit descent, spectral-radius equivalence, upper-matrix domination, finite policy selection, relation to CMR1196 weights, conditional product-block triangularity, and the spectral frontier | PROVED as a reduction; proving a suitable upper matrix has spectral radius below one remains OPEN | `docs/262-prime-power-collateral-reproduction-matrix.md` |
| CMR1270--1277 | Rational Lyapunov certificates, integer scaling, perturbation robustness, constructive block gluing, deterministic row selection, exact finite-bank integer checks, coarse-class lifting, and the exact-certificate endpoint | PROVED | `docs/263-prime-power-rational-spectral-certificate.md` |
| CMR1278--1285 | Six full side-three states, exact potential table, unique response rule, clean target responses, restricted-host singleton blockage, zero offspring block, conditional gluing, and the scoped side-three endpoint | PROVED only for the standard full grid and verified common-affine copies; arbitrary scattered residual factors retain CMR1176 | `docs/264-prime-power-side-three-strict-target-improvement.md` |
| CMR1286--1293 | Full side-four state stock, complete target-response search, strict lower responses, canonical policy, restricted lowering expansion, finite budget, credit descent, and the scoped endpoint | PROVED only for the standard full grid and verified common-affine copies | `docs/265-prime-power-side-four-finite-improvement.md` |
| CMR1294--1301 | Full side-five state stock, 12/13-state response banks, target-response table, strict lower responses, canonical policy, restricted lowering expansion, finite budget, and the scoped endpoint | PROVED only for the standard full grid and verified common-affine copies | `docs/266-prime-power-side-five-finite-improvement.md` |
| CMR1302--1309 | Edge-containing regular factorization, exact union of all forbidden-extension banks, canonical extension recovery, extension-free target optimization, target destruction, restricted lowering response, scope separation, and the extension-free endpoint | PROVED | `docs/267-prime-power-extension-free-target-response-family.md` |
| CMR1310--1317 | Full side-six state stock, extension-free response table, immediate trap classification, equal-response escape graph, corrected feeder/two-cycle trap core, clean CMF1 two-layer escape, restricted lowering expansion, and the scoped endpoint | PROVED only for the standard full grid and verified common-affine copies; six two-cycles plus twelve one-step feeders, no fixed points | `docs/268-prime-power-side-six-target-response-traps.md` |

The branch still does not prove the all-`n` conjecture.

The target-versus-collateral frontier now has exact finite quantities.  For one
fixed-target degree-two bank, compatible rank-`r` prescriptions have explicit
permanent-ratio bounds; restricted availability has an explicit penalty; and a
pointwise full-collateral envelope assigns every created triple to one absolute
entering edge and one real line.  Optimizing those envelopes over target cells
forces either strict improvement, unit-wall descent, or one quantitatively heavy
rank-one/rank-two/rank-three line or star certificate.

The dynamic version is a live-credit reproduction system.  Every triple has one
last creation time and one physical owner cell.  A finite response policy has an
expected offspring matrix `A`; a positive rational vector with `Av<v`, equivalently
`rho(A)<1`, is an exact weighted-potential certificate.  Rational certificates can
be checked by integer arithmetic, tolerate bounded error, and glue constructively
across genuinely block-upper-triangular products.

The standard full grids of sides three through six now have explicit finite
response classifications.  This is root/affine finite evidence only.  It is not a
statement about scattered residual factor coordinates, where real collinearity
must remain in the inherited parent geometry.

The active frontier is therefore:

1. construct an honest line/height/carry/fixed-interface upper offspring matrix
   with spectral radius below one, or a rational vector proving `Av<v`;
2. prove that last-entering ownership makes unit-wall and child-product matrices
   block triangular up to a quantitatively absorbable interface block;
3. establish the same certificate in prime-field and low-height regimes; and
4. assemble arbitrary side lengths while retaining CRT collision/local-line
   offspring classes.
