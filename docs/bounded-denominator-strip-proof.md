# Exact \(q\)-strip decomposition

This note proves BDA1 for the perfect-alignment chambers supplied by PA2.
It also gives a canonical \(q^2\)-class decomposition for arbitrary wrap
residues, which is useful when a translated chamber is normalized before
calling the absorber.

Throughout, representatives lie in \(\{1,\ldots,p-1\}\).  For
\(m\in\{1,\ldots,p-1\}\) and \(0\leq k<m\), define

\[
I_{m,k}
=
\left\{z\in\{1,\ldots,p-1\}:
 k=\left\lfloor\frac{mz}{p}\right\rfloor\right\}.
\]

## BDA1a -- exact arithmetic strips

### Lemma BDA1a -- PROVED

Each carry cell is the integer interval

\[
I_{m,k}
=
\left[
\left\lceil\frac{kp}{m}\right\rceil,
\left\lceil\frac{(k+1)p}{m}\right\rceil-1
\right]\cap\{1,\ldots,p-1\}.
\]

For a fixed \(q\geq2\) and residue \(r\in\mathbb Z/q\mathbb Z\), put

\[
S_{m,r}^{(q)}
=
\bigcup_{\substack{0\leq k<m\\k\equiv r\pmod q}} I_{m,k}.
\]

Then the \(q\) sets \(S_{m,r}^{(q)}\) form a canonical partition of the
nonzero coordinate representatives.

### Proof

The equation \(\lfloor mz/p\rfloor=k\) is equivalent to

\[
kp\leq mz<(k+1)p.
\]

Taking the least and greatest integral solutions gives the displayed
interval.  Every carry \(k\in\{0,\ldots,m-1\}\) has one residue modulo
\(q\), so grouping the disjoint carry intervals by that residue gives the
partition. \(\square\)

## BDA1b -- chamber decomposition on a hyperbola layer

Fix \(a\in\mathbb F_p^\times\), a scalar \(g\), and its representative
inverse \(h=\langle g^{-1}\rangle_p\).  On

\[
H_a=\{(x,y):xy\equiv a\pmod p\},
\]

define

\[
\mathcal C_{r,s}
=
H_a\cap
\left(S_{g,r}^{(q)}\times S_{h,s}^{(q)}\right).
\]

### Theorem BDA1b -- PROVED

The sets \(\mathcal C_{r,s}\), \(r,s\in\mathbb Z/q\mathbb Z\), have the
following properties.

1. They canonically partition \(H_a\) into at most \(q^2=O_q(1)\) classes.
2. In \(\mathcal C_{r,s}\), the source and target wrap indices have the
   fixed residues \(r,s\).
3. Every class is the intersection of a permutation layer with explicit
   unions of arithmetic intervals.
4. Every row and column occurs at most once in every class.
5. Reversing the scalar relation exchanges \(g,h\) and \(r,s\).  In
   particular, \(\mathcal C_{0,0}\) is canonical under the red--blue
   channel swap.
6. Deleting any set of exceptional points merely deletes those points from
   the same classes; no class labels change.

### Proof

Items 1--3 follow from BDA1a applied independently to the two coordinates.
The map \(x\mapsto\langle a/x\rangle_p\) is a bijection, so \(H_a\) is a
perfect matching between its row and column sets; item 4 is inherited by
every subset.  Source--target reversal swaps the two inverse scalar carry
coordinates, proving item 5.  The labels are pointwise arithmetic
functions, so item 6 is immediate. \(\square\)

## BDA1c -- the finite interpolation list

Use the notation of PA1--PA2.  Thus \(d\mid g-1\), \(d\mid h-1\), an
interior parameter is \(0<t<d\), and

\[
\frac td=\frac{t'}q,\qquad \gcd(t',q)=1.
\]

For \(U=(x,y)\), put

\[
V=(\langle gx\rangle_p,\langle hy\rangle_p),\quad
A=\left\lfloor\frac{gx}{p}\right\rfloor,\quad
B=\left\lfloor\frac{hy}{p}\right\rfloor.
\]

### Theorem BDA1c -- PROVED

The perfect chamber is exactly

\[
\mathcal P_{a,g,t}=\mathcal C_{0,0}.
\]

On this chamber the aligned point is given by the single rational pattern

\[
\begin{aligned}
W_x&=x+\frac{t'}q(V_x-x),\\
W_y&=V_y+\frac{t'}q(y-V_y).
\end{aligned}
\]

Across all reduced parameters with denominator \(q\), there are only
\(\varphi(q)=O_q(1)\) such patterns.

### Proof

PA2 says perfect alignment is equivalent to \(q\mid A\) and \(q\mid B\),
which is precisely membership in \(\mathcal C_{0,0}\).

Write

\[
\lambda=1+\frac td(g-1).
\]

Since \(V_x=gx-pA\),

\[
x+\frac td(V_x-x)
=
\lambda x-p\frac{tA}{d}.
\]

This is integral exactly when \(d\mid tA\), equivalently \(q\mid A\).
When integral it is a convex combination of two representatives and is
congruent to \(\lambda x\), so it equals
\(\langle\lambda x\rangle_p\).

Similarly, with

\[
m=h-\frac td(h-1)
\]

and \(V_y=hy-pB\),

\[
V_y+\frac td(y-V_y)
=
my-p\frac{(d-t)B}{d}.
\]

Because \(\gcd(d-t,d)=\gcd(t,d)\), this is integral exactly when
\(q\mid B\), and then equals \(\langle my\rangle_p\).  Reduced numerators
are precisely the units \(t'\) modulo \(q\), of which there are
\(\varphi(q)\). \(\square\)

Together BDA1a--BDA1c prove all five bullets in BDA1 for the PA2 input.
They do not supply a decreasing local trade; that starts at BDA2.
