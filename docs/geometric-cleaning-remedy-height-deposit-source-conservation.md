# Geometric-cleaning remedy/height deposit source conservation

This note records GC2jg--GC2jk. It supplies a physical lineage contract for the named remedy-capacity and height-source deposits used by the cumulative integrated cleaning network.

## Contract

Fix finite physical source occurrences, remedy-capacity classes and height-source classes. Initial physical source mass, initial remedy and height balances and exact exogenous source deposits are nonnegative integers. A physical transition is occurrence-faithful and may move or discard source mass but may not increase it. Issuing one remedy-capacity or height-source unit debits one unit from one retained physical predecessor occurrence. Paid cleaning flow debits the corresponding named balance.

## Theorem block

### GC2jg — one joint mass account

At every time, live physical source mass, live remedy balance, live height-source balance, cumulative paid remedy/height use and terminally discarded source mass belong to one additive account.

### GC2jh — exact issuance transfer

A named remedy or height deposit is not new mass: it transfers one physical source unit into one exact capacity class while preserving the retained occurrence and class addresses.

### GC2ji — conservation identity

For every valid history,

`live source + live remedy + live height + paid use + terminal loss = initial source + initial balances + exogenous source deposits`.

The equality gives the cumulative deposit bound required by GC2jb--GC2jf.

### GC2jj — first amplification witness

Source-less issuance, splitting one source unit into multiple deposits, mass-increasing transition, missing predecessor lineage or an omitted capacity class returns the first exact physical witness.

### GC2jk — reset boundary

Changed source, remedy, height, role, occurrence or compatibility fields are outer resets and are not charged to the conserved account.

## Finite audit

Run:

`python scripts/verify_gc_remedy_height_deposit_source_conservation.py`

The deterministic audit checks 6,500 histories, 61,973 steps, 22,688 physical source classes, 22,808 remedy classes, 22,654 height classes, 11,429 remedy deposits, 10,489 height deposits, 8,410 paid capacity units, 9,575 terminal units, 4,281 valid histories and 2,219 injected source-less, splitting or mass-increase witnesses.

## Scope

This theorem does not construct the concrete physical source dictionary or prove the integrated cause/remedy/height compatibility graph. It does not prove GC5 or the no-three-in-line conjecture.