# Petal-reservoir expansion for boundary sunflowers

`docs/405` reduces every large fixed-signature boundary-witness family to a
sunflower: all paths share one boundary core of size at most three and their
remaining boundary petals are pairwise disjoint.  This chapter records the
source-target expansion consequence when repair actions can be marked by those
petals.

The statements are general interfaces.  They do not construct the required
petal-local prime-patching actions.

## 1. Bounded target reuse on a sunflower

Let `F` be a finite sunflower family of witness paths.  Regard the paths as
sources.  For each `P in F`, let `T(P)` be a nonempty finite set of admissible
repair targets.  Put

```text
q=min_(P in F) |T(P)|
```

and define the target multiplicity

```text
m(y)=#{P in F:y in T(P)}.
```

### Theorem PP3bxw -- PROVED / PETAL-RESERVOIR MULTIPLICITY ENVELOPE

If

```text
m(y)<=h
```

for every target, then the uniform-on-reservoir policy

```text
P(P,y)=1/|T(P)|  for y in T(P)
```

has reverse-column load at most

```text
h/q.
```

Consequently the optimal fractional reverse load of the sunflower action graph
satisfies

```text
lambda_*<=h/q,
```

and there is a finite fractional layer bank with load ratio at most `h/q`.

#### Proof

For one target `y`,

```text
sum_(P in F) P(P,y)
 =sum_(P:y in T(P)) 1/|T(P)|
 <=m(y)/q
 <=h/q.
```

Take the maximum over targets.  The optimum cannot exceed the load of this
policy, and finite-bank realizability follows from `PP3bvq`. ∎

Thus a sunflower converts the remaining analytic question into two local
quantities: how many petal actions each path has and how many petals can produce
the same target.

## 2. Intrinsic petal markers

Write the boundary sunflower as

```text
B(P)=C disjoint_union D(P),
```

where `C` is the common boundary core and the petals `D(P)` are pairwise
disjoint.

Call a map

```text
mu: union_(P in F) T(P) -> union_(P in F) D(P)
```

an **intrinsic petal marker** when

```text
mu(y) in D(P)  whenever y in T(P).
```

The word intrinsic means that `mu(y)` depends only on the target `y`, not on a
choice of source that reaches it.

### Theorem PP3bxx -- PROVED / INTRINSIC-MARKER TARGET SEPARATION

If the sunflower reservoirs admit an intrinsic petal marker, then

```text
T(P) intersect T(P')=emptyset
```

for distinct paths `P,P'`.

#### Proof

Suppose `y` belonged to both reservoirs.  Intrinsicness would give one marker
`mu(y)` lying in both `D(P)` and `D(P')`.  Distinct sunflower petals are
disjoint, a contradiction. ∎

A target encoding even one source-independent changed petal vertex therefore
eliminates all cross-petal reverse collisions.

## 3. Exact disjoint-reservoir optimum

### Theorem PP3bxy -- PROVED / EXACT SUNFLOWER PETAL LAYER VALUE

If the target reservoirs are pairwise disjoint, then

```text
lambda_*=1/min_(P in F)|T(P)|.
```

In particular, under the marker condition of `PP3bxx`, if every path has at
least `q` petal-local targets then

```text
lambda_*<=1/q.
```

The optimum is attained by a finite fractional layer bank.

#### Proof

For any nonempty source subfamily `A`, disjointness gives

```text
|N(A)|=sum_(P in A)|T(P)|
      >=|A| min_(P in F)|T(P)|.
```

The exact expansion formula `PP3bvp` therefore gives the upper bound
`1/min_P|T(P)|`.  A singleton source having minimum reservoir size gives the
matching lower bound.  Apply `PP3bvq` for the finite bank. ∎

This identifies a concrete closure route for the boundary branch.  After the
sunflower extraction, it is enough to build multiple clean actions whose final
target intrinsically records one changed petal component.  The common boundary
core may be handled uniformly and does not itself create target overlap.

## 4. Finite diagnostic

Run

```bash
python scripts/check_sunflower_petal_reservoir_expansion.py
```

The script exhausts every nonempty source subset of a stored sunflower action
graph, verifies the multiplicity envelope, checks intrinsic-marker separation,
and compares the exact expansion optimum with the predicted disjoint-reservoir
value.

The next theorem identifier after this chapter is `PP3bxz`.
