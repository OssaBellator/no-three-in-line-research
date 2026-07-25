# Unit Hall wall factorisation has finite tree-wide stock

CMR734--CMR740 replace one essential-return host of side `m` by two exact factor
hosts of sides `a,b` satisfying

\[
a+b=m-1.
\]

This chapter aggregates that identity over the complete branching factor tree.
The total side mass decreases by one at every split, so essential-return
factorisation cannot create an unbounded binary recursion. Its node, edge,
token, and certificate stocks are explicit polynomials in the initial side.

Start with one factor host of side `d`. Whenever a current node has an essential
returned target edge and its canonical unit Hall wall, apply CMR735 and replace
the node by its positive-side factor children. Zero-side factors are discarded.
Other matching-preserving deletions may occur inside nodes but do not increase
any stock below.

## 1. Total factor-side mass decreases exactly by one

Let `mathcal F_j` be the current forest of active factor nodes after `j` unit-wall
splits, and put

\[
S_j=\sum_{H\in\mathcal F_j}\operatorname{side}(H).
\]

### Theorem CMR741 -- PROVED

Every unit-wall split satisfies

\[
\boxed{S_{j+1}=S_j-1.}
\]

Consequently

\[
\boxed{S_j=d-j.}
\]

### Proof

A split removes one node of side `m` and inserts children of sides `a,b` with
`a+b=m-1` by CMR736. All other nodes are unchanged. ∎

The identity is independent of how unbalanced the wall is.

## 2. Split, node, leaf, and depth bounds

### Theorem CMR742 -- PROVED

The complete unit-wall factor tree has:

1. at most `d` split nodes;
2. at most `2d+1` created nodes, including zero-side children before they are
   discarded;
3. at most `d+1` leaves;
4. root-to-leaf depth at most `d`.

Every positive child has side strictly smaller than its parent.

### Proof

CMR741 shows that each split lowers the nonnegative side mass by one, so there
are at most `d` splits. A binary split creates at most two children, yielding at
most `1+2d` total nodes and at most one more leaf than split nodes. Along a path,
CMR736 lowers positive side by at least one, so the depth is at most `d`. ∎

Thus branching does not evade strict side descent.

## 3. Cubic tree-wide host-edge stock

For a node `v`, write `m_v` for its side. Define

\[
E_{\mathrm{tree}}(d)
=
\sum_v m_v^2.
\]

### Theorem CMR743 -- PROVED

Every unit-wall factor tree satisfies

\[
\boxed{
E_{\mathrm{tree}}(d)
\le
\sum_{j=1}^{d}j^2
=
\frac{d(d+1)(2d+1)}6.
}
\]

Hence the total owner-labelled physical factor-edge stock over all nodes is at
most this quantity.

### Proof

Let

\[
F(m)=\sum_{j=1}^{m}j^2.
\]

The function `F` is superadditive on nonnegative integers: if `a,b>=0`, then

\[
F(a+b)-F(a)-F(b)
=
\sum_{j=1}^{b}\bigl((a+j)^2-j^2\bigr)
\ge0.
\]

Induct on the root side. If the root does not split, its contribution is at most
`d^2<=F(d)`. If it splits into sides `a,b` with `a+b=d-1`, the inductive bound is

\[
d^2+F(a)+F(b)
\le
d^2+F(d-1)
=F(d).
\]

Every side-`m_v` host has at most `m_v^2` edges. ∎

The extremal stock is attained by a completely unbalanced chain of sides
`d,d-1,...,1`.

## 4. Exact tree-wide full-token stock

Assume the ambient inherited parent has side `p^h`.

### Theorem CMR744 -- PROVED

The total owner-labelled nonroot full-token stock attached to all factor edges
in the unit-wall tree is at most

\[
\boxed{
(p+1)(h-1)
\frac{d(d+1)(2d+1)}6.
}
\]

For a history of episodes carrying at least `Q>=1` tree-owner edge witnesses
each and an integer `mu>=2`, at least one of the following holds.

