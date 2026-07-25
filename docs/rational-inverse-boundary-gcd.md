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

## RI2h -- maximal invariant gcd core

Define

\[
K(D)
=
\{x\in D:\tau_r(x)\in D\}
=
D\cap\tau_r(D).
\]

### Theorem RI2h -- PROVED

The set \(K(D)\) is the unique largest \(\tau_r\)-invariant subset of
\(D\), and

\[
\boxed{
|D\setminus K(D)|=B(D),
\qquad
P_{K(D)}
=
\operatorname{monic}\gcd(P_D,P_D^\tau).
}
\]

In particular, the gcd itself is the root polynomial of the maximal
invariant core and satisfies

\[
\boxed{
P_{K(D)}^\tau
=
\left(\prod_{c\in K(D)}(r-c)\right)P_{K(D)}.
}
\]

Let \(f(K)\) be the number of fixed points of \(\tau_r\) in \(K(D)\).
The rational image decomposes exactly as

\[
\boxed{
F_r(D)
=
F_r(K(D))
\mathbin{\dot\cup}
F_r(D\setminus K(D)),
}
\]

where \(F_r\) is injective on \(D\setminus K(D)\), and hence

\[
\boxed{
|F_r(D)|
=
\frac{|K(D)|+f(K)}2+B(D).
}
\]

### Proof

If \(x\in K(D)\), then \(x,\tau_r(x)\in D\).  Applying the involution
again shows that \(\tau_r(x)\in K(D)\), so the core is invariant.  If
\(J\subseteq D\) is invariant and \(x\in J\), then
\(\tau_r(x)\in J\subseteq D\), whence \(x\in K(D)\).  Thus every
invariant subset lies in \(K(D)\), proving uniqueness and maximality.
The boundary identity follows directly from the definition.

RI2g identifies the roots of the monic gcd as exactly the points
\(x\in D\) whose partners also lie in \(D\).  These are precisely
\(K(D)\), all with multiplicity one, so the polynomial identity follows.
The core has zero boundary, and the displayed functional equation is
the zero-boundary part of RI2g applied to \(K(D)\).

Every fibre of \(F_r\) is a \(\tau_r\)-orbit.  Two distinct boundary
points cannot have the same image, since they would be partners and
would therefore both belong to the core.  Likewise, a boundary point
cannot share an image with a core point.  Thus the two image pieces are
disjoint and the boundary piece has cardinality \(B(D)\).  The invariant
core is a union of two-cycles and \(f(K)\) fixed points, so it has
\((|K(D)|+f(K))/2\) image values.  This proves the last box.
\(\square\)

There is therefore no iterative boundary-pruning cascade.  A
low-boundary quotient component splits in one step into an exact
functional-equation core of size \(|D|-B(D)\) and exactly \(B(D)\)
injective image outliers.  RI3 may classify the maximal core, while an
absorber interface need only pay for the explicitly listed outliers.

## RI2i -- orbit-trace quotient and core factorization

Put

\[
\delta=r(r-1),
\qquad
\sigma_r(x)
=
(x-r)+\frac{\delta}{x-r}.
\]

### Theorem RI2i -- PROVED

For every \(x\in D_r\),

\[
\boxed{
F_r(x)=2r-1+\sigma_r(x),
}
\]

and, for \(x,z\in D_r\),

\[
\boxed{
\sigma_r(x)=\sigma_r(z)
\quad\Longleftrightarrow\quad
z=x\ \text{or}\ z=\tau_r(x).
}
\]

Thus \(\sigma_r\) is an exact coordinate on the
\(\tau_r\)-orbit quotient, and \(F_r\) is its affine translate.

Let \(K\subseteq D_r\) be invariant.  For every nonfixed orbit
\(O=\{x,\tau_r(x)\}\), put \(s_O=\sigma_r(x)\), and let
\(\mathcal O_2(K)\) be the set of its two-element orbits.  Then

\[
\boxed{
P_K(X)
=
\prod_{\substack{x\in K\\\tau_r(x)=x}}(X-x)
\prod_{O\in\mathcal O_2(K)}
\left(
(X-r)^2-s_O(X-r)+\delta
\right).
}
\]

In particular, the image of the invariant core is explicitly

\[
\boxed{
F_r(K)
=
\{\,2r-1+s_O:O\text{ is a }\tau_r\text{-orbit in }K\,\}.
}
\]

### Proof

Write \(y=x-r\).  Since

\[
\tau_r(x)-r=\frac{\delta}{x-r}=\frac\delta y,
\]

the trace is constant on each involution orbit.  Direct expansion gives

