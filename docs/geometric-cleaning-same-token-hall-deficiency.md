# Weighted Hall deficiency from a compatible same-token fan

**Branch:** `research/geometric-cleaning`

GC4m--GC4p count the shared token once and pay all additional destroyed factors through bounded reuse. This note closes the remaining accounting branch: if the noncommon pool is too small to pay a constant fraction, the same fan is already a quantitatively Hall-deficient demand system.

## Noncommon pool

Let `I` be an installably compatible same-token fan. Operation `y` has demand weight `lambda_y` and destroys the common token `pi` plus additional current factors `E_y`. Put

\[
W=\sum_{y\in I}\lambda_y,
\qquad
p_y=\sum_{Q\in E_y}\omega_Q,
\qquad
P=\sum_{y\in I}p_y.
\]

Let

\[
U=
\sum_{Q\in\cup_yE_y}\omega_Q
\]

be the actual noncommon union capacity. Assume every noncommon factor belongs to at most `r` sets `E_y`. Then

\[
P\le rU,
\qquad
U\le P.
\]

Fix `kappa>=1` and `0<eta<1`.

## GC4q -- union payment or weighted Hall deficiency -- PROVED

Exactly one of the following quantitative alternatives applies.

1. **Substantial noncommon pool.** If
   \[
   P\ge\frac{\eta W}{\kappa},
   \]
   then the joint installation destroys current factor weight at least
   \[
   \boxed{
   \omega_\pi+\frac{\eta W}{r\kappa}.
   }
   \]

2. **Deficient noncommon pool.** If
   \[
   P<\frac{\eta W}{\kappa},
   \]
   form the weighted bipartite incidence system with:
   - operation demand `lambda_y/kappa`;
   - factor capacity `omega_Q`;
   - edge `yQ` exactly when `Q in E_y`.

   The full operation set has Hall deficiency greater than
   \[
   \boxed{
   \frac{(1-\eta)W}{\kappa}.
   }
   \]

### Proof

In the first branch, bounded reuse gives

\[
U\ge P/r\ge\eta W/(r\kappa).
\]

Add the common token once.

In the second branch, total scaled demand is `W/kappa`. Its complete neighbouring capacity is `U<=P<eta W/kappa`. Demand minus neighbouring capacity is therefore greater than `(1-eta)W/kappa`, which is a valid weighted Hall deficiency for the full operation set. QED.

No operation-by-operation source assignment is needed for this dichotomy.

## GC4r -- half-scale router -- PROVED

With `eta=1/2`, every compatible same-token fan gives either

\[
\boxed{
\omega_\pi+\frac{W}{2r\kappa}
}
\]

of union-safe current payment, or a weighted Hall deficiency greater than

\[
\boxed{
\frac{W}{2\kappa}.
}
\]

### Proof

Substitute `eta=1/2` in GC4q. QED.

## Composition with the weighted fan extraction

Let a GC4l same-token, same-role fibre have total weight `W_0` and conflict degree at most `Gamma`. Then it contains a compatible family of weight

\[
W_I\ge\frac{W_0}{\Gamma+1}.
\]

## GC4s -- labelled-fan payment/deficiency composition -- PROVED

Under the noncommon reuse bound `r`, the GC4l compatible family yields either current payment at least

\[
\boxed{
\omega_\pi+
\frac{W_0}{2r\kappa(\Gamma+1)}
}
\]

or a weighted Hall deficiency greater than

\[
\boxed{
\frac{W_0}{2\kappa(\Gamma+1)}.
}
\]

### Proof

Apply GC4r to the compatible family of weight at least `W_0/(Gamma+1)`. QED.

## GC4t -- corrected same-token overload interface -- PROVED UNDER THE DESTRUCTION-FAITHFUL HALL CONTRACT

In the deficiency branch of GC4q or GC4s, apply the existing minimal weighted Hall-core extraction to the operation--noncommon-factor system.

One obtains a minimal exact deficiency core retaining the displayed deficit, followed by one of the already proved outputs:

1. an atomic capacity overload;
2. a same-resource conflict overload;
3. a compatible same-role deficiency fan;
4. or failure of destruction-faithful eligibility.

Thus the GC4o noncommon-underweight output no longer stops at a ratio statement. It either pays through its aggregate noncommon pool or enters the branch's existing exact Hall-core and created-collateral machinery with a quantified deficit.

## Consequence for GC5

The unresolved geometric work is now narrower:

- pay or neutralize the exact minimal Hall core returned by GC4t;
- route its created collateral or bounded-denominator structure;
- preserve clean height through the selected transition.

The shared-token and aggregate-capacity accounting itself is complete.

## Finite check

`scripts/verify_gc_same_token_hall_deficiency.py` exhausts small weighted operation--factor incidence systems, checks the bounded-reuse union payment and verifies the quantitative weighted Hall-deficiency alternative.
