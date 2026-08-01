# Radius-64 corrected boundary transition

This chapter continues the canonical corrected nine-block state from `docs/621`.
It first closes the remaining radius-32 correction budget, then widens the offset
window without changing the block catalogue or saturation invariant.

## Theorem PP3cwv — budget-eight radius-32 obstruction

The two radius-32 tenth-block candidates are `P2` and `P3` at offset `-32`.
Each has one minimum five-point conflict transversal. For each candidate, every
choice of three further deleted points was checked: `67525` deletion triples per
candidate. No eight-point row-and-column-preserving refill is legal.

Thus increasing the correction budget from seven to eight does not extend the
radius-32 corrected chain.

## Theorem PP3cww — radius-64 tenth transition

In the widened offset window `[-64,64]`, the block `P3` at offset `64` has the
unique three-point conflict core

```text
(12,47), (21,98), (26,79).
```

No correction of total size at most five exists. The following six-point
correction preserves every row and column degree:

```text
delete:
(2,2), (3,0), (12,47), (21,98), (26,79), (32,100)

add:
(2,98), (3,100), (12,2), (21,0), (26,47), (32,79)
```

The resulting state has eighty points, ten corrected blocks, and no collinear
triple.

## Theorem PP3cwx — no raw eleventh extension

From the corrected ten-block state, all `8*129=1032` typed eleventh-block
attempts in offset window `[-64,64]` contain a collinear triple. Hence there is
no raw eleventh extension in the widened window.

The corrected path has therefore advanced from nine to ten blocks, but no
periodic component or eleventh correction is established.
