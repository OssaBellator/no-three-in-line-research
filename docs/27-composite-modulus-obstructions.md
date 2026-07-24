# Composite-modulus affine hosts: exact progress and obstructions

This chapter records rigorous progress on `tracks/all-n-composite-modulus.md`.
It deliberately separates the easy saturation problem from the difficult
real-collinearity problem.

Throughout, \([z]_N\) denotes the standard representative of \(z\bmod N\) in
\(\{0,\ldots,N-1\}\), and all Euclidean statements concern these standard
integer lifts.

## 1. Affine channels saturate every modulus

For \(m,c\in\mathbb Z_N\), define

\[
A_{m,c}(N)=\{(x,[mx+c]_N):0\le x<N\}.
\]

### Theorem CMA1 — PROVED

Let \(N\ge2\), let \(m\in\mathbb Z_N^\times\), and let
\(c_0\ne c_1\pmod N\). Then

\[
A_{m,c_0}(N)\cup A_{m,c_1}(N)
\]

contains exactly two distinct points in every row and every column.

In particular, this construction uses every residue class, including all
nonunit rows and columns.

### Proof

Each map \(x\mapsto mx+c_i\) is a permutation of \(\mathbb Z_N\), so each
channel contains one point in every row and every column. At a fixed column
\(x\), the two row values differ by \(c_1-c_0\ne0\). At a fixed row \(y\), the
two preimages are

\[
m^{-1}(y-c_0),\qquad m^{-1}(y-c_1),
\]

and they are distinct for the same reason. ∎

This completes the saturation portion of CM1. It does **not** produce a
no-three channel.

## 2. Exact carry criterion for an affine lift

Choose integer representatives

\[
1\le m\le N-1,\qquad 0\le c<N,
\]

and write

\[
y_x=[mx+c]_N=mx+c-Nk_x,
\qquad
k_x=\left\lfloor\frac{mx+c}{N}\right\rfloor.
\]

For three points \(P_i=(x_i,y_{x_i})\), define the oriented area

\[
\Delta(P_1,P_2,P_3)
=
(x_2-x_1)(y_{x_3}-y_{x_1})
-
(x_3-x_1)(y_{x_2}-y_{x_1}).
\]

### Theorem CMA2 — PROVED

For every three column indices \(x_1,x_2,x_3\),

\[
\Delta(P_1,P_2,P_3)
=
-N\Bigl(
(x_2-x_1)(k_{x_3}-k_{x_1})
-
(x_3-x_1)(k_{x_2}-k_{x_1})
\Bigr).
\]

Consequently, three lifted affine-channel points are real collinear if and
only if the three carry-graph points

\[
(x_i,k_{x_i})
\]

are real collinear.

### Proof

Substitute \(y_x=mx+c-Nk_x\) into the determinant. The contribution of
\(mx+c\) cancels because it is affine in \(x\), leaving exactly the displayed
multiple of the carry determinant. ∎

This is a complete real-lift criterion, not merely a modular incidence test.

## 3. Universal affine obstruction

The preceding criterion can be sharpened to a complete negative result.

### Theorem CMA3 — PROVED

For every \(N\ge5\), every \(1\le m\le N-1\), and every \(c\), the standard
lift of \(A_{m,c}(N)\) contains a real collinear triple.

Thus no affine modular permutation channel can satisfy CM2 once \(N\ge5\).

### Proof

Let

\[
d_x=y_{x+1}-y_x
\qquad(0\le x\le N-2).
\]

Adding \(m\) wraps at most once, so every \(d_x\) is one of the two values

\[
m,\qquad m-N.
\]

If \(d_x=d_{x+1}\) for some \(x\), then the three consecutive points at
columns \(x,x+1,x+2\) have equal successive displacement vectors and are
collinear.

Otherwise every adjacent pair of differences is unequal. Since only two
values are available, the sequence \(d_x\) alternates. Hence

\[
y_{x+2}-y_x=d_x+d_{x+1}=2m-N
\]

for every possible \(x\). In particular, the points at columns \(0,2,4\) are
collinear. ∎

The obstruction is stronger than a failed parameter search: it eliminates
the entire affine-permutation family.

## 4. Exact alternating-cycle structure

Although affine channels fail geometrically, their row-column graph is fully
tractable.

### Theorem CMA4 — PROVED

Let \(m\in\mathbb Z_N^\times\), \(c_0\ne c_1\), and put

\[
t=m^{-1}(c_0-c_1)\pmod N.
\]

The bipartite row-column graph of
\(A_{m,c_0}(N)\cup A_{m,c_1}(N)\) is a disjoint union of

\[
g=\gcd(t,N)=\gcd(c_0-c_1,N)
\]

alternating cycles, each of length

\[
\frac{2N}{g}.
\]

In particular, when \(c_1-c_0\) is a unit, the union is one alternating
Hamiltonian cycle of length \(2N\).

### Proof

Start at column \(x\), traverse the \(c_0\)-edge to row \(mx+c_0\), then
traverse the \(c_1\)-edge backward to the unique column

