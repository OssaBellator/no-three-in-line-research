# Generic matching branch width factors over exchange SCCs

CMR850--CMR853 identify the distinguishing rank of a perfect matching with the
feedback-vertex number of its exchange digraph. The tight rollback face already
has an SCC product in CMR454--CMR456. The same structure is purely matching-
theoretic and holds for every bipartite host.

Fix a balanced bipartite host `H`, a perfect matching

\[
Q=\{q_i=(i,\pi(i)):i\in L\},
\]

and its exchange digraph `D=D_Q(H)`. Let

\[
\mathcal S=\{C_1,\ldots,C_s\}
\]

be the strongly connected components of `D`.

## 1. An allowed nonmatching edge is usable exactly on a directed cycle

### Theorem CMR854 -- PROVED

For a nonmatching host edge

\[
a=(i,\pi(j)),
\qquad i\ne j,
\]

the following are equivalent.

1. `a` belongs to some perfect matching of `H`.
2. The exchange arc `i\to j` lies on a directed cycle of `D`.
3. The vertices `i,j` lie in the same strongly connected component of `D`.

### Proof

If a perfect matching uses `a`, its symmetric difference with `Q` contains an
alternating cycle using `a`, which contracts to a directed cycle containing
`i\to j`. A directed cycle containing the arc flips to a perfect matching using
`a` by CMR850. An arc lies on a directed cycle exactly when its endpoints belong
to the same SCC. ∎

Thus cross-component host edges are matching-inactive relative to the complete
perfect-matching family.

## 2. Exact union of all perfect-matching edges

Define

\[
A_Q
=
Q\cup
\{(i,\pi(j))\in E(H):C(i)=C(j)\}.
\]

### Theorem CMR855 -- PROVED

The graph `A_Q` is exactly the union of all perfect matchings of `H`, and

\[
\boxed{
\operatorname{PM}(A_Q)=\operatorname{PM}(H).
}
\]

### Proof

Every `Q` edge is in a perfect matching. CMR854 characterises every usable
nonmatching edge. Thus `A_Q` is the union of the matching family. Every perfect
matching of `H` lies in `A_Q`, while `A_Q\subseteq H` gives the reverse inclusion
of perfect-matching families. ∎

Deleting matching-inactive cross-SCC edges loses no feasible state.

## 3. Exact SCC product

For `C\in\mathcal S`, let `H_C` be the balanced bipartite block induced by source
vertices `C` and target vertices `\pi(C)` inside `A_Q`.

### Theorem CMR856 -- PROVED

The complete perfect-matching family factors exactly:

\[
\boxed{
\operatorname{PM}(H)
\cong
\prod_{C\in\mathcal S}\operatorname{PM}(H_C).
}
\]

A singleton acyclic component contributes only its matching edge `q_i`. Every
nontrivial SCC is a flexible block in which each `q_i` can be omitted by some
local perfect matching.

### Proof

CMR855 leaves no usable edge between distinct SCC blocks. Every block is balanced
and contains its `Q` edges. Hence a global perfect matching is exactly an
independent local perfect matching in every block. The singleton and flexibility
statements follow from CMR852. ∎

This is the generic counterpart of the rollback-face product CMR456.

## 4. Distinguishing rank is additive over cyclic SCCs

Let `Q_C=Q\cap E(H_C)` and define

\[
\delta_C
=
\delta_{\operatorname{PM}(H_C)}(Q_C).
\]

### Theorem CMR857 -- PROVED

One has

\[
\boxed{
\delta_{\operatorname{PM}(H)}(Q)
=
\sum_{C\in\mathcal S}\delta_C.
}
\]

Singleton acyclic components have `\delta_C=0`. For every nontrivial component,

\[
\boxed{
\delta_C=\operatorname{fvs}(D[C])\ge1.
}
\]

### Proof

Apply exact product additivity CMR849 to CMR856. A singleton block is a singleton
matching family. For a nontrivial block use CMR851 on its induced exchange
digraph, which contains a directed cycle. ∎

Only cyclic SCCs contribute completeness width.

## 5. Width concentration or many independent flexible blocks

Let `c` be the number of cyclic SCCs and let

\[
\delta=\delta_{\operatorname{PM}(H)}(Q).
\]

### Theorem CMR858 -- PROVED

At least one of the following equivalent quantitative descriptions holds.

1. One cyclic SCC has local distinguishing rank at least
   \[
   \boxed{\left\lceil\frac{\delta}{c}\right\rceil}.
   \]
2. There are `c` independent flexible factors, each contributing at least one
   unit of distinguishing rank, so
   \[
   \boxed{c\le\delta.}
   \]

### Proof

The positive integers `\delta_C` sum to `\delta` by CMR857. Average for the first
statement and use positivity for the second. ∎

The alternatives are used differently: concentration recurses inside one SCC,
while many SCCs expose an exact product of independent exchange blocks.

## 6. Exact branch cover assembled componentwise

For each cyclic component choose a minimum local distinguishing set

\[
B_C\subseteq Q_C,
\qquad |B_C|=\delta_C,
\]

and put `B=\bigsqcup_C B_C`.

### Theorem CMR859 -- PROVED

The global state-exclusion cover

\[
\boxed{
\operatorname{PM}(H)\setminus\{Q\}
=
\bigcup_{f\in B}(\operatorname{PM}(H)-f)
}
\]

has minimum possible width `|B|=\delta`. Every child deletion belongs to exactly
one SCC factor and leaves all other factors unchanged.

### Proof

CMR849 says the union of local minimum distinguishing sets is globally minimum.
Apply CMR847 for the exact cover. The factor-locality follows from the disjoint
SCC product. ∎

The branch cover is additive across components rather than a Cartesian product
of branch choices.

## 7. High local width means robust low-rank exchange

### Theorem CMR860 -- PROVED

If one SCC block has local distinguishing rank greater than `r`, then every
subset of at most `r` edges of its base matching `Q_C` occurs in another local
perfect matching of `H_C`.

In particular:

1. local width greater than one means every base edge is avoidable;
2. width greater than two means every compatible base pair is retained by an
   alternative local matching;
3. width greater than three means every base triple is retained by an alternative
   local matching.

### Proof

Apply CMR848 to the local matching family. ∎

This converts large SCC feedback width into exact low-rank extension richness.

## 8. Generic SCC-width endpoint

### Corollary CMR861 -- PROVED

For a full one-layer matching factor, completeness-preserving state exclusion has
an exact SCC normal form:

1. delete all matching-inactive cross-SCC edges for free;
2. contract singleton forced SCCs;
3. factor the matching family over cyclic SCCs;
4. add their local feedback-vertex widths;
5. either recurse into one high-width SCC or expose many independent flexible
   factors;
6. assemble a minimum global branch cover from minimum local covers.

The remaining two-layer completeness problem is to combine this one-layer SCC
normal form with layer-disjointness, or to show that many independent flexible
SCC blocks yield a globally compatible joint-state improvement.

### Proof

Combine CMR854--CMR860 with CMR846--CMR853. ∎

No all-`n` theorem is claimed. Usable-edge characterisation, exact SCC products,
width additivity, component concentration, and local branch covers are checked in
[`scripts/verify_prime_power_generic_exchange_scc.py`](../scripts/verify_prime_power_generic_exchange_scc.py).
