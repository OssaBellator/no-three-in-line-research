# Prime-patching parity index supplement: `docs/645--650`

This supplement continues the cumulative PP3 index after `docs/644`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cyx--PP3cyz | The corrected twelve-block state has an exact thirteenth spectrum; all ninety-three best cores correct within budget seven; a four-point transition reaches thirteen blocks | PROVED | `docs/645-corrected-thirteenth-boundary-transition.md` |
| PP3cza--PP3czc | `t` source motifs with `e` extra corruptions retain exactly `3t-e` good centres, giving sharp finite and rate-dependent Hall thresholds | PROVED / CONDITIONAL INTERFACE | `docs/646-bad-centre-amplification.md` |
| PP3czd--PP3czf | The target--transient graph is connected 3-regular, has forty-nine perfect matchings, and yields 12,544 ordered distinct-buffer batches | PROVED / FINITE REDUCTION | `docs/647-distinct-transient-threshold-batching.md` |
| PP3czg--PP3czi | The canonical thirteen-pair source has no insertion-plus-local-transposition extension to fourteen pairs; the exact neighbourhood minimum is three triples | PROVED / LOCAL OBSTRUCTION | `docs/648-fourteen-pair-local-extension-obstruction.md` |
| PP3czj--PP3czl | Recurring shell collateral is asymptotically affordable exactly when `6*delta+c<3`; fixed setup is separately amortizable | PROVED / CONDITIONAL SOURCE COLUMN | `docs/649-recurring-shell-collateral-barrier.md` |
| PP3czm--PP3czo | Candidate completion stays `25/30`, fixture arithmetic is unchanged, and zero global rows are promoted | PROVED | `docs/650-uniformity-frontier-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The radius-64 thirteenth minimum-transversal histogram is

```text
3:3, 4:8, 5:25, 6:84, 7:163, 8:240,
9:15, 10:37, 11:123, 12:135, 13:135, 14:64.
```

The eleven attempts of minimum size at most four have ninety-three minimum cores.
Every core corrects within budget seven, with minimum budget distribution
`4:19, 5:45, 6:26, 7:3`.  The canonical `P0` offset-56 four-point transition
gives a legal 104-point thirteen-block state.  No raw fourteenth block survives
in radius 64.

### Localized Hall transport

For `t` disjoint four-centre source motifs and `e` additional corruptions, exactly
`3t-e` good centres remain.  The numerical interface is `3t-e>=28`.  Ten motifs
suffice without extra corruption and tolerate two; a third requires eleven.
Cross-copy geometry and the two degree-two restricted families remain open.

### Fractional direct-clean layers

The eight targets and eight transient cells form a connected 3-regular bipartite
graph.  It has forty-nine perfect matchings.  Choosing one and one of two swap
orders per incidence gives `49*2^8=12544` ordered eight-target batches with no
buffer-cell reuse.  Intermediate legality is still missing.

### Support-chord repair words

The canonical thirteen-pair source has no no-three extension in the complete
23,273-candidate neighbourhood obtained by row-column insertion plus at most one
layer transposition.  The unique minimum has three triples, and 25,229 valid
ordered move sequences of length at most two from that minimum do not improve it.
A fourteen-pair source needs nonlocal rearrangement or a different family.

### Clean-macro shells

For `k` periods, recurring collateral `c`, per-use overhead `delta`, and fixed
setup `S`, exact cost is `k(12+6*delta+c)+S`.  Fixed setup can be amortized, but
recurring burden must satisfy `6*delta+c<3`.  At unit macro cost, at most two
integer recurring controls per period are affordable.

### Integration

Candidate completion remains `25/30`.  The fixture fixed point and positive
slack are unchanged.  Every actual row remains fixture-derived.

## Exact diagnostics

```bash
python scripts/check_frontier_645_650.py
```

The next available theorem identifier is `PP3czp`.
