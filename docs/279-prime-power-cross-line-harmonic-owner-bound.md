# Cross-line owner collateral is controlled by conditional harmonic pair energy

CMR1390--CMR1397 give exact owner-edge weights through rook classes.  This
chapter converts the full owner load, including rank-two and rank-three
collateral, to a pairwise primitive-direction energy.  The conversion uses the
shared owner edge before any independent linewise maximum is taken.

Retain an inherited `n x n` board, an old state

\[
S=O\cup M,
\]

a target `e in M`, and a response `R in PM(H_e)`.  For distinct physical cells
`a,b`, let

\[
h(a,b)=\max(|u|,|v|),
\]

where `(u,v)` is the primitive integer direction from `a` to `b`.  Axis pairs
may be omitted because an axis line contains at most two cells of the union of
two matchings.

## Primitive-height line capacity

### Theorem CMR1398 -- PROVED

A nonaxis line of primitive height `h` contains at most

\[
\boxed{1+\left\lfloor\frac{n-1}{h}\right\rfloor}
\]

parent-board cells.  After fixing one cell on the line, at most
`floor((n-1)/h)` other cells remain.

### Proof

Successive integer points differ by a nonzero integer multiple of the
primitive direction.  Across `t` gaps, one coordinate changes by at least
`t h`, while every coordinate range has length `n-1`.  Hence `t h<=n-1`. ∎

## Harmonic bound for one realized owner

For an entering owner `a in R\setminus M`, let

\[
E_a(R)=
\left[
O\cup(R\cap M)\cup\{b\in R\setminus M:a\prec b\}
\right]\setminus\{a\}.
\]

### Theorem CMR1399 -- PROVED

\[
\boxed{
\gamma_e(a,R)
\le
\frac{n-1}{2}
\sum_{\substack{b\in E_a(R)\\a,b\text{ nonaxis}}}
\frac1{h(a,b)}.
}
\]

### Proof

For a nonaxis line `L` through `a`, let `z_L` be its eligible population from
CMR1382 and let `h_L` be its primitive height.  CMR1398 gives

\[
z_L-1\le\frac{n-1}{h_L}.
\]

Therefore

\[
\binom{z_L}{2}
\le
\frac{n-1}{2h_L}z_L.
\]

Sum over lines through `a`.  Each eligible cell lies on one unique line
through `a` and contributes `1/h(a,b)`.  Apply CMR1382. ∎

The quadratic line populations have become one harmonic first moment over the
cells incident with the shared owner edge.

## Exact conditional harmonic star

Let `R` be uniform on the extension-free bank.  Put

\[
p_e(a)=\Pr(a\in R),
\qquad
p_e(a,b)=\Pr(a,b\in R)
\]

for compatible allowed edges.  These are exact rank-one and rank-two rook
probabilities.  Define

\[
\mathscr H_e(a)
=
\sum_{\substack{b\in O\\a,b\text{ nonaxis}}}
\frac1{h(a,b)}
+
\frac1{p_e(a)}
\sum_{\substack{b\in E(H_e)\setminus\{a\}\\
                 \{a,b\}\text{ compatible}\\
                 a,b\text{ nonaxis}}}
\frac{p_e(a,b)}{h(a,b)}.
\]

### Theorem CMR1400 -- PROVED

Conditioned on `a in R`,

\[
\boxed{
\mathbb E
\left[
\sum_{\substack{b\in(O\cup R)\setminus\{a\}\\a,b\text{ nonaxis}}}
\frac1{h(a,b)}
\ \middle|\ a\in R
\right]
=
\mathscr H_e(a).
}
\]

### Proof

The matching `O` is fixed.  For a response edge `b`, its conditional selection
probability is `p_e(a,b)/p_e(a)`.  Sum the indicators with weight `1/h(a,b)`.
∎

## Closed harmonic owner weight

### Theorem CMR1401 -- PROVED

\[
\boxed{
g_e(a)\le\Gamma_e^{\rm harm}(a)
:=\frac{n-1}{2}\mathscr H_e(a).}
\]

### Proof

Condition CMR1399 on `a in R`, enlarge the eligible set to all selected cells
other than `a`, and apply CMR1400. ∎

Thus all collateral ranks are controlled using only exact one-edge and two-edge
rook probabilities plus primitive direction height.

## Harmonic assignment certificate

### Theorem CMR1402 -- PROVED

If rational potentials satisfy

\[
\alpha_x+\beta_y\ge\Gamma_e^{\rm harm}(x,y)
\]

on every allowed edge, then

\[
\boxed{
\mathbb E N(R)\le\sum_x\alpha_x+\sum_y\beta_y.
}
\]

If the right side is below `D_S(e)`, an extension-free strict improvement
exists.  In a restricted host, add the exact unavailable-edge penalty from
CMR1396.

### Proof

CMR1401 dominates the exact conditional owner weights.  Apply the assignment
dual and CMR1387. ∎

## Dyadic height decomposition

For dyadic `H`, let `mathscr H_{e,H}(a)` retain only pairs with

\[
H\le h(a,b)<2H.
\]

### Theorem CMR1403 -- PROVED

\[
\boxed{
\mathscr H_e(a)=\sum_H\mathscr H_{e,H}(a).
}
\]

If `alpha^H,beta^H` dominate

\[
\frac{n-1}{2}\mathscr H_{e,H}(a)
\]

for every band, their sums dominate `Gamma_e^{harm}`.  Bandwise rational
dual certificates therefore add exactly.

### Proof

Every nonaxis pair has one primitive height and belongs to one dyadic band.
Sum the nonnegative identities and inequalities. ∎

## Uniform high-height tail

Let `mathscr H_e^{>=H_0}(a)` denote the part of the conditional star from pairs
with primitive height at least `H_0`.

### Theorem CMR1404 -- PROVED

For every `H_0>=1`,

\[
\boxed{
\mathscr H_e^{\ge H_0}(a)
\le
\frac{2n-1}{H_0}.
}
\]

Consequently

\[
\boxed{
 g_e(a)
\le
\frac{n-1}{2}\mathscr H_e^{<H_0}(a)
+
\frac{(n-1)(2n-1)}{2H_0}.
}
\]

### Proof

Conditioned on `a in R`, there are `n` opposite-layer cells and `n-1` other
response edges.  At most `2n-1` nonaxis pair terms occur, and every term in
the tail is at most `1/H_0`.  Apply CMR1401. ∎

Only the finitely many low-height bands require arithmetic control.

## Harmonic-owner endpoint

### Corollary CMR1405 -- PROVED

1. Every owner triple load is bounded by a harmonic star around its entering
   edge.
2. The conditional star is a closed expression using exact rank-one and
   rank-two rook probabilities.
3. Rank-three collateral requires no separate probability estimate in this
   envelope.
4. Assignment duals couple all lines sharing matching vertices.
5. Primitive-height bands add exactly, and the high-height tail is explicit.
6. The unresolved mass is confined to low-height conditional pair energy,
   where prefix, quotient and carry estimates can be applied.

The remaining theorem must bound the low-height assignment dual, not an
independent sum of line maxima.  No all-`n` theorem is claimed.

The results are checked in
[`scripts/verify_prime_power_cross_line_harmonic_owner.py`](../scripts/verify_prime_power_cross_line_harmonic_owner.py).
