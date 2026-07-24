# Collision involution and necessary corrections to RI1/RI4

Put

\[
F_r(x)=\frac{x(1-x)}{r-x},
\qquad
r\in\mathbb F_p^\times\setminus\{1\}.
\]

Because quotient sets are used later, the natural nonzero domain is

\[
D_r=\mathbb F_p^\times\setminus\{1,r\}.
\]

On this domain \(F_r\) is defined and nonzero.

## RI0 -- exact fibres of \(F_r\)

### Theorem RI0 -- PROVED

For \(x,z\ne r\),

\[
F_r(x)-F_r(z)
=
\frac{(x-z)\bigl(r-r(x+z)+xz\bigr)}
{(r-x)(r-z)}.
\]

Consequently

\[
F_r(x)=F_r(z)
\iff
x=z
\quad\hbox{or}\quad
(x-r)(z-r)=r(r-1).
\]

Define

\[
\tau_r(x)=\frac{r(x-1)}{x-r}.
\]

Then \(\tau_r\) is an involution of \(D_r\), every fibre of \(F_r\) on
\(D_r\) is one \(\tau_r\)-orbit, and

\[
\boxed{|F_r(C)|\geq \left\lceil\frac{|C|}{2}\right\rceil}
\]

for every \(C\subseteq D_r\).

### Proof

Cross multiplication gives

\[
\begin{aligned}
&x(1-x)(r-z)-z(1-z)(r-x)\\
&\qquad=(x-z)\bigl(r-r(x+z)+xz\bigr),
\end{aligned}
\]

which proves the first two formulas. Solving the second factor for \(z\)
gives

\[
z=r+\frac{r(r-1)}{x-r}
=\frac{r(x-1)}{x-r}.
\]

The symmetric equation
\((x-r)(z-r)=r(r-1)\) shows directly that applying \(\tau_r\) twice returns
\(x\). For \(r\ne0,1\), the values \(0,1,r\) have no preimage under
\(\tau_r\) from \(D_r\), so \(D_r\) is invariant. Thus each fibre has one
or two elements, which proves the cardinality bound. \(\square\)

RI0 is sharp as a general set theorem: selecting both points from many
two-element \(\tau_r\)-orbits gives image size exactly half the source size.
Any stronger expansion theorem must therefore use the multiplicative-coset
geometry, not only the degree of \(F_r\).

## RI1 is false when the full subgroup is allowed

### Proposition RI1-obstruction -- PROVED

The stated RI1 alternative is false for \(H=\mathbb F_p^\times\).

### Proof

Fix \(0<\epsilon<1/2\), take \(H=\mathbb F_p^\times\), and let

\[
C=D_r=H\setminus\{1,r\}.
\]

For all sufficiently large \(p\),

\[
|C|=p-3>(1/2+\epsilon)(p-1).
\]

The nonzero set \(F_r(C)\) meets only the unique \(H\)-coset and has at most
\(|H|\) points. It therefore cannot contain
\((1+c_\epsilon)|H|\) points and cannot meet two \(H\)-cosets. The group
does not have order two, and \(|C|\) is unbounded, so neither of the other
alternatives applies. \(\square\)

The corrected RI1 hypothesis must require a **proper** subgroup, for
example

\[
2\leq |H|\leq (p-1)/2,
\]

and must state explicitly that \(C\subseteq D_r\). The same domain
restriction is required in RI2--RI3; otherwise a full source coset can
contain the pole \(r\) or the zero \(1\).

## RI4 is false for sets merely covered by order-two cosets

### Proposition RI4-obstruction -- PROVED

There are arbitrarily long nonperiodic chains of singleton sets

\[
C_{i+1}=F_{r_i}(C_i)
\]

such that every \(C_i\) is covered by an order-two subgroup coset and no
quotient-set growth occurs.

### Proof

Choose any sequence of distinct nonzero elements
\(c_0,c_1,\ldots,c_s\), none equal to \(1\), with
\(c_{i+1}\ne c_i-1\). Put

\[
C_i=\{c_i\},
\qquad
r_i=c_i+\frac{c_i(1-c_i)}{c_{i+1}}.
\]

Then \(r_i\ne c_i\), and direct substitution gives

\[
F_{r_i}(c_i)=c_{i+1}.
\]

The condition \(c_{i+1}\ne c_i-1\) gives \(r_i\ne0\), while distinctness
gives \(r_i\ne1\). Each singleton is contained in the order-two coset
\(c_i\{1,-1\}\), and both its quotient set and its image quotient set have
size one. The chain is nonperiodic because the \(c_i\) are distinct.
Taking a larger prime permits arbitrarily large \(s\). \(\square\)

RI4 must consequently require full order-two cosets, or a quantitative
density in each covering coset, and must specify how mass lost when a pair
collapses is charged. A bare coset-cover conclusion cannot imply bounded
periodicity.

## What remains

The corrected inverse problem is now:

- RI1 for proper nontrivial \(H\) and \(C\subseteq D_r\);
- RI2 with poles and zeros deleted or isolated explicitly;
- RI3 with the same domain convention;
- RI4 for full or quantitatively dense order-two cosets, including a mass
  condition that rules out singleton chains;
- conversion of the resulting finite configurations to the RI5 absorber
  interface.

`scripts/verify_rational_inverse.py` exhaustively checks RI0 on small
primes and preserves the two counterexamples as regressions.
