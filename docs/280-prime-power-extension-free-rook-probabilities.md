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

### Theorem CMR1414 -- PROVED

The residual forbidden board has rook numbers

\[
\boxed{r_j(P)=\binom qj+\varepsilon(P)\binom{q-d}{j-1}.}
\]

### Proof

Either omit the surviving off-diagonal forbidden edge and choose `j` diagonal
cells, or use it and choose `j-1` from the `q-d` nonadjacent diagonals. ∎

### Theorem CMR1415 -- PROVED

\[
\boxed{
B_n(P)=
\sum_{j=0}^{n-r}(-1)^j
\left[\binom qj+\varepsilon\binom{q-d}{j-1}\right](n-r-j)!.
}
\]

### Proof

Apply rook-polynomial inclusion--exclusion after contracting `P`. ∎

### Corollary CMR1416 -- PROVED

For uniform `R in PM(H_e)`,

\[
\boxed{
\Pr(P\subseteq R)=
\frac{B_n(P)}{D_n(n-2)/(n-1)}.
}
\]

The value depends only on `(n,r,q,d,epsilon)`.

### Theorem CMR1417 -- PROVED

For fixed `n,r`, there are at most

\[
\boxed{6(n-r+1)}
\]

exact probability classes.

### Theorem CMR1418 -- PROVED

For ranks one through three, the exact values obey

\[
\Pr(P\subseteq R)\le\frac1{n-2}
\quad(r=1),
\]

and

\[
\Pr(P\subseteq R)\le\frac{\lambda_n}{(n)_r}
\quad(r=2,3).
\]

### Theorem CMR1419 -- PROVED

If `V^e_{r,q,d,epsilon}` counts genuinely new candidate triples in one rook
class, then

\[
\boxed{
\mathbb E N(R)=
\sum_{r=1}^3\sum_{q,d,\varepsilon}
V^e_{r,q,d,\varepsilon}
\frac{B_n(r,q,d,\varepsilon)}{D_n(n-2)/(n-1)}.
}
\]

### Theorem CMR1420 -- PROVED

For unavailable allowed edges `U`,

\[
\boxed{\mathbb E|R\cap U|=\sum_{a\in U}p_e(a).}
\]

Hence

\[
\mathbb E N(R)+(\Phi(S)+1)\sum_{a\in U}p_e(a)<D_S(e)
\]

forces a host-feasible strict improvement.

### Corollary CMR1421 -- PROVED

Every extension-free collateral prescription has an exact closed probability
in a linear-size rank table.  Expected collateral and unavailable-edge use are
exact rook-class dot products.  The remaining work is geometric combination
across shared response edges, inherited lines, primitive heights, prefixes and
carry classes.  No all-`n` theorem is claimed.

Checked by
[`scripts/verify_prime_power_extension_free_rook_probabilities.py`](../scripts/verify_prime_power_extension_free_rook_probabilities.py).
