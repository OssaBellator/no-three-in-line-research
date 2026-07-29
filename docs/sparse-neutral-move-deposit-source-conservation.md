# Sparse neutral-move deposit source conservation

This note records SAS5kf--SAS5kj. It supplies occurrence-faithful physical lineage for the named neutral-move deposits used by the cumulative joint cancellation/completion bank.

## Contract

Fix finite physical neutral-source occurrences and neutral-move classes. Initial source mass, initial move balances and exact exogenous source deposits are nonnegative integers. A legal source transition may move or discard mass but may not increase it. Issuing one neutral-move unit debits one retained physical source unit and credits one exact move class. Pair-execution and completion-task payments debit the shared move balance.

## Theorem block

### SAS5kf — one neutral resource account

Live physical source mass, live neutral-move balance, cumulative pair-execution debit, cumulative completion-task debit and terminally discarded mass belong to one additive account.

### SAS5kg — exact move issuance

Every named neutral-move deposit is a transfer from one retained physical source occurrence into one exact move class. No move capacity appears without predecessor lineage.

### SAS5kh — conservation identity

For every valid history,

`live source + live moves + pair debit + task debit + terminal loss = initial source + initial moves + exogenous source deposits`.

Thus the cumulative shared bank cannot receive more capacity than the physical source account supplies.

### SAS5ki — shared pair/task debit

A move unit used for legal sign-pair execution is unavailable to residual completion, and conversely. The identity therefore composes with SAS5ka--SAS5ke without double spending.

### SAS5kj — first amplification or reset witness

Source-less issuance, splitting one source unit into multiple move units, mass increase, omitted move classes, changed boundary/task addresses or missing predecessor lineage returns the first exact witness.

## Finite audit

Run:

`python scripts/verify_sas_neutral_move_deposit_source_conservation.py`

The deterministic audit checks 6,500 histories and 68,417 steps, with 22,740 source classes, 26,081 neutral-move classes, 79,326 initial source units, 39,236 initial move units, 11,145 exogenous source units, 12,995 move deposits, 13,032 pair debits, 12,888 task debits, 11,446 terminal units, 4,346 valid histories and 2,154 injected source-less, splitting or mass-increase witnesses.

## Scope

This theorem does not prove concrete core shareability, sign-pair Hall inequalities or the physical pair/task/move graph. It does not prove SAS6 or the no-three-in-line conjecture.