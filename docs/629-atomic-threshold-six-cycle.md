# Atomic threshold six-cycle support

The previous tranche reduces every nearest legal threshold replacement to two
conservative `2x2` swaps with an illegal visible intermediate. This chapter
identifies the exact simultaneous support required by the compound.

## Theorem PP3cxb — six-cell support classification

For each of the eight nearest legal degree-four target matrices, the difference
from the stored source matrix has exactly three entries `-1` and three entries
`+1`. These six cells use exactly three rows and three columns, with degree two
at every used row and column.

Consequently the signed support is one simple alternating six-cycle `C6` in the
row-column bipartite graph.

## Theorem PP3cxc — eight distinct atomic cycles

The eight nearest targets yield eight distinct alternating six-cycles. No
margin-preserving operation supported on fewer than six cells, fewer than three
rows, or fewer than three columns reaches any target.

Thus the smallest possible direct source operation is a simultaneous three-token
rotation around one of these six-cycles.

## Theorem PP3cxd — factorization obstruction

Each atomic six-cycle has exactly six ordered factorizations into two conservative
`2x2` swaps, giving forty-eight paths through twenty distinct intermediate
matrices. None of the intermediates is decomposable into four legal
no-three-in-line layers.

The geometric frontier is therefore exact: realize one six-cell alternating
cycle atomically on actual source cells, or prove that the recorded source
catalogue cannot support such an exposed-state-safe operation.
