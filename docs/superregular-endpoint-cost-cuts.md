# Endpoint-cost Hall cuts for stationary switching flows

**Branch:** `research/superregular-resampling`

SRR2i turns a declared geometric event inventory into a min-cost Hall flow with a nonnegative integer endpoint cost. This note evaluates that optimization exactly by matching ranks of low-cost endpoint sets. The remaining geometric problem becomes a family of explicit Hall-deficiency bounds.

## Integer endpoint costs

Let `Gamma subseteq A x B` satisfy Hall's condition and let

\[
c:B\longrightarrow\mathbb Z_{\ge0}
\]

be an endpoint cost. For a feasible Hall flow `w`, put

\[
q_w(b)=\sum_a w_{ab}.
\]

Define

\[
\operatorname{OPT}(c)
=
\min_{w\in P(\Gamma)}
\sum_{b\in B}c(b)q_w(b).
\]

For each integer `k>=1`, let

\[
B_{<k}=\{b\in B:c(b)<k\},
\]

and let `r_k` be the maximum number of vertices of `A` that can be matched injectively into `B_{<k}`.

## SRR2j -- an optimal endpoint-cost flow is integral -- PROVED

There is an optimal feasible Hall flow supported on one matching saturating `A`.

### Proof

The polytope `P(Gamma)` is the bipartite matching polytope with equality one at every vertex of `A` and capacity at most one at every vertex of `B`. Its constraint matrix is totally unimodular, so every vertex is integral. A linear objective attains its minimum at a vertex. QED.

## SRR2k -- exact sublevel-rank formula -- PROVED

Let `C=max_b c(b)`. Then

\[
\boxed{
\operatorname{OPT}(c)
=
\sum_{k=1}^{C}\bigl(|A|-r_k\bigr).
}
\]

### Proof

For any saturating matching `M`,

\[
\sum_{b\in M}c(b)
=
\sum_{k=1}^{C}
|\{b\in M:c(b)\ge k\}|.
\]

At most `r_k` selected endpoints can lie in `B_{<k}`, so every matching has at least `|A|-r_k` selected endpoints of cost at least `k`. This proves the lower bound.

The subsets of `B` that can be matched injectively from subsets of `A` form a transversal matroid of rank `|A|`. Run the matroid greedy algorithm in nondecreasing endpoint cost until a basis is obtained. At every sublevel `B_{<k}`, greedy selects a maximal independent subset and therefore exactly `r_k` endpoints from that sublevel. Its cost attains all the lower bounds simultaneously. By SRR2j it is a feasible optimal Hall flow. QED.

## Hall-deficiency form

For `X subseteq A`, write

\[
N_{<k}(X)=N_\Gamma(X)\cap B_{<k}.
\]

Define the low-cost Hall deficiency

\[
\delta_k
=
\max_{X\subseteq A}
\bigl(|X|-|N_{<k}(X)|\bigr)_+.
\]

## SRR2l -- exact endpoint-cost deficiency formula -- PROVED

For every `k`,

\[
\boxed{\delta_k=|A|-r_k,}
\]

and therefore

\[
\boxed{
\operatorname{OPT}(c)=\sum_{k=1}^{C}\delta_k.
}
\]

### Proof

The deficiency form of Hall's theorem states that the maximum number of vertices of `A` matchable into a specified endpoint set `S` is

\[
|A|-
\max_{X\subseteq A}
\bigl(|X|-|N(X)\cap S|\bigr)_+.
\]

Apply this with `S=B_{<k}` and substitute into SRR2k. QED.

## SRR2m -- failed low-cost flow localizes to one threshold cut -- PROVED

If

\[
\operatorname{OPT}(c)\ge T>0,
\]

then for some `1<=k<=C` there is a set `X subseteq A` satisfying

\[
\boxed{
|X|-|N_\Gamma(X)\cap B_{<k}|
\ge
\frac{T}{C}.
}
\]

Every endpoint outside `B_{<k}` has event cost at least `k`.

### Proof

SRR2l gives `sum_k delta_k>=T`, so one `delta_k>=T/C`. Choose a set `X` attaining that deficiency. The final assertion is the definition of `B_{<k}`. QED.

## Consequence for SRR2

For an actual event inventory, it is no longer necessary to reason about an abstract fractional optimizer.

- Low event cost follows exactly from small Hall deficiencies into every event-cost sublevel.
- Failure returns one threshold `k` and one flawed-state set `X` that cannot access enough endpoints carrying fewer than `k` events.
- Superregular switching arguments can now target these explicit low-cost neighbourhood cuts.

This is stronger information than global Hall feasibility and more geometric than the linear-program formulation alone.

## Finite check

`scripts/verify_superregular_endpoint_cost_cuts.py` enumerates small Hall-feasible bipartite graphs and integer endpoint costs, compares the exact minimum matching cost with both the sublevel-rank and Hall-deficiency sums, and verifies the threshold-cut localization.
