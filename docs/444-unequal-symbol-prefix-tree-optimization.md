# Unequal-symbol prefix-tree optimization

`docs/438` optimizes prefix codes when every schedule symbol has the same
retention factor.  Actual corridor marker moves may have different survival
probabilities.  This chapter reduces that asymmetric problem to a finite exact
search over ordered full prefix trees.

## 1. Fixed-tree assignment

Let a binary symbol `0` retain mass `p_0` and symbol `1` retain mass `p_1`.
A leaf word `w` has survival

```text
P(w)=product_(s in w) p_s.
```

Bank `i` has uncoded risk `rho_i`; assigning it to `w` gives coded risk
`rho_i/P(w)`.

### Theorem PP3cbs -- PROVED / SORTED LEAF ASSIGNMENT

For a fixed prefix tree, an optimal minimax assignment pairs larger bank risks
with larger leaf survivals.  If

```text
rho_1>=...>=rho_K,
P_1>=...>=P_K,
```

then the optimum on that tree is

```text
max_i rho_i/P_i.
```

#### Proof

Consider an inversion with `rho_a>=rho_b` but `P_a<P_b`.  Swapping the two
banks cannot increase the larger of the two ratios, since both
`rho_a/P_b<=rho_a/P_a` and `rho_b/P_a<=rho_a/P_a`.  Remove inversions until the
orders agree. ∎

## 2. Finite tree search

### Theorem PP3cbt -- PROVED / REDUCED TREE DEPTH BOUND

With `K` banks, an optimal binary prefix tree may be chosen full, with exactly
`K-1` internal nodes and depth at most `K-1`.  Hence the unequal-symbol minimax
risk is obtained by a finite search over ordered full binary trees with `K`
leaves, followed by the sorted assignment from `PP3cbs`.

#### Proof

Suppress every unary internal node; this only shortens descendant words and
increases their survival.  A full binary tree with `K` leaves has `K-1` internal
nodes, so no root-to-leaf path contains more than `K-1` internal nodes. ∎

## 3. Exact feasibility certificate

### Theorem PP3cbu -- PROVED / ASYMMETRIC PREFIX-TREE CERTIFICATE

A proposed risk `R` is feasible exactly when some ordered full binary tree with
`K` leaves has sorted survivals `P_1>=...>=P_K` satisfying

```text
P_i>=rho_i/R
```

for all sorted bank risks `rho_i`.  A tree and its sorted leaf assignment form a
complete finite certificate.

#### Proof

Necessity is the definition of coded risk.  Sufficiency follows by assigning
banks and leaves in sorted order.  Finiteness follows from `PP3cbt`. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_unequal_symbol_prefix_trees.py
```

For `p_0=2/3`, `p_1=1/2`, and five unequal bank risks, the script enumerates all
fourteen ordered full binary trees and all `5!` assignments per tree.  It finds
exact optimum `2/3` with codewords

```text
00, 01, 11, 100, 101.
```

The next theorem identifier after this chapter is `PP3cbv`.
