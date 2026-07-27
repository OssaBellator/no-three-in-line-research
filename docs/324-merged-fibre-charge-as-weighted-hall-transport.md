# Merged fibre charge as weighted Hall transport

`docs/321` computes the charge of one labelled parity-clean rotation followed by
exact fibre regeneration.  The unresolved issue is label merging: several source
cycles and several rotation labels may send mass to the same clean output.  This
chapter gives an exact optimization formula for that merged charge.

No weighted expansion estimate or asymptotic flaw-walk theorem is claimed.

## 1. Source and target fibre weights

Fix one atomic three-owner flaw `A` with owner set `S`.  Let `X_A` be the set of
parity-satisfiable Hamilton cycles whose prescribed owner assignments admit at
least one clean orientation containing `A`.

For `rho in X_A`, let

```text
c(rho) = number of parity components,
r_A(rho) = number of those components met by the three owners of A.
```

The number of clean signed source states over `rho` that contain `A` is

```text
w_A(rho)=2^(c(rho)-r_A(rho)).
```

For every parity-satisfiable target cycle `eta`, put

```text
v(eta)=2^c(eta),
```

the size of its complete clean orientation fibre.

Join `rho in X_A` to `eta` when `eta` is obtained from `rho` by an
owner-intersecting successor rotation and is parity satisfiable.  Every such edge
deletes `A` by PP3blo.

## 2. Exact merged-column formula

Let `P(rho,eta)` be any row-stochastic cycle kernel supported on the above
bipartite graph.  After choosing `eta`, randomize uniformly over its clean
orientation fibre as in PP3bmd.

### Proposition PP3bmv -- PROVED / EXACT MERGED COLUMN MASS

For every clean signed output state over target cycle `eta`, the total transition
mass from all clean source states containing `A` is

```text
M_A(eta)
 = [1/v(eta)] sum_(rho in X_A) w_A(rho) P(rho,eta).
```

Consequently the action charge is

```text
gamma_A(P)=max_eta M_A(eta).
```

#### Proof

There are exactly `w_A(rho)` clean source orientations over `rho` that contain
`A`.  Each chooses target cycle `eta` with probability `P(rho,eta)` and then
chooses each of the `v(eta)` clean target orientations with probability
`1/v(eta)`.  Summing these equal contributions over source cycles gives the
formula. ∎

For a deterministic labelled edge, this specializes to PP3bmj.

## 3. Weighted Hall characterization of the optimal charge

For `U subseteq X_A`, let `N(U)` be its set of reachable clean target cycles and
write

```text
w_A(U)=sum_(rho in U) w_A(rho),
v(N(U))=sum_(eta in N(U)) v(eta).
```

### Theorem PP3bmw -- PROVED / OPTIMAL TRANSPORT CHARGE

The smallest possible merged charge among all supported row-stochastic kernels
is

```text
gamma_A^*
 = max_(empty != U subseteq X_A) w_A(U)/v(N(U)).
```

#### Proof

A charge bound `gamma` is equivalent, by PP3bmv, to transporting supply
`w_A(rho)` from each source cycle to adjacent target cycles whose capacities are
`gamma v(eta)`.  The total outgoing transport from each source must equal its
supply.

Necessity is immediate: every subset `U` can send mass only into `N(U)`, so

```text
w_A(U)<=gamma v(N(U)).
```

For sufficiency, build the standard source--left--right--sink network.  Give the
source-to-left arc at `rho` capacity `w_A(rho)`, every allowed left-to-right arc
infinite capacity, and the right-to-sink arc at `eta` capacity
`gamma v(eta)`.  The displayed inequalities are exactly the finite-cut
conditions.  Max-flow/min-cut therefore supplies a complete transport.  Divide
the transported mass leaving `rho` by `w_A(rho)` to obtain the required
row-stochastic kernel.  Taking the least feasible `gamma` proves the formula. ∎

This is a weighted Hall theorem, not an approximation: it includes every source
fibre multiplicity and every possible label collision.

## 4. Stationary-scale lower bound and the exact missing expansion

### Corollary PP3bmx -- PROVED / GLOBAL MASS LOWER BOUND

Every supported action satisfies

```text
gamma_A(P)
 >= w_A(X_A)/v(N(X_A)).
```

If every clean target cycle is reachable, the right side is the proportion of
all clean signed states lying over source cycles that contain `A`.

#### Proof

Use `U=X_A` in PP3bmw. ∎

Thus probability-scale charge cannot be smaller than the clean-measure mass of
the flaw.  Conversely, no additional label-merging loss occurs if every subset
expands at the same weighted scale.

### Corollary PP3bmy -- PROVED / SUFFICIENT WEIGHTED EXPANSION CRITERION

Suppose there is a constant `K` such that every `U subseteq X_A` satisfies

```text
v(N(U)) >= (m^3/K) w_A(U).
```

Then there is an owner-intersecting fibre-regenerated deletion action with

```text
gamma_A <= K/m^3.
```

More generally, replacing `m^3/K` by any expansion factor `E_m` gives charge at
most `1/E_m`.

#### Proof

Substitute the weighted expansion inequality into PP3bmw. ∎

This is exactly the stationary three-owner scale needed by the sparse causal
interface in `docs/311` and the logarithmic trajectory window in `docs/317`.

## 5. Relation to charge-aware labels

PP3bml guarantees that every audited source cycle and owner triple has at least
one labelled edge with column mass at most `1/8`.  That is a pointwise edge
statement.  PP3bmw shows why it does not by itself control an unlabelled action:
a subset of source fibres may still have too little weighted target
neighbourhood.

The correct finite and asymptotic diagnostics are therefore:

1. weighted neighbourhood ratios `w_A(U)/v(N(U))`;
2. weighted conductance or spectral expansion of the owner-intersecting clean
   rotation graph;
3. whether the worst cut is global, local, or concentrated on low-component
   fibres;
4. whether several clean rotations or a short clean walk enlarge `N(U)` to the
   required `Theta(m^3)` scale;
5. whether the pair-safe `O(log m)` instances from PP3bmu have uniformly better
   weighted expansion.

## 6. Revised charge frontier

The label-merging problem is no longer qualitative.  It is equivalent to proving
one of the following:

1. the weighted Hall expansion in PP3bmy for one-step owner-intersecting clean
   rotations;
2. the analogous expansion after `Theta(log m)` trajectory-local clean steps;
3. a weaker weighted witness inequality sufficient for termination;
4. a biased clean-cycle measure under which the source weights and target fibre
   weights satisfy the required transport cuts.

The clean orientation coordinate is already exactly regenerated; all remaining
charge loss is encoded by weighted expansion in the Hamilton-cycle coordinate.
