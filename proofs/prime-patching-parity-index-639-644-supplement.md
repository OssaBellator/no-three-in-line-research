# Prime-patching parity index supplement: `docs/639--644`

This supplement continues the cumulative PP3 index after `docs/638`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cyf--PP3cyh | Complete twelfth conflict spectrum; all five low-core attempts correct; canonical five-point correction reaches twelve blocks | PROVED | `docs/639-corrected-twelfth-boundary-transition.md` |
| PP3cyi--PP3cyk | The actual source-star fixture has three good centres out of four and yields an exact bad-centre pruning interface | PROVED / CONDITIONAL INTERFACE | `docs/640-source-star-centre-pruning.md` |
| PP3cyl--PP3cyn | Every native threshold factorization exposes one transient unit cell and has minimum seven-cell batch support | PROVED / FINITE REDUCTION | `docs/641-threshold-transient-buffer-cell.md` |
| PP3cyo--PP3cyq | A thirteen-pair saturated source supports all 4,096 run compositions and contains induced eleven-pair sources, but anchors do not descend | PROVED / CONDITIONAL SOURCE MODEL | `docs/642-thirteen-pair-saturated-anchor-reservoir.md` |
| PP3cyr--PP3cyt | Fixed shell collateral amortizes exactly when per-use overhead is below one half, with an exact minimum-period law | PROVED / CONDITIONAL COST MODEL | `docs/643-shell-batch-amortization.md` |
| PP3cyu--PP3cyw | Candidate completion remains `25/30`; fixture arithmetic is unchanged and zero global rows are promoted | PROVED | `docs/644-scaling-mechanisms-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The exact twelfth histogram is

```text
3:1, 4:4, 5:8, 6:101, 7:173, 8:239,
9:8, 10:25, 11:75, 12:146, 13:158, 14:94.
```

Five attempts have minimum transversal at most four, with sixty-one cores total.
All five correct within budget seven. The canonical `P2` offset-64 five-point
correction produces a legal ninety-six-point twelve-block state. No raw
thirteenth extension exists in radius 64.

### Localized Hall transport

The stored binary source-star fixture has one bad centre of partner degree three
and three matching-shaped centres with residual completion counts `4,6,3`. If
`b` bad centres are pruned, the mixed-degree pipeline needs `28+b` resources on
the centred side and twenty-eight on the other side. Ten copies of the numerical
four-centre pattern are the first count providing at least twenty-eight good
centres, but no geometric cross-copy theorem is known.

### Fractional direct-clean layers

All forty-eight native two-swap factorizations touch seven cells. The extra cell
is a transient source-unit cell; the eight unit cells each occur six times. A
native atomic batch must therefore protect the six-cell target circuit plus one
cancelling buffer cell.

### Support-chord repair words

A twenty-six-cell no-three source on `13 x 13` supplies thirteen anchor pairs and
passes all 4,096 run compositions with maximum coordinate magnitude 180. Its
incidence components have pair-sizes `2,2,4,5`; deleting either two-pair component
leaves an induced eleven-pair saturated source, but no anchor matching respects
those components.

### Clean-macro shells

Across `t` periods the candidate cost is `t(12+6 delta)+C`. It beats the baseline
exactly when `t(3-6 delta)>C`; fixed collateral is amortizable iff `delta<1/2`.
At zero overhead the minimum period count is `floor(C/3)+1`.

### Integration

Candidate completion remains `25/30`; the fixture fixed point and slack are
unchanged. All direct rows remain fixture-derived and the gate stays closed.

## Exact diagnostics

```bash
python scripts/check_frontier_639_644.py
```

The next available theorem identifier is `PP3cyx`.
