# Rational Inverse Expansion Research Track

**Branch:** `research/rational-inverse-expansion`

This branch studies simultaneous structure of a multiplicative set and its image under the rational secant map, including collision involutions, subgroup-coset overlap, quotient cycles, order-two obstructions, and the physical-lift interface needed by absorber banks. Canonical proofs are under `docs/`.

> **Status:** Scale-localized physical completion debt decomposes into closed permutation components, and all opposite-layer occupancy patterns are now executable. Zero blockers install directly, multiple blockers use a derangement, and a singleton blocker is moved by transposition with any auxiliary blocker cell. The remaining bottleneck is collateral: compare the completed active matching and the auxiliary-transposition bank against the paid fixed-edge mass, or classify the failed profile whose raw blocker collateral grows linearly with `n-1`.

## Branch map

- [`docs/rational-inverse-expansion.md`](docs/rational-inverse-expansion.md): main dependency chain.
- [`docs/rational-inverse-collision-and-obstructions.md`](docs/rational-inverse-collision-and-obstructions.md)
- [`docs/rational-inverse-subgroup-overlap.md`](docs/rational-inverse-subgroup-overlap.md)
- [`docs/rational-inverse-union-collision.md`](docs/rational-inverse-union-collision.md)
- [`docs/rational-inverse-cross-coset-cap.md`](docs/rational-inverse-cross-coset-cap.md)
- [`docs/rational-inverse-target-cosets.md`](docs/rational-inverse-target-cosets.md)
- [`docs/rational-inverse-weil-overlap.md`](docs/rational-inverse-weil-overlap.md)
- [`docs/rational-inverse-fibre-energy.md`](docs/rational-inverse-fibre-energy.md)
- [`docs/rational-inverse-quotient-boundary.md`](docs/rational-inverse-quotient-boundary.md)
- [`docs/rational-inverse-boundary-gcd.md`](docs/rational-inverse-boundary-gcd.md)
- [`docs/rational-inverse-quotient-cycles.md`](docs/rational-inverse-quotient-cycles.md)
- [`docs/rational-inverse-fixed-edge-bank.md`](docs/rational-inverse-fixed-edge-bank.md)
- [`docs/rational-inverse-lift-coherence.md`](docs/rational-inverse-lift-coherence.md)
- [`docs/rational-inverse-completion-debt.md`](docs/rational-inverse-completion-debt.md): cycle/path decomposition of physical completion debt.
- [`docs/rational-inverse-two-layer-completion.md`](docs/rational-inverse-two-layer-completion.md): blocker derangements and the provisional singleton case.
- [`docs/rational-inverse-singleton-rigidity.md`](docs/rational-inverse-singleton-rigidity.md): proof that partial current/target installation cannot bypass one blocker.
- [`docs/rational-inverse-singleton-transposition.md`](docs/rational-inverse-singleton-transposition.md): auxiliary blocker transposition and exact `1/(n-1)` collateral bank.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch-specific theorem ledger.

## Highest-value frontier

1. Bound the active and blocker collateral of the RI5l--RI5n completed state, or localize a failed profile using its two crossed-cell channels.
2. Convert the resulting heavy blocker profile into alternating-core, carry, or bounded-denominator structure.
3. Complete the bank-ready audit and invoke the conditional fixed-edge coset bank.

The scripts verify finite-field identities and small quotient/lift models; they do not replace the arbitrary-size proofs.
