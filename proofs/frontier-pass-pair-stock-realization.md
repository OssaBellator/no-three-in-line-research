# Frontier pass: BDA pair-stock realization

## Added

- BDA5cg: exact realization-class partition of a disjoint pair stock.
- BDA5ch: one class retains at least a `1/K` fraction.
- BDA5ci: class-specific realization and capacity accounting.
- BDA5cj: complete realized-line router.

## Corrected frontier

A bounded-incidence heavy line now yields a quantitatively heavy context-disjoint stock in one finite realization class. Remaining work is to prove class efficiency, handle high-incidence context stars and import higher-rank events.

## Verification

`scripts/verify_bda_pair_stock_realization.py` checks class partitions and inherited quantitative bounds.