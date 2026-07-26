# Exact row-column cylinder types for extension-free target banks

CMR1358--CMR1373 use universal cylinder bounds in the extension-free bank

\[
\mathcal B_e=\operatorname{PM}(K_{n,n}\setminus(O\cup\{e\})).
\]

The remaining same-owner problem is sensitive to correlations between lines and
matching rows/columns.  This chapter keeps that information exactly.  After
normalising the fixed opposite matching `O` to the identity, every compatible
rank-one, rank-two or rank-three prescription has one of finitely many
row-column incidence types.  Inclusion--exclusion gives its exact number of
extensions in `B_e`.

All geometric cells retain their original parent-grid coordinates.  The
normalisation below is used only for counting perfect matchings.

## 1. Opposite-matching coordinates

For every target column `y`, let `iota_O(y)` be the unique row `x` with
`(x,y) in O`.  Replace a labelled cell `(x,y)` by

\[
\overline{(x,y)}=(x,\iota_O(y)).
\]

Then `O` becomes the identity matching.  Write the forbidden target edge as

\[
\bar e=(u,v),\qquad u\ne v.
\]

### Theorem CMR1374 -- PROVED

The column relabelling is a bijection between `B_e` and the permutations of
`[n]` which have no fixed point and do not use `(u,v)`.  It preserves
containment of every labelled prescription.

### Proof

A response avoids `O` exactly when its transformed permutation avoids every
identity cell.  It avoids `e` exactly when it avoids `(u,v)`.  Row and column
incidence and prescription containment are preserved by the bijection.  No
claim about geometric collinearity after relabelling is made. ∎

## 2. Residual incidence parameters

Let `P` be a compatible transformed prescription of rank `r`, disjoint from the
identity and from `(u,v)`.  Put

\[
R(P)=\{x:(x,y)\in P\},\qquad
C(P)=\{y:(x,y)\in P\},
\]

\[
t(P)=|R(P)\cap C(P)|,
\qquad
m=n-r,
\qquad
d=n-|R(P)\cup C(P)|=n-2r+t(P).
\]

The forbidden edge `(u,v)` remains after conditioning on `P` precisely when

\[
\varepsilon(P,e)=
\mathbf 1_{u\notin R(P),\ v\notin C(P)}.
\]

When `epsilon=1`, define

\[
c(P,e)=
\mathbf 1_{u\notin C(P)}+
\mathbf 1_{v\notin R(P)}.
\]

Thus `c` counts the residual identity cells `(u,u)` and `(v,v)` which conflict
with `(u,v)`.

### Theorem CMR1375 -- PROVED

After fixing `P`, the residual `m x m` board has exactly `d` forbidden identity
cells.  If `epsilon=1`, it also has the forbidden cell `(u,v)`, which is
compatible with exactly `d-c` of those identity cells.

### Proof

An identity cell `(i,i)` survives exactly when neither row `i` nor column `i`
is used by `P`, giving `d`.  The edge `(u,v)` survives exactly under the stated
row/column condition.  It conflicts only with `(u,u)` by row and `(v,v)` by
column, whenever those cells survive. ∎

## 3. Exact cylinder count

For integers `q>=0` and `0<=s<=q`, define

\[
A(q,s)=
\sum_{j=0}^{q-s}(-1)^j\binom{q-s}{j}(q-j)!.
\]

This counts permutations of `q` positions avoiding fixed points on `q-s`
prescribed diagonal cells; `s` diagonal positions are unrestricted.

### Theorem CMR1376 -- PROVED

Let

\[
\theta(P,e)=(r,t,\varepsilon,c).
\]

The exact number of response matchings containing `P` is

\[
\boxed{
\nu_n(r,t,\varepsilon,c)
=
A(n-r,r-t)
-
\varepsilon A(n-r-1,r-t+c-1).
}
\]

Consequently

\[
\boxed{
\Pr_{R\in\mathcal B_e}(P\subseteq R)
=
\frac{\nu_n(r,t,\varepsilon,c)}
{D_n(n-2)/(n-1)}.
}
\]

### Proof

Without using `(u,v)`, inclusion--exclusion over the `d` residual identity
cells gives

\[
\sum_{j=0}^{d}(-1)^j\binom dj(m-j)!
=A(m,m-d)=A(n-r,r-t).
\]

If `(u,v)` remains, subtract permutations which use it.  After fixing that
edge, `m-1` rows and columns remain, and only the `d-c` identity cells
compatible with it can also be imposed.  Their inclusion--exclusion count is

\[
A(m-1,(m-1)-(d-c))
=A(n-r-1,r-t+c-1).
\]

Divide by the exact bank size from CMR1358. ∎

## 4. Constant type stock

### Theorem CMR1377 -- PROVED

