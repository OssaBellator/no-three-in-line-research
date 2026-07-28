# Superregular-resampling frontier pass 2

This addendum records the threshold-degree transportation bounds proved after the current branch theorem index. It does not change the status of SRR2, SRR4 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SRR2n--SRR2r | At every endpoint-cost threshold, left minimum degree and right maximum load bound the complete Hall deficiency; bounded remote conditioning subtracts only its actual local switching incidence, and the resulting degree-deficiency sums bound one-step, two-layer and multistep endpoint cost | PROVED UNDER THE LOCAL-INCIDENCE AND DETERMINISTIC-LOCALITY CONTRACTS | `docs/superregular-threshold-degree-cost-bound.md` |

## Updated frontier

The min-cost endpoint objective now has a concrete sufficient route through threshold-local degree/load estimates. Remaining work is geometric: prove strong enough `d_k/D_k` ratios for bounded-cycle switching graphs and the actual rank-two/rank-three event inventories in arbitrary superregular hosts, then upgrade the local conflict endpoint beyond global first moment.

No statement here proves SRR2, SRR4 or the no-three-in-line conjecture.
