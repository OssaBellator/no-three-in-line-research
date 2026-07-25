# Exact completion at bounded factor-incidence treewidth

OP2e treats cores at bounded variable-deletion distance from a factor
cactus. A different large class is controlled by separators rather than
feedback size: canonical checks need only one mismatch bit across a
factor-graph separator.

Let \(B\) be the bipartite factor-incidence graph with variable nodes
\(V\), check nodes \(\mathcal C\), and

\[
I=\sum_{C\in\mathcal C}|N(C)|
\]

incidence edges. Every variable \(v\) has a nonempty current domain
\(\mathcal A_v\) of size at most \(h\), and every check \(C\) forbids
one canonical tuple \(f_C\).

## OP2f -- bounded incidence-treewidth completion

### Theorem OP2f -- PROVED

If the factor-incidence graph \(B\) has treewidth at most \(t\), then
satisfiability and a satisfying assignment can be decided in

\[
\boxed{
O\!\left(
\max\{h,4\}^{\,t+1}
\bigl(|V|+|\mathcal C|+I\bigr)
\right)
}
\]

time from a width-\(t\) tree decomposition. An unsatisfiable instance
has an exact certificate consisting of the empty root table and the
finite separator-table recurrences below.

The bound is independent of check arity except through the incidence
graph and \(I\).

### Separator state

Use a nice tree decomposition with introduce-vertex, introduce-edge,
forget-vertex, and join nodes, arranging that every incidence edge is
introduced exactly once before either endpoint is forgotten.

For a bag \(\beta\), a state contains:

- one label \(a_v\in\mathcal A_v\) for every variable node
  \(v\in\beta\);
- one bit \(b_C\in\{0,1\}\) for every check node \(C\in\beta\).

The bit \(b_C\) is the OR of the mismatch indicators
\([a_v\ne f_C(v)]\) over incidences of \(C\) already introduced in the
processed subtree. A table entry is feasible exactly when the forgotten
variables extend the displayed labels, every forgotten check is
satisfied, and the displayed bits have this meaning.

### Recurrences

- Introducing a variable enumerates its current labels.
- Introducing a check initializes its bit to zero.
- Introducing an incidence edge \(Cv\) replaces
  \[
  b_C\quad\text{by}\quad b_C\vee[a_v\ne f_C(v)].
  \]
- Forgetting a variable existentially projects over its label.
- Forgetting a check retains only states with \(b_C=1\).
- At a join, the two child states must agree on every bag-variable
  label, and their bits combine by
  \[
  b_C=b_C^{(1)}\vee b_C^{(2)}.
  \]

At an empty root, the instance is satisfiable exactly when the unique
empty state is feasible. Stored predecessor choices reconstruct all
labels.

### Correctness

The connected-bag property ensures that every incidence touching a
forgotten node has already been introduced. A canonical check depends on
the processed side only through whether that side has supplied at least
one mismatch, so its one-bit summary is lossless. The introduce-edge
rule records the exact contribution of one incidence. Forgetting a
check with bit zero would accept its forbidden tuple and is therefore
disallowed; bit one means the check is permanently satisfied.

At a join, the processed incidence sets are disjoint and share only the
bag boundary. Agreement of variable labels and OR of mismatch bits are
therefore necessary and sufficient for combining the two extensions.
Induction over the decomposition proves the table semantics and the root
criterion.

A bag containing \(v\) variables and \(c\) checks has at most
\(h^v2^c\) states, with \(v+c\le t+1\). At a join there are
\(h^v4^c\) compatible pairs before OR aggregation. Both quantities are
at most \(\max\{h,4\}^{t+1}\). A nice decomposition has
\(O(|V|+|\mathcal C|+I)\) nodes, proving the complexity bound.
\(\square\)

## Consequence for OP2

Bounded incidence treewidth is complementary to OP2e. It permits
arbitrarily many overlapping cycles and arbitrarily large
variable-feedback distance, while the one-bit check interface avoids a
primal-graph clique blow-up from high-arity checks. Thus a residual core
requiring arithmetic Tanner expansion can now be assumed to have
unbounded factor-incidence treewidth as well as unbounded
variable-deletion distance from factor cacti.

This is an exact topological reduction, not the missing arithmetic
expansion theorem: the orbit construction must still prove that its
unbounded-width cores expand or enter a classified absorber.

`scripts/verify_phase_incidence_treewidth.py` exhaustively compares a
width-bounded transfer dynamic program with brute force for all
\(4^7\) binary canonical-check labellings of the noncactus
two-by-three ladder.
