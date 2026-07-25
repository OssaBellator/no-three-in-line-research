# Sparse Algebraic Spread Research Track

**Branch:** `research/sparse-algebraic-spread`

This branch studies explicit sparse algebraic hosts with perfect-matching spread, exact switching ratios, zero-conflict block embeddings, and balanced compression back to the standard grid. Branch proofs are canonical under `docs/`.

> **Status:** The sparse block host and its matching distribution are understood substantially better than the final standard-grid compression. The current sharp frontier is the arithmetic classification or batching of high-load two-column swap certificates returned by SAS5i.

## Branch map

- [`docs/sparse-algebraic-spread.md`](docs/sparse-algebraic-spread.md): main dependency chain.
- [`docs/sparse-block-host-spread.md`](docs/sparse-block-host-spread.md)
- [`docs/sparse-four-cycle-switching.md`](docs/sparse-four-cycle-switching.md)
- [`docs/sparse-general-switching-ratio.md`](docs/sparse-general-switching-ratio.md)
- [`docs/sparse-spread-composition.md`](docs/sparse-spread-composition.md)
- [`docs/sparse-expanded-grid-zero-conflict.md`](docs/sparse-expanded-grid-zero-conflict.md)
- [`docs/sparse-zero-energy-blocks.md`](docs/sparse-zero-energy-blocks.md)
- [`docs/sparse-block-affine-energy.md`](docs/sparse-block-affine-energy.md)
- [`docs/sparse-block-host-geometric-obstruction.md`](docs/sparse-block-host-geometric-obstruction.md)
- [`docs/sparse-balanced-compression-energy.md`](docs/sparse-balanced-compression-energy.md)
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch-specific theorem ledger.

## Highest-value frontier

1. Batch several SAS5i high-load swaps with disjoint or controlled scopes.
2. Classify repeated high-load column-pair and label patterns arithmetically.
3. Preserve zero-conflict block geometry while compressing to an exactly balanced standard-grid colouring.

The scripts in `scripts/` exhaust small instances and verify the displayed identities; they are not proofs for arbitrary size.
