# Canonical augmentation of prefix-code shapes

`docs/492` counts labelings on one fixed marker tree.  The tree shape itself may
also be chosen.  This chapter generates rooted non-plane full binary prefix-tree
shapes without duplicates and filters them by the exact survival objective.

A leaf is encoded by `L`.  An internal node with child encodings `u,v` is encoded
by the ordered pair `(min(u,v),max(u,v))` under one fixed total order.

## 1. Canonical shape representatives

### Theorem PP3chy -- PROVED / UNIQUE UNORDERED-TREE ENCODING

Two rooted full binary trees are isomorphic after arbitrary child swaps if and
only if their recursive canonical encodings are equal.  Thus each unordered
prefix-tree shape has one canonical representative.

#### Proof

At a leaf the claim is immediate.  Inductively, an isomorphism matches the
unordered pair of child isomorphism classes, and sorting their unique encodings
produces the same parent encoding.  Conversely, equal sorted child encodings
inductively give child isomorphisms and hence a parent isomorphism. ∎

## 2. Isomorph-free augmentation

### Theorem PP3chz -- PROVED / UNORDERED SPLIT RECURRENCE

Let `T_n` be the canonical shapes with `n` leaves.  Then

```text
T_1={L},
T_n={canon(u,v):u in T_i, v in T_(n-i), 1<=i<=n-i}.
```

Set insertion removes the residual duplicates when `i=n-i`.  The ordinary
generating function `T(z)=sum_(n>=1)|T_n|z^n` satisfies

```text
T(z)=z+(T(z)^2+T(z^2))/2.
```

#### Proof

Every nontrivial full binary tree has a root split into two smaller unordered
full binary trees.  Ordering by leaf count and then canonical encoding selects
one orientation.  Conversely every listed pair creates one valid tree.  The
Pólya term `(T(z)^2+T(z^2))/2` counts unordered pairs with the diagonal corrected
by the substitution `z->z^2`. ∎

## 3. Optimal-shape filtering

### Theorem PP3cia -- PROVED / FINITE OPTIMAL ORBIT CERTIFICATE

For fixed leaf number and any automorphism-invariant rational Bellman objective,
canonical shapes can be evaluated exactly and filtered to the optimal shape
orbits.  Storing the canonical representatives and their recursive objective
values is a complete finite certificate.

#### Proof

There are finitely many canonical shapes at fixed leaf number.  The Bellman
recurrence is invariant under child swaps and uses rational data, so each shape
has an exact value.  Exhaustive comparison proves optimality; recursive replay
localizes any failed value or shape claim. ∎

## 4. Stored exact fixture

The audit `scripts/check_canonical_prefix_tree_augmentation.py` obtains the shape
counts

```text
1,1,1,2,3,6,11,23
```

for one through eight leaves.  With six equal-risk banks and equal binary symbol
survivals `1/2`, the objective is `2^(maximum depth)`.  Among six canonical
six-leaf shapes, exactly two have minimum height three and attain optimum eight.

## 5. Prime-patching consequence

Code search can now vary both leaf assignments and the marker-tree shape without
revisiting isomorphic trees.  The output is an explicit optimal shape orbit,
ready for the labeling and cycle-index machinery developed in the preceding
chapters.
