# Same-channel cross carries and scalar wrap centers

This chapter complements two preceding carry-classification results:

- [`23-aligned-anchor-carry-cells.md`](23-aligned-anchor-carry-cells.md) gives the fine determinant factorisation for aligned anchors;
- [`24-secant-star-carry-dispersion.md`](24-secant-star-carry-dispersion.md) gives the canonical product-carry dispersion theorem for endpoint-disjoint secant stars and the combined paid-bank transition.

Here we retain three nonoverlapping refinements:

1. an exact cross-carry invariant for a same-channel secant involution;
2. a coordinate-free scalar-wrap classification with explicit rational centers;
3. an integer-factorisation bound inside every perfect-wrap chamber.

Throughout, nonzero residues use representatives in \(\{1,\ldots,p-1\}\).

## 1. Exact cross carry on one secant involution

Fix distinct channels \(H_a,H_b\), put \(r=b/a\), and take

\[
B_z=(z,w)=\left(z,\left\langle\frac bz\right\rangle_p\right)\in H_b.
\]

For \(x\in\mathbb F_p^*\), let

\[
u=T_z(x)=\frac{z(x-z)}{rx-z}
\]

be its partner under the projective secant involution on \(H_a\). Consider a fully affine nonfixed orbit and write

\[
P_x=(x,y_x),\qquad P_u=(u,y_u),
\qquad y_t=\left\langle\frac at\right\rangle_p.
\]

### Theorem CF1 — PROVED

For every oriented affine secant parameter \(x\),

\[
\boxed{(x-z)(y_u-w)\equiv b-a\pmod p.}
\]

Therefore

\[
\kappa_z(x)
=
\frac{(x-z)(y_u-w)-(b-a)}p
\]

is an integer, and

\[
\boxed{
B_z,P_x,P_u\text{ are real-collinear}
\iff
\kappa_z(x)=\kappa_z(u).
}
\]

### Proof

The projective secant relation gives

\[
(x-z)(y_u-w)
\equiv
(u-z)(y_x-w)
\pmod p.
\]

Using \(y_u\equiv a/u\), \(w\equiv b/z\), and

\[
r xu=z(x+u-z)
\]

shows that each cross product is congruent to \(b-a\). Their difference is the real determinant of \(B_z,P_x,P_u\), so it vanishes exactly when the two integer carries agree. \(\square\)

## 2. Divisor bound at one cross-carry level

For an integer level \(t\), put

\[
N_t=b-a+pt.
\]

Every represented level satisfies

\[
0<|N_t|\le(p-2)^2.
\]

Let \(s_t(z;a,b)\) count the real secant pairs through \(B_z\), with both endpoints on \(H_a\), having common cross carry \(t\).

### Theorem CF2 — PROVED

\[
\boxed{s_t(z;a,b)\le\tau(|N_t|),}
\]

where \(\tau\) is the positive-divisor function.

Consequently, a same-channel real secant star containing \(M\) pairs occupies at least

\[
\boxed{\frac{M}{\Delta_p^{\mathrm{cross}}}}
\]

distinct cross-carry levels, where

\[
\Delta_p^{\mathrm{cross}}
=
\max_{1\le n\le(p-2)^2}\tau(n)
=
p^{o(1)}.
\]

### Proof

At level \(t\), every oriented parameter satisfies

\[
(x-z)(y_u-w)=N_t.
\]

The nonzero integer \(x-z\) is a signed divisor of \(N_t\) and determines \(x\). Thus there are at most \(2\tau(|N_t|)\) oriented parameters. Every real secant pair contributes two orientations. \(\square\)

This is finer than product-carry dispersion for a same-channel star because it uses the anchor-specific secant involution.

## 3. Universal scalar-wrap determinant

Let

\[
U=(x,y)\in[1,p-1]^2
\]

and take distinct \(\alpha,\beta\in\{2,\ldots,p-1\}\). Define coordinatewise lifted multiples

\[
P_\alpha(U)=\langle\alpha U\rangle_p,
\qquad
P_\beta(U)=\langle\beta U\rangle_p,
\]

and carry vectors

\[
K_\alpha(U)=
\left(
\left\lfloor\frac{\alpha x}{p}\right\rfloor,
\left\lfloor\frac{\alpha y}{p}\right\rfloor
\right),
\]

with \(K_\beta(U)\) defined analogously.

### Theorem CF3 — PROVED

Writing \(A=K_\alpha(U)\) and \(B=K_\beta(U)\), the three points

\[
U,P_\alpha(U),P_\beta(U)
\]

are real-collinear exactly when

\[
\boxed{
p\det(A,B)
=(\alpha-1)\det(U,B)-(\beta-1)\det(U,A).}
\]

### Proof

Use

\[
P_\alpha(U)-U=(\alpha-1)U-pA,
\qquad
P_\beta(U)-U=(\beta-1)U-pB
\]

and expand the determinant. \(\square\)

## 4. Carry cells and common rational centers

Fix \(A,B\). Inside the corresponding carry cell, CF3 becomes

\[
\det\bigl(U,(\alpha-1)B-(\beta-1)A\bigr)
=p\det(A,B).
\]

For one coordinate \(q\in\{1,\ldots,p-1\}\), the pair

\[
\left(
\left\lfloor\frac{\alpha q}{p}\right\rfloor,
\left\lfloor\frac{\beta q}{p}\right\rfloor
\right)
\]

is constant on at most

\[
\rho_{\alpha,\beta}\le\alpha+\beta-1
\]

intervals. Hence the square has at most \(\rho_{\alpha,\beta}^2\) joint carry cells.

### Theorem CF4 — PROVED

For one modular-hyperbola channel \(H_c\):

