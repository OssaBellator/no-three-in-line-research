# Composite history-cycle reset and constant residual core

PX294--PX314 reduce a trajectory-saturated terminal obstruction to an antichain
child `Q` on which no off-diagonal cell is currently allowed.  The non-base
forbidden cells of `Q x Q` are partitioned among edge-disjoint historical
partial matchings.  This chapter uses their union rather than one colour at a
time.

A directed cycle in the historical union is an executable principal cycle after
releasing only the ancestor levels carrying its edges.  If the union is
acyclic, a topological ordering forces an entire reverse triangular boundary
into the bounded base graph.  In particular the child order is at most
`Delta_0+1`, improving the earlier `2Delta_0+1` pair-count threshold and reducing
the genuinely no-reset templates to constant order for fixed base degree.

## 1. Historical-union cycle reset

Retain the antichain child `Q` of order `s` and the decomposition

\[
F[Q]=D[Q]\cup F_0[Q]\cup \widehat H_1[Q]\cup\cdots\cup\widehat H_d[Q],
\]

where the releasable historical sets `widehat H_j` are pairwise edge-disjoint
and disjoint from `F_0`.  Let

\[
H^\mathrm{rel}=\bigcup_{j=1}^d\widehat H_j[Q].
\]

### Theorem PX315 -- PROVED

If the directed graph `H^rel` contains a directed cycle `C`, then releasing the
ancestor constraints containing the edges of `C` makes `C` an allowed principal
cycle trade.  At most `|C|<=s` ancestor levels are released.

### Proof

Every edge of `C` belongs to one unique `widehat H_j`, because the historical
sets are edge-disjoint.  It is not base-forbidden.  Remove the distinct ancestor
constraints represented on `C`.  Every cycle edge is then allowed, and the
cycle gives one incoming and one outgoing selected cell at each of its vertices.
Hence it is a principal row-column-preserving cyclic rematching.  The number of
distinct released levels is at most the number of cycle edges. \(\square\)

The theorem supplies a bounded composite reset candidate.  Its full causal cost
is evaluated by the exact terminal optimizer; the statement does not assert
that arbitrary ancestor release is automatically lexicographically improving.

## 2. Acyclic historical union forces a base boundary

### Theorem PX316 -- PROVED

If `H^rel` is acyclic, then there is an ordering

\[
q_1,\ldots,q_s
\]

of `Q` such that

\[
\boxed{(q_j,q_i)\in F_0\quad\text{for every }1\le i<j\le s.}
\]

Consequently row `q_s` and column `q_1` each contain at least `s-1` base-forbidden
cells, and therefore

\[
\boxed{s\le\Delta_0+1.}
\]

### Proof

Take a topological ordering of the acyclic graph `H^rel`, so every historical
arc points forward.  Since `Q` is an antichain child, no off-diagonal cell of
`Q x Q` is allowed.  For `i<j`, the reverse cell `(q_j,q_i)` is not historical,
because it points backward in the topological order.  It is not diagonal, so it
must be base-forbidden.  Taking `j=s` gives `s-1` base cells in row `q_s`; taking
`i=1` gives `s-1` base cells in column `q_1`.  The base row and column degree
bound is `Delta_0`. \(\square\)

### Corollary PX317 -- PROVED

Every trajectory antichain child satisfies one of the following.

1. Its releasable historical union contains a directed cycle, giving the bounded
   composite reset of PX315.
2. It has order at most `Delta_0+1` and contains a completely reverse-triangular
   base boundary in a topological ordering.

In particular, when `Delta_0=0`, every child of order at least two has a
composite historical-cycle reset.

## 3. Constant residual template census

### Theorem PX318 -- PROVED

For fixed `Delta_0`, every no-composite-reset antichain child belongs to a finite
family depending only on `Delta_0`.  More explicitly, put `s<=Delta_0+1`.
After deleting empty historical restrictions, there are at most

\[
\boxed{s(s-1)}
\]

nonempty ancestor layers on `Q`, and every principal rematching together with
every subset of releasable layers can be exhaustively evaluated in

\[
\boxed{O_{\Delta_0}(1)}
\]

time.

### Proof

The releasable historical sets are edge-disjoint subsets of the `s(s-1)`
off-diagonal cells, so at most that many restrictions are nonempty.  For fixed
`s`, there are finitely many base graphs, partial-permutation colour classes,
subsets of nonempty colours, and principal permutations.  Since
`s<=Delta_0+1`, their total number depends only on `Delta_0`.  The exact
rank-at-most-three certificate table of PX273 evaluates each candidate. \(\square\)

Thus the trajectory terminal branch is no longer a growing path-forest census.
It is either a bounded composite cycle release, or a constant-size residual
obstruction certificate controlled entirely by the base degree.

## 4. Verification

Run

```bash
python scripts/verify_product_composite_history_cycle.py
```

The verifier exhausts all base/historical classifications of off-diagonal cells
through order four, checks the historical-cycle alternative, and confirms that
an acyclic historical union forces the reverse triangular base boundary and
`s<=Delta_0+1`.  It also performs randomized checks through order eight.
