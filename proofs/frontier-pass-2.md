# Superregular-resampling frontier pass 2

This addendum records the threshold-degree transportation bounds proved after the current branch theorem index. It does not change the status of SRR2, SRR4 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SRR2s--SRR2w | At every endpoint-cost threshold, left minimum degree and right maximum load bound the complete Hall deficiency; bounded remote conditioning subtracts only its actual local switching incidence, and the resulting degree-deficiency sums bound one-step, two-layer and multistep endpoint cost | PROVED UNDER THE LOCAL-INCIDENCE AND DETERMINISTIC-LOCALITY CONTRACTS | `docs/superregular-threshold-degree-cost-bound.md` |
| SRR2x--SRR2ab | Relative threshold imbalance `epsilon=(1-(d-b)/D)_+` bounds exact conditioned Hall deficiencies and endpoint cost; failed event budget forces one threshold with quantified relative degree/load imbalance | PROVED UNDER THE LOCAL-INCIDENCE AND DETERMINISTIC-LOCALITY CONTRACTS | `docs/superregular-relative-threshold-slack.md` |

## Updated frontier

The min-cost endpoint objective now has both an exact threshold-degree bound and a dimensionless relative-slack target. Remaining work is geometric: prove small conditioned imbalance `(1-(d_k-b_k)/D_k)_+` for bounded-cycle switching graphs and the actual rank-two/rank-three event inventories in arbitrary superregular hosts, then upgrade the local conflict endpoint beyond global first moment.

No statement here proves SRR2, SRR4 or the no-three-in-line conjecture.
