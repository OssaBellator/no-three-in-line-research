# SAS compatible-fan output-ledger concentration

The heavy-core router returns a compatible residual-independent fan. This note transfers that fan to a finite family of exact barrier and neutral output ledgers.

## Setup

Let `F` be a simultaneously executable compatible fan. Candidate `Q` has weight `w_Q` and a nonnegative output vector

`g(Q)=(g_1(Q),...,g_L(Q))`

in a retained finite dictionary of exact barrier/neutral ledgers. Assume every candidate has total certified output

`sum_j g_j(Q) >= gamma w_Q`

for one retained `gamma>0`. Ledger `j` has initial-plus-deposited capacity `C_j` when the output is a consumable neutral resource; barrier ledgers may instead be terminal outputs.

## SAS5ih — aggregate output identity

Because the fan is compatible and execution is additive under the shared-core contract, total output is the coordinatewise sum

`G_j=sum_Q g_j(Q)`.

No cross-candidate cancellation is allowed unless it is represented in the retained output vector.

## SAS5ii — finite-ledger concentration

Some ledger satisfies

`G_j >= (gamma/L) sum_Q w_Q`.

Thus every large compatible fan yields one quantitatively large exact barrier or neutral output class.

## SAS5ij — capacity-paid alternative

If every consumable ledger satisfies `G_j<=C_j`, the entire fan output is paid by the finite ledger bank. If not, the branch returns one least overloaded exact ledger. Terminal barrier ledgers are returned directly rather than charged.

## SAS5ik — weighted and rational form

The same inequalities hold for rational candidate weights, outputs and capacities after clearing one common denominator. Candidate multiplicity may be folded into `w_Q` without changing the conclusion.

## SAS5il — combined fan router

The iterated heavy-core route now ends in:

- an exact nonshareable core obstruction;
- a capacity-paid common-core execution;
- a compatible fan producing one large exact barrier/neutral ledger;
- one overloaded output ledger;
- or a reset caused by omitted output, nonadditive execution or a changing ledger dictionary.

The note does not prove the menu-specific lower bound `gamma`, identify which outputs are terminal barriers, or establish the final balanced-compression inequality.

No statement here proves SAS6 or the no-three-in-line conjecture.