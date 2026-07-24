# All-n product track: blockwise and affine stage

**Branch:** `research/all-n-product-construction`

This addendum records the product-track results after non-global blockwise digit
maps were introduced.  Read it with
[`tracks/all-n-product-construction.md`](all-n-product-construction.md) and the
product-specific theorem index
[`proofs/product-theorem-index.md`](../proofs/product-theorem-index.md).

## Current ledger

| Item | Current status |
|---|---|
| PC1 | **COMPLETE / ENLARGED.** Arbitrary blockwise fine-digit permutations preserve the simple four-regular factor-product host; every degree-two state is saturated and decomposes into two permutation layers. |
| PC2 | **SUBSTANTIAL PARTIAL.** Global-radix determinant and projection-fibre bounds remain valid for the original hosts. Non-global block maps require host-specific integer determinant checks or a new piecewise formula. |
| PC3 | **OPEN / FINITE ESCAPE AND FINITE OBSTRUCTIONS.** Blockwise reversal gives an exact side-ten solution and defeats the unmodified `2 x 5` gap for selected factors. The complete reversal census and normalized affine censuses show that neither reversal nor normalized affine maps are universal. |
| PC4 | **OPEN.** No infinite multiplicative closure class is proved. |
| PC5 | **OPEN / FINITE CERTIFICATES.** Product-derived exact saturated configurations are recorded at sides 6, 8, 9, and 10, without arithmetic coverage. |
| PC6 | **SUBSTANTIAL PARTIAL.** The full-selector repair graph is connected and admits composite balanced trades. Block maps enlarge the host geometry, but no uniform resampling-or-infeasibility theorem is known. |

## New exact results

- **PX28:** fixing one inner permutation while retaining both outer layers gives
  an explicit `O(mn)` saturated blockwise product.
- **PX29:** among the sixteen identity/reversal assignments at `2 x 5`, exactly
  the four varying in both row and column blocks succeed; each has 13 successful
  factor/orientation hosts involving 9 of 32 layer-unordered side-five factors.
- **PX30:** the simultaneous-reversal one-inner-layer family is completely
  classified through base side eight.
- **PX31:** among 70,400 normalized affine one-inner-layer states at `2 x 5`,
  exactly three succeed; all use reversal/reversal and yield the same side-ten
  configuration.
- **PX32:** the canonical side-five factor from the 35-line core remains
  full-selector infeasible in all 1,600 normalized affine second-block hosts.

## Interpretation

The quantified global-host obstruction PX23 is not intrinsic to the ambient
`10 x 10` grid or to factor-compatible composition: non-global block maps remove
it for selected factors.  The positive mechanism is nevertheless rigid.

1. Variation in both coarse row and coarse column block maps is necessary inside
   the identity/reversal family.
2. Normalized affine translations and non-reversal multipliers create no new
   one-layer scalar witness.
3. Even the exact full selector cannot rescue the canonical 35-line factor using
   normalized affine second-block maps.

## Exact next targets

1. **All-block affine census or theorem.** Allow affine maps independently in
   every coarse block and identify valid normalizations justified by genuine
   affine symmetries of the scalar grid.
2. **Non-affine map selection.** Choose block permutations from factor secant
   signatures rather than from a fixed affine family.
3. **Core-guided enlargement.** Determine which cell movements or block maps
   hit every clause of the canonical 35-line core while preserving four-regular
   saturation.
4. **Model-or-core theorem.** Extend the exact full-selector CNF to return either
   a no-three degree-two state or a bounded structured infeasibility certificate.

## Verification

```bash
python scripts/verify_product_blockwise_digits.py
python scripts/verify_product_blockwise_reversal.py
python scripts/verify_product_one_layer_classification.py
python scripts/verify_product_affine_one_layer.py
python scripts/verify_product_canonical_affine_full_selector.py
python scripts/verify_product_2x5_unsat_core.py
```

All statements remain finite or structural.  The branch still has no
multiplicative closure theorem or arithmetic coverage theorem.
