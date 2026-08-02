# Side-six minimax repair path multiplicity

This chapter counts complete minimax-optimal paths to a no-three state in the canonical 546-state side-six repair graph. It refines the first-move choice census but remains a finite diagnostic.

## PX1149 — complete path census

The 544 nonsolutions have a total of `5,579` minimax-optimal solution paths when paths are counted separately from each starting state. Individual states have between one and 38 such paths.

The exact path-count histogram is replayed by the verifier.

## PX1150 — forced first moves equal globally unique paths

Exactly `102` nonsolutions have one minimax-optimal first move. Exactly the same `102` states have only one complete minimax-optimal path to a solution.

Thus local forcing and global forcing coincide in this graph. The remaining `442` nonsolutions have at least two complete optimal paths.

## PX1151 — bounded-uphill states retain complete path reserve

The ten states whose minimax barrier exceeds their current potential have complete path counts

`4,4,6,6,7,7,9,9,11,11`.

Therefore none of the bounded-uphill states is globally forced. Their first-move choice reserve survives through complete solution paths.

## PX1152 — the unique three-step state has thirty paths

The unique state requiring three minimax-optimal moves has exactly `30` complete optimal paths.

The finite graph therefore separates two difficulties for a global theorem:

1. 102 ordinary states have no local or global choice reserve;
2. the exceptional uphill states have several complete routes, so the missing issue is coordination across fibres rather than local existence.

No global resampling theorem follows from this finite graph alone.

## Verification

```bash
python scripts/verify_product_side_six_repair_path_multiplicity.py
```
