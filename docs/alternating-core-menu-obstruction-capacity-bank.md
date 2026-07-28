# AC5 menu-obstruction capacity bank

This note isolates the repeated-failure problem left by the restricted-menu audit. It is conditional on exact physical obstruction labels and explicit capacity accounting; it does not assert that those capacities exist in every menu.

## Setup

Fix a finite exact obstruction dictionary `L`. For each class `lambda in L`, retain:

- an initial nonnegative capacity `C_lambda`;
- recorded deposits `D_lambda` made by named physical source operations;
- a positive payment threshold `tau_lambda`;
- an occurrence-faithful ledger balance.

Every failed restricted-menu attempt must return one exact obstruction class `lambda` whose certified load is at least `tau_lambda`. Paying that failure debits at least `tau_lambda` from the corresponding balance. No failure may be relabelled after the fact, and no capacity may appear without a recorded deposit.

## AC5az — exact class partition

Every failed menu attempt belongs to one exact retained obstruction class. Hence the total paid load is the sum of the classwise paid loads; there is no unlabelled remainder.

## AC5ba — classwise payment bound

For every `lambda`,

`tau_lambda N_lambda <= C_lambda + D_lambda`,

where `N_lambda` is the number of paid failures of class `lambda`. Therefore

`N_lambda <= floor((C_lambda + D_lambda)/tau_lambda)`.

## AC5bb — global failure bound

The total number of paid menu failures satisfies

`N_paid <= sum_lambda floor((C_lambda + D_lambda)/tau_lambda)`.

The same statement holds for rational capacities and loads after clearing one common denominator.

## AC5bc — exact overload return

If a failed menu names class `lambda` while its remaining balance is below `tau_lambda`, then the branch returns the exact physical obstruction overload `(lambda, tau_lambda)` rather than discarding the menu or charging an unrelated class.

## AC5bd — paid replenishment alternative

Repeated failure is therefore finite unless one of the following happens:

1. a named source operation deposits new capacity;
2. the obstruction dictionary changes;
3. the exact class label is not retained;
4. the certified threshold is not debited occurrence-faithfully.

Items 2–4 are explicit reset or omitted-field obstructions. Item 1 is an exact source-payment interface for AC4/BDA/GC/SAS rather than free replenishment.

## Router

Combine this bank with the AC5 restricted-menu audit:

- positive slack gives the existing descending installation path;
- nonpositive slack returns one exact heavy class;
- that class is paid from its finite/deposited capacity bank;
- insufficient balance returns one exact overload;
- unrecorded replenishment or relabelling returns reset.

The result does not compute the menu-specific capacities, thresholds, or deposits. Those remain physical arithmetic obligations.

No statement here proves AC5, AC6 or the no-three-in-line conjecture.