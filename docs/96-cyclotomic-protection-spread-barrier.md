# Cyclotomic protection versus rank-three spread

PX173 protects every fixed finite direction family, while PX175 proves that a
direct rectangle argument needs polynomially many protected directions.  A
natural algebraic shortcut is to use a cyclotomic permutation which is
orthogonal to many linear maps.  This chapter records a sharp obstruction to
that shortcut.

The obstruction has two levels.

1. Every cyclotomic class is an affine packet in the graph, and one packet
   already forces repeated affine-triangle shapes.
2. Near-linear orthomorphisms can be orthogonal to many linear maps, but they
   retain an affine graph on all but one packet and therefore have essentially
   the worst possible rank-three spread.

Let \(p\) be an odd prime and let \(d\mid p-1\).  Write

\[
m=\frac{p-1}{d}.
\]

A cyclotomic map of index \(d\) has the form

\[
f(0)=0,
\qquad
f(x)=a_i x
\quad(x\in C_{d,i}),
\]

where every multiplicative class \(C_{d,i}\) has size \(m\).

## 1. One affine packet already forces triangle concentration

Recall the affine-triangle multiplicity from PX129:

\[
\tau_f(r,t,s)
=
\#\left\{
(u,v):u\ne v,
\frac{f(v)-f(u)}{v-u}=r,
\frac{f(u+t(v-u))-f(u)}{f(v)-f(u)}=s
\right\}.
\]

## Theorem PX176 -- PROVED

Suppose \(f\) is a permutation which is cyclotomic of index \(d\), and
\(m\ge3\).  Then

\[
\boxed{
\tau(f)
\ge
\left\lceil\frac{(m)_3}{p-2}\right\rceil.
}
\]

If \(f\) is strong complete and its affine similarity orbit is used as in PX129,
then its normalized rank-three cylinder constant satisfies

\[
\boxed{
K_3\ge\frac{(m)_3}{p}.
}
\]

### Proof

Fix one cyclotomy class \(C_{d,i}\).  Every graph point over that class lies on
one affine line:

\[
(x,f(x))=(x,a_i x).
\]

Take an ordered triple of distinct rows \(u,v,w\in C_{d,i}\).  There is a unique

\[
t=\frac{w-u}{v-u}\in\mathbb F_p\setminus\{0,1\}.
\]

The corresponding graph triple has

\[
r=a_i,
\qquad
s=
\frac{a_iw-a_iu}{a_iv-a_iu}
=t.
\]

There are exactly \((m)_3\) ordered triples in the class.  They are distributed
among only \(p-2\) possible values of \(t\), so one bin
\(	au_f(a_i,t,t)\) has the displayed size.

PX129 gives

\[
K_3=\frac{p-2}{p}\tau(f),
\]

which proves the orbit bound. \(\square\)

## Corollary PX177 -- PROVED

Let \(f_p\) be a strong-complete cyclotomic seed of index \(d_p\), with packet
size \(m_p=(p-1)/d_p\).  If its affine-orbit rank-three constant satisfies

\[
K_3\le p^\gamma,
\]

then

\[
(m_p)_3\le p^{1+\gamma}.
\]

In particular, for \(m_p\ge4\),

\[
\boxed{
m_p\le2p^{(1+\gamma)/3}}
\]

and hence

\[
\boxed{
d_p\ge\frac{p-1}{2p^{(1+\gamma)/3}}
=\Omega\!\left(p^{(2-\gamma)/3}\right).}
\]

Thus subpower rank-three spread requires

\[
\boxed{d_p\ge p^{2/3-o(1)}.}
\]

### Proof

The first assertion is PX176.  For \(m\ge4\),

\[
(m)_3=m(m-1)(m-2)\ge\frac{m^3}{4},
\]

so \(m^3\le4p^{1+\gamma}\), and the convenient factor \(2\) gives the stated
bound. \(\square\)

