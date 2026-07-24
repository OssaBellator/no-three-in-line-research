# Prime-power displacement signatures and one-channel syndrome

This chapter continues the valuation-completed reciprocal analysis from
[`docs/28-prime-power-completed-reciprocals.md`](28-prime-power-completed-reciprocals.md).
It supplies an exact same-channel displacement filter and the first general
real-triple syndrome bound for a nonlinear full composite channel.

Let \(N=p^k\), and let \(R_{\mathbf c}\) be the completed reciprocal
permutation.  For a nonzero integer \(z\), write \(v_p(z)\) for its
\(p\)-adic valuation.

## 1. Every secant is p-adically diagonal

Take two distinct channel points

\[
P=(x,R_{\mathbf c}(x)),
\qquad
P'=(x',R_{\mathbf c}(x')),
\]

and write their exact lifted displacement as

\[
(a,b)=(x'-x,R_{\mathbf c}(x')-R_{\mathbf c}(x)).
\]

### Theorem CMR6 — PROVED

Every completed-reciprocal secant satisfies

\[
v_p(a)=v_p(b).
\]

Consequently, a displacement vector whose two coordinates have unequal
\(p\)-adic valuation has multiplicity zero inside one channel.  After removing
the common power of \(p\), both coordinates of every primitive secant
direction are units modulo \(p\).

### Proof

