# Rational-inverse cumulative integrated physical-collateral bank

This note records RI5ee--RI5ei. It extends the integrated physical-source/collateral/demand network through repeated epochs with exact current balances.

## Contract

Fix physical source classes `P`, collateral classes `C`, combined owner/charge demand classes `D`, and complete relations `P -> C` and `C -> D`. Current physical and collateral balances are integral. Named exogenous deposits enter only their exact physical class before an epoch.

## Theorem block

### RI5ee — current two-level balances

Initial balances, named physical deposits and actual flow debits determine every later physical and collateral balance exactly.

### RI5ef — epoch integrated payment

At each epoch one max-flow simultaneously chooses physical collateral issuance, use of existing collateral and payment of combined owner/charge demand.

### RI5eg — cumulative conservation

Across every fully paid prefix, physical issuance plus remaining physical mass equals initial plus deposited physical mass, while collateral use never exceeds existing collateral plus issued mass.

### RI5eh — first mixed failure cut

The first unpaid epoch returns one canonical physical-source/collateral/demand minimum cut whose deficit equals current unpaid mass.

### RI5ei — reset boundary

Changed owner fields, collateral addresses, compatibility, hidden deposits, splitting, source-less creation or missing predecessor lineage returns reset or amplification.

## Finite audit

Run `python scripts/verify_ri_cumulative_integrated_physical_collateral_bank.py`.

The audit checks 5,000 systems and 8,408 epochs: 17,525 physical, 17,436 collateral and 17,577 demand classes; 67,732 compatibility arcs; 44,553 named physical deposits; 71,704 demand units; 64,254 paid and 7,450 unpaid units; and 2,012 first deficient epochs.

## Scope

The theorem does not construct the arithmetic compatibility graph or prove genuinely free owner sources. It does not prove RI6 or the no-three-in-line conjecture.
