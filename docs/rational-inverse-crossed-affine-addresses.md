# Affine-line addresses for crossed singleton channels

**Branch:** `research/rational-inverse-expansion`

RI5o--RI5p localize failure of the singleton auxiliary-transposition bank to a vertical, horizontal, or paired crossed-cell channel. This note assigns every such collateral triple an exact primitive direction and signed affine offset. Inside a fixed channel, that address identifies the auxiliary state.

## Auxiliary displacement coordinates

Retain the fixed blocker corner

\[
q_0=(c_0,r_0)
\]

and an auxiliary blocker cell

\[
p_c=(c,r_c).
\]

Write

\[
\Delta c=c-c_0,
\qquad
\Delta r=r_c-r_0.
\]

Both differences are nonzero. Factor the auxiliary displacement uniquely as

\[
\boxed{
(\Delta c,\Delta r)=m(a,b),
}
\]

where

\[
a>0,
\qquad
\gcd(a,|b|)=1,
\qquad
m\ne0.
\]

The crossed cells inserted by the auxiliary state are

\[
V_c=(c_0,r_c),
\qquad
H_c=(c,r_0).
\]

For a primitive direction

\[
e=(\alpha,\beta),
\qquad \alpha>0,
\]

write

\[
L(e,O)=
\{Z:\det(e,Z-q_0)=O\}
\]

for the corresponding signed affine line.

## RI5q -- exact crossed affine addresses -- PROVED

Every variable collateral triple in one auxiliary state lies on one of the following exact affine lines.

### Vertical channel

Suppose the triple contains \(V_c\) but not \(H_c\), and let \(e=(\alpha,\beta)\) be its primitive line direction. Then

\[
\boxed{
O=\alpha\Delta r=\alpha m b,
}
\]

and every cell \(Z\) of the triple satisfies

\[
\boxed{
\det(e,Z-q_0)=\alpha m b.
}
\]

### Horizontal channel

Suppose the triple contains \(H_c\) but not \(V_c\). Its primitive direction \(e=(\alpha,\beta)\) has \(\beta\ne0\), and

\[
\boxed{
O=-\beta\Delta c=-\beta m a.
}
\]

Thus

\[
\boxed{
\det(e,Z-q_0)=-\beta m a
}
\]

for every cell \(Z\) in the triple.

### Paired channel

Suppose the triple contains both \(V_c\) and \(H_c\). Its primitive line direction is the reflected auxiliary direction

\[
\boxed{
e=(a,-b),
}
\]

and its signed offset is

\[
\boxed{
O=mab.
}
\]

Equivalently, the third cell \(Z\) satisfies

\[
\boxed{
\det((a,-b),Z-q_0)=mab.
}
\]

### Address injectivity

Inside any fixed channel, the pair

\[
\boxed{(e,O)}
\]

determines the auxiliary column \(c\) uniquely.

### Proof

In the vertical channel, \(V_c-q_0=(0,\Delta r)\), so

\[
\det(e,V_c-q_0)=\alpha\Delta r.
\]

Every point on the same line has the same determinant against \(e\). Since \(\alpha>0\), the offset determines \(\Delta r\). The blocker matching has one column in each row, so \(r_c=r_0+\Delta r\) determines \(c\).

In the horizontal channel, \(H_c-q_0=(\Delta c,0)\), giving

\[
\det(e,H_c-q_0)=-\beta\Delta c.
\]

Three matching cells use distinct rows, so a horizontal-channel collateral line cannot be horizontal; hence \(eta\ne0\). The offset determines \(\Delta c\), and therefore \(c=c_0+\Delta c\).

For the paired channel,

\[
H_c-V_c=(\Delta c,-\Delta r)=m(a,-b),
\]

so the primitive direction is \((a,-b)\). Moreover,

\[
\det((a,-b),V_c-q_0)
=
\det((a,-b),(0,mb))
=mab.
\]

