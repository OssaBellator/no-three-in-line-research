# Zero-conflict embedding of the complete sparse block host

SAS5d eliminates internal triples one block at a time but does not
coordinate different blocks.  If a polynomially expanded column range
is allowed, a direct greedy embedding eliminates **all** compatible
collinear triples of the block host, including cross-block triples.

Let \(N=bd\), partition \(N\) distinct integer row coordinates into

\[
R_1\sqcup\cdots\sqcup R_b,
\qquad |R_\ell|=d,
\]

and seek pairwise disjoint \(d\)-element column sets \(C_\ell\).  The
abstract host is

\[
G=\bigsqcup_{\ell=1}^b R_\ell\times C_\ell.
\]

A geometric conflict is a collinear triple of host cells using three
distinct rows and three distinct columns.

## SAS5e -- expanded-grid zero-conflict embedding

### Theorem SAS5e -- PROVED

There are disjoint integer column sets \(C_1,\ldots,C_b\), each of size
\(d\), for which

\[
\boxed{T(G)=0.}
\]

They may be chosen inside

\[
\boxed{
[0,M_{N,d}],
\qquad
M_{N,d}
=
N-1+d\sum_{k=0}^{N-1}\binom{kd}{2}
=O(d^3N^3).
}
\]

Thus the entire sparse complete-block matching host has a compatible
triple-free embedding in a polynomially expanded rectangular grid.

### Greedy construction

Choose an ordering of \(N\) block labels in which every
\(\ell\in\{1,\ldots,b\}\) occurs exactly \(d\) times.  At step \(k\),
\(k\) columns have been installed and the host contains exactly \(kd\)
cells.

Suppose the next label is \(\ell\).  For each \(r\in R_\ell\) and each
pair of existing cells, forbid the unique real column coordinate \(c\),
when it exists, for which the new cell \((r,c)\) is collinear with that
pair.  There are at most

\[
d\binom{kd}{2}
\]

forbidden values.  Choose the first integer larger than the previous
column coordinate which is not forbidden, assign it to \(C_\ell\), and
install all \(d\) cells in \(R_\ell\times\{c\}\).

### Proof

At step \(k\), each choice of a new row and an existing cell pair
determines at most one point on their line, so the stated forbidden-value
bound holds.  Among the next

\[
d\binom{kd}{2}+1
\]

integers at least one is available.  Starting with previous coordinate
\(-1\) and summing these gap bounds for \(k=0,\ldots,N-1\) gives
\(M_{N,d}\).

Suppose a compatible collinear triple existed after the construction.
Its three column coordinates are distinct, so consider the cell in its
latest-installed column.  The other two cells were already present when
that column was chosen.  The new cell's row together with that existing
pair made its column coordinate one of the forbidden values, a
contradiction.  Triples containing two cells installed in the same step
use the same column and are not compatible.  Hence \(T(G)=0\).
\(\square\)

## Exact endpoint and remaining compression wall

For \(d\ge2\), combine SAS5e with the product matching measure SAS1a and
the residual derangement layer SAS4b.  Every two-layer outcome is a
simple saturated \(2\)-factor, and because the host itself has no
compatible collinear triple, every outcome is no-three-in-line in the
expanded embedding.  No probabilistic conflict estimate is needed.

This is not yet the standard \(N\times N\) endpoint.  The construction
uses \(N\) column vertices but their integer coordinates may range up to
\(M_{N,d}\).  Relabelling them by \(0,\ldots,N-1\) need not preserve
collinearity.  The complete block model's remaining SAS5 obstruction is
therefore a precise **coordinate-compression problem**: realize the same
zero- or low-conflict geometry in an \(N\)-sized coordinate interval,
or replace it by a host stable under such compression.

`scripts/verify_sparse_expanded_grid.py` runs the construction on
consecutive, interlaced, and nonuniform small row blocks, checks the
coordinate bound, and directly enumerates every compatible host triple.
