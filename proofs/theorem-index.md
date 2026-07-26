# Sparse-algebraic-spread theorem index

This ledger contains the branch-specific results only.

| ID | Statement | Status | Location |
|---|---|---|---|
| SAS1a | Sparse complete-block hosts have an all-rank product matching measure | PROVED | `docs/sparse-block-host-spread.md` |
| SAS2a | Linear four-cycle switch count gives `O(1/d)` edge spread | PROVED | `docs/sparse-four-cycle-switching.md` |
| SAS2b | General labelled switching ratio bounds one-edge probability | PROVED | `docs/sparse-general-switching-ratio.md` |
| SAS3a | Conditional edge bounds imply fixed-rank sparse spread | PROVED | `docs/sparse-spread-composition.md` |
| SAS3b | Sparse switching persists under compatible conditioning | PROVED | `docs/sparse-four-cycle-switching.md` |
| SAS3c | General labelled switching ratios persist under conditioning | PROVED | `docs/sparse-general-switching-ratio.md` |
| SAS4a | Conditional two-layer spread composes to `(2C/d)`-spread | PROVED | `docs/sparse-spread-composition.md` |
| SAS4b | Residual block derangements give conditional all-rank two-layer spread | PROVED | `docs/sparse-block-host-spread.md` |
| SAS5a | Global conflict mass yields a saturated 2-factor | PROVED | `docs/sparse-spread-composition.md` |
| SAS5b | Consecutive sparse blocks have supercubic compatible collinear-triple load | PROVED | `docs/sparse-block-host-geometric-obstruction.md` |
| SAS5c | Complete sparse blocks have exact one-dimensional affine-shape energy | PROVED | `docs/sparse-block-affine-energy.md` |
| SAS5d | Every row set has an integer companion with zero internal block energy | PROVED | `docs/sparse-zero-energy-blocks.md` |
| SAS5e | Every complete sparse block host has a polynomial-range zero-conflict embedding | PROVED | `docs/sparse-expanded-grid-zero-conflict.md` |
| SAS5f | Standard-grid compression has exact balanced-colour affine-triple energy | PROVED | `docs/sparse-balanced-compression-energy.md` |
| SAS5g | Exact conditional energy gives a deterministic balanced decoder | PROVED | `docs/sparse-balanced-compression-energy.md` |
| SAS5h | Swap descent lowers energy or returns a quantified near-conflict bank | PROVED | `docs/sparse-balanced-compression-energy.md` |
| SAS5i | A positive swap-local minimum has one column pair concentrating destroyed conflicts and repairs | PROVED | `docs/sparse-balanced-compression-energy.md` |
| SAS5j–SAS5l | Concentrated swaps have twelve destruction and repair words; double-scope words have unique rational addresses and one word pair retains explicit weight | PROVED | `docs/sparse-concentrated-swap-words.md` |
| SAS5m–SAS5p | Every double-scope rational address has an exact reduced-denominator criterion and lies on one primitive progression; one direction and exact parallel line retain polynomially quantified weight | PROVED | `docs/sparse-double-scope-divisor-progressions.md` |
| SAS5q–SAS5t | Every singleton-scope word has an exact primitive two-gap dilation model; one primitive row shape and exact row-triple family retain polynomially quantified weight | PROVED | `docs/sparse-singleton-scope-dilations.md` |
| SAS5u–SAS5y | Primitive parameter families have an exact board-length bound; diffuse mass forces bounded shape, while dense support yields disjoint adjacent parameter pairs with one common increment | PROVED | `docs/sparse-parameter-chain-density.md` |
| SAS5z–SAS5ad | Column reflection canonically pairs every destruction word with one repair word; failure localizes to one boundary or at most two reflected-label defects, and primitive increments reverse exactly | PROVED | `docs/sparse-swap-reflection-router.md` |
| SAS5ae–SAS5ai | A heavy reflected-label role yields an exact defect column or a disjoint balanced donor-swap bank; bounded column-scope incidence gives a compatible subbank | PROVED UNDER THE DECLARED INCIDENCE CAP FOR SAS5ah | `docs/sparse-reflected-label-defect-router.md` |
| SAS5aj–SAS5an | Bounded global column incidence gives a constraint-compatible donor subbank with exact additive energy; positive gain survives, while local failure yields many distinct repaired records | PROVED UNDER THE GLOBAL COLUMN-INCIDENCE CAP `Lambda` | `docs/sparse-donor-batch-energy.md` |
| SAS5ao–SAS5as | Distinct donor defects give distinct designated mirror records; composing the fixed original swap with a compatible donor bank preserves a quantified simultaneous repair family and gives post-swap additive energy | PROVED WITH ORIGINAL-SWAP COMPOSITION; UNDER THE GLOBAL COLUMN-INCIDENCE CAP `Lambda` | `docs/sparse-designated-mirror-repair-bank.md` |
| SAS5at–SAS5ax | In a double-scope defect role, the original swap plus one donor repairs the whole weighted defect-column fibre; top fibres admit `d-2` donor matching and explicit weighted retention | PROVED WITH ORIGINAL-SWAP COMPOSITION; UNDER `Lambda` FOR THE ADDITIVE SUBBATCH | `docs/sparse-double-scope-weighted-defect-fibres.md` |
| SAS5ay–SAS5bc | Singleton fibres with at most `h` donor-labelled companions admit `d-2-h` whole-fibre donor matching and weighted retention; failure concentrates on one exact companion column | PROVED WITH ORIGINAL-SWAP COMPOSITION; UNDER `Lambda` FOR THE ADDITIVE SUBBATCH | `docs/sparse-singleton-companion-obstruction-router.md` |
| SAS5bd–SAS5bh | A fixed companion column and primitive singleton shape reconstruct at most one defect; weighted concentration yields one heavy exact fibre, which either repairs or has donor-companion saturation | PROVED WITH ORIGINAL-SWAP COMPOSITION | `docs/sparse-companion-column-arithmetic-localization.md` |
| SAS5bi–SAS5bm | A heavy singleton fibre splits over divisor scales; one scale retains `1/tau(|z-x|)` weight and either repairs or forces the full donor class into one congruence progression | PROVED WITH ORIGINAL-SWAP COMPOSITION | `docs/sparse-saturated-fibre-divisor-scale.md` |
| SAS5bn–SAS5br | One repaired divisor scale contributes exact `+1` mixed curvature per record; at a swap-local minimum this gives an energy barrier or a concentrated negative cross-interaction fibre | PROVED WITH ORIGINAL-SWAP COMPOSITION | `docs/sparse-divisor-scale-mixed-energy-ledger.md` |
| SAS5bs–SAS5bw | Conjunction records under two disjoint swaps have curvature only in `{-1,0,1}`; negative curvature has exactly two single-swap-only orientations, and one endpoint-pair/orientation/scope-type fibre retains `1/24` of the negative mass | PROVED | `docs/sparse-negative-mixed-curvature-patterns.md` |
| SAS5bx–SAS5cb | Two fixed swap-endpoint columns and one primitive row ratio reconstruct the third column uniquely; mate types are already fixed, while the outside type loses at most `24(N-1)^2` before exact column concentration | PROVED | `docs/sparse-negative-cross-third-column-arithmetic.md` |
| SAS5cc–SAS5cg | A fixed primitive row ratio leaves only row scale and base row; the single-swap-only orientation forces the entire required-label vector, so one exact negative record retains `1/[576N(N-1)^3]` of the scale-level negative mass | PROVED | `docs/sparse-negative-cross-exact-record-collapse.md` |
| SAS5ch–SAS5cl | Exact-record aliases aggregate with no energy loss; one rank-three record has mixed-curvature incidence at most two across endpoint-disjoint donors, yielding a two-reuse budget for heavy collateral and improving composed moves | PROVED | `docs/sparse-exact-record-alias-and-donor-incidence.md` |
| SAS5cm–SAS5cq | Summing the exact mixed-energy identity over an endpoint-disjoint donor bank gives a lower bound `L_bank-2Omega_cross`, a joint budget for selected scale mass plus improvement depth, and an average positive-barrier threshold | PROVED | `docs/sparse-donor-bank-aggregate-energy.md` |
| SAS6 | Arithmetic batching or classification of concentrated swap certificates | OPEN; THE NEGATIVE MIXED-CURVATURE BRANCH NOW HAS AN EXACT PHYSICAL-RECORD QUOTIENT, TWO-USE COLLATERAL BUDGET AND AGGREGATE DONOR-BANK ENERGY ROUTER, WHILE THE OTHER EXACT-SCALE BRANCH IS A COPRIME DONOR-SATURATED PROGRESSION; CONSTRUCTING SCALE-DOMINANT BANKS, EXPLOITING COLLATERAL-DOMINANT HEAVY RECORDS, HIGH-INCIDENCE AND BOUNDARY PROFILES REMAIN | `docs/sparse-algebraic-spread.md` |

No statement here proves the global conjecture.