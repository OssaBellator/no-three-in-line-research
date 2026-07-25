# Geometric obstruction for consecutive sparse blocks

SAS1a and SAS4b solve the matching-measure problem on a disjoint union of
complete \(d\times d\) blocks. This note shows that the natural
consecutive grid embedding of that host cannot also satisfy the global
SAS5 triple threshold.

Let \(N=bd\). Partition the row and column coordinates into consecutive
intervals

\[
R_\ell=\{r_\ell,\ldots,r_\ell+d-1\},
\qquad
C_\ell=\{c_\ell,\ldots,c_\ell+d-1\},
\]

and place one complete bipartite block on \(R_\ell\times C_\ell\) for
each \(\ell\). The intervals may be paired in any order.

## SAS5b -- consecutive-block triple lower bound

### Proposition SAS5b -- PROVED

For \(d\geq3\), the number \(T(G_{b,d})\) of compatible real collinear
candidate triples satisfies

\[
\boxed{
T(G_{b,d})
\geq
b\binom d3
=
\frac{N(d-1)(d-2)}6.
}
\]

Consequently, for every family with \(d=o(N)\) and \(d\geq3\),

\[
\frac{T(G_{b,d})}{d^3}
\geq
\frac{N}{6d}
\left(1-\frac1d\right)
\left(1-\frac2d\right)
\longrightarrow\infty.
\]

Thus no fixed constant \(c>0\) can make the SAS5 global condition
\(T(G)<c d^3\) hold eventually for these consecutively embedded block
hosts.

### Proof

Inside block \(\ell\), consider

\[
D_\ell
=
\{(r_\ell+t,c_\ell+t):0\leq t<d\}.
\]

These \(d\) cells lie on the real line

\[
y-x=c_\ell-r_\ell.
\]

Every three distinct cells of \(D_\ell\) have distinct rows and distinct
columns, so they form a compatible forbidden partial matching of rank
three. This gives \(\binom d3\) distinct triples per block. Blocks have
disjoint cell sets, so the triples counted in different blocks are
distinct, proving the first box.

Dividing by \(d^3\) and using \(N=bd\) gives the displayed ratio. Since
\(d=o(N)\), its first factor \(N/d\) diverges; the other two factors are
positive for \(d\geq3\) and tend to one when \(d\) grows. If \(d\) stays
bounded above three, they instead stay bounded away from zero. \(\square\)

## Consequence for the sparse track

The abstract block product remains a valid all-rank spread construction,
but its consecutive geometric realization is not a candidate for the
global-conflict endpoint SAS5a. A successful continuation must change at
least one of:

- the embedding, using nonconsecutive coordinate sets with a proved
  triple bound;
- the host, replacing complete blocks by a geometrically sparse
  algebraic graph while preserving switching spread; or
- the endpoint, using a local resampling theorem that does not require
  \(T(G)=O(d^3)\).

`scripts/verify_sparse_block_geometry.py` constructs the local diagonals
and checks the exact lower-bound count on small block systems.
