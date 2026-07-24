# Arithmetic classification of perfect-alignment chambers

This chapter sharpens the perfect-affine exception from the aligned-anchor carry theorem. It classifies every scalar parameter for which the leading carry coefficient vanishes and proves denominator-sensitive sparsity for the resulting perfect-alignment chambers.

Throughout, `p` is an odd prime. Fix

\[
g\in\{2,\ldots,p-1\},
\qquad
h=\langle g^{-1}\rangle_p,
\]

and write

\[
gh=1+\mu p.
\]

For `lambda in {1,...,p-1}`, put

\[
m=\langle\lambda h\rangle_p,
\]

\[
h\lambda=m+\rho p,
\qquad
gm=\lambda+\nu p,
\]

and recall the aligned-anchor leading carry coefficient

\[
\eta=-\mu+\nu+\rho.
\]

## 1. Exact interpolation-parameter classification

### Lemma PA1 — PROVED

\[
\boxed{
\eta=\mu(\lambda-1)-(g-1)\rho.
}
\]

Let

\[
d=\gcd(\mu,g-1),
\qquad
\mu=d\mu_0,
\qquad
g-1=dv_0.
\]

Then

\[
\boxed{
\eta=0
\iff
\lambda=1+tv_0
}
\]

for a unique integer

\[
0\le t\le d.
\]

For this parameter,

\[
\boxed{
\rho=t\mu_0,
\qquad
m=h-t\frac{h-1}{d}.
}
\]

### Proof

From

\[
g(h\lambda-\rho p)=\lambda+\nu p
\]

and `gh=1+mu p`, one obtains

\[
\nu=\lambda\mu-g\rho.
\]

Substitution gives the first identity.

If `eta=0`, then

\[
\mu_0(\lambda-1)=v_0\rho.
\]

Coprimality of `mu_0,v_0` gives

\[
\lambda=1+tv_0,
\qquad
\rho=t\mu_0
\]

for an integer `t>=0`. Also `d` divides `h-1`: modulo `d`, the identities `g=1`, `mu=0`, and `gh=1+mu p` give `h=1`. Hence

\[
m=h\lambda-p\rho
=h+t\frac{h(g-1)-p\mu}{d}
=h-t\frac{h-1}{d}.
\]

Since `1<=m<=h`, one has `0<=t<=d`.

Conversely, every `t` in this range gives integer `lambda,rho,m` by the displayed formulas, and direct substitution gives `eta=0`. \(\square\)

The endpoint parameters are

\[
t=0:\quad \lambda=1,\ W_x=U_x,
\]

and

\[
t=d:\quad \lambda=g,\ W_x=V_x.
\]

An admissible aligned anchor is distinct from both inserted cells, so only

\[
1\le t\le d-1
\]

can contribute to the perfect-alignment obstruction. In particular, when

\[
\gcd(\mu,g-1)=1,
\]

there is no admissible perfect-alignment parameter.

## 2. Reduced denominator and wrap-index criterion

Fix an interior parameter and write

\[
\frac{t}{d}=\frac{t'}q,
\qquad
q=\frac d{\gcd(t,d)},
\qquad
\gcd(t',q)=1.
\]

Thus `q>=2` is the reduced denominator of the affine interpolation parameter.

For a base point

\[
(x,y)\in H_a,
\qquad y=\langle a/x\rangle_p,
\]

put

\[
A=\left\lfloor\frac{gx}{p}\right\rfloor,
\qquad
B=\left\lfloor\frac{hy}{p}\right\rfloor.
\]

### Theorem PA2 — PROVED

For an `eta=0` interpolation parameter, the aligned anchor is perfectly affine-interpolated between the switched endpoints if and only if

\[
\boxed{q\mid A\quad\text{and}\quad q\mid B.}
\]

Equivalently, the source and target wrap indices both lie in the zero residue class modulo the reduced denominator.

### Proof

The interpolation residuals from the aligned carry theorem are

\[
R_x=(\lambda-1)A-(g-1)D
\]

and

\[
R_y=(g-\lambda)B-(g-1)C,
\]

because `eta=0`. Using

\[
\lambda-1=\frac td(g-1)
\]

gives

\[
R_x=0
\iff
dD=tA
\iff q\mid A.
\]

For the converse implication, when `q|A`, the point

\[
x+\frac td(\langle gx\rangle_p-x)
\]

is an integer in `[1,p-1]`, is congruent to `lambda x` modulo `p`, and hence equals `\langle\lambda x\rangle_p`; therefore `R_x=0`.

Similarly,

\[
g-\lambda=\frac{d-t}{d}(g-1),
\]

and `gcd(d-t,d)=gcd(t,d)`, so

\[
R_y=0\iff q\mid B.
\]

The two residuals vanish exactly when the real affine interpolation is exact. \(\square\)

The arithmetic behind this criterion is consistent in both coordinates. Since `q` divides `d`, it divides `g-1` and `mu`; reducing

\[
gh=1+\mu p
\]

modulo `q` also gives

\[
h\equiv1\pmod q.
\]

## 3. Denominator-sensitive chamber sparsity

Let

\[
\mathcal P_{a,g,t}
=
\left\{
 x\in\mathbb F_p^*:
 q\mid\left\lfloor\frac{gx}{p}\right\rfloor,
 q\mid\left\lfloor\frac{h\langle a/x\rangle_p}{p}\right\rfloor
\right\}.
\]

### Theorem PA3 — PROVED

The perfect-alignment population satisfies

\[
\boxed{
|\mathcal P_{a,g,t}|
\le
\min\left\{
\left\lceil\frac gq\right\rceil
\left\lceil\frac pg\right\rceil,
\left\lceil\frac hq\right\rceil
\left\lceil\frac ph\right\rceil
\right\}.
}
\]

In particular,

\[
\boxed{|\mathcal P_{a,g,t}|\le\frac{4p}{q}.}
\]

Consequently, if one perfect-alignment parameter contains at least `epsilon p` base points, then

\[
\boxed{q\le\frac4\epsilon.}
\]

### Proof

The carry

\[
A=\left\lfloor\frac{gx}{p}\right\rfloor
\]

ranges through `0,...,g-1`. At most `ceil(g/q)` of these values are divisible by `q`. For a fixed value of `A`, the defining interval for `x` contains at most `ceil(p/g)` integers. This gives the first bound in the minimum.

Apply the same argument to

\[
B=\left\lfloor\frac{hy}{p}\right\rfloor
\]

and use that `x -> y=\langle a/x\rangle_p` is a permutation to obtain the second bound.

Because `q<=g-1` and `q<=h-1` for an interior parameter, each ceiling product is at most `4p/q`. \(\square\)

## 4. Consequence for alternating closure

The perfect-alignment branch is now divided into two regimes.

1. **Large denominator.** Its population is quantitatively sparse by PA3.
2. **Small denominator.** Every point lies at one of finitely many rational affine positions
   \[
   \frac{t'}q,
   \qquad q=O(1),
   \]
   and its source and target wrap indices are constrained modulo `q`.

Thus a positive-density perfect-wrap obstruction is a bounded-denominator object. The next absorber problem is finite-dimensional:

> For every fixed denominator `q`, construct a row-column-preserving alternating trade that absorbs the `q`-striped perfect-interpolation chambers, or classify the finite list of multiplicative-coset exceptions in which such a trade can be frozen.

This is stronger than treating perfect-wrap chambers as arbitrary dense subsets of the grid.
