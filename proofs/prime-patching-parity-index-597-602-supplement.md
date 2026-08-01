# Prime-patching parity index supplement: `docs/597--602`

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ctj--PP3ctl | All 2112 one-extra-incidence degree-preserving boundary swaps fail | PROVED / FINITE OBSTRUCTION | `docs/597-widened-degree-preserving-boundary-swap-obstruction.md` |
| PP3ctm--PP3cto | A `4 x 5` Hall host gives minimum residual blocker number two for every label injection | PROVED FOR COORDINATE HOST | `docs/598-four-by-five-hall-host-robustness.md` |
| PP3ctp--PP3ctr | One unique source augmentation admits 120 ordered legal five-layer decompositions | PROVED FOR AGGREGATE ENLARGEMENT | `docs/599-unique-five-slot-threshold-augmentation.md` |
| PP3cts--PP3ctu | Endpoint-reusing support chords have aggregate collision count `925166131890` | PROVED FOR ENCODED GEOMETRY | `docs/600-endpoint-reusing-support-chord-census.md` |
| PP3ctv--PP3ctx | The recorded shell catalogue has no odd-coset action; conditional unit actions cost `1/20` throughput | PROVED / SOURCE ABSENCE | `docs/601-recorded-shell-catalogue-coset-absence.md` |
| PP3cty--PP3cua | Candidate completion stays `23/30`; no ledger row is promoted | PROVED | `docs/602-structural-enlargement-evidence-gate.md` |

## Frontier update

The boundary repair class remains obstructed after one additional
degree-preserving swap.  By contrast, adding one Hall host column removes every
singleton residual blocker, and adding one aggregate threshold slot yields a
unique legal five-layer enlargement.  The prefix frontier now has an exact
nonzero endpoint-reuse incidence census, while the shell audit proves that the
needed odd action is absent from the recorded source catalogue.

These are structural enlargements and exact obstructions, not a proof of the
all-`n` theorem.  All actual ledger rows remain fixture-derived.

## Exact diagnostics

```bash
python scripts/check_frontier_597_602.py
```

The next available theorem identifier is `PP3cub`.
