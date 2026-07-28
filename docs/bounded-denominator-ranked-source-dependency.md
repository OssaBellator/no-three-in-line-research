# BDA ranked source-dependency potential

This note treats source creation that is not free but is mediated by a finite acyclic physical dependency graph. It complements the paid replenishment bank; it does not cover a genuine directed source cycle.

## Setup

Let source tokens occupy ranks `0,1,...,R`. Rank-zero tokens are the only exogenous initial or deposited tokens. A source-creation operation may move token mass from rank `r` to rank `r+1`, preserving or decreasing total token mass. It may split labels, but every output token retains the exact consumed predecessor address. No operation moves mass backward or introduces unrecorded mass.

Terminal positive-source edges used by a wall restoration are represented by tokens at any retained rank. Consuming such an edge destroys the corresponding token mass.

## BDA5ck — layer conservation

At every time, total retained token mass is at most the initial rank-zero mass plus all recorded rank-zero deposits.

## BDA5cl — bounded creation throughput

Every token crosses at most `R` rank boundaries. Therefore the cumulative source-creation mass is at most

`R(C_0 + D_0)`,

where `C_0` is initial exogenous mass and `D_0` is total recorded exogenous deposit mass.

This is a throughput bound, not merely a bound on the final stock.

## BDA5cm — restoration payment

Every selected positive source edge from the large-jump compensation theorem consumes retained token mass. Thus the total paid restoration mass is bounded by the same exogenous source account, while repeated relabelling of one physical token is forbidden by predecessor lineage.

## BDA5cn — dependency-cycle return

If a source operation requires a token from the same or a higher rank, the ranked contract fails and returns the least directed dependency cycle in the exact source-operation graph. Such a cycle is the remaining cyclic self-replenishment obstruction; it is not declared paid.

## BDA5co — combined router

Combine the ranked potential with the source-mass and paid-replenishment banks:

- initial and externally deposited tokens have finite total mass;
- acyclic internal creation has total throughput at most `R(C_0+D_0)`;
- wall restorations debit the resulting tokens;
- a backward dependency returns one exact source cycle;
- a changed operation dictionary or lost predecessor address returns reset.

The result is independent of jump magnitude and word length once the exact source-token lineage is retained. It does not prove that the BDA arithmetic operations admit such a ranked dependency graph.

No statement here proves BDA6 or the no-three-in-line conjecture.