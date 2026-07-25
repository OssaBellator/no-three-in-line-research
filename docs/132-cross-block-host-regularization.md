# Cross-block host regularization

PP3qy reduces a credit-poor homogeneous rectangle bank to paired four-state
cross-block supervariables.  The remaining local obstruction is an exact
\(2\)-by-\(2\) Hall failure after unary source restrictions and one designated
recapture exclusion in each owner direction.

When the underlying unary-forbidden endpoint graph has sublinear maximum degree,
such failures are sparse.  Almost the entire rectangle bank can be paired into
safe cross-block supervariables.

## 1. One directional failure needs a genuine unary edge

Let \(F\) be the simple unary-forbidden endpoint graph coming from collisions,
fixed-source secants, and any other non-designated unary restriction.  Assume
its maximum left and right degree is at most \(d\).

For two resource-disjoint rectangles \(s,t\), consider the direction

\[
L_s\longrightarrow R_t.
\]

Before unary pruning this is \(K_{2,2}\).  Direct designated recapture for owner
\(s\) removes at most one cell in its distinguished owner column.

### Proposition PP3qz -- PROVED

If the directional safe host \(H_{s\to t}\) has no perfect matching, then
\(F\cap(L_s\times R_t)\) is nonempty.

The transposed statement holds for \(H_{t\to s}\).

#### Proof

Deleting no recapture cell leaves \(K_{2,2}\), which has a perfect matching.
Deleting one recapture cell leaves a three-edge \(K_{2,2}\), which also has a
perfect matching.  Therefore failure after all restrictions requires at least
one additional unary-forbidden edge from \(F\). ∎

This separates the unavoidable one-per-owner recapture restriction from the
true source-safe obstruction.

## 2. Bad-partner degree

Form a graph \(\mathcal B\) on the rectangle variables, joining \(s,t\) when at
least one of the two directional hosts \(H_{s\to t},H_{t\to s}\) has no perfect
matching.

### Theorem PP3ra -- PROVED

Every rectangle has degree at most

\[
\boxed{4d}
\]

in \(\mathcal B\).

#### Proof

Fix rectangle \(s\).

For a forward failure \(H_{s\to t}\), PP3qz supplies an edge of \(F\) between one
of the two left resources in \(L_s\) and one of the two right resources in
\(R_t\).  The right-resource pairs \(R_t\) are disjoint across the rectangle
bank.  The two vertices of \(L_s\) have total \(F\)-degree at most \(2d\).
Hence at most \(2d\) partners \(t\) can fail in the forward direction.

For a reverse failure \(H_{t\to s}\), charge the required \(F\)-edge to one of
the two right resources in \(R_s\).  Their total right degree is at most \(2d\),
so at most another \(2d\) partners fail in the reverse direction.  Add the two
bounds. ∎

No multiplicity assumption is needed: one forbidden cell belongs to one unique
cross block because the rectangle resource pairs are disjoint.

## 3. Pairing almost the entire bank

Let the credit-poor homogeneous bank have \(h\) rectangles.  A **good pair** is
a nonedge of \(\mathcal B\), equivalently a pair for which both directional safe
hosts have perfect matchings.

### Proposition PP3rb -- PROVED

There is a matching of good pairs that leaves at most

\[
4d+1
\]

rectangles unmatched.

#### Proof

Take a maximal matching in the good-pair graph.  Its unmatched vertex set \(U\)
is independent in the good graph, so every pair of vertices in \(U\) is an edge
of the bad-pair graph \(\mathcal B\).  Thus \(U\) is a clique in a graph of
maximum degree at most \(4d\).  Hence

\[
|U|\le4d+1.
\]

∎

In particular, if \(d=o(h)\), then

\[
(1-o(1))\frac h2
\]

pairwise resource-disjoint good cross-block supervariables exist.

## 4. Sparse-unary bypass of the credit-poor signature

### Theorem PP3rc -- PROVED

Let a credit-poor homogeneous rectangle bank have size \(h\to\infty\).  Suppose
the non-designated unary-forbidden endpoint graph has maximum degree

\[
d=o(h).
\]

Then, after discarding \(o(h)\) rectangles, the bank may be partitioned into
resource-disjoint pairs, each with a nonempty source-safe cross-block state set.
Every paired block:

- is an equal-margin finite-state supervariable;
- moves both designated owner endpoints;
- has removal credit at least two;
- avoids direct recapture of both designated owner units in every retained safe
  state.

#### Proof

Apply PP3rb and then PP3qu--PP3qv to every good pair.  The safe host definition
already includes direct recapture exclusions. ∎

Thus sparse unary source geometry completely removes the local \(2\)-by-\(2\)
Hall obstruction.

## 5. Revised credit-poor endpoint

### Corollary PP3rd -- PROVED

The credit-poor homogeneous signature has the following exact alternatives.

1. **Sparse-unary multistate bank.**  If \(d=o(h)\), almost all rectangles pair
   into safe four-state supervariables.  The remaining task is their
   rank-at-most-three multistate clause mass and unary/binary paid cost.
2. **Unary endpoint concentration.**  Some endpoint resource has
   
   \[
   \Omega(h)
   \]
   
   non-designated unary-forbidden cross-block cells.
3. **Multistate collateral concentration.**  Safe cross-block states exist on a
   linear paired bank, but every product or local-lemma selection has geometric
   bad-box mass or insertion cost comparable to its two-per-block credit.

The original credit-poor Boolean signature and its local cross-block Hall
problem are therefore closed under sparse unary degree.  The remaining
obstruction is again a unary endpoint star or a multistate weighted core.