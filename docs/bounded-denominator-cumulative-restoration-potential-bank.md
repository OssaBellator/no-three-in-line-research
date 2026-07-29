# Bounded-denominator cumulative restoration-potential bank

This note records BDA5ei--BDA5em. It extends the one-epoch restoration/source transport of BDA5ed--BDA5eh to repeated restoration epochs with exact primitive-integer balances.

## Contract

Fix finite primitive-integer source classes `S`, restoration classes `R` and a complete compatibility relation `S -> R`. At epoch `t`, source class `s` has current nonnegative integral potential balance `p_t(s)`. Exact named potential deposits are added before the epoch, and restoration class `r` has exact integral demand `d_t(r)`. Every paid restoration unit debits one compatible source-potential unit. Changing weights, gains, restoration addresses or compatibility is outside the contract.

## Theorem block

### BDA5ei — current primitive-potential balances

Initial balances, named deposits and actual flow debits determine every later source balance exactly. All balances remain nonnegative integers.

### BDA5ej — epoch Hall criterion

The epoch is fully paid exactly when the bipartite source/restoration network has maximum flow `sum_r d_t(r)`. Equivalently, every restoration subset satisfies its capacitated Hall inequality against the current compatible source balances.

### BDA5ek — cumulative restoration identity

Across every fully paid prefix, cumulative restoration potential debited from each source class is at most its initial balance plus its named deposits. Summing over source classes bounds the total paid restoration potential.

### BDA5el — first unpaid restoration cut

At the first epoch whose maximum flow is deficient, a canonical maximizing Hall-deficit subset of restoration classes and its compatible source neighborhood retain the exact unpaid potential. This is the returned arithmetic target.

### BDA5em — reset and amplification boundary

Changed primitive weights, changed gain factors, hidden deposits, source-less creation, splitting, missing predecessor lineage or payment across a noncompatible edge returns reset or amplification rather than restoration payment.

## Finite audit

Run:

`python scripts/verify_bda_cumulative_restoration_potential_bank.py`

The deterministic audit checks 6,000 systems and 10,108 epochs, with 23,922 source classes, 23,916 restoration classes, 45,550 compatibility arcs, 95,788 initial potential units, 64,376 deposited units, 96,124 restoration-demand units, 80,218 paid units, 15,906 unpaid units and 214,812 exact Hall-subset checks.

## Scope

This theorem does not construct the physical primitive weights, damping factors or compatibility graph. It does not prove BDA6 or the no-three-in-line conjecture.