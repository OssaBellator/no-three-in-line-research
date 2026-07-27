# Union-safe payment for compatible same-token fans

**Branch:** `research/geometric-cleaning`

GC4l extracts a large compatible fan inside one token and one role fibre but correctly refuses to count the shared token once per reopening. This note gives the exact replacement: count the shared token once and charge all other destroyed current factors through their bounded fan reuse.

## Compatible fan factor ledger

Let `I` be an installably compatible fan. Every operation `y in I` destroys the same current token factor `pi` and a set `E_y` of additional current factors. Give every current factor `Q` a nonnegative weight `omega_Q`. Put

\[
p_y=\sum_{Q\in E_y}\omega_Q,
\qquad
P=\sum_{y\in I}p_y.
\]

Assume every noncommon factor belongs to at most `r` of the sets `E_y`, where `r>=1`. Let

\[
G_{\rm union}
=
\sum_{Q\in\{\pi\}\cup\bigcup_yE_y}\omega_Q
\]

be the actual current factor weight destroyed by the joint installation.

## GC4m -- exact shared-token union bound -- PROVED

\[
\boxed{
G_{\rm union}
\ge
\omega_\pi+\frac{P}{r}.
}
\]

The common token is counted exactly once.

### Proof

Write `d_Q=|{y:Q in E_y}|`. Then `d_Q<=r` and

\[
P=\sum_{Q\ne\pi}d_Q\omega_Q
\le r\sum_{Q\in\cup_yE_y}\omega_Q.
\]

Add the one common-token contribution `omega_pi`. QED.

## Weighted fan demands

Let `lambda_y` be the retained current-incidence or latent demand weight of operation `y`, and put `W=sum_y lambda_y`. Fix `kappa>=1`. Call `y` eligible when

\[
\lambda_y\le\kappa p_y.
\]

## GC4n -- eligible fan payment -- PROVED

If eligible operations carry total demand `W_E`, their joint installation destroys noncommon current factor weight at least

\[
\boxed{
\frac{W_E}{r\kappa}.
}
\]

Including the shared token, the union gain is at least

\[
\boxed{
\omega_\pi+\frac{W_E}{r\kappa}.
}
\]

### Proof

Eligibility gives `sum_{y in E}p_y>=W_E/kappa`. Apply GC4m to the eligible subfamily. QED.

## GC4o -- compatible same-token fan router -- PROVED

For every compatible weighted fan and every `kappa>=1`, one of the following holds.

1. **Union-paid fan.** Eligible operations carry at least `W/2`; the joint installation destroys current factor weight at least

   \[
   \boxed{\omega_\pi+\frac{W}{2r\kappa}.}
   \]

2. **Noncommon-underweight fan.** Ineligible operations carry more than `W/2`, and every retained operation satisfies the exact local overload

   \[
   \boxed{\lambda_y/p_y>\kappa,}
   \]

   with `p_y=0` interpreted as an infinite ratio.

### Proof

Eligible and ineligible operations partition the fan weight. If the eligible side has at least half, apply GC4n. Otherwise the ineligible side has more than half and every one of its members violates the eligibility inequality. QED.

## GC4p -- composition with GC4l -- PROVED

Let a GC4l same-token, same-role fibre have total weight `W_0` and conflict maximum degree at most `Gamma`. Its compatible subfamily has weight at least

\[
W_I\ge\frac{W_0}{\Gamma+1}.
\]

Under the noncommon reuse bound `r`, GC4o gives either union-safe current payment at least

\[
\boxed{
\omega_\pi+
\frac{W_0}{2r\kappa(\Gamma+1)}
}
\]

or a noncommon-underweight compatible subfan of weight greater than `W_0/[2(Gamma+1)]`.

### Proof

Apply GC4l and then GC4o to the retained compatible family. QED.

## Corrected geometric frontier

A broad same-token fan no longer fails merely because its common token cannot be reused as payment. It either has a factor-conservative union gain from the additional destroyed factors, or it returns a quantitatively large exact family whose current demand is larger than its entire noncommon destroyed-factor pool by factor `kappa`. The latter is the correct high-load input for the existing capacity-overload and created-collateral routers.

## Finite check

`scripts/verify_gc_same_token_union_payment.py` exhausts small weighted operation--factor incidence systems, verifies the bounded-reuse union inequality and checks the eligible/underweight weighted dichotomy.
