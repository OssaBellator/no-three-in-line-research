# Frontier pass: RI footprint-costed repairs

## New closure

- RI5hq bounds the overlap conflict graph by `h(beta-1)` and extracts at least `ceil(|Q|/[h(beta-1)+1])` footprint-disjoint repairs.
- RI5hr proves disjoint local repair maps commute, preserve the carried matching, and decrease collateral deficit by the selected batch size.
- RI5hs either executes the batch inside the typed reserve or returns the least exact resource shortage.
- RI5ht bounds cumulative repair expenditure by `kappa(Delta_0 + sum U_j)`.

## Verified finite record

Seed `731` checks 2,500 repair systems, footprint degrees, greedy extraction, typed reserve routing, and a 5,000-epoch churn-funded cost ledger.

## Remaining frontier

Construct the actual RI repair maps and footprints; prove concrete overlap, unit-cost, reserve, and replenishment bounds; charge all arithmetic/geometric effects through the occurrence-faithful ledger. The global conjecture remains open.