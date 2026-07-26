# Complete branch width is a distinguishing rank

CMR830--CMR845 reduce completeness to viable single-edge branching in a
core-free equal-cardinality family. Branching on every edge of a rejected state
is often redundant. The exact compressed width is the minimum number of its
edges which uniquely identify that state inside the current family.

For a full perfect-matching family this invariant has a standard exchange
interpretation: it is the minimum directed feedback-vertex-set size of the
exchange digraph relative to the rejected matching. Product factorisation makes
the invariant additive rather than multiplicative.

Let `\mathcal F` be a nonempty equal-cardinality family on a finite labelled
ground set, and fix `Q\in\mathcal F`. Define the alternative-support hypergraph

\[
\mathcal H_Q
=
\{Q\setminus R:R\in\mathcal F,\ R\ne Q\}.
\]

A subset `B\subseteq Q` **distinguishes** `Q` when no alternative state contains
all of `B`. Define

\[
\delta_{\mathcal F}(Q)
=
\min\{|B|:B\subseteq Q,\ B\text{ distinguishes }Q\}.
\]

For a singleton family, the empty set distinguishes `Q`, so `\delta=0`.

## 1. Distinguishing rank is a transversal number

### Theorem CMR846 -- PROVED

A subset `B\subseteq Q` distinguishes `Q` if and only if it meets every member of
`\mathcal H_Q`. Consequently

\[
\boxed{
\delta_{\mathcal F}(Q)=\tau(\mathcal H_Q),
}
\]

the transversal number of the alternative-support hypergraph.

### Proof

An alternative `R` contains `B` exactly when
`B\cap(Q\setminus R)=\varnothing`. Thus no alternative contains `B` precisely
when `B` intersects every difference support. ∎

## 2. Exact compressed branch cover

### Theorem CMR847 -- PROVED

For `B\subseteq Q`,

\[
\boxed{
\mathcal F\setminus\{Q\}
=
\bigcup_{f\in B}(\mathcal F-f)
}
\]

if and only if `B` distinguishes `Q`.

Therefore the minimum number of single-edge children whose union excludes only
`Q` is exactly

\[
\boxed{\delta_{\mathcal F}(Q).}
\]

### Proof

An alternative `R` belongs to the displayed union exactly when it omits at least
one edge of `B`. This holds for every alternative exactly when no alternative
contains `B`. The rejected state belongs to no child because it contains every
edge of `B`. Minimise over `B`. ∎

CMR831 is the special choice `B=Q`.

## 3. High distinguishing rank gives local exchange richness

### Theorem CMR848 -- PROVED

For an integer `s\ge0`, if

\[
\delta_{\mathcal F}(Q)>s,
\]

then every subset `B\subseteq Q` with `|B|\le s` is contained in some alternative
state `R\ne Q`.

### Proof

If some such `B` were contained in no alternative, it would distinguish `Q` with
size at most `s`. ∎

In particular, distinguishing rank greater than three means every labelled edge,
pair, and triple of `Q` occurs in another feasible state.

## 4. Distinguishing rank is additive in exact products

Let the ground sets be disjoint and let

\[
\mathcal F
=
\mathcal F_1\times\cdots\times\mathcal F_m
=
\{R_1\sqcup\cdots\sqcup R_m:R_i\in\mathcal F_i\}.
\]

Fix `Q=Q_1\sqcup\cdots\sqcup Q_m`.

### Theorem CMR849 -- PROVED

One has

\[
\boxed{
\delta_{\mathcal F}(Q)
=
\sum_{i=1}^{m}\delta_{\mathcal F_i}(Q_i).
}
\]

### Proof

For the upper bound, take minimum distinguishing sets `B_i\subseteq Q_i` and use
`B=\bigsqcup_i B_i`. Any product state containing `B` contains each `B_i` and
therefore equals `Q_i` in every factor.

For the lower bound, decompose any distinguishing set as
`B=\bigsqcup_i B_i`. If some `B_i` failed to distinguish `Q_i`, choose an
alternative factor state containing `B_i` and keep all other factors equal to
`Q_j`. The resulting product alternative contains all of `B`, contradiction.
Thus `|B_i|\ge\delta_i` for every factor. ∎

