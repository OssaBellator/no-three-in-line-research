# Prime-power completed reciprocals and companion layers

This chapter develops a positive prime-power candidate family for
`tracks/all-n-composite-modulus.md`.  Unlike the unit hyperbola, the channel
below is a permutation of the entire residue ring, including every nonunit
stratum.  Its real-line intersections are not yet bounded by two, but all
large intersections are forced into one explicit Hensel-tangent cell.

Throughout, standard representatives lie in
\(\{0,\ldots,p^k-1\}\).  For a nonzero integer \(z\), write \(v_p(z)\) for
its \(p\)-adic valuation and put \(v_p(0)=\infty\).

## 1. Valuation-completed reciprocal channels

Let \(N=p^k\).  For each \(0\le r<k\), choose a unit

\[
c_r\in (\mathbb Z/p^{k-r}\mathbb Z)^\times.
\]

Define \(R_{\mathbf c}:\mathbb Z_N\to\mathbb Z_N\) by
\(R_{\mathbf c}(0)=0\).  If \(x\ne0\), write

\[
x=p^r u,
\qquad
r=v_p(x),
\qquad
u\in(\mathbb Z/p^{k-r}\mathbb Z)^\times,
\]

and set

\[
R_{\mathbf c}(x)
=
p^r[c_r u^{-1}]_{p^{k-r}}.
\]

Thus each nonzero valuation stratum is inverted internally, rather than being
omitted.

### Theorem CMR1 — PROVED

For every prime power \(N=p^k\), the map \(R_{\mathbf c}\) is a
valuation-preserving involution.  In particular, its graph is a full
permutation channel containing one point in every row and every column.

### Proof

If \(x=p^r u\), then \(c_r u^{-1}\) is a unit modulo \(p^{k-r}\), so
\(R_{\mathbf c}(x)\) has valuation exactly \(r\).  On the same stratum,
applying the map twice replaces \(u\) by

\[
c_r(c_r u^{-1})^{-1}=u
\pmod {p^{k-r}}.
\]

The standard representative is therefore returned exactly.  The point zero
is fixed.  Hence the map is an involution and therefore a permutation. ∎

This gives a nonlinear full channel at every prime power.  It repairs the
nonunit-coverage failure of the ordinary unit hyperbola, but not yet its
line-cap problem.

## 2. Exact stratum equation for a real line

Let

\[
L: Ax+By=C
\]

be a primitive integer line, so \(\gcd(A,B)=1\).  Suppose a nonzero channel
point on \(L\) has valuation \(r\):

\[
x=p^r u,
\qquad
y=p^r v,
\qquad uv\equiv c_r\pmod {p^{k-r}}.
\]

Necessarily \(p^r\mid C\).  Put

\[
m=k-r,
\qquad C_r=C/p^r.
\]

### Theorem CMR2 — PROVED

Every point of valuation \(r\) on \(L\) produces a unit root modulo \(p^m\)
of

\[
Q_r(U)=A U^2-C_rU+B c_r\equiv0\pmod {p^m}.
\]

Consequently, the number of real channel points of valuation \(r\) on \(L\)
is at most the number of unit roots of this quadratic congruence.

### Proof

The exact line equation gives

\[
Au+Bv=C_r.
\]

Multiplying by the unit \(u\), and using \(uv\equiv c_r\pmod{p^m}\), gives

\[
Au^2-C_ru+Bc_r\equiv0\pmod{p^m}.
\]

Distinct standard values of \(x=p^r u\) give distinct residues \(u\) modulo
\(p^m\). ∎

This is the prime-power analogue of the conic intersection equation, but with
an explicit valuation label.

## 3. Only the top valuation stratum can be singular

Assume in this section that \(p\) is odd.  First take \(C\ne0\), and write
\(h=v_p(C)\).

For every \(r<h\), the coefficient \(C_r\) vanishes modulo \(p\).  Therefore

\[
Q_r(U)\equiv AU^2+Bc_r\pmod p.
\]

If \(A\) and \(B\) are both units modulo \(p\), this polynomial has unit
discriminant \(-4ABc_r\), so it has at most two roots and every root is
simple.  If exactly one of \(A,B\) is divisible by \(p\), it has no unit root.

At the top possible stratum \(r=h<k\), put

