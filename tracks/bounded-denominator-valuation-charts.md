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

`scripts/verify_bda_valuation_charts.py` exhaustively checks the
truncated valuation, unit-pivot, and projective-ratio identities for
small primitive directions, scales, and prime powers.
