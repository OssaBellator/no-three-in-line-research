# Affine-line addresses for crossed singleton channels

**Branch:** `research/rational-inverse-expansion`

RI5o--RI5p localize failure of the singleton auxiliary-transposition bank to a vertical, horizontal, or paired crossed-cell channel. This note assigns every such collateral triple an exact primitive direction and signed affine offset. Inside a fixed channel, that address identifies the auxiliary state.

## Auxiliary coordinates

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

Both differences are nonzero. Factor the displacement uniquely as

\[
\boxed{(\Delta c,\Delta r)=m(a,b),}
\]

where \(a>0\), \(\gcd(a,|b|)=1\), and \(m\ne0\).

The auxiliary transposition inserts

\[
V_c=(c_0,r_c),
\qquad
H_c=(c,r_0).
\]

For a primitive direction \(e=(α,β)\), normalized by \(α>0\), define

\[
L(e,O)=\{Z:\det(e,Z-q_0)=O\}.
\]

## RI5q -- exact crossed affine addresses -- PROVED

Every variable collateral triple in one auxiliary state lies on one of the following exact affine lines.

### Vertical channel

If the triple contains \(V_c\) but not \(H_c\), and \(e=(α,β)\) is its primitive direction, then

\[
\boxed{O=α\Delta r=αmb,}
\]

so every cell \(Z\) of the triple obeys

\[
\boxed{\det(e,Z-q_0)=αmb.}
\]

### Horizontal channel

If the triple contains \(H_c\) but not \(V_c\), then its primitive direction \(e=(α,β)\) has \(β\ne0\), and

\[
\boxed{O=-β\Delta c=-βma.}
\]

Thus every cell \(Z\) of the triple obeys

\[
\boxed{\det(e,Z-q_0)=-βma.}
\]

### Paired channel

If the triple contains both crossed cells, then its primitive direction is the reflected auxiliary direction

\[
\boxed{e=(a,-b),}
\]

and its signed offset is

\[
\boxed{O=mab.}
\]

Equivalently, its third cell \(Z\) satisfies

\[
\boxed{\det((a,-b),Z-q_0)=mab.}
\]

### Address injectivity

Inside any fixed channel, the pair

\[
\boxed{(e,O)}
\]

determines the auxiliary column \(c\) uniquely.

### Proof

For the vertical channel,

\[
V_c-q_0=(0,\Delta r),
\]

and hence

\[
\det(e,V_c-q_0)=α\Delta r.
\]

The offset determines \(\Delta r\). Since the blocker matching has one column in each row, \(r_c=r_0+\Delta r\) determines \(c\).

For the horizontal channel,

\[
H_c-q_0=(\Delta c,0),
\]

so

\[
\det(e,H_c-q_0)=-β\Delta c.
\]

A horizontal-channel collateral line cannot itself be horizontal because matching triples use distinct rows. Thus \(β\ne0\), and the offset determines \(\Delta c\), hence \(c\).

For the paired channel,

\[
H_c-V_c=(\Delta c,-\Delta r)=m(a,-b),
\]

which gives the reflected direction. Also

\[
\det((a,-b),V_c-q_0)
=
\det((a,-b),(0,mb))
=mab.
\]

The reflected primitive direction determines \((a,b)\), and the nonzero product \(ab\) makes the offset determine \(m\). Thus the address determines \(p_c=q_0+m(a,b)\), and therefore \(c\). \(\square\)

## Explicit intersection addresses

Let the two context cells in a one-cross channel be

\[
X=(x_1,y_1),
\qquad
Y=(x_2,y_2).
\]

In the vertical channel, collinearity determines the crossed row:

\[
\boxed{
r_c=
\frac{(x_2-c_0)y_1-(x_1-c_0)y_2}{x_2-x_1}.
}
\]

In the horizontal channel, collinearity determines the crossed column:

\[
\boxed{
c=
\frac{(y_2-r_0)x_1-(y_1-r_0)x_2}{y_2-y_1}.
}
\]

Thus a fixed context pair cannot recur in the same channel for two different auxiliaries.

## RI5r -- direction-offset concentration router -- PROVED

Let one RI5o channel/profile class have total candidate weight \(S\). Group it by primitive line direction, with weights \(S_e\).

For every threshold \(γ>0\), either some direction has

\[
\boxed{S_e>γ,}
\]

or at least

\[
\boxed{\left\lceil S/γ\right\rceil}
\]

distinct primitive directions occur.

Fix a heavy direction \(e\) of weight \(R=S_e\), and group it by signed offset, with weights \(R_O\). For every threshold \(β>0\), either some exact affine line has

\[
\boxed{R_O>β,}
\]

or at least

\[
\boxed{\left\lceil R/β\right\rceil}
\]

distinct offsets occur. These are distinct parallel affine lines and distinct auxiliary states.

### Proof

The direction classes partition \(S\), and the offset classes partition \(R\). The two alternatives are the weighted pigeonhole principle. Address injectivity proves that distinct offsets in a fixed channel and direction correspond to distinct auxiliaries. \(\square\)

## Quantitative RI5o consequence

Under failure of RI5n, RI5o supplies a channel/profile class with

\[
S\ge\frac{(n-1)(W-F)}{3L}.
\]

Therefore the failed bank returns one of:

- at least
  \[
  \left\lceil\frac{(n-1)(W-F)}{3Lγ}\right\rceil
  \]
  primitive collateral directions;
- one primitive direction carrying more than \(γ\), followed by at least \(\lceil R/β\rceil\) distinct parallel offsets;
- one exact affine line and auxiliary state carrying more than \(β\).

For the paired channel, the direction is the reflection of the old blocker-edge direction and the offsets \(mab\) form a radial scale stack. For the vertical and horizontal channels, the offsets are \(α(r_c-r_0)\) and \(-β(c-c_0)\), so parallel-line spread is exactly crossed-row or crossed-column spread.

## Interface to RI6, AC3, and BDA

The three crossed channels now share one arithmetic language.

- Direction spread is genuine slope growth.
- Parallel-line spread is a paid affine-offset stack.
- A heavy exact line is localized to one auxiliary rectangle.
- The paired channel uses the same reflection \((a,b)\mapsto(a,-b)\) as the BDA \(CD\) decoder.

The quotient label and physical scale class remain attached, so repeated heavy addresses can enter the finite profile quotient while spread enters geometric or alternating-core cleaning.

## Finite check

`scripts/verify_rational_crossed_affine_addresses.py` exhausts small blocker permutations and every newly created collinear matching triple. It verifies all three signed-offset identities, reflected paired directions, context-pair intersection formulas, address injectivity, and the nested direction/offset weighted router.