# Carry-filtered secant stars and wrap cells

This chapter complements [`23-aligned-anchor-carry-cells.md`](23-aligned-anchor-carry-cells.md). That chapter gives a detailed determinant factorization for aligned anchors in the original hyperbola parameters. Here we prove two additional geometric statements:

1. same-channel secant stars admit an exact integer carry factorization and a divisor bound at each carry level;
2. coordinatewise scalar lifts admit a universal wrap-cell classification with explicit rational centers.

Together with the paid common-ratio conversion theorem, these statements reduce the alternating-closure obstruction to cross-channel stars and explicitly classified perfect-wrap chambers.

Throughout, residues are represented by integers in \(\{1,\ldots,p-1\}\).

## 1. Same-channel cross carries

Fix distinct channels \(H_a,H_b\), put \(r=b/a\), and take

\[
B_z=(z,w)=\left(z,\left\langle\frac bz\right\rangle_p\right)\in H_b.
\]

For \(x\in\mathbb F_p^*\), let

\[
u=T_z(x)=\frac{z(x-z)}{rx-z}
\]

be its partner under the projective secant involution on \(H_a\). Consider only fully affine nonfixed orbits. Write

\[
P_x=(x,y_x),\qquad P_u=(u,y_u),
\qquad y_t=\left\langle\frac at\right\rangle_p.
\]

### Theorem CF1 — PROVED

For every oriented affine secant parameter \(x\),

\[
\boxed{(x-z)(y_u-w)\equiv b-a\pmod p.}
\]

Hence

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
(x-z)(y_u-w)\equiv(u-z)(y_x-w)\pmod p.
\]

Using \(y_u\equiv a/u\), \(w\equiv b/z\), and

\[
r xu=z(x+u-z),
\]

shows that each cross product is congruent to \(b-a\). Their difference is the real collinearity determinant, so it vanishes exactly when the two integer carries agree. \(\square\)

## 2. Divisor control and carry dispersion

For a carry level \(t\), put

\[
N_t=b-a+pt.
\]

Every represented level satisfies

\[
0<|N_t|\le(p-2)^2.
\]

Let \(s_t(z;a,b)\) be the number of real secant pairs through \(B_z\), with both endpoints in \(H_a\), having common carry \(t\).

### Theorem CF2 — PROVED

\[
\boxed{s_t(z;a,b)\le\tau(|N_t|),}
\]

where \(\tau\) is the positive-divisor function.

Consequently, a same-channel real secant star containing \(M\) pairs occupies at least

\[
\boxed{\frac{M}{\Delta_p}}
\]

distinct carry levels, where

\[
\Delta_p=\max_{1\le n\le(p-2)^2}\tau(n)
=
\exp\!\left(O\!\left(\frac{\log p}{\log\log p}\right)\right)
=p^{o(1)}.
\]

### Proof

At level \(t\), every oriented parameter satisfies

\[
(x-z)(y_u-w)=N_t.
\]

The nonzero integer \(x-z\) is a signed divisor of \(N_t\) and determines \(x\). Thus there are at most \(2\tau(|N_t|)\) oriented parameters. Each real secant pair contributes two orientations. \(\square\)

This gives a genuine carry-dispersion theorem: a polynomially large same-channel star cannot remain inside a bounded family of carry levels.

## 3. Universal scalar wrap criterion

Let

\[
U=(x,y)\in[1,p-1]^2
\]

and take distinct \(\alpha,\beta\in\{2,\ldots,p-1\}\). Define

\[
P_\alpha(U)=\langle\alpha U\rangle_p,
\qquad
P_\beta(U)=\langle\beta U\rangle_p
\]

coordinatewise, and set

\[
K_\alpha(U)=
\left(
\left\lfloor\frac{\alpha x}{p}\right\rfloor,
\left\lfloor\frac{\alpha y}{p}\right\rfloor
\right),
\]

with \(K_\beta(U)\) defined analogously.

### Theorem CF3 — PROVED

