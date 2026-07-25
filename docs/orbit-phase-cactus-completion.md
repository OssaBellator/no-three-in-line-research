# Exact reduction of binary-check cactus cores

OP2b completes every incidence pseudoforest. Multiply-cyclic components
can still be solved exactly when their residual checks have arity two and
the contracted variable graph is a cactus.

Contract every binary check to an edge between its two variables, retaining
parallel edges and their distinct forbidden ordered pairs. A connected
multigraph is a cactus when every edge lies on at most one cycle. Its
block--cut graph is a tree whose blocks are bridges or cycles.

Variables may already have nonempty allowed-label sets after unary
preprocessing. A binary check forbids one ordered pair of labels.

## OP2c -- cactus message reduction

### Theorem OP2c -- PROVED

For a binary-check canonical phase CSP whose contracted variable graph is
a cactus, satisfiability and a satisfying assignment can be decided in

\[
O\!\left(
\;h\sum_{uv\in E}|\mathcal A_u||\mathcal A_v|
\right),
\qquad
h=\max_v|\mathcal A_v|,
\]

time.

If the instance is unsatisfiable, the algorithm returns a boundary
variable whose allowed-label set is emptied by explicit block messages;
this is an articulation variable except possibly in the final block. Thus
every obstruction in this class is a certified unary saturation after
exact cactus compression.

### Proof

Root the block--cut tree. Process a leaf block \(B\) with articulation
variable \(a\); if \(B\) is the final block, use an arbitrary vertex as
the boundary.

If \(B\) is a bridge \(av\), compute for each allowed label of \(a\)
whether some allowed label of \(v\) avoids the edge's one forbidden pair.
This is a two-variable table scan.

If \(B\) is a cycle

\[
a=v_0,v_1,\ldots,v_k,v_{k+1}=a,
\]

fix a boundary label \(t\) at \(a\). Run path dynamic programming around
the cycle. For \(i=0,\ldots,k\), retain the labels of \(v_{i+1}\) reachable
from a retained label of \(v_i\) while satisfying the edge
\(v_iv_{i+1}\). At the closing edge, keep \(t\) exactly when some retained
label of \(v_k\) is compatible with it. Store one predecessor for every
retained state.

The resulting message is the set \(M_B\subseteq\mathcal A_a\) of boundary
labels extendable over all of \(B\). Replace the leaf block by the unary
restriction

\[
\mathcal A_a\leftarrow\mathcal A_a\cap M_B
\]

and delete its private vertices and edges. If this set becomes empty, the
stored block tables and earlier child messages certify that every label of
\(a\) is impossible.

Otherwise continue up the block--cut tree. The final block is accepted
exactly when its dynamic-programming table is nonempty. Reverse the stored
predecessors to recover all deleted block assignments.

The block--cut tree separates distinct child blocks at their articulation
variable, so their only joint requirement is that the chosen articulation
label belong to every child message. Hence the induction is exact.
Each bridge table costs
\(O(|\mathcal A_a||\mathcal A_v|)\); each cycle edge is scanned once for
each pair of endpoint labels and each fixed boundary label. Summing over
blocks gives the displayed bound.
\(\square\)

## Canonical-cycle interpretation

When all internal domains still have size at least two, a leaf canonical
cycle can reject at most the closing edge's forbidden label at its
articulation: every other articulation label already satisfies that edge,
and the remaining path can be completed greedily. Several child cycles
can nevertheless reject different labels and saturate a binary
articulation. This is a real multiply-cyclic obstruction, but OP2c turns
it into an explicit unary certificate rather than leaving a generic cycle
core.

The remaining OP2 topology can therefore be restricted further to:

- a unary saturation which must be paid or absorbed;
- a residual arity-three check in the multiply-cyclic core; or
- a binary-check contracted graph with a noncactus block, equivalently a
  block containing at least two independent cycles.

`scripts/verify_phase_cactus.py` exhaustively checks two-cycle binary
flowers against brute force and retains an explicit unary-saturation
example.
