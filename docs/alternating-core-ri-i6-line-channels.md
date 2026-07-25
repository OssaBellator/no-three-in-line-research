# Exact line-channel normal form for closed-bank I6 collateral

**Branch:** `research/alternating-core-chain`

AC3bs and AC3bw reduce heavy active collateral to one exact affine line and one fixed tuple of I6 channels. This note removes the remaining geometric multiplicity by writing every line-channel intersection as a linear or quadratic equation and recording the resulting finite root word.

## Setup

Fix a nonzero I6 channel parameter

$$
\lambda=\lambda_\chi
$$

and its modular conic

$$
H_\lambda=\{(x,\lambda/x):x\in\mathbb F_p^\times\}.
$$

Let the reduction of one exact real affine line be

$$
AX+BY=C,
\qquad (A,B)\ne(0,0)
$$

over the odd prime field.

## AC3by -- exact line-channel equation -- PROVED

Exactly one of the following forms applies.

1. **Vertical line.** If `B=0`, then
   $$
   x=c=C/A,
   $$
   and the channel contributes at most the unique cell
   $$
   (c,\lambda/c),
   $$
   provided `c!=0`.
2. **Horizontal line.** If `B!=0` and `A=0`, put `b=C/B`. The channel equation is
   $$
   bx=\lambda.
   $$
   Since `lambda!=0`, it has exactly one solution when `b!=0` and no solution when `b=0`.
3. **Genuinely sloped line.** If `AB!=0`, put
   $$
   s=-A/B,
   \qquad
   b=C/B.
   $$
   Then a channel point on the line has column coordinate satisfying
   $$
   \boxed{
   sX^2+bX-\lambda=0.
   }
   $$
   Its discriminant is
   $$
   \boxed{
   \Delta_\lambda=b^2+4s\lambda.
   }
   $$
   Therefore the channel contributes zero, one, or two cells according as `Delta_lambda` is a nonsquare, zero, or a nonzero square. For a chosen square root `delta_lambda`, the roots are
   $$
   \boxed{
   x_\pm=\frac{-b\pm\delta_\lambda}{2s}.
   }
   $$

### Proof

The vertical and horizontal cases are immediate substitutions into `xy=lambda`. In the remaining case, solve the line equation as `y=sx+b` and multiply by `x`. The quadratic formula gives the discriminant and roots. QED.

## AC3bz -- exact root-word alphabet on one heavy line -- PROVED

Fix one exact affine line and an ordered tuple of `r` I6 channels, where `r<=3`.

- On a vertical or horizontal line, every channel has at most one cell. Hence any compatible moving tuple is unique once the channel tuple is fixed.
- On a genuinely sloped line, every channel cell is indexed by one of at most two quadratic-root branches. Thus a tuple using one cell from each of `r` channels has at most
  $$
  \boxed{2^r}
  $$
  branch words.
- If one channel contributes two distinct cells, those cells must be both roots of its quadratic. Their unordered pair is forced, with
  $$
  \boxed{
  x_1+x_2=-b/s,
  \qquad
  x_1x_2=-\lambda/s.
  }
  $$
  Consequently a `(2,1)` source-rank-two class has at most two branch words, one for each possible root in the singleton channel.

This recovers and sharpens the line multiplicities used in AC3bv:

- `(1,1;N)`: one word on vertical/horizontal lines and at most four on sloped lines;
- `(2,1)` or `(1,2)`: impossible on vertical/horizontal lines and at most two on sloped lines;
- `(1,1,1)`: one word on vertical/horizontal lines and at most eight on sloped lines.

### Proof

Apply AC3by's solution count independently to each channel. A repeated channel requires two distinct intersections, so the quadratic must have both roots and the pair is fixed by Vieta's formula. QED.

## AC3ca -- mixed-channel difference identity -- PROVED

On one genuinely sloped line `y=sx+b`, let

$$
Z_i=(x_i,\lambda_i/x_i)
$$

be points from channels `lambda_i`. Then

$$
\boxed{
\lambda_1-\lambda_2
=
(x_1-x_2)\bigl(s(x_1+x_2)+b\bigr).
}
$$

If `x_1!=x_2`, this gives the exact quotient law

$$
\boxed{
\frac{\lambda_1-\lambda_2}{x_1-x_2}
=s(x_1+x_2)+b.
}
$$

For a repeated-channel pair `lambda_1=lambda_2`, distinct columns force

$$
\boxed{
s(x_1+x_2)+b=0,
}
$$

which is the same sum relation supplied by Vieta.

### Proof

Each point satisfies `lambda_i=sx_i^2+bx_i`. Subtract the two identities and factor the difference of squares. QED.

## AC3cb -- heavy-line finite arithmetic router -- PROVED

Let one exact line/channel/multiplicity class have raw weight `S`.

1. If the line is vertical or horizontal, its moving-cell tuple is unique. The output is one heavy exact physical tuple, with any remaining fixed-cell incidence retained.
2. If the line is genuinely sloped, split by the finite quadratic-root word. One word carries at least:
   - `S/4` in the `(1,1;N)` case;
   - `S/2` in the `(2,1)` or `(1,2)` case;
   - `S/8` in the `(1,1,1)` case.
3. Every selected word retains the exact line coefficients `(s,b)`, channel parameters, discriminants, chosen roots, and all pairwise mixed-channel difference identities.

Thus a heavy line is no longer an unresolved geometric family. It is a heavy exact cell tuple or one of at most eight explicit quadratic branch words. The remaining task is payment/termination of that exact tuple or arithmetic word through the AC resource, carry, BDA, or geometric-cleaning routers.

### Proof

AC3bz bounds the number of branch words. Weighted pigeonhole gives the displayed shares. AC3ca supplies the retained identities. QED.

## Finite check

`scripts/verify_ac_ri_i6_line_channels.py` exhausts every modular affine line and every nonzero channel parameter for `p=5,7,11,13`. It verifies the vertical/horizontal cases, the quadratic and discriminant root sets, Vieta identities, mixed-channel difference laws, and the branch-word bounds for all source-rank-two and source-rank-three multiplicity types.