\[
C_h=C/p^h,
\qquad
m=k-h,
\qquad
\Delta_h=C_h^2-4ABc_h.
\]

### Theorem CMR3 — PROVED

Let \(p\) be odd and let \(L:Ax+By=C\) be primitive.

1. If \(C=0\), then \(L\) contains at most \(2k+1\) points of
   \(R_{\mathbf c}\).  All nonzero points occur with at most two in each
   valuation stratum; the extra point is the origin.
2. If \(C\ne0\) and \(h=v_p(C)\ge k\), then \(L\) contains at most \(2k\)
   channel points.
3. If \(0\le h<k\) and one of \(A,B\) is divisible by \(p\), then \(L\)
   contains at most one channel point.
4. If \(0\le h<k\) and \(A,B\) are units modulo \(p\), then

   \[
   |L\cap R_{\mathbf c}|
   \le 2h+\rho_p(k-h,\Delta_h),
   \]

   where \(\rho_p(m,\Delta)\) is the number of solutions of

   \[
   Z^2\equiv\Delta\pmod {p^m}.
   \]

   More explicitly, with \(\nu=v_p(\Delta)\):

   - if \(\nu\ge m\), then \(\rho_p(m,\Delta)=p^{\lfloor m/2\rfloor}\);
   - if \(\nu<m\) is odd, then \(\rho_p(m,\Delta)=0\);
   - if \(\nu=2t<m\), then \(\rho_p(m,\Delta)\) is either \(0\) or
     \(2p^t\), according as \(\Delta/p^{2t}\) is a nonsquare or square
     modulo \(p\).

In particular,

\[
|L\cap R_{\mathbf c}|
\le
2k+2p^{\lfloor k/2\rfloor}+1
=O(\log N+\sqrt N).
\]

If a line exceeds the simple-root bound \(2h+2\), then every excess point lies
in the single top stratum \(r=h\), and its unit coordinate satisfies

\[
2Au\equiv C_h\pmod p.
\]

Thus every large line is confined to one explicit Hensel-tangent cell.

### Proof

A point of valuation \(r\) requires \(p^r\mid C\), so no stratum above \(h\)
can occur when \(h<k\).  For \(r<h\), the preceding reduction modulo \(p\)
shows that there are at most two simple roots when \(A,B\) are units, and no
unit roots when exactly one is divisible by \(p\).  Simple roots lift uniquely
to every power of \(p\).

At \(r=h\), if one of \(A,B\) is divisible by \(p\), the reduction of
\(Q_h\) is linear with nonzero derivative, so there is at most one lift.
If \(A,B\) are units, completing the square gives the exact equivalence

\[
(2AU-C_h)^2\equiv\Delta_h\pmod {p^m}.
\]

Because \(2A\) is a unit, this change of variable is bijective.  The displayed
formula for \(\rho_p\) is the standard odd-prime square-root count: factor out
the largest even power of \(p\), and use the two simple square roots of a
nonzero quadratic residue modulo \(p\).  When \(\Delta\equiv0\pmod{p^m}\),
the roots are exactly the multiples of \(p^{\lceil m/2\rceil}\).

For \(C=0\), every nonzero stratum is of the simple lower type, and the origin
also lies on the line.  The global coarse bound follows by maximizing the
preceding estimates.  Finally, a singular top root reduces to the unique
double root \(2Au=C_h\pmod p\). ∎

The theorem does not prove a constant line cap.  It replaces an uncontrolled
ring-conic failure by a single, explicitly parameterized tangent cell.

## 4. A universal Hamiltonian companion layer

The second layer can be added without sacrificing saturation or alternating
cycle length.  Let \(N=p^k\), and define

\[
q_p=
\begin{cases}
p,&p\text{ odd},\\
4,&p=2,
\end{cases}
\qquad
\sigma_p(y)=[(1+q_p)y+1]_N.
\]

For \(p=2\), the assertions below also hold at \(N=2\), with the obvious
reduction of \(q_p\) modulo \(N\).

### Theorem CMR4 — PROVED

Let \(f\) be any permutation of \(\mathbb Z_N\), and define

\[
g=\sigma_p\circ f.
\]

Then:

