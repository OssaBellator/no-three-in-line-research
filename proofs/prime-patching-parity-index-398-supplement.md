# Prime-patching parity index supplement: `docs/398`

This supplement extends the cumulative parity index and the `docs/396--397`
supplement.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bwf--PP3bwh | Boundary conflict witnesses have at most 510 owner/bridge/label signatures; an exact conflict packing localizes to one fixed signature with loss at most 510, and global recleaning cost localizes with total loss at most 1530 | PROVED | `docs/398-fixed-signature-boundary-conflict-localization.md` |

## Frontier update

Any covering rotation with large recleaning cost now yields a constant-loss local
core in which every positive-weight conflict pair has the same ordered owner
list, the same direct-versus-boundary bridge pattern, and the same parity-label
word. Under a boundary-component size cap, the core contains linearly many
distinct conflict pairs at that one fixed signature.

The remaining geometric task is finite-type: for each of at most 510 signatures,
bound its total packing mass across pair-safe covering rotations or convert a
dense fixed-signature core into a new improving rotation or trade.

The next available theorem identifier is `PP3bwi`.