Exact wall, child-routing, skeleton, and essential-core products therefore add
branch width across residual factors; they do not multiply it.

## 5. Exchange digraph of one perfect matching

Let `H=(L,R;E)` be a balanced bipartite host and let

\[
Q=\{q_i=(i,\pi(i)):i\in L\}
\]

be a perfect matching. Define the directed exchange graph `D_Q(H)` on vertex set
`L` by placing an arc

\[
i\longrightarrow j
\]

whenever `i\ne j` and the nonmatching edge `(i,\pi(j))` belongs to `H`.

### Theorem CMR850 -- PROVED

Every alternative perfect matching `R` of `H` determines a nonempty collection
of vertex-disjoint directed cycles in `D_Q(H)`. Its moved vertex set is exactly

\[
\{i:q_i\in Q\setminus R\}.
\]

Conversely, every directed cycle in `D_Q(H)` gives an alternative perfect
matching obtained by replacing the `Q` edges on that cycle with its exchange
arcs.

### Proof

Express `R` relative to the target order of `Q`: source `i` is matched to
`\pi(\sigma(i))` for a permutation `\sigma`. Fixed points retain `q_i`; every
nontrivial cycle of `\sigma` uses the corresponding directed arcs. Conversely,
flipping one directed cycle covers the same source and target vertices exactly
once and leaves all other `Q` edges unchanged. ∎

## 6. Matching distinguishing rank equals feedback-vertex number

Let `\operatorname{fvs}(D)` denote the minimum number of vertices meeting every
directed cycle of `D`.

### Theorem CMR851 -- PROVED

For the complete matching family `\operatorname{PM}(H)`,

\[
\boxed{
\delta_{\operatorname{PM}(H)}(Q)
=
\operatorname{fvs}(D_Q(H)).
}
\]

### Proof

Identify a subset of `Q` with its source-vertex set. By CMR850, an alternative
matching omits exactly the `Q` edges on a nonempty union of directed cycles.
Therefore a subset distinguishes `Q` exactly when it meets every directed cycle.
Minimise. ∎

Thus complete branch-width control for a one-layer matching factor is an exact
directed cycle-transversal problem.

## 7. Essential edges are the acyclic vertices of the exchange support

### Theorem CMR852 -- PROVED

A matching edge `q_i\in Q` is nonessential in `H` if and only if vertex `i` lies
on a directed cycle of `D_Q(H)`.

Consequently, after contracting the complete essential core, every residual
vertex lies on at least one directed cycle, while the distinguishing rank remains
the minimum number of vertices meeting all such cycles.

### Proof

The edge `q_i` is omitted by some perfect matching exactly when `i` belongs to
the moved set of an alternative. Apply both directions of CMR850. ∎

Core-freeness guarantees cycle coverage of every vertex but does not by itself
bound the feedback-vertex number.

## 8. Distinguishing-rank branch endpoint

### Corollary CMR853 -- PROVED

At every completeness-preserving state-exclusion node:

1. the exact minimum child-cover width is `\delta_{\mathcal F}(Q)`;
2. width greater than `s` forces every rank-at-most-`s` prescription of `Q` to
   occur in another state;
3. exact product factors contribute additively to the width;
4. for a full matching factor, the width is the directed feedback-vertex number
   of its exchange digraph;
5. after full essential-core contraction, every residual matching vertex lies on
   an exchange cycle.

The active completeness frontier is therefore to control feedback-vertex width
or low-rank distinguishing prescriptions in the core-free residual factors, and
to lift that control through the two-layer disjointness coupling.

### Proof

Combine CMR846--CMR852 with the complete branching and core normal forms
CMR830--CMR845. ∎

No all-`n` theorem is claimed. Hypergraph transversals, exact branch covers,
product additivity, exchange-cycle correspondence, feedback-vertex equality, and
essential-edge characterisation are checked in
[`scripts/verify_prime_power_distinguishing_rank.py`](../scripts/verify_prime_power_distinguishing_rank.py).
