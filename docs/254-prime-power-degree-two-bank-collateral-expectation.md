# Degree-two target banks have a universal collateral expectation bound

CMR1190--CMR1197 isolate the missing prime-power step as a target-versus-collateral
inequality.  This chapter gives the first direct inequality for one canonical
fixed-target response bank.

Fix a saturated two-layer state `S` on a residual side `n>=4`.  Choose one selected
physical target cell `e` in layer `ell`, and let `O` be the fixed opposite-layer
perfect matching.  Since the two selected layers are physically disjoint,
`e notin O`.

Relabel rows and columns so that `O` is the identity.  Choose a perfect matching
`F` which contains `e` and is disjoint from `O`, and put

\[
G=K_{n,n}\setminus(O\cup F),
\qquad
\mathcal B=\operatorname{PM}(G).
\]

Every `R in mathcal B` gives the saturated response state `Q_R=O union R` and
removes the physical cell `e`.

Define

\[
\kappa_n=\left(\frac{n}{n-2}\right)^n.
\]

## 1. A disjoint forbidden extension always exists

### Theorem CMR1198 -- PROVED

For every `n>=3`, every perfect matching `O`, and every edge `e notin O`, there is
a perfect matching `F` such that

\[
e\in F,
\qquad
F\cap O=\varnothing.
\]

### Proof

Relabel `O` as the identity and write `e=(i,j)` with `i ne j`.  Choose an `n`-cycle
whose cyclic order places `j` immediately after `i`.  Its permutation matching
contains `(i,j)` and has no fixed point, hence is disjoint from the identity.  Undo
the relabelling. ∎

Thus the degree-two response bank may always be chosen with exactly two forbidden
edges at every row and column.

## 2. The response graph is regular and has many perfect matchings

### Theorem CMR1199 -- PROVED USING THE VAN DER WAERDEN PERMANENT BOUND

The graph `G` is `(n-2)`-regular on both bipartition classes and

\[
\boxed{
|\mathcal B|
=\operatorname{per}(A_G)
\ge
n!\left(\frac{n-2}{n}\right)^n.
}
\]

Moreover

\[
\boxed{\kappa_n\le16}
\qquad(n\ge4).
\]

### Proof

The disjoint perfect matchings `O,F` remove exactly two incident edges at every
vertex.  Hence `A_G/(n-2)` is doubly stochastic.  Van der Waerden gives

\[
\operatorname{per}(A_G/(n-2))\ge n!/n^n,
\]

which yields the displayed lower bound after rescaling.

For the constant, the function

\[
x\longmapsto x\log\frac{x}{x-2}
\]

is decreasing for `x>2`, since

\[
\log(1+2/(x-2))<2/(x-2).
\]

Therefore `kappa_n<=kappa_4=16`. ∎

The side-three bank is the exact singleton response of CMR1174--CMR1176 and is
kept separate from this estimate.

## 3. Rank-r cylinder probabilities

Let `P` be a set of `r` pairwise compatible edges of `G`, with `1<=r<=3`.  Delete
their source and target endpoints and write `G/P` for the residual graph.

### Theorem CMR1200 -- PROVED

Under the uniform law on `mathcal B`,

\[
\boxed{
\Pr(P\subseteq R)
=
\frac{|\operatorname{PM}(G/P)|}{|\operatorname{PM}(G)|}.
}
\]

Consequently

\[
\boxed{
\Pr(P\subseteq R)
\le
\frac{\kappa_n}{(n)_r}
\le
\frac{16}{(n)_r}.
}
\]

If `P` is incompatible or contains an edge outside `G`, its occurrence probability
is zero.

### Proof

Restriction and reinsertion of `P` give a bijection between bank matchings
containing `P` and perfect matchings of `G/P`.  The numerator is at most `(n-r)!`,
while CMR1199 bounds the denominator below by

\[
n!((n-2)/n)^n.
\]

Divide and use `(n-r)!/n!=1/(n)_r`. ∎

This estimate is geometry-free and applies to every fixed-core or loaded-line
bank whose forbidden extension is chosen disjointly from the opposite layer.

## 4. Exact physical collateral classification

Let `mathcal T(S)` be the physical collinear triples of the old state.  For a
physical triple `U notin mathcal T(S)`, put

\[
P_U=U\setminus O,
\qquad
r(U)=|P_U|.
\]

Let `mathcal V_r` be the triples `U notin mathcal T(S)` for which `r(U)=r` and
`P_U` is a compatible rank-`r` subset of `G`.  Put `V_r=|mathcal V_r|`.

