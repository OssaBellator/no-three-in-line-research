# Sparse cumulative joint cancellation/completion bank

This note records SAS5ka--SAS5ke. It extends the joint sign-pair/completion transport through repeated zero-boundary epochs with one shared neutral-move balance vector.

## Contract

Let `P` be exact sign-pair execution-cost classes, `T` exact residual completion-task classes, and `M` exact boundary-neutral move classes. Pair and task demands share one complete compatibility graph into `M`. Move class `m` has a current nonnegative integer balance. Exact named deposits are applied before each epoch; successful flow debits actual shared source use once.

## Theorem block

### SAS5ka — current shared balance

The epoch state retains the exact current neutral-move balance vector and all named deposits. Pair-cost and task classes are not given separate copies of the same capacity.

### SAS5kb — joint epoch transport

Combine pair-cost and completion-task demands into one capacitated bipartite flow to neutral moves. Full execution/completion is equivalent to flow value equal to total combined demand.

### SAS5kc — cumulative debit law

For every successful epoch, debit each neutral-move class by its actual sink flow. Cumulative pair execution plus task completion through that class is at most initial balance plus named deposits.

### SAS5kd — first mixed cut

The first unpaid epoch returns the residual minimum mixed pair/task/move cut. Its deficit is the exact unexecuted or incomplete mass at current balances.

### SAS5ke — reset boundary

Changed pair legality, residual-task identity, omitted compatibility, nonneutral moves, nonadditive capacity, hidden deposits or capacity reuse return reset rather than completion.

## Proof

Integral max-flow gives one shared allocation in each epoch. Flow conservation identifies exact move use. Induction over successful epochs proves the cumulative balance law; max-flow/min-cut gives the first mixed obstruction.

## Finite audit

Run `python scripts/verify_sas_cumulative_joint_cancellation_completion_bank.py`.

## Scope

This does not construct the physical pair/task/move graph or prove its capacities and deposits. It does not prove SAS6 or the no-three-in-line conjecture.