This rules out every bounded-index or moderately growing-index cyclotomic seed
for the PX173 spread problem.  Any viable cyclotomic construction must operate
in the high-index, small-packet regime, such as the sign-pair quotient of
PX148--PX151.

## 2. Near-linear protection has maximal affine freezing

A near-linear map of index \(d\) has multipliers

\[
f=[a,b,b,\ldots,b],
\qquad a\ne b.
\]

It differs from the affine map

\[
F(x)=bx
\]

only on the single class \(C_{d,0}\), hence on exactly \(m\) rows.  It agrees
with \(F\) on

\[
q=p-m
\]

rows, including zero.

Fear and Wanless prove that a near-linear index-\(d\) orthomorphism is
orthogonal to exactly

\[
\frac{p-3d-1}{d}=m-3
\]

linear orthomorphisms.  Their Theorem 10 states this for \(d>2\); the same
formula \((p-7)/2=m-3\) is classical for \(d=2\).  Orthogonality to the linear
map \(x\mapsto cx\) means precisely that

\[
x\longmapsto f(x)-cx
\]

is a permutation, equivalently that the graph of \(f\) omits secant slope \(c\).
Thus near-linear maps genuinely can protect many linear directions.

## Theorem PX178 -- PROVED, USING THE FEAR--WANLESS COUNT

Let \(f\) be a strong-complete near-linear cyclotomic map of index \(d\ge2\).
Then:

1. \(f\) omits exactly \(m-3\) nontrivial linear slopes counted by the
   Fear--Wanless orthogonality theorem;
2. its affine-orbit triangle constant satisfies

   \[
   \boxed{
   K_3\ge\frac{(p-m)_3}{p};
   }
   \]
3. since \(m\le(p-1)/2\),

   \[
   \boxed{
   K_3
   \ge
   \frac{((p+1)/2)_3}{p}
   =\Omega(p^2).
   }
   \]

Consequently no near-linear cyclotomic family can provide the subpower
rank-three spread required after PX175, regardless of how its index varies.

### Proof

Only the second assertion needs proof.  On the \(q=p-m\) rows where \(f=F\),
every ordered triple of distinct rows gives an affine graph triple.  The
\((q)_3\) ordered triples are distributed among the \(p-2\) row ratios, so

\[
\tau(f)\ge
\left\lceil\frac{(q)_3}{p-2}\right\rceil.
\]

Applying PX129 gives

\[
K_3=\frac{p-2}{p}\tau(f)\ge\frac{(q)_3}{p}.
\]

A nonlinear near-linear orthomorphism has \(d\ge2\), hence
\(m=(p-1)/d\le(p-1)/2\) and \(q\ge(p+1)/2\). \(\square\)

## 3. Consequence for the polynomial-direction frontier

The cyclotomic literature does not remove PX175 by itself.

- Low or moderate index gives packets too large for subpower triangle spread by
  PX176--PX177.
- Near-linear maps can omit an explicit family of \(m-3\) slopes, but PX178
  proves that their affine complement freezes rank three at order \(p^2\).
- A viable algebraic construction must therefore be both **high index** and
  **globally nonlinear across almost every packet**.

This sharply identifies the remaining cyclotomic target: construct a
strong-complete map with index at least \(p^{2/3-o(1)}\), orthogonal to a
polynomially large prescribed family of linear maps, and with no large affine
subfamily.  The fixed-index existence theorems do not address this regime; the
Fear--Wanless paper explicitly leaves orthogonality at relatively large least
index as a future direction.

## External input

David Fear and Ian M. Wanless, *Existence results for cyclotomic
orthomorphisms*, Journal of Algebraic Combinatorics 46 (2017), 1--14,
Theorem 10.  The arXiv version is 2101.00859.

## Verification

Run

```bash
python scripts/verify_product_cyclotomic_protection_spread_barrier.py
```

The verifier checks exact two-packet examples, the affine-packet triangle lower
bound, the high-index consequence, and the Fear--Wanless count identity on
representative prime fields.