1. One exact owner-edge pair occurs in at least `mu` episodes.
2. 
   \[
   \boxed{
   J
   \le
   \frac{(\mu-1)E_{\mathrm{tree}}(d)}{Q}.
   }
   \]

### Proof

CMR413 assigns exactly `(p+1)(h-1)` labelled nonroot token incidences to each
physical edge, with owner and multiplicity retained. Apply CMR743. The recurrence
bound is incidence double counting against the finite owner-edge stock. ∎

A recurrent owner edge enters the established reintroduction and recreation
ledgers; it is not declared fresh.

## 5. Tree-wide target-certificate stock

At a node of side `m`, there are at most `binom(m^2,3)` physical three-edge
certificate signatures.

### Theorem CMR745 -- PROVED

The owner-labelled certificate stock over the whole unit-wall factor tree is at
most

\[
\boxed{
C_{\mathrm{tree}}(d)
\le
\sum_{j=1}^{d}\binom{j^2}{3}.
}
\]

For every integer `nu>=2`, a history of `K` owner-labelled certificate episodes
reaches one of:

1. one exact certificate in at least `nu` episodes;
2. 
   \[
   \boxed{
   K
   \le
   (\nu-1)C_{\mathrm{tree}}(d).
   }
   \]

### Proof

Let

\[
G(m)=\sum_{j=1}^{m}\binom{j^2}{3}.
\]

Its summands are nondecreasing, so the same shifted-sum argument as in CMR743
gives `G(a)+G(b)<=G(a+b)`. Induction over a split `a+b=m-1` gives the displayed
stock. The history bound is the pigeonhole principle. ∎

Collinearity, compatibility, and host sparsity only reduce the count.

## 6. Tree-wide monotone deletion stock

At each node, CMR740 uses at most the number of factor edges at that node as
matching-preserving target deletions.

### Theorem CMR746 -- PROVED

Across the entire unit-wall factor tree, the total number of monotone local edge
deletions performed by all CMR740 normalisations is at most

\[
\boxed{
E_{\mathrm{tree}}(d)
\le
\frac{d(d+1)(2d+1)}6.
}
\]

If a deleted physical edge later returns under the same absolute parent
coordinates, it enters CMR715 and CMR720--CMR733 as reintroduction or owner
change rather than another fresh deletion.

### Proof

A node deletes each of its current physical edges at most once before its host
owner changes or the node splits. Sum the node edge stocks and apply CMR743. The
return statement is the cited deletion-ancestry ledger. ∎

## 7. Unit-wall factor-tree endpoint

### Corollary CMR747 -- PROVED

Every execution generated by repeated essential-return unit walls reaches at
least one of the following after finite tree-wide stock.

1. A forced target certificate converted into the target closure.
2. A matching-preserving deletion inside a strict wall factor.
3. Strict contraction of an essential edge.
4. Pure or mixed obstruction inside lower-dimensional factors, handled by the
   product and child recursions CMR629--CMR705.
5. One recurrent owner edge or owner-labelled certificate.
6. Genuine edge reintroduction, routing change, envelope change, or another
   finite owner transition.
7. Exhaustion of all positive factor-side mass after at most `d` wall splits.

Thus branching essential-return factorisation has finite cubic edge/token stock
and finite certificate stock. It cannot be an unbounded source of new matching
owners. The remaining prime-power frontier is dynamic conversion of recurrent
edge, token, and target signatures against the protected reserve and inherited
parent budgets.

### Proof

Combine the exact local endpoint CMR740 with the mass, node, edge, token,
certificate, and deletion stocks CMR741--CMR746. ∎

No all-`n` theorem is claimed. Split-tree mass, superadditive stock bounds, and
recurrence arithmetic are checked in
[`scripts/verify_prime_power_unit_wall_factor_tree.py`](../scripts/verify_prime_power_unit_wall_factor_tree.py).
