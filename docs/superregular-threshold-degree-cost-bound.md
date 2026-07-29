# Threshold-degree bounds for endpoint transportation cost

**Branch:** `research/superregular-resampling`

SRR2j--SRR2m identify the exact endpoint-cost objective as the sum of low-cost Hall deficiencies. The remaining task is geometric: bound those deficiencies in switching graphs. This note gives a direct local criterion. At every event-cost threshold, left minimum degree and right maximum load bound the complete Hall deficiency. Bounded remote conditioning enters only through the number of low-cost switching incidences it actually deletes.

The theorem is deterministic and does not assume independence, expansion beyond the displayed degree data, or a complete host.

## Threshold graphs

Let `Gamma subseteq A x B` satisfy Hall's condition, with

\[
|A|=n.
\]

Let `c:B->Z_{>=0}` be an endpoint event cost and let `C=max c`. For `1<=k<=C`, define the low-cost threshold graph

\[
G_k=(A,B_{<k};E_k),
\qquad
B_{<k}=\{b:c(b)<k\}.
\]

Let

\[
d_k=\min_{a\in A}\deg_{G_k}(a),
\qquad
D_k=\max_{b\in B_{<k}}\deg_{G_k}(b),
\]

with the convention that the degree bound below is `n` when `d_k=0` or `B_{<k}` is empty.

For positive `d<=D`, define

\[
\Delta(n;d,D)
=
\max_{1\le s\le n}
\left(s-\left\lceil\frac{ds}{D}\right\rceil\right)_+.
\]

## SRR2s -- degree/load Hall-deficiency bound -- PROVED

For every threshold `k`, the low-cost Hall deficiency satisfies

\[
\boxed{
\delta_k
\le
\Delta(n;d_k,D_k).
}
\]

In particular,

\[
\boxed{
\delta_k
\le
n\left(1-\frac{d_k}{D_k}\right)_+
}
\]

whenever `d_k,D_k>0`.

### Proof

Fix `X subseteq A` with `|X|=s`. At least `d_ks` low-cost edges leave `X`. Every endpoint in `N_{<k}(X)` receives at most `D_k` of them, so

\[
|N_{<k}(X)|\ge\left\lceil\frac{d_ks}{D_k}\right\rceil.
\]

Hence the deficiency of `X` is bounded by the displayed expression for `s`. Maximize over `s`. Dropping the ceiling and using `s<=n` gives the second bound. QED.

The criterion is sharp for degree data alone: disjoint unions of complete bipartite pieces can attain the edge-count lower bound.

## SRR2t -- explicit endpoint-cost bound -- PROVED

Under the hypotheses above,

\[
\boxed{
\operatorname{OPT}(c)
\le
\sum_{k=1}^{C}\Delta(n;d_k,D_k).
}
\]

Consequently, if a target event budget is `T` and

\[
\sum_{k=1}^{C}\Delta(n;d_k,D_k)<T,
\]

then an integral saturating switching matching has total endpoint event cost below `T`.

### Proof

SRR2l gives `OPT(c)=sum_k delta_k`. Apply SRR2s term by term. Integrality is SRR2j. QED.

This converts the min-cost flow problem to threshold-local degree and congestion estimates.

## Remote partial matching conditioning

Let a bounded remote partial matching or other deterministic condition delete switching incidences but create no new low-cost incidence. Suppose `h` conditioned assignments are exposed and, for threshold `k`, each exposed assignment deletes at most `kappa_k` low-cost neighbours of any fixed flawed state.

Let the conditioned threshold graph have degree parameters `d_k',D_k'`.

## SRR2u -- local conditioning loss -- PROVED

The conditioned parameters satisfy

\[
\boxed{
d_k'\ge(d_k-h\kappa_k)_+,
\qquad
D_k'\le D_k.
}
\]

Therefore

\[
\boxed{
\delta_k'
\le
\Delta\bigl(n;(d_k-h\kappa_k)_+,D_k\bigr),
}
\]

using the value `n` when the conditioned minimum degree is zero.

### Proof

Each exposed assignment deletes at most `kappa_k` incident low-cost edges at one flawed state, so at most `h kappa_k` are lost from its degree. Deletion cannot increase any endpoint load. Apply SRR2s to the conditioned graph. QED.

The loss depends on local switching incidence, not the total number of host holes.

## SRR2v -- conditioned endpoint-cost criterion -- PROVED

Under the conditioning contract,

\[
\boxed{
\operatorname{OPT}(c\mid\mathcal C)
\le
\sum_{k=1}^{C}
\Delta\bigl(n;(d_k-h\kappa_k)_+,D_k\bigr).
}
\]

Thus any actual rank-two/rank-three event inventory is bank-ready whenever the right-hand side is below its declared current/protected event budget.

### Proof

Apply SRR2t to the conditioned threshold graphs and substitute SRR2u. QED.

## SRR2w -- multistep and two-layer accumulation -- PROVED UNDER DETERMINISTIC LOCALITY

Consider a deterministic sequence of one- or two-layer resampling steps indexed by `j`. At step `j`, let the active endpoint-cost inventory have threshold parameters `n_j,C_j,d_{j,k},D_{j,k}` and conditioned incidence losses `h_j kappa_{j,k}`. If every switching step preserves the declared deterministic locality region, then the total endpoint event cost along the path is at most

\[
\boxed{
\sum_j\sum_{k=1}^{C_j}
\Delta\bigl(n_j;(d_{j,k}-h_j\kappa_{j,k})_+,D_{j,k}\bigr).
}
\]

A current/protected drift audit may use this sum directly; no independence between steps or layers is required.

### Proof

SRR2v bounds each step conditionally on the complete preceding history. Deterministic locality ensures that the event inventory and deletion constants used at step `j` are valid for that history. Sum the pathwise bounds. QED.

## Updated SRR frontier

The endpoint-cost problem now has a concrete sufficient route:

1. compute the low-event threshold minimum degree `d_k` of each flawed state;
2. compute the maximum reverse endpoint load `D_k`;
3. charge remote conditioning by the actual local incidence `h kappa_k`;
4. insert the resulting degree-deficiency sum into the exact min-cost objective.

The remaining superregular work is to prove strong enough `d_k/D_k` ratios for bounded-cycle switching graphs and the actual rank-two/rank-three geometric event inventories. Spread and Hall feasibility alone still do not imply those ratios.

## Finite check

`scripts/verify_srr_threshold_degree_cost.py` enumerates small Hall-feasible costed bipartite graphs, computes exact threshold deficiencies and minimum matching cost, verifies the degree/load bounds, and audits local-incidence conditioning by edge deletion.
