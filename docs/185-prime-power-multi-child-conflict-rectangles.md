# Cross-child conflicts form low-rank boxes in one fixed routing product

CMR656--CMR663 reduce every recurrent pure factor to one fixed vertex-routing
skeleton.  Under that skeleton the matching family is an exact product of
matching hosts lying in strict child prefix cells.  This chapter records how the
candidate-conflict potential interacts with that product.

Fix a finite index set `A` of nonempty child factors.  For each `a in A`, let
`H_a` be a balanced bipartite host of side `d_a` with at least one perfect
matching, and put

\[
\mathcal P_a=\operatorname{PM}(H_a),
\qquad
 d=\sum_{a\in A}d_a.
\]

The child factors have pairwise disjoint source sets and pairwise disjoint target
sets.  A product state is

\[
M(\mathbf P)=\bigcup_{a\in A}P_a,
\qquad
\mathbf P=(P_a)_{a\in A}\in\prod_{a\in A}\mathcal P_a.
\]

All edges retain their original parent-grid coordinates.  A **candidate atom**
is a compatible collinear triple of host edges.  It is **pure** when all three
edges lie in one child factor and **mixed** otherwise.

## 1. Exact pure/mixed decomposition

For a state `M(\mathbf P)`, let `X_a(P_a)` count candidate conflicts contained
in child factor `a`, and let `X_\times(\mathbf P)` count mixed conflicts.

### Theorem CMR664 — PROVED

For every product state,

\[
\boxed{
X(M(\mathbf P))
=
\sum_{a\in A}X_a(P_a)+X_\times(\mathbf P).
}
\]

The summands are pairwise disjoint and exhaustive.

### Proof

Every three-edge subset of the disjoint union of child edge sets has a unique
support set of child factors.  Its support has size one precisely in the pure
case and size at least two precisely in the mixed case.  Restrict this partition
to compatible collinear triples. ∎

## 2. Exact child-rank vectors

For a mixed atom `T`, define

\[
r_a(T)=|T\cap E(H_a)|.
\]

### Theorem CMR665 — PROVED

Every mixed atom has one of the two rank patterns

\[
\boxed{(2,1)}
\qquad\text{or}\qquad
\boxed{(1,1,1)},
\]

up to permutation of the child labels.  In particular,

\[
\boxed{0\le r_a(T)\le2}
\]

for every child factor.

### Proof

The positive ranks are positive integers summing to three.  Mixedness requires
at least two positive parts.  The only resulting integer partitions are
`2+1` and `1+1+1`. ∎

Thus cross-child geometry never creates a prescription of rank three inside one
child factor.

## 3. Occurrence is an exact Cartesian box

For a mixed atom `T`, put

\[
T_a=T\cap E(H_a)
\]

and define

\[
\mathcal P_a(T_a)
=
\{P\in\mathcal P_a:T_a\subseteq P\}.
\]

When `T_a` is empty, interpret `\mathcal P_a(T_a)=\mathcal P_a`.

### Theorem CMR666 — PROVED

The complete product-state family containing `T` is exactly

\[
\boxed{
\mathcal B_T
=
\prod_{a\in A}\mathcal P_a(T_a).
}
\]

Hence `T` is active in the product if and only if every nonempty child
prescription `T_a` extends to a perfect matching of `H_a`.

### Proof

The child edge sets are disjoint.  Therefore `T` is contained in the union
`\bigcup_aP_a` exactly when every local part `T_a` is contained in its local
matching `P_a`.  These conditions are independent across the factors. ∎

## 4. Sparse mixed-atom stock relative to one child

Fix a distinguished child `a_*` of side `d_*` and put

\[
v=d-d_*.
\]

Let `R_*` be the union of all host edges outside `H_{a_*}`.

### Theorem CMR667 — PROVED

Every mixed atom contains at least one edge of `R_*`, and

\[
\boxed{|R_*|\le v^2.}
\]

Consequently the complete mixed-atom stock obeys

\[
\boxed{
N_\times
\le
|R_*|\binom{d^2-1}{2}
\le
v^2\binom{d^2-1}{2}.
}
\]

