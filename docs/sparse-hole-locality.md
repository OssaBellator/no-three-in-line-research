# Remote-cylinder locality for arbitrary sparse host holes

SRR2a computes matching cylinders when the missing cells form a partial
matching.  The same locality estimate does not require that geometry:
rook numbers give the exact correction for an arbitrary sparse set of
holes.

Let

\[
G_Q=K_{N,N}\setminus Q,
\qquad |Q|=t,
\]

where \(Q\) is any set of missing cells, and let \(\mu_Q\) be uniform on
the perfect matchings of \(G_Q\).  For a host-valid partial matching
\(E\) of rank \(s\), let \(Q_E\) be the bipartite graph of missing cells
whose row and column are both unused by \(E\).  Write \(r_j(Q_E)\) for
the number of rank-\(j\) matchings in \(Q_E\), with \(r_0(Q_E)=1\).

## SRR2b -- sparse-hole cylinder locality

### Theorem SRR2b -- PROVED

The number of host perfect matchings extending \(E\) is

\[
\boxed{
Z_Q(E)
=
\sum_{j\geq0}
(-1)^j r_j(Q_E)(N-s-j)!.
}
\]

Equivalently,

\[
Z_Q(E)=(N-s)!\,\alpha_Q(E),
\]

where, whenever \(N-s>t\),

\[
\boxed{
1-\frac{t}{N-s}
\leq
\alpha_Q(E)
\leq1.
}
\]

Let \(F,B\) be compatible host-valid partial matchings of ranks \(f,b\)
with disjoint row and column sets.  If \(N-f>t\) and \(N-b>t\), then

\[
\boxed{
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
\leq
\frac{(N)_b}{(N-f)_b}
\frac1{
\left(1-\frac{t}{N-f}\right)
\left(1-\frac{t}{N-b}\right)
}.
}
\]

For fixed \(f,b\) and an arbitrary missing set of size \(t=o(N)\), the
right side is \(1+o(1)\).

### Proof

After fixing \(E\), a set of missing cells can occur in one completion
exactly when it is a matching in \(Q_E\).  A rank-\(j\) missing
matching is contained in \((N-s-j)!\) completions.  Inclusion--exclusion
over all missing cells therefore groups by rook rank and gives the first
box.

After normalization, \(\alpha_Q(E)\) is the probability that a uniform
permutation between the \(N-s\) unused rows and columns avoids \(Q_E\).
Every surviving missing cell occurs with probability \(1/(N-s)\).
There are at most \(t\) of them, so the union bound gives the lower
estimate; the upper estimate is immediate.

For disjoint compatible cylinders,

\[
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
=
\frac{Z_Q(F\cup B)Z_Q(\varnothing)}
{Z_Q(F)Z_Q(B)}.
\]

Substitution gives

\[
\frac{(N)_b}{(N-f)_b}
\frac{\alpha_Q(F\cup B)\alpha_Q(\varnothing)}
{\alpha_Q(F)\alpha_Q(B)}.
\]

Bound the numerator factors by one and use the two lower bounds in the
denominator. \(\square\)

## Stationary resampling consequence

Every vertex of \(G_Q\) has degree at least \(N-t\).  SRR1d therefore
gives at least

\[
\boxed{N-2t-1}
\]

one-layer four-cycle partners for every distinguished present edge.
When this is positive, its exact uniform-stationary flaw-removal kernel
applies.  The switch cannot create a vertex-disjoint remote cylinder
pathwise, and SRR2b supplies its \(1+o(1)\) conditional inflation.

Thus all five one-layer SRR1 properties hold for **every** missing-cell
set of sublinear cardinality, not only a deleted matching.  Likewise
SRR3f supplies at least \(N-2t-3\) stationary choices in the two-layer
space when it is nonempty.  The remaining two-layer difficulty is the
remote correlation created by conditioning on the edge-disjoint second
matching.

This theorem concerns a sublinear *total number* of holes.  A genuinely
superregular host may have \(\Theta(N^2)\) missing cells, so SRR2b does
not complete SRR2--SRR4; it removes arbitrary sparse-hole geometry from
the unresolved range.

`scripts/verify_sparse_hole_locality.py` enumerates every set of at most
three holes in \(K_{4,4}\), checks the rook-polynomial extension counts,
the union-bound correction, all eligible rank-at-most-two remote
cylinders, and the stationary switching lower bound.
