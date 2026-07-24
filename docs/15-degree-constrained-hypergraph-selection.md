# Degree-constrained hypergraph selection

This chapter gives an exact endpoint theorem for selecting a saturated no-three-in-line configuration from a sufficiently clean candidate host.

## 1. Clone-space reduction

Let \(R=C=[n]\). For every row and column create two clones:

\[
\widehat R=R\times\{1,2\},\qquad \widehat C=C\times\{1,2\}.
\]

Put \(N=2n\). A perfect matching of \(K_{N,N}\) chooses one edge incident with every row clone and every column clone.

For a grid cell \(x=(r,c)\), its four clone lifts are

\[
\Gamma(x)=\{(r_i,c_j):i,j\in\{1,2\}\}.
\]

If a perfect matching never chooses two disjoint lifts of the same cell, then its projection is a set of exactly \(2n\) distinct grid cells with exactly two in every row and column.

This converts the exact degree requirement into an ordinary perfect-matching constraint.

## 2. Canonical bad events

Let \(G\subseteq R\times C\) be the allowed candidate cells.

We use a uniformly random perfect matching \(M\) of \(K_{N,N}\). There are three types of canonical bad event.

### Type 1: unavailable cell

For every clone edge \(e\in\Gamma(x)\) with \(x\notin G\), forbid

\[
A_e=\{e\in M\}.
\]

This event is specified by a partial matching of size one.

### Type 2: duplicate cell

For each allowed cell \(x=(r,c)\), the only two pairs of disjoint clone lifts are

\[
\{(r_1,c_1),(r_2,c_2)\},
\qquad
\{(r_1,c_2),(r_2,c_1)\}.
\]

Forbid both pairs. Each duplicate event is specified by a partial matching of size two.

### Type 3: collinear triple

Horizontal and vertical triples are automatically impossible after projection, since each original row and column receives exactly two cells.

For every collinear triple \(T=\{x,y,z\}\subseteq G\) with distinct rows and distinct columns, and every choice of one clone lift of each cell forming a partial matching, forbid the event that all three lifted edges lie in \(M\).

Because the three original rows and columns are distinct, there are exactly

\[
2^6=64
\]

clone lifts of each original triple.

A perfect matching avoiding every bad event projects to a saturated \(2n\)-point no-three-in-line set contained in \(G\).

## 3. Random matching probabilities

If \(F\) is a fixed partial matching of size \(s\) in \(K_{N,N}\), then

\[
\Pr(F\subseteq M)=\frac1{(N)_s},
\qquad
(N)_s=N(N-1)\cdots(N-s+1).
\]

The canonical-event conflict graph joins two events when their defining partial matchings are incompatible. The Lu--Szekely matching-space local lemma says this is a negative dependency graph.

For a clone vertex \(v\in\widehat R\cup\widehat C\), define its probability load

\[
L(v)=\sum_{A:\,v\in V(F_A)}\Pr(A),
\]

where \(F_A\) is the partial matching defining \(A\).

## 4. Exact local-load theorem

### Theorem D1 -- PROVED

If

\[
\boxed{\max_v L(v)\le\frac1{24},}
\]

then \(G\) contains a set of exactly \(2n\) distinct cells, with exactly two in every row and column, and with no three collinear.

### Proof

For every bad event \(A\), put

\[
x_A=2\Pr(A).
\]

Every defining partial matching has at most three edges and hence at most six clone vertices.

If \(B\) is adjacent to \(A\) in the negative dependency graph, then the partial matchings defining \(A\) and \(B\) conflict at some clone vertex belonging to \(F_A\). Therefore

\[
\sum_{B\sim A}x_B
\le
2\sum_{v\in V(F_A)}L(v)
\le
12\cdot\frac1{24}
=
\frac12.
\]

For numbers \(x_i\in[0,1]\),

\[
\prod_i(1-x_i)\ge1-\sum_i x_i.
\]

Hence

\[
x_A\prod_{B\sim A}(1-x_B)
\ge
2\Pr(A)\left(1-\frac12\right)
=
\Pr(A).
\]

The lopsided Lovasz local lemma gives positive probability that no bad event occurs. Projecting such a perfect matching gives the required configuration. \(\square\)

## 5. Geometric form of the load

For an original row \(r\), let

