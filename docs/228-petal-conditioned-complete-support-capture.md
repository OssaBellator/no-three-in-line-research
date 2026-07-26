# Petal-conditioned complete-support capture

PP3aod--PP3aoj capture every canonical source and insertion event by helper
support when only the marked centre is fixed.  The paid endpoints of the unary
arc-petal, rank-three path/grid, and rank-four partner/fan chains condition on one
or more additional local arcs.  After that conditioning, an event has one of two
forms:

1. its complete endpoint support lies in the bounded fixed local skeleton;
2. it uses at least one additional helper index.

The second class is captured by a residual helper-support hypergraph and vanishes
on an independent helper block.  The first class is a finite local-core table.  If
the fixed skeleton is one directed path, every compatible additional arc on the
same vertices is either already fixed or creates a forbidden proper cycle, so the
local table is deterministic.

Thus diffuse residual collateral is absent from every explicit petal endpoint.
The remaining paid quantity is a finite local skeleton cost, a second-generation
terminal pencil, or an external completion-host obstruction.

## 1. Fixed local arc forests

Fix a marked centre `c`.  Let

```text
F={a_1,...,a_r}
```

be a compatible directed arc forest on a fixed endpoint-index set `K` containing
`c`, where `r<=4` and `|K|<=5`.  Assume `F` contains no proper directed cycle.

The applications are:

```text
A_2 arc petal:              r=1,
B_3 directed path petal:    r=2 or 4,
B_4 partner/fan petal:      r=2,
transition clean chain:     r=4.
```

Choose an additional helper set `I_0` disjoint from `K`, put

```text
I=K union I_0,
```

and choose a uniform directed single cycle on `I` conditional on containing every
arc of `F`.

### Proposition PP3aok -- PROVED

If `F` has `p` directed path components and `|I|=b`, then the number of
conditional single-cycle states is

```text
(b-r-1)!.
```

Every additional compatible set of `u` arcs has conditional probability

```text
1/(b-r-1)_u,
```

unless it joins `F` to form a proper directed cycle, in which case the probability
is zero.

#### Proof

Contract every path component of `F` to one ordered object.  Since every fixed arc
reduces the number of cyclic objects by one, there are `b-r` objects and hence
`(b-r-1)!` directed cyclic orders.  Contracting `u` additional compatible arcs
reduces the object count by `u`, unless a proper cycle is formed. ∎

This simultaneously contains PP3add, PP3abh, PP3zt, and the fixed two-arc binary
conditioning laws.

## 2. Local-core and helper-supported classes

For every canonical source-invalid or positive insertion signature `G` compatible
with `F`, write

```text
supp_K(G)=supp(G) cap K,
supp_H(G)=supp(G)\K.
```

Call `G` **local-core** when `supp_H(G)=empty`; otherwise call it
**helper-supported**.

Let

```text
H_F
```

be the simple hypergraph of all nonempty helper supports `supp_H(G)` of positive
helper-supported source or insertion signatures.  Count each support once,
independent of witness multiplicity and insertion weight.

### Proposition PP3aol -- PROVED

Every selected canonical event not represented in the local-core table has one
edge of `H_F` contained in the selected helper set `I_0`.

Consequently, if `I_0` is independent in `H_F`, every source or insertion event in
the conditional state is local-core.

#### Proof

A nonlocal event has nonempty helper support by definition.  Selection of the
event requires all of its endpoint indices, so its helper support lies in `I_0`.
Independence excludes this. ∎

All multiplicity attached to an excluded helper support vanishes with it.

## 3. Finite local-core objective

Let `R_F>0` be the exact removal credit supplied by the selected petal or marked
centre.  Under the conditional single-cycle law, let

```text
S_F^loc = number of selected local-core source-invalid events,
J_F^loc = selected local-core insertion cost.
```

Both variables depend only on the cyclic connections among the at most five fixed
vertices and the contracted helper block.

### Theorem PP3aom -- PROVED

Suppose `I_0` is independent in `H_F`.  If

```text
E[S_F^loc + J_F^loc/R_F] < 1,
```

then one conditional single-cycle state is source-valid, has total insertion cost
below `R_F`, and gives a strict paid improvement.

