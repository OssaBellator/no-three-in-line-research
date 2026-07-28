# Sparse cumulative integrated physical-move bank

This note records SAS5kk--SAS5ko. It composes physical neutral-source issuance with the joint sign-pair/completion demand bank across repeated epochs.

## Contract

Fix physical neutral-source classes `P`, neutral-move classes `M`, and mixed demand classes `D` containing sign-pair costs and completion tasks. Retain complete relations `P -> M` and `M -> D`. Current physical and move balances are integral, and named deposits enter only exact physical classes.

## Theorem block

### SAS5kk — current physical and move balances

Initial balances, named physical deposits and actual flow debits determine every later physical-source and neutral-move balance exactly.

### SAS5kl — epoch integrated payment

One maximum flow simultaneously chooses physical move issuance, use of existing move balance and payment of pair plus completion demand.

### SAS5km — cumulative shared-capacity identity

Across every fully paid prefix, pair and task debits use each neutral-move unit at most once, while physical issuance never exceeds initial plus deposited physical mass.

### SAS5kn — first physical mixed cut

The first unpaid epoch returns one canonical physical-source/move/pair-task cut with deficit equal to current unpaid mixed demand.

### SAS5ko — reset boundary

Changed boundary addresses, incomplete pair or task compatibility, hidden deposits, splitting, source-less creation or missing predecessor lineage returns reset or amplification.

## Finite audit

Run `python scripts/verify_sas_cumulative_integrated_physical_move_bank.py`.

The audit checks 5,200 systems and 8,486 epochs: 18,130 physical-source, 18,294 neutral-move and 20,686 mixed demand classes; 75,012 compatibility arcs; 45,013 named physical deposits; 82,930 demand units; 73,255 paid and 9,675 unpaid units; and 2,464 first deficient epochs.

## Scope

The theorem does not prove physical sign-pair Hall inequalities, core shareability or output lower bounds. It does not prove SAS6 or the no-three-in-line conjecture.
