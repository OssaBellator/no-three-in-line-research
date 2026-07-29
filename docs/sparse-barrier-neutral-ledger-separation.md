# Sparse algebraic spread: barrier/neutral ledger separation

## Scope

This note records SAS5im--SAS5iq. It separates the additive output of a compatible sparse fan into terminal barrier ledgers and consumable neutral ledgers. It does not prove the concrete output lower bound or classify which physical ledgers are terminal.

Let `B` be the finite set of retained barrier ledgers and `N` the finite set of retained neutral ledgers. Compatible execution produces a componentwise nonnegative additive output vector. Write `U_B`, `U_N`, and `U=U_B+U_N` for the total barrier, neutral, and complete output mass.

Fix `0<theta<1`.

## SAS5im: aggregate separation

Exactly one of the following weak alternatives holds:

- `U_B >= theta U`;
- `U_N > (1-theta)U`.

No cancellation is possible because all retained output coordinates are nonnegative.

## SAS5in: barrier concentration

In the barrier branch, one exact barrier ledger receives at least

`theta U/|B|`.

This is a terminal barrier certificate whenever the selected ledger is declared nonconsumable by the surrounding theorem.

## SAS5io: neutral concentration

In the neutral branch, one exact neutral ledger receives more than

`(1-theta)U/|N|`.

Thus a large compatible fan cannot disperse all output across the finite neutral dictionary.

## SAS5ip: neutral capacity routing

If neutral ledger `n` has initial-plus-deposited capacity `C_n`, then the complete neutral output is either paid componentwise or returns one least exact overloaded neutral ledger. This composes directly with the earlier fan-output concentration bank.

## SAS5iq: reset boundary

Signed cancellation, an output coordinate omitted from `B union N`, dynamic ledger creation, or nonadditive execution is returned as a ledger-classification reset. It is not counted as barrier progress or neutral payment.

## Remaining frontier

The remaining SAS work is to prove the concrete per-candidate output lower bound, identify terminal barrier versus genuinely consumable neutral ledgers, establish exact core shareability, and connect the resulting certificate to boundary profiles and balanced compression. SAS6 and the no-three-in-line conjecture are not proved.