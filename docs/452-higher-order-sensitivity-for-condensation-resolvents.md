# Higher-order sensitivity for condensation resolvents

`docs/446` gives exact first finite differences for one bridge or one local SCC
resolvent. Several uncertain blocks may occur on the same condensation path.
Because the condensation graph is acyclic, their complete interaction expansion
is finite.

## 1. Transfer notation

Let `F_u` be the baseline core-to-`u` forward transfer, `G_v` the baseline
`v`-to-core backward transfer, and `T_(v,s)` the baseline transfer from entry at
component `v` through component `s`. Perturb bridge `e=(u,v)` by a nonnegative
block `H_e`.

### Theorem PP3ccq -- PROVED / EXACT MIXED SECOND DIFFERENCE

For two bridge perturbations `e=(u,v)` and `f=(s,t)`,

```text
Delta_e Delta_f K=F_u H_e T_(v,s) H_f G_t
```

when a condensation path can use `e` before `f`. The mixed difference is zero
when the two perturbations are order-incompatible.

#### Proof

A path contributing to the mixed difference must use both perturbed bridges.
Acyclicity fixes their order. Split each such path into its forward prefix, the
first perturbation, the unique baseline middle transfer, the second perturbation,
and its backward suffix. ∎

## 2. Complete finite expansion

### Theorem PP3ccr -- PROVED / MULTILINEAR PATH EXPANSION

For any finite family of bridge perturbations,

```text
K(H)=K(0)+sum_(nonempty compatible chains e_1<...<e_r)
 F_(u_1) H_(e_1) T_(v_1,u_2) ... H_(e_r) G_(v_r).
```

The degree is at most the number of condensation components minus one.

#### Proof

Expand every perturbed bridge as baseline plus increment inside the finite
condensation-path sum. Each path uses every bridge at most once, and grouping
terms by the ordered increment set gives the formula. ∎

## 3. Quadratic remainder envelope

### Theorem PP3ccs -- PROVED / PAIR-PRICE ERROR BOUND

Let `K^+` be the all-upper correction, and compute all-upper transfers
`F^+,G^+,T^+`. Then

```text
0<=K^+-K-sum_e F_u H_e G_v
 <=sum_(e<f compatible) F_u^+ H_e T_(v,s)^+ H_f G_t^+.
```

The same statement covers local SCC-resolvent increments after representing each
local increment as an atomic position in the topological product.

#### Proof

The left side is the sum of expansion terms containing at least two increments.
Choose any ordered pair of increments from such a term. Replacing every other
factor by its all-upper value embeds the term in the corresponding pair-price
summand. Summing over all pairs may overcount but cannot undercount. ∎

## Frontier consequence

Condensation uncertainty now has an exact finite Taylor polynomial rather than
only a first-order envelope. The pair-price bound rigorously decides whether
first-order sensitivity is sufficient or whether a specific interacting block
pair must be sharpened.
