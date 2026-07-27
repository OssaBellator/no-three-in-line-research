# Sparse Algebraic Spread Research Track

**Branch:** `research/sparse-algebraic-spread`

This branch studies explicit sparse algebraic hosts with perfect-matching spread, exact switching ratios, zero-conflict block embeddings, and balanced compression back to the standard grid. Branch proofs are canonical under `docs/`.

> **Status:** The sparse block host and its matching distribution are understood substantially better than the final standard-grid compression. The concentrated SAS5i swap certificate has now been developed through exact destruction/repair words, divisor and dilation arithmetic, weighted parameter-chain batching, donor execution, two-swap mixed-curvature ledgers, matched-square composition, aggregate negative-collateral installation, and opposite-destroyer payment. SAS5gq--SAS5gt additionally show that a composed-only output cannot immediately recycle on the same operation square: after rebasing at the composed state its full weight is current-only payment for the reverse square. The remaining bottlenecks are global aggregate barrier payment, changed-signature recycling cycles, legality of the creator/opposite-destroyer squares in every word family, failed-incidence neutral output, and boundary/high-incidence profiles.

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
- [`docs/sparse-concentrated-swap-words.md`](docs/sparse-concentrated-swap-words.md): finite destruction/repair words and exact swap addresses.
- [`docs/sparse-weighted-parameter-chain-batching.md`](docs/sparse-weighted-parameter-chain-batching.md): weighted common-step extraction.
- [`docs/sparse-common-step-pair-execution-router.md`](docs/sparse-common-step-pair-execution-router.md): compatible execution of common-step pairs.
- [`docs/sparse-matched-repair-square-composition.md`](docs/sparse-matched-repair-square-composition.md): physical two-stage matched-square composition.
- [`docs/sparse-negative-collateral-physical-installation.md`](docs/sparse-negative-collateral-physical-installation.md): installation of aggregate negative collateral.
- [`docs/sparse-opposite-destroyer-payment.md`](docs/sparse-opposite-destroyer-payment.md): opposite-destroyer payment and recycled output routing.
- [`docs/sparse-composed-only-reversal.md`](docs/sparse-composed-only-reversal.md): involutive reversal of composed-only output to current payment.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch-specific theorem ledger.

## Highest-value frontier

1. Pay or terminate aggregate creator and opposite-swap barriers across many operation squares.
2. Prove that changed-signature composed-output trajectories consume new finite addresses, descend, or enter one exact recurrent profile cycle.
3. Establish mixed-orientation creator and opposite-destroyer legality for every localized arithmetic word family, including base-state single-swap admissibility.
4. Batch neutral outputs when global incidence caps fail and classify the returned high-incidence column or constraint fibres.
5. Resolve positive-base-row realization, heavy-parameter comparison, boundary profiles, and exact balanced standard-grid compression.

The scripts in `scripts/` exhaust small instances and verify the displayed identities; they are not proofs for arbitrary size.
