# Bounded-hole endpoint flows and shifted cost quantiles

**Branch:** `research/superregular-resampling`

SRR2j--SRR2m express the minimum aggregate event cost of a stationary Hall
flow through the matching ranks of endpoint-cost sublevel sets. This note
supplies a direct rank bound when each flawed state excludes only a bounded
number of otherwise available endpoints. It is not a theorem for an arbitrary
superregular switching graph: the new hypothesis is the explicit left-hole
bound below.

## Bounded left-hole model

Let `Gamma subseteq A x B` satisfy Hall's condition and put

\[
H(a)=B\setminus N_\Gamma(a).
\]

Assume

\[
\boxed{|H(a)|\le \Delta\qquad(a\in A).}
\]

For `S subseteq B`, let `r(S)` be the maximum number of vertices of `A` that
can be matched injectively into `S`.

## SRR2s -- bounded holes preserve sublevel rank -- PROVED

For every endpoint set `S subseteq B`,

\[
\boxed{
 r(S)\ge \min\{|A|,(|S|-\Delta)_+\}.
}
\]

Equivalently, the Hall deficiency into `S` satisfies

\[
\boxed{
 |A|-r(S)
 \le
 \min\{|A|,(|A|-|S|+\Delta)_+\}.
}
\]

### Proof

For every nonempty `X subseteq A`,

\[
B\setminus N_\Gamma(X)=\bigcap_{a\in X}H(a).
\]

The intersection is contained in each `H(a)`, so it has size at most
`Delta`. Hence

\[
|N_\Gamma(X)\cap S|\ge |S|-\Delta.
\]

The deficiency form of Hall's theorem gives

\[
|A|-r(S)
=
\max_{X\subseteq A}
\bigl(|X|-|N_\Gamma(X)\cap S|\bigr)_+.
\]

The empty set contributes zero. For nonempty `X`, the preceding lower bound
and `|X|<=|A|` give deficiency at most
`(|A|-|S|+Delta)_+`, with the trivial cap `|A|`. Rearranging proves the rank
form. QED.

## Shifted endpoint quantiles

Let `c:B -> Z_{>=0}` and write the endpoint costs in nondecreasing order

\[
c_{(1)}\le c_{(2)}\le\cdots\le c_{(|B|)}.
\]

Assume `|B|>=|A|+Delta`.

## SRR2t -- shifted-quantile matching bound -- PROVED

There is a matching `M` saturating `A` such that, after ordering its selected
endpoints by nondecreasing cost, its `i`-th endpoint has cost at most
`c_(i+Delta)`. Consequently

\[
\boxed{
 \operatorname{OPT}(c)
 \le
 \sum_{i=1}^{|A|}c_{(i+\Delta)}.
}
\]

### Proof

Let `S_i` be the set of the first `i+Delta` endpoints in the global cost
order. SRR2s gives `r(S_i)>=i`. The endpoint sets matchable from subsets of
`A` form a transversal matroid of rank `|A|`. Its greedy basis in
nondecreasing cost therefore has selected at least `i` endpoints by the time
all of `S_i` has been scanned. Thus its `i`-th selected endpoint costs at most
`c_(i+Delta)`. Summing proves the display. By SRR2j a minimum-cost Hall flow
may be chosen as such a saturating matching. QED.

The loss is exactly an endpoint-order shift, not a multiplicative worst-cost
factor. When `Delta=0`, the `|A|` cheapest endpoints can be used.

## SRR2u -- aggregate event-load consequence -- PROVED

Let `E` be the declared multiset of geometric events and let

\[
c(b)=m_E(b)
\]

be the number of events containing endpoint `b`. Under the stationary flow
normalization of SRR2i, one feasible resampling flow satisfies

\[
\boxed{
 \sum_{C\in E}\Pr(Y\in C)
 \le
 \frac1{|A|}
 \sum_{i=1}^{|A|}c_{(i+\Delta)}.
}
\]

In particular, if at least `|A|+Delta` endpoints have event multiplicity at
most `t`, then one stationary flaw-removing flow has expected event count at
most `t`.

### Proof

SRR2i identifies the expected aggregate event count with
`OPT(c)/|A|`. Apply SRR2t. For the final assertion, every shifted order
statistic in the sum is at most `t`. QED.

## Interface and remaining gap

The theorem applies once a concrete bounded-cycle switching construction proves
that each flawed state misses at most `Delta` candidate unflawed endpoints.
It then gives the actual rank-two/rank-three event inventory an exact cost
bound through its endpoint multiplicity quantiles. Arbitrary superregular
hosts can still have a large left-hole degree in the switching graph, so the
central SRR2 problem remains to construct a graph with a useful `Delta`, or to
replace the uniform hole bound by sharper threshold-local intersection bounds.

## Finite check

`scripts/verify_srr_bounded_hole_flow.py` exhausts small Hall-feasible bipartite
graphs with bounded left-hole degree, verifies the sublevel-rank estimate, and
compares the exact minimum matching cost with the shifted-quantile bound for
all small integer endpoint-cost vectors.
