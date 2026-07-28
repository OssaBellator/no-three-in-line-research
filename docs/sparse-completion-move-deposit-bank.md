# Sparse completion-move deposit bank

This note records SAS5jq--SAS5ju. It extends zero-boundary completion transport across repeated balanced-compression epochs without reusing a boundary-neutral move.

## Contract

Fix finite exact residual-task classes `T`, finite exact boundary-neutral completion-move classes `M`, and a complete compatibility graph. At epoch `e`, task `t` has integral demand `d_e(t)`. Move `m` has a current integral balance, increased only by exact named deposits before the epoch. Every paid task unit debits one compatible move unit and preserves the zero boundary vector.

## Theorem block

### SAS5jq — current completion flow

All residual tasks are completed boundary-neutrally if and only if every task subset `X` satisfies

`sum_{t in X} d_e(t) <= sum_{m in N(X)} b_e(m)`.

### SAS5jr — canonical incomplete cut

Failure returns the least maximum-deficit task subset and its exact move neighborhood. Its deficit equals the maximum number of tasks that cannot be completed in the current epoch.

### SAS5js — cumulative move conservation

Across fully completed epochs, cumulative debit from move class `m` is at most its initial balance plus all exact named deposits into `m`.

### SAS5jt — persistent zero-boundary completion

If every epoch is paid, all selected completion moves preserve the zero boundary vector and cumulative completion is exact. Otherwise the first unpaid epoch returns its current canonical task/move cut.

### SAS5ju — reset boundary

A move that changes the boundary, an omitted task or compatibility arc, relabelled residual state, unrecorded move deposit, capacity reuse or nonadditive completion effect returns reset.

## Proof

SAS5jq and SAS5jr are integral max-flow/min-cut. Exact per-move debits give SAS5js. Boundary neutrality is retained on every compatibility arc, proving SAS5jt.

## Finite audit

Run `python scripts/verify_sas_completion_move_deposit_bank.py`.

The deterministic audit checks 6,000 systems, 8,974 epochs, 36,744 compatibility arcs, 56,981 task-demand units, 18,989 completed units, 13,479 deposit units, 4,616 deficient epochs with 19,310 incomplete units, and 159,576 Hall-subset checks.

## Scope

This theorem does not construct the physical residual-task or boundary-neutral move graph, nor prove its balances and deposits. SAS6 and the no-three-in-line conjecture are not proved.