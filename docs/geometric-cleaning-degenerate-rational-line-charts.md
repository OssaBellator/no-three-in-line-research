# Rational line-following structure of coefficient-degenerate charts

**Branch:** `research/geometric-cleaning`

GC4at--GC4ax give root-count capacities for nonzero polynomial collinearity determinants. The remaining coefficient-degenerate branch has

\[
\det(X_2-X_1,X_3-X_1)\equiv0.
\]

This note resolves that branch over the rational function field.

Put

\[
A(t)=X_2(t)-X_1(t),
\qquad
B(t)=X_3(t)-X_1(t),
\]

with vector degrees `p=deg A` and `q=deg B`.

## GC4ay -- rational dependence of an identically collinear chart -- PROVED

Assume

\[
\det(A(t),B(t))\equiv0.
\]

Then exactly one of the following holds:

1. `A=0` as a vector polynomial, so `X_1=X_2` identically;
2. `A!=0`, and there is a rational function
   \[
   \lambda(t)\in F(t)
   \]
   such that
   \[
   \boxed{B(t)=\lambda(t)A(t)}
   \]
   in `F(t)^2`.

If coordinate `s` has `A_s!=0`, one may take

\[
\boxed{
\lambda(t)=\frac{B_s(t)}{A_s(t)}.
}
\]

### Proof

If `A=0`, branch 1 holds. Otherwise choose a nonzero coordinate `A_s`. The determinant identity says `A_s B_{3-s}-A_{3-s}B_s=0`. Dividing in the field `F(t)` by `A_s` gives `B_{3-s}=(B_s/A_s)A_{3-s}`, while the chosen coordinate satisfies the same identity trivially. QED.

## GC4az -- bounded rational chart degrees -- PROVED

For the choice above, write `lambda=f/g` with

\[
f=B_s,
\qquad
g=A_s.
\]

Then

\[
\boxed{
\deg f\le q,
\qquad
\deg g\le p.
}
\]

After cancellation by `gcd(f,g)`, these degree bounds can only improve.

### Proof

Coordinate degrees are bounded by their vector degrees. Cancelling a common factor does not increase either degree. QED.

## GC4ba -- denominator-exception capacity -- PROVED

Suppose at most `M` physical operations share one parameter value. On the chart `lambda=f/g`, the denominator-exception set

\[
Z_g=\{t:g(t)=0\}
\]

contains at most `p` parameter values and therefore at most

\[
\boxed{pM}
\]

physical operations, unless `g` is the zero polynomial, which is excluded by the coordinate choice.

Outside `Z_g`, all three moving cells satisfy

\[
\boxed{
X_3(t)=X_1(t)+\lambda(t)(X_2(t)-X_1(t)).
}
\]

### Proof

A nonzero polynomial of degree at most `p` has at most `p` roots. Multiply by the physical parameter multiplicity. The rational dependence from GC4ay is defined whenever `g(t)!=0`. QED.

## GC4bb -- complete degenerate-chart router -- PROVED

Every coefficient-degenerate polynomial collinearity chart has one exact continuation:

1. one pair of moving cells is identically coincident;
2. a bounded-degree rational line-following chart `lambda=f/g` holds away from at most `pM` denominator-exception operations;
3. the exceptional operations are charged by their top `pM` eligible weights;
4. one coordinate chart, field, parameter, multiplicity, alias, lineage or occurrence record fails;
5. or the rational line-following family is returned as a persistent geometric concentration requiring direct owner/line payment.

Thus an identically-zero determinant is not an unstructured failure. It is either an exact pair-collision profile or a bounded-degree rational dependence plus a root-bounded exceptional set.

## Corrected GC5 frontier

Nondegenerate polynomial charts have root-count capacities, while degenerate charts have rational line-following structure. Remaining work is to pay persistent rational line families, control denominator-exception weights, and construct the actual finite chart dictionaries for cleaning operations.

## Finite check

`scripts/verify_gc_degenerate_rational_line_charts.py` exhausts small polynomial vector pairs, checks that determinant-zero pairs are either identically coincident or rationally dependent by cross multiplication, and verifies denominator root bounds.