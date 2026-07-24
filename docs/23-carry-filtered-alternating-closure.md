# Carry-filtered alternating closure

This chapter begins the alternating-closure phase after the weighted common-ratio bank theorem. It uses the exact projective secant geometry from [`22-incidence-conic-pencil.md`](22-incidence-conic-pencil.md), but keeps track of the integer carries discarded by projective reduction.

The output is a rigorous partial closure theorem:

- a same-channel secant star must disperse through many integer carry levels;
- a large aligned-anchor class must either be bounded by a carry-cell count or concentrate in explicitly described common-wrap chambers.

The remaining cases are cross-channel secant stars and the common-wrap chambers themselves.

Throughout, residues are represented by integers in \(\{1,\ldots,p-1\}\).

## 1. Same-channel cross carries

Fix distinct channels \(H_a,H_b\), put \(r=b/a\), and take an anchor

\[
B_z=(z,w)=\left(z,\left\langle\frac bz\right\rangle_p\right)\in H_b.
\]

For \(x\in\mathbb F_p^*\), let

\[
u=T_z(x)=\frac{z(x-z)}{rx-z}
\]

be the second projective intersection with \(H_a\). We only consider fully affine nonfixed orbits, so \(x,u\notin\{0,\infty\}\) and \(x\ne u\). Write

\[
P_x=(x,y_x),\qquad P_u=(u,y_u),
\]

with \(y_t=\langle a/t\rangle_p\).

### Theorem CF1 — PROVED

For every oriented affine secant parameter \(x\),

\[
\boxed{
(x-z)(y_u-w)\equiv b-a\pmod p.
}
\]

Hence the cross carry

\[
\kappa_z(x)
=
\frac{(x-z)(y_u-w)-(b-a)}p
\]

is an integer. Moreover,

\[
\boxed{
B_z,P_x,P_u\text{ are real-collinear}
\iff
\kappa_z(x)=\kappa_z(u).
}
\]

### Proof

The projective secant relation says that \(B_z,P_x,P_u\) are collinear modulo \(p\). Comparing the two displacement slopes gives

\[
(x-z)(y_u-w)\equiv(u-z)(y_x-w)\pmod p.
\]

Using \(y_u\equiv a/u\), \(w\equiv b/z\), and the secant equation

\[
r xu=z(x+u-z),
\]

one obtains

\[
(x-z)(y_u-w)\equiv b-a\pmod p.
\]

The real determinant is

\[
(x-z)(y_u-w)-(u-z)(y_x-w).
\]

Both terms are congruent to \(b-a\) modulo \(p\), so dividing their difference by \(p\) gives the carry equality. \(\square\)

## 2. Divisor control at one carry level

For an integer carry value \(t\), put

\[
N_t=b-a+pt.
\]

Because the two coordinate differences lie in \([-(p-2),p-2]\), every represented level satisfies

\[
0<|N_t|\le(p-2)^2.
\]

Let \(s_t(z;a,b)\) be the number of real affine secant pairs through \(B_z\) on \(H_a\) with common carry \(t\).

### Theorem CF2 — PROVED

For every carry level,

\[
\boxed{
s_t(z;a,b)\le \tau(|N_t|),
}
\]

where \(\tau(n)\) is the positive-divisor function.

Consequently, if a same-channel real secant star contains \(M\) pairs, then it occupies at least

\[
\boxed{
\frac{M}{\Delta_p}
}
\]

distinct carry levels, where

\[
\Delta_p=\max_{1\le n\le(p-2)^2}\tau(n).
\]

The classical maximal-order bound for the divisor function gives

\[
\Delta_p=\exp\!\left(O\!\left(\frac{\log p}{\log\log p}\right)\right)=p^{o(1)}.
\]

### Proof

Fix \(t\). An oriented parameter \(x\) at that level satisfies

\[
(x-z)(y_u-w)=N_t.
\]

