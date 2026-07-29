# SRR frontier pass: hole multiplicity and threshold mass

| IDs | Result | Status |
|---|---|---|
| SRR2ag | Common threshold holes are bounded by source-hole mass divided by cut size and vanish above endpoint multiplicity | PROVED |
| SRR2ah | Threshold Hall deficiency has an explicit cardinality-plus-mass bound | PROVED |
| SRR2ai | Uniform endpoint multiplicity and threshold hole mass bound the total minimum endpoint-flow cost | PROVED |
| SRR2aj | Failure returns threshold size, total hole mass, endpoint multiplicity or one small source cut | PROVED |

Canonical proof: `docs/superregular-hole-multiplicity-thresholds.md`.

## Sharpened frontier

1. Bound low-cost endpoint hole multiplicity in the actual bounded-cycle switching menus.
2. Bound total source-hole mass at every relevant event-cost threshold after conditioning.
3. Extend the resulting estimates to two-layer and multistep stationary resampling.

The exact baseline deficiency `(|A|-|S|)_+` is retained when a threshold set is smaller than the source side.