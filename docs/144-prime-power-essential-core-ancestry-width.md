# The essential core gives a polynomial ancestry-width bound

CMR426--CMR428 reduce harmonic-packet scheduling to one terminal fully forced
certificate. CMR217 attaches each essential edge of that certificate to the
deletion at which it first became essential. The remaining concern is the width
of the resulting ancestry ledger.

At the level relevant to matching feasibility, this width is automatically
polynomial. Essential edges in a matchable bipartite host form a matching, and
essentiality is monotone under later matchability-preserving deletions. Hence the
entire deletion pass has a final essential core of at most `t` edges. Every
fully forced rank-`1/2/3` certificate is a subset of that core.

Certificates with the same prescribed edge set are identified in this chapter.
Geometric labels may decorate such a node, but they do not create a new matching
dependency or a new CMR217 exchange link.

Let

\[
G_0\supseteq G_1\supseteq\cdots\supseteq G_d
\]

be a balanced bipartite deletion pass with `t` vertices on each side and at
least one perfect matching in every `G_i`. Write

\[
\operatorname{Ess}(G)
=
\{e\in E(G):e\text{ belongs to every perfect matching of }G\}.
\]

## 1. Essential edges form a matching

### Theorem CMR429 — PROVED

For every matchable balanced bipartite graph `G`, the set

\[
\operatorname{Ess}(G)
\]

is itself a matching. Consequently,

\[
\boxed{
|\operatorname{Ess}(G)|\le t.
}
\]

### Proof

If two distinct essential edges shared a left or right endpoint, no perfect
matching could contain both. But every perfect matching must contain every
essential edge, a contradiction. Therefore essential edges are pairwise
vertex-disjoint. ∎

## 2. The final essential core

Assume `G_0` has no essential edge, as in the half-degree host of CMR212. Put

\[
E_i
=
\operatorname{Ess}(G_i)\setminus\operatorname{Ess}(G_{i-1}),
\qquad
1\le i\le d,
\]

and let

\[
E_*
=
\operatorname{Ess}(G_d).
\]

### Theorem CMR430 — PROVED

The essential sets are monotone:

\[
\operatorname{Ess}(G_0)
\subseteq
\operatorname{Ess}(G_1)
\subseteq\cdots\subseteq
\operatorname{Ess}(G_d).
\]

The first-essentiality layers `E_i` are pairwise disjoint and partition `E_*`:

\[
\boxed{
E_*
=
\bigsqcup_{i=1}^d E_i.
}
\]

In particular,

\[
\boxed{
\sum_{i=1}^d|E_i|
=
|E_*|
\le t.
}
\]

### Proof

CMR426 proves monotonicity. An essential edge cannot be deleted while preserving
a perfect matching, so every edge remains present after its first-essentiality
time. The set difference layers are therefore disjoint and their union is the
final essential set. Apply CMR429. ∎

Thus only `t` distinct edges can ever acquire a CMR217 first-essentiality link
throughout the entire pass.

## 3. Forced certificate and link counts

A fully forced rank-`r` certificate, with `1\le r\le3`, has every prescribed
edge in `E_*`. After deduplication by prescribed edge set, define

\[
S_3(t)
=
\binom t1+
\binom t2+
\binom t3
\]

and

\[
L_3(t)
=
\binom t1+
2\binom t2+
3\binom t3.
\]

### Theorem CMR431 — PROVED

The number of distinct fully forced rank-`1/2/3` prescribed edge sets in one
deletion pass is at most

\[
\boxed{
S_3(t)
=
t+\binom t2+\binom t3
< t^3+t.
}
\]

The total number of CMR217 ancestry links from all such distinct certificates,
counted with one link per prescribed edge, is at most

\[
\boxed{
L_3(t)
=
t+2\binom t2+3\binom t3
=
t\left(1+(t-1)+\binom{t-1}{2}\right)
<3t^3.
}
\]

More precisely, if `n_i=|E_i|`, then the number of ancestry links pointing to
deletion step `i` is at most

\[
\boxed{
n_i\left(1+(t-1)+\binom{t-1}{2}\right).
}
\]

### Proof

Every fully forced certificate is a nonempty subset of `E_*` of size at most
three. Since `|E_*|\le t`, the number of such subsets is at most `S_3(t)`.

For the link count, each rank-`r` subset contributes `r` links. Equivalently,
fix one essential edge. It belongs to

\[
1+(|E_*|-1)+\binom{|E_*|-1}{2}
\]

subsets of size at most three. Summing over all essential edges gives `L_3(t)`.
If a link points to step `i`, its prescribed edge lies in `E_i`; restrict the
same count to the `n_i` edges of that layer. The displayed polynomial estimates
are immediate. ∎

## 4. Polynomial edge-set ancestry ledger

Construct the CMR218 ancestry DAG, but identify fully forced certificates with
the same prescribed edge set. Retain the deletion certificate at every step as
a possible parent node.

### Corollary CMR432 — PROVED

The deduplicated edge-set ancestry ledger in one deletion pass has at most

\[
\boxed{
d+S_3(t)}
\]

nodes and at most

\[
\boxed{L_3(t)<3t^3}
\]

forced-certificate ancestry links. Its incoming link width at deletion step `i`
is at most

\[
\boxed{
n_i\left(1+(t-1)+\binom{t-1}{2}\right),}
\]

and the sum of these incoming widths over all deletion steps is at most
`L_3(t)`.

Using CMR423,

\[
 d\le t(t-1),
\]

so the entire deduplicated ledger has polynomial size.

### Proof

There are `d` deletion-certificate nodes. CMR431 bounds the distinct fully forced
edge-set nodes and their links. The incoming-width formula is the final
statement of CMR431, and CMR423 bounds `d`. Acyclicity remains CMR218. ∎

This removes unbounded or factorial **edge-set width** from the ancestry
frontier. What remains is geometric and algorithmic: use the polynomial family
of exchange links simultaneously, or show that many links with different
p-adic, primitive-height, quotient, or carry labels force strict expansion or
resource consumption.

## 5. Revised frontier

Within one deletion pass:

1. packet processing completes or reaches one terminal forced certificate by
   CMR428;
2. every essential edge belongs to one final matching core of size at most `t`;
3. every distinct fully forced rank-`1/2/3` edge-set certificate is one of fewer
   than `t^3+t` subsets of that core;
4. all distinct CMR217 edge-set ancestry links total fewer than `3t^3`.

The next theorem is therefore not a raw width bound. It must exploit the
exchange cycles themselves: find a large low-overlap subfamily which can be
flipped simultaneously, or prove that high overlap concentrates on a bounded
p-adic/carry signature which opens an existing prefix, envelope, or line-clean
continuation.

No all-`n` theorem is claimed here. Essential-core monotonicity, subset counts,
link identities, and incoming-width sums are checked in
[`scripts/verify_prime_power_essential_core_ancestry.py`](../scripts/verify_prime_power_essential_core_ancestry.py).
