# BDA frontier pass: line-pair payment

**Branch:** `research/bounded-denominator-absorbers`

## New theorem block

- **BDA5cc:** bounded context-cell incidence gives a weighted matching of size at least `W_L/(2d-1)`.
- **BDA5cd:** high-incidence context-star versus disjoint-pair dichotomy.
- **BDA5ce:** the matching provides capacity-one context-cell ticket stock.
- **BDA5cf:** complete connector/resonant/radial heavy-line router.

## Executable check

`scripts/verify_bda_line_pair_matching_router.py`

Equivalent local execution verified **3,308** weighted line-pair graphs.

## Updated frontier

Every heavy off-diagonal line now yields either one high-incidence context cell or a large vertex-disjoint pair family. Remaining work is to bound/pay the context-star incidence, realize payment or tickets on the disjoint pairs, route owners, and import higher-rank events.