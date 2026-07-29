# Boundary-phase impurity, conflict energy, and bounded witnesses

`docs/385` identifies component-local recleaning with a feasible labelled graph,
`docs/388` gives its exact imbalance formula, and `docs/391` gives the exact cost
of merging graph components.  This chapter separates the large boundary-component
weights from the at most three owner variables.  The resulting boundary impurity
is an exact structural obstruction up to an additive three, and it is controlled
by a pair-conflict energy supported on bounded labelled paths.

The statements are general.  They do not prove that a useful covering rotation
has small boundary impurity.

## 1. Boundary phase masses

Fix a connected component `R` of the feasible boundary graph `Gamma` and a
propagated reference assignment `z_0`.  Let

```text
X_R = boundary-component vertices x_j in R,
Y_R = owner vertices y_t in R.
```

For `a in {0,1}`, define

```text
B_R^a = sum_(x_j in X_R: z_0(x_j)=a) |C_j|,
t_R^a = #{y_t in Y_R: z_0(y_t)=a}.
```

Put

```text
B_R = B_R^0+B_R^1,
q_R = min(B_R^0,B_R^1).
```

The number `q_R` is independent of the choice of propagated root phase, because
complementing the component interchanges the two boundary phase masses.

### Theorem PP3bvy -- PROVED / BOUNDARY-MINORITY COST SANDWICH

Let `c_R` be the exact minimum owner-Hamming recleaning cost contributed by `R`.
Then

```text
q_R <= c_R <= q_R+|Y_R|.
```

Consequently, with

```text
Q = sum_R q_R,
```

the global optimum satisfies

```text
Q <= c_min <= Q+|T| <= Q+3.
```

Moreover the stricter `T`-only recleaning system is feasible if and only if

```text
q_R=0
```

for every graph component `R`.

#### Proof

The two feasible phases on `R` have costs

```text
B_R^0+t_R^0
```

and

```text
B_R^1+t_R^1.
```

Therefore

```text
c_R=min(B_R^0+t_R^0,B_R^1+t_R^1).
```

Each displayed quantity is at least its boundary part, so `c_R>=q_R`.  Choose a
phase attaining the smaller boundary mass.  Its owner contribution is at most
`|Y_R|`, giving the upper bound.  Sum over graph components; the owner sets
partition `T`.

By `PP3but`, `T`-only feasibility is equivalent to all boundary vertices in each
component having one common propagated value.  Since all boundary weights are
positive, that is equivalent to one of `B_R^0,B_R^1` being zero, hence to
`q_R=0`. ∎

Thus the possible contribution of the owner variables is uniformly bounded.  The
asymptotic Hamming obstruction is exactly the minority mass among boundary
components.

## 2. Exact pair-conflict energy

For a component with `B_R>0`, define

```text
E_R = B_R^0 B_R^1.
```

Equivalently,

```text
E_R
 = sum_(x in X_R: z_0(x)=0)
   sum_(x' in X_R: z_0(x')=1)
     |C_x| |C_x'|.
```

Set `E_R/B_R=0` when `B_R=0`.

### Theorem PP3bvz -- PROVED / EXACT IMPURITY-ENERGY FORMULA

For every component with `B_R>0`,

```text
q_R
 = [B_R-sqrt(B_R^2-4E_R)]/2.
```

In particular,

```text
E_R/B_R <= q_R <= 2E_R/B_R.
```

Therefore

```text
sum_R E_R/B_R
 <= Q
 <= 2 sum_R E_R/B_R
```

and

```text
c_min <= 3+2 sum_R E_R/B_R.
```

#### Proof

Write `a=B_R^0` and `b=B_R^1`.  Then `B_R=a+b`, `E_R=ab`, and

```text
|a-b|=sqrt((a+b)^2-4ab).
```

Since `min(a,b)=(a+b-|a-b|)/2`, the exact formula follows.  If
`q=min(a,b)` and `M=max(a,b)`, then

```text
E_R/B_R=qM/(q+M).
```

The factor `M/(q+M)` lies in `[1/2,1]`, proving the two-sided estimate.  Sum and
apply `PP3bvy`. ∎

This converts phase alignment into a second-order statistic.  It is enough to
control the capacity-weighted mass of opposite-phase boundary pairs; no global
orientation enumeration is needed.

## 3. Averaging over candidate rotations

Let `Omega` be any finite or probabilistic family of candidate covering rotations.
For a candidate `omega`, let `Gamma_omega` be its feasible boundary graph and put

```text
Phi(omega)=sum_R E_R(omega)/B_R(omega),
```

with the zero convention above.

### Corollary PP3bwa -- PROVED / CONFLICT-ENERGY AVERAGING CRITERION

Every candidate obeys

```text
c_min(omega) <= 3+2 Phi(omega).
```

Hence

```text
min_(omega in Omega) c_min(omega)
 <= 3+2 E_omega Phi(omega).
```

More generally, if an event `G` of positive probability is imposed, then some
candidate in `G` satisfies

```text
c_min(omega)
 <= 3+2 E[Phi(omega) | G].
```

#### Proof

The pointwise inequality is `PP3bvz`.  Taking expectations and using that a
minimum is at most an average proves the first averaging statement.  Apply the
same argument to the conditional distribution on `G`. ∎

The remaining asymptotic task can therefore be attacked by bounding an expected
opposite-phase pair energy over a pair-safe or clean family of covering rotations.

## 4. Bounded local witnesses for phase conflict

Every edge of `Gamma` is either owner--boundary or owner--owner.  There are at
most three owner vertices in the whole graph.

### Theorem PP3bwb -- PROVED / SIX-EDGE PHASE-CONFLICT WITNESS

If two boundary vertices `x,x'` lie in one graph component and have opposite
propagated phases, then there is a simple path `P` from `x` to `x'` such that

```text
|E(P)| <= 6
```

and the XOR of the edge labels on `P` is one.

More precisely, if the component contains `k` owner vertices, then `P` uses at
most `k` owner vertices, at most `k+1` boundary vertices, and at most `2k` edges.

#### Proof

Take a shortest path between `x` and `x'`.  It is simple.  Every boundary vertex
is adjacent only to owner vertices, while consecutive owner vertices may also be
joined directly by an owner--owner edge.  A simple path uses each of the `k`
owner vertices at most once.  Between consecutive owner vertices it contains at
most one boundary vertex, and it has the two boundary endpoints.  Hence it uses
at most `k+1` boundary vertices and at most `2k` edges.  Since `k<=|T|<=3`, the
length is at most six.

Propagation along any path gives

```text
xor_(e in P) label(e)=z_0(x) xor z_0(x')=1.
```

∎

Thus every term in the conflict energy is supported by a parity-odd labelled
pattern on at most seven graph vertices.  Large recleaning cost cannot hide in an
unbounded logical dependency: it must supply large weighted mass of bounded
local witnesses.

## 5. Revised covering-rotation frontier

For a candidate covering rotation there are now three equivalent or comparable
alignment statistics:

1. exact boundary minority mass `Q`;
2. opposite-phase pair energy `sum_R E_R/B_R`, within a factor two of `Q`;
3. weighted mass of parity-odd paths of length at most six witnessing those pairs.

The exact recleaning cost differs from `Q` by at most three.  A uniform low-cost
recleaning theorem therefore follows from either a direct boundary-minority bound
or a conflict-energy estimate over candidate rotations.  Conversely, failure
forces a large weighted family of bounded parity-conflict witnesses.

The next theorem identifier after this chapter is `PP3bwc`.