The nonzero integer \(x-z\) is a signed divisor of \(N_t\), and it determines \(x\). Thus there are at most \(2\tau(|N_t|)\) oriented parameters at level \(t\). Each real secant pair contributes exactly two orientations, proving the first bound. The dispersion bound follows by summing over represented levels. \(\square\)

### Interpretation

A large same-channel secant star cannot be supported by one carry value or by a bounded family of carry values. Projectively, all secants belong to one involution; in the real lift, a polynomially large star must spread across polynomially many carry levels up to a subpolynomial loss.

## 3. Scalar lifts and wrap vectors

The aligned-anchor obstruction from the common-ratio conversion theorem has a different form. Let

\[
U=(x,y)\in[1,p-1]^2
\]

and let \(\alpha,\beta\in\{2,\ldots,p-1\}\) be distinct. Define the coordinatewise lifted multiples

\[
P_\alpha(U)=\langle\alpha U\rangle_p,
\qquad
P_\beta(U)=\langle\beta U\rangle_p,
\]

and their carry vectors

\[
K_\alpha(U)=
\left(
\left\lfloor\frac{\alpha x}{p}\right\rfloor,
\left\lfloor\frac{\alpha y}{p}\right\rfloor
\right),
\]

\[
K_\beta(U)=
\left(
\left\lfloor\frac{\beta x}{p}\right\rfloor,
\left\lfloor\frac{\beta y}{p}\right\rfloor
\right).
\]

Then

\[
P_\alpha(U)=\alpha U-pK_\alpha(U),
\qquad
P_\beta(U)=\beta U-pK_\beta(U).
\]

### Theorem CF3 — PROVED

Put \(A=K_\alpha(U)\) and \(B=K_\beta(U)\). The three lifted points

\[
U,P_\alpha(U),P_\beta(U)
\]

are real-collinear if and only if

\[
\boxed{
p\det(A,B)
=(\alpha-1)\det(U,B)-(\beta-1)\det(U,A).
}
\]

### Proof

The two displacement vectors from \(U\) are

\[
P_\alpha(U)-U=(\alpha-1)U-pA,
\]

\[
P_\beta(U)-U=(\beta-1)U-pB.
\]

Expanding their determinant and dividing by \(p\) gives the displayed identity. \(\square\)

## 4. Carry cells

Fix the carry vectors \(A,B\). Inside that carry cell, CF3 becomes the affine-line equation

\[
\det\bigl(U,(\alpha-1)B-(\beta-1)A\bigr)
=p\det(A,B).
\]

For one coordinate \(t\in\{1,\ldots,p-1\}\), the pair

\[
\left(
\left\lfloor\frac{\alpha t}{p}\right\rfloor,
\left\lfloor\frac{\beta t}{p}\right\rfloor
\right)
\]

is constant on at most

\[
\rho_{\alpha,\beta}\le\alpha+\beta-1
\]

intervals. Hence the square is partitioned into at most \(\rho_{\alpha,\beta}^2\) joint carry cells.

### Theorem CF4 — PROVED

Let \(H_c\) be one modular-hyperbola channel. In every carry cell satisfying

\[
(\alpha-1)B\ne(\beta-1)A,
\]

the aligned collinearity condition contains at most two points of \(H_c\).

Therefore the total number of aligned points outside the degenerate carry cells is at most

\[
\boxed{
2\rho_{\alpha,\beta}^2
\le2(\alpha+\beta-1)^2.
}
\]

Let

\[
d=\gcd(\alpha-1,\beta-1),
\quad
\alpha-1=d\alpha',
\quad
\beta-1=d\beta'.
\]

A carry cell is degenerate precisely when there is

\[
S=(s_x,s_y)\in\{0,\ldots,d\}^2
\]

such that

\[
A=\alpha'S,
\qquad
B=\beta'S.
\]

There are at most

\[
\boxed{(d+1)^2}
\]

degenerate cells. In such a cell, every point \(U\) satisfies

