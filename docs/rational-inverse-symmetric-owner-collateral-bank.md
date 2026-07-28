# RI symmetric owner-collateral bank

The two-lift antisymmetric ledger cancels on every complete physical transposition. This note isolates the remaining symmetric payment and gives it an exact finite owner ledger.

## Setup

Fix the complete terminal geometry, its one- or two-lift physical fibre, and the retained finite owner/coherence address. For each exact owner class `o`, retain:

- initial collateral `C_o >= 0`;
- recorded deposits `D_o >= 0` made by named source operations;
- occurrence-faithful symmetric debits.

A complete transposition orbit has zero antisymmetric debt. Its remaining nonnegative payment demand is an exact symmetric cost assigned to one retained owner class. Costs may be rational after clearing one common denominator.

## RI5cb — transposition reduction

Every complete two-lift orbit reduces to its symmetric cost. The choice of orientation cannot move cost between owner classes or create an antisymmetric remainder.

## RI5cc — classwise collateral inequality

For every owner class,

`P_o <= C_o + D_o`,

where `P_o` is cumulative paid symmetric cost. Hence every fixed minimum payment `s_o>0` can occur at most

`floor((C_o+D_o)/s_o)`

times.

## RI5cd — exact overload return

If the selected symmetric owner cost exceeds the remaining class balance, the branch returns the exact owner-collateral overload `(o,s)` rather than changing orientation, owner or coherence labels.

## RI5ce — deposit alternative

Further symmetric payment requires a named collateral deposit. An unrecorded owner source, owner change, coherence change, host change or context change is an explicit reset or omitted-field obstruction.

## RI5cf — terminal fibre router

Combining the quadratic/secant fibre bounds, owner/coherence quotient, antisymmetric cancellation and this bank gives:

- at most two physical lifts per complete geometry address;
- no long hidden orientation cycle;
- zero antisymmetric payment on complete transposition cycles;
- finite symmetric payment from exact owner collateral;
- otherwise one owner overload, deposit source or retained-field reset.

The note does not prove the arithmetic collateral lower bound or construct the physical owner deposits required by RI6.

No statement here proves RI6 or the no-three-in-line conjecture.