\[
x'=m^{-1}(mx+c_0-c_1)=x+t.
\]

Thus two graph edges implement translation by \(t\) on \(\mathbb Z_N\).
Translation by \(t\) has \(g\) orbits of size \(N/g\), giving the claimed
cycle decomposition. ∎

This completes the alternating-cycle bullet of CM3 for affine pairs.

## 5. Affine displacement multiplicity is necessarily large

### Theorem CMA5 — PROVED

Let \(m\) be a unit and write

\[
c_1-c_0\equiv\delta\pmod N,
\qquad 1\le\delta\le N-1.
\]

Among the \(N\) corresponding-column pairs

\[
(x,[mx+c_0]_N),\qquad (x,[mx+c_1]_N),
\]

the real displacement is either

\[
(0,\delta)
\quad\text{or}\quad
(0,\delta-N).
\]

These occur with multiplicities \(N-\delta\) and \(\delta\), respectively.
Therefore one displacement occurs at least \(\lceil N/2\rceil\) times.

### Proof

The first channel visits every row \(r\) exactly once. Replacing \(r\) by
\([r+\delta]_N\) changes the lifted row by \(\delta\) for
\(0\le r<N-\delta\), and by \(\delta-N\) for \(N-\delta\le r<N\). ∎

Hence affine pairs fail the bounded-displacement requirement in CM3 by a
linear factor.

## 6. Unit hyperbolas do not saturate composite grids

For a unit \(c\), define the unit hyperbola

\[
H_c^\times(N)
=
\{(x,[cx^{-1}]_N):x\in\mathbb Z_N^\times\}.
\]

### Proposition CMH1 — PROVED

The channel \(H_c^\times(N)\) occupies exactly the unit rows and unit columns.
It has \(\varphi(N)\) points and omits exactly \(N-\varphi(N)\) rows and the
same number of columns.

A union of any number of such unit-hyperbola channels still omits every
nonunit row and column.

### Proof

Multiplication by the unit \(c\) and inversion both permute
\(\mathbb Z_N^\times\), and neither operation produces a nonunit. ∎

This resolves the nonunit-coverage counterexample required by the track.

## 7. Squarefree hyperbola line collapse

The prime-field conic line cap fails immediately for squarefree composite
moduli.

### Theorem CMH2 — PROVED

Let \(N\) be odd and squarefree with \(r=\omega(N)\) distinct prime factors.
Then \(H_1^\times(N)\) contains exactly \(2^r\) points on the real diagonal
\(y=x\).

### Proof

A diagonal point belongs to \(H_1^\times(N)\) exactly when

\[
x^2\equiv1\pmod N.
\]

For each odd prime \(p\mid N\), there are exactly two choices
\(x\equiv\pm1\pmod p\). The Chinese remainder theorem gives exactly \(2^r\)
solutions modulo \(N\). Their standard lifts are the points \((x,x)\), all on
the real line \(y=x\). ∎

For example, modulo \(15\), the four points

\[
(1,1),\ (4,4),\ (11,11),\ (14,14)
\]

lie in \(H_1^\times(15)\).

## 8. Prime-power anti-diagonal collapse

Repeated prime factors create an even larger Hensel-multiplicity obstruction.

### Theorem CMH3 — PROVED

Let \(N=p^k\), where \(p\) is odd and \(k\ge2\). Set

\[
a=\frac{N-1}{2},
\qquad
c\equiv a^2\pmod N.
\]

Then \(H_c^\times(N)\) contains

\[
p^{\lfloor k/2\rfloor}
\]

points on the real anti-diagonal

\[
x+y=N-1.
\]

### Proof

Let

\[
q=p^{\lceil k/2\rceil}.
\]

There are \(N/q=p^{\lfloor k/2\rfloor}\) residues satisfying
\(x\equiv a\pmod q\). Each is a unit because \(a\not\equiv0\pmod p\). Put
\(y=N-1-x=2a-x\). Then

\[
xy=x(2a-x)=a^2-(x-a)^2\equiv a^2\equiv c\pmod N,
\]

because \(q^2\) is divisible by \(p^k\). Thus every \((x,y)\) lies in
\(H_c^\times(N)\), and all lie on the stated real line. ∎

For \(N=9\), this gives the three collinear points

\[
(1,7),\ (4,4),\ (7,1)
\]

in \(H_7^\times(9)\).

### Proposition CMH4 — PROVED

For \(N=2^k\) with \(k\ge3\), \(H_1^\times(N)\) contains four points on
\(y=x\).

### Proof

The congruence \(x^2\equiv1\pmod{2^k}\) has the four standard solutions

\[
1,\quad -1,\quad 1+2^{k-1},\quad -1+2^{k-1}.
\]

Each produces a diagonal hyperbola point. ∎

Together, CMH2–CMH4 supply explicit quadratic-congruence and line-collapse
counterexamples for the natural composite hyperbola route.

## 9. Zero-divisor line equations cannot be cancelled

