# Cycle-sum payment on a finite normalized phase orbit

**Branch:** `research/orbit-phase-expansion`

OP4ap--OP4ar show that a complete normalized component profile has one cyclic quotient orbit. The remaining return problem is physical: local scores may include a phase-dependent potential that changes from one traversal to the next. This note removes that artificial drift by summing around the exact orbit.

Let the nonzero invariant vector `Omega` have additive order

\[
R=\operatorname{ord}_h(\Omega),
\]

and write the orbit phases as

\[
\phi_j=j\Omega,
\qquad j\in\mathbb Z/R\mathbb Z.
\]

## OP4as -- exact coboundary cancellation -- PROVED

Suppose the physical score of traversal `j` admits a decomposition

\[
G_j=P_j-D_j+\Phi(\phi_j)-\Phi(\phi_{j+1}),
\]

where `P_j>=0` is declared current payment, `D_j>=0` is declared physical debt or obstruction, and `Phi` is any real-valued phase potential on the finite orbit. Then

\[
\boxed{
\sum_{j=0}^{R-1}G_j
=
\sum_{j=0}^{R-1}P_j-
\sum_{j=0}^{R-1}D_j.
}
\]

### Proof

The potential terms telescope cyclically:

\[
\sum_j(\Phi(\phi_j)-\Phi(\phi_{j+1}))=0,
\]

because `phi_R=phi_0`. QED.

## OP4at -- closed-orbit payment/obstruction router -- PROVED

Under OP4as, exactly one of the following holds:

1. `sum_j P_j > sum_j D_j`, in which case `sum_j G_j>0` and at least one traversal has positive physical score;
2. `sum_j D_j > sum_j P_j`, in which case the orbit returns an aggregate physical obstruction of excess weight `sum_j D_j-sum_j P_j`;
3. the totals are equal, in which case `sum_j G_j=0`; either every `G_j=0`, giving an exact balanced orbit, or the orbit contains both a positive and a negative traversal.

### Proof

Use OP4as and compare the two nonnegative totals. A positive sum forces one positive summand. In the equal-total case, a zero-sum finite list is either identically zero or has both signs. QED.

## OP4au -- finite return-ticket criterion -- PROVED UNDER THE SCORE CONTRACT

Assume every debt term `D_j` is assigned to one least physical cause from a finite obstruction dictionary, and every positive traversal consumes current demand or closes an absorber. Then a full reset-free return of the normalized profile has one exact continuation:

1. a positive-score traversal pays or absorbs;
2. one obstruction class carries aggregate debt at least
   \[
   \boxed{
   \frac{\sum_jD_j}{K}
   }
   \]
   when the obstruction dictionary has size `K`;
3. an exact balanced orbit has `G_j=0` for every phase and may receive one capacity-one return ticket;
4. the score decomposition, debt classification or fixed-profile contract fails at one named physical field.

### Proof

Apply OP4at. In the debt-dominant branch, pigeonhole the classified aggregate debt over the `K` obstruction classes. In the equal branch, if some score is positive then branch 1 applies; otherwise all scores are zero. QED.

## OP4av -- corrected OP5 frontier -- PROVED

Finite quotient recurrence and phase-potential drift are now fully removed from the return problem. What remains is physical: define the score decomposition for the actual owner/occurrence/scale/carry transition, pay the positive traversal, concentrate the returned obstruction, or justify the one balanced-orbit ticket. Zero-vector profiles still enter the same physical audit directly without a quotient cycle.

## Finite check

`scripts/verify_phase_cycle_sum_payment.py` exhausts small cyclic score decompositions, verifies coboundary cancellation, and checks the three-way payment/debt/balanced router.