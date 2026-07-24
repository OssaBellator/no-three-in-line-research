# All-rank two-layer spread in a sparse block host

This note supplies an explicit sparse host for which the measure and
first-matching deletion obligations in SAS1--SAS4 can be completed
exactly.

Let \(N=bd\). Partition both vertex classes into \(b\) corresponding
blocks of size \(d\), and let

\[
G_{b,d}=\bigsqcup_{\ell=1}^b K_{d,d}.
\]

This is a balanced \(d\)-regular host. Taking \(b\to\infty\) allows
\(d=o(N)\). Perfect matchings factor independently across the blocks.

We use two elementary estimates. For \(0\leq r\leq d\),

\[
\boxed{(d)_r\geq(d/3)^r.}
\]

Indeed, the average of the largest \(r\) values among
\(\log1,\ldots,\log d\) is at least their overall average, while

\[
\frac{\log(d!)}d
\geq\frac1d\int_1^d\log x\,dx
\geq\log d-1>\log(d/3).
\]

Also, the derangement number \(!d\) satisfies

\[
\boxed{!d\geq d!/3\qquad(d\geq2).}
\]

This follows from the alternating expansion
\(!d/d!=\sum_{k=0}^d(-1)^k/k!\), whose odd partial sums from \(d=3\)
onward are at least \(1/3\), while even partial sums are larger.

## SAS1a -- first-layer all-rank spread

### Theorem SAS1a -- PROVED

Choose a uniform perfect matching independently in every \(K_{d,d}\)
block, and let \(M_1\) be their union. Then for every edge set \(F\),

\[
\boxed{
\Pr(F\subseteq M_1)\leq(3/d)^{|F|}.
}
\]

### Proof

If \(F\) is not a matching or uses an edge outside the host, its
probability is zero. Otherwise, let \(r_\ell\) be its rank in block
\(\ell\). A uniform block permutation contains those prescribed edges
with probability \(1/(d)_{r_\ell}\). Independence and the falling
factorial estimate give

\[
\Pr(F\subseteq M_1)
=\prod_\ell\frac1{(d)_{r_\ell}}
\leq
\prod_\ell(3/d)^{r_\ell}
=(3/d)^{|F|}.
\]

\(\square\)

## SAS4b -- residual derangement layer

Condition on \(M_1\). In each block, \(G_{b,d}-M_1\) is
\(K_{d,d}\) with one perfect matching deleted. Choose \(M_2\)
independently and uniformly from the derangements in each residual block.

### Theorem SAS4b -- PROVED

For every edge set \(F\subseteq E(G_{b,d})\setminus M_1\),

\[
\boxed{
\Pr(F\subseteq M_2\mid M_1)
\leq(9/d)^{|F|}.
}
\]

Consequently

\[
\boxed{
\Pr(F\subseteq M_1\cup M_2)
\leq(18/d)^{|F|}
}
\]

for every edge set \(F\), and \(M_1\cup M_2\) is a simple saturated
2-factor.

### Proof

In one residual block, suppose \(F\) prescribes \(r\geq1\) compatible
edges. There are at most \((d-r)!\) permutations extending them, while
the residual matching space has exactly \(!d\) states. Hence

\[
\Pr(F\text{ in the residual block}\mid M_1)
\leq
\frac{(d-r)!}{!d}
\leq
\frac3{(d)_r}
\leq
3(3/d)^r
\leq
(9/d)^r.
\]

The rank-zero factor equals one. Multiplication over independent blocks
proves the conditional all-rank bound.

The first layer also satisfies the weaker \((9/d)\)-spread bound. Apply
SAS4a with \(C=9\) to obtain \((18/d)\)-spread for the union.
The layers are edge-disjoint by construction, and each is perfect, so
their union is a simple graph of degree two at every vertex.
\(\square\)

## Exact scope

The block host completes the probability-measure, all-rank conditioning,
and first-layer deletion parts of SAS1--SAS4 for a concrete
\(d\)-regular sparse family. It deliberately does not claim the robust
small-set expansion suggested for connected algebraic hosts; block
factorization replaces that hypothesis here.

SAS5 remains open for this family. The candidate cells in the block host
may contain far more than \(O(d^3)\) real collinear triples, including
triples crossing different blocks. The theorem therefore supplies a
fully controlled sparse matching measure, not yet a no-three-in-line
endpoint.

`scripts/verify_sparse_block_host.py` exhaustively checks all first-layer
and residual derangement cylinders through block size six.