### Proposition CMZ1 — PROVED

Over \(\mathbb Z_6\), the equation

\[
2(y-x)\equiv0\pmod6
\]

is not equivalent to \(y-x\equiv0\pmod6\). Instead it is the union of the two
primitive diagonal fibres

\[
y-x\equiv0\pmod6,
\qquad
y-x\equiv3\pmod6.
\]

### Proof

The displayed equation is equivalent to \(y-x\equiv0\pmod3\), which has the
two stated residue classes modulo \(6\). ∎

Thus multiplying a line equation by a zero divisor can merge distinct
toroidal lines. Any ring-line formalism must normalize primitive integer
coefficients before reduction.

## 10. Real and modular collinearity: the correct implication

### Theorem CML1 — PROVED

Every real collinear triple of standard grid points is collinear modulo \(N\).
Equivalently, if \(d=(u,v)\) is the primitive integer direction of the real
line, then all three points have the same toroidal line coordinate

\[
\lambda_d(x,y)=vx-uy\pmod N.
\]

### Proof

The integer \(vx-uy\) is constant on the real line, hence remains constant
after reduction modulo \(N\). ∎

Therefore a **genuine** toroidal no-three set, meaning one that protects every
primitive direction fibre, cannot acquire a real collinear triple under
standard lifting. The corresponding “mandatory counterexample” in the track
does not exist under this definition.

The converse is false.

### Proposition CML2 — PROVED

For every odd \(N\ge3\), the points

\[
(0,0),\quad (1,2),\quad \left(\frac{N+1}{2},1\right)
\]

have determinant \(-N\). They are collinear modulo \(N\) but not over the
reals.

For every even \(N\ge4\), the points

\[
(0,0),\quad (0,2),\quad \left(\frac N2,0\right)
\]

also have determinant \(-N\).

This is the correct lift warning: modular incidence can be a false positive,
but never a false negative for real collinearity.

### Lemma CML3 — PROVED

If a triple has modular determinant \(0\pmod N\) and its integer determinant
satisfies

\[
|\Delta|<N,
\]

then it is real collinear.

### Proof

The only multiple of \(N\) strictly between \(-N\) and \(N\) is zero. ∎

Any successful CRT lifting theorem may use this lemma by forcing a sufficiently
small determinant representative.

## 11. Naive CRT product channels have mixed-projection triples

Let \(u,v>1\) be coprime, \(N=uv\), and let

\[
f_u:\mathbb Z_u\to\mathbb Z_u,
\qquad
f_v:\mathbb Z_v\to\mathbb Z_v.
\]

Define the coordinatewise CRT function \(f_N\) by

\[
f_N(x)\equiv f_u(x\bmod u)\pmod u,
\qquad
f_N(x)\equiv f_v(x\bmod v)\pmod v.
\]

When the local maps are permutations, \(f_N\) is a permutation, so global
row/column repetition is not the issue.

### Theorem CMCRT1 — PROVED

For the three distinct global points

\[
P_0=(0,f_N(0)),
\qquad
P_u=(u,f_N(u)),
\qquad
P_v=(v,f_N(v)),
\]

their integer determinant is divisible by \(N\).

More precisely, \(P_0\) and \(P_u\) have the same projection modulo \(u\),
while \(P_0\) and \(P_v\) have the same projection modulo \(v\).

### Proof

Modulo \(u\), both \(0\) and \(u\) have local column \(0\), so the definition
of \(f_N\) gives identical local rows. Hence the determinant is \(0\pmod u\).
Likewise, modulo \(v\), the points \(P_0\) and \(P_v\) coincide, so the
determinant is \(0\pmod v\). Coprimality gives divisibility by \(uv=N\). ∎

This does not by itself prove that the three lifted points are real collinear.
It proves that a local argument of the form “one factor sees three distinct
arc points” cannot handle all global triples. A CRT assembly theorem needs a
mixed-collision signature or a determinant-size argument.

## 12. Consequences for the track

The completed pieces are:

- CM1 saturation for every modulus via two affine permutation channels;
- the exact row-column cycle decomposition for those channels;
- an exact real carry criterion for affine lifts;
- a proof that every affine channel fails CM2 for \(N\ge5\);
- a proof that affine pairs have linear displacement multiplicity;
- explicit squarefree, odd-prime-power, and \(2\)-power hyperbola line
  collapses;
- exact nonunit-coverage and zero-divisor counterexamples;
- the correct real-to-modular lifting implication;
- the mixed-projection obstruction to naive CRT product proofs.

The remaining positive tasks are still substantial:

1. find a nonlinear full permutation channel over a broad composite class with
   a genuine real line cap;
2. obtain bounded displacement multiplicity and a repairable syndrome for a
   two-channel pair;
3. develop carry signatures that include nonunit strata at prime powers;
4. overcome mixed local-projection triples in CRT assembly;
5. prove enough modulus coverage for CM6.

The computational companion is
`scripts/verify_composite_modulus.py`.
