# Frontier pass: complete prime-minus-one AN seed census

## Active branch

`agent/ac-prime-seed-census`

Only AC is active. Historical branches are used as immutable theorem libraries.

## Theorem block

- **AC5nk:** exact finite high-secant seed counts through `p=37`.
- **AC5nl:** complete two-layer state guardrail.
- **AC5nm:** canonical improving transfer seeds at `p=19,23,29`.
- **AC5nn:** explicit nonimproving `p=31` AN bank.
- **AC5no:** exact AC1 normalized heavy rank at `p=31`.
- **AC5np:** explicit heavy anchor `(12,12)` of degree 20.
- **AC5nq:** complete `p=31` split into 140 improving and 76 nonimproving orientations.
- **AC5nr:** strongest canonical `p=31` decrease `108 -> 75`.
- **AC5ns:** exact six-direction decomposition of the heavy-anchor family.

## Main finite results

The first tested prime with a seven-pair seed in this precise family is `p=19`. The retained orientation counts at `p=19,23,29,31,37` are

`56, 144, 600, 216, 2512`.

At `p=31`, complete bank evaluation gives:

- retained seed orientations: `216`;
- improving orientations: `140`;
- nonimproving orientations: `76`;
- maximum exact decrease: `33`.

The strongest recorded seed uses `H_1`, `H_12`, switch rows `16,24`, candidate `(16,16)`, and has:

- bank size: `1094`;
- current potential: `108`;
- fixed potential: `59`;
- best potential: `75`;
- improving states: `1083`.

The canonical failure seed uses `H_1`, `H_2`, switch rows `4,16`, candidate `(16,16)`. Its complete 1088-state bank has minimum potential 108 against current potential 106.

AC1 selects rank one. The heaviest anchor cell `(12,12)` supports 20 certificates, split by line direction as

`10, 6, 1, 1, 1, 1`.

The first two classes are the diagonal and anti-diagonal and contain 16 of the 20 occurrences. They are created mixed-source collateral, not current payment.

## Corrected computation

An earlier exploratory calculation omitted unchanged switch-layer points and therefore reported invalid low successor potentials. The committed verifier includes every unchanged point of both layers and asserts full state cardinality before evaluating collateral. The incorrect values are not used by any theorem.

## Validation

Run:

`python scripts/verify_ac_prime_seed_census.py`

The corrected deterministic audit reconstructs all displayed prime counts, exhausts all 216 p=31 orientations, verifies both explicit seeds and checks the complete-state regression guardrail.

## Next frontier

1. Continue the explicit 75-potential p=31 successor.
2. Classify the mixed-source rich-line AC1 return.
3. Seek a uniform arithmetic predictor for improving versus nonimproving seeds.
4. Extend the census and terminal-path search to further prime-minus-one boards.

AC6 and the global no-three-in-line conjecture remain open.
