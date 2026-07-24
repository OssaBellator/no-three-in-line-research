# Saturation, clones, reservoirs, and shadows

## 1. Two permutation layers

### Proposition S1 — PROVED

Every saturated configuration \(S\subseteq[n]^2\) decomposes into two permutation graphs.

### Proof

Interpret selected cells as edges of a bipartite graph between columns and rows. Every vertex has degree two. Every finite 2-regular bipartite graph is a disjoint union of even cycles. Alternately colour each cycle red and blue. Each colour gives degree one at every row and column, hence a perfect matching and therefore a permutation graph. ∎

This reduction is foundational: every saturation-preserving move may be viewed as an alternating-cycle switch in a bipartite graph.

## 2. Reservoir completion

Let \(R\subseteq S\) be removed and put \(X=S\setminus R\). Define row and column deficits

\[
a_x=2-|X\cap(\{x\}\times[n])|,
\qquad
b_y=2-|X\cap([n]\times\{y\})|.
\]

Then

\[
\sum_xa_x=
\sum_yb_y=|R|=:m.
\]

Create \(a_x\) clones of column \(x\) and \(b_y\) clones of row \(y\). Join a column clone to a row clone when the underlying cell may be inserted without creating a line defect with two retained points.

A perfect matching in this clone graph completes the deficits.

## 3. Active-coordinate secant shadow

For an active column \(x\), let \(Q_x(X)\) be the number of row clones whose cells in column \(x\) are blocked by secants through pairs of retained points. Define \(Q^y(X)\) symmetrically and

\[
Q(X)=\max\left(\max_xQ_x(X),\max_yQ^y(X)\right).
\]

### Proposition S2 — PROVED UNDER HYPOTHESES

If

\[
Q(X)+1\le\varepsilon^2m,
\]

then the full clone host has complement maximum degree at most \(\varepsilon^2m\). In particular it is a near-complete superregular bipartite graph in the standard dense sense.

### Proof sketch

A clone loses one neighbour for each blocked active cell and possibly one further neighbour from a multiplicity or loop restriction. Thus every clone has at least \(m-(Q(X)+1)\ge(1-\varepsilon^2)m\) neighbours. The same estimate holds on both sides. Near-complete bipartite graphs satisfy the usual regularity inequalities directly by inclusion-exclusion. ∎

## 4. Adaptive cleaning

For one active coordinate, build a blocker graph on retained points: a pair is adjacent if its secant blocks an active cell. Endpoints of a maximal matching form a vertex cover. Removing those endpoints clears all blockers for that coordinate.

This yields a cost-or-bank alternative:

- few matching edges: clean the coordinate economically;
- many matching edges: obtain many vertex-disjoint blocker secants.

### Important limitation

The secant bank is a bank of **latent obstructions**. Its secants need not currently be bad lines. Any proof must explain how the bank pays for actual potential destruction.

## 5. Pair-shadow regularization

In an externally clean completion host, a new defect caused by two inserted cells and one retained point has a unique retained anchor. For an anchor \(p\), let \(d_2(p)\) count candidate assignment pairs producing such a triple.

Removing anchors with \(d_2(p)>\Theta\) leaves

\[
|\mathcal C_2|\le2n\Theta.
\]

This is useful under a spread completion measure, but making it scale-sensitive and compatible with target batches remains open.
