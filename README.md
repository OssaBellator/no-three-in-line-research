# Rational Inverse Expansion Research Track

**Branch:** `research/rational-inverse-expansion`

This branch studies simultaneous structure of a multiplicative set and its image under the rational secant map, including collision involutions, subgroup-coset overlap, quotient cycles, order-two obstructions, and the physical-lift interface needed by absorber banks. Canonical proofs are under `docs/`.

> **Status:** Scale-localized physical completion debt decomposes into closed permutation components. Opposite-layer occupancy is resolved by a global blocker derangement whenever the number of blocked desired cells is zero or at least two. Exactly one blocked desired cell leaves one explicit alternating component, and that component is rigid: no nontrivial current/target mixture preserves the active matching. The remaining bottleneck is therefore an actual blocker move, external-cell extension, or arithmetic delegation, together with collateral comparison for installed components.

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
- [`docs/rational-inverse-two-layer-completion.md`](docs/rational-inverse-two-layer-completion.md): blocker derangements and the singleton-blocker alternative.
- [`docs/rational-inverse-singleton-rigidity.md`](docs/rational-inverse-singleton-rigidity.md): proof that partial current/target installation cannot bypass one blocker.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch-specific theorem ledger.

## Highest-value frontier

1. Move or absorb the unique blocker in the heavy RI5i/RI5k component using its quotient, scale, carry, and path labels.
2. Bound collateral for the jointly installed RI5h completion components and feed failure into the paid-bank profile machinery.
3. Install the conditional fixed-edge coset bank after the singleton debt is absorbed or delegated.

The scripts verify finite-field identities and small quotient/lift models; they do not replace the arbitrary-size proofs.