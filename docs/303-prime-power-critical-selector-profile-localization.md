# Critical paid-pair selectors localize to one exact profile class

CMR1558--CMR1565 show that a paid-pair selector with candidate-only expectation
`A_L<1` is a bounded splice into repeated return.  The complementary regime
must not remain a diffuse candidate row.  The candidate term already has the
exact residual-rank and line-profile partition of CMR1334--CMR1341, so any
near-critical selector concentrates quantitatively in one finite class.

This chapter gives a gap-parameter normal form.  For every `eta in (0,1]`, a
selector either has a uniform restoration cap, or one exact rank/profile band
carries at least `(1-eta)/(3B_n^3)` of the candidate expectation.  Exact rook
probability bounds then convert that expectation into a candidate-count lower
bound.  Thus only finitely many concentrated critical rows remain.

Fix a CMR531 paid-pair selector on a residual board of side `n>=2`.  Its
candidate-only expectation is

\[
A_L=\sum_{C\in\mathcal C_L}\Pr(C\subseteq R),
\]

where `mathcal C_L` is the corrected family of genuinely new candidate
prescriptions and `R` is the selector response law.  Every prescription has
residual rank `r in {1,2,3}` and one exact line-count profile `(o,g,m)`.

Put

\[
B_n=2+\lfloor\log_2n\rfloor.
\]

Use the dyadic class

\[
\chi(C)=
\bigl(r,b_n(o),b_n(g),b_n(m)\bigr).
\]

There are at most

\[
\boxed{N_n=3B_n^3}
\]

such classes.

## 1. Exact class decomposition

For a class `chi`, define

\[
A_\chi
=
\sum_{\substack{C\in\mathcal C_L\\\chi(C)=\chi}}
\Pr(C\subseteq R).
\]

### Theorem CMR1598 -- PROVED

\[
\boxed{
A_L=\sum_\chi A_\chi,
\qquad
A_\chi\ge0,
}
\]

and at most `N_n=3B_n^3` summands are nonzero.

### Proof

The exact residual-rank/profile classes partition the corrected candidate
family.  All prescription probabilities are nonnegative.  CMR1338 gives the
class-count bound. ∎

The same statement remains true after refining `chi` by owner layer, primitive
height, prefix, carry, root/fixed-interface or exchange-cycle labels; only the
number of classes changes by the corresponding finite factor.

## 2. Gap-parameter selector dichotomy

Fix a rational number

\[
0<\eta\le1.
\]

### Theorem CMR1599 -- PROVED

Every paid-pair selector satisfies at least one of the following.

1. **Subunit return splice.**
   \[
   \boxed{A_L\le1-\eta.}
   \]
   For every unavailable-edge cap `B_0>=|B_L|`, CMR1564 gives the restoration
   bound
   \[
   \boxed{
   T_L
   \le
   \left\lfloor
   \frac{2+B_0/(n-1)}{\eta}
   \right\rfloor.
   }
   \]
2. **Concentrated candidate class.**  One exact class `chi` satisfies
   \[
   \boxed{
   A_\chi>
   \frac{1-\eta}{3B_n^3}.
   }
   \]

If `A_L>=1`, the stronger bound

\[
\boxed{A_\chi\ge\frac1{3B_n^3}}
\]

holds for some class.

### Proof

If branch one fails, then `A_L>1-eta`.  Sum at most `3B_n^3` nonnegative class
contributions and pigeonhole.  The critical specialization uses `A_L>=1`. ∎

Thus a selector cannot be both outside every bounded return-splice class and
diffuse over all rank/profile bands.

## 3. Candidate-count localization from a prescription cap

Fix one class `chi` of residual rank `r`.  Let

\[
P_\chi
=
\max_{C:\chi(C)=\chi}
\Pr(C\subseteq R).
\]

and let `N_chi` be the number of corrected candidate prescriptions in the class.

### Theorem CMR1600 -- PROVED

Whenever `P_chi>0`,

\[
\boxed{
N_\chi
\ge
\left\lceil\frac{A_\chi}{P_\chi}\right\rceil.
}
\]

Consequently, in the concentrated branch of CMR1599,

\[
\boxed{
N_\chi
\ge
\left\lceil
\frac{1-\eta}{3B_n^3P_\chi}
\right\rceil.
}
\]

For a critical selector `A_L>=1`, replace `1-eta` by one.

### Proof

The class contribution is a sum of `N_chi` nonnegative terms, each at most
`P_chi`.  Hence `A_chi<=N_chi P_chi`; rearrange and use integrality. ∎

The exact component-rook probability may be used for `P_chi`.  A host-uniform
line-clean coefficient `kappa` gives the coarser bound

\[
P_\chi\le\frac{\kappa}{(n)_r}.
\]

## 4. Uniform rank/profile candidate lower bound

