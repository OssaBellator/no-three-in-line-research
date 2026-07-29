# Bank-ready audit for one-target terminal interactions

**Branch:** `research/rational-inverse-expansion`

RI5ac--RI5ae reduce every shadow-free terminal active obstruction to one of
thirteen component words and then to a one-target or two-target hyperbola
interaction. This note completes the normalized collateral calculation for
the one-target branch once the selected physical block satisfies the bank-ready
hypotheses of RI5a.

Let

\[
X=\bigcup_{\alpha=1}^m u_\alpha H,
\qquad |H|=h,
\]

and use the uniform I6 state bank `M_(sigma,t)` on the installed physical block.
A **bank-ready rank-one prescription** fixes one source coset, one target row
coset and one within-coset shift. Equivalently, it imposes

\[
\sigma(\alpha)=\beta,
\qquad t_\alpha=s.
\]

## RI5bd -- exact one-cell I6 cylinder law -- PROVED

Every compatible bank-ready rank-one prescription occurs in exactly

\[
(m-1)!h^{m-1}
\]

of the `m!h^m` I6 states. Its probability is therefore

\[
\boxed{\frac1{mh}.}
\]

### Proof

The prescription fixes one value of the permutation and one shift coordinate.
The remaining `m-1` permutation values and `m-1` shifts are free. QED.

## One-target terminal records

A one-target terminal record consists of two state-independent context cells
and one prescribed bank cell. The record is present exactly when that one
cell prescription is present. Records may share the same prescribed cell or
context pair; no independence is asserted or needed.

## RI5be -- exact weighted one-target collateral -- PROVED

Let `T_1` be any weighted multiset of bank-ready one-target terminal records,
with nonnegative costs `c(T)`, and put

\[
Q_1=\sum_{T\in T_1}c(T).
\]

For a uniform I6 state, the expected total one-target collateral is exactly

\[
\boxed{\frac{Q_1}{mh}.}
\]

### Proof

Each record indicator has expectation `1/(mh)` by RI5bd. Sum the weighted
indicators and use linearity of expectation. Shared cells merely correlate
the indicators and do not change their individual expectations. QED.

## RI5bf -- context-pair multiplicity audit -- PROVED

For one fixed pair of distinct context cells, at most two target-hyperbola
cells can complete a one-target terminal triple. Hence a one-target event
inventory can be canonicalized by

\[
(\text{context pair},\text{target column},\text{component/profile word}),
\]

with target-column multiplicity at most two before the finite profile split.
This multiplicity is an inventory bound only; RI5be remains the correct
expectation even when the two records are fully correlated.

### Proof

The context pair determines one affine line. RI5w shows that a line meets the
nondegenerate target hyperbola in at most two cells. QED.

## RI5bg -- one-target fixed-edge comparison -- PROVED UNDER THE BANK-READY
## HYPOTHESES

Let `W` be the paid fixed-edge weight neutralized by the I6 bank, let `F` be
state-independent collateral, let `Q_1` be the complete one-target terminal
collateral weight, and let `C_>=2` be the exact expected collateral from every
remaining rank-two-or-higher prescription, evaluated with its actual cylinder
law. If

\[
\boxed{
\left(1-\frac1{mh}\right)W
>
F+\frac{Q_1}{mh}+C_{\ge2},
}
\]

then one I6 state strictly improves the paid potential.

### Proof

RI5a gives expected paid destruction at least
`(1-1/(mh))W`. RI5be gives the exact one-target contribution. Add the
state-independent and remaining exact collateral terms. Positive expected
net gain implies one improving state. QED.

## Physical audit and remaining branch

Every record used in RI5be must carry its physical source coset, target row
coset and within-coset shift. A normalized target that is outside the installed
block, lacks a coherent physical occurrence, or changes scale is returned to
the RI5d--RI5e physical-lift router; it is not silently charged at `1/(mh)`.

Thus the bank-ready one-target terminal branch has a complete collateral
formula. The remaining RI6 interaction work is the two-target secant branch,
non-bank-ready physical lifts, arithmetic owner payment, and replenishable
source recurrence.

## Finite check

`scripts/verify_ri_one_target_bank_audit.py` enumerates small I6 banks, verifies
the exact rank-one prescription count and weighted expectation, and checks the
at-most-two context-pair intersection law on small finite-field hyperbolas.
