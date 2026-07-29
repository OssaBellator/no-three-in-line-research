# Pruned subset search for unequal-symbol codes

`docs/450` gives the correct `O(3^K)` subset dynamic program for unequal symbol survivals. This chapter adds a generalized Kraft lower bound, a finite exact risk oracle, and safe branch pruning.

Let the two symbol survival factors be `p_0,p_1 in (0,1)`. Bank `i` has base risk `rho_i`. A codeword `w` has survival

```text
P(w)=product_(s in w) p_s,
```

and realized risk `rho_i/P(w)`.

## 1. Generalized Kraft lower bound

There is a unique `theta>0` satisfying

```text
p_0^theta+p_1^theta=1.
```

### Theorem PP3cdc -- PROVED / SURVIVAL-KRAFT LOWER BOUND

For every complete binary prefix code with one leaf per bank,

```text
sum_i P(w_i)^theta=1.
```

Consequently every code of maximum risk `R` satisfies

```text
R>=(sum_i rho_i^theta)^(1/theta).
```

#### Proof

The leaf identity follows by induction on the full binary tree: replacing one node of weight `P^theta` by its two children preserves total weight because `p_0^theta+p_1^theta=1`. If `rho_i/P(w_i)<=R`, then `P(w_i)^theta>=(rho_i/R)^theta`. Summing gives the lower bound. ∎

## 2. Finite exact decision oracle

### Theorem PP3cdd -- PROVED / FINITE RISK CANDIDATES

With `K` banks, an optimal full binary tree has depth at most `K-1`. Therefore the exact optimum belongs to the finite set

```text
{rho_i/(p_0^a p_1^b):
  1<=i<=K, a,b>=0, a+b<=K-1}.
```

For a proposed risk `R`, feasibility is decided recursively by

```text
F_R({i}) iff rho_i<=R,
```

and for `|S|>1`, `F_R(S)` holds iff some proper nonempty split `A,S\A` satisfies one of

```text
F_(Rp_0)(A) and F_(Rp_1)(S\A),
F_(Rp_1)(A) and F_(Rp_0)(S\A).
```

#### Proof

A full binary tree with `K` leaves has no root-to-leaf path longer than `K-1` after suppressing unary vertices. Its maximum leaf risk is attained by one bank, proving the candidate claim. The recursion is exactly the choice of the two root subtrees and their symbol labels. ∎

## 3. Exact branch pruning

### Theorem PP3cde -- PROVED / KRAFT-PRUNED SUBSET DP

At any recursive node containing bank subset `S` under accumulated survival `P`, every completion has risk at least

```text
L(S,P)=(sum_(i in S) rho_i^theta)^(1/theta)/P.
```

Hence a split orientation whose larger child lower bound is at least the best known incumbent may be discarded without changing the optimum.

#### Proof

Apply `PP3cdc` to the subtree and divide by its accumulated parent survival. Any discarded branch cannot improve the incumbent. ∎

The lower bound is especially convenient when `theta` is rational. In the stored audit `p_0=3/5`, `p_1=4/5`, and `theta=2`, so all pruning comparisons are exact rational square comparisons.

## 4. Exact audit

Run

```bash
python scripts/check_pruned_unequal_symbol_code_dp.py
```

The audit finds exact optimum `125/576`, verifies all 30,240 assignments on the 42 ordered six-leaf trees, checks 81 finite candidates, and safely prunes 308 partition orientations.
