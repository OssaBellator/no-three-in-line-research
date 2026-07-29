# Mixed one-local and two-local balanced-floor templates

**Branch:** `research/bounded-denominator-absorbers`

BDA5br--BDA5bt close the six unordered off-diagonal comparisons among the one-local channels `A,B,C,D`. The nine remaining templates involve `CD` or `AB`. This note gives their exact line-incidence classification.

Translate the common anchor `P` to the origin and retain

\[
d=(a,b),\quad H=h+q,
\]

\[
z_A=(ha,hb),\ z_B=(Ha,Hb),\ z_C=(ha,Hb),\ z_D=(Ha,hb).
\]

The role-`u` `CD` context line is

\[
L_{CD}(u):
\det(z_C-z_D,X-P)=u\det(z_C,z_D),
\]

and the `AB` context line is

\[
L_{AB}=P+\operatorname{span}(d).
\]

## BDA5bu -- CD versus one-local line-coincidence criterion -- PROVED

Let the other role use one local cell `U=P+vz`, where `z` is one of `z_A,z_B,z_C,z_D`. A one-local context pair can have both cells on `L_CD(u)` only if

\[
\boxed{v\det(z_C-z_D,z)=u\det(z_C,z_D).}
\]

If this equation fails, every one-local context line through `U` meets `L_CD(u)` in at most one context cell.

For the four channels the coincidence equation becomes

\[
\boxed{
\begin{array}{c|c}
z&\text{resonance}\cr\hline
z_A&2hv=u(2h+q),\\
z_B&2Hv=u(2h+q),\\
z_C&v=u,\\
z_D&v=u.
\end{array}}
\]

Thus for distinct roles `u!=v`, the `CD-C` and `CD-D` templates never have coincident context lines; `CD-A` and `CD-B` do so only on the two displayed arithmetic resonance profiles.

### Proof

Two shared context cells force the one-local context line to equal `L_CD(u)`, hence its local cell `P+vz` lies on that line. Substitution gives the determinant equation. Direct calculation gives

\[
\det(z_C,z_D)=-abq(2h+q),
\]

\[
\det(z_C-z_D,z_A)=-2habq,
\quad
\det(z_C-z_D,z_B)=-2Habq,
\]

and the value `-abq(2h+q)` for `z_C,z_D`. QED.

## BDA5bv -- AB versus one-local classification -- PROVED

A one-local cell `P+vz` lies on `L_AB` exactly when

\[
\boxed{\det(d,z)=0.}
\]

This holds for `z_A,z_B` and fails for `z_C,z_D`, since

\[
\det(d,z_C)=abq,
\qquad
\det(d,z_D)=-abq.
\]

Consequently:

1. `AB-A` and `AB-B` may share the full radial context line;
2. `AB-C` and `AB-D` share at most one context cell with any one-local context line.

### Proof

The local point lies on the radial line through `P` exactly when its direction vector is parallel to `d`. The determinant values are immediate. If it is not on the radial line, a distinct one-local context line intersects the radial line in at most one point. QED.

## BDA5bw -- CD versus AB unique intersection -- PROVED

The lines `L_CD(u)` and `L_AB` meet in exactly one context point. Writing that point as `P+td`,

\[
\boxed{
t=\frac{u(2h+q)}{2}.
}
\]

In particular, a `CD-AB` comparison cannot share two distinct context cells.

### Proof

Substitute `X=P+td` into the `CD` equation. Since

\[
\det(z_C-z_D,d)=-2abq\ne0,
\]

there is exactly one solution, and division by the displayed determinant gives the value of `t`. QED.

## BDA5bx -- complete nine-template router -- PROVED

Every remaining off-diagonal template has one exact continuation:

1. `CD-A` or `CD-B`: one arithmetic resonance profile, or at most one shared context cell per one-local address;
2. `CD-C` or `CD-D`: at most one shared context cell;
3. `AB-A` or `AB-B`: radial-line concentration or exclusive residuals;
4. `AB-C` or `AB-D`: at most one shared context cell;
5. `CD-AB`: one fixed line-intersection point.

Therefore all fifteen unordered off-diagonal balanced-floor templates now have explicit incidence geometry. Remaining BDA6 work is weighted payment/realization, arithmetic owner routing, and higher-rank imports; no off-diagonal template remains geometrically unclassified.

## Finite check

`scripts/verify_bda_mixed_two_local_templates.py` checks all determinant identities, resonance conditions and line-intersection multiplicities on finite integer parameter ranges.