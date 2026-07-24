# Prime-power valuation charts for primitive slope chains

BDA3g factors every compatible collinear relative address as

\[
\begin{pmatrix}
U&V\\
S&T
\end{pmatrix}
=
\begin{pmatrix}a\\b\end{pmatrix}
\begin{pmatrix}m&n\end{pmatrix},
\qquad
a>0,\quad \gcd(a,|b|)=1.
\]

For composite \(q\), a residue matrix can have no globally invertible
entry even though the primitive direction is visible prime by prime.
The exact obstruction is common divisibility of both point scales.

## BDA3h -- valuation-pivot classification

Fix a prime power \(\ell^e\Vert q\).  Put

\[
\kappa_\ell
=
\min\{e,v_\ell(m),v_\ell(n)\},
\]

with \(v_\ell(0)=\infty\).

### Theorem BDA3h -- PROVED

The value \(\kappa_\ell\) is determined by the coordinate-difference
matrix modulo \(\ell^e\): it is the minimum truncated \(\ell\)-adic
valuation of its four entries.

If \(\kappa_\ell<e\), divide all four entries by
\(\ell^{\kappa_\ell}\) and reduce modulo

\[
L_\ell=\ell^{e-\kappa_\ell}.
\]

The resulting matrix

\[
\widetilde M_\ell
=
\begin{pmatrix}a\\b\end{pmatrix}
\begin{pmatrix}
m/\ell^{\kappa_\ell}&n/\ell^{\kappa_\ell}
\end{pmatrix}
\pmod {L_\ell}
\]

has a unit entry.  Any unit pivot
\((\widetilde M_\ell)_{ij}\) uniquely determines both projective
classes

\[
\boxed{
[a:b]\in\mathbb P^1(\mathbb Z/L_\ell\mathbb Z),
\qquad
[m/\ell^{\kappa_\ell}:n/\ell^{\kappa_\ell}]
\in\mathbb P^1(\mathbb Z/L_\ell\mathbb Z).
}
\]

Explicitly, if \(i'\ne i\) and \(j'\ne j\), then

