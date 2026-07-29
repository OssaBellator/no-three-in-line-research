# Permutation-layer realization of threshold matrices

`docs/509` rounds a rational threshold matrix while preserving its margins, and
`docs/515` orders its row actions with bounded prefix discrepancy.  When sources
and action channels have equal integral margins, the whole matrix can be executed
in collision-free permutation layers.

Let `A=(a_{ij})` be an `m x m` nonnegative integer matrix whose every row sum and
every column sum equals `M`.

## 1. Exact permutation decomposition

### Theorem PP3ckp -- PROVED / INTEGRAL BIRKHOFF LAYERS

There exist permutation matrices `P_1,...,P_M` such that

```text
A=P_1+...+P_M.
```

Every positive entry used by a layer was positive in the current residual
matrix.

#### Proof

Regard `A` as an `M`-regular bipartite multigraph between sources and action
channels.  Hall's theorem gives a perfect matching.  Delete it; the residual
multigraph is `(M-1)`-regular.  Induction gives all `M` perfect matchings, whose
incidence matrices are the required permutations. ∎

## 2. Collision-free deterministic execution

### Theorem PP3ckq -- PROVED / SLOTWISE CONSERVATIVE SCHEDULE

Execute permutation `P_t` in slot `t`.  Then every source chooses exactly one
action in every slot, every action channel is used exactly once in every slot,
and the period totals reproduce `A` exactly.  Consequently every linear
threshold load has exactly the rational average encoded by `A/M`, with no source
or channel collision.

#### Proof

A permutation matrix has one entry in every row and column.  Summing the layers
recovers each requested source-action multiplicity.  Linearity gives the load
identity. ∎

## 3. Finite certificate and rectangular extension

### Theorem PP3ckr -- PROVED / MATCHING-LAYER AUDIT

A proposed decomposition is certified by checking that every layer is a
permutation and that their entrywise sum is `A`.  Rectangular matrices or unequal
margins reduce to the square regular case by adding dummy sources, dummy action
channels, and zero-cost slack entries; deleting the dummy assignments recovers a
valid schedule for the original system.

#### Proof

The two finite checks are exactly the defining identities.  Standard balancing
adds enough slack incidence to equalize the bipartition and all degrees, after
which `PP3ckp` applies. ∎

## 4. Stored exact fixture

The audit `scripts/check_birkhoff_threshold_layers.py` uses

```text
2 1 1 0
0 2 1 1
1 0 2 1
1 1 0 2.
```

Its lexicographically first four layers are

```text
(0,1,2,3), (0,1,2,3), (1,2,3,0), (2,3,0,1).
```

There are 84 ordered decompositions.  Every stored slot has zero source
collisions and zero action-channel collisions.

## 5. Prime-patching consequence

Conservative threshold mixtures can now be compiled into simultaneous physical
slots, not merely independent per-source words.  Exact global action totals are
realized with no instantaneous channel overbooking.