#### Proof

PP3aol removes every helper-supported event.  The displayed nonnegative local
objective therefore equals the complete source-count-plus-normalized-insertion
objective.  An outcome below one has no source violation and insertion cost below
`R_F`.  Apply PP3kx. ∎

The theorem uses no global source or insertion first moment after the independent
helper block is selected.

## 4. Spanning-path simplification

Say that `F` is a **spanning local path** when its arcs form one directed path
using every vertex of `K`.

### Proposition PP3aon -- PROVED

For a spanning local path, every compatible directed arc whose two endpoints both
belong to `K` is either:

1. one of the fixed path arcs; or
2. incompatible with the path because it repeats a tail or head; or
3. the endpoint-to-start arc closing a proper directed cycle.

Hence every selected local-core canonical event is supported entirely on the
fixed path arcs.  Its source status and insertion weight are deterministic before
the remaining cycle is completed.

#### Proof

Every internal path vertex already has one fixed incoming and one fixed outgoing
arc.  The first vertex has only its incoming slot free and the last has only its
outgoing slot free.  The only compatible new arc on the path vertex set is from
the last vertex to the first, which closes the proper cycle. ∎

Write the resulting deterministic local insertion cost as `J_F^det`.  A
source-clean spanning path therefore pays whenever

```text
J_F^det<R_F.
```

No residual collateral remains.

## 5. Independent completion or second-generation pencil

Let the unused helper reservoir have size `N_F`, and let the desired number of
additional helpers be `b-|K|`.  The maximum helper-support rank in `H_F` is at
most five.

### Theorem PP3aoo -- PROVED

Exactly one of the following occurs.

1. `H_F` has an independent helper set of size `b-|K|`, and PP3aom reduces the
   complete paid problem to the finite local-core objective.
2. There is a fixed residual helper core of size at most four with at least

   ```text
   (N_F-b) /
   [sum_(j=0)^4 binom(b-1,j)]
   ```

   distinct variable extensions.

For adaptive `b=N_F^(o(1))`, the extension family has size `N_F^(1-o(1))`.

#### Proof

Apply PP3ano to `H_F`, replacing the required helper count by `b-|K|` and
weakening the denominator using `|K|=O(1)`. ∎

Thus a failed independent completion is another explicit terminal pencil, now
conditioned on the original petal skeleton.

## 6. Bank-level endpoint

Let `B` be a bank of pairwise noncentral-resource-disjoint local petals.  For each
`e in B`, let `F_e`, `R_e`, and `H_e` denote its fixed skeleton, credit, and
residual helper hypergraph.  Assume `R_e>=R_*>0`.

### Corollary PP3aop -- PROVED

At least one of the following holds.

1. Some petal has an independent helper completion and local-core objective below
   one, giving a strict paid improvement.
2. Every independently completable petal has local-core insertion/source cost at
   its own removal-credit scale.
3. A subfamily of petals carries second-generation fixed-core pencils with
   `N_e^(1-o(1))` extensions.
4. The conditional single-cycle, controller-pool, distinguished-endpoint, Hall,
   alternating, or source-clean skeleton host fails explicitly.

Diffuse helper-supported collateral cannot obstruct the entire petal bank.

#### Proof

Apply PP3aom--PP3aoo petal by petal.  The four alternatives are exhaustive. ∎

## 7. Application to the three insertion ranks

### Corollary PP3aoq -- PROVED / CONDITIONAL EXISTING PETAL INTERFACES

The live `A_2`, `B_3`, and `B_4` paid endpoints reduce further as follows.

1. A fixed-axis unary arc petal has one fixed arc; its residual helper-supported
   source and insertion costs vanish on an independent completion.
2. A rank-three path petal conditioned on its two-arc or five-index path has only
   its deterministic local path cost plus the finite local-core table.
3. A rank-four partner/fan petal conditioned on its two disjoint arcs has a finite
   four-vertex local-core table; every other cost is helper-supported and can be
   annihilated.

Failure produces local cost at the petal-credit scale, a second-generation
near-linear pencil, or an explicit external host obstruction.  No diffuse
noncentral source or insertion term remains at these endpoints.

The no-three-in-line conjecture remains unproved.
