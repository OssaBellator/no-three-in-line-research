# Rational-inverse cumulative owner-charge deposit bank

This note records RI5df--RI5dj. It extends the one-epoch owner-charge transportation theorem to a sequence of exact collateral deposits and debits.

## Contract

Let owners have integral perturbation-charge demands and let a finite set of exact collateral sources have current integral balances. At each epoch:

- exact nonnegative deposits are added to named source balances;
- the complete owner/source compatibility graph is retained;
- a paid charge unit consumes one source unit;
- owner, host, context and coherence fields remain fixed for the transport.

## RI5df — current-balance Hall criterion

At each epoch all owner charge is paid exactly if and only if every owner subset has demand at most the current balance of its reachable sources.

## RI5dg — exact balance debit

For a fully paid epoch, choose the canonical integral maximum flow and debit each source by its exact used amount. No source becomes negative.

## RI5dh — cumulative deposit bound

For every source and every prefix of the epoch sequence,

`cumulative debit <= initial balance + cumulative named deposits`.

Summing over sources bounds total paid compatibility-deletion charge.

## RI5di — first unpaid epoch

If an epoch cannot be paid, the least maximizing owner subset is retained as the canonical unpaid owner/source cut with deficiency equal to the untransported charge. Earlier paid epochs remain valid debits.

## RI5dj — reset boundary

Unrecorded collateral creation, source relabelling, omitted compatibility arcs, changing owner/coherence data or one source unit paying several charge units without debit returns reset or amplification.

## Finite audit

Run:

`python scripts/verify_ri_owner_charge_deposit_bank.py`

The deterministic audit checks 5,000 systems, 9,343 epochs, 51,185 compatibility arcs, 25,016 deposit units and 99,470 Hall-subset tests.

## Scope

The theorem does not prove the concrete arithmetic owner/source graph or create collateral. It supplies the cumulative accounting interface needed once physical source deposits and capacities are established. RI6 and the no-three-in-line conjecture remain open.
