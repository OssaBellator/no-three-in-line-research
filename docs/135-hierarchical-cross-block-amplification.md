# Hierarchical cross-block amplification

PP3rn leaves a five-supervariable local contradiction as one possible outcome of
the four-state cross-block bank.  This contradiction is tied to that local state
space.  The cross-block construction may be iterated: pair two equal-size
supervariables and use only matchings between their resource blocks.

At every level, direct designated recapture removes fewer edges than are needed
to destroy all perfect matchings of the complete cross host.  Under sublinear
unary endpoint degree, almost the whole bank can be paired again.  Consequently
no bounded-level local CSP contradiction is terminal.

## 1. Level-\(b\) resource blocks

A **level-\(b\) block** contains \(b\) original rectangles.  It has:

- a left resource set \(L_B\) of size \(2b\);
- a right resource set \(R_B\) of size \(2b\);
- \(b\) distinguished owner columns, one from each original rectangle;
- at least \(b\) designated removal-credit units when all owners move.

Distinct blocks are resource-disjoint.

For two level-\(b\) blocks \(B,C\), a **level-\(2b\) cross state** is the union of:

- a perfect matching \(L_B\to R_C\);
- a perfect matching \(L_C\to R_B\).

### Proposition PP3rq -- PROVED

Before pruning, a paired level-\(2b\) block has exactly

\[
((2b)!)^2
\]

cross states.  Every state is a perfect matching on the combined resources,
uses no cell of either internal block \(L_B\times R_B\) or
\(L_C\times R_C\), moves all \(2b\) designated owners, and preserves every row
and column margin.

#### Proof

Choose independently one of the \((2b)!\) bijections in each cross direction.
Their union covers all \(4b\) left and \(4b\) right resources exactly once.  The
right resources used by an owner column belong to the other block and are
therefore disjoint from its original right-resource set. ∎

## 2. Minimum deletion needed to kill a complete matching host

### Lemma PP3rr -- PROVED

At least \(n\) edges must be deleted from \(K_{n,n}\) to produce a bipartite graph
with no perfect matching.

#### Proof

If the residual graph has no perfect matching, Hall gives a nonempty left set
\(X\) with

\[
|N(X)|\le|X|-1.
\]

Every edge from \(X\) to the complement of \(N(X)\) was deleted, so the number of
deleted edges is at least

\[
|X|(n-|N(X)|)
\ge
|X|(n-|X|+1).
\]

For \(1\le|X|\le n\), this expression is at least \(n\). ∎

The bound is sharp by isolating one vertex.

## 3. Direct recapture never kills a hierarchical cross host

In the direction \(L_B\to R_C\), every one of the \(b\) owner columns in \(B\)
has at most one direct-recapture cell: its nonaxis designated line meets that
fixed column and the row set \(R_C\) in at most one cell.  Thus at most \(b\)
direct-recapture edges are excluded.

### Proposition PP3rs -- PROVED

For every \(b\ge1\), the complete directional host \(K_{2b,2b}\) after deleting
all direct designated-recapture cells still has a perfect matching.

Consequently every pair of level-\(b\) blocks has at least one formal cross state
that directly preserves all \(2b\) designated owner credits.

#### Proof

There are at most \(b<2b\) deleted edges in each direction.  Lemma PP3rr says
that at least \(2b\) deletions are required to eliminate every perfect matching.
Choose a perfect matching independently in both directions. ∎

This generalizes PP3qt from original rectangle pairs to every hierarchy level.

## 4. Unary-safe pairing at every level

Let \(F\) be the non-designated unary-forbidden endpoint graph, with maximum left
and right degree at most \(d\).  Delete both the direct-recapture edges and the
edges of \(F\) from every directional cross host.

Form a bad-pair graph on the level-\(b\) blocks: join \(B,C\) when at least one of
the two directional hosts has no perfect matching.

### Theorem PP3rt -- PROVED

Every level-\(b\) block has bad-pair degree at most

