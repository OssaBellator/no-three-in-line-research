# All-n product track: repair stage update

**Branch:** `research/all-n-product-construction`

This update should be read with
[`tracks/all-n-product-construction.md`](all-n-product-construction.md).
It records the results obtained after the full degree-two product-host state
space was introduced.

## Updated ledger

| Item | Current status |
|---|---|
| PC1 | **COMPLETE.** Every spanning degree-two state in the four-regular factor-product host is saturated and decomposes into two permutation layers. |
| PC2 | **SUBSTANTIAL PARTIAL.** The complete flattened collinearity equation has at most quadratic multiplicity inside one fixed projection fibre. Type-`(2,2)` weighted-direction signatures have a sharper linear opposite-factor bound. Global elimination remains open. |
| PC3 | **OPEN.** Exact phase and full-selector 3-CNFs exist, but both unmodified global-host routes have finite obstructions. |
| PC4 | **OPEN.** No infinite multiplicative closure class is known. |
| PC5 | **OPEN.** Exact side-6, side-8, and side-9 certificates exist, without arithmetic coverage. |
| PC6 | **SUBSTANTIAL PARTIAL.** The repair graph is connected and has an exact cycle-collateral identity. Pure monotone descent and its natural pair-line refinement are refuted. In the canonical crossed side-six host, every bad state nevertheless has an improving endpoint within two cycle toggles, with maximum uphill barrier one. |

## New proved components

- **PX13:** complete projection-fibre concentration;
- **PX14:** sharp direction multiplicity for type `(2,2)`;
- **PX15:** exact alternating-cycle collateral identity;
- **PX18:** exact two-cycle batch improvement in the canonical crossed side-six
  host.

## New refutations

- **PX16:** every bad state has a triple-count-improving one-cycle toggle;
- **PX17:** lexicographic triple count plus pair-line energy guarantees
  monotone repair.

## Exact next target

A useful replacement for monotone repair would prove one of the following.

1. **Bounded-uphill batch theorem.** Every feasible bad product-host state has a
   bounded batch of cycle toggles with a lower-potential endpoint and
   intermediate collateral controlled by projection-fibre loads.
2. **Resampling-or-infeasibility theorem.** The exact full-selector 3-CNF either
   admits a no-three degree-two model or produces a structured certificate such
   as the exhaustive `2 x 5` obstruction.
3. **Enlarged-host theorem.** Add factor-compatible offsets or non-global digit
   maps so that the finite infeasible hosts acquire a sufficiently regular
   repair space.

The principal missing ingredient is now global coordination between many
quadratically bounded projection fibres, rather than an elementary carry or
line-multiplicity estimate.

## Verification

```bash
python scripts/verify_product_hybrid_repair.py
python scripts/verify_product_two_cycle_batch.py
```
