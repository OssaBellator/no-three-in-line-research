# The extension-free target bank has the same permanent lower bound

CMR1302--CMR1309 identify the union over all forbidden extensions through a
target cell `e` as

\[
\operatorname{PM}(K_{n,n}\setminus(O\cup\{e\})).
\]

The earlier expectation theorem CMR1198--CMR1208 averaged inside one fixed
`(n-2)`-regular graph `K_{n,n}\setminus(O\cup F)`.  It was not clear that the
larger extension-free bank retained a comparable permanent denominator.

It does.  The graph obtained by deleting one perfect matching and one additional
nonmatching edge supports an explicit doubly stochastic matrix with every entry
at most `1/(n-2)`.  Van der Waerden then gives exactly the same lower bound used
for the fixed-extension bank.  Thus one may average uniformly over all response
matchings which omit the target cell, without first choosing `F`.

## 1. Normalized extension-free graph

Relabel the fixed opposite matching as the identity and the target edge as

\[
e=(0,1).
\]

Put

\[
H_e=K_{n,n}\setminus(O\cup\{e\}),
\qquad n\ge4,
\]

and let `C={2,...,n-1}`.

Define a matrix `X=(x_{ij})` supported on `H_e` by

\[
x_{0j}=\frac1{n-2}\quad(j\in C),
\]

\[
x_{10}=x_{1j}=\frac1{n-1}\quad(j\in C),
\]

\[
x_{i0}=\frac1{n-1},
\qquad
x_{i1}=\frac1{n-2}
\quad(i\in C),
\]

and

\[
x_{ij}=g_n
=\frac{n^2-5n+5}{(n-1)(n-2)(n-3)}
\quad(i,j\in C,\ i\ne j).
\]

All forbidden entries are zero.

## 2. Explicit doubly stochastic scaling

### Theorem CMR1350 -- PROVED

For every `n>=4`, all displayed entries are positive and `X` is doubly
stochastic:

\[
\boxed{
\sum_jx_{ij}=1,
\qquad
\sum_ix_{ij}=1.
}
\]

### Proof

Rows and columns `0` and `1` are immediate.  For `i in C`,

\[
\frac1{n-1}+\frac1{n-2}+(n-3)g_n=1.
\]

The same identity gives every column in `C`.  The numerator
`n^2-5n+5` is positive for integer `n>=4`. ∎

## 3. Maximum entry

### Theorem CMR1351 -- PROVED

\[
\boxed{
0<x_{ij}\le\frac1{n-2}
}
\]

on every allowed edge.

### Proof

The entries `1/(n-1)` and `1/(n-2)` have the claim.  For `g_n`,

\[
g_n\le\frac1{n-2}
\iff
n^2-5n+5\le(n-1)(n-3),
\]

which reduces to `n>=2`. ∎

## 4. Permanent lower bound

### Theorem CMR1352 -- PROVED

The extension-free response bank satisfies

\[
\boxed{
|\operatorname{PM}(H_e)|
\ge
n!\left(\frac{n-2}{n}\right)^n.
}
\]

### Proof

Van der Waerden gives

\[
\operatorname{per}(X)\ge\frac{n!}{n^n}.
\]

Every perfect-matching monomial in `per(X)` is at most `(n-2)^{-n}` by CMR1351.
Therefore

\[
\operatorname{per}(X)
\le
|\operatorname{PM}(H_e)|(n-2)^{-n}.
\]

Combine the inequalities. ∎

The denominator is identical to CMR1199.

## 5. Prescription probabilities

Let `R` be uniform on `PM(H_e)` and put

\[
\kappa_n=\left(\frac n{n-2}\right)^n.
\]

### Theorem CMR1353 -- PROVED

For every compatible rank-`r` prescription `P subseteq E(H_e)`, where
`1<=r<=3`,

\[
\boxed{
\Pr(P\subseteq R)
\le
\frac{\kappa_n}{(n)_r}.
}
\]

### Proof