\[
\boxed{4d}.
\]

This bound is independent of \(b\).

#### Proof

If \(L_B\to R_C\) has no perfect matching, Lemma PP3rr says that at least \(2b\)
edges of the complete host are absent.  Direct recapture accounts for at most
\(b\), so at least \(b\) distinct edges of \(F\cap(L_B\times R_C)\) are present.

The \(2b\) vertices of \(L_B\) have total \(F\)-degree at most \(2bd\).  The right
sets \(R_C\) are disjoint across partner blocks.  Therefore at most

\[
\frac{2bd}{b}=2d
\]

partners fail in the forward direction.  The reverse direction is charged to
the \(2b\) vertices of \(R_B\) and contributes at most another \(2d\) bad
partners. ∎

### Corollary PP3ru -- PROVED

A bank of \(H\) level-\(b\) blocks contains a matching of unary-safe pairs leaving
at most

\[
4d+1
\]

blocks unmatched.

If \(d=o(H)\), then almost all blocks amplify to level-\(2b\) blocks with nonempty
safe cross-state sets and at least \(2b\) designated credits each.

#### Proof

Use the maximal-good-pair matching argument PP3rb with the maximum-degree bound
PP3rt. ∎

## 5. Iteration through every fixed depth

### Theorem PP3rv -- PROVED

Fix an integer \(k\ge1\).  Start with a linear bank of original rectangles and
assume the non-designated unary endpoint degree is \(o(H)\) at every retained
bank scale.  After \(k\) amplification rounds, one obtains

\[
(1-o(1))\frac{H}{2^k}
\]

resource-disjoint level-\(2^k\) blocks.  Every block has:

- \(2^{k+1}\) left and \(2^{k+1}\) right endpoint resources;
- a nonempty finite set of unary-safe cross states;
- at least \(2^k\) designated removal-credit units;
- exact rank-at-most-three multistate bad boxes;
- exact unary/binary multistate insertion cost.

#### Proof

Induct on the rounds using PP3ru.  Since \(k\) is fixed, the sum of the
\(o(H)\) discarded blocks over all rounds is still \(o(H)\).  Proposition PP3rq
and the equal-margin argument PP3qw give the structural claims at each level.
A collinear triple meets at most three disjoint block supports, while a blocker
pair meets at most two. ∎

## 6. Consequence for local contradictions

### Corollary PP3rw -- PROVED

No contradiction involving only a bounded number of states and a bounded number
of blocks at one fixed hierarchy level is a terminal obstruction under sparse
unary degree.  The bank may be amplified once more and all geometry recomputed
in the new cross-block state space.

In particular, the three-rectangle Boolean contradiction and the five-
supervariable four-state contradiction are bypassed by the next hierarchy level.

#### Proof

Pair almost the entire current bank by PP3ru.  Proposition PP3rq shows that the
new states avoid every internal cell of the old block supports, so bad boxes
supported only on the old states do not directly constrain the amplified bank.
Recompute its exact bad boxes as in PP3bi. ∎

This does not assert that repeated amplification must eventually succeed.  It
shows that failure at every fixed depth is a coherent hierarchical obstruction,
not a finite local contradiction.

## 7. Revised hierarchical endpoint

### Corollary PP3rx -- PROVED

In the sparse-unary superregular recapture branch, the remaining rectangle
obstruction has one of the following forms.

1. At some hierarchy level, a linear family of blocks has no locally admissible
   cross state.
2. Unary or binary insertion cost is concentrated at the credit scale of the
   level-\(b\) blocks.
3. Residual matching unary or binary shadow is concentrated at the same scale.
4. The adaptive high-support source estimate fails.
5. The hierarchy remains locally feasible but no fixed amplification depth
   admits diffuse paid completion.

Finite signed contradictions at any fixed level are no longer separate open
cases.  The genuinely new object is a possible infinite-depth cross-block
hierarchy of concentrated geometry or cost.