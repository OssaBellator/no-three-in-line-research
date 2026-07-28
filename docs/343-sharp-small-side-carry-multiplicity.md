# Sharp small-side carry multiplicity

The general carry theorem bounds the number of ordered triples at one fixed nonzero signed determinant by `4n(2n-1)` for a saturated side-`n` no-three factor. This chapter records the exact small-side profiles and quantifies the finite slack.

## PX1105 — sides two and three

- Side 2 has two valid ordered factor pairs. Every pair has maximum fixed-level multiplicity 12, versus the general bound 24.
- Side 3 has four valid ordered factor pairs. Every pair has maximum fixed-level multiplicity 36, versus the general bound 60.

## PX1106 — side four profile

Among the 40 valid ordered side-four factor pairs, the per-pair maximum fixed-level multiplicity has distribution

- 36 for 16 pairs;
- 42 for 20 pairs;
- 48 for 4 pairs.

The sharp global maximum is 48, versus the general bound 112.

## PX1107 — side five profile

Among the 64 valid ordered side-five factor pairs, the per-pair maximum fixed-level multiplicity has distribution

- 54 for 16 pairs;
- 63 for 16 pairs;
- 66 for 24 pairs;
- 72 for 8 pairs.

The sharp global maximum is 72, versus the general bound 180.

## PX1108 — finite three-fifths improvement

For every saturated no-three permutation pair of sides two through five, the exact maximum is at most three-fifths of the general cap. Equality occurs only at side three.

This is a finite diagnostic, not a proof that the factor `3/5` persists for arbitrary side. It identifies a concrete strengthening of the carry multiplicity theorem worth testing before attempting second-generation collateral concentration.

## Verification

```bash
python scripts/verify_product_carry_multiplicity_sharp_small.py
```
