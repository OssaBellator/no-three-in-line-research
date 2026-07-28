# Geometric-cleaning cumulative integrated remedy-height bank

This note records GC2jb--GC2jf. It extends the integrated cause/remedy/height network through repeated cleaning epochs with exact named deposits and debits.

## Contract

Fix complete cause, remedy and height-source addresses and both compatibility layers during each epoch. Remedy class `r` has current capacity `u_r`; height-source class `h` has current capacity `v_h`. Between epochs, exact named deposits may increase these balances. Each epoch has integral cause demands. Every paid unit traverses one complete `cause -> remedy -> height source` path.

## Theorem block

### GC2jb — current balance state

The state retains the exact current remedy and height-source balance vectors. Deposits are applied to their named classes before the epoch flow.

### GC2jc — integrated epoch payment

Use the split-remedy max-flow network from GC2iw--GC2ja with the current balance vectors. Full payment is equivalent to flow value equal to total cause demand.

### GC2jd — exact cumulative debit

For a successful epoch, debit each remedy by the flow through its split edge and each height source by its sink flow. Every paid unit is charged once at both constrained layers, so cumulative debit never exceeds initial capacity plus named deposits.

### GC2je — first mixed cut

The first epoch without full flow returns its residual minimum mixed cause/remedy/height cut. Its deficit is the exact unpaid cause mass at the current balances.

### GC2jf — reset boundary

Changing physical classes during an epoch, omitted compatibility, nonadditive capacity, hidden deposits, capacity reuse or untagged feedback return reset rather than payment.

## Proof

Apply integral max-flow independently at each current state. Flow conservation identifies exact remedy and height-source use. Induction over epochs preserves nonnegative balances and the cumulative initial-plus-deposit bounds. Max-flow/min-cut gives the first failure certificate.

## Finite audit

Run `python scripts/verify_gc_cumulative_integrated_remedy_height_bank.py`.

## Scope

This does not construct the physical network or prove its capacities and deposits. It does not prove GC5 or the no-three-in-line conjecture.