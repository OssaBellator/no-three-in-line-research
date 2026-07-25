# Primitive-slope dictionary for radial decoder collateral

**Branch:** `research/bounded-denominator-absorbers`

BDA5m--BDA5n reduce the balanced decoder floor to one- or two-local-cell determinant loci. BDA3g classifies every actual collinear triple by one primitive spatial direction. This note identifies that direction for every BDA5n channel and gives the remaining concentration-versus-spread router.

## Primitive normalization

For a nonzero integer vector \(z=(r,s)\), write

\[
\operatorname{prim}(z)
\]

for the unique primitive vector on the same line whose first coordinate is positive. Retain the BDA normalization

\[
d=(a,b),
\qquad a>0,
\qquad \gcd(a,|b|)=1.
\]

## BDA5o -- exact primitive-slope dictionary -- PROVED

### One-local channels

Let \(z\in\{z_A,z_B,z_C,z_D\}\), and suppose the two fixed context cells satisfy

\[
Y-X=t e,
\]

where \(t\ne0\) and \(e\) is primitive. The triple containing the inserted cell \(P+wz\) is collinear exactly when

\[
\boxed{
\det(X-P,e)=w\det(z,e).
}
\]

If \(\det(z,e)=0\), then the context line passes through \(P\) and has primitive direction \(\operatorname{prim}(z)\). This is the BDA5m anchor-ray wall.

If \(\det(z,e)\ne0\), the primitive direction \(e\) and the role \(w\) determine the exact signed affine offset of the context line from \(P\).

### Explicit wall directions

The four one-cell channels produce only three anchor-ray directions:

\[
\boxed{
\begin{aligned}
A,B &: d=(a,b),\\
C &: \operatorname{prim}(ha,Hb),\\
D &: \operatorname{prim}(Ha,hb).
\end{aligned}
}
\]

### Two-local channels

The blocker pair \(AB\) lies on the original radial line, so its primitive direction is

\[
\boxed{d=(a,b).}
\]

The active pair \(CD\) lies on an affine line with direction

\[
z_C-z_D=q(-a,b).
\]

After primitive normalization, every \(CD\) context line has direction

\[
\boxed{(a,-b).}
\]

Moreover its role-dependent offset is

\[
\boxed{
\det((a,-b),X-P)
=
wab(2h+q).
}
\]

Hence the \(u\)- and \(v\)-role \(CD\) lines have the same primitive direction and signed offsets separated by

\[
\boxed{
(u-v)ab(2h+q)\ne0.
}
\]

### Proof

Since \(Y-X=te\), divide the BDA5m one-cell identity by \(t\) to obtain

\[
\det(X-P-wz,e)=0,
\]

which is the first displayed equation. If \(\det(z,e)=0\), then \(e\) and \(z\) are parallel, while \(\det(X-P,e)=0\) places \(P\) on the context line.

The wall directions follow from the four channel vectors. For \(CD\), substitute

\[
z_C-z_D=-q(a,-b)
\]

and

\[
\det(z_C,z_D)=-abq(2h+q)
\]

into BDA5m and divide by \(-q\). The \(AB\) statement follows from \(z_A,z_B\in\operatorname{span}(d)\). \(\square\)

Thus every wall or two-local output uses one of at most four explicit primitive directions:

\[
\boxed{
(a,b),
\quad
(a,-b),
\quad
\operatorname{prim}(ha,Hb),
\quad
\operatorname{prim}(Ha,hb).
}
\]

## BDA5p -- heavy primitive slope or slope spread -- PROVED

Let a non-wall one-local BDA5n channel family have total collateral weight \(S\). For every represented primitive context direction \(e\), let \(S_e\) be its total weight.

For every real threshold \(\beta>0\), at least one of the following holds:

1. **Heavy primitive slope:** some direction \(e\) has
   \[
   \boxed{S_e>\beta.}
   \]
   All its context lines have the exact role-dependent offset
   \[
   \det(X-P,e)=w\det(z,e).
   \]
2. **Primitive-slope spread:** at least
   \[
   \boxed{
   \left\lceil\frac{S}{\beta}\right\rceil
   }
   \]
   distinct primitive directions are represented.

Outcome 2 holds whenever outcome 1 fails.

### Proof

The primitive-direction classes partition the family:

\[
S=\sum_e S_e.
\]

If every \(S_e\le\beta\), fewer than \(\lceil S/\beta\rceil\) positive classes cannot sum to \(S\). The offset identity is BDA5o. \(\square\)

## Quantitative BDA5l consequence

Under the BDA5l failed-floor hypothesis, the BDA5n selected channel has weight at least

\[
\frac{D-F}{72L},
\]

or at least \((D-F)/(144L)\) after a one-local wall/non-wall split.

Therefore every role side now returns one of:

- that much weight on one of four explicit primitive directions;
- a non-wall primitive direction carrying more than a chosen threshold \(\beta\), with exact affine offset;
- at least \(\lceil (D-F)/(144L\beta)\rceil\) distinct primitive directions.

This is exactly the BDA3g interface: concentration enters the valuation and residue charts, while spread pays for genuinely new slope classes.

## Finite check

`scripts/verify_bda_role_slope_dictionary.py` exhausts small integer decoder parameters, primitive context directions, channel walls, `CD` offsets, and the weighted heavy-slope/spread router.