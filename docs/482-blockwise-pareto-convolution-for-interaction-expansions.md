# Blockwise Pareto convolution for interaction expansions

`docs/476` computes the complete multioutput frontier for one interaction forest.
Condensation systems often split into independent SCC blocks or independent root
families.  This chapter composes their exact frontiers without enumerating every
global expansion plan.

Block `i` has finite plans `P_i`.  A plan has integer work `w_i(P)` and exact
nonnegative omitted-output vector `E_i(P) in Q_+^r`.

## 1. Exact budget convolution

### Theorem PP3cgc -- PROVED / MINKOWSKI PARETO COMPOSITION

Let `F^(i)_b` be the nondominated error vectors attainable in block `i` with work
at most `b`.  The global budget-`B` frontier is

```text
F_B=minimal elements of
    union_(b_1+...+b_m<=B)
      [F^(1)_(b_1)+...+F^(m)_(b_m)],
```

where `+` is vector addition.  Iterated budget convolution computes the exact
global frontier.

#### Proof

Every global plan decomposes uniquely into one plan per independent block, and
its work and omitted outputs add.  Conversely, every choice of block plans gives
a global plan.  Taking the coordinatewise minimal vectors after every budget
split therefore gives exactly the global nondominated set. ∎

## 2. Safe local dominance pruning

### Theorem PP3cgd -- PROVED / DOMINANCE COMMUTES WITH CONVOLUTION

If `u<=v` coordinatewise within one block at no greater work, then for every
nonnegative error vector `h` from the remaining blocks,

```text
u+h<=v+h.
```

Thus dominated block vectors and dominated intermediate convolution vectors may
be deleted permanently.  Storing one parent pointer for every retained vector
reconstructs an exact global expansion plan.

#### Proof

Coordinatewise order is translation invariant under addition of a nonnegative
vector.  Therefore no dominated partial vector can become nondominated after
composition.  Parent pointers follow the budget split and retained summands
back to concrete block plans. ∎

## 3. Compositional tolerance certificates

### Theorem PP3cge -- PROVED / BLOCKWISE MINIMUM-WORK CERTIFICATE

For tolerance vector `tau`, the minimum global work is the least `B` for which
some vector in the convolved frontier `F_B` satisfies `e<=tau`.  The preceding
frontier is an exact impossibility certificate.  A complete finite verifier needs
only the certified local block frontiers, the convolution tables, dominance
checks, and the parent path of the selected feasible vector.

#### Proof

`PP3cgc` enumerates every attainable global error up to dominance.  Hence a
feasible plan exists exactly when a frontier vector lies in the tolerance box.
Minimality follows from the first such budget, and `PP3cgd` makes the stored
parent reconstruction exact. ∎

## 4. Stored exact fixture

The audit `scripts/check_blockwise_interaction_pareto_convolution.py` has three
independent blocks and 18 raw global plans.  Exact convolution gives frontier
sizes

```text
budget 0,1,2,3,4,5: 1,3,3,3,2,1.
```

Tolerance `(1,1)` is impossible at budget two, whose complete obstruction
frontier is

```text
(1,9/5), (7/5,7/5), (9/5,1).
```

At budget three, the unique feasible vector is exactly `(1,1)`, reconstructed
from the middle one-work plan in each block.

## 5. Prime-patching consequence

Interaction truncation can now be certified SCC block by SCC block.  Small local
Pareto tables compose into a global minimum-work proof, and every retained global
tradeoff carries an explicit blockwise expansion schedule.