If `v=0`, there are no mixed atoms.

### Proof

An atom containing no outside edge would lie wholly in the distinguished child
and would be pure.  The outside factors have sides summing to `v`; their edge
stock is at most

\[
\sum_{a\ne a_*}d_a^2
\le
\left(\sum_{a\ne a_*}d_a\right)^2
=v^2.
\]

Choose one canonical outside edge of the atom and then overcount the other two
edges from the complete `d^2`-cell factor board. ∎

The bound is intentionally coarse but depends polynomially on the total side
and quadratically on the outside side.

## 5. Dirty clean-factor products concentrate on one box

For each child, let

\[
\mathcal C_a
=
\{P\in\mathcal P_a:X_a(P)=0\}
\]

be its pure-conflict-free matching family.  Assume every `\mathcal C_a` is
nonempty.

### Theorem CMR668 — PROVED

If every state in

\[
\mathcal C=\prod_{a\in A}\mathcal C_a
\]

contains a mixed conflict, then some active mixed atom `T` satisfies

\[
\boxed{
|\mathcal B_T\cap\mathcal C|
\ge
\frac{|\mathcal C|}{N_\times}.
}
\]

Equivalently,

\[
\boxed{
\prod_{a\in A}
\frac{|\mathcal C_a\cap\mathcal P_a(T_a)|}{|\mathcal C_a|}
\ge
\frac1{N_\times}.
}
\]

For every child touched by `T`, its individual occurrence fraction is therefore
at least `1/N_\times`.

### Proof

By CMR664, a state in `\mathcal C` is dirty only through a mixed atom.  The
active mixed-atom boxes from CMR666 cover `\mathcal C`.  There are at most
`N_\times` of them, so one box contains at least the displayed average.  The
box cardinality factors over the children.  Since every factor fraction is at
most one, a product at least `1/N_\times` forces each nontrivial factor fraction
to be at least `1/N_\times`. ∎

## 6. Distinguished-child low-rank alternative

### Theorem CMR669 — PROVED

For the atom supplied by CMR668, exactly one of the following holds relative to
`a_*`.

1. **Outside-product trigger.**  `T_{a_*}` is empty, so the complete atom lies in
   the product of the outside child factors, of total side `v<d`.
2. **Rank-one child trigger.**  `|T_{a_*}|=1`, and at least a
   `1/N_\times` fraction of `\mathcal C_{a_*}` contains that edge.
3. **Rank-two child trigger.**  `|T_{a_*}|=2`, and at least a
   `1/N_\times` fraction of `\mathcal C_{a_*}` contains that compatible pair.

### Proof

CMR665 gives rank zero, one, or two in the distinguished child.  Rank zero gives
the first branch.  In the positive-rank cases apply the final assertion of
CMR668. ∎

Thus the many-factor product never hides a high-rank obstruction in a selected
large child.

## 7. Essentiality action on one active box

### Theorem CMR670 — PROVED

Let `T` be any active mixed atom.

1. If every edge of every nonempty prescription `T_a` is essential in `H_a`,
   then `T` belongs to every state of the complete child product.
2. Otherwise some edge `e in T_a` is nonessential in its child host.  Deleting
   `e` from `H_a` preserves at least one perfect matching and destroys the
   complete occurrence box `\mathcal B_T`.

### Proof

In the first branch, every local perfect matching contains every local edge of
`T`, so CMR666 gives the full product as the occurrence box.

In the second branch, by definition of nonessentiality there is a perfect
matching of `H_a` avoiding `e`; hence `H_a-e` remains matchable.  No state of
the reduced product can contain all of `T`, because the selected edge is absent
from its host. ∎

This is the multi-child form of the matching-preserving deletion versus forced-
certificate dichotomy.  The finite iteration is recorded in CMR677--CMR683.

No all-`n` theorem is claimed.  Rank vectors, occurrence boxes, atom-stock
bounds, dirty-product averaging, and the essentiality action are checked in
[`scripts/verify_prime_power_multi_child_conflicts.py`](../scripts/verify_prime_power_multi_child_conflicts.py).
