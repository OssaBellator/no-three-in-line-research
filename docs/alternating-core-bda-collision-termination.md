# Finite termination of lower and mixed-collision BDA fronts

**Branch:** `research/alternating-core-chain`

AC3ec--AC3eg reduce every one-sided BDA scalar front to a bounded lower-scale profile, one of two mixed scalar collisions, an executable clean pair, or a missing-support installation profile. This note proves that the first two outputs are finite arithmetic states. A mixed collision determines the adjacent scale pair exactly from the reduced role scalars and the denominator, while the lower-scale output has `1<=h<=q`.

## Setup

Fix nonzero distinct integer role scalars `u,v`, a denominator `q>=1`, an occupied scale `h>=1`, and an orientation

$$
\sigma\in\{-1,+1\}.
$$

Put

$$
H=h+\sigma q.
$$

For `H>0`, the two mixed collisions are

$$
\mathrm{I}:\quad hu=Hv,
$$

and

$$
\mathrm{II}:\quad hv=Hu.
$$

Define

$$
d=\gcd(|u|,|v|),
\qquad
u_0=u/d,
\qquad
v_0=v/d.
$$

Then `u_0,v_0` are coprime signed integers.

## AC3eh -- exact mixed-collision normal form -- PROVED

Assume `H>0` and one mixed collision holds. Then:

1. the reduced role scalars have the same sign,
   $$
   u_0v_0>0;
   $$
2. with
   $$
   a=|u_0|,
   \qquad
   b=|v_0|,
   \qquad
   \delta=|a-b|,
   $$
   the integers `a,b` are positive and coprime, `delta>=1`, and
   $$
   \boxed{\delta\mid q;}
   $$
3. the unordered adjacent scale pair is uniquely determined by
   $$
   \boxed{
   \{h,H\}
   =
   \left\{
   \frac{aq}{\delta},
   \frac{bq}{\delta}
   \right\};
   }
   $$
4. collision I occurs exactly with
   $$
   h=\frac{bq}{\delta},
   \qquad
   H=\frac{aq}{\delta},
   \qquad
   \sigma=\operatorname{sgn}(a-b),
   $$
   where `a,b` retain the order induced by `u_0,v_0`;
5. collision II is the same formula with `a,b` interchanged, and the two equations cannot hold simultaneously.

### Proof

For collision I, cancellation of `d` gives

$$
hu_0=Hv_0.
$$

Since `h,H>0`, the ratio `v_0/u_0=h/H` is positive, so `u_0,v_0` have the same sign. Taking absolute values gives

$$
ha=Hb.
$$

Coprimality yields a positive integer `t` such that

$$
h=bt,
\qquad
H=at.
$$

Using `H-h=sigma q`,

$$
(a-b)t=\sigma q.
$$

Thus `sigma=sgn(a-b)`, `delta t=q`, and the divisibility and scale formulas follow. Collision II is obtained by swapping `u,v`.

If both equations held, then `u/v=v/u`, hence `u^2=v^2`. Since `u!=v`, this forces `u=-v`, contradicting the same-sign conclusion. QED.

## AC3ei -- bounded finite scale alphabet -- PROVED

Fix `q` and one exact ordered role word `(u,v)`.

1. A lower-bound front has
   $$
   \boxed{1\le h\le q,}
   $$
   and therefore at most `q` occupied scales.
2. Across both orientations and both mixed equations there is at most one unordered positive collision pair. It exists only when `delta` divides `q`.
3. If `|u|,|v|<=B`, every collision scale satisfies
   $$
   \boxed{1\le h,H\le Bq.}
   $$
4. Hence the combined lower/collision output has a finite scale alphabet independent of the prime grid size.

### Proof

The lower bound is AC3ed. AC3eh gives uniqueness. Since `a,b<=B` and `delta>=1`, its explicit formulas give `h,H<=Bq`. QED.

## AC3ej -- collision return is the existing reverse-edge ticket -- PROVED

Let a mixed collision occur at the unordered support address

$$
\tau=(P,\{h,H\},q,d,u,v,\text{role decorations}).
$$

Reversing the adjacent-scale direction exchanges `h,H` and exchanges collision I with collision II, but leaves `tau` unchanged. The capacity-one AC3ef ticket therefore forbids the only immediate collision return.

AC3eh also shows that there is no second distinct collision pair for the same exact `(q,u,v)` role word. Repeated collision output is consequently reuse of the same finite support ticket or a change in a retained arithmetic decoration.

### Proof

The unordered formula in AC3eh is symmetric in `a,b`. Direction reversal changes only the ordering and the named equation. Both traversals use the same AC3ef ticket, and uniqueness excludes another pair. QED.

## AC3ek -- quantitative localization of bounded fronts -- PROVED

A lower front of paid weight `W_low` has one exact scale class of weight at least

$$
\boxed{W_{low}/q.}
$$

A mixed-collision class needs no scale pigeonhole once `(q,u,v)` and the equation type are fixed.

Combining with AC3eg, an endpoint front from paid weight `W_x` returns a collision profile of weight at least

$$
\boxed{\frac{W_x}{32R\rho L}}
$$

or one exact lower scale of weight at least

$$
\boxed{\frac{W_x}{32qR\rho L}}.
$$

For an oriented variation front the corresponding bounds are

$$
\boxed{\frac{W_x}{64R\rho L}}
$$

and

$$
\boxed{\frac{W_x}{64qR\rho L}}.
$$

The factor `rho` is omitted in the same AC3ar exceptional cases as before.

### Proof

Apply weighted pigeonhole to the `q` lower scales, use AC3eh for collision uniqueness, and substitute the AC3eg class bounds. QED.

## Consequence

The lower-scale and mixed-collision outputs are no longer recurrent scalar frontiers.

- Lower fronts are finite exact scale states with `h<=q`.
- Mixed collisions are divisibility states `delta|q` with one determined adjacent pair.
- Their only raw reversal is the ticketed AC3ef edge.
- No prime-dependent scale tower remains.

AC3el--AC3eo separately close support faithfulness and heterogeneous product execution for the clean-pair output. The remaining one-sided-front work is potential termination of the returned decoder collateral profiles and the privately paid missing-support installation banks.

## Finite check

`scripts/verify_ac_bda_collision_termination.py` exhausts signed role scalars, denominators, scales and both orientations. It verifies coprime normal form, divisibility, uniqueness, mutual exclusion, bounded scales, reverse-ticket identity and the quantitative localization constants.