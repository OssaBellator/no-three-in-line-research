# Weight-quantile capacities for protected-height events

**Branch:** `research/geometric-cleaning`

GC4ad--GC4ag bound one protected-event address by incidence times a maximum operation weight.  That estimate can be wasteful when only a few operations are heavy.  This note replaces it by the exact largest-weight capacity permitted by the incidence bound.

Let `I` be the retained compatible same-token fan.  Every unsafe operation `y` has weight `lambda_y>0` and one least protected-event address `p(y)`.  For an address `p`, let `Y_p` be the set of operations that are physically eligible to carry address `p`, after aliases and occurrence identities are fixed.  Write the weights in `Y_p` in nonincreasing order

\[
\lambda_{p,[1]}\ge\lambda_{p,[2]}\ge\cdots.
\]

For an integer `d>=0`, put

\[
S_p(d)=\sum_{i=1}^{\min\{d,|Y_p|\}}\lambda_{p,[i]}.
\]

## GC4ah -- exact top-weight incidence capacity -- PROVED

If the occurrence-faithful incidence of address `p` satisfies

\[
|I_p|\le d_p,
\]

then its demand obeys

\[
\boxed{
H_p\le U_p:=S_p(d_p).
}
\]

This is the largest possible address demand consistent with the eligible operation weights and the incidence cap.

### Proof

`H_p` is the sum of the weights of the subset `I_p subseteq Y_p`.  Among all subsets of `Y_p` of size at most `d_p`, the maximum weight is obtained by the `d_p` largest eligible weights, whose sum is `S_p(d_p)`. QED.

## GC4ai -- exact aggregate quantile capacity -- PROVED

Under incidence caps `d_p` for every address,

\[
\boxed{
U=\sum_pU_p
\le
\sum_pS_p(d_p).
}
\]

If only a global operation-weight order

\[
\lambda_{[1]}\ge\lambda_{[2]}\ge\cdots
\]

is available, then

\[
\boxed{
U\le\sum_p\sum_{i=1}^{d_p}\lambda_{[i]}.
}
\]

For a uniform incidence cap `d` and dictionary size `K_H`,

\[
\boxed{
U\le K_H\sum_{i=1}^{d}\lambda_{[i]}.
}
\]

### Proof

Sum GC4ah.  The global top-`d_p` weights dominate the top eligible weights for each address.  The uniform formula is immediate. QED.

## GC4aj -- quantile-safe clean-height router -- PROVED

Suppose

\[
\sum_pS_p(d_p)\le\eta W,
\qquad 0\le\eta<1.
\]

Then the retained fan yields one of:

1. clean-height-preserving current payment at least
   \[
   \boxed{
   \omega_\pi+\frac{(1-\eta)W}{2r\kappa};
   }
   \]
2. a clean-height-safe Hall deficiency greater than
   \[
   \boxed{
   \frac{(1-\eta)W}{2\kappa};
   }
   \]
3. one exact address whose physical incidence exceeds `d_p`;
4. one eligibility, alias, occurrence, lineage, context or weight-record field fails.

### Proof

When all incidence and record fields hold, GC4ah gives valid occurrence-faithful capacities with total at most `eta W`.  Apply GC4ab.  A failed incidence cap or record field is returned by its least address. QED.

## GC4ak -- corrected protected-height frontier -- PROVED

A finite protected-event dictionary no longer needs a uniform maximum-weight estimate.  It is enough to prove address incidence caps and control the top eligible operation weights.  Failure returns one concrete high-incidence address or one exact eligibility/record defect.  The remaining geometric task is therefore to bound `d_p` and the eligible top-weight sums for the actual line, certificate and height addresses.

## Finite check

`scripts/verify_gc_protected_event_weight_quantiles.py` exhausts small eligible operation sets, weights and incidence caps, checks that the top-`d` sum is the exact extremal capacity, and verifies the aggregate and relative-capacity inequalities.
