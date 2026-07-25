# Bounded-Denominator Absorbers Research Track

**Branch:** `research/bounded-denominator-absorbers`

This branch develops the finite-denominator exception route produced by perfect-alignment and wrap-center concentration. The canonical proof notes are under `docs/`; verification programs remain under `scripts/`.

> **Status:** BDA4e-compatible clean radial pairs admit a full heterogeneous decoder product. Rank-one collateral reduces to one of `36` two-role channel comparisons. All one-cell channels now share the same prime-power determinant state `h det(d,e)`; mixed walls either descend to the strict divisor `q/gcd(h,q)` or are coprime terminal profiles, while the reflected `CD` channel has one scalar cancellation tower. The remaining bottleneck is classification of the visible scalar and integer lifts, the heavy rank-two/rank-three profile, clean-support failure, and recurrent finite-profile cycles.

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
- [`docs/bounded-denominator-heterogeneous-decoder-product.md`](docs/bounded-denominator-heterogeneous-decoder-product.md): simultaneous local menus and exact product collateral.
- [`docs/bounded-denominator-rank-one-collateral.md`](docs/bounded-denominator-rank-one-collateral.md): balanced-floor decomposition and deterministic rank-one suppression.
- [`docs/bounded-denominator-balanced-floor-localization.md`](docs/bounded-denominator-balanced-floor-localization.md): four occupancy types and two-role arithmetic localization.
- [`docs/bounded-denominator-role-geometry.md`](docs/bounded-denominator-role-geometry.md): determinant-address comparison of the two decoder roles.
- [`docs/bounded-denominator-role-slope-dictionary.md`](docs/bounded-denominator-role-slope-dictionary.md): explicit primitive directions and heavy-slope/spread routing.
- [`docs/bounded-denominator-role-valuation-collapse.md`](docs/bounded-denominator-role-valuation-collapse.md): common prime-power scalar, mixed-wall precision, and `CD` cancellation profile.
- [`docs/bounded-denominator-wall-descent.md`](docs/bounded-denominator-wall-descent.md): strict-divisor or coprime-terminal wall reduction.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch theorem ledger.

## Highest-value frontier

1. Classify repeated visible scalar lifts of `h det(d,e)` and the `CD` cancellation scalar inside the finite transition quotient.
2. Apply BDA3c--BDA3e to the heavy rank-two or rank-three profile returned by BDA5j.
3. Classify clean-support failure and the five affine anchor-chain outputs from BDA4e.
4. Prove that every directed cycle in the finite transition quotient contains an improving decoder, strict denominator descent, or a terminal absorber state.

The verification scripts check finite identities and small instances only.