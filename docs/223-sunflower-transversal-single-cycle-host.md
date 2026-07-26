# Sunflower-transversal single-cycle hosts

The positive-support reductions PP3ama--PP3amy leave three simple geometries at a
marked endpoint:

1. a fixed or nested helper-resource pencil;
2. a fixed-core source-invalid sunflower;
3. a resource-disjoint bank of positive signatures.

All three admit one common host law.  Select distinct petals and take exactly one
helper index from each selected petal.  Then use a uniform single-cycle state on
the marked centre and the chosen helpers.

The law annihilates every signature in the target sunflower or bank before any
source or paid estimate is made.  At the same time it has an exact product
cylinder law on residual patterns.  Thus the geometry itself is not a terminal
host obstruction: under residual source/paid slack it gives a source-valid paid
state, while failure means that the *remaining* collateral already reaches the
marked credit scale.

## 1. Fixed-core petal systems

Let `c` be a forced marked endpoint index.  Let

```text
F subseteq V\{c}
```

be a fixed optional helper core, and let

```text
P_1,...,P_H subseteq V\({c} union F)
```

be nonempty pairwise disjoint petals.  For each `j`, let `Sigma_j` be a family of
positive source-invalid or insertion signatures whose endpoint-index support
contains

```text
{c} union F union P_j.
```

Only the support inclusion is used; each signature may carry arbitrary positive
weight or witness multiplicity.

Assume one of the following.

1. `F` is nonempty.
2. Every petal has size at least two.

The first alternative covers every nonempty fixed-core or nested-resource pencil.
The second covers the empty-core rank-three/rank-four binary banks and all
empty-core high-support source-signature banks from PP3amu.

## 2. The transversal helper law

Fix an integer `b` with

```text
2 <= b <= H+1.
```

Choose a uniform ordered-free `(b-1)`-subset `J` of `[H]`.  Independently for each
`j in J`, choose one uniform helper index

```text
x_j in P_j.
```

Put

```text
I={c} union {x_j:j in J}.
```

Finally choose a uniform directed single cycle on the `b` indices in `I`.

### Proposition PP3amz -- PROVED

Every target signature in

```text
Sigma_* = union_j Sigma_j
```

is absent from every state in the transversal law.

#### Proof

If `F` is nonempty, the selected block `I` is disjoint from `F`, so no target
signature has all its support selected.  If `F` is empty, the block meets every
petal in at most one index, while every petal has size at least two.  Again no
target signature has all its support selected.  The conclusion is deterministic
and is independent of signature weight and witness multiplicity. ∎

Thus a fixed/nested pencil is killed by omitting its optional core, while a
disjoint signature bank is killed by taking a transversal of its petals.

## 3. Exact helper-cylinder probabilities

Let `X` be a fixed set of `t` helper indices, none equal to `c` or in `F`.

### Proposition PP3ana -- PROVED

If two members of `X` lie in the same petal, then

```text
Pr(X subseteq I)=0.
```

Otherwise suppose the members of `X` lie in distinct petals
`P_(j_1),...,P_(j_t)`.  Then

```text
Pr(X subseteq I)
=
(b-1)_t/(H)_t * product_(ell=1)^t 1/|P_(j_ell)|.
```

In particular,

```text
Pr(X subseteq I) <= ((b-1)/H)^t.
```

#### Proof

The `t` required petals belong to the uniform `(b-1)`-subset with probability
`(b-1)_t/(H)_t`.  Conditional on that event, the required helper is chosen from
petal `P_(j_ell)` with probability `1/|P_(j_ell)|`, independently across the
distinct petals. ∎

This is a genuine spread law with ambient size `H`, even when the original pool
has much larger size `N` or `Q`.

## 4. Joint helper-and-arc cylinders

Let `A` be a compatible prescribed set of `r<=3` directed arcs on the marked
block.  Let `X(A)` be the set of helper indices used by those arcs, excluding the
marked centre `c`, and put `t=|X(A)|`.

### Theorem PP3anb -- PROVED

If two indices of `X(A)` lie in one petal, or if the arcs of `A` contain a proper
directed cycle, then the transversal single-cycle state contains `A` with
probability zero.  Otherwise

```text
Pr(A selected)
=
[(b-1)_t/(H)_t]
[product_(x in X(A)) 1/|P(x)|]
[1/(b-1)_r].
```

Consequently, for fixed `r<=3`,