1. the graphs of \(f\) and \(g\) are pointwise disjoint and contain exactly
   two points in every row and column;
2. their row-column bipartite graph is one alternating Hamiltonian cycle of
   length \(2N\);
3. among corresponding-column pairs, every exact lifted vertical displacement
   occurs at most \(p\) times for odd \(p\), and at most \(4\) times for
   \(p=2\).

### Proof

A fixed point of \(\sigma_p\) would satisfy \(q_p y+1\equiv0\pmod p\), which
is impossible.  Thus the two graph points in each column are distinct, and
both layers are permutations.

Traversing an \(f\)-edge from a column to a row and then a \(g\)-edge backward
implements \(f^{-1}\sigma_p^{-1}f\) on columns.  It therefore has the same
cycle structure as \(\sigma_p\).

For odd \(p\),

\[
\sigma_p^t(0)=\frac{(1+p)^t-1}{p},
\]

and the lifting-the-exponent identity gives

\[
v_p((1+p)^t-1)=1+v_p(t).
\]

Hence the first positive return modulo \(p^k\) occurs at \(t=p^k=N\).  For
\(p=2\), the same argument uses

\[
v_2(5^t-1)=2+v_2(t)
\]

and again gives first return at \(t=2^k=N\).  Thus \(\sigma_p\) is one
\(N\)-cycle.

Finally, if two rows \(y,y'\) have the same exact lifted displacement under
\(\sigma_p\), then they have the same displacement modulo \(N\), so

\[
q_p(y-y')\equiv0\pmod N.
\]

There are at most \(\gcd(q_p,N)\) possible rows in one congruence class,
which is \(p\) for odd \(p\) and at most \(4\) for \(p=2\).  Since \(f\) is a
permutation, the same multiplicity bound holds across columns. ∎

Applied to \(f=R_{\mathbf c}\), this gives a nonlinear full two-channel host
at every prime power, with an exact Hamiltonian alternating cycle and bounded
vertical corresponding-column multiplicity.  Full two-dimensional
displacement multiplicity and cross-channel syndrome bounds remain open.

## 5. Exact binary digit-linear no-three channels

The completed reciprocal family gives a scalable line classification but not
a no-three theorem.  A separate digital family supplies exact finite positive
examples.

Write

\[
x=\sum_{j=0}^{k-1}x_j2^j,
\qquad x_j\in\mathbb F_2.
\]

For an invertible binary matrix \(M=(m_{ij})\), define

\[
y_i=\sum_jm_{ij}x_j\pmod2,
\qquad
F_M(x)=\sum_i y_i2^i.
\]

The following matrices are listed by row masks, with bit \(j\) of a mask equal
to \(m_{ij}\):

\[
\begin{array}{c|c}
k&\text{row masks}\\\hline
3&(4,2,5)\\
4&(8,4,2,13)\\
5&(28,8,2,25,29).
\end{array}
\]

### Theorem CMR5 — PROVED BY EXHAUSTIVE FINITE CHECK

For \(N=8,16,32\), the graph of the corresponding \(F_M\) is a permutation
channel with no real collinear triple.

### Verification

For each matrix, exact binary elimination checks invertibility.  The verifier
then evaluates all

\[
\binom N3
\]

triples with the integer determinant

\[
(x_2-x_1)(y_3-y_1)-(x_3-x_1)(y_2-y_1)
\]

and finds none equal to zero.

These are one-channel results, not saturated \(2N\)-point solutions.  They show
that digit mixing can avoid the universal affine obstruction and should be
treated as a serious prime-power candidate family.

## 6. Remaining endpoint

The prime-power track is now reduced to sharper positive questions:

1. replace the \(O(\sqrt N+\log N)\) completed-reciprocal line cap by a
   constant cap, or prove a repairable bound on the tangent cells;
2. control arbitrary two-dimensional displacement multiplicity for the
   companion pair, not only corresponding-column vertical displacement;
3. bound same- and cross-channel real triple syndrome;
4. find a scalable matrix family extending CMR5 beyond \(2^5\), or prove a
   recursive digit-lifting theorem;
5. integrate the local prime-power host with a mixed-projection-aware CRT
   theorem.

The computational companion is
[`scripts/verify_prime_power_channels.py`](../scripts/verify_prime_power_channels.py).