A fixed reflected direction determines \((a,b)\), while the nonzero product \(ab\) makes the offset determine \(m\). Hence it determines \(p_c=q_0+m(a,b)\), and therefore \(c\). \(\square\)

## Explicit intersection addresses

Let the two context cells in a one-cross channel be

\[
X=(x_1,y_1),
\qquad
Y=(x_2,y_2).
\]

In the vertical channel, \(x_1\ne x_2\) and collinearity determines the crossed row uniquely:

\[
\boxed{
r_c
=
\frac{(x_2-c_0)y_1-(x_1-c_0)y_2}{x_2-x_1}.
}
\]

In the horizontal channel, \(y_1\ne y_2\) and collinearity determines the crossed column uniquely:

\[
\boxed{
c
=
\frac{(y_2-r_0)x_1-(y_1-r_0)x_2}{y_2-y_1}.
}
\]

Thus a fixed context pair cannot recur in the same channel for two different auxiliaries.

## RI5r -- direction-offset concentration router -- PROVED

Let one RI5o channel/profile class have total candidate weight \(S\). Group its candidates by primitive line direction \(e\), writing \(S_e\) for the corresponding weight.

For every real threshold \(\gamma>0\), either some direction satisfies

\[
\boxed{S_e>\gamma,}
\]

or at least

\[
\boxed{
\left\lceil\frac{S}{\gamma}\right\rceil
}
\]

distinct primitive directions occur.

Now fix a heavy direction \(e\) of weight \(R=S_e\), and group it by signed offset \(O\), with weights \(R_O\). For every threshold \(eta>0\), either some exact affine line satisfies

\[
\boxed{R_O>\beta,}
\]

or at least

\[
\boxed{
\left\lceil\frac{R}{\beta}\right\rceil
}
\]

distinct offsets occur. In the latter case they are distinct parallel affine lines and distinct auxiliary states.

### Proof

The direction classes partition \(S\). If none exceeds \(\gamma\), fewer than \(\lceil S/\gamma\rceil\) positive classes cannot sum to \(S\). The offset classes similarly partition \(R\). RI5q proves that distinct offsets in a fixed channel and direction correspond to distinct auxiliaries. \(\square\)

## Quantitative RI5o consequence

Under failure of RI5n, RI5o supplies a channel/profile class with

\[
S\ge
\frac{(n-1)(W-F)}{3L}.
\]

Therefore the failed bank returns one of:

- at least
  \[
  \left\lceil
  \frac{(n-1)(W-F)}{3L\gamma}
  \right\rceil
  \]
  primitive collateral directions;
- one primitive direction carrying more than \(\gamma\), followed by at least \(\lceil R/\betaceil\) distinct parallel offsets;
- one exact affine line and auxiliary state carrying more than \(eta\).

For the paired channel the primitive direction is the reflection of the old blocker-edge direction, and the offsets \(mab\) form a radial scale stack. For the vertical and horizontal channels, the offsets are respectively \(\alpha(r_c-r_0)\) and \(-\beta(c-c_0)\), so parallel-line spread is exactly crossed-row or crossed-column spread.

## Interface to RI6, AC3, and BDA

The three crossed channels now share one arithmetic language.

- Direction spread is genuine slope growth.
- Parallel-line spread is a paid affine-offset stack.
- A heavy exact line is localized to one auxiliary rectangle.
- In the paired channel the old blocker direction \((a,b)\) and new collateral direction \((a,-b)\) form the same reflection pair that appears in the BDA \(CD\) decoder.

The quotient label and physical scale class remain attached, so repeated heavy addresses can enter the finite profile quotient while spread enters geometric or alternating-core cleaning.

## Finite check

`scripts/verify_rational_crossed_affine_addresses.py` exhausts small blocker permutations and every newly created collinear matching triple. It verifies all three signed-offset identities, reflected paired directions, context-pair intersection formulas, injectivity of `(channel, direction, offset)`, and the nested direction/offset weighted router.