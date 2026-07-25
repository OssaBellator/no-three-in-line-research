# Optimal rollback states have sparse balanced level skeletons

CMR453--CMR461 factor the minimum rollback face into strongly connected blocks
and sharpen the shortest-path potential range to `[-k,0]`, where
`k=\kappa(e)` is the minimum rollback cost. This chapter uses the potential
more directly. Every optimum defines a permutation of the base matching
vertices. Tightness says that each permutation arrow changes potential by
`-1`, `0`, or `1`.

Because the permutation preserves every level-prefix cardinality, upward and
downward arrows balance across every adjacent level cut. Upward arrows are
restored edges, so there can be at most `k` of them. Hence every minimum
rollback state has a cross-level skeleton of at most `2k` edges. Once that
skeleton is fixed, all remaining choices factor independently inside the
potential levels.

Use the binary-cost notation of CMR448--CMR461. Let

\[
M=\{m_j=\ell_jr_j:1\le j\le t\}
\]

be a minimum-cost perfect matching of cost

\[
k=c(M),
\]

and let `A` be the optimal-allowed core of CMR455. Choose an integral tight
potential

\[
\phi:[t]\to\{-k,-k+1,\ldots,0\}.
\]

For another optimum `N`, write

\[
N=\{\ell_jr_{\sigma(j)}:1\le j\le t\}
\]

relative to the right endpoints of `M`. Thus `\sigma` is a permutation. Since
all edges of `A` are tight,

\[
\phi(\sigma(j))-\phi(j)
=
c(\ell_jr_{\sigma(j)})-c(m_{\sigma(j)})
\in\{-1,0,1\}.
\]

## 1. Exact level-cut conservation

For `-k\le r<0`, let

\[
U_r(N)
=
|\{j:\phi(j)=r,\ \phi(\sigma(j))=r+1\}|,
\]

and

\[
D_r(N)
=
|\{j:\phi(j)=r+1,\ \phi(\sigma(j))=r\}|.
\]

### Theorem CMR462 — PROVED

For every optimum `N` and every adjacent level cut,

\[
\boxed{U_r(N)=D_r(N).}
\]

Consequently, if

\[
U(N)=\sum_rU_r(N),
\qquad
D(N)=\sum_rD_r(N),
\]

then

\[
\boxed{U(N)=D(N).}
\]

### Proof

Put

\[
S_r=\{j:\phi(j)\le r\}.
\]

Because `\sigma` is a permutation, the number of arrows leaving `S_r` equals
the number entering `S_r`. A tight arrow changes level by at most one, so the
only arrows leaving are those counted by `U_r(N)` and the only arrows entering
are those counted by `D_r(N)`. Hence the two counts are equal. Sum over `r`.
∎

This is an exact circulation law for the rollback potential.

## 2. Sparse cross-level support

Call an edge of `N` **cross-level** when

\[
\phi(\sigma(j))\ne\phi(j).
\]

### Corollary CMR463 — PROVED

Every minimum rollback matching satisfies

\[
\boxed{U(N)=D(N)\le k}
\]

and therefore has at most

\[
\boxed{2k}
\]

cross-level edges.

More precisely, every upward edge is a marked edge replacing an unmarked base
edge, while every downward edge is an unmarked edge replacing a marked base
edge.

### Proof

For an upward edge the tight level equation has value `+1`, so

\[
c(\ell_jr_{\sigma(j)})=1,
\qquad
c(m_{\sigma(j)})=0.
\]

Thus every upward edge is one of the exactly `k` marked edges used by `N`, and
`U(N)\le k`. CMR462 gives `D(N)=U(N)`. The downward description follows from
the level equation `-1`. ∎

Thus all but at most `2k` edges of every optimum stay inside one potential
level.

## 3. Balanced level residuals

For a level `s`, let

\[
V_s=\{j:\phi(j)=s\}.
\]

For an optimum `N`, let `O_s(N)` be the source vertices of level `s` used by
cross-level edges, and let `I_s(N)` be the target indices of level `s` reached
by cross-level edges.

### Theorem CMR464 — PROVED

For every level `s`,

\[
\boxed{|O_s(N)|=|I_s(N)|.}
\]