1. every nondegenerate cell,
   \[
   (\alpha-1)B\ne(\beta-1)A,
   \]
   contains at most two aligned points of \(H_c\);
2. the total nondegenerate aligned population is at most
   \[
   \boxed{2\rho_{\alpha,\beta}^2};
   \]
3. writing
   \[
   d=\gcd(\alpha-1,\beta-1),
   \quad
   \alpha-1=d\alpha',
   \quad
   \beta-1=d\beta',
   \]
   a carry cell is degenerate exactly when
   \[
   A=\alpha'S,
   \qquad B=\beta'S
   \]
   for some \(S\in\{0,\ldots,d\}^2\);
4. there are at most \((d+1)^2\) degenerate cells, and every point in such a cell is automatically aligned through
   \[
   \boxed{C_S=\frac p dS.}
   \]

### Proof

A nondegenerate cell imposes one genuine real line. A real line meets a lifted prime modular-hyperbola channel in at most two points after primitive normalization and reduction modulo \(p\).

For a degenerate cell,

\[
(\alpha-1)B=(\beta-1)A.
\]

Coprimality of \(\alpha',\beta'\) gives \(A=\alpha'S\), \(B=\beta'S\). Substitution yields

\[
P_\alpha(U)-U
=(\alpha-1)\left(U-\frac p dS\right),
\]

\[
P_\beta(U)-U
=(\beta-1)\left(U-\frac p dS\right),
\]

so both lifted points lie on the radial line through \(U\) and \(C_S\). \(\square\)

Theorem CF4 is a geometric companion to CA1–CA4. The CA theorem gives a sharp factorization and divisor bound inside each aligned signature; CF4 describes every degenerate scalar cell by one explicit rational center.

## 5. Factorisation inside a perfect-wrap chamber

Fix a degenerate chamber with index

\[
S=(s_x,s_y).
\]

For \(U=(x,y)\) in this chamber define centered integer coordinates

\[
X=d x-p s_x,
\qquad
Y=d y-p s_y.
\]

Put

\[
m=\max(\alpha,\beta)
\]

and

\[
\Delta_p^{\mathrm{wrap}}
=
\max_{1\le n<p^2}\tau(n).
\]

### Theorem CF5 — PROVED

Every point \(U\in H_c\) in the chamber satisfies

\[
\boxed{XY\equiv d^2c\pmod p}
\]

and

\[
\boxed{|X|,|Y|<\frac{pd}{m}.}
\]

Consequently the chamber contains at most

\[
\boxed{
2\left(
\left\lceil\frac{2pd^2}{m^2}\right\rceil+1
\right)
\Delta_p^{\mathrm{wrap}}
}
\]

points of \(H_c\).

### Proof

For either multiplier \(\gamma\in\{\alpha,\beta\}\), write

\[
\gamma-1=d\gamma'.
\]

The chamber condition in one coordinate is

\[
\left\lfloor\frac{\gamma x}{p}\right\rfloor
=
\gamma's_x.
\]

Therefore

\[
-\frac{ps_x}{\gamma}
\le
X
<
\frac{p(d-s_x)}{\gamma}.
\]

Using the larger multiplier gives \(|X|<pd/m\), and the same argument gives the bound for \(Y\).

Since \(xy\equiv c\pmod p\),

\[
XY=(dx-ps_x)(dy-ps_y)
\equiv d^2c\pmod p.
\]

Thus

\[
XY=d^2c+pt
\]

for an integer \(t\). The interval \(|XY|<(pd/m)^2\) allows at most

\[
\left\lceil\frac{2pd^2}{m^2}\right\rceil+1
\]

values of \(t\). Each nonzero integer \(d^2c+pt\), whose absolute value is below \(p^2\), has at most \(2\tau(|d^2c+pt|)\) ordered signed factorisations \((X,Y)\). The map \(U\mapsto(X,Y)\) is injective. \(\square\)

### Corollary CF6 — PROVED

If \(E_{\mathrm{wrap}}\) perfectly aligned points occupy \(h\) nonempty degenerate chambers, then

\[
\boxed{
h\ge
\frac{E_{\mathrm{wrap}}}{
2(\lceil2pd^2/m^2\rceil+1)\Delta_p^{\mathrm{wrap}}}.}
\]

In particular, a large perfect-alignment class either disperses through many explicit rational centers or has multipliers with a large common divisor relative to their size.

## 6. Canonical alternating transition

The combined transition is Theorem SC3 in the secant-star chapter:

\[
\boxed{
\text{paid common-ratio bank}
\Longrightarrow
\text{improvement, carry dispersion, or perfect alignment}.
}
\]

CF1–CF6 refine its structural outputs:

- same-channel stars have anchor-specific cross-carry dispersion;
- perfect-alignment cells have explicit rational centers;
- every perfect-wrap chamber has divisor-controlled occupancy.

No high-load branch is now anonymous. The remaining issue is termination: one must prove that repeated alternating propagation cannot indefinitely create new carry signatures and wrap centers without either exhausting their finite budget or entering an absorbable algebraic exception.

## 7. Remaining target

### Target CF7 — OPEN: monotone carry-complexity potential

Construct a potential charging:

- product-carry signatures from SC2;
- same-channel cross-carry levels from CF2;
- nondegenerate aligned signatures from CA4;
- occupied perfect-wrap centers from CF6.

Prove that every non-improving alternating closure step raises this potential by a quantified amount, while the total possible potential is bounded by the size and channel complexity of the active core.

## Verification

```bash
python scripts/verify_carry_closure.py --prime 17
```

checks CF1–CF5 exhaustively for small odd primes. It is a finite sanity check, not a proof for arbitrary \(p\).
