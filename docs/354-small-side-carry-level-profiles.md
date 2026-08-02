# Exact small-side carry-level profiles

This chapter refines the finite carry-multiplicity census for every saturated no-three permutation pair of sides two through five. It is a finite diagnostic, not an asymptotic carry theorem.

## PX1146 — exact peak distributions

The maximum ordered multiplicity of one nonzero signed determinant level has the following distribution across factor pairs:

| Side | Factor pairs | Peak distribution |
|---:|---:|---|
| 2 | 2 | `12:2` |
| 3 | 4 | `36:4` |
| 4 | 40 | `36:16, 42:20, 48:4` |
| 5 | 64 | `54:16, 63:16, 66:24, 72:8` |

Thus only `4/40` side-four pairs and `8/64` side-five pairs attain the previously recorded global maxima.

## PX1147 — exact determinant-support distributions

The number of positive determinant levels occurring in one factor pair is distributed as follows:

| Side | Positive-level support distribution |
|---:|---|
| 2 | `1:2` |
| 3 | `3:4` |
| 4 | `6:4, 7:20, 8:16` |
| 5 | `11:24, 12:16, 13:8, 14:16` |

Every signed histogram is exactly symmetric under `D -> -D`.

## PX1148 — refined finite carry target

The side-five cap `72` is exceptional rather than typical: `56` of the `64` factor pairs have peak multiplicity at most `66`, and `16` have peak `54`.

Any asymptotic carry theorem should therefore distinguish a small high-concentration class from the generic factor pairs, rather than applying the worst-case cap uniformly. A useful next target is a structural characterization of the pairs attaining the highest peak and an absorber or dispersion argument for that exceptional class.

No asymptotic improvement follows from these finite counts alone.

## Verification

```bash
python scripts/verify_product_carry_level_profiles.py
```
