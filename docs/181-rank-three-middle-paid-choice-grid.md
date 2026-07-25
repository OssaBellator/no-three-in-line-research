# Rank-three middle paths as a paid two-resource choice grid

PP3abn--PP3abu reduce fixed-centre rank-three binary `Xi` weight to a
conditioned cheap chain, a weighted middle rectangle, or a small-core heavy
outer-role family. The middle rectangle is already an exact object from the
paid binary-grid machinery.

For each predecessor `p` and successor `s`, the middle path

```text
p -> c -> s
```

is the two-cell local state

```text
{p->c, c->s}.
```

The first cell lies on the fixed endpoint column `c`; the second lies on the
fixed endpoint row `c`. Thus the predecessor and successor choices form an
opposite-side two-resource choice grid. Jointly averaging the local pair and its
residual matching is precisely PP3ze.

This chapter makes that identification exact and removes a weighted middle
rectangle as an independent rank-three frontier. It does not convert the
small-core heavy predecessor/successor families left by PP3abt.

## 1. Exact local-grid representation

Retain the fixed centre `c` and the high-choice sets

```text
P=P_3(lambda),
S=S_3(lambda)
```

from PP3abr. Define the two choice lines

```text
A={a_p=p->c : p in P},
B={b_s=c->s : s in S}.
```

Let

```text
T={(p,s) in P x S :
   p!=s and p->c->s is source-valid}.
```

### Proposition PP3aco -- PROVED

The map

```text
(p,s) -> (a_p,b_s)
```

is a bijection from `T` to a family of compatible local pairs between the two
fixed resource lines `A` and `B`. For each state, its exact local rank-three
middle cost is

```text
mu(p,s)=beta_M(p,s).
```

After fixing `(a_p,b_s)`, exactly two left and two right endpoint resources have
been used, so the residual endpoint host is the same local-pair residual host
appearing in PP3ze.

#### Proof

The tails of the two cells are `p,c` and their heads are `c,s`. They are
compatible exactly when `p!=s`. Source validity is the definition of membership
in `T`. The rank-three pattern supported on the two cells is the middle path
`p->c->s`, whose weight is `beta_M(p,s)`. The used typed resources are the
variable predecessor row, fixed centre column, fixed centre row, and variable
successor column, exactly the opposite-side two-resource geometry of
PP3zh. ∎

For every fixed controller candidate cell `z`, the states of `T` whose local
pair creates `z` form a matching between `P` and `S`, by the same secant-line
argument as PP3zh.

## 2. Small product or an almost-complete valid grid

Put

```text
D_c=|M_c|+N,
```

where `M_c` is the source-invalid middle relation and the `N` term covers
diagonal pairs.

Let `omega=omega(m)` be any slowly growing function with

```text
omega -> infinity,
omega=m^(o(1)).
```

### Proposition PP3acp -- PROVED

At least one of the following holds.

1. **Small outer core:**

   ```text
   min(|P|,|S|) <= sqrt(omega D_c).
   ```

2. **Almost-complete valid grid:**

   ```text
   |P||S| > omega D_c
   ```

   and

   ```text
   |T| >= |P||S|-D_c
       = (1-o(1))|P||S|.
   ```

If no source-clean five-index chain has deterministic rank-three cost below
`lambda`, every state in alternative 2 satisfies

```text
mu(p,s)>=lambda/3.
```

#### Proof

If the product is at most `omega D_c`, its smaller factor is at most the square
root. Otherwise at most `|M_c|` pairs are source-invalid and at most `N` are
diagonal, so the displayed lower bound holds. Since `D_c/(|P||S|)<1/omega`,
the valid fraction tends to one. The weight bound is PP3abr. ∎

At the slab-optimal scale `D_c=m^(1+o(1))`, alternative 1 has size
`m^(1/2+o(1))`.

## 3. Joint paid selection on the middle grid

For each `t=(p,s) in T`, let `G_t` be the residual endpoint host after fixing
`p->c` and `c->s`. Classify every remaining source-invalid canonical pattern by
the number `u` of additional residual matching arcs required, and write its
count or nonnegative weight as

```text
S_t,u,  0<=u<=3.
```

Let `C_t` be the remaining non-middle insertion cost, and let `R(t)>=R_*>0` be
the exact removal credit of the local move.

### Theorem PP3acq -- PROVED FROM PP3ze

Assume every `G_t`, `t in T`, is superregular with one common fixed-rank spread
constant `K`. If

```text
(1/|T|) sum_{t in T} [
  sum_{u=0}^3 K^u S_t,u/(q-2)^u
  + (beta_M(t)+E[C_t])/R_*
] < 1,
```

then one middle state and one residual perfect matching give a source-valid
strict decrease of `Xi`.

#### Proof

Apply PP3ze to the local pair family in PP3aco, with local multiplicity
`mu(t)=beta_M(t)`. The proof of PP3ze only uses uniform choice from the supplied
compatible state family and therefore applies to `T`. ∎

The middle pair and residual completion are selected simultaneously; no
state-by-state completion hypothesis beyond the common superregular spread law
is introduced.

## 4. Weighted failure and projective candidate cover

Put

```text
W_M(T)=sum_{t in T} beta_M(t).
```

### Corollary PP3acr -- PROVED FROM PP3zf--PP3zi

Suppose the averaged source and non-middle residual terms in PP3acq are `o(1)`.
Then either a strict paid completion exists or

```text
W_M(T) >= (1-o(1))R_* |T|.
```

If `beta_M(t)` counts distinct controller-candidate incidences, then every one
candidate colours a matching between `P` and `S`, and paid failure requires at
least

```text
W_M(T)/min(|P|,|S|)
```

distinct candidates.

In the almost-complete branch of PP3acp this is

```text
Omega(R_* max(|P|,|S|)).
```

#### Proof

The weighted lower bound is PP3zg. The matching-colour statement is PP3zh in
the opposite-side row/column geometry identified by PP3aco. Summing candidate
matching sizes gives the first candidate bound, and
`|T|=(1-o(1))|P||S|` gives the final display. ∎

Thus a bare heavy middle rectangle is not terminal. The hard cases are
credit-scale weighted multiplicity, a candidate-rich projective cover, residual
source/paid concentration, or residual-host failure.

## 5. Revised rank-three endpoint

### Corollary PP3acs -- PROVED

At a source-light captive centre, rank-three binary `Xi` weight reduces to one
of:

1. a conditioned cheap five-index chain and its residual completion criterion;
2. a small predecessor or successor choice core of size `m^(1/2+o(1))`,
   together with the near-complete heavy outer-role family of PP3abt;
3. a paid average completion on the middle two-resource grid;
4. a credit-scale weighted middle grid;
5. a candidate-rich projective matching cover;
6. residual source, paid, conditional-Hall, or alternating-host structure.

Therefore a weighted middle rectangle is no longer an independent marked-`Xi`
frontier. The remaining genuinely rank-three-specific object is the
small-core/near-complete heavy predecessor or successor family.

## 6. Finite diagnostic

The script

```text
scripts/check_rank_three_middle_choice_grid.py
```

checks a finite middle-pair instance. It verifies the small-product versus
almost-complete-valid-grid dichotomy, computes the exact average local weight,
tests the paid inequality with supplied residual averages and removal credit,
and, when candidate incidences are supplied, verifies that each candidate
colours a matching and checks the projective-cover lower bound. The stored
example realizes the weighted-grid/projective-cover branch.
