# Superregular installation of common-line rectangles

The exact installation theorem PP3om requires a residual perfect matching after
rectangle resources are reserved. In a superregular endpoint host this residual
matching is automatic for every sufficiently small linear subbank. The only new
unary issue is whether the opposite rectangle diagonal belongs to the host.

The adaptive source-validity preparation also survives this reservation. Hence
the residual matching may be chosen no-three against the retained source before
the rectangle variables are exposed.

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
  had size at least \(\epsilon q\), lower regularity would give an edge from
  \(X\) to that complement. Hence \(|N(X)|>q'-\epsilon q\ge|X|\).
- If \(|X|>q'-\epsilon q\) and some right vertex had no neighbor in \(X\), all
  its neighbors would lie in a set of size below \(\epsilon q\), contradicting
  its residual degree.

Thus Hall's condition holds. ∎

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

## 4. Source-valid residual matching

Assume the endpoint bank has undergone the adaptive preparation PP3nr. Thus all
unary-invalid endpoint arcs and anchored transitions have been removed by
resource deletion, while the normalized support-rank-four anchored-pair and
support-rank-at-least-four inserted-triple expression is \(o(1)\).

Let \(q_0\) be the residual side size after rectangle resources are reserved, and
assume

\[
q_0\ge\nu q
\]

for a fixed constant \(\nu>0\).

### Theorem PP3ov -- PROVED FROM PP3ip AND SR1

The residual source-safe host contains a perfect matching \(M_0\) such that the
retained source together with the cells of \(M_0\) is no-three-in-line.

Moreover, the uniform residual perfect-matching law has fixed-rank probability
\(O_\nu(q_0^{-r})\), and conditioning on source validity preserves this bound up
to a constant factor for every fixed rank.

#### Proof

After PP3nr there is no unary-invalid arc among retained resources. Excluding the
surviving original endpoint edges removes only a partial matching, so the
forbidden complement of the residual host has maximum degree at most one.
Because \(q_0\to\infty\), PP3ip makes this residual host superregular with density
\(1-o(1)\). SR1 therefore gives a constant \(K=K(\nu)\) such that every
prescribed residual matching of fixed rank \(r\) occurs with probability at most
\((K/q_0)^r\).

Reserving rectangle resources can only decrease every anchored-pair and
inserted-triple pattern count. Replacing denominator \(q\) by
\(q_0\ge\nu q\) changes the normalized rank-two and rank-three expressions by
at most \(\nu^{-2}\) and \(\nu^{-3}\). Their sum remains \(o(1)\).

The expected number of remaining source-invalid anchored pairs and inserted
triples in a uniform residual perfect matching is therefore \(o(1)\). Unary
source-invalid arcs and transitions are absent by construction, so a residual
source-valid perfect matching exists.

The source-valid event has probability \(1-o(1)\). Dividing any fixed-rank
cylinder probability by this probability preserves the
\(O_\nu(q_0^{-r})\) bound. ∎

This matching absorbs every source-validity condition involving only residual
matching cells. It may contribute a fixed base amount to the shadow-cost
objective, but it creates no empty geometric clause.

## 5. Rectangle variables after residual preparation

### Corollary PP3ow -- PROVED

In the cross-safe adaptively prepared branch, choose the residual matching
\(M_0\) from PP3ov and fix it before exposing rectangle states. Then:

1. every no-three violation containing only retained-source points and residual
   matching cells is absent;
2. every remaining geometric clause contains at least one rectangle variable;
3. the exact clause rank remains at most three;
4. the exact shadow change remains a degree-at-most-two pseudo-Boolean function,
   with the residual matching contribution absorbed into its constant and unary
   state tables.

Consequently common-line rectangle conversion is reduced to finding a satisfying
rectangle-state assignment with negative exact cost. Residual matching and
residual source validity are no longer separate obstructions.

#### Proof

The first statement is PP3ov. Apply PP3on after adding the fixed residual
matching cells to the retained set \(F\). Any forbidden triple not already
excluded must meet at least one variable support, and it meets at most three.
The shadow decomposition PP3oo allows fixed residual cells to contribute to the
constant term or to unary costs involving one rectangle state; pairs of rectangle
cells contribute binary costs. ∎

## 6. Revised dense-host endpoint

### Corollary PP3ox -- PROVED

For an adaptively prepared endpoint host, the common-line rectangle branch has
the following exact alternatives.

1. A linear cross-safe rectangle bank is saturation- and source-validity-
   installable. The only remaining task is a satisfiable negative-cost assignment
   for its rank-at-most-three CNF and quadratic shadow objective.
2. The unary forbidden support contains a linear matching of cross cells.

The genuinely separate residual-host issue is confined to endpoint hosts that
remain matchable but do not admit the near-complete adaptive cleanup.