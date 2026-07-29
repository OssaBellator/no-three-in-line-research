# Pareto transfer matrices for repeated interaction motifs

`docs/494` handles a general bounded-width interaction join tree.  Repeated local
motifs have additional algebraic structure.  This chapter packages one motif as
a finite Pareto transfer matrix and uses exact semiring powers to treat long
chains without expanding every global plan.

For separator states `s,t`, let a matrix entry be a finite antichain of tuples

```text
(work, omitted-output vector, backpointer)
```

for one motif taking `s` to `t`.

## 1. Pareto transfer semiring

### Theorem PP3cie -- PROVED / ANTICHAIN MATRIX PRODUCT

Define addition as union followed by coordinatewise dominance pruning.  Define
multiplication as pairwise addition of work and output vectors, concatenation of
backpointers, and dominance pruning.  These operations form an idempotent
semiring on finite Pareto antichains.  Matrix multiplication over this semiring
computes the exact frontier for concatenated motifs.

#### Proof

Union represents alternative plans.  Minkowski addition represents independent
concatenation.  Coordinatewise dominance is preserved after adding any
nonnegative continuation, so quotienting by dominated elements is safe.
Associativity and distributivity descend from ordinary set union and vector
addition; pruning selects the same minimal elements independent of grouping. ∎

## 2. Exact repeated squaring

### Theorem PP3cif -- PROVED / PARETO MATRIX POWER

For a repeated motif of length `L`, the exact start--end frontier is the
corresponding entry of the `L`th Pareto-semiring matrix power.  Binary
exponentiation computes it using `O(log L)` matrix multiplications, with exact
pruning after every product.

#### Proof

Induction on `L` identifies matrix multiplication with concatenating adjacent
motif blocks.  Binary exponentiation is only a reassociation of this associative
product, so it preserves the exact frontier. ∎

## 3. Reconstruction and minimum work

### Theorem PP3cig -- PROVED / POWERED FRONTIER CERTIFICATE

Given a tolerance vector, the minimum feasible work is the least work coordinate
among powered-frontier entries below that tolerance.  Stored multiplication
backpointers reconstruct a complete motif plan.  The remaining frontier vectors
with smaller work form a matching impossibility certificate.

#### Proof

Every repeated-chain plan appears in the powered entry and is dominated by one
of its antichain elements.  Thus feasibility and minimum work are read directly
from the exact frontier.  Backpointer recursion reverses the matrix products. ∎

## 4. Stored exact fixture

The audit `scripts/check_pareto_transfer_matrix_power.py` has two separator
states and four transitions `A,B,C,D`.  A length-eight chain has 128 direct plans
from state zero back to state zero, but only 17 nondominated work--error vectors.
Three squaring stages reproduce exactly the direct frontier.  Under tolerance
`(4,4)`, the unique feasible plan is

```text
BDBDBDBD
```

with minimum work eight.

## 5. Prime-patching consequence

Repeated interaction gadgets can now be certified by powering one small exact
transfer matrix.  Long periodic or translationally repeated prime-patching
interfaces need not be unfolded into exponentially many global expansion plans.
