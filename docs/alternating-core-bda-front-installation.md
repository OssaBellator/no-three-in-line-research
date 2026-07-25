# Installation audit for one-sided BDA scalar fronts

**Branch:** `research/alternating-core-chain`

AC3du--AC3dx return privately paid endpoint and oriented missing-partner fronts. Their remaining geometry is now audited directly. A front record already contains one actual paid radial triple at scale `h`; its formal adjacent partner is at `H=h+sigma q`, where `sigma` is the missing direction. If `H>0`, the only failures of the clean five-cell BDA5a support are two explicit mixed scalar collisions or absence of one of the two partner cells from the active layer.

## Formal adjacent partner

Fix one paid-faithful ordinary or reflected BDA record with anchor `P`, primitive radial direction `d`, distinct nonzero role scalars `u,v`, denominator `q`, occupied scale `h>0`, and orientation

$$
\sigma\in\{-1,+1\}.
$$

Put

$$
H=h+\sigma q.
$$

The occupied radial triple is

$$
T_h(P)=
\{P,P+hu\,d,P+hv\,d\}.
$$

When `H>0`, define the formal partner cells and triple

$$
U_H=P+Hu\,d,
\qquad
V_H=P+Hv\,d,
$$

$$
T_H(P)=\{P,U_H,V_H\}.
$$

The partner has the same denominator, primitive directions, scalar residue and role word because replacing `h` by `h+sigma q` does not change any scalar congruence modulo `q`.

## AC3ec -- exact five-cell support criterion -- PROVED

Assume `H>0` and that both formal partner cells `U_H,V_H` belong to the current active permutation layer. Then the five cells

$$
P,
\quad P+hu\,d,
\quad P+hv\,d,
\quad U_H,
\quad V_H
$$

have distinct rows and columns exactly when

$$
\boxed{
hu\ne Hv
\quad\text{and}\quad
hv\ne Hu.
}
$$

Under these two inequalities they form the clean support required by BDA5a, and `T_H(P)` is an actual current radial triple. Therefore the BDA rectangle, phase-flip, or blocker-seed decoder menu is executable on the pair `(h,H)`.

### Proof

The occupied triple is genuine, so `u!=v` and its three cells are distinct. Since `H>0` and `u,v` are nonzero, neither formal partner cell equals `P`, and `U_H!=V_H`. The equalities between the same roles at the two scales are impossible because `H-h=sigma q!=0`:

$$
hu=Hu\Longrightarrow q u=0,
\qquad
hv=Hv\Longrightarrow q v=0.
$$

Thus the only possible cross-scale point equalities are `hu=Hv` and `hv=Hu`. Because all five cells lie in one permutation matching, distinct cells automatically have distinct rows and distinct columns. If neither mixed equality holds, the support is exactly the clean five-cell support of BDA5a. QED.

## AC3ed -- four-way adjacent-partner router -- PROVED

Every privately paid endpoint or oriented-front record belongs to exactly one of the following classes.

1. **Lower-bound front:** `H<=0`. This can occur only for the downward orientation. It gives the exact bounded-scale relation
   $$
   \boxed{1\le h\le q.}
   $$
2. **Mixed scalar collision:** `H>0` and
   $$
   hu=Hv
   \quad\text{or}\quad
   hv=Hu.
   $$
   The record returns one of these two exact rational role equations together with its paid slot bucket.
3. **Actual clean partner:** `H>0`, neither mixed collision holds, and both `U_H,V_H` are current active cells. AC3ec makes `(T_h(P),T_H(P))` an executable clean BDA pair. It does not matter whether the partner occurrence was selected in the original paid profile: the original front bucket supplies current payment, while any partner payment is additional.
4. **Missing-support partner:** `H>0`, neither mixed collision holds, and at least one of `U_H,V_H` is absent from the active layer. Record the exact missing subset
   $$
   M_H\subseteq\{U_H,V_H\},
   \qquad
   1\le |M_H|\le2,
   $$
   and for each missing cell whether it is empty or occupied by the blocker layer.

