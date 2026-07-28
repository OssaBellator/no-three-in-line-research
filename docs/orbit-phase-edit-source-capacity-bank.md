# Orbit-phase edit-source capacity bank

This note records OP4cg--OP4ck. It composes cumulative signature-edit variation with finite exact edit-source capacities.

## Contract

Every source-deletion edit has a retained nonnegative capacity charge and one exact edit-source class from a finite dictionary. Each class has initial capacity and recorded deposits. Source additions have zero adverse charge. Unit-field edits remain separate labelled events and are not silently absorbed into source deletion.

## Theorem block

### OP4cg — classwise edit charge

For each edit-source class `lambda`, let `Q_lambda` be the cumulative capacity of all source deletions assigned to that class. The total deletion charge is `sum_lambda Q_lambda`.

### OP4ch — variation domination

Cumulative positive residual-deficit variation is at most `sum_lambda Q_lambda`.

### OP4ci — capacity payment

If `Q_lambda <= C_lambda + D_lambda` for every class, all positive deficit variation in the epoch is paid by the edit-source bank.

### OP4cj — overload witness

If payment fails, the least class satisfying `Q_lambda > C_lambda + D_lambda` is an exact edit-source overload. The associated deletion occurrences and retained source capacities are part of the witness.

### OP4ck — reset boundary

Changing source capacities, relabelling deletion classes, folding unit changes into source deletion, omitting additions/deletions, or introducing unrecorded deposits returns reset.

## Proof

OP4cb--OP4cf bounds each positive deficit jump by the capacity deleted at that step. Summing and partitioning by exact edit-source class gives OP4cg and OP4ch. The remaining statements are the classwise bank alternative.

## Remaining physical work

The theorem leaves the physical construction of edit-source classes, their capacities and deposits, and the independent payment of unit-field edits open.