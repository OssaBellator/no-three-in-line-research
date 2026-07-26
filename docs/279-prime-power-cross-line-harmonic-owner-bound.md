# Cross-line owner collateral is controlled by conditional harmonic pair energy

CMR1390--CMR1397 give exact owner-edge weights through rook classes.  This
chapter converts the full owner load, including rank-two and rank-three
collateral, to a pairwise primitive-direction energy.  The conversion uses the
shared owner edge before any linewise maximum is taken.

Retain an inherited `n x n` board, an old state

\[
S=O\cup M,
\]

a target `e in M`, and a response `R in PM(H_e)`.  For distinct physical cells
`a,b`, let

\[
h(a,b)=\max(|u|,|v|)
\]

where `(u,v)` is the primitive integer direction from `a` to `b`.  Axis pairs
may be omitted throughout because an axis line contains at most two cells of
the union of two matchings.

## Primitive-height line capacity

### Theorem CMR1398 -- PROVED

A nonaxis line of primitive height `h` contains at most

\[
\boxed{
1+\left\lfloor\frac{n-1}{h}\right\rfloor
}
\]

cells of the parent board.  Hence, after fixing one cell `a` on the line, at
most `floor((n-1)/h)` other board cells remain.

### Proof

Successive integer points differ by a nonzero integer multiple of the
primitive direction.  Across `t` successive gaps, one coordinate changes by
at least `t h`, while every coordinate range in the board has length `n-1`.
Thus `t h<=n-1`. ∎

## Harmonic bound for one realized owner

Use the owner order of CMR1215.  For an entering owner `a in R setminus M`, let

\[
E_a(R)=
\left[O\cup(R\cap M)\cup\{b\in R\setminus M:a\prec b\}\right]\setminus\{a\}.
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

For a nonaxis line `L` through `a`, let `z_L` be the number of eligible other
cells from CMR1382 and let `h_L` be its primitive height.  CMR1398 gives

\[
z_L-1\le\frac{n-1}{h_L}.
\]

Therefore

\[
\binom{z_L}{2}
\le
\frac{n-1}{2h_L}z_L.
\]

Sum over lines through `a`.  Every eligible cell `b` lies on one unique line
through `a` and contributes exactly `1/h(a,b)` to the resulting first moment.
Use the exact owner-line formula CMR1382. ∎

This is the cross-line gain: the quadratic populations `binom(z_L,2)` are paid
by one harmonic first moment over the cells incident with the owner.

## Exact conditional harmonic star

Let `R` now be uniform on the extension-free bank.  Put

\[
p_e(a)=\Pr(a\in R)
\]

and, for two compatible allowed edges,

\[
p_e(a,b)=\Pr(a,b\in R).
\]

Both are exact rook probabilities from CMR1376.  Define

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
\sum_{\substack{b\in (O\cup R)\setminus\{a\}\\a,b\text{ nonaxis}}}
\frac1{h(a,b)}
\ \middle|\ a\in R
\right]
=
\mathscr H_e(a).
}
\]

### Proof

The opposite matching `O` is fixed.  For a response edge `b`, the conditional
selection probability is `p_e(a,b)/p_e(a)`.  Sum the corresponding indicators
with weights `1/h(a,b)`. ∎

The eligible set in CMR1399 is a subset of `(O union R) setminus {a}`, so this
conditional star is an upper envelope.

## Closed harmonic owner weight

### Theorem CMR1401 -- PROVED

The exact conditional owner weight of CMR1393 satisfies

\[
\boxed{
g_e(a)
\le
\Gamma_e^{\rm harm}(a)
:=
\frac{n-1}{2}\mathscr H_e(a).
}
\]

### Proof

Condition CMR1399 on `a in R`, enlarge the eligible set to all selected cells
other than `a`, and apply CMR1400. ∎

Thus every same-owner triple rank is controlled using only exact rank-one and
rank-two rook probabilities and primitive direction heights.

## Harmonic assignment certificate

### Theorem CMR1402 -- PROVED

Suppose rational row and column potentials satisfy

\[
\alpha_x+\beta_y
\ge
\Gamma_e^{\rm harm}(x,y)
\]

on every allowed edge.  Then

\[
\boxed{
\mathbb E N(R)
\le
\sum_x\alpha_x+\sum_y\beta_y.
}
\]

If this sum is below `D_S(e)`, an extension-free strict improvement exists.
For a restricted host, add the exact unavailable-edge penalty of CMR1396.

### Proof

CMR1401 dominates the exact conditional owner weights.  Apply the assignment
dual and improvement theorem CMR1386--CMR1387. ∎

This certificate couples all real lines through common response rows and
columns.

## Dyadic height decomposition

For dyadic `H`, let `mathscr H_{e,H}(a)` be the part of `mathscr H_e(a)` from
pairs with

\[
H\le h(a,b)<2H.
\]

### Theorem CMR1403 -- PROVED

\[
\boxed{
\mathscr H_e(a)=\sum_H\mathscr H_{e,H}(a).
}
\]

If potentials `alpha^H,beta^H` dominate

\[
\frac{n-1}{2}\mathscr H_{e,H}(a)
\]

for every height band, then their sums dominate `Gamma_e^{harm}`.  Hence
bandwise rational certificates add exactly.

### Proof

Every nonaxis pair has one primitive height and belongs to one dyadic band.
All terms are nonnegative, so the decomposition and addition of dual
inequalities are exact. ∎

## Uniform high-height tail

### Theorem CMR1404 -- PROVED

For every threshold `H_0>=1`,

\[
\boxed{
\sum_{H\ge H_0}\mathscr H_{e,H}(a)
\le
\frac{2n-1}{H_0}.
}
\]

Consequently

\[
\boxed{
 g_e(a)
\le
\frac{n-1}{2}
\sum_{H<H_0}\mathscr H_{e,H}(a)
+
\frac{(n-1)(2n-1)}{2H_0}.
}
\]

### Proof

Conditioned on `a in R`, there are exactly `n` opposite-layer cells and `n-1`
other response edges.  At most `2n-1` nonaxis pair terms occur.  Every term of
height at least `H_0` has weight at most `1/H_0`.  Apply CMR1401. ∎

Thus only finitely many low-height bands require arithmetic control; the
remaining tail is explicit.

## Harmonic-owner endpoint

### Corollary CMR1405 -- PROVED

The cross-line diagonal problem now has the following pair-energy normal form.

1. Every owner triple load is bounded by a harmonic star around its entering
   edge.
2. The conditional star has a closed formula using exact rank-one and rank-two
   rook probabilities.
3. Rank-three collateral requires no separate probability estimate in this
   envelope.
4. Row/column assignment duals couple all lines sharing matching vertices.
5. Primitive-height bands add exactly, and the high-height tail is bounded by
   `(n-1)(2n-1)/(2H_0)` per owner edge.
6. The unresolved mass is confined to low-height conditional pair energy,
   where the existing prefix, quotient and carry machinery applies.

The remaining theorem must bound the low-height assignment dual, not the
independent sum of line maxima.  No all-`n` theorem is claimed.

The line-capacity, harmonic-star, exact conditional-pair and tail identities
are checked in
[`scripts/verify_prime_power_cross_line_harmonic_owner.py`](../scripts/verify_prime_power_cross_line_harmonic_owner.py).
