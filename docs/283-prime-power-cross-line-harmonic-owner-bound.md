# Cross-line owner collateral is controlled by harmonic pair energy

Fix one inherited owner with response matching side `d`.  Let

\[
W_\omega=
\max\{x_{\max}-x_{\min},y_{\max}-y_{\min}\}
\]

be the maximum coordinate span of its source and target sets in the original
parent grid.  This distinction is essential for scattered residual factors.
Retain old state `S=O union M`, target `e in M`, and uniform response
`R in PM(H_e)`.  For distinct cells `a,b`, let `h(a,b)` be their primitive
integer direction height.  Axis pairs may be omitted because two matching
layers put at most two cells on an axis line.

### Theorem CMR1438 -- PROVED

A nonaxis line of primitive height `h` contains at most

\[
\boxed{1+\left\lfloor\frac{W_\omega}{h}\right\rfloor}
\]

owner-board cells.

### Proof

Across `t` primitive gaps, one coordinate changes by at least `t h`, while the
available coordinate span is at most `W_omega`. ∎

For entering owner `a`, let

\[
E_a(R)=
\left[O\cup(R\cap M)\cup\{b\in R\setminus M:a\prec b\}\right]
\setminus\{a\}.
\]

### Theorem CMR1439 -- PROVED

\[
\boxed{
\gamma_e(a,R)
\le
\frac{W_\omega}{2}
\sum_{\substack{b\in E_a(R)\\a,b\text{ nonaxis}}}
\frac1{h(a,b)}.
}
\]

### Proof

If a line through `a` has `z` eligible other cells and height `h`, CMR1438
gives `z-1<=W_omega/h`; hence

\[
\binom z2\le\frac{W_\omega}{2h}z.
\]

Sum the exact owner-line formula CMR1422. ∎

Let

\[
p_e(a)=\Pr(a\in R),
\qquad p_e(a,b)=\Pr(a,b\in R),
\]

and define

\[
\mathscr H_e(a)=
\sum_{\substack{b\in O\\a,b\text{ nonaxis}}}\frac1{h(a,b)}
+
\frac1{p_e(a)}
\sum_{\substack{b\in E(H_e)\setminus\{a\}\\
\{a,b\}\text{ compatible}\\a,b\text{ nonaxis}}}
\frac{p_e(a,b)}{h(a,b)}.
\]

### Theorem CMR1440 -- PROVED

Conditioned on `a in R`,

\[
\boxed{
\mathbb E\left[
\sum_{\substack{b\in(O\cup R)\setminus\{a\}\\a,b\text{ nonaxis}}}
\frac1{h(a,b)}\ \middle|\ a\in R
\right]=\mathscr H_e(a).}
\]

### Proof

The `O` contribution is fixed; a response partner has conditional probability
`p_e(a,b)/p_e(a)`. ∎

### Theorem CMR1441 -- PROVED

\[
\boxed{
g_e(a)\le\Gamma_e^{\rm harm}(a)
:=\frac{W_\omega}{2}\mathscr H_e(a).}
\]

### Proof

Condition CMR1439 on `a` and enlarge the eligible set to all selected partners.
∎

### Theorem CMR1442 -- PROVED

If rational potentials satisfy

\[
\alpha_x+\beta_y\ge\Gamma_e^{\rm harm}(x,y)
\]

on allowed edges, then

\[
\boxed{\mathbb E N(R)\le\sum_x\alpha_x+\sum_y\beta_y.}
\]

A dual sum below `D_S(e)` forces strict improvement, with the exact CMR1436
host penalty in restricted hosts.

### Theorem CMR1443 -- PROVED

For dyadic bands `H<=h<2H`,

\[
\boxed{\mathscr H_e(a)=\sum_H\mathscr H_{e,H}(a).}
\]

Bandwise rational assignment duals add exactly.

Let `mathscr H_e^{>=H_0}(a)` retain pairs of height at least `H_0`.

### Theorem CMR1444 -- PROVED

\[
\boxed{\mathscr H_e^{\ge H_0}(a)\le\frac{2d-1}{H_0}.}
\]

Consequently

\[
\boxed{
g_e(a)
\le\frac{W_\omega}{2}\mathscr H_e^{<H_0}(a)
+\frac{W_\omega(2d-1)}{2H_0}.}
\]

### Proof

Conditioned on `a`, there are `d` fixed and `d-1` other response partners;
each tail term is at most `1/H_0`. ∎

### Corollary CMR1445 -- PROVED

The same-owner diagonal problem is reduced to a low-height conditional pair
energy coupled through one assignment dual.  All geometry is measured in the
original owner coordinates through `W_omega`, while response probabilities use
the matching side `d`.  Rank-three collateral needs no separate probability
estimate.  No all-`n` theorem is claimed.

Checked in the full-grid specialization by
[`scripts/verify_prime_power_cross_line_harmonic_owner.py`](../scripts/verify_prime_power_cross_line_harmonic_owner.py).
