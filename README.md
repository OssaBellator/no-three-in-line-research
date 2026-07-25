# Bounded-Denominator Absorbers Research Track

**Branch:** `research/bounded-denominator-absorbers`

This branch develops the finite-denominator exception route produced by perfect-alignment and wrap-center concentration. The canonical proof notes are under `docs/`; verification programs remain under `scripts/`.

> **Status:** Rank-one decoder collateral reduces to one of `36` two-role channel comparisons. All one-cell channels share the scalar state `h det(d,e)`. Repeated scalar lifts lie in one `q/g` progression, where `g=gcd(|det(d,e)|,q)`; dense recurrence has a finite transverse increment library and yields paid co-anchored genuine radial pairs `h,h+q`. Bounded row/column load feeds these pairs to the proved rectangle decoder, while high load returns one of five affine anchor chains. The former dispersed-anchor inequality is now replaced by an exact overlap-variation identity: every scalar profile yields a paid pair bank, a paid extreme-slot front, or a parity-disjoint oriented missing-partner front, with guarantees `W/4,W/4,W/8` at threshold `theta=1/2`. Mixed walls descend to a strict divisor or are coprime terminal profiles. The reflected `CD` offset is closed at denominator level: `gcd(A(2h+q),q)=gcd(2Ah,q)`, its reduced residue is a unit, and one fixed residue is a class modulo `q/gcd(2A,q)`. Extra valuation cancellation above `q` is invisible, and AC3dj--AC3dm import this exact profile into the alternating-core role dictionary. The remaining bottlenecks are installation or denominator descent for the explicit one-sided fronts, affine anchor-chain termination, heavy rank-two/rank-three profiles, support faithfulness, and recurrent finite-profile cycles.

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
- [`docs/bounded-denominator-role-valuation-collapse.md`](docs/bounded-denominator-role-valuation-collapse.md): common prime-power scalar, mixed-wall precision, and exact integer reflected valuation.
- [`docs/bounded-denominator-wall-descent.md`](docs/bounded-denominator-wall-descent.md): strict-divisor or coprime-terminal wall reduction.
- [`docs/bounded-denominator-scalar-lift-spacing.md`](docs/bounded-denominator-scalar-lift-spacing.md): `q/g` spacing and modulus-geometry duality.
- [`docs/bounded-denominator-residual-determinant.md`](docs/bounded-denominator-residual-determinant.md): transverse normal form and finite increment library.
- [`docs/bounded-denominator-scalar-q-pairs.md`](docs/bounded-denominator-scalar-q-pairs.md): extraction of genuine `h,h+q` decoder pairs.
- [`docs/bounded-denominator-gstep-coanchor.md`](docs/bounded-denominator-gstep-coanchor.md): weighted co-anchor extraction across interlaced scalar paths.
- [`docs/bounded-denominator-overlap-variation.md`](docs/bounded-denominator-overlap-variation.md): exact pair-overlap identity and endpoint/oriented missing-partner fronts.
- [`docs/bounded-denominator-reflected-scalar.md`](docs/bounded-denominator-reflected-scalar.md): exact reflected gcd, reduced unit, and scalar-slot spacing.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch theorem ledger.

## Highest-value frontier

1. Install or force strict denominator descent for the explicit endpoint and oriented missing-partner fronts from BDA5af--BDA5ah.
2. Classify the five affine anchor chains through a terminating decoder/descent alternative.
3. Apply BDA3c--BDA3e to the heavy rank-two or rank-three profile returned by BDA5j.
4. Prove that every directed cycle in the finite transition quotient contains an improving decoder, strict denominator descent, scalar-pair/front return, or terminal absorber state.
5. Prove support faithfulness for reflected and ordinary AC role outputs so the extracted co-anchor families enter executable BDA decoders.

The verification scripts check finite identities and small instances only.