\[
F_r(x)
=
\frac{(r+y)(r+y-1)}y
=
2r-1+y+\frac\delta y.
\]

For \(w=z-r\),

\[
y+\frac\delta y=w+\frac\delta w
\]

is equivalent, after multiplying by \(yw\), to

\[
(y-w)(yw-\delta)=0.
\]

Hence \(z=x\) or \(w=\delta/y\), the latter being
\(z=\tau_r(x)\).  This proves the quotient assertions.

On a two-element orbit, the two shifted roots are \(y\) and
\(\delta/y\).  Their monic quadratic is

\[
Y^2-\left(y+\frac\delta y\right)Y+\delta.
\]

Substituting \(Y=X-r\) gives the displayed factor.  Fixed orbits
contribute their linear factors.  Multiplying over the disjoint orbits
proves the polynomial factorization, and the affine trace identity gives
the image formula. \(\square\)

RI2i converts the functional-equation core from RI2h into an explicit
set of orbit-trace parameters.  The unresolved multiplicative rigidity
is now precise: determine when the sparse coset polynomial can factor
into these fixed linear and trace-quadratic orbit factors, or turn the
resulting finite trace bank into an absorber.

## RI2j -- orbit norm and quotient-coset product law

Let \(z=\tau_r(x)\) and \(y=F_r(x)\) for \(x\in D_r\).

### Theorem RI2j -- PROVED

Every rational-inverse orbit obeys the exact sum and norm identities

\[
\boxed{
x+z=y+1,
\qquad
xz=ry.
}
\]

Equivalently, its one- or two-point orbit is the root multiset of

\[
\boxed{
X^2-(y+1)X+ry.
}
\]

Let \(H\leq\mathbb F_p^\times\).  If

\[
x\in \alpha H,
\qquad
z\in\beta H,
\]

then

\[
\boxed{
y\in r^{-1}\alpha\beta H.
}
\]

Consequently, compress any invariant core \(K\) to the following simple
quotient support relation on \(\mathbb F_p^\times/H\): join source
cosets \(A,B\) when one \(\tau_r\)-orbit of \(K\) meets both, and colour
that quotient edge by the target coset containing its common image.
The edge colour is forced to be

\[
\boxed{
\operatorname{col}(A,B)=r^{-1}AB.
}
\]

At a fixed source coset \(A\), one target colour \(C\) determines at
most one neighbouring source coset,

\[
\boxed{
B=rCA^{-1}.
}
\]

Thus if \(F_r(K)\) meets \(k\) target \(H\)-cosets, every source vertex
of the quotient support relation has at most \(k\) distinct neighbours
(with a fixed-orbit loop counted once).

### Proof

The affine trace formula in RI2i gives

\[
y=2r-1+\left((x-r)+(z-r)\right)=x+z-1,
\]

which is the sum identity.  Directly from
\[
z=\frac{r(x-1)}{x-r},
\qquad
y=\frac{x(x-1)}{x-r},
\]
we obtain \(xz=ry\).  Vieta's formula gives the orbit polynomial.

Taking multiplicative \(H\)-cosets in the norm identity yields
\(yH=r^{-1}(xH)(zH)\), proving the product law and the edge-colour
formula.  Solving \(C=r^{-1}AB\) for \(B\) proves uniqueness at a fixed
source vertex.  Only colours met by \(F_r(K)\) can occur, so there are
at most \(k\) distinct neighbours. \(\square\)

RI2j turns the trace factorization into a multiplicative quotient
constraint.  A low-target-coset invariant core is supported on a
bounded-degree coset relation whose colours are not arbitrary: they are
the products of its endpoint cosets divided by \(r\).  The remaining
RI3 rigidity may therefore combine sparse-polynomial structure with
this exact product-coloured quotient graph, while RI5 may treat each
fixed endpoint-coset pair as one absorber channel.

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
statement.  RI2h identifies that common factor exactly with the maximal
invariant core and separates the boundary as injective image outliers.
RI3 may now attack coefficient rigidity or sparse-polynomial gcd
structure rather than an unlabelled quotient graph.  These theorems do
not themselves classify the functional-equation core.

`scripts/verify_rational_boundary_gcd.py` exhaustively checks the
boundary degree, zero-boundary functional equation, and sparse
coset-polynomial identity through small primes.  It also verifies the
maximal invariant core, exact gcd polynomial, and disjoint image
decomposition, together with the affine orbit-trace quotient and
trace-quadratic core factorization.  The same regressions check the
orbit sum/norm law and the product-coloured quotient-coset relation.
