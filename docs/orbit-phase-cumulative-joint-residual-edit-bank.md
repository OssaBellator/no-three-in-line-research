# Orbit-phase cumulative joint residual/edit bank

This note records OP4dk--OP4do. It extends the one-epoch joint residual/edit source comparison through repeated edit epochs.

## Contract

Fix exact source classes `S`, zero-drift residual classes `R`, edit-cost classes `E`, and complete compatibility relations `S -> R` and `S -> E`. Current source balances and named deposits are integral. Residual and edit demands retain all unit-sensitive fields.

## Theorem block

### OP4dk — current shared source balances

Initial balances, named deposits and actual mixed-flow debits determine every later source balance exactly.

### OP4dl — epoch mixed Hall criterion

At each epoch one maximum flow simultaneously pays residual and edit demand. Full payment is equivalent to every mixed residual/edit Hall inequality against current source capacity.

### OP4dm — cumulative no-double-spend identity

Across every fully paid prefix, total residual plus edit debit from each source is at most its initial balance plus named deposits.

### OP4dn — first unpaid mixed cut

The first deficient epoch returns one canonical residual/edit/source cut with deficit equal to current unpaid demand.

### OP4do — reset boundary

Changed unit fields, compatibility, hidden deposits, omitted deletions, source-less creation or split lineage returns reset or amplification.

## Finite audit

Run `python scripts/verify_op_cumulative_joint_residual_edit_bank.py`.

The audit checks 5,200 systems and 6,629 epochs: 18,273 source, 15,541 residual and 15,615 edit classes; 59,806 compatibility arcs; 36,515 named deposits; 98,231 total demand units; 72,526 paid and 25,705 unpaid units; 4,319 first deficient epochs; and 535,659 exact mixed Hall-subset checks.

## Scope

The theorem does not construct the physical residual/edit graph or prove its source deposits. It does not prove OP5 or the no-three-in-line conjecture.
