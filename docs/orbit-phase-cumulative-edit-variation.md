# Orbit-phase cumulative edit variation

This note records OP4cb--OP4cf. It upgrades the one-step dynamic signature bound to a pathwise variation account.

## Contract

Fix residual demands and source capacities during an edit epoch. At step `t`, the complete residual/source graph may add or delete compatibility arcs. Deleting an arc to source `s` has charge `c_s`; additions have charge zero. Unit-class changes are retained as separate paid edits.

Let `Delta_t` be the maximum residual Hall deficit after step `t`.

## Theorem block OP4cb--OP4cf

1. Adding compatibility arcs cannot increase `Delta_t`.
2. Deleting one arc incident with source `s` increases the maximum deficit by at most `c_s`.
3. Therefore the cumulative positive variation satisfies
   `sum_t (Delta_t-Delta_{t-1})_+ <= sum_t deletion_charge_t`.
4. The number of jumps of size at least `J` is at most the total deletion charge divided by `J`.
5. If an epoch returns to the exact initial signature graph, its final deficit is the initial deficit; all intermediate positive variation is still paid by deleted-capacity charge.
6. Unit changes, new residual/source identities and omitted legality fields are separate edits or resets.

## Consequence

Dynamic action width is harmless when signature edits have a finite exact deletion-capacity account. The remaining OP task is a physical bound on that account and on the separate unit-edit stock.

## Finite audit

Run:

`python scripts/verify_op_cumulative_edit_variation.py`

The audit follows random edit paths and verifies every one-step increase and the cumulative positive variation bound.

## Scope

The result assumes fixed demands/capacities and a complete edit history. It does not control unbounded source creation or prove OP5 or the global conjecture.
