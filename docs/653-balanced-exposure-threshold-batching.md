# Balanced-exposure threshold batching

This chapter refines the 49 distinct-transient assignments from
`docs/647-distinct-transient-threshold-batching.md`. It classifies all swap-order
choices by intermediate-state collisions and exposed-cell load.

## PP3czv — Complete ordered-batch collision census

There are 49 perfect matchings between the eight nearest legal targets and the
eight transient source cells. Each matched target-cell incidence has two swap
orders, giving `49*2^8 = 12,544` ordered distinct-buffer batches.

The number of distinct intermediate matrices in a batch has exact histogram

```text
4:7, 5:84, 6:634, 7:2804, 8:9015.
```

Thus distinct transient buffers do not force distinct exposed intermediate
matrices. The union of changed cells across the eight intermediates has exact
histogram

```text
14:164, 15:2808, 16:9572.
```

## PP3czw — Sharp exposure-balance theorem

Each of the eight first swaps changes four matrix cells, so every batch has 32
cell-exposure incidences on a 16-cell matrix. Therefore some cell is exposed at
least twice.

Across all 12,544 batches, the maximum per-cell exposure has exact histogram

```text
2:49, 3:1553, 4:7970, 5:2972.
```

Exactly 49 batches attain the lower bound two. In each such batch every one of
the 16 cells is exposed exactly twice. Moreover, each of the 49 transient-cell
perfect matchings has exactly one swap-order choice with this perfectly balanced
exposure profile.

This gives a canonical order selection for every distinct-buffer assignment.

## PP3czx — Balanced exposure does not restore legality

For each of the 49 perfectly balanced batches, none of its eight intermediate
matrices belongs to the legal four-layer matrix set. Thus all 392 balanced
intermediate occurrences remain matrix-illegal.

The obstruction is sharp at the matrix interface: buffer reuse and exposure
imbalance can both be eliminated, but the exposed states are still illegal. A
geometric source primitive must therefore hide the intermediate states, replace
the two-swap factorization, or prove a stronger notion of protected exposure.

## Reproducibility

Run

```bash
python scripts/check_threshold_balanced_exposure_batch.py
```

The checker reconstructs the legal-layer matrices, all 48 ordered two-swap
factorizations, all 49 perfect matchings, and all 12,544 order selections.