- \(m_R(r)\) be the number of unavailable cells in row \(r\);
- \(\tau_R(r)\) be the number of allowed collinear triples with distinct rows and columns containing a cell in row \(r\).

Define \(m_C(c)\) and \(\tau_C(c)\) analogously for columns, and put

\[
m_* = \max\{\max_r m_R(r),\max_c m_C(c)\},
\]

\[
\tau_* = \max\{\max_r\tau_R(r),\max_c\tau_C(c)\}.
\]

For a fixed row clone:

1. every unavailable original cell produces two singleton events containing that clone, contributing
   \[
   \frac{2m_R(r)}{N}=\frac{m_R(r)}n;
   \]
2. every allowed original cell produces two possible duplicate events containing that clone, contributing at most
   \[
   \frac{2n}{(N)_2}=\frac1{2n-1};
   \]
3. every original collinear triple containing row \(r\) has exactly \(32\) lifted triple events containing the fixed row clone, contributing
   \[
   \frac{32\tau_R(r)}{(N)_3}.
   \]

The same calculation holds for column clones.

### Corollary D2 -- PROVED

It is sufficient that

\[
\boxed{
\frac{m_*}{n}
+
\frac1{2n-1}
+
\frac{32\tau_*}{(2n)(2n-1)(2n-2)}
\le
\frac1{24}.
}
\]

Under this inequality, \(G\) contains a saturated no-three-in-line configuration.

## 6. Concrete robust endpoint

### Corollary D3 -- PROVED

For \(n\ge100\), the following simpler hypotheses suffice:

\[
m_*\le\frac n{100},
\qquad
\tau_*\le\frac{n^3}{200}.
\]

Indeed,

\[
\frac1{100}
+
\frac1{199}
+
\frac{32(n^3/200)}{(2n)(2n-1)(2n-2)}
<
\frac1{24}.
\]

Thus an endpoint cleaning theorem only needs to leave at least \(99\%\) of the cells available in every row and column and reduce residual triple incidence below \(n^3/200\) per row and column.

The constants are deliberately non-optimized.

## 7. Concentration contrapositive

### Corollary D4 -- PROVED

If no saturated conflict-free selection exists in \(G\), then

\[
\boxed{
\tau_*
>
\frac{(2n)(2n-1)(2n-2)}{32}
\left(
\frac1{24}-\frac{m_*}{n}-\frac1{2n-1}
\right)
}
\]

whenever the expression in parentheses is positive.

Hence failure of exact selection in a near-complete host forces a row or column carrying \(\Omega(n^3)\) residual collinear triples.

This is a useful inverse statement: a stalled endpoint cannot be diffuse.

## 8. Multiscale form

Partition nonaxis collinear triples into dyadic primitive-height bands and write

\[
\tau_*=\max_v\sum_H\tau_H(v).
\]

The theorem depends only on the sum of the local band loads. Thus reverse-scale cleaning may allocate a total budget

\[
\sum_H\tau_H(v)\le\frac{n^3}{200}
\]

for every row and column.

The full grid has a logarithmic accumulation over direction scales, so it does not satisfy this endpoint criterion directly. The theorem identifies the exact task of the geometric stage: remove or algebraically absorb enough high-load direction families that the remaining local sum is constant-sized rather than logarithmic.

## 9. Relation to conflict-free matching theory

The clone reduction turns the problem into a perfect matching avoiding conflicts of sizes one, two and three. General conflict-free matching theorems provide almost-perfect matchings under near-regularity and codegree assumptions, and newer covering theorems provide exact coverage in suitable two-stage settings.

The theorem above is narrower but exact and self-contained for the complete clone matching space. Its main limitation is the near-complete-host requirement. The next extension is a superregular-host version in which the uniform perfect-matching distribution is replaced by a spread distribution or a conflict-free matching process on a dense bipartite graph.

## 10. Next target

### Superregular clone-selection lemma -- OPEN

Let \(G\subseteq R\times C\) be an \((\varepsilon,d/n)\)-superregular bipartite graph. Prove an analogue of Theorem D1 with probabilities \(O(d^{-s})\) for prescribed compatible sets of \(s\) clone edges and a dependency or resampling structure strong enough for the lopsided local lemma.

A successful version should replace the unavailable-cell term \(m_*/n\) by superregularity hypotheses and replace \(n\) by the local degree \(d\).