\[
P_\alpha(U)-U
=(\alpha-1)
\left(U-\frac p d S\right),
\]

\[
P_\beta(U)-U
=(\beta-1)
\left(U-\frac p d S\right).
\]

Thus all three points are automatically collinear through the rational center

\[
\boxed{C_S=\frac p d S.}
\]

### Proof

In a nondegenerate cell the carry equation is one genuine real affine line. Any real line meets one lifted prime modular-hyperbola channel in at most two points: after dividing the line equation by its integer content, reduction modulo \(p\) gives either a nonzero line equation or no solutions, and a nonzero line meets the conic \(XY=cZ^2\) at most twice.

For degeneracy, the vector equation

\[
(\alpha-1)B=(\beta-1)A
\]

and coprimality of \(\alpha',\beta'\) imply

\[
A=\alpha'S,
\qquad B=\beta'S
\]

coordinatewise, with \(0\le s_x,s_y\le d\). Substitution into the lifted displacement formulas yields the common-center identities. \(\square\)

## 5. Application to aligned anchors

In the common-ratio bank, one switched point is

\[
U_i=\left(x_i,\frac{a}{g x_i}\right)\in H_{a/g}.
\]

Its companion is the coordinatewise \(g\)-multiple

\[
V_i=P_g(U_i),
\]

and an aligned opposite-colour anchor with

\[
\lambda^2=bg/a
\]

is

\[
W_i=P_\lambda(U_i).
\]

Assume \(1,g,\lambda\) are distinct; otherwise two of the three points coincide and there is no genuine triple.

### Corollary CF5 — PROVED

Represent \(g,\lambda\) by integers in \(\{2,\ldots,p-1\}\), and let

\[
\rho=\rho_{g,\lambda},
\qquad
d=\gcd(g-1,\lambda-1).
\]

For any aligned-anchor signature, at most

\[
\boxed{2\rho^2\le2(g+\lambda-1)^2}
\]

real aligned anchors lie outside the common-wrap chambers.

If the aligned-anchor multiplicity is \(\Lambda>2\rho^2\), then at least

\[
\boxed{\Lambda-2\rho^2}
\]

of its bases lie in a union of at most \((d+1)^2\) explicit chambers, each radial about one center

\[
\frac p d(s_x,s_y).
\]

## 6. Partial alternating-closure theorem

Combining CF2 and CF5 with the common-ratio decoder-or-structure theorem gives the following refinement.

### Theorem CF6 — PROVED

A failed paid common-ratio bank produces one of the following:

1. an improving rectangle;
2. a cross-channel secant star;
3. a same-channel secant star dispersed over at least \(M/\Delta_p\) integer carry levels;
4. an aligned-anchor family with at most \(2\rho^2\) nonexceptional members;
5. concentration in at most \((d+1)^2\) explicit common-wrap radial chambers.

Thus the previously anonymous alternating obstruction has been reduced to two unresolved geometric mechanisms:

- cross-channel carry-filtered secant stars;
- dense occupation of common-wrap chambers.

## 7. Next exact targets

### Target CF7: cross-channel carry factorization

For a real line through an anchor on \(H_b\), with one endpoint on \(H_a\) and one on \(H_c\), find an integer factorization or low-degree carry invariant giving a divisor-type bound analogous to CF2.

### Target CF8: common-wrap chamber sparsity

Each degenerate chamber has side lengths at most

\[
\frac{p}{\max(\alpha,\beta)}.
\]

Prove that a modular hyperbola cannot occupy many such chambers heavily unless its parameters lie in one of the already classified multiplicative-coset exceptions. Results on close points of modular hyperbolas are directly relevant here, but no uniform chamber-sparsity theorem sufficient for the full closure argument is proved in this notebook.

## Verification

The script

```bash
python scripts/verify_carry_closure.py --prime 17
```

checks CF1–CF4 exhaustively for small odd primes. It is a finite verification, not a proof for arbitrary \(p\).
