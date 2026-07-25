# Superregular installation of common-line rectangles

The exact installation theorem PP3om requires a residual perfect matching after
rectangle resources are reserved. In a superregular endpoint host this residual
matching is automatic for every sufficiently small linear subbank. The only new
unary issue is whether the opposite rectangle diagonal belongs to the host.

## 1. Robust perfect matching after balanced vertex deletion

Let \(G=(L,R;E)\) be an \((\epsilon,d)\)-superregular balanced bipartite graph
with \(|L|=|R|=q\). Thus every vertex has degree at least \(dq\), and every pair
of subsets of size at least \(\epsilon q\) has edge density at least
\(d-\epsilon\).

### Proposition PP3or -- PROVED

Assume

\[
0<\eta<d-\epsilon.
\]

Delete at most \(\eta q\) vertices from each side, leaving equal side sizes.
Then the residual graph has a perfect matching.

#### Proof

Write the residual side size as \(q'\). Every remaining vertex has degree at
least

\[
(d-\eta)q>\epsilon q.
\]

Let \(X\) be a subset of the residual left side.

- If \(|X|\le\epsilon q\), one vertex of \(X\) has at least
  \((d-\eta)q\ge|X|\) residual neighbors.
- If \(\epsilon q<|X|\le q'-\epsilon q\) and the complement of \(N(X)\)
  had size at least \(\epsilon q\), superregular density would give an edge from
  \(X\) to that complement, a contradiction. Hence
  \(|N(X)|>q'-\epsilon q\ge|X|\).
- If \(|X|>q'-\epsilon q\) and some right vertex had no neighbor in \(X\), all
  its neighbors would lie in a set of size below \(\epsilon q\), contradicting
  its residual degree.

Thus Hall's condition holds. ∎

The argument uses only lower regularity and minimum degree.

## 2. Cross-safe rectangles

Let \(\mathcal Q\) be the resource-disjoint rectangle bank from PP3ok. A
rectangle is **cross-safe** when both cells of its opposite diagonal \(D_s^1\)
are edges of the source-safe endpoint host \(G\).

### Theorem PP3os -- PROVED

Suppose \(|\mathcal Q|\ge cq\) for fixed \(c>0\). At least one of the following
holds.

1. There are at least \(cq/2\) cross-safe rectangles.
2. The unary forbidden complement of \(G\) contains a matching of size at least
   \(cq/2\), with one forbidden cross cell chosen from each of that many
   rectangles.

#### Proof

If fewer than half the rectangles are cross-safe, at least \(cq/2\) rectangles
have a forbidden cell on their opposite diagonal. Choose one such cell from each.
Distinct rectangles use disjoint endpoint resources, so the chosen cells form a
matching. ∎

Thus failure of opposite-diagonal safety is itself a linear unary obstruction,
not diffuse collateral.

## 3. Automatic residual completion

### Corollary PP3ot -- PROVED

Assume alternative 1 of PP3os and choose a constant

\[
0<\xi<\min\{c/2,(d-\epsilon)/2\}.
\]

Select any \(k=\lfloor\xi q\rfloor\) cross-safe rectangles. Reserve their two
left and two right resources. Then:

1. the residual endpoint host has a perfect matching;
2. every choice of one diagonal in each rectangle, restricted to host-supported
   diagonals, extends to a complete endpoint permutation;
3. choosing the cross diagonal in every selected rectangle is a valid host
   matching before higher-rank source and patch constraints are imposed.

#### Proof

The reservation deletes \(2k\le2\xi q<(d-\epsilon)q\) vertices from each side.
Apply PP3or with \(\eta=2\xi\). The remaining statements are PP3om and the
definition of cross-safe. ∎

This removes residual matching as a separate issue in the superregular branch.

## 4. Revised dense-host endpoint

### Corollary PP3ou -- PROVED

For a superregular source-safe endpoint host, the common-line rectangle branch
has the following exact alternatives.

1. A linear cross-safe rectangle bank is saturation-installable, and the
   remaining problem is the rank-at-most-three geometric CSP with negative
   quadratic shadow cost from PP3on--PP3op.
2. The unary forbidden support contains a linear matching of cross cells.

If the first branch fails after installation, the failure is geometric-CSP or
paid-cost concentration. If the second branch occurs, it joins the existing
unary Hall/matching obstruction rather than creating a new class.

The genuinely separate residual-host issue is therefore confined to matchable
but non-superregular endpoint hosts.