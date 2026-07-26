# Exact rook formulas for extension-free prescription probabilities

The authoritative range begins at CMR1414 because CMR1374--CMR1413 was
occupied concurrently by a different theorem chain.

Relabel the opposite matching `O` as the identity and the deleted target edge
as `e=(0,1)`.  Fix a compatible rank-`r` prescription `P`, disjoint from `O`
and not containing `e`.  Let `R(P)` and `C(P)` be its used row and column sets.
Define

\[
q(P)=|\{i:i\notin R(P),\ i\notin C(P)\}|,
\]

\[
\varepsilon(P)=
\mathbf 1_{\{0\notin R(P),\ 1\notin C(P)\}},
\]

and, when `epsilon(P)=1`,

\[
d(P)=
\mathbf 1_{\{0\notin R(P),\ 0\notin C(P)\}}
+
\mathbf 1_{\{1\notin R(P),\ 1\notin C(P)\}}.
\]

Set `d(P)=0` when `epsilon(P)=0`.

## Residual rook numbers

### Theorem CMR1414 -- PROVED

After contracting `P`, the residual forbidden board consists of `q=q(P)`
disjoint diagonal cells and, when `epsilon=1`, one extra off-diagonal cell
meeting exactly `d=d(P)` diagonal cells.  Its nonattacking `j`-rook number is

\[
\boxed{
r_j(P)=\binom qj+\varepsilon(P)\binom{q-d}{j-1}.
}
\]

### Proof

A forbidden rook set either omits the extra edge and chooses `j` diagonal
cells, or contains it and chooses `j-1` cells from the `q-d` nonadjacent
diagonal cells. ∎

## Exact completion count

### Theorem CMR1415 -- PROVED

Let

\[
B_n(P)=|\{R\in\operatorname{PM}(H_e):P\subseteq R\}|.
\]

Then

\[
\boxed{
B_n(P)=
\sum_{j=0}^{n-r}(-1)^j
\left[
\binom qj+\varepsilon\binom{q-d}{j-1}
\right](n-r-j)!.
}
\]

### Proof

Apply rook-polynomial inclusion--exclusion to the residual forbidden board of
CMR1414. ∎

## Exact prescription probability

### Corollary CMR1416 -- PROVED

Using the exact extension-free bank size

\[
|\operatorname{PM}(H_e)|=D_n\frac{n-2}{n-1},
\]

one has

\[
\boxed{
\Pr(P\subseteq R)=
\frac{B_n(P)}{D_n(n-2)/(n-1)}.
}
\]

The probability depends only on

\[
\boxed{(n,r,q(P),d(P),\varepsilon(P)).}
\]

## Finite probability classes

### Theorem CMR1417 -- PROVED

For fixed `n` and `r`, all compatible prescriptions occupy at most

\[
\boxed{6(n-r+1)}
\]

exact probability classes.

### Proof

There are at most `n-r+1` values of `q`, two values of `epsilon`, and three
values of `d`; empty classes are omitted. ∎

## Universal bounds remain valid

### Theorem CMR1418 -- PROVED

For ranks one through three, the exact probability satisfies

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

The exact numerator is bounded by the earlier rank-one marginal theorem and by
`(n-r)!` unrestricted completions for ranks two and three. ∎

## Exact expected collateral

For a target bank through `e`, let `V^e_{r,q,d,epsilon}` count genuinely new
physical triples in the corresponding rook class.

### Theorem CMR1419 -- PROVED

\[
\boxed{
\mathbb E N(R)=
\sum_{r=1}^3\sum_{q,d,\varepsilon}
V^e_{r,q,d,\varepsilon}
\frac{B_n(r,q,d,\varepsilon)}{D_n(n-2)/(n-1)}.
}
\]

### Proof

A candidate triple occurs exactly when its residual prescription is contained
in the response matching.  Partition by rook class and use linearity of
expectation. ∎

## Exact unavailable-edge penalty

### Theorem CMR1420 -- PROVED

For any unavailable allowed-edge set `U`,

\[
\boxed{
\mathbb E|R\cap U|=\sum_{a\in U}p_e(a),
}
\]

where every `p_e(a)` is the exact rank-one rook probability.
Consequently, with `m=Phi(S)`, the inequality

\[
\mathbb E N(R)+(m+1)\sum_{a\in U}p_e(a)<D_S(e)
\]

forces a host-feasible response of potential below `m`.

### Proof

Use indicator linearity and the standard `(m+1)` feasibility penalty. ∎

## Rook-probability endpoint

### Corollary CMR1421 -- PROVED

Every extension-free collateral prescription now has an exact closed
probability in a linear-size rank table.  Exact expected collateral and exact
unavailable-edge use are finite rook-class dot products.  The remaining
same-owner problem is geometric: combine these probabilities across shared
response edges, real lines, primitive heights, prefix cells and carry classes.
No all-`n` theorem is claimed.

Checked by
[`scripts/verify_prime_power_extension_free_rook_probabilities.py`](../scripts/verify_prime_power_extension_free_rook_probabilities.py).
