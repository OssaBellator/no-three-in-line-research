# Exact fibre energy for dense coset subsets

The collision involution from RI0 converts cardinality nonexpansion under
\(F_r\) into an exact count of points paired by one Möbius involution.  This
is the first structural reduction needed for the corrected RI1.

Use

\[
D_r=\mathbb F_p^\times\setminus\{1,r\},
\qquad
\tau_r(x)=\frac{r(x-1)}{x-r}.
\]

For \(C\subseteq D_r\), let \(\mathcal P_r(C)\) be the set of unordered
two-element orbits

\[
\{x,\tau_r(x)\}
\]

which are entirely contained in \(C\).  Fixed points of \(\tau_r\) are not
included.

## RI1a -- exact image-loss identity

### Theorem RI1a -- PROVED

\[
\boxed{
|F_r(C)|=|C|-|\mathcal P_r(C)|.
}
\]

In particular, if

\[
|F_r(C)|\leq(1-\delta)|C|,
\]

then \(C\) contains at least \(\delta|C|\) disjoint collision pairs and at
least \(2\delta|C|\) elements \(x\) for which
\(\tau_r(x)\in C\setminus\{x\}\).

### Proof

RI0 says the fibres of \(F_r\) on \(D_r\) are exactly the
\(\tau_r\)-orbits.  A one-element intersection of \(C\) with an orbit
contributes one source point and one image point.  A full nonfixed
two-element orbit contributes two source points and one image point, a
loss of exactly one.  Distinct orbits have distinct images.  Summing over
the orbits proves the identity.  The final assertions follow because the
pairs in \(\mathcal P_r(C)\) are disjoint. \(\square\)

The lower bound \(|F_r(C)|\geq|C|/2\) is the immediate extremal case.  More
importantly, every failure of cardinality expansion now supplies linear
mass on one explicit correspondence rather than an unspecified
small-doubling set.

## RI1b -- collision curve inside a subgroup coset

Let \(H\leq\mathbb F_p^\times\) and \(C\subseteq x_0H\cap D_r\).  Write

\[
x=x_0u,\qquad z=x_0v,\qquad u,v\in H.
\]

### Corollary RI1b -- PROVED

Every pair in \(\mathcal P_r(C)\) gives a solution in \(H^2\) of

\[
\boxed{
x_0^2uv-rx_0(u+v)+r=0.
}
\]

Hence the nonexpansion conclusion in RI1a gives at least
\(\delta|C|\) disjoint solutions of this equation with both corresponding
points in \(C\).

### Proof

RI0 gives the collision equation

\[
(x-r)(z-r)=r(r-1).
\]

Expanding it and substituting \(x=x_0u\), \(z=x_0v\) yields

\[
x_0^2uv-rx_0(u+v)+r=0.
\]

Apply RI1a to count the solutions coming from full collision orbits.
\(\square\)

Thus the corrected dense-coset theorem can focus on one concrete question:
bound or classify dense subsets of \(H^2\) on this bilinear curve.  A
character-sum or incidence estimate must either show that the collision
mass is too small, or identify the subgroup/coset configurations on which
the curve has exceptional density.

This reduction does not by itself prove quotient-set expansion for
\(F_r(C)\), and it does not classify the exceptional high-incidence
curves.  Those remain the substantive parts of RI1 and RI3.