At most `(n-r)!` perfect matchings contain `P`.  Divide by the CMR1352 lower
bound. ∎

Thus all fixed-extension candidate-count estimates transfer unchanged to the
extension-free bank after replacing `G` by `H_e`.

## 6. Extension-free collateral criterion

Let `V_r^e` count genuinely new physical triples whose residual prescription in
`H_e` has rank `r`, with old response-layer subsets subtracted as in
CMR1222--CMR1224.  Put

\[
\mathcal C_e(S;O)
=
\frac{V_1^e}{n}
+
\frac{V_2^e}{(n)_2}
+
\frac{V_3^e}{(n)_3}.
\]

### Theorem CMR1354 -- PROVED

For uniform `R in PM(H_e)`,

\[
\boxed{
\mathbb E N(R)
\le
\kappa_n\mathcal C_e(S;O).
}
\]

Every response omits `e`, so it destroys at least the old target load `D_S(e)`.
Consequently

\[
\boxed{
\kappa_n\mathcal C_e(S;O)<D_S(e)
}
\]

forces an ambient strict improvement.

### Proof

Apply CMR1353 to every corrected candidate prescription and sum.  The response
graph itself omits `e`. ∎

No optimization over forbidden extensions remains in this criterion.

## 7. Restricted-host penalty

Let `b_e` be the number of edges of `H_e` unavailable in the current rematched-
layer host, and let `m=Phi(S)`.

### Theorem CMR1355 -- PROVED

If

\[
\boxed{
\kappa_n
\left[
\mathcal C_e(S;O)+\frac{(m+1)b_e}{n}
\right]
<
D_S(e),
}
\]

then some extension-free response is feasible and has potential below `m`.

### Proof

CMR1353 with `r=1` bounds the expected number of unavailable edges used by
`kappa_n b_e/n`.  Add the penalty `(m+1)` and repeat the feasibility-forcing
argument of CMR1207. ∎

If all extension-free responses are blocked, their inclusion-minimal blocker
cover is an exact deficiency-one unit wall by CMR1150--CMR1157.

## 8. Canonical implementation by a forbidden extension

### Theorem CMR1356 -- PROVED

For every `R in PM(H_e)`, the graph

\[
K_{n,n}\setminus(O\cup R)
\]

is `(n-2)`-regular and contains `e`.  Hence it has a perfect matching `F_R`
containing `e`.  Choosing the first such matching in a fixed order gives

\[
R\in\operatorname{PM}(K_{n,n}\setminus(O\cup F_R)).
\]

### Proof

The complement of two disjoint perfect matchings is regular.  CMR1302 says every
edge of a regular bipartite graph belongs to a 1-factor.  Since `R` omits `e` and
`O` does not contain it, the edge remains in the complement. ∎

Thus the uniform extension-free response law is a genuine mixture of executable
fixed-extension banks.

## 9. Extension-free endpoint

### Corollary CMR1357 -- PROVED

For every target cell outside the fixed opposite matching and every `n>=4`:

1. the complete response family omitting that cell has the same permanent lower
   bound as a fixed-extension bank;
2. rank-one, rank-two and rank-three prescription probabilities retain the
   factor `kappa_n/(n)_r`;
3. the corrected line-profile formulas of CMR1334--CMR1349 apply with `G=H_e`;
4. one explicit target-versus-collateral inequality replaces optimization over
   all forbidden extensions;
5. restricted availability adds the same finite unavailable-edge penalty;
6. complete blockage gives unit-wall descent;
7. every chosen response has a canonical realizing forbidden extension.

The remaining diagonal-block problem may therefore use one extension-free bank
per target cell.  This reduces both the exact credit state space and the coarse
upper quotient without weakening the permanent denominator.  No all-`n` theorem
is claimed.

The doubly stochastic scaling, permanent bound, prescription ratios, restricted
penalty and canonical extension are checked in
[`scripts/verify_prime_power_extension_free_permanent.py`](../scripts/verify_prime_power_extension_free_permanent.py).
