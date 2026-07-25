# Conditional fixed-edge coset-bank conversion

RI4a confines every order-two colour-ratio component to at most four
source \(H\)-cosets, and RI4b localizes a constant fraction of its paid
weight to one quotient edge.  If those normalized quotient cosets have
already been certified as one installed physical hyperbola block, the
full coset-union bank from I6 can be used on that block.  This note
records the resulting survival probabilities and the executable
collateral criterion under that physical-lift hypothesis.

The hypothesis is not automatic.  The quotient vertices classify
\(c=z/x\), while I6 acts on physical columns.  The occurrence base
\(x\) may vary.
[`rational-inverse-lift-coherence.md`](rational-inverse-lift-coherence.md)
proves RI5d--RI5e, gives the exact scale-coset audit, and exhibits the
normalization obstruction.

Let \(H\leq\mathbb F_p^\times\) have order \(h\), and let

\[
X=\bigcup_{\alpha=1}^m u_\alpha H,
\qquad
1\leq m\leq4,
\]

be the union of the distinct source cosets used by the component.  On a
hyperbola layer \(xy=a\), its current cells are

\[
e_x=(x,a/x),
\qquad
x\in X.
\]

Assume explicitly that these are physical columns and current cells of
one permutation layer, not merely normalized root labels; that the full
block \(X\) and its row set \(aX^{-1}\) are installed; and that every
paid orbit below is supported on this block.  These are the
**bank-ready hypotheses** of RI5e.

For \(\sigma\in S_m\) and \(t=(t_1,\ldots,t_m)\in H^m\), use the I6
state

\[
M_{\sigma,t}
=
\bigcup_{\alpha=1}^m
\left\{
\left(
u_\alpha g,
\frac{a}{u_{\sigma(\alpha)}t_\alpha g}
\right):g\in H
\right\}.
\]

There are \(m!h^m\) equally weighted states, including the current
state.  Undoing any normalization of the ratio variable merely
multiplies the \(u_\alpha\) and leaves all statements below unchanged.

## RI5a -- paid fixed-edge neutralization

### Theorem RI5a -- PROVED

A prescribed current cell in one source coset survives a uniform I6
state with probability

\[
\boxed{\frac1{mh}.}
\]

Any collection of current cells from one source coset survives
simultaneously with the same probability.  Current cells from two
distinct source cosets survive simultaneously with probability

\[
\boxed{
\frac1{(m)_2h^2}.
}
\]

More generally, compatible prescribed cells in \(r\) distinct source
cosets and \(r\) distinct target row cosets survive with probability

\[
\boxed{
\frac1{(m)_rh^r},
\qquad
1\leq r\leq m.
}
\]

Let \(\mathscr O\) be any paid family of current
\(\tau_r\)-orbits on one localized quotient edge, and assign
nonnegative weights \(w(O)\).  An orbit is neutralized when at least one
of its current endpoint cells is absent from the new state.  Put

\[
W=\sum_{O\in\mathscr O}w(O).
\]

Then the expected neutralized weight is at least

\[
\boxed{
\left(1-\frac1{mh}\right)W.
}
\]

Consequently some I6 state neutralizes at least this much paid weight.

### Proof

Take a current cell with column \(u_\alpha g\).  It belongs to
\(M_{\sigma,t}\) exactly when

\[
u_{\sigma(\alpha)}t_\alpha=u_\alpha.
\]

Distinctness of the \(H\)-cosets forces
\(\sigma(\alpha)=\alpha\), and then \(t_\alpha=1\).  A uniform
permutation fixes \(\alpha\) with probability \(1/m\), independently
of the uniform \(t_\alpha\), giving \(1/(mh)\).  The same two conditions
retain every current cell in that source coset, proving the
same-coset assertion.

For two distinct source cosets, the permutation must fix both indices
and both shifts must be one.  The probability is

\[
\frac{(m-2)!}{m!}\frac1{h^2}
=
\frac1{(m)_2h^2}.
\]

For a general compatible rank-\(r\) prescription, the required
source-to-target assignments fix \(r\) values of \(\sigma\), leaving
\((m-r)!\) permutations, and fix \(r\) independent shifts.  Division
by \(m!h^m\) gives the general cylinder probability.

A fixed or same-coset orbit survives only if its source block is the
current block, with probability \(1/(mh)\).  A cross-coset orbit
survives with probability \(1/((m)_2h^2)\), which is at most
\(1/(mh)\).  Therefore every orbit is neutralized with probability at
least \(1-1/(mh)\).  Linearity of expectation proves the paid bound,
and averaging supplies one state attaining it. \(\square\)

## Exact collateral interface

Partition possible collateral into a state-independent contribution
\(F\) and a family \(\mathcal T\) of compatible prescriptions.  Give
each prescription a nonnegative cost \(c(T)\), and let \(r(T)\) be its
number of distinct prescribed source and target cosets.  The I6
cylinder formula gives expected variable collateral

\[
\boxed{
\mathcal C
=
\sum_{T\in\mathcal T}
\frac{c(T)}{(m)_{r(T)}h^{r(T)}}.
}
\]

### Corollary RI5b -- PROVED

If

\[
\boxed{
\left(1-\frac1{mh}\right)W
>
F+\mathcal C,
}
\]

then one row-column-preserving I6 state strictly lowers the paid
potential.

### Proof

For a uniform bank state, the expected paid destruction is at least the
left side, while the expected collateral is at most the right side.
The expected net improvement is therefore positive, so some state has
positive net improvement.  Every state is a perfect matching on the
same rows and columns by I6. \(\square\)

### Corollary RI5c -- PROVED

Let \(W_{\mathrm{comp}}\) be the total paid point or orbit weight in one
order-two quotient component.  Use the I6 bank on its \(m\) source
cosets and let \(F+\mathcal C\) be the fixed plus normalized collateral
for the edge selected by RI4b.

In the alternating-square case, an improving state exists whenever

\[
\boxed{
\frac14
\left(1-\frac1{mh}\right)
W_{\mathrm{comp}}
>
F+\mathcal C.
}
\]

In the loop-and-edge case, it is enough that

\[
\boxed{
\frac13
\left(1-\frac1{mh}\right)
W_{\mathrm{comp}}
>
F+\mathcal C.
}
\]

### Proof

RI4b selects one quotient edge of weight at least
\(W_{\mathrm{comp}}/4\) in the square and at least
\(W_{\mathrm{comp}}/3\) in the collapsed template.  Apply RI5b to that
edge. \(\square\)

RI5a--RI5c complete the finite-state comparison of a **bank-ready**
paid order-two quotient edge.  No new state construction is required
after physical installation: the source cosets use I6, and the only
remaining estimate is the explicit normalized collateral sum above.
Prescriptions with repeated source or target cosets must be placed in
\(F\) or evaluated with their actual block correlation; they are not
silently assigned the distinct-coset cylinder probability.

They do not prove that normalized RI4b or OP4i density is bank-ready.
RI5d shows that the base scales are algebraically free, while RI5e
returns scale mismatch, scale growth, a physical point star, or a
scale-localized partial lift before this theorem may be invoked.

`scripts/verify_rational_fixed_edge_bank.py` enumerates every I6 state
for small \(m,h\), checks same-block, cross-block, and all-rank cylinder
probabilities, and verifies the paid neutralization average.
