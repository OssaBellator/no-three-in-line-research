# Exact rook formulas for extension-free prescription probabilities

CMR1358--CMR1373 use the extension-free bank

\[
H_e=K_{n,n}\setminus(O\cup\{e\})
\]

and bound compatible rank-two and rank-three prescriptions by the universal
factor `lambda_n/(n)_r`.  The exact probability depends on how the prescribed
edges meet the deleted target edge and the opposite permutation.  After
relabeling `O` as the identity and `e=(0,1)`, the residual forbidden board is a
partial identity matching plus at most one off-diagonal edge.  Its rook
polynomial is explicit.

Fix a compatible prescription `P` of rank `r`, disjoint from `O` and not
containing `e`.  Let `R(P)` and `C(P)` be its used source rows and target
columns.  Put

\[
q(P)=|\{i:i\notin R(P),\ i\notin C(P)\}|.
\]

Let

\[
\varepsilon(P)=
\mathbf 1_{\{0\notin R(P),\ 1\notin C(P)\}},
\]

so `epsilon(P)=1` exactly when the extra forbidden edge `e=(0,1)` survives
contraction.  When it survives, define

\[
d(P)=
\mathbf 1_{\{0\notin R(P),\ 0\notin C(P)\}}
+
\mathbf 1_{\{1\notin R(P),\ 1\notin C(P)\}}.
\]

Thus `d(P)` is the number, zero through two, of surviving diagonal forbidden
edges sharing an endpoint with `e`.

## Residual forbidden-board rook numbers

### Theorem CMR1374 -- PROVED

After fixing `P`, the residual forbidden board consists of `q=q(P)` pairwise
disjoint diagonal cells and, when `epsilon=1`, one extra cell meeting exactly
`d=d(P)` of those diagonal cells.  Its number of nonattacking `j`-rook subsets
is

\[
\boxed{
 r_j(P)=
 \binom qj
 +\varepsilon(P)\binom{q-d}{j-1},
}
\]

with the usual convention that an out-of-range binomial coefficient is zero.

### Proof

A nonattacking forbidden set either omits the extra edge, giving `binom(q,j)`
choices among the diagonal matching, or contains it.  In the latter case the
`d` adjacent diagonal edges are unavailable and the remaining `j-1` rooks are
chosen from `q-d` disjoint cells.  These cases are disjoint and exhaustive. ∎

## Exact number of bank completions

Let

\[
B_n(P)=|\{R\in\operatorname{PM}(H_e):P\subseteq R\}|.
\]

### Theorem CMR1375 -- PROVED

\[
\boxed{
B_n(P)=
\sum_{j=0}^{n-r}
(-1)^j
\left[
\binom qj+\varepsilon\binom{q-d}{j-1}
\right]
(n-r-j)!.
}
\]

### Proof

After contracting the compatible prescription, count permutations of the
remaining `n-r` rows and columns avoiding the residual forbidden board.
Rook-polynomial inclusion--exclusion gives the displayed sum, and CMR1374
supplies the rook numbers. ∎

This formula is valid for every rank, not only ranks one through three.

## Exact prescription probability

Recall from CMR1358 that

\[
|\operatorname{PM}(H_e)|=D_n\frac{n-2}{n-1}.
\]

### Corollary CMR1376 -- PROVED

For uniform `R` in the extension-free bank,

\[
\boxed{
\Pr(P\subseteq R)
=
\frac{B_n(P)}{D_n(n-2)/(n-1)}.
}
\]

The value depends only on

\[
\boxed{(n,r,q(P),d(P),\varepsilon(P)).}
\]

### Proof

Divide the exact completion count by the exact bank size.  The rook formula
contains no other data from `P`. ∎

## Finite probability classes

### Theorem CMR1377 -- PROVED

For fixed `n` and rank `r`, all compatible prescriptions fall into at most

\[
\boxed{6(n-r+1)}
\]

exact probability classes: `q` has at most `n-r+1` values,
`epsilon` has two values and `d` has three values.  Empty parameter classes are
simply omitted.

### Proof

Apply CMR1376 and count the possible parameter tuples. ∎

This replaces a prescription-by-prescription permanent computation by a
linear-size table for every rank.

## Relation to the universal bounds

### Theorem CMR1378 -- PROVED

For `r=1,2,3`, the exact value of CMR1376 obeys the previously proved bounds

\[
\Pr(P\subseteq R)\le\frac1{n-2}
\quad(r=1),
\]

and

\[
\Pr(P\subseteq R)\le\frac{\lambda_n}{(n)_r}
\quad(r=2,3).
\]

### Proof

The exact numerator counts a subfamily of the bank.  For rank one apply
CMR1360.  For ranks two and three, at most `(n-r)!` unrestricted permutations
contain `P`; dividing by the exact denominator gives CMR1361. ∎

The new formula may be strictly smaller because it retains all surviving
forbidden cells after contraction.

## Exact expected collateral by rook class

Let `V_{r,q,d,epsilon}^e` be the number of genuinely new physical collateral
triples whose residual prescription has rank `r` and the displayed rook
parameters relative to the target bank through `e`.

### Theorem CMR1379 -- PROVED

For the uniform extension-free response,

\[
\boxed{
\mathbb E N(R)
=
\sum_{r=1}^3
\sum_{q,d,\varepsilon}
V_{r,q,d,\varepsilon}^e
\frac{B_n(r,q,d,\varepsilon)}{D_n(n-2)/(n-1)}.
}
\]

Here `B_n(r,q,d,epsilon)` denotes the finite alternating sum in CMR1375.

### Proof

Each genuinely new candidate triple occurs exactly when its residual
prescription is contained in the response matching.  Partition the candidates
by their exact rook class and use linearity of expectation. ∎

Unlike CMR1362, this is an equality rather than an upper bound.

## Restricted-host penalty with exact marginals

Let `U` be any set of unavailable allowed response edges.  For each edge `a`,
use its exact rank-one rook probability `p_e(a)` from CMR1376.

### Theorem CMR1380 -- PROVED

\[
\boxed{
\mathbb E|R\cap U|=\sum_{a\in U}p_e(a).
}
\]

Consequently, with `m=Phi(S)`, if

\[
\mathbb E N(R)
+(m+1)\sum_{a\in U}p_e(a)
<D_S(e),
\]

then some response is host-feasible and has potential below `m`.

### Proof

The first identity is linearity of expectation.  Add the standard
`(m+1)` feasibility penalty.  Any response using an unavailable edge has
penalized score at least one, while a negative penalized expectation forces a
feasible response with negative new-minus-destroyed score. ∎

## Rook-probability endpoint

### Corollary CMR1381 -- PROVED

For every extension-free target bank:

1. every rank-one, rank-two and rank-three collateral prescription has an exact
   closed probability;
2. the probability has only the five parameters `(n,r,q,d,epsilon)`;
3. exact expected collateral is a finite rook-class dot product;
4. unavailable-edge use has an exact marginal sum;
5. the universal constants `1/(n-2)` and `lambda_n/(n)_r` are honest relaxations
   of this table.

The remaining same-owner problem is no longer missing prescription
probabilities.  It is to combine these exact rook classes across many real
lines and target cells using shared-edge assignment, primitive height,
prefix/carry structure or a subcritical upper-quotient weight.  No all-`n`
theorem is claimed.

The formulas are checked in
[`scripts/verify_prime_power_extension_free_rook_probabilities.py`](../scripts/verify_prime_power_extension_free_rook_probabilities.py).
