# Superregular-resampling frontier pass 2

This addendum records the threshold-degree transportation bounds proved after the current branch theorem index. It does not change the status of SRR2, SRR4 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SRR2s--SRR2w | At every endpoint-cost threshold, left minimum degree and right maximum load bound the complete Hall deficiency; bounded remote conditioning subtracts only its actual local switching incidence, and the resulting degree-deficiency sums bound one-step, two-layer and multistep endpoint cost | PROVED UNDER THE LOCAL-INCIDENCE AND DETERMINISTIC-LOCALITY CONTRACTS | `docs/superregular-threshold-degree-cost-bound.md` |
| SRR2x--SRR2ab | Relative threshold imbalance `epsilon=(1-(d-b)/D)_+` bounds exact conditioned Hall deficiencies and endpoint cost; failed event budget forces one threshold with quantified relative degree/load imbalance | PROVED UNDER THE LOCAL-INCIDENCE AND DETERMINISTIC-LOCALITY CONTRACTS | `docs/superregular-relative-threshold-slack.md` |
| SRR2ac--SRR2ag | Near-biregular reference degree errors combine as `(eta+beta+zeta)/(1+zeta)` to bound conditioned threshold deficiency and integral endpoint cost | PROVED UNDER THE NEAR-BIREGULAR AND LOCAL-CONDITIONING CONTRACTS | `docs/superregular-near-biregular-threshold-slack.md` |
| SRR2ah--SRR2al | Coordinatewise tensor products factor left minimum degree and right maximum load exactly; local layer errors multiply into a global conditioned imbalance, and failure identifies one bad layer | PROVED UNDER THE TENSOR-FACTOR AND LOCAL-CONDITIONING CONTRACTS | `docs/superregular-tensor-product-threshold-slack.md` |
| SRR2am--SRR2aq | A graph obtained from a tensor reference by at most `lambda_L` left deletions and `lambda_R` right additions has `d>=d_0-lambda_L` and `D<=D_0+lambda_R`; these perturbations enter the exact relative-slack and endpoint-cost bounds locally | PROVED UNDER THE LOCAL PERTURBATION-ACCOUNTING CONTRACT | `docs/superregular-near-product-perturbation.md` |
| SRR2ar--SRR2av | The exact weighted conflict graph of feasible switching candidates has an executable independent subfamily of weight at least `sum_v w_v/(deg(v)+1)`; maximum conflict degree `Delta` retains at least a `1/(Delta+1)` fraction | PROVED UNDER THE COMPLETE PAIRWISE-CONFLICT GRAPH CONTRACT | `docs/superregular-weighted-conflict-thinning.md` |

## Updated frontier

The endpoint min-cost objective now has exact degree/load, relative-slack, near-biregular, bounded-layer tensor and near-product perturbation criteria. The resulting candidate mass also has a deterministic weighted conflict-thinning endpoint. Remaining geometric work is to construct suitable tensor references for the actual switching graphs, prove small layer/perturbation/conditioning errors, bound their exact conflict graph and handle genuinely higher-order omitted interactions.

No statement here proves SRR2, SRR4 or the no-three-in-line conjecture.