Writing \(A=K_\alpha(U)\), \(B=K_\beta(U)\), the points

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

## 4. Nondegenerate cells and common-wrap centers

Fix \(A,B\). Inside that carry cell, CF3 is

\[
\det\bigl(U,(\alpha-1)B-(\beta-1)A\bigr)
=p\det(A,B).
\]

The pair of one-dimensional carries

\[
\left(
\left\lfloor\frac{\alpha t}{p}\right\rfloor,
\left\lfloor\frac{\beta t}{p}\right\rfloor
\right)
\]

is constant on at most

\[
\rho_{\alpha,eta}\le\alpha+\beta-1
\]

intervals. Hence there are at most \(\rho_{\alpha,eta}^2\) two-dimensional carry cells.

### Theorem CF4 — PROVED

For one modular-hyperbola channel \(H_c\):

1. every nondegenerate carry cell,
   \[
   (\alpha-1)B\ne(\beta-1)A,
   \]
   contains at most two aligned points of \(H_c\);
2. the total nondegenerate aligned population is at most
   \[
   \boxed{2\rho_{\alpha,eta}^2};
   \]
3. writing
   \[
   d=\gcd(\alpha-1,\beta-1),
   \quad
   \alpha-1=d\alpha',
   \quad
   \beta-1=d\beta',
   \]
   a cell is degenerate exactly when
   \[
   A=\alpha'S,
   \qquad B=\beta'S
   \]
   for some \(S\in\{0,\ldots,d\}^2\);
4. there are at most \((d+1)^2\) degenerate cells, and every point in one such cell is automatically aligned through the rational center
   \[
   \boxed{C_S=\frac p dS.}
   \]

### Proof

A nondegenerate cell imposes one genuine real line. A real line meets a lifted prime modular-hyperbola channel in at most two points, after primitive normalization and reduction modulo \(p\).

For a degenerate cell,

\[
(\alpha-1)B=(\beta-1)A.
\]

Coprimality of \(\alpha',\beta'\) gives \(A=\alpha'S\), \(B=\beta'S\). Then

\[
P_\alpha(U)-U
=(\alpha-1)\left(U-\frac p dS\right),
\]

\[
P_\beta(U)-U
=(\beta-1)\left(U-\frac p dS\right),
\]

which proves the common-center statement. \(\square\)

Theorem CF4 is a geometric companion to CA1–CA4: CA2 gives a divisor bound per nondegenerate aligned signature, while CF4 gives a global line bound per scalar carry cell and identifies every degenerate cell by an explicit rational center.

## 5. Partial alternating-closure reduction

### Theorem CF5 — PROVED

A failed paid common-ratio bank produces at least one of the following:

1. an improving rectangle;
2. a cross-channel secant star;
3. a same-channel secant star spread over at least \(M/\Delta_p\) carry levels;
4. an aligned-anchor family dispersed over many nondegenerate carry signatures, as in CA4;
5. a large perfect-alignment population in explicit carry slabs, and in the scalar-cell formulation, inside at most \((d+1)^2\) common-wrap radial chambers.

Thus the remaining alternating-closure mechanisms are now:

- **cross-channel stars**, for which a two-channel carry factorization is still missing;
- **perfect-wrap chambers**, which require a chamber-sparsity or absorber theorem.

## 6. Next exact targets

### Target CF6: cross-channel carry factorization

For one line through an anchor on \(H_b\), with endpoints on distinct channels \(H_a,H_c\), find a fixed-degree integer carry invariant giving a divisor-type bound analogous to CF2.

### Target CF7: perfect-wrap chamber sparsity

A degenerate scalar cell has side lengths at most

\[
\frac{p}{\max(\alpha,\beta)}.
\]

Prove that many modular-hyperbola points cannot occupy these cells unless they form one of the multiplicative-coset exceptions already isolated by the inverse-additive theory.

## Verification

```bash
python scripts/verify_carry_closure.py --prime 17
```

checks CF1–CF4 exhaustively for small odd primes. It is a finite sanity check, not a proof for arbitrary \(p\).
