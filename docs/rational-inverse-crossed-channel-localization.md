# Crossed-channel localization of failed singleton banks

**Branch:** `research/rational-inverse-expansion`

RI5m--RI5n turn the former singleton-blocker obstruction into an \((n-1)\)-state auxiliary-transposition bank. This note classifies every variable blocker-layer certificate in that bank by the crossed cells it uses.

## Crossed cells

Keep the fixed singleton blocker

\[
q=(c_0,r_0)
\]

and write the auxiliary blocker in column \(c\ne c_0\) as

\[
p_c=(c,r_c),
\qquad r_c=M_1(c).
\]

The RI5l state indexed by \(c\) inserts

\[
V_c=(c_0,r_c),
\qquad
H_c=(c,r_0).
\]

The cells \(V_c\) form a vertical star in the fixed column \(c_0\), while the cells \(H_c\) form a horizontal star in the fixed row \(r_0\).

Every variable collateral triple contains at least one of these two cells, and RI5m shows that its auxiliary index \(c\) is unique.

Partition the variable triples into three disjoint channel words:

1. \(V\): contains \(V_c\) but not \(H_c\);
2. \(H\): contains \(H_c\) but not \(V_c\);
3. \(VH\): contains both \(V_c\) and \(H_c\).

## RI5o -- crossed-channel profile localization -- PROVED

Assume \(W>F\) and the RI5n improvement criterion fails. Let

\[
\sigma:\mathcal T\to\Sigma,
\qquad |\Sigma|=L,
\]

be any finite arithmetic profile map. Then one channel/profile class has raw candidate weight at least

\[
\boxed{
\frac{(n-1)(W-F)}{3L}.
}
\]

The selected class has one of the following exact geometries.

### Vertical channel

Every candidate contains one cell

\[
\boxed{(c_0,r_c)}
\]

in the fixed column \(c_0\), with the rows \(r_c\) distinct across auxiliaries.

### Horizontal channel

Every candidate contains one cell

\[
\boxed{(c,r_0)}
\]

in the fixed row \(r_0\), with the columns \(c\) distinct across auxiliaries.

### Paired rectangle channel

Every candidate contains both opposite cross cells

\[
(c_0,r_c),
\qquad
(c,r_0)
\]

of the rectangle determined by \(q\) and \(p_c\). If its third cell is \(Z=(s,t)\), collinearity is exactly

\[
\boxed{
(c-c_0)(t-r_c)
-
(r_0-r_c)(s-c_0)
=0.
}
\]

Thus the third cell lies on the opposite rectangle diagonal through the two crossed cells.

### Proof

RI5n gives total raw variable weight at least \((n-1)(W-F)\). The three channel words and the \(L\) profile values partition the exact candidates into at most \(3L\) classes, proving the lower bound.

The vertical and horizontal descriptions are their definitions. For the paired channel, expand the determinant

\[
\det(H_c-V_c,Z-V_c)=0.
\]

This gives the displayed equation. \(\square\)

## RI5p -- heavy auxiliary or crossed-cell spread -- PROVED

Let one channel/profile class from RI5o have total weight \(S\). For auxiliary column \(c\), let \(S_c\) be the weight of candidates in the class created by that auxiliary state.

For every real threshold \(\beta>0\), exactly one of the following quantitative outputs is available:

1. **Heavy auxiliary rectangle:** some \(c\) satisfies
   \[
   \boxed{S_c>\beta.}
   \]
2. **Crossed-cell spread:** at least
   \[
   \boxed{
   \left\lceil\frac{S}{\beta}\right\rceil
   }
   \]
   distinct auxiliary columns carry positive class weight.

In the vertical channel these give distinct rows in one fixed column. In the horizontal channel they give distinct columns in one fixed row. In the paired channel they give distinct auxiliary rectangles sharing the singleton corner \(q\).

### Proof

The auxiliary classes partition the selected weight:

\[
S=\sum_{c\ne c_0}S_c.
\]

If no class exceeds \(\beta\), fewer than \(\lceil S/\beta\rceil\) positive classes would have total weight below \(S\), a contradiction. \(\square\)

## Interface to RI6 and alternating closure

A failed RI5n bank is no longer an arbitrary blocker-collateral family.

- A vertical output is a paid fixed-column star.
- A horizontal output is a paid fixed-row star.
- A paired output is a paid fan of opposite rectangle diagonals through one fixed blocker corner.
- RI5p either localizes payment to one explicit auxiliary rectangle or supplies quantitative physical spread.

These are direct inputs for the alternating-core anchor/resource routers, geometric cleaning, and the bounded-denominator rectangle dictionary. The quotient label and physical scale class remain attached throughout.

## Finite check

`scripts/verify_rational_crossed_channels.py` exhausts small blocker permutations, auxiliary states, variable matching triples, channel partitions, rectangle-diagonal identities, profile pigeonholing, and the heavy-auxiliary/spread alternative.