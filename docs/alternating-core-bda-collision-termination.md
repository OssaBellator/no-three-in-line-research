# Finite termination of lower and mixed-collision BDA fronts

**Branch:** `research/alternating-core-chain`

AC3ec--AC3eg reduce every one-sided BDA scalar front to a bounded lower-scale profile, one of two mixed scalar collisions, an executable clean pair, or a missing-support installation profile. This note proves that the first two outputs are finite arithmetic states. A mixed collision determines the adjacent scale pair exactly from the reduced role scalars and the denominator, while the lower-scale output has `1<=h<=q`.

## Setup

Fix nonzero distinct integer role scalars `u,v`, a denominator `q>=1`, an occupied scale `h>=1`, an orientation

$$
\sigma\in\{-1,+1\},
$$

and

$$
H=h+\sigma q.
$$

For a positive partner scale `H>0`, the two mixed collisions are

$$
\mathrm{I}:\quad hu=Hv,
$$

and

$$
\mathrm{II}:\quad hv=Hu.
$$

Put

$$
d=\gcd(|u|,|v|),
\qquad
u=u/d,
\qquad
\omega=v/d.
$$

Then `nu,omega` are coprime signed integers.

## AC3eh -- exact mixed-collision normal form -- PROVED

Assume `H>0` and one mixed collision holds.

1. The reduced role scalars have the same sign:
   $$
   \nu\omega>0.
   $$
2. Put
   $$
   a=|\nu|,
   \qquad
   b=|\omega|,
   \qquad
   \delta=|a-b|.
   $$
   Then `a,b` are positive coprime integers, `delta>=1`, and
   $$
   \boxed{\delta\mid q.}
   $$
3. The unordered adjacent scale pair is uniquely determined:
   $$
   \boxed{
   \{h,H\}
   =
   \left\{
   \frac{aq}{\delta},
   \frac{bq}{\delta}
   \right\}.
   }
   $$
4. Collision I occurs exactly with
   $$
   h=\frac{bq}{\delta},
   \qquad
   H=\frac{aq}{\delta},
   \qquad
   \sigma=\operatorname{sgn}(a-b),
   $$
   after replacing `a,b` by the absolute reduced coefficients in the same signed order as `u,v`.
5. Collision II is the same formula with `a,b` interchanged. The two collision equations cannot hold simultaneously.

### Proof

For collision I, cancellation of `d` gives

$$
h\nu=H\omega.
$$

Because `h,H>0`, the quotient `\omega/\nu=h/H` is positive, so `nu,omega` have the same sign. After taking absolute values,

$$
ha=Hb.
$$

Coprimality of `a,b` gives a positive integer `t` with

$$
h=bt,
\qquad
H=at.
$$

Since `H-h=sigma q`,

$$
(a-b)t=\sigma q.
$$

Thus `sigma=sgn(a-b)`, `delta t=q`, and the displayed divisibility and scale formulas follow. Collision II is identical after swapping `u,v`.

If both equations held, then division would give `u/v=v/u`, hence `u^2=v^2`. Since `u!=v`, this forces `u=-v`, contradicting the already proved same-sign condition. QED.

## AC3ei -- bounded finite scale alphabet -- PROVED

Fix `q` and one exact ordered role word `(u,v)`.

1. A lower-bound front has
   $$
   \boxed{1\le h\le q.}
   $$
   Hence it has at most `q` possible occupied scales.
2. Across both orientations and both mixed equations, there is at most one unordered positive collision pair. It exists only when the reduced absolute difference `delta` divides `q`.
3. If `|u|,|v|<=B`, every scale in a mixed collision satisfies
   $$
   \boxed{
   1\le h,H\le Bq.
   }
   $$
4. Therefore, after fixing the denominator and bounded role word, the combined lower/collision output has a finite scale alphabet independent of the prime grid size.

### Proof

The lower-bound statement is AC3ed. AC3eh gives uniqueness of the unordered collision pair. Since `a,b<=B` and `delta>=1`, the explicit formulas give `h,H<=Bq`. QED.

## AC3ej -- collision return is the already ticketed reverse edge -- PROVED

Let a mixed collision occur at the unordered support address

$$
\tau=(P,\{h,H\},q,d,u,v,\text{role decorations}).
$$

Reversing the adjacent-scale direction exchanges `h` and `H` and exchanges collision I with collision II, but leaves `tau` unchanged. Hence the capacity-one AC3ef ticket already forbids the only immediate collision return.

Moreover, AC3eh shows that no second distinct mixed-collision pair exists for the same exact `(q,u,v)` role word. Thus repeated collision output in one exact role profile is necessarily reuse of the same finite support ticket or a change in some retained arithmetic decoration.

### Proof

The explicit unordered pair in AC3eh is symmetric in `a,b`. Reversing the direction changes only the ordering of the two scales and the named mixed equation. The exact support address uses the unordered pair, so both traversals consume the same AC3ef ticket. Uniqueness excludes another pair. QED.

## AC3ek -- quantitative localization of bounded fronts -- PROVED

Let a selected lower-bound front have paid weight `W_low`. Since `h` lies in `{1,...,q}`, one exact scale class has paid weight at least

$$
\boxed{W_{low}/q.}
$$

A mixed-collision class needs no further scale pigeonhole after `(q,u,v)` and the collision type are fixed, because AC3eh already determines `h,H` exactly.

Combining with AC3eg, an endpoint front originating from paid weight `W_x` returns either a collision profile at weight at least

$$
\boxed{
\frac{W_x}{32R\rho L}
}
$$

or one exact lower scale at weight at least

$$
\boxed{
\frac{W_x}{32qR\rho L}.
}
$$

For an oriented variation front the corresponding bounds are

$$
\boxed{
\frac{W_x}{64R\rho L}
}
$$

and

$$
\boxed{
\frac{W_x}{64qR\rho L}.
}
$$

The factor `rho` is omitted in the same AC3ar exceptional cases as before.

### Proof

The first assertion is weighted pigeonhole on the `q` possible lower scales. The collision assertion is AC3eh. Substitute the AC3eg four-way class bounds. QED.

## Consequence

The lower-scale and mixed-collision outputs are no longer recurrent scalar frontiers.

- Lower fronts are finite exact scale states with `h<=q`.
- Mixed collisions are divisibility states `delta|q` with one explicitly determined adjacent pair.
- Their only raw reversal is the already ticketed AC3ef edge.
- No prime-dependent scale tower remains in either output.

The remaining BDA front work is the actual potential comparison for clean decoder pairs and privately paid missing-support installation banks, together with finite processing of their scoped overload labels.

## Finite check

`scripts/verify_ac_bda_collision_termination.py` exhausts signed role scalars, denominators, scales and both orientations. It verifies the coprime normal form, divisibility condition, uniqueness, mutual exclusion of the two collision equations, bounded-scale alphabet, reverse-ticket identity and quantitative localization constants.