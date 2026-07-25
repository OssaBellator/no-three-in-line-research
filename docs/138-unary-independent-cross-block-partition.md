# Unary-independent cross-block partition

PP3sh obtains superregular growing cross-block hosts when the non-designated
unary maximum degree satisfies \(d=o(\sqrt H)\).  The square-root threshold is an
artifact of grouping arbitrary rectangles.  Instead, first colour the rectangle
interaction graph defined by unary-forbidden cells.  Every colour class is
unary-independent, and splitting its classes into growing groups loses only
\(O(db)\) rectangles.

This produces near-complete superregular cross hosts for every sublinear unary
maximum degree \(d=o(H)\).

## 1. Rectangle interaction graph

Let the resource-disjoint rectangle bank have size \(H\).  Every rectangle \(s\)
has two left endpoint resources \(L_s\) and two right endpoint resources \(R_s\).

Let \(F\) be the non-designated unary-forbidden endpoint graph, with maximum left
and right degree at most \(d\).  Form a simple graph \(\Gamma_F\) on the
rectangles by joining \(s,t\) when \(F\) contains an edge in either cross block

\[
L_s\times R_t
\qquad\text{or}\qquad
L_t\times R_s.
\]

### Proposition PP3si -- PROVED

The maximum degree of \(\Gamma_F\) is at most

\[
\boxed{4d}.
\]

#### Proof

Fix rectangle \(s\).  The two vertices of \(L_s\) have total \(F\)-degree at
most \(2d\), so at most \(2d\) partner rectangles have a forbidden edge from
\(L_s\) into their right-resource pair.  The two vertices of \(R_s\) have total
right degree at most \(2d\), so at most another \(2d\) partners have a forbidden
edge from their left pair into \(R_s\). ∎

Thus \(\Gamma_F\) has a proper colouring with at most \(4d+1\) colours.

## 2. Almost-complete partition into unary-independent groups

Choose a power of two \(b=b(H)\) such that

\[
b\longrightarrow\infty,
\qquad
(d+1)b=o(H),
\qquad
H/b\longrightarrow\infty.
\]

Such a choice is supplied by PP3ry with \(d+1\) in place of \(d\).

### Theorem PP3sj -- PROVED

After discarding \(o(H)\) rectangles, the bank partitions into

\[
(1-o(1))\frac Hb
\]

groups of exactly \(b\) rectangles such that no non-designated unary-forbidden
edge joins resources of two different rectangles in the same group.

#### Proof

Properly colour \(\Gamma_F\) with at most \(4d+1\) colours.  Split every colour
class into groups of size \(b\), discarding its final remainder of fewer than
\(b\) vertices.  The total discarded count is below

\[
(4d+1)b=o(H).
\]

Every group lies in one independent colour class, so no pair of its rectangles
is adjacent in \(\Gamma_F\). ∎

Unary edges internal to one original rectangle are irrelevant below because the
new states use only cross cells between the two halves of a group.

## 3. Direct construction of growing cross blocks

Split one unary-independent group into two halves \(B,C\), each containing
\(b/2\) rectangles.  The directional cross hosts have side size \(b\):

\[
L_B\longrightarrow R_C,
\qquad
L_C\longrightarrow R_B.
\]

### Proposition PP3sk -- PROVED

The only unary exclusions in either directional host are direct designated-
recapture cells.  There are at most \(b/2\) such cells per direction.

Consequently both directional hosts contain perfect matchings, and their union
is a level-\(b\) cross state moving all \(b\) designated owners and preserving at
least \(b\) removal-credit units.

#### Proof

Unary independence from PP3sj removes every edge of \(F\) between the two
halves.  Each of the \(b/2\) owner columns in the source half contributes at most
one direct-recapture exclusion.  Lemma PP3rr says that at least \(b\) deletions
are needed to destroy every perfect matching of \(K_{b,b}\), so at most \(b/2\)
deletions cannot do so.  Choose one matching in each direction. ∎

Thus no iterative safe-pair search is needed to reach the growing block scale.

## 4. Recapture pruning and superregularity

In one directional host, the total target-side direct-recapture degree is at
most \(b/2\).  Delete every original rectangle containing a target resource of
recapture degree above \(b^{2/3}\), and balance the two halves as in PP3sd.

### Theorem PP3sl -- PROVED

After deleting \(O(b^{1/3})\) rectangles from one group, both directional hosts
have side size

\[
b'=(1-o(1))b
\]

and forbidden-complement maximum degree

\[
O(b^{2/3})=o(b').
\]

Hence both hosts are near-complete superregular graphs.  The pruned block retains
\((1-o(1))b\) designated owner credits.

Across all groups, the total recapture-pruning loss is

\[
O\left(\frac Hb b^{1/3}\right)
=
O(Hb^{-2/3})
=o(H).
\]

#### Proof

The heavy-target count and balancing loss are PP3sd with the non-designated
unary term absent.  After pruning, every left resource loses at most one direct-
recapture edge and every right resource loses at most \(b^{2/3}\).  Apply PP3ip.
The global loss estimate follows from the number of groups and \(b\to\infty\).
∎

## 5. Spread and paid state selection

Choose independent uniform perfect matchings in the two directional
superregular hosts.

### Corollary PP3sm -- PROVED FROM SR1

Every prescribed compatible rank-\(r\) collection of block cells occurs with
probability

\[
O(b^{-r})
\]

for fixed \(r\).  The block has a source-admissible strict paid state whenever
its source and shadow counts satisfy the PP3sg inequality with

\[
R_b\ge(1-o(1))b.
\]

#### Proof

Use PP3sf and PP3sg. ∎

## 6. Complete sublinear-unary conclusion

### Theorem PP3sn -- PROVED

Let a superregular recapture-line rectangle bank have size \(H\to\infty\), and
suppose its non-designated unary-forbidden endpoint graph has maximum degree

\[
d=o(H).
\]

Then, after discarding \(o(H)\) rectangles, it decomposes into a growing number
of growing-credit blocks whose local cross-state hosts are near-complete
superregular and have fixed-rank spread.

#### Proof

Apply PP3sj, PP3sk, PP3sl, and PP3sm. ∎

The only unary-degree obstruction left by the rectangle hierarchy is therefore
linear maximum degree.

## 7. Revised rectangle frontier

### Corollary PP3so -- PROVED

In the superregular recapture branch, failure of block-state conversion requires
one of:

1. a unary endpoint resource with
   
   \[
   \Omega(H)
   \]
   
   forbidden cross-block cells;
2. source or shadow weights concentrated in the paid growing-block expression
   PP3sg;
3. failure of the adaptive high-support source estimate after the block
   partition;
4. a matchable but non-superregular ambient endpoint host before rectangle
   extraction.

Sublinear unary maximum degree, arbitrary signed rectangle signatures, bounded
local contradictions, and irregular local cross hosts are no longer separate
obstructions.