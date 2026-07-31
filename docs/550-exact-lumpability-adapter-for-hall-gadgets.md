# Exact lumpability adapter for Hall gadgets

The Hall row in `docs/543--548` assumes a small family of syndrome kernels.  A
geometric gadget, however, acts on a larger local state space containing endpoint,
controller, and source data.  This chapter gives a finite criterion under which
the large transition system projects exactly to the certified Hall kernels.

Let `Omega` be a finite microscopic state space partitioned into syndrome fibres
`F_1,...,F_q`.  A gadget type `s` has a nonnegative integer transition matrix
`M_s` with common row sum `D`.

## 1. Exact syndrome lumpability

### Theorem PP3cny -- PROVED / HALL GADGET LUMPABILITY

Assume that for every gadget `s`, every pair of fibres `(F_i,F_j)`, and every
microscopic state `x in F_i`, the total transition count

```text
sum_(y in F_j) M_s(x,y)=K_s(i,j)
```

is independent of `x`.  Then the syndrome process is exactly Markov with quotient
matrix `K_s/D`.  For every switching word and every initial microscopic state,
aggregating the microscopic transition counts by fibres gives the same vector as
multiplying the corresponding quotient matrices.

#### Proof

For one step, the displayed identity says that aggregation after applying `M_s`
depends only on the aggregate mass in each source fibre.  This is the standard
strong-lumpability identity.  Induction over the switching word proves exact
commutation for every product. ∎

## 2. Uniform law and contraction pass to the quotient

### Theorem PP3cnz -- PROVED / DOUBLY-REGULAR LUMPED HALL KERNEL

Assume in addition that all fibres have the same size and every `M_s` has common
column sum `D`.  Then every quotient `K_s` has row and column sum `D`, so the
uniform syndrome law is stationary.  Every Dobrushin, switch-word, and
reverse-load certificate proved for the quotient kernels therefore applies to
the microscopic gadget family without approximation.

#### Proof

Row sums of `K_s` equal `D` by construction.  Summing the microscopic column
identities over one target fibre and dividing by its common size gives column
sum `D` for the quotient.  `PP3cny` identifies every aggregated microscopic
product with the quotient product, so all quotient estimates transfer exactly. ∎

## 3. Finite geometric adapter

### Theorem PP3coa -- PROVED / LOCAL HALL TRANSITION VERIFIER

For a fixed finite gadget catalogue and syndrome partition, the hypotheses of
`PP3cny--PP3cnz` are decidable by a finite integer audit.  If the quotient family
has a certified horizon `m`, worst syndrome count `H`, and every target has Hall
degree at least `d`, then the actual microscopic reverse load is at most

```text
H/(D^m d).
```

A failed audit returns a specific gadget, source fibre, pair of microscopic
states, and target fibre witnessing non-lumpability.

#### Proof

All required equalities are finite sums of stored transition counts.  Under
success, `PP3cny` gives the exact quotient count `H`, and division by the target
degree gives the reverse-load bound.  Under failure, the unequal finite sums are
the claimed witness. ∎

## 4. Stored exact fixture

The audit `scripts/check_hall_lumpability_adapter.py` refines each of the three
syndromes into two microscopic states.  Every quotient entry is replaced by a
balanced `2 by 2` integer block.  The resulting six-state matrices are doubly
regular and lump exactly to

```text
A=((3,1,0),(0,3,1),(1,0,3)),
B=((3,1,0),(1,0,3),(0,3,1)).
```

The audit checks microscopic-to-quotient commutation for every switching word
through length ten.  It reconstructs the sharp eight-block deviation
`2401/98304`, the worst count `23446` out of `4^8`, and the degree-sixteen
reverse load

```text
11723/524288.
```

## 5. Prime-patching consequence

The Hall realization row no longer requires guessing that a microscopic gadget
behaves like a small kernel.  It is enough to enumerate the actual local states,
choose the geometric syndrome partition, and verify the finite lumpability
identities.  The stored six-state refinement demonstrates the adapter but is not
yet the actual prime-patching gadget census.
