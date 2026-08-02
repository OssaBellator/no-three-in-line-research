# Threshold transient buffer-cell catalogue

`docs/635` proves that each desired threshold change is an indivisible
alternating `C6` in the transportation kernel. This chapter determines the exact
extra footprint required when that atom is represented by the repository-native
pair of conservative `2x2` swaps.

## 1. Seven-cell batch footprint

### Theorem PP3cyl — PROVED / ONE TRANSIENT CELL PER FACTORIZATION

Every one of the forty-eight ordered two-swap factorizations has union support of
size seven. Six cells are the target alternating `C6`; the seventh cell is
changed by the first swap and cancelled by the second.

#### Proof

Enumerate all conservative swaps from the stored source matrix and all second
swaps reaching one of the eight nearest legal targets. Compare the union of the
two four-cell supports with the six-cell source-target difference. Every record
has sizes `7` and `1`. ∎

## 2. Complete transient-cell catalogue

### Theorem PP3cym — PROVED / EIGHT BALANCED BUFFER CELLS

The possible transient cells are exactly the eight source cells of multiplicity
one:

```text
(0,1), (0,2), (1,2), (1,3),
(2,0), (2,3), (3,0), (3,1).
```

Each transient cell occurs in exactly six ordered factorizations.

#### Proof

`scripts/check_threshold_transient_cell_batch.py` counts the transient singleton
for every ordered factorization. The support is precisely the set of unit entries
of the source matrix, and the multiplicity distribution is constant six. ∎

## 3. Geometric source obligation

### Theorem PP3cyn — PROVED / MINIMUM NATIVE BATCH EXPOSURE

Any realization that batches two repository-native conservative swaps must
protect a seven-cell footprint: the full six-cell circuit plus one cancelling
source-unit buffer cell. A six-cell exposed operation cannot be obtained merely
by hiding the intermediate ordering of two ordinary swaps.

#### Proof

The first assertion is `PP3cyl`; `PP3cym` shows that the extra cell is unavoidable
for every factorization and identifies every possible choice. ∎

## Consequence

The remaining threshold task is now geometric and finite in type: realize one of
eight seven-cell batches with legal exposed states, or introduce a genuinely new
primitive whose support is the six-cell circuit itself.