```text
Pr(A selected)
<=
K^r ((b-1)/H)^t b^(-r)
```

for one absolute constant `K` and all sufficiently large `b`.

#### Proof

First expose the helper block and use PP3ana.  Conditional on containing all
required indices, PP3yy gives the exact single-cycle cylinder probability
`1/(b-1)_r`, unless the prescribed arcs form a proper directed cycle.  Multiply
the two exact factors. ∎

Patterns touching many distinct petals therefore receive an additional power of
`b/H` beyond the ordinary single-cycle arc factor.

## 5. Residual source-valid paid criterion

Let `R_c>0` be the exact removal credit of the marked trade.  Remove the complete
target support `Sigma_*` from the source and insertion objectives.  Let

```text
Z_res
```

be the nonnegative random variable consisting of

1. the number of all remaining source-invalid events; and
2. the remaining insertion cost divided by `R_c`.

### Theorem PP3anc -- PROVED / CONDITIONAL RESIDUAL-LOAD INTERFACE

If

```text
E Z_res < 1,
```

then one transversal single-cycle state is source-valid, contains no target
signature, and has insertion cost below `R_c`.  Hence it gives a strict paid
improvement.

#### Proof

Proposition PP3amz makes every target signature identically absent.  Since
`Z_res` is nonnegative and has expectation below one, some outcome has value
below one.  Its integer source-invalid count is zero and its normalized insertion
cost is below one.  Apply the exact insertion-cost-minus-removal-credit identity
PP3kx. ∎

The theorem permits arbitrary multiplicity on the eliminated sunflower or bank.
Only residual patterns outside that target family are charged.

### Corollary PP3and -- PROVED

Classify residual patterns by:

```text
t = number of distinct petal helper indices required,
r = number of prescribed arcs after the marked centre is fixed.
```

If their total nonnegative source/paid weights are `W_(t,r)`, then a sufficient
condition for PP3anc is

```text
sum_(t,r) K^r W_(t,r) ((b-1)/H)^t b^(-r) < 1.
```

Terms supported entirely on the marked centre or on other deterministic data have
`t=0` and receive no petal gain.  Those are exactly the residual centre-core
terms already isolated in PP3aaf--PP3aaj and PP3amy.

#### Proof

Sum the joint cylinder bound PP3anb over the residual pattern classes, after
normalizing paid weights by `R_c`. ∎

Thus failure of the host theorem is residual centre-core or global
support-ranked mass at the marked credit scale, not the sunflower geometry.

## 6. Availability at the active scales

For the ambient binary geometries of PP3ame and PP3amh, the extracted petal count
satisfies

```text
H=Omega(Q)
```

in rank three or

```text
H=Omega(Q/q^(1/3))
```

in rank four.  Under `q^3/Q=o(1)`, both satisfy `H/q -> infinity`.

For the high-support marked-source geometries PP3amv,

```text
H in {
 Omega(N/b^(1/3)),
 Omega(N),
 Omega(N/b^(1/4)),
 Omega(N/b^(2/5))
}.
```

Every one is `omega(W)` and hence `omega(b)` throughout
`0<kappa<19/80`.

### Proposition PP3ane -- PROVED

Every pencil, sunflower, or disjoint signature bank produced by PP3ame,
PP3amh, or PP3amv contains enough petals to support the transversal law at the
corresponding selected-state size.

#### Proof

The ambient inequalities follow from `q^3/Q=o(1)`.  The marked-source inequalities
are PP3amw together with `b=o(W)`. ∎

## 7. Revised marked-host endpoint

### Corollary PP3anf -- PROVED / CONDITIONAL SOURCE-HOST INTERFACE

The fixed/nested-resource pencils and fixed-core source-invalid sunflowers in
PP3amy are not independent host geometries.  They have the following exact
endpoint.

1. A transversal single-cycle state annihilates the complete target support and
   gives a source-valid strict paid improvement.
2. Residual centre-core source or insertion load already reaches the removal-
   credit scale.
3. Residual petal-touching support-ranked mass reaches the threshold in PP3and.
4. A distinguished-endpoint, Hall, alternating, or controller-pool compatibility
   condition outside the source-support calculation fails explicitly.

The same conclusion applies to the fixed-partner pencils and resource-disjoint
binary links of PP3ami.  Consequently the remaining marked-host problem is no
longer to realize a sunflower or pencil.  It is to control residual credit-scale
collateral and the external endpoint-host constraints.

This does not complete the no-three-in-line conjecture.