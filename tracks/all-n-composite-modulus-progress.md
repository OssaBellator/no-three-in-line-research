# Composite-modulus track: current progress and revised bottlenecks

This is the current addendum to
[`tracks/all-n-composite-modulus.md`](all-n-composite-modulus.md). The detailed
claims are indexed in
[`proofs/composite-modulus-theorem-index.md`](../proofs/composite-modulus-theorem-index.md).

## Current state of CM1–CM6

### CM1 — nonlinear full channels and saturated banks: substantial completion

Valuation-completed reciprocals are full nonlinear permutation channels at
every prime power. They preserve every valuation stratum, including all
nonunits. A universal affine row companion produces a disjoint saturated pair
whose row-column graph is one alternating Hamiltonian cycle.

The entire pair now decomposes into `N/p` column blocks of size `p`. Both
layers may be permuted independently inside every block, giving

\[
(p!)^{2N/p}
\]

executable saturated states with an exact product cylinder law.

### CM2 — real line cap: narrowed but open

For odd prime powers, every line intersection reduces to simple lower
valuation roots plus one possible top Hensel-tangent cell. The coarse cap is

\[
O(\sqrt N+\log N).
\]

CMR11 adds exact real geometry: tangent roots lie in one or two spaced residue
classes, and an unbalanced Euclidean slope shortens the feasible coordinate
interval by the coefficient ratio. Large cells must therefore be both
`p`-adically singular and slope-balanced.

A constant or repairable uniform line cap is still open.

### CM3 — displacement and syndrome: obstruction localized and banked

Same- and cross-channel secants have explicit valuation quadratics and
mixed-layer carry identities. The one-channel triple syndrome is bounded by

\[
O(N^{5/2}+N^2\log N).
\]

CMR14 proves that completed reciprocals cannot have bounded same-channel
displacement multiplicity: one exact top-digit displacement repeats at least

\[
\frac{p-1}{p^2}N
\]

times. CMR15–CMR17 then identify these collisions as internal to disjoint
`p`-point blocks and install full executable permutation banks with exact
spread. CMR19–CMR22 extend the block system through every valuation stratum and
both layers.

Thus the bounded-codegree target is refuted, but the structured-collision
replacement is complete. The missing result is a weighted cross-block
certificate bound.

### CM4 — prime-power carry calculus: decoder space constructed

The branch now contains:

- valuation-stratum line quadratics;
- exact odd-prime square-root multiplicities;
- one singular top tangent cell;
- same-channel displacement products;
- companion cross-displacement quadratics;
- a universal mixed-layer determinant carry identity;
- exact top-digit collision blocks in every valuation stratum;
- independent full permutation banks in both layers;
- an exact normalized one-, two-, and three-cell certificate expectation.

The remaining decoder theorem is no longer existential. It must bound the
normalized certificate mass of the explicit CMR21 product bank, or show that a
large mass forces a smaller structured absorber.

### CM5 — CRT assembly: open

Real triples always project to modular triples, but naive coordinatewise CRT
products contain mixed-projection triples. No ordered-box assembly theorem yet
handles cases where different point pairs collapse in different factors.

### CM6 — coverage: finite and one-layer digital progress

Exact saturated no-three configurations are recorded at composite side lengths

\[
4,6,8,9,10.
\]

Binary digit-linear one-channel no-three permutations are verified at

\[
8,16,32,64.
\]

The `64`-point matrix is a direct extension of an alternate `32`-point matrix,
but all `4096` invertible direct one-bit block extensions of it fail at `128`.
No scalable saturated class is known.

## Revised bottlenecks

1. **Global block-bank certificate bound.** Bound the CMR22 weighted mass of
   real-collinear certificates in the all-stratum two-layer bank by a
   repairable quantity, preferably `o(1)` after conditioning or multiscale
   cleaning.
2. **Balanced tangent-cell theorem.** Bound exact real populations when the
   discriminant is highly divisible and the line coefficients have comparable
   magnitude. CMR11 already handles the unbalanced regime.
3. **Cross-block codegree after contraction.** Prove that contracting each
   top-digit block removes all linear displacement concentration and leaves a
   small weighted secant shadow.
4. **Digital saturation at 64.** Pair the CMR12 permutation with a second
   disjoint permutation layer without creating a real triple.
5. **Non-block digital lift to 128.** Search all-block modifications or
   triangular nonlinear Boolean terms; direct one-bit extension is refuted.
6. **Mixed-projection CRT signature.** Add a signature recording which pair
   collapses in each local factor and force either a small global determinant
   or an absorbable collision pattern.

## Checks

```bash
python scripts/verify_prime_power_tangent_digital.py --max-modulus 125
python scripts/verify_prime_power_displacement_obstruction.py --max-modulus 343
python scripts/verify_prime_power_top_digit_blocks.py --max-modulus 125
python scripts/verify_prime_power_companion_blocks.py --max-modulus 125
python scripts/verify_prime_power_block_collateral.py
python scripts/verify_prime_power_all_stratum_bank.py --max-modulus 125
```

These are finite exact checks. They do not constitute a complete all-`n`
construction.