\[
\boxed{
\frac{d_{i'}}{d_i}
=
\frac{(\widetilde M_\ell)_{i'j}}
{(\widetilde M_\ell)_{ij}},
\qquad
\frac{c_{j'}}{c_j}
=
\frac{(\widetilde M_\ell)_{ij'}}
{(\widetilde M_\ell)_{ij}}
\pmod {L_\ell},
}
\]

where \(d=(a,b)\) and
\(c=(m/\ell^{\kappa_\ell},n/\ell^{\kappa_\ell})\).

If \(\kappa_\ell=e\), the residue matrix is zero modulo \(\ell^e\);
equivalently,

\[
\boxed{
m\equiv n\equiv0\pmod{\ell^e}.
}
\]

### Proof

Primitivity gives

\[
\min\{v_\ell(a),v_\ell(b)\}=0.
\]

For an outer product, the minimum valuation of all four entries is
therefore

\[
\min\{v_\ell(m),v_\ell(n)\},
\]

truncated at \(e\).  This proves the first assertion and the zero-matrix
equivalence.

When \(\kappa_\ell<e\), the divided direction vector still has a unit
coordinate, and the divided scale vector has a unit coordinate by the
definition of \(\kappa_\ell\).  Their outer product consequently has a
unit entry.  At a unit pivot both corresponding factors are units.
Dividing the other entry in its column recovers the direction ratio;
dividing the other entry in its row recovers the scale ratio.  A
unimodular two-vector is determined up to multiplication by a unit by
either such affine chart, proving uniqueness of the two projective
classes. \(\square\)

## Consequence for the \(q\)-profile

Apply BDA3h independently to every prime power dividing \(q\).  Every
nonzero local residue component has a unit-pivot chart and therefore
determines the primitive slope and relative point-scale classes at the
visible precision.  The only invisible component is one on which both
point scales are multiples of the full prime power.

Thus the singular residue wall from BDA3g is no longer an arbitrary
zero-divisor phenomenon.  It is exactly a common-scale valuation tower.
BDA4 may split a heavy slope chain into finitely many prime-power charts;
continued loss of slope information forces increasing common
divisibility of \(m\) and \(n\), which is the scale parameter that must
be paid, bounded, or absorbed.

This theorem does not bound that valuation tower across repeated
re-extractions.  It supplies its exact local state and removes all other
composite-denominator ambiguity.

## BDA4b -- finite common-content tower

Suppose the three cells lie in an integer box whose coordinate diameter
is at most \(N\).  For every prime \(\ell\mid q\), define the untruncated
common-scale height

\[
\nu_\ell(m,n)=\min\{v_\ell(m),v_\ell(n)\},
\]

and put

\[
\boxed{
V_q(m,n)=\sum_{\ell\mid q}\nu_\ell(m,n),
\qquad
g_q(m,n)=\prod_{\ell\mid q}\ell^{\nu_\ell(m,n)}.
}
\]

Let

\[
L_\ell(N)=\max\{k\geq0:\ell^k\leq N\}.
\]

### Theorem BDA4b -- PROVED

For every compatible triple in the box,

\[
\boxed{
0\leq V_q(m,n)
\leq
\sum_{\ell\mid q}L_\ell(N).
}
\]

Repeatedly choose any prime \(\ell\mid q\) dividing both current scales
and replace

\[
(m,n)\longmapsto(m/\ell,n/\ell).
\]

Every step lowers \(V_q\) by exactly one.  After exactly
\(V_q(m,n)\) steps the process reaches the unique pair

\[
\boxed{
(m^\circ,n^\circ)
=
\left(\frac m{g_q(m,n)},\frac n{g_q(m,n)}\right),
}
\]

for which no prime divisor of \(q\) divides both coordinates.  At that
terminal pair, every prime-power component \(\ell^e\Vert q\) has
\(\kappa_\ell=0\) in BDA3h and therefore has a unit-pivot chart at full
modulus \(\ell^e\).

### Proof

Because \(a\geq1\),

\[
|m|=\frac{|U|}{a}\leq N,
\qquad
|n|=\frac{|V|}{a}\leq N.
\]

The two scales are nonzero.  Hence
\(v_\ell(m),v_\ell(n)\leq L_\ell(N)\), which proves the boxed height
bound.

Dividing both scales by \(\ell\) subtracts one from
\(\nu_\ell\) and leaves every other prime valuation unchanged, so it
lowers \(V_q\) by exactly one.  Prime division commutes, and the total
power removed at \(\ell\) is forced to be
\(\ell^{\nu_\ell(m,n)}\).  Thus every order ends after exactly \(V_q\)
steps at the displayed unique pair.

For each \(\ell\mid q\), at least one of \(m^\circ,n^\circ\) is an
\(\ell\)-adic unit.  Primitivity of \((a,b)\) likewise makes at least
one direction coordinate an \(\ell\)-adic unit.  Their outer product
therefore has a unit entry modulo \(\ell^e\), so BDA3h applies with
\(\kappa_\ell=0\). \(\square\)

BDA4b closes the internal singular-division recursion for one geometric
address.  In a prime-minus-one grid one may take \(N\leq p-1\), giving
an explicit \(O_q(\log p)\) ceiling.  A BDA4 transition system must
record the untruncated height rather than only the saturated residue
\(\min(e,\nu_\ell)\); after the canonical common content is removed,
the remaining classification concerns \(q\)-primitive slope/scale
profiles and genuine profile cycles, not an invisible valuation tower.

## BDA3i -- global projective atlas after content removal

Write \(R_q=\mathbb Z/q\mathbb Z\).  A vector in \(R_q^2\) is
**unimodular** when its two coordinates generate \(R_q\).  Integer
primitivity makes \(d=(a,b)\) unimodular modulo \(q\), and BDA4b makes
\(c=(m^\circ,n^\circ)\) unimodular modulo \(q\).

Let \(\mathbb P^1(R_q)\) be the set of unimodular vectors modulo
multiplication by a unit.

### Theorem BDA3i -- PROVED

The normalized residue matrix

\[
M^\circ
=
\begin{pmatrix}a\\b\end{pmatrix}
\begin{pmatrix}m^\circ&n^\circ\end{pmatrix}
\pmod q
\]

uniquely determines both projective classes

\[
\boxed{
[a:b]\in\mathbb P^1(R_q),
\qquad
[m^\circ:n^\circ]\in\mathbb P^1(R_q).
}
\]

Moreover,

\[
\boxed{
|\mathbb P^1(R_q)|
=
\prod_{\ell^e\Vert q}
(\ell^e+\ell^{e-1})
=
q\prod_{\ell\mid q}\left(1+\frac1\ell\right).
}
\]

After fixing one representative of every projective class, every
unimodular rank-one residue matrix has a unique representation

\[
\boxed{
M=s\,d_0c_0^{\mathsf T},
\qquad
s\in R_q^\times.
}
\]

Consequently the number of such matrices is exactly

\[
\boxed{
\varphi(q)\,|\mathbb P^1(R_q)|^2.
}
\]

### Proof

Suppose

\[
dc^{\mathsf T}=d'(c')^{\mathsf T}
\]

with all four factor vectors unimodular.  Choose a linear functional
\(\alpha\) with \(\alpha(d)=1\).  Applying \(\alpha\) to the matrix
identity gives

\[
c=u c',
\qquad
u=\alpha(d').
\]

Because \(c\) is unimodular, its coordinates generate the unit ideal;
as both are multiples of \(u\), the element \(u\) must be a unit.
Choose a functional taking value one on \(c'\) and apply it on the
right to obtain \(d'=u d\).  Thus the two projective classes are forced.
Fixing representatives then leaves the unique product of the two
factor units as the scalar \(s\).

For \(q=\ell^e\), there are
\(\ell^{2e}-\ell^{2e-2}\) unimodular vectors.  The free action of the
\(\varphi(\ell^e)=\ell^{e-1}(\ell-1)\) units gives

\[
|\mathbb P^1(\mathbb Z/\ell^e\mathbb Z)|
=\ell^e+\ell^{e-1}.
\]

The Chinese remainder theorem multiplies these counts over the prime
powers dividing \(q\).  Finally, a projective-class pair and a unit
scalar give distinct matrices by the uniqueness just proved, yielding
the last count. \(\square\)

BDA3i assembles the prime-power pivots into one finite composite-modulus
profile even when the matrix has no globally unit entry.  After the
common-content tower is removed, the residue part of a primitive
slope/scale address has exactly the finite atlas above.  The remaining
BDA4 unboundedness is therefore in integer lifts and transition cycles,
not composite-residue factorization.

`scripts/verify_bda_valuation_charts.py` exhaustively checks the
truncated valuation, unit-pivot, and projective-ratio identities for
small primitive directions, scales, and prime powers.  It also checks
the canonical common-content reduction, exact height descent, box
ceiling, terminal unit pivots, global projective uniqueness, and the
exact CRT atlas count for composite denominators.
