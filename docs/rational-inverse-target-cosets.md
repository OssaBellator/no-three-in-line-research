# Target-coset equidistribution for the rational inverse map

RI1d bounds collision partners which remain in the source coset. The same
four-point character argument counts how the entire source coset is
distributed among target \(H\)-cosets.

Let \(H\leq\mathbb F_p^\times\) have index \(m\). For source and target
coset representatives \(x_0,y_0\), define

\[
N(x_0H,y_0H)=
\left|\left\{
x\in x_0H\setminus\{1,r\}:
F_r(x)\in y_0H
\right\}\right|.
\]

## RI1e -- target-coset equidistribution

### Theorem RI1e -- PROVED

For every \(r\neq0,1\),

\[
\boxed{
\left|
N(x_0H,y_0H)-\frac{p-3}{m^2}
\right|
\leq
3\left(1-\frac1{m^2}\right)\sqrt p
<3\sqrt p.
}
\]

Put

\[
A_m(p)=
\frac{p-3}{m^2}
+3\left(1-\frac1{m^2}\right)\sqrt p.
\]

Then every subset

\[
C\subseteq x_0H\setminus\{1,r\}
\]

satisfies

\[
\boxed{
N_H(F_r(C))\geq\frac{|C|}{A_m(p)},
}
\]

where \(N_H\) counts the target \(H\)-cosets met by the image.

If \(m\geq 2\) and \(|C|>A_m(p)\), the image meets at least two target
cosets. Moreover,
two target cosets contain respectively at least

\[
\boxed{
\frac{|C|}{2m}
\quad\text{and}\quad
\frac{|C|-A_m(p)}{2(m-1)}
}
\]

distinct values of \(F_r(C)\).

### Proof

Write \(x=x_0u\). Choose a character \(\chi\) of exact order \(m\) with
kernel \(H\). Orthogonality gives

\[
N(x_0H,y_0H)
=
\frac1{m^2}
\sum_{a,b=0}^{m-1}
\sum_u
\chi^a(u)
\chi^b\!\left(F_r(x_0u)/y_0\right)
\]

over the admissible values
\(u\in\mathbb F_p^\times\setminus\{x_0^{-1},rx_0^{-1}\}\).
Up to a constant character factor, the \((a,b)\)-summand is the character
of

\[
u^{a+b}(1-x_0u)^b(r-x_0u)^{-b}.
\]

Multiply inside the character by the polynomial \(m\)-th-power mask

\[
\left(u(1-x_0u)(r-x_0u)\right)^m.
\]

This leaves every admissible term unchanged and makes the excluded values
zero. The resulting polynomial has divisor orders congruent modulo \(m\)
at

\[
0,\quad x_0^{-1},\quad rx_0^{-1},\quad\infty
\]

are congruent modulo \(m\) to

\[
a+b,\quad b,\quad-b,\quad-(a+b).
\]

All are divisible by \(m\) only for \((a,b)=(0,0)\). The principal term
contributes \(p-3\); each of the other \(m^2-1\) terms has four divisor
points and absolute value at most \(3\sqrt p\) by the standard Weil
character bound. Division by \(m^2\) proves the first display.

Every target coset has at most \(A_m(p)\) preimages in the full source
coset. If \(F_r(C)\) meets \(k\) target cosets, then

\[
|C|\leq kA_m(p),
\]

which proves the coset-count bound.

For the density statement, partition \(C\) by target coset. Its largest
part has at least \(|C|/m\) source points. No part has more than
\(A_m(p)\), so the points outside a largest part have total at least
\(|C|-A_m(p)\); one of the other \(m-1\) parts has at least their average.
Every fibre of \(F_r\) has size at most two by RI0, so the corresponding
numbers of distinct image values are at least half those source counts.
\(\square\)

## Consequences

If

\[
\frac{p-3}{m^2}
>
3\left(1-\frac1{m^2}\right)\sqrt p,
\]

the image of a full source coset meets every target \(H\)-coset, with at
least half the lower-bound preimage count in distinct values.

For fixed proper index \(m\) and
\(|C|>(1/2+\epsilon)|H|\), the condition \(|C|>A_m(p)\) holds for all
sufficiently large \(p\). RI1e then gives two target cosets with explicit
positive densities depending on \(\epsilon\) and \(m\). Thus the
corrected RI1 target-coset alternative is proved for every fixed subgroup
index. Uniformity when \(m\) grows with \(p\), and conversion of the
resulting many-coset image to RI3--RI5 absorbers, remain open.

## RI2a -- full coverage in the small-index regime

### Corollary RI2a -- PROVED

If

\[
\boxed{
p-3>3(m^2-1)\sqrt p,
}
\]

then for every source coset \(x_0H\) and every target coset \(y_0H\),

\[
N(x_0H,y_0H)>0.
\]

Consequently, if \(C\) is any nonempty union of full \(H\)-cosets, then

\[
\boxed{
N_H\!\left(F_r(C\setminus\{1,r\})\right)=m.
}
\]

Thus RI2 is complete with maximal target-coset coverage throughout this
small-index range, which includes every fixed \(m\) for sufficiently
large \(p\) and, asymptotically, indices
\(m<(1/\sqrt3-o(1))p^{1/4}\).

### Proof

The RI1e lower bound is

\[
N(x_0H,y_0H)
\geq
\frac{p-3-3(m^2-1)\sqrt p}{m^2},
\]

which is positive under the displayed hypothesis. Hence one full source
coset already has image in every one of the \(m\) target cosets. A
nonempty union contains such a source coset, and adding further source
points cannot remove image cosets. \(\square\)

The unresolved RI2 range begins when \(m\) is comparable to or larger
than \(p^{1/4}\), where the individual character-sum error can dominate
the main term and correlations among several source cosets must be used.

`scripts/verify_rational_target_cosets.py` exhaustively checks every
source/target coset count, the squared Weil inequality, and the RI2a
positivity implication through prime \(43\).
