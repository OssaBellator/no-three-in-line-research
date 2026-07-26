# Cross-line owner collateral is controlled by harmonic pair energy

Fix an inherited `n x n` owner, old state `S=O union M`, target `e in M`, and
uniform response `R in PM(H_e)`.  For distinct cells `a,b`, let `h(a,b)` be the
maximum coordinate of their primitive integer direction.  Axis pairs may be
omitted because two matching layers put at most two cells on an axis line.

## Primitive-height capacity

### Theorem CMR1438 -- PROVED

A nonaxis line of primitive height `h` contains at most

\[
\boxed{1+\left\lfloor\frac{n-1}{h}\right\rfloor}
\]

parent-board cells.

### Proof

Across `t` primitive gaps, one coordinate changes by at least `t h`, while the
board coordinate range is `n-1`. ∎

## Realized harmonic owner bound

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
\frac{n-1}{2}
\sum_{\substack{b\in E_a(R)\\a,b\text{ nonaxis}}}
\frac1{h(a,b)}.
}
\]

### Proof

If a line through `a` has `z` eligible other cells and height `h`, then
`z-1<=(n-1)/h`; hence

\[
\binom z2\le\frac{n-1}{2h}z.
\]

Sum the exact owner-line formula CMR1422 over lines through `a`. ∎

## Exact conditional harmonic star

Let

\[
p_e(a)=\Pr(a\in R),
\qquad
p_e(a,b)=\Pr(a,b\in R).
\]

Define

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
\right]=\mathscr H_e(a).
}
\]

### Proof

The `O` contribution is fixed; each response partner has conditional
probability `p_e(a,b)/p_e(a)`. ∎

### Theorem CMR1441 -- PROVED

\[
\boxed{
g_e(a)\le\Gamma_e^{\rm harm}(a)
:=\frac{n-1}{2}\mathscr H_e(a).}
\]

### Proof

Condition CMR1439 on `a in R` and enlarge its eligible set to all other selected
cells. ∎

All triple ranks are now controlled by exact one-edge and two-edge rook
probabilities.

## Assignment certificate

### Theorem CMR1442 -- PROVED

If rational potentials satisfy

\[
\alpha_x+\beta_y\ge\Gamma_e^{\rm harm}(x,y)
\]

on allowed edges, then

\[
\boxed{\mathbb E N(R)\le\sum_x\alpha_x+\sum_y\beta_y.}
\]

A dual sum below `D_S(e)` forces strict improvement; the exact CMR1436 host
penalty applies in restricted hosts.

### Proof

Use CMR1441 in the assignment theorem CMR1426--CMR1427. ∎

## Height decomposition and tail

For dyadic `H`, retain pairs with `H<=h<2H` in `mathscr H_{e,H}(a)`.

### Theorem CMR1443 -- PROVED

\[
\boxed{\mathscr H_e(a)=\sum_H\mathscr H_{e,H}(a).}
\]

Bandwise rational assignment duals add exactly.

### Proof

Every nonaxis pair belongs to one primitive-height band and all terms are
nonnegative. ∎

Let `mathscr H_e^{>=H_0}(a)` retain pairs of height at least `H_0`.

### Theorem CMR1444 -- PROVED

\[
\boxed{\mathscr H_e^{\ge H_0}(a)\le\frac{2n-1}{H_0}.}
\]

Consequently

\[
\boxed{
g_e(a)
\le\frac{n-1}{2}\mathscr H_e^{<H_0}(a)
+\frac{(n-1)(2n-1)}{2H_0}.}
\]

### Proof

Conditioned on `a`, there are at most `n` fixed and `n-1` response partners;
each tail term is at most `1/H_0`. ∎

### Corollary CMR1445 -- PROVED

The same-owner diagonal problem is reduced to a low-height conditional pair
energy coupled through one bipartite assignment dual.  Rank-three collateral
needs no separate probability estimate.  The remaining arithmetic task is to
bound the low-height dual using prefix, quotient and carry structure.  No
all-`n` theorem is claimed.

Checked by
[`scripts/verify_prime_power_cross_line_harmonic_owner.py`](../scripts/verify_prime_power_cross_line_harmonic_owner.py).
