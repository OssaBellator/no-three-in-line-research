# Subset dynamic programming for unequal-symbol codes

`docs/444` reduces unequal symbol survivals to a finite prefix-tree search. A
simple interval recurrence is not valid in general because the leaf survivals
of the two root subtrees may interleave. This chapter gives the correct exact
subset dynamic program.

## 1. Fixed-tree assignment

Let bank `i` have base risk `rho_i`. A leaf `w` has survival

```text
s(w)=product_(a in w) p_a,
```

and contributes risk `rho_i/s(w)`.

### Theorem PP3cck -- PROVED / SORTED LEAF ASSIGNMENT

For a fixed prefix tree, an optimal assignment pairs larger bank risks with
larger leaf survivals.

#### Proof

Suppose `rho_i<=rho_j` and `s_a<=s_b`. A crossed assignment has term
`rho_j/s_a`, which dominates both terms after pairing the smaller risk with the
smaller survival and the larger risk with the larger survival. Repeating
adjacent exchanges gives the sorted assignment. ∎

## 2. Exact subset recurrence

For a nonempty bank set `S`, let `V(S)` be the optimal minimax risk of a binary
prefix tree rooted at survival one. Then `V({i})=rho_i`.

### Theorem PP3ccl -- PROVED / UNEQUAL-SYMBOL SUBSET DP

For `|S|>=2`,

```text
V(S)=min_(empty!=A proper subset S)
 min(
   max(V(A)/p_0, V(S\A)/p_1),
   max(V(A)/p_1, V(S\A)/p_0)
 ).
```

#### Proof

The two children of the root partition the bank set into two nonempty parts.
Placing a subtree below symbol `a` scales its optimum by `1/p_a`. The two terms
cover both child orientations. Conversely, joining optimal subtrees for any
partition realizes the displayed value. ∎

## 3. Exact reconstruction

### Theorem PP3ccm -- PROVED / FINITE TREE ORACLE

The recurrence evaluates all `2^K-1` nonempty bank subsets with `O(3^K)` exact
rational transitions, reconstructs an optimal prefix tree, and never needs depth
more than `K-1`.

#### Proof

Across all subsets, ordered root partitions are counted by the three choices
"left, right, absent" for each bank. Back-pointers reconstruct the minimizing
partition and orientation. Every full binary tree with `K` leaves has a reduced
representative of depth at most `K-1`. ∎

## Frontier consequence

Unequal marker survivals now have an exact dynamic program rather than a Catalan
tree enumeration. The state space is exponential only in the number of banks,
which is the finite corridor-type quotient rather than the ambient grid size.
