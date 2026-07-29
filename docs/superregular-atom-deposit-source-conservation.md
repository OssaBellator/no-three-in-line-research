# Superregular atom-capacity deposit source conservation

This note records SRR2cp--SRR2ct. It supplies occurrence-faithful physical lineage for the named atom-capacity deposits used by the cumulative conditioned atom bank.

## Contract

Fix finite physical source occurrences and a complete witness-atom dictionary. Initial physical source mass, initial atom-capacity balances and exact exogenous source deposits are nonnegative integers. Physical transitions may move or discard source mass but may not increase it. Issuing one atom-capacity unit debits one retained physical source unit and credits one exact witness atom. Paid conflict burden debits the atom balance.

## Theorem block

### SRR2cp — joint source/atom account

Live physical source mass, live atom-capacity balance, cumulative paid atom burden and terminally discarded source mass form one additive account.

### SRR2cq — occurrence-faithful atom issuance

Every named atom deposit transfers one physical source unit into one exact witness-atom class. The source occurrence, atom address and threshold epoch remain retained.

### SRR2cr — conservation identity

For every valid history,

`live source + live atom capacity + paid burden + terminal loss = initial source + initial atom capacity + exogenous source deposits`.

Thus cumulative atom deposits cannot exceed the declared physical stock.

### SRR2cs — composition with the executable bound

Whenever the current atom balances pay the actual conditioned burden, SRR2ck--SRR2co retains the same-threshold executable-weight guarantee. The source account certifies only the capacity supply; it does not alter the conflict-thinning inequality.

### SRR2ct — first amplification or reset witness

Source-less atom deposits, splitting, mass increase, omitted witness atoms, changed threshold addresses or missing predecessor lineage return the first exact witness rather than extra capacity.

## Finite audit

Run:

`python scripts/verify_srr_atom_deposit_source_conservation.py`

The deterministic audit checks 6,500 histories and 68,331 steps, with 22,646 physical source classes, 25,838 witness atoms, 79,336 initial source units, 38,478 initial atom units, 13,126 exogenous source units, 15,262 atom deposits, 32,802 paid burden units, 13,214 terminal units, 4,414 valid histories and 2,086 injected source-less, splitting or mass-increase witnesses.

## Scope

This theorem does not construct the geometric witness-atom dictionary or prove the concrete burden, conditioning and deposit estimates. It does not prove SRR2, SRR4 or the no-three-in-line conjecture.