Let `kappa_chi` be the strong, singleton or endpoint-overlap coefficient
applicable to the selector response row.  Put

\[
\widehat P_\chi
=
\min\left\{1,\frac{\kappa_\chi}{(n)_r}\right\}.
\]

### Theorem CMR1601 -- PROVED

In the concentrated branch, some rank/profile class satisfies

\[
\boxed{
N_\chi
\ge
\left\lceil
\frac{(1-\eta)(n)_r}
{3B_n^3\kappa_\chi}
\right\rceil
}
\]

whenever `kappa_chi/(n)_r<=1`; in general use

\[
\boxed{
N_\chi
\ge
\left\lceil
\frac{1-\eta}{3B_n^3\widehat P_\chi}
\right\rceil.
}
\]

For `A_L>=1`, replace `1-eta` by one.

### Proof

Apply CMR1600 with the uniform prescription bound. ∎

This lower bound is deliberately class-local.  It does not add candidates from
different historical selector episodes.

## 5. Exact rational and integer localization

Suppose all prescription probabilities in one exact selector host have common
denominator `D>0`.  Write

\[
A_\chi=\frac{a_\chi}{D},
\qquad
a_\chi\in\mathbb Z_{\ge0}.
\]

### Theorem CMR1602 -- PROVED

The critical condition `A_L>=1` is the integer inequality

\[
\boxed{
\sum_\chi a_\chi\ge D.
}
\]

It forces one class with

\[
\boxed{
a_\chi\ge\left\lceil\frac{D}{3B_n^3}\right\rceil.}
\]

More generally, failure of `A_L<=1-eta` for rational `eta=s/t` in lowest terms
forces one class satisfying

\[
\boxed{
 t a_\chi>
 \frac{(t-s)D}{3B_n^3}
}
\]

and hence the corresponding strict integer ceiling.

### Proof

Clear the common denominator and pigeonhole the resulting nonnegative integers.
For the gap form, multiply `A_L>1-s/t` by `tD`. ∎

This is compatible with exact rook denominators and the integer certificate
format of CMR1270--CMR1277.

## 6. Refined geometric class concentration

Let every rank/profile class be further partitioned into at most `J` exact
geometric subclasses, for example by

- canonical entering owner and layer;
- primitive-height band;
- absolute token or prefix class;
- quotient/carry label;
- root residue and partner type;
- fixed-interface or thin-factor type.

### Theorem CMR1603 -- PROVED

If branch one of CMR1599 fails, one refined class carries more than

\[
\boxed{
\frac{1-\eta}{3JB_n^3}
}
\]

of the selector candidate expectation.  In the critical case `A_L>=1`, one
refined class carries at least

\[
\boxed{
\frac1{3JB_n^3}.
}
\]

### Proof

There are at most `3JB_n^3` nonnegative refined contributions. ∎

The factor `J` must be the actual finite class count.  No hidden infinite
geometric partition is permitted.

## 7. Selector normal form for the recurrent quotient

### Theorem CMR1604 -- PROVED

For every rational gap `eta in (0,1]`, the paid-pair selector part of the
same-owner quotient may be refined into only two types.

1. **Return-splice classes:** `A_L<=1-eta`, with zero candidate self-row and the
   explicit CMR1599 restoration cap.
2. **Concentrated critical classes:** one exact rank/profile/geometric class
   carries the quantitative mass of CMR1599 or CMR1603 and is retained as the
   candidate row.

There is no additional diffuse selector diagonal class.

### Proof

Apply CMR1599 to every exact selector state and retain the witnessing class in
branch two.  The classes partition the state family, while CMR1561 gives the
zero selector self-row in branch one. ∎

The return-splice classes couple to the return assignment through the single
CMR1586 dual.  The concentrated classes must be compared with destroyed credit
using line-clean integer budgets, owner/height envelopes, or structural descent.

## 8. Critical-selector endpoint

### Corollary CMR1605 -- PROVED

The selector frontier is now finite and quantitative.

1. Below a chosen gap from one, every selector is a bounded return splice.
2. Outside that regime, one exact rank/profile class carries explicit positive
   expectation.
3. Exact or uniform rook probabilities convert the expectation into a candidate-
   count lower bound.
4. Rational denominators give an exact integer localization certificate.
5. Further owner, height, prefix, carry, root and thin labels preserve finite
   concentration with only their explicit class-count factor.

The remaining critical-selector task is no longer to control an undifferentiated
`A_L>=1` row.  It is to certify finitely many concentrated geometric classes
against destroyed target load or place them on strict transfer arcs.  No all-`n`
theorem is claimed.

Gap dichotomies, dyadic class concentration, probability-to-count conversion,
integer localization and refined class bounds are checked in
[`scripts/verify_prime_power_critical_selector_localization.py`](../scripts/verify_prime_power_critical_selector_localization.py).
