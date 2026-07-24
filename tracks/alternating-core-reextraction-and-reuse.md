# Compatible re-extraction and an exact no-recycling criterion

This note proves two finite combinatorial interfaces used between AC1 and
AC4.  It does not supply the geometric conflict-degree or signature-reuse
bounds; it identifies exactly which bounds are sufficient.

## AC2a -- weighted compatible re-extraction

Let \(\mathcal O\) be a finite family of candidate structural objects
returned by AC1.  Give \(o\in\mathcal O\) a paid destroyed-incidence
weight \(w(o)\geq0\).  Join two objects in a conflict graph whenever they
cannot be installed simultaneously.  The conflict relation must include:

- overlap of active rows, columns, or replacement cells;
- overlap of paid certificates, so destroyed weight is not double-counted;
- any pair whose simultaneous installation creates a cross-object
  certificate or violates a protected bank contract.

### Lemma AC2a -- PROVED

If the conflict graph has maximum degree at most \(\Delta\), then it
contains a compatible family \(\mathcal I\) satisfying

\[
\boxed{
\sum_{o\in\mathcal I}w(o)
\geq
\frac1{\Delta+1}
\sum_{o\in\mathcal O}w(o).
}
\]

If every selected object has collateral at most
\(\eta w(o)\), and all nonadditive cross-object collateral was included
in the conflict relation, their simultaneous installation has total
collateral at most

\[
\eta\sum_{o\in\mathcal I}w(o).
\]

### Proof

A graph of maximum degree \(\Delta\) has a greedy proper colouring with at
most \(\Delta+1\) colours.  The colour classes are compatible.  One
colour class has at least a \(1/(\Delta+1)\) fraction of the total vertex
weight.  On a compatible colour class, paid certificate sets are disjoint
and all forbidden cross-effects have been excluded, so destroyed weight
and the assumed per-object collateral bounds add.
\(\square\)

Thus the constant-factor part of AC2 is complete once AC1's arithmetic
labels give a conflict graph of bounded degree.  A bound on ordinary
support overlap alone is not enough: certificate overlap and cross-object
creation must also be edges.

## AC3b -- ticketed signature potential

Let \(\Sigma\) be the finite signature universe from AC3a.  Give every
signature \(\sigma\) a nonnegative integer reuse budget \(R_\sigma\).
A closure state records an exposed set \(E\subseteq\Sigma\) and counters

\[
0\leq c_\sigma\leq R_\sigma.
\]

Assume every nonterminal transition does at least one of:

1. expose a signature outside \(E\); or
2. increment \(c_\sigma\) for a previously exposed signature without
   exceeding \(R_\sigma\).

### Lemma AC3b -- PROVED

The integer potential

\[
\boxed{
\Xi_{\rm ticket}
=|E|+\sum_{\sigma\in\Sigma}c_\sigma
}
\]

strictly increases at every nonterminal transition and satisfies

\[
0\leq\Xi_{\rm ticket}
\leq
|\Sigma|+\sum_{\sigma\in\Sigma}R_\sigma.
\]

Consequently the closure makes at most

\[
|\Sigma|+\sum_\sigma R_\sigma-\Xi_{\rm ticket}(s_0)+1
\]

oracle calls before termination.

### Proof

Exposure is permanent, so the first kind of transition increases
\(|E|\).  The second increases one counter.  All terms are nonnegative
and the displayed capacities give the upper bound.  Apply the bounded
integer-growth argument of AC4a.
\(\square\)

The substantive geometric assertion in AC3 is now the construction of
the tickets: an old signature must consume a charge attached to current
syndrome incidence, an original certificate, or a finite exceptional
state, and the corresponding \(R_\sigma\) must be \(p^{o(1)}\).

## AC3c -- exact unticketed cycle obstruction

Collapse closure states which have the same exposed-signature data, and
let \(Q\) be the finite directed graph of transitions carrying only old
signatures and consuming no ticket.

### Lemma AC3c -- PROVED

There is an integer potential strictly increasing on every edge of \(Q\)
if and only if \(Q\) is acyclic.

### Proof

A directed cycle is incompatible with strict increase: summing the
inequalities around the cycle would make a value strictly smaller than
itself.  Conversely, if \(Q\) is acyclic, assign each vertex the maximum
length of a directed path ending there.  Every edge extends such a path
by one, so the assigned integer strictly increases.
\(\square\)

Therefore a repeated-signature cycle cannot be repaired by choosing
different coefficients in the same potential.  AC3 must break every such
cycle by a paid bank, BDA/RI delegation, terminal improvement, or a
finite consumable ticket.  This is an exact audit criterion for the
remaining no-recycling proof.

`scripts/verify_ac_reextraction.py` exhaustively checks the weighted
colouring bound through six objects, the directed-cycle criterion through
four quotient states, and a finite ticket trace.
