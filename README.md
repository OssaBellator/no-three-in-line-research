# Bounded-Denominator Absorbers Research Track

**Branch:** `research/bounded-denominator-absorbers`

This branch develops the finite-denominator exception route produced by perfect-alignment and wrap-center concentration. The canonical proof notes are under `docs/`; verification programs remain under `scripts/`.

> **Status:** The branch now reaches an explicit local decoder for clean co-anchored adjacent radial pairs. The remaining bottleneck is global: regularize enough paid radial pairs, control joint collateral across their decoder states, and close every cycle of the finite profile transition quotient.

## Branch map

- [`docs/bounded-denominator-absorbers.md`](docs/bounded-denominator-absorbers.md): main dependency chain.
- [`docs/bounded-denominator-strip-proof.md`](docs/bounded-denominator-strip-proof.md)
- [`docs/bounded-denominator-local-bank.md`](docs/bounded-denominator-local-bank.md)
- [`docs/bounded-denominator-conflict-regularization.md`](docs/bounded-denominator-conflict-regularization.md)
- [`docs/bounded-denominator-product-bank.md`](docs/bounded-denominator-product-bank.md)
- [`docs/bounded-denominator-profile-localization.md`](docs/bounded-denominator-profile-localization.md)
- [`docs/bounded-denominator-finite-transition.md`](docs/bounded-denominator-finite-transition.md)
- [`docs/bounded-denominator-relative-address.md`](docs/bounded-denominator-relative-address.md)
- [`docs/bounded-denominator-primitive-slope.md`](docs/bounded-denominator-primitive-slope.md)
- [`docs/bounded-denominator-valuation-charts.md`](docs/bounded-denominator-valuation-charts.md)
- [`docs/bounded-denominator-lift-separation.md`](docs/bounded-denominator-lift-separation.md)
- [`docs/bounded-denominator-radial-pair-regularization.md`](docs/bounded-denominator-radial-pair-regularization.md)
- [`docs/bounded-denominator-radial-rectangle-decoder.md`](docs/bounded-denominator-radial-rectangle-decoder.md)
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch theorem ledger.

## Highest-value frontier

1. Turn the BDA4e/BDA4f radial-pair output into a large compatible family satisfying the BDA5d collateral inequality.
2. Classify repeated single-blocker decoder failures by the finite valuation and primitive-slope charts.
3. Prove that every directed cycle in the finite transition quotient contains an improving decoder or a terminal absorber state.

The verification scripts check finite identities and small instances only.