### Theorem CMR1201 -- PROVED

For every response `R in mathcal B`,

\[
\boxed{
|\mathcal T(Q_R)\setminus\mathcal T(S)|
=
\sum_{r=1}^{3}
\sum_{U\in\mathcal V_r}
\mathbf 1_{P_U\subseteq R}.
}
\]

No rank-zero new triple occurs.

### Proof

The physical cell set of `Q_R` is the disjoint union of the fixed cells `O` and the
response cells `R`.  Thus `U subseteq Q_R` exactly when every cell of `U\setminus
O` lies in `R`.  If `U\setminus O` is incompatible or uses a forbidden edge, this
is impossible.  A rank-zero triple would lie wholly in the unchanged opposite
layer and would already belong to `mathcal T(S)`. ∎

Hence every possible new triple appears once, under its exact residual
prescription.

## 5. Expected collateral bound

Define the normalized collateral score

\[
\mathcal C(S;O,F)
=
\frac{V_1}{n}
+
\frac{V_2}{(n)_2}
+
\frac{V_3}{(n)_3}.
\]

### Theorem CMR1202 -- PROVED

For the uniform response bank,

\[
\boxed{
\mathbb E_{R\in\mathcal B}
|\mathcal T(Q_R)\setminus\mathcal T(S)|
\le
\kappa_n\,\mathcal C(S;O,F)
\le
16\,\mathcal C(S;O,F).
}
\]

The exact expectation is

\[
\sum_{r=1}^{3}
\sum_{U\in\mathcal V_r}
\frac{|\operatorname{PM}(G/P_U)|}{|\operatorname{PM}(G)|}.
\]

### Proof

Average the exact identity of CMR1201 and apply CMR1200 to every prescription. ∎

The exact permanent ratios may be used in finite or low-side calculations instead
of the universal factor `kappa_n`.

## 6. Guaranteed destroyed load

Let

\[
D_S(e)
=
|\{T\in\mathcal T(S):e\in T\}|.
\]

### Theorem CMR1203 -- PROVED

Every response state `Q_R` destroys all `D_S(e)` old targets containing `e`:

\[
\boxed{
|\mathcal T(S)\setminus\mathcal T(Q_R)|
\ge D_S(e).
}
\]

### Proof

The matching `F` contains `e`, so every response matching in `G` omits `e`.  The
opposite layer also omits `e`.  Hence the physical cell `e` is absent from `Q_R`,
and no old triple containing it survives. ∎

Additional old triples may also be destroyed.

## 7. One-bank strict-improvement criterion

### Theorem CMR1204 -- PROVED

If

\[
\boxed{
\kappa_n\,\mathcal C(S;O,F)<D_S(e),
}
\]

then some response state satisfies

\[
\boxed{
\Phi(Q_R)<\Phi(S).
}
\]

The simpler sufficient condition

\[
16\,\mathcal C(S;O,F)<D_S(e)
\]

is valid uniformly for `n>=4`.

### Proof

For every response,

\[
\Phi(Q_R)-\Phi(S)
=N(R)-L(R).
\]

CMR1202 bounds `E N(R)` above by `kappa_n mathcal C`, while CMR1203 bounds
`L(R)` below by `D_S(e)` pointwise.  The displayed hypothesis makes the average
potential change negative, so one summand is negative. ∎

This is an actual target-versus-collateral theorem, not merely finite scheduler
termination.

## 8. Positive minima satisfy a collateral barrier

### Corollary CMR1205 -- PROVED

If `S` is a minimum-potential state in the current complete response cylinder,
then for every selected target cell `e`, every opposite layer `O`, and every
disjoint forbidden extension `F` containing `e`,

\[
\boxed{
D_S(e)
\le
\kappa_n\,\mathcal C(S;O,F).
}
\]

Therefore a positive minimum can persist only when each fixed-target bank carries
normalized collateral at least its destroyed target load divided by `kappa_n`.

### Proof

Otherwise CMR1204 would produce a state of smaller potential in the same response
cylinder. ∎

This does not prove minimum zero.  It converts the open CMR1196 inequality into an
explicit finite geometric score for one canonical bank.  Disjoint-extension
existence, permanent lower bounds, prescription probabilities, exact collateral
classification, and the improvement criterion are checked in
[`scripts/verify_prime_power_degree_two_bank_collateral.py`](../scripts/verify_prime_power_degree_two_bank_collateral.py).