These four classes partition every front family. Hence one class carries at least one quarter of its paid weight.

### Proof

First split by `H<=0` or `H>0`. In the positive case split by the two mixed equalities. If neither occurs, split by whether both formal partner cells belong to the active layer. These conditions are mutually exclusive and exhaustive. AC3ec supplies conclusion 3. QED.

## AC3ee -- privately paid missing-support bank -- PROVED

Let a selected missing-support class have total paid weight `W_miss`. Retain the private occupied-slot buckets from AC3dv and build the complete AC3v conflict graph on the one- or two-cell partner-installation envelopes. Every edge includes row/column, replacement, blocker, protected-bank, potential-factor and paid-set interactions.

For every `K>=1`, either:

1. one installation object has closed-neighbourhood paid load greater than `K` times its own weight, and AC2d returns one finite support/arithmetic label; or
2. a compatible privately paid installation family carries at least
   $$
   \boxed{W_{miss}/K.}
   $$

The selected family has exact additive payment and collateral. Its remaining local alternatives are direct partner installation, blocker repair, strict effective-denominator descent, or one explicit support-faithfulness witness.

### Proof

AC3dv gives disjoint private paid buckets. AC3v gives exact legality and additivity on independent envelopes. Apply AC2c. QED.

## AC3ef -- adjacent-pair no-backtracking ticket -- PROVED

For every positive adjacent scale pair, give the unordered exact support address

$$
\tau=
(P,\{h,H\},q,d,u,v,\text{role decorations})
$$

one capacity-one transition ticket. Any installation or decoder transition which changes the occupied side from `h` to `H` or from `H` to `h` consumes this same ticket.

Therefore the immediate two-step backtrack

$$
h\longrightarrow H\longrightarrow h
$$

cannot occur in the unticketed transition graph. Reappearance of the same adjacent support address is an explicit finite-ticket reopening under AC3b--AC3e.

### Proof

The reverse transition has the same anchor, unordered scale pair, denominator, directions and role decorations, so it uses the same ticket `tau`. Two opposite traversals require two units of capacity, while `tau` has capacity one. QED.

## AC3eg -- quantitative composition -- PROVED

Choose the `theta=1/2` front router of AC3dx. For an AC3am denominator-role class of paid weight `W_x`, one exact endpoint front has weight at least

$$
\frac{W_x}{8R\rho L},
$$

and one exact oriented variation front has weight at least

$$
\frac{W_x}{16R\rho L}.
$$

After AC3ed, one of the four partner classes therefore carries at least

$$
\boxed{
\frac{W_x}{32R\rho L}
}
$$

from an endpoint front, or

$$
\boxed{
\frac{W_x}{64R\rho L}
}
$$

from an oriented variation front. In the missing-support case, AC3ee divides the corresponding bound by at most `K` unless a labelled paid overload occurs.

The factor `rho` is omitted in the fixed-exclusion and repeated-residual-pair cases exactly as in AC3ar and AC3dx.

### Proof

Apply the four-way weighted pigeonhole split in AC3ed to the two AC3dx lower bounds, then apply AC3ee to the missing-support class. QED.

## Consequence

The one-sided BDA scalar fronts no longer stop at a formal missing partner. Every record now becomes:

- a bounded lower-scale profile `h<=q`;
- one of two exact mixed role equations;
- an executable clean BDA pair;
- or a privately paid one- or two-cell support-installation bank or labelled overload.

The immediate adjacent-scale reversal is ticketed. Remaining work is the collateral comparison for the clean-pair and installation banks, and arithmetic termination of the lower-bound, collision, or overload labels.

## Finite check

`scripts/verify_ac_bda_front_installation.py` exhausts small signed role scalars, scales, denominators and partner occupancy words. It checks the exact five-cell collision criterion, the four-way partition, blocker/empty missing-cell labels, the capacity-one backtrack ticket, and the `1/32` and `1/64` composition constants.