# Superregular-resampling frontier pass 2

This addendum records the threshold-degree transportation bounds proved after the current branch theorem index. It does not change the status of SRR2, SRR4 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SRR2s--SRR2w | At every endpoint-cost threshold, left minimum degree and right maximum load bound the complete Hall deficiency; bounded remote conditioning subtracts only its actual local switching incidence, and the resulting degree-deficiency sums bound one-step, two-layer and multistep endpoint cost | PROVED UNDER THE LOCAL-INCIDENCE AND DETERMINISTIC-LOCALITY CONTRACTS | `docs/superregular-threshold-degree-cost-bound.md` |
| SRR2x--SRR2ab | Relative threshold imbalance `epsilon=(1-(d-b)/D)_+` bounds exact conditioned Hall deficiencies and endpoint cost; failed event budget forces one threshold with quantified relative degree/load imbalance | PROVED UNDER THE LOCAL-INCIDENCE AND DETERMINISTIC-LOCALITY CONTRACTS | `docs/superregular-relative-threshold-slack.md` |
| SRR2ac--SRR2ag | If a threshold switching graph is near-biregular around reference degree `rho`, then forward deficit `eta`, reverse overload `zeta` and conditioning loss `beta` give `epsilon <= (eta+beta+zeta)/(1+zeta)` and an explicit integral endpoint-cost criterion | PROVED UNDER THE REFERENCE-DEGREE AND LOCAL-INCIDENCE CONTRACTS | `docs/superregular-near-biregular-threshold-slack.md` |

## Updated frontier

The min-cost endpoint objective now has:

1. an exact threshold degree/load bound;
2. a dimensionless relative-slack target;
3. a near-biregular sufficient criterion in which forward deficit, reverse overload and conditioning loss enter additively.

Remaining work is geometric: construct bounded-cycle switching graphs for the actual rank-two/rank-three event inventories in arbitrary superregular hosts and prove small reference-degree errors `eta_k,zeta_k,beta_k`, then feed the resulting pathwise transportation cost into the local conflict endpoint beyond global first moment.

No statement here proves SRR2, SRR4 or the no-three-in-line conjecture.