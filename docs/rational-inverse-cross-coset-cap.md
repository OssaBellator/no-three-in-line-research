# Uniform cross-coset collision caps

RI2c localizes a loss of target cosets to one bilinear curve between two
source cosets. The four-point character calculation used for RI1d also
counts that curve uniformly for every pair of source cosets.

Let \(H\leq\mathbb F_p^\times\) have index \(m\) and order
\(h=(p-1)/m\). For source cosets \(x_iH,x_jH\), put

\[
J_{ij}
=
\left|\left\{
x\in x_iH\setminus\{1,r\}:
\tau_r(x)\in x_jH
\right\}\right|,
\]

where

\[
\tau_r(x)=\frac{r(x-1)}{x-r}.
\]

As before, define

\[
A_m(p)
=
\frac{p-3}{m^2}
+3\left(1-\frac1{m^2}\right)\sqrt p.
\]

## RI2d -- cross-coset Weil cap

### Theorem RI2d -- PROVED

For every ordered pair of source cosets,

\[
\boxed{
\left|J_{ij}-\frac{p-3}{m^2}\right|
\le
3\left(1-\frac1{m^2}\right)\sqrt p,
}
\]

and hence \(J_{ij}\le A_m(p)\).

If

\[
C=\bigcup_{i=1}^s x_iH,
\qquad
D=C\setminus\{1,r\},
\]

then the number of full nonfixed collision pairs in \(D\) satisfies

\[
\boxed{
|\mathcal P_r(D)|
\le
\frac{s^2}{2}A_m(p).
}
\]

### Proof

Write \(x=x_i u\). Membership of \(x\) in \(x_iH\) and of
\(\tau_r(x)\) in \(x_jH\) is detected by two order-\(m\) character
averages. Up to a constant character factor, the \((a,b)\)-summand is
the character of

\[
u^a(x_i u-1)^b(x_i u-r)^{-b}.
\]

This is exactly the four-point divisor from RI1d. After the same
\(m\)-th-power mask, the principal term contributes \(p-3\), while each
of the other \(m^2-1\) terms has absolute value at most \(3\sqrt p\).
Division by \(m^2\) proves the first box.

Partition the collision pairs by their unordered source-coset type. For
\(i<j\), each pair between \(x_iH\) and \(x_jH\) is counted exactly once
by \(J_{ij}\), so that type has at most \(A_m(p)\) pairs. Within one
coset, every nonfixed pair contributes two endpoints to \(J_{ii}\), so
the diagonal type has at most \(A_m(p)/2\) pairs. Summing over
\(\binom s2\) off-diagonal and \(s\) diagonal types gives

\[
\binom s2 A_m(p)+\frac{s}{2}A_m(p)
=
\frac{s^2}{2}A_m(p).
\]

\(\square\)

## RI2e -- quantitative union coverage

### Corollary RI2e -- PROVED

Let \(e=|C\cap\{1,r\}|\), and let \(k\) be the number of target
\(H\)-cosets met by \(F_r(D)\). Then

\[
\boxed{
(s-k)h
\le
e+\frac{s^2}{2}A_m(p).
}
\]

In particular, if

\[
\boxed{
e+\frac{s^2}{2}A_m(p)<h,
}
\]

then \(F_r(D)\) meets at least \(s\) target cosets.

### Proof

RI2b gives

\[
|\mathcal P_r(D)|\ge(s-k)h-e.
\]

Combine this with RI2d and rearrange. Under the strict second
hypothesis, \(s-k<1\); it is an integer, so \(k\ge s\). \(\square\)

Since

\[
\frac{A_m(p)}h
=
\frac{p-3}{m(p-1)}
+\frac{3(m^2-1)\sqrt p}{m(p-1)}
=
\frac1m+O\!\left(\frac{m}{\sqrt p}\right),
\]

RI2e is effective well beyond the full-coverage range
\(m=O(p^{1/4})\). For fixed \(s\) and \(m=o(\sqrt p)\), its loss from
\(s\) target cosets tends to zero, apart from the explicitly deleted
points. What remains for RI2 is the genuinely high-index regime or the
classification of cases where the cross-coset cap is saturated.

`scripts/verify_rational_cross_collision.py` exhaustively checks every
ordered coset pair and every union of at most three source cosets through
prime \(31\), using squared integer forms of the Weil inequalities.