Let \(r=v_p(x)\) and \(s=v_p(x')\), with the convention that the origin has
valuation \(k\).

If \(r\ne s\), then

\[
v_p(x'-x)=\min(r,s).
\]

The channel preserves valuation pointwise, so the two row values have
valuations \(r,s\), and their difference has the same valuation
\(\min(r,s)\).

Now suppose \(r=s<k\).  Write

\[
x=p^r u,
\qquad x'=p^r v,
\]

with \(u,v\) units modulo \(p^{k-r}\).  On this stratum,

\[
R_{\mathbf c}(x)=p^r c_r u^{-1},
\qquad
R_{\mathbf c}(x')=p^r c_r v^{-1}
\pmod {p^k}.
\]

Therefore

\[
R_{\mathbf c}(x')-R_{\mathbf c}(x)
\equiv
-p^r c_r\frac{v-u}{uv}
\pmod {p^k}.
\]

The factors \(c_r,u,v\) are units, so the modular row difference and the
column difference \(p^r(v-u)\) have the same valuation below \(k\).  Their
standard lifted differences are nonzero integers of absolute value below
\(p^k\), so adding a multiple of \(p^k\) cannot change that valuation. ∎

This closes an exact displacement-signature subtask of CM3.  It is not yet a
constant multiplicity bound.

## 2. Exact same-stratum secant product

Suppose the two endpoints in CMR6 have the same valuation \(r\).  Put

\[
t=v_p(a)=v_p(b),
\qquad
\alpha=a/p^t,
\qquad
\beta=b/p^t.
\]

Then \(r\le t<k\), and \(\alpha,\beta\) are units modulo \(p\).

### Theorem CMR7 — PROVED

With \(x=p^r u\) and \(x'=p^r v\), one has the exact reduced secant signature

\[
uv\equiv-c_r\alpha\beta^{-1}
\pmod {p^{k-t}}.
\]

Equivalently, the first endpoint parameter obeys

\[
u\bigl(u+p^{t-r}\alpha\bigr)
\equiv-c_r\alpha\beta^{-1}
\pmod {p^{k-t}}.
\]

For odd \(p\), candidate same-stratum secants with fixed displacement are
therefore controlled by one explicit square-root congruence.  If

\[
D_{r,t}
=
\bigl(p^{t-r}\alpha\bigr)^2
+4c_r\alpha\beta^{-1},
\]

then the number of residue classes for \(u\pmod {p^{k-t}}\) is exactly the
number of square roots of \(D_{r,t}\) modulo \(p^{k-t}\), and is bounded by

\[
2p^{\lfloor(k-t)/2\rfloor}.
\]

### Proof

The reciprocal difference identity on the common stratum is

\[
\frac b{p^r}
\equiv
-c_r\frac{a/p^r}{uv}
\pmod {p^{k-r}}.
\]

Both sides are divisible by \(p^{t-r}\).  Dividing by this power reduces the
modulus to \(p^{k-t}\) and gives

\[
\beta\equiv-c_r\alpha(uv)^{-1}
\pmod {p^{k-t}}.
\]

This is the first displayed congruence.  Since
\(v-u=a/p^r=p^{t-r}\alpha\), substitution gives the quadratic in \(u\).
For odd \(p\), completing the square gives

\[
\bigl(2u+p^{t-r}\alpha\bigr)^2
\equiv D_{r,t}
\pmod {p^{k-t}}.
\]

The square-root count is the one classified in Theorem CMR3. ∎

The missing multiplicity upgrade is now precise: one must control lifts from
these reduced residue classes together with the cross-stratum cases
\(v_p(x)\ne v_p(x')\).

## 3. A general one-channel syndrome bound

Let \(T(R_{\mathbf c})\) denote the number of unordered real collinear triples
inside one completed-reciprocal channel.  Theorem CMR3 gives the coarse line
cap

\[
L_{p,k}=2k+2p^{\lfloor k/2\rfloor}+1.
\]

### Theorem CMR8 — PROVED

For every odd prime power \(N=p^k\),

\[
T(R_{\mathbf c})
\le
\frac{L_{p,k}-2}{3}\binom N2.
\]

In particular,

\[
T(R_{\mathbf c})
=
O\!\left(N^{5/2}+N^2\log N\right).
\]

### Proof

For each real line \(\ell\), let \(s_\ell\) be its channel occupancy.  Every
unordered pair of channel points determines exactly one real line, so

\[
\sum_\ell\binom{s_\ell}{2}=\binom N2.
\]

For every \(3\le s\le L_{p,k}\),

\[
\binom s3
=
\frac{s-2}{3}\binom s2
\le
\frac{L_{p,k}-2}{3}\binom s2.
\]

Summing over the lines proves the claim. ∎

This is far above the desired \(O(N\log^C N)\) endpoint, but it is a rigorous
finite syndrome bound for a nonlinear full channel over every odd prime
power.  The tangent-cell classification and CMR7 identify exactly where a
sharper count must be proved.

## 4. Computational evidence and next target

For the uniform choice \(c_r=1\), exact checks give:

| \(p^k\) | maximum real line | real collinear triples |
|---:|---:|---:|
| 9 | 5 | 10 |
| 27 | 7 | 93 |
| 81 | 9 | 580 |
| 243 | 12 | 3303 |
| 25 | 5 | 30 |
| 125 | 8 | 809 |

These values are finite observations, not asymptotic claims.  They are much
smaller than the worst-case CMR8 bound and suggest the next concrete theorem:
prove a divisor-sensitive count for exact real points inside one
Hensel-tangent cell, rather than counting every modular square root as a real
line point.

The checks are implemented in
[`scripts/verify_prime_power_displacement.py`](../scripts/verify_prime_power_displacement.py).

## 5. Exact companion cross-displacement quadratic

Let

\[
\sigma_p(y)=[(1+e_p)y+1]_N,
\qquad
 e_p=\begin{cases}p,&p\text{ odd},\\4,&p=2,\end{cases}
\]

and put \(G=\sigma_p\circ R_{\mathbf c}\).  Consider an oriented cross-channel
pair

\[
P=(x,R_{\mathbf c}(x)),
\qquad
P'=(x+a,G(x+a)),
\]

with exact lifted displacement \((a,b)=P'-P\).  Suppose both columns are
nonzero and lie in the same valuation stratum \(r\).  Write

\[
x=p^r u,
\qquad
a=p^r\alpha,
\qquad m=k-r.
\]

Then \(u\) and \(u+\alpha\) are units modulo \(p^m\).

### Theorem CMR9 — PROVED

Every such cross-channel pair satisfies

\[
b\equiv1\pmod {p^r}.
\]

Putting \(B=(b-1)/p^r\), its first endpoint parameter obeys the exact
quadratic congruence

\[
B u^2+(B\alpha-c_r e_p)u+c_r\alpha
\equiv0\pmod {p^m}.
\]

For odd \(p\), if \(p\nmid B\), the possible residue classes of \(u\) are in
bijection with square roots modulo \(p^m\) of

\[
\mathcal D
=(B\alpha-c_rp)^2-4Bc_r\alpha.
\]

Hence the number of candidate same-stratum cross-channel pairs with fixed
exact displacement is at most

\[
\rho_p(m,\mathcal D)
\le2p^{\lfloor m/2\rfloor}.
\]

### Proof

Modulo \(N\), the row displacement equation is

\[
p^r c_r\bigl((1+e_p)(u+\alpha)^{-1}-u^{-1}\bigr)+1
\equiv b.
\]

The first term is divisible by \(p^r\), proving \(b\equiv1\pmod {p^r}\).
After subtracting one and dividing by \(p^r\), multiplication by
\(u(u+\alpha)\) gives

\[
B u(u+\alpha)
\equiv c_r(e_pu-\alpha)
\pmod {p^m},
\]

which is the displayed quadratic.  When \(p\) and \(B\) are units, completing
the square with leading coefficient \(B\) gives the stated discriminant and
the square-root count from Theorem CMR3. ∎

This is the first exact companion cross-channel displacement equation.  The
remaining cases are cross-stratum pairs and the singular regime
\(p\mid B\).

## 6. Exact mixed-layer determinant carry identity

The companion map also has a universal exact carry normal form, independent
of the special choice of base permutation.  Let \(f\) be any permutation of
\([N]\), put

\[
q(y)=\left\lfloor\frac{(1+e_p)y+1}{N}\right\rfloor,
\qquad
d(y)=e_py+1-Nq(y),
\]

so that \(\sigma_p(y)=y+d(y)\) as standard integers.

For columns \(x_i\), write \(y_i=f(x_i)\), choose layer indicators
\(\varepsilon_i\in\{0,1\}\), and set

\[
z_i=y_i+\varepsilon_i d(y_i).
\]

### Theorem CMR10 — PROVED

The exact integer determinant of the three chosen layer points is

\[
\begin{aligned}
\Delta((x_i,z_i)_{i=1}^3)
={}&\Delta((x_i,y_i)_{i=1}^3)\\
&+(x_2-x_1)(\varepsilon_3d(y_3)-\varepsilon_1d(y_1))\\
&-(x_3-x_1)(\varepsilon_2d(y_2)-\varepsilon_1d(y_1)).
\end{aligned}
\]

In particular, for three points all in the companion layer,

\[
\Delta_G
=(1+e_p)\Delta_f
-N\Bigl((x_2-x_1)(q(y_3)-q(y_1))
-(x_3-x_1)(q(y_2)-q(y_1))\Bigr).
\]

Thus every same- or mixed-layer real triple is governed by an explicit base
determinant plus a bounded-range companion carry determinant.

### Proof

Substitute \(z_i=y_i+\varepsilon_i d(y_i)\) into the determinant and use its
linearity in the row coordinates.  When all three indicators equal one, the
constant terms in \(d(y)=e_py+1-Nq(y)\) cancel, the \(e_py\) contribution is
\(e_p\Delta_f\), and the remaining term is the displayed multiple of \(N\).
∎

CMR9 and CMR10 reduce the companion cross-channel CM3 target to explicit
quadratic-root and carry-determinant counts.  A near-linear syndrome theorem
still requires controlling the singular cross-displacement cells and the
number of exact real solutions inside each carry signature.