For residual ranks `r in {1,2,3}`, the probability of a prescription depends
only on

\[
(r,t,\varepsilon,c),
\qquad
0\le t\le r,
\quad
\varepsilon\in\{0,1\},
\quad
0\le c\le2.
\]

There are at most

\[
\boxed{72}
\]

formal types, independent of `n`; impossible parameter combinations are simply
absent.

### Proof

CMR1376 depends on `P` only through the four displayed parameters.  The crude
stock is

\[
\sum_{r=1}^3(r+1)\cdot2\cdot3=54,
\]

which is already at most 72.  The larger round number is retained to allow a
separate layer/owner bit in later quotient implementations. ∎

## 5. Exact new-collateral expectation

Fix an old state `S=O union M` and one target edge `e in M`.  Let `N_e` be the
set of physical collinear triples `T` such that

1. `T` is contained in `O union E(H_e)`;
2. `T` is not contained in `S`;
3. the residual prescription `P_T=T setminus O` is nonempty and matching-
   compatible.

For a geometric or credit class `gamma`, let

\[
H_e(\gamma;r,t,\varepsilon,c)
\]

count triples in `N_e` of class `gamma` whose transformed residual prescription
has the indicated cylinder type.

### Theorem CMR1378 -- PROVED

For uniform `R in B_e`, the exact expected number of new class-`gamma` credits
is

\[
\boxed{
\mathbb E N_\gamma(R)
=
\frac1{|\mathcal B_e|}
\sum_{r,t,\varepsilon,c}
H_e(\gamma;r,t,\varepsilon,c)
\nu_n(r,t,\varepsilon,c).
}
\]

In particular, summing over `gamma` gives the exact expected collateral, not an
upper bound.

### Proof

A candidate triple occurs exactly when its complete residual prescription is
contained in `R`.  CMR1376 gives that probability exactly.  Sum the indicators
and group by type and credit class. ∎

## 6. Exact surviving-old and destroyed-load rows

For an old target `T in T(S)`, put `P_T=T setminus O`.  A target wholly in `O`
survives every response.  If `P_T` contains `e`, its survival probability is
zero.  Otherwise transform `P_T` and use CMR1376.

### Theorem CMR1379 -- PROVED

The expected destroyed old load is exactly

\[
\boxed{
\mathbb E L(R)
=
\sum_{T\in\mathcal T(S),\ P_T\ne\varnothing}
\left(1-
\frac{\nu_n(P_T;e)}{|\mathcal B_e|}
\right),
}
\]

where `nu_n(P_T;e)=0` when `P_T` contains `e` or is unavailable.  Hence

\[
\mathbb E[\Phi(O\cup R)-\Phi(S)]
=
\mathbb E N(R)-\mathbb E L(R)
\]

is an exact rational quantity determined by finite cylinder-type histograms.

### Proof

Apply the same containment calculation to every old target residual
prescription.  Linearity of expectation and the exact new-minus-lost identity
complete the proof. ∎

## 7. Weighted offspring rows and upper quotients

Let `v_gamma>0` be any proposed coarse credit weights.

### Theorem CMR1380 -- PROVED

The uniform extension-free bank has exact expected new weight

\[
\boxed{
\frac1{|\mathcal B_e|}
\sum_{\gamma,r,t,\varepsilon,c}
 v_\gamma H_e(\gamma;r,t,\varepsilon,c)
 \nu_n(r,t,\varepsilon,c).
}
\]

Taking componentwise maxima of the histograms over one parent class gives an
honest host-uniform upper-quotient row in the sense of CMR1329.  After clearing
the bank denominator and the weights, every row is an exact integer
inequality.

### Proof

Multiply the exact class expectations of CMR1378 by `v_gamma` and sum.  Rowwise
histogram domination is exactly the upper-quotient argument of CMR1329, and all
cylinder counts are integers. ∎

## 8. Exact-cylinder endpoint

### Corollary CMR1381 -- PROVED

Extension-free same-owner offspring now admit a finite exact decomposition by

\[
\boxed{
(\text{geometric credit class},r,t,\varepsilon,c).
}
\]

This refinement:

1. preserves original real-line geometry;
2. retains exact response row/column correlation;
3. replaces the universal factor-four higher-rank estimate by exact rational
   cylinder probabilities;
4. computes both created and destroyed credit expectations;
5. supplies exact rational or integer upper-quotient rows.

It does not imply that the uniform extension-free law is subcritical.  The next
frontier is to choose a nonuniform or deterministic response policy using
cross-line edge assignment, primitive height, prefix and carry structure.

No all-`n` theorem is claimed.  The exact counts and histogram identities are
checked in
[`scripts/verify_prime_power_extension_free_exact_cylinders.py`](../scripts/verify_prime_power_extension_free_exact_cylinders.py).
