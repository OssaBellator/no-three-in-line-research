# Protected-slope rigidity and the growing-uniformity window

PX175 proves that a direct polynomial rectangle codegree saving requires
polynomially many protected directions.  There is also an upper rigidity
threshold: if too many finite-field slopes are protected, every simultaneous-
rainbow permutation is affine and therefore has the rank-three freezing from
PX140.

The external input is the Rédei--Megyesi direction theorem: a set of \(p\)
points in \(\mathbb F_p^2\) which is not a line determines at least

\[
\frac{p+3}{2}
\]

projective directions.

Let

\[
f:\mathbb F_p\to\mathbb F_p
\]

be a permutation.  Its graph determines neither the vertical direction nor the
horizontal direction.  Let \(R\subseteq\mathbb F_p^*\) be a set of protected
finite slopes, meaning that

\[
f(v)-f(u)\ne r(v-u)
\]

for every \(r\in R\) and every \(u\ne v\).  Equivalently, each map

\[
x\longmapsto f(x)-rx
\]

is a permutation.

## Theorem PX176 -- PROVED USING THE RÉDEI--MEGYESI THEOREM

If

\[
\boxed{
|R|>\frac{p-5}{2},
}
\]

then \(f\) is affine:

\[
\boxed{
f(x)=gx+b}
\]

for one slope \(g\notin R\).

Consequently, any probability distribution supported on permutations protecting
such an \(R\) is a distribution on affine graphs.  Its rank-three cylinder
constant is \(\Omega(p)\), so it cannot satisfy the subpower protected-spread
conclusion of PX173.

### Proof

If the graph is not a line, Rédei--Megyesi says that it determines at least
\((p+3)/2\) directions.  Because \(f\) is a function, the vertical direction
is absent.  Because it is a permutation, the horizontal direction is absent.
Every finite nonzero direction in \(R\) is absent by protection.  Thus the
number of directions it can determine is at most

\[
(p-1)-|R|.
\]

Under the displayed hypothesis,

\[
(p-1)-|R|<\frac{p+3}{2},
\]

contradicting the theorem.  Hence the graph is a line.  A nonvertical line
which is the graph of a permutation has the displayed affine form, and its
slope cannot lie in \(R\).

The rank-three statement is PX140, or equivalently the affine freezing
calculation in PX101. \(\square\)

## 2. Height families

For an integer cutoff \(H\), let

\[
R_H
=
\left\{
\pm ba^{-1}\pmod p:
1\le a,b\le H,
\ \gcd(a,b)=1
\right\}.
\]

This is the slope family required to protect all positive and negative
primitive integer directions through height \(H\), after multiplying by the
fixed local scalar.

When

\[
2H^2<p,
\]

reduced rational pairs do not collide modulo \(p\), and positive and negative
slopes are disjoint.  Therefore

\[
|R_H|
=2\#\{(a,b)\in[H]^2:\gcd(a,b)=1\}
\ge\frac{H^2}{2}.
\]

The lower bound uses the elementary coprime-pair estimate from PX175.

PX176 implies that once \(|R_H|>(p-5)/2\), every exact protected permutation
is affine.  Thus finite-field direction protection cannot simultaneously have
both of the following properties:

1. more than half of all nonzero slopes protected;
2. nonlinear rank-three spread.

## 3. Combined exponent window

Suppose one seeks rectangle conflict codegree

\[
d^{1-\varepsilon},
\qquad d=n^3.
\]

PX175 requires at least

\[
\Omega(n^{6\varepsilon})
\]

protected real direction classes.  PX176 allows a nonlinear local permutation
only while the corresponding finite-field slope set has size at most about
\(p/2\).

For a one-prime local model with \(p\asymp n\), the natural open exponent
window is therefore

\[
\boxed{0<\varepsilon<\frac16.}
\]

This is not an existence theorem inside the window.  It identifies where a
growing-uniformity theorem could possibly work:

- PX175 rules out fixed or polylogarithmic uniformity for a fixed polynomial
  saving;
- PX176 rules out protecting a positive majority of all slopes while retaining
  nonlinear spread;
- a successful theorem must handle \(p^\kappa\) simultaneous forms for some
  \(0<\kappa<1\), with \(\kappa=6\varepsilon\) in the direct rectangle
  application.

## Verification

Run

```bash
python scripts/verify_product_direction_rigidity.py
```

The verifier exhausts the protected-slope permutation problem at
\((p,H)=(5,1),(7,2),(11,2)\) and confirms that every solution is affine, with
exactly \(p(p-1-|R_H|)\) solutions.

The asymptotic theorem uses Rédei--Megyesi rather than the finite verifier.
