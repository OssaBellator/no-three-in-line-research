# Geometric-cleaning height-source deposit bank

This note records GC2ir--GC2iv. It extends the remedy-height source transport across repeated cleaning epochs with exact source balances and named deposits.

## Contract

Fix finite exact remedy-height demand classes `R`, finite physical height-source classes `S`, and a complete compatibility graph. At each epoch, the already selected cause/remedy flow induces integral height demand `h_t(r)`. Source balances receive only exact named deposits before the epoch. A paid height unit debits one compatible source unit.

## Theorem block

### GC2ir — current height-source payment

All induced height demand is paid exactly if and only if every remedy-class subset `X` satisfies

`sum_{r in X} h_t(r) <= sum_{s in N(X)} b_t(s)`.

### GC2is — canonical source cut

Failure returns the least maximum-deficit remedy subset and its exact height-source neighborhood. Its deficit is the maximum unpaid induced height mass.

### GC2it — cumulative source conservation

Across fully paid epochs, cumulative debit from each height source is at most its initial balance plus all exact named deposits into that source.

### GC2iu — composition with clean-height preservation

When the cause/remedy stage and every induced height-source stage are paid, cumulative additive height loss is fully accounted by physical height-source debits. The first failure remains either the earlier cause/remedy cut or the current height-source cut.

### GC2iv — reset boundary

Changing the selected cause/remedy flow, remedy cost, compatibility graph, source identity, deposit ledger or occurrence lineage without recording the change returns reset.

## Proof

GC2ir and GC2is are integral max-flow/min-cut. Summing exact source debits proves GC2it. Apply the two stages in order to obtain GC2iu.

## Finite audit

Run `python scripts/verify_gc_height_source_deposit_bank.py`.

The deterministic audit checks 5,500 systems, 8,122 epochs, 33,685 compatibility arcs, 52,108 induced height-demand units, 17,075 paid units, 12,327 deposit units, 4,200 deficient epochs with 17,771 unpaid units, and 148,762 Hall-subset checks.

## Scope

The theorem assumes the selected remedy flow and induced height demand are occurrence-faithful. It does not construct the physical graphs, costs, balances or deposits. GC5 and the no-three-in-line conjecture are not proved.