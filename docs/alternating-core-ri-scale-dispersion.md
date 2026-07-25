# Finite-ratio routing of coherent RI scale dispersion

**Branch:** `research/alternating-core-chain`

AC3bd may return more than `K` coherent physical base-scale cosets instead of one heavy scale. This note shows that scale dispersion is already a bounded-degree geometric object. After fixing one normalized complete-fibre profile, each scale uses at most four quotient column cosets and four quotient row cosets, so a constant fraction of the scales is row-column-disjoint.

## Quotient support of one coherent scale

Fix a multiplicative subgroup `H` and work in the quotient group

$$
\Gamma=\mathbb F_p^\times/H.
$$

Fix one exact normalized complete fibre with labels

$$
A=cH,
\qquad
B=c^\dagger H,
\qquad
C=gH,
\qquad
R=rH,
$$

satisfying

$$
B=RCA^{-1}.
$$

For one coherent base-scale coset `S`, the two root occurrences use physical column cosets contained in

$$
\boxed{
\mathcal C(S)=\{S,CS,AS,BS\}.
}
$$

Relative to the source row coset `aS^{-1}`, their row cosets are contained in

$$
\boxed{
\mathcal R(S)=
\{1,C^{-1},BC^{-1},AC^{-1}\}\,aS^{-1}.
}
$$

### Verification of the row labels

The source and partner rows are `aS^{-1}` and `aC^{-1}S^{-1}`. The `A`-root anchor lies on `H_b`, so its row coset is

$$
bA^{-1}S^{-1}
=
aRA^{-1}S^{-1}
=
aBC^{-1}S^{-1}.
$$

The `B`-root anchor similarly has row coset

$$
bB^{-1}S^{-1}
=
aRB^{-1}S^{-1}
=
aAC^{-1}S^{-1}.
$$

## AC3dg -- exact scale-conflict alphabet -- PROVED

Let

$$
\mathcal M=\{1,C,A,B\},
$$

$$
\mathcal N=\{1,C^{-1},BC^{-1},AC^{-1}\}.
$$

Two distinct scale cosets `S,T` can share a physical column or row used by their complete-fibre supports only when

$$
\boxed{
TS^{-1}
\in
\mathcal M\mathcal M^{-1}
\cup
\mathcal N\mathcal N^{-1}.
}
$$

The union on the right has at most thirty-one elements, including the identity. Hence there are at most

$$
\boxed{30}
$$

nontrivial scale-conflict ratios.

### Proof

A column collision has `mu S=nu T` for `mu,nu in M`, so `TS^{-1}=nu^{-1}mu`, an element of `MM^{-1}`. A row collision has the identical quotient form with multipliers in `N`; inversion of the common scale causes no change to the quotient-set bound. Each of `MM^{-1}` and `NN^{-1}` has at most sixteen elements, and both contain the identity. Their union therefore has at most `16+16-1=31` elements. QED.

## AC3dh -- row-column-disjoint scale extraction -- PROVED

Build the scale-conflict graph on any family of represented coherent scales, joining two scales when their complete-fibre physical supports share a row or column. Then

$$
\boxed{\Delta\le30.}
$$

Consequently:

1. among `J` represented scales, at least
   $$
   \boxed{\lceil J/31\rceil}
   $$
   have pairwise row-column-disjoint physical supports;
2. if the scales carry nonnegative weights of total `W`, one row-column-disjoint subfamily carries at least
   $$
   \boxed{W/31}.
   $$

### Proof

For a fixed scale `S`, each nontrivial conflict ratio from AC3dg determines at most one scale `T`. Thus the degree is at most thirty. A greedy colouring uses at most thirty-one colours; take the largest colour class, unweighted or weighted. QED.

## AC3di -- coherent scale-dispersion router -- PROVED

Let a coherent complete-fibre family of total paid weight `W` occupy `J` physical scale cosets after fixing the exact normalized fibre and desired finite decorations.

For every scale-load threshold `beta>0`, one of the following holds.

1. **Heavy scale:** one scale carries weight greater than `beta` and enters the closed fixed-edge bank.
2. **Many scales:** at least
   $$
   \boxed{\lceil W/\beta\rceil}
   $$
   scales occur.
3. **Disjoint scale bank:** independently of the threshold, a row-column-disjoint scale subfamily carries weight at least
   $$
   \boxed{W/31}
   $$
   and contains at least `ceil(J/31)` scales.

The selected scales have disjoint source, partner and both anchor row/column cosets. Their full nonadditive conflict graph is then completed by AC3v; bounded conflict gives an executable independent bank, while overload returns one finite arithmetic conflict label through AC2c--AC2d.

### Proof

The heavy-or-many statement is weighted pigeonhole. AC3dh gives the disjoint bank. The final conflict completion is exactly the proved AC3v--AC3x interface and does not assume that row-column disjointness alone controls collateral. QED.

## Completed simultaneous interface

AC3dy--AC3eb in [`alternating-core-ri-multiscale-product.md`](alternating-core-ri-multiscale-product.md) complete the step left open in the first version of this note.

- Exact scale buckets are private current-payment resources and satisfy Hall with equality.
- Applying AC2c to the full repair-envelope graph gives a scope-complete bank of weight at least
  $$
  \boxed{W/(31K)}
  $$
  or one finite paid overload label.
- On an independent scale family, the closed-I6 product expectation is exactly the sum of the local expectations.
- If the product bank does not improve, one of the five aggregate terms `F,C1,C2,C3,B` carries weight at least
  $$
  \boxed{W/(310K)}.
  $$

Thus physical-scale dispersion no longer has a simultaneous-installation or payment gap. Its remaining outputs are the already classified local RI profiles or a finite scoped overload.

## Finite check

`scripts/verify_ac_ri_scale_dispersion.py` enumerates finite cyclic quotient groups, exact label quadruples satisfying `B=RCA^{-1}`, checks both support alphabets and the thirty-ratio bound, constructs the scale-conflict graph, and verifies the `1/31` weighted extraction. `scripts/verify_ac_ri_multiscale_product.py` checks private scale Hall payment, scope-complete extraction, exact product expectation, and the `1/(310K)` failed-bank constant.