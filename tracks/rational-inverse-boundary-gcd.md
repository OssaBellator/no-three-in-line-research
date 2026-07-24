# Polynomial gcd certificate for rational quotient boundary

RI2f turns collision saturation into the boundary

\[
B(D)=|\{x\in D:\tau_r(x)\notin D\}|
\]

of a set \(D\subseteq D_r\) under the rational involution.  That
boundary has an exact algebraic certificate: it is the degree defect of
a polynomial and its Möbius transform.

For finite \(D\subseteq D_r\), put \(n=|D|\) and

\[
P_D(X)=\prod_{c\in D}(X-c).
\]

Clear the denominator after applying \(\tau_r\):

\[
\begin{aligned}
P_D^\tau(X)
&=(X-r)^nP_D\!\left(\frac{r(X-1)}{X-r}\right)\\
&=\prod_{c\in D}
\bigl((r-c)X+r(c-1)\bigr).
\end{aligned}
\]

Both polynomials have degree \(n\), since \(r\notin D\).

## RI2g -- boundary/gcd identity

### Theorem RI2g -- PROVED

For every \(D\subseteq D_r\),

\[
\boxed{
\deg\gcd(P_D,P_D^\tau)=n-B(D).
}
\]

In particular,

\[
\boxed{
B(D)=0
\quad\Longleftrightarrow\quad
P_D^\tau(X)
=
\left(\prod_{c\in D}(r-c)\right)P_D(X).
}
\]

More generally, a boundary of size at most \(L\) is equivalent to
\(P_D\) and \(P_D^\tau\) sharing a factor of degree at least \(n-L\).

### Proof

Every root of \(P_D\) is simple and lies in \(D_r\).  For \(x\ne r\),

\[
P_D^\tau(x)=0
\quad\Longleftrightarrow\quad
\tau_r(x)\in D.
\]

The cleared polynomial does not acquire \(r\) as a root, because every
linear factor takes the nonzero value \(r(r-1)\) at \(X=r\).
Consequently the common roots are exactly

\[
\{x\in D:\tau_r(x)\in D\},
\]

whose size is \(n-B(D)\).  All transformed roots are simple because
\(\tau_r\) is an involution of \(D_r\).  This proves the gcd-degree
identity.

If \(B(D)=0\), the two degree-\(n\) polynomials have the same roots and
are proportional.  The leading coefficient of \(P_D^\tau\) is
\(\prod_{c\in D}(r-c)\), while \(P_D\) is monic, giving the displayed
functional equation.  Its converse is immediate. \(\square\)

## Coset-union form

If

\[
C=\bigcup_{i\in S}x_iH,
\qquad |H|=h,
\]

then

\[
\boxed{
P_C(X)=\prod_{i\in S}(X^h-x_i^h).
}
\]

For the punctured domain \(D=C\setminus\{1,r\}\), \(P_D\) is obtained
from this sparse coset polynomial by deleting the present factors
\((X-1)\) and \((X-r)\).  RI2g therefore converts a low-boundary
quotient cut into a high-degree common factor between an explicit sparse
coset polynomial and its Möbius transform.

This is the algebraic classification interface missing after RI2f:
zero-boundary exceptional chains satisfy an exact functional equation,
while boundary \(L\) gives a degree-\(n-L\) approximate divisibility
statement.  RI3 may now attack coefficient rigidity or sparse-polynomial
gcd structure rather than an unlabelled quotient graph.  The theorem
does not itself bound the degree of that gcd.

`scripts/verify_rational_boundary_gcd.py` exhaustively checks the
boundary degree, zero-boundary functional equation, and sparse
coset-polynomial identity through small primes.