After deleting those source and target indices, the level-preserving edges of
`N` form a perfect matching

\[
V_s\setminus O_s(N)
\longrightarrow
V_s\setminus I_s(N).
\]

### Proof

The outgoing cross-level count at level `s` is

\[
U_s(N)+D_{s-1}(N),
\]

with nonexistent boundary terms interpreted as zero. The incoming count is

\[
D_s(N)+U_{s-1}(N).
\]

CMR462 equates the corresponding terms, so the counts are equal. Every source
and target index is used once by the permutation `\sigma`; after removing the
cross-level incidences, the remaining arrows at level `s` therefore form a
bijection between the displayed residual sets. ∎

## 4. Exact factorization conditional on the skeleton

Let `A_s` be the same-level part of the optimal-allowed core between
`\{\ell_j:j\in V_s\}` and `\{r_j:j\in V_s\}`. A **feasible level skeleton** is
a partial matching `S` of cross-level edges of `A` such that

1. every edge changes level by exactly one;
2. every level has equally many source and target endpoints in `S`;
3. for every level `s`, the residual graph
   \[
   A_s-(O_s(S)\cup I_s(S))
   \]
   has a perfect matching.

### Theorem CMR465 — PROVED

The optimum family is the disjoint union

\[
\boxed{
\operatorname{PM}(A)
\cong
\bigsqcup_{S\in\mathfrak S}
\left(
\{S\}
\times
\prod_s
\operatorname{PM}
\bigl(A_s-(O_s(S)\cup I_s(S))\bigr)
\right),
}
\]

where `\mathfrak S` is the family of feasible level skeletons. Every skeleton
has even size at most `2k`.

### Proof

Given an optimum `N`, take its cross-level edges as `S`. CMR463 gives the size
bound and CMR464 gives the residual perfect matchings, so `N` appears on the
right-hand side.

Conversely, combine a feasible skeleton with one residual perfect matching in
each level. The endpoint-balance condition makes the union a global perfect
matching of `A`. By CMR455 every perfect matching of `A` is minimum cost. The
cross-level edge set is uniquely recoverable, so the union is disjoint. ∎

This is an exact state-space decomposition, not only a counting bound.

## 5. Finite skeleton count and repeated-slot transfer

### Corollary CMR466 — PROVED

The number of feasible cross-level skeletons satisfies

\[
\boxed{
|\mathfrak S|
\le
\sum_{u=0}^{k}t^{4u}
\le
(k+1)t^{4k}.
}
\]

The same bound and factorization hold for every binary marked-edge problem of
CMR461, including one compatible recursive ancestor-return slot after hard
constraints are encoded as host deletions.

Hence a minimum-marked state is determined by

1. one of at most `(k+1)t^{4k}` sparse balanced cross-level skeletons; and
2. independent zero-cost perfect matchings inside the residual level hosts.

### Proof

A skeleton has `2u` cross-level edges for some `0\le u\le k`. Each edge has at
most `t^2` choices, so the number with `2u` edges is at most `t^{4u}`. Sum over
`u`. The transfer follows by applying the proof to the binary cost `1_B` from
CMR461. ∎

The estimate deliberately overcounts; its role is to isolate the only
potentially unbounded motion inside the same-level residual hosts.

## 6. Revised frontier

The rollback and repeated-ancestor problems now have a common exact normal
form.

- Positive marked-cost excursions are removed by minimum-cost normalization.
- SCC factorization localizes marked dependence to at most `k` active blocks.
- Every optimum has at most `2k` cross-level edges.
- Conditional on that sparse skeleton, all remaining choices factor by
  potential level.

The active frontier is therefore no longer arbitrary movement in a layered
host. It is zero-cost movement inside one same-level residual host. The next
geometric theorem should show that a large such host yields a Hall/prefix/
line-clean continuation or p-adic, quotient, primitive-height, carry, reserve,
or envelope concentration. If every residual level host is small, CMR465 is a
strict product decomposition into lower-dimensional matching problems.

No all-`n` theorem is claimed here. Cut conservation, sparse support, exact
conditional products, and exhaustive small binary-cost instances are checked in
[`scripts/verify_prime_power_rollback_level_skeleton.py`](../scripts/verify_prime_power_rollback_level_skeleton.py).
