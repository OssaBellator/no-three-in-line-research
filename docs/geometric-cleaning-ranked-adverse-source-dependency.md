# GC ranked adverse-source dependency

The global-shortage potential shows that recurrent count failure needs target recreation or donor destruction. This note bounds those adverse sources when they arise from a finite acyclic physical dependency system.

## Setup

Adverse-source tokens occupy ranks `0,1,...,R`. Rank-zero tokens are initial or externally deposited physical resources. A dependency operation moves token mass from rank `r` to rank `r+1`, preserving or decreasing total mass and retaining the consumed predecessor address. Each output unit is labelled exactly as either:

- one target-recreation unit, or
- one donor-destruction unit.

No operation moves mass backward or introduces unrecorded mass.

## GC2hi — adverse layer conservation

At every time, total retained adverse-source mass is at most the initial rank-zero mass plus recorded rank-zero deposits.

## GC2hj — bounded adverse throughput

Every token crosses at most `R` dependency boundaries. Therefore cumulative target-recreation plus donor-destruction mass is at most

`R(C_0+D_0)`.

## GC2hk — shortage-cycle payment

Every closed global-shortage count cycle needs adverse mass equal to its target-removal plus donor-addition progress. Hence cumulative recurrent progress is bounded by the ranked adverse-source throughput.

## GC2hl — exact dependency-cycle return

If an adverse operation consumes from the same or a higher rank, the contract returns the least directed cycle in the physical adverse-source graph. That cycle is the remaining self-replenishing obstruction and is not counted as paid progress.

## GC2hm — combined global-shortage router

The global shortage branch now routes to:

- monotone target removal or donor addition;
- payment from a finite ranked adverse-source potential;
- one exact directed adverse-source cycle;
- an unrecorded deposit, changed dictionary or lost predecessor reset.

This note does not prove that geometric target recreation and donor destruction possess the required ranked dependency structure, nor does it address untagged feedback or clean-height preservation.

No statement here proves GC5 or the no-three-in-line conjecture.