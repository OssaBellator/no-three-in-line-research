# Ambient binary positive support: avoidance and link decomposition

PP3age--PP3agg leave positive-density ambient rank-three or rank-four binary
support stars through one fixed endpoint resource.  Their degrees were counted
with event multiplicity.  A large multiplicity on one pair of inserted arcs is
not intrinsically difficult: a selected state that avoids that positive support
signature pays zero cost from the entire multiplicity.

This chapter first replaces weighted/event multiplicity by distinct positive
support signatures using an exact conditioned single-cycle calculation.  A dense
rank-three signature star is then a dense graph link; a dense rank-four signature
star is a dense 3-uniform link.  Standard star--matching decompositions give
fixed-partner pencils or resource-disjoint support banks.

The support-avoidance statement is conditional on residual source/paid slack.  The
link decompositions themselves are unconditional combinatorial theorems.

## 1. Distinct binary support signatures

Let the ambient tied endpoint bank have index set `[Q]`, fix one typed endpoint
resource `v`, and condition on retaining its underlying endpoint index.  A
**positive binary signature** is a compatible pair of directed inserted arcs,
with positive foreign binary insertion weight, recorded only once regardless of
that weight or the number of candidate incidences it blocks.

Let

```text
S_3(v)
```

be the number of distinct positive signatures of endpoint-index rank three
incident with `v`, and let `S_4(v)` be the analogous rank-four count.

Choose the other `q-1` indices uniformly and then choose a uniform single-cycle
state on the selected `q` indices, where `q>=4`.

### Proposition PP3ama -- PROVED

A fixed compatible rank-three signature incident with `v` is selected with
probability

```text
p_3=1/((Q-1)(Q-2)).
```

A fixed compatible rank-four signature incident with `v` is selected with
probability

```text
p_4=(q-3)/((Q-1)(Q-2)(Q-3)).
```

If the two prescribed arcs contain a proper directed cycle, their selection
probability is zero.

#### Proof

A rank-`h` signature needs its other `h-1` endpoint indices in the conditioned
subbank, with probability

```text
(q-1)_(h-1)/(Q-1)_(h-1).
```

Conditional on those indices, the two compatible arcs occur in a uniform
single-cycle state with probability

```text
1/((q-1)(q-2))
```

by PP3yy, unless they form a proper directed cycle, in which case the probability
is zero.  Cancel the factors for `h=3,4`. ∎

The cancellation at rank three is exact and independent of `q`.

## 2. Positive-support avoidance

Let `R_c>0` be the removal credit of the selected marked endpoint.  Normalize all
source-invalid counts and all paid insertion classes other than the complete
rank-three/rank-four positive support through `v` into a nonnegative random
objective `Z_other`.

### Theorem PP3amb -- PROVED / CONDITIONAL RESIDUAL-SLACK INTERFACE

Suppose

```text
E Z_other <= 1-tau
```

for one fixed `tau in (0,1)`.  If

```text
p_3 S_3(v)+p_4 S_4(v)<tau,
```

then some conditioned single-cycle state is source-valid, selects no positive
rank-three or rank-four signature through `v`, and has remaining insertion cost
below `R_c`.  It therefore gives a strict paid improvement.

#### Proof

Let `X_3,X_4` count selected distinct positive signatures.  Proposition PP3ama
gives

```text
E(X_3+X_4)=p_3S_3(v)+p_4S_4(v).
```

The expectation of `Z_other+X_3+X_4` is below one.  Some outcome has value below
one.  The signature counts and source-invalid counts are nonnegative integers, so
they vanish there; the remaining normalized paid cost is below one.  Avoiding a
positive signature removes its complete weight and multiplicity. ∎

### Corollary PP3amc -- PROVED

Under residual slack `tau`, failure of positive-support avoidance forces at least
one of

```text
S_3(v)>=tau (Q-1)(Q-2)/2,
```

or

```text
S_4(v)>=tau (Q-1)(Q-2)(Q-3)/(2(q-3)).
```

Thus multiplicity is eliminated before structural extraction.

## 3. Rank-three graph link

After pigeonholing the finitely many typed roles of `v` and the two directed arcs,
a rank-three signature is represented by an edge on the other `Q-1` endpoint
indices.  Let this simple graph have `E_3` edges.

### Proposition PP3amd -- PROVED

For every integer `D>=1`, the rank-three link contains either

1. one partner index incident with at least `D` signatures; or
2. a matching of at least `E_3/(2D)` signatures.

#### Proof

If the maximum degree is at least `D`, use its star.  Otherwise a maximal matching
of size `s` has `2s` endpoints covering all edges, each of degree below `D`, so
`E_3<2sD`. ∎

### Corollary PP3ame -- PROVED

If `E_3=Omega(Q^2)`, then the link contains either

1. a fixed second-resource pencil with `Omega(Q)` distinct final partners; or
2. an `Omega(Q)` matching of pairwise resource-disjoint rank-three signatures.

#### Proof

Take `D` to be a sufficiently small fixed multiple of `Q` in PP3amd. ∎

The pencil is the fixed-second-resource/two-resource choice-grid interface.  The
matching is a resource-disjoint binary-event bank.

## 4. Rank-four 3-uniform link

After role pigeonholing, a rank-four signature is represented by a triple of the
other endpoint indices.  Let the resulting simple 3-uniform hypergraph have `E_4`
edges.

### Proposition PP3amf -- PROVED

For every real `D>=1`, the rank-four link contains either

1. a partner index whose graph link has at least `D` edges; or
2. a vertex-disjoint matching of at least `E_4/(3D)` triples.

#### Proof

If some vertex degree is at least `D`, use its graph link.  Otherwise greedily
select a triple and delete every triple meeting one of its three vertices.  Each
selection removes fewer than `3D` triples. ∎

In the first alternative, apply PP3amd to the graph link.

### Corollary PP3amg -- PROVED

Every rank-four link with `E_4` distinct signatures contains at least one of:

1. a fixed two-partner pencil of size `Omega(E_4^(1/3))`;
2. a fixed first-partner family containing `Omega(E_4^(1/3))` pairwise
   resource-disjoint partner pairs;
3. an `Omega(E_4^(1/3))` matching of vertex-disjoint partner triples.

#### Proof

Take `D=ceil(E_4^(2/3))` in PP3amf.  In the hypergraph-matching branch the size is
`Omega(E_4^(1/3))`.  In the high-degree branch the graph link has at least
`E_4^(2/3)` edges; apply PP3amd with threshold `ceil(E_4^(1/3))`. ∎

### Corollary PP3amh -- PROVED

Under the rank-four lower bound of PP3amc,

```text
E_4=Omega(Q^3/q)
```

after finite role pigeonholing.  Therefore one of the three rank-four structures
in PP3amg has size

```text
Omega(Q/q^(1/3)).
```

This tends to infinity whenever `q=o(Q^3)` and is much larger than the selected
subbank scale for every sufficiently slow adaptive choice of `q` used in PP3agb.

## 5. Conversion interfaces

### Theorem PP3ami -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

A non-paid ambient rank-three or rank-four binary support star through `v` has one
of the following outcomes.

1. A conditioned single-cycle state avoids its complete positive support and gives
   a strict paid improvement.
2. A fixed second-resource or fixed two-partner pencil feeds the conditional
   binary-star, fixed-cell fan, choice-grid, or Hall interfaces.
3. A resource-disjoint pair/triple bank feeds recapture-free endpoint thinning,
   ambient support cleaning, or final-state direct allocation.
4. Residual source/paid load already consumes the marked credit.
5. Source, transition, anchor, Hall, alternating, distinguished-endpoint, or
   endpoint-host preparation fails explicitly.

#### Proof

Apply PP3amb.  On failure use PP3amc, pigeonhole finitely many typed roles, and
apply PP3ame or PP3amh.  The listed structures are precisely the interfaces of
PP3afu--PP3agg, PP3ago--PP3agt, and the conditional binary-resource theorems. ∎

### Corollary PP3amj -- PROVED

Raw event multiplicity and an unstructured positive-density ambient binary star
are no longer separate paid frontiers.  The remaining binary objects are simple
fixed-partner pencils, resource-disjoint link matchings, residual marked
collateral, or explicit host failure.

The no-three-in-line conjecture remains unproved.
