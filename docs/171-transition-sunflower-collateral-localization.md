# Transition sunflower collateral localization

PP3zw--PP3aae already convert a failed fixed-centre transition branch into a free
or one-pool credited endpoint bank of the marked target size

```text
W=m^(19/40+o(1)).
```

The selected petals share only the captive centre. Their predecessor, middle,
witness-anchor, old-row, and old-column resources are pairwise disjoint outside
that centre.

This disjointness controls insertion collateral more strongly than a raw credited
bank. Every source-invalid or dynamic-`Xi` pattern has bounded endpoint/resource
support, so it can touch the noncentral resources of only boundedly many petals.
Averaging over the credited endpoints removes every diffuse noncentral
contribution. Failure localizes to the fixed captive centre or to a global
support-ranked weight threshold.

## 1. Abstract disjoint-petal incidence bound

Let `B` be one free or one-pool sunflower subbank from PP3aac. For each petal
`i in B`, let `A_i` be its complete noncentral typed resource set:

```text
A_i={
 predecessor endpoint row and column,
 middle endpoint row and column,
 witness-anchor row and column
}.
```

The sets `A_i` are pairwise disjoint by PP3zy. Let `C` denote the shared captive
centre resources.

Let `F` be any family of source or paid patterns. Give each pattern `F in F` a
nonnegative weight `w(F)` and a typed resource support `supp(F)` of size at most
`r_0`.

### Proposition PP3aaf -- PROVED

One has

```text
sum_{i in B}
sum_{F: supp(F) cap A_i != empty} w(F)
<= r_0 sum_{F in F} w(F).
```

#### Proof

Fix one pattern `F`. Since the petal resource sets `A_i` are pairwise disjoint,
every petal met by `supp(F)` consumes a distinct support resource of `F`. Hence
`F` meets at most `r_0` petals. Sum first over petals and then over patterns. ∎

This applies to integer source-event counts and to exact nonnegative insertion
weights.

## 2. Core-only and petal-touching decomposition

For a marked endpoint `z_i` from petal `i`, choose a filler block and endpoint
state as in PP3xp--PP3zd. Classify every remaining source or paid pattern by:

1. the number `r` of additional random endpoint arcs it requires;
2. whether its fixed support meets `A_i`.

Write

```text
X_i,r = petal-touching total weight,
Y_i,r = centre-core total weight.
```

The centre-core class contains patterns whose fixed support avoids `A_i`; in the
transition application the only petal-common distinguished resource is the
captive centre `C`.

### Theorem PP3aag -- PROVED

For every additional-arc rank `r`,

```text
(1/|B|) sum_i X_i,r
<= r_0 W_r/|B|,
```

where `W_r` is the total global weight of the corresponding rank-`r` pattern
class.

After multiplying by the fixed-rank cylinder factor, the averaged first moment is
bounded by

```text
sum_r K^r [
  (1/|B|) sum_i Y_i,r
  + r_0 W_r/|B|
]/b^r.
```

#### Proof

Apply PP3aaf separately to each rank class. Conditional on one marked endpoint and
its filler block, the single-cycle cylinder law PP3yy contributes at most an
absolute constant times `b^-r`. ∎

Thus the bank-size gain is lost only on centre-core terms common to the petals.

## 3. One-pool source-valid endpoint

Assume the one-pool alternative of PP3aae. The bank lies inside one controller
pool and has size at least `W`. Use the marked filler size

```text
b=m^(kappa+o(1)),
0<kappa<19/80.
```

### Corollary PP3aah -- PROVED

Assume the averaged centre-core source term is `o(1)` and every global
petal-touching source class satisfies

```text
W_r/(W b^r)=o(1)
```

with its appropriate support-ranked selection factor. Then at least one of the
following holds.

1. All but `o(W)` sunflower endpoints are light for every nonunary source class,
   and some unary-light endpoint admits a source-valid single-cycle marked filler
   state.
2. The bank contains no unary-light endpoint, in which case PP3yf--PP3yi extract
   an `Omega(W)` unary-forbidden resource matching.

#### Proof

PP3aag makes the averaged petal-touching contribution `o(1)`. Add the centre-core
term and apply Markov's inequality over the `W` marked endpoints. This leaves all
but `o(W)` endpoints light for the nonunary source classes.

If one of them satisfies the unary hypotheses of PP3za, that theorem gives a
source-valid single-cycle state. Otherwise unary failure holds throughout a
linear subbank, and PP3yf--PP3yi give the resource-matching alternative. ∎

The former pool-local source-mass problem is therefore even more localized on a
transition sunflower: noncentral petal resources cannot support many exceptional
endpoints, while hard-unary failure remains an explicit resource bank.

## 4. Dynamic-Xi paid endpoint

Let `R_i>=R_*>0` be the distinguished certificate-removal credit of petal `i`.
Split exact unary/binary `Xi` insertion weights into centre-core and
petal-touching classes after their cylinder factors are included.

### Theorem PP3aai -- PROVED

Under the source-valid endpoint alternative of PP3aah, a strict dynamic decrease
exists whenever

```text
(1/|B|) sum_i J_i^core
+ O(W_var/|B|)
< R_*,
```

where `J_i^core` is the expected centre-core insertion cost and `W_var` is the
global support-ranked petal-touching weight.

#### Proof

Use PP3aag for the petal-touching weights, add the centre-core expectation, and
apply the exact insertion-cost-minus-removal-credit identity PP3kx to a
source-valid marked endpoint whose total paid first moment lies below its credit.
∎

Negating the criterion gives one of:

1. centre-core insertion weight at the captive-centre credit scale;
2. global petal-touching weight of order `W R_*` after support normalization;
3. hard-unary or residual-host failure in the marked endpoint construction.

## 5. Free sunflower endpoints

In the free-bank alternative of PP3aae, the same incidence bound PP3aaf applies.
The endpoint distribution is the distinguished free-endpoint trade law rather
than a pool-compatible marked filler. Any fixed-rank spread law on that free bank
therefore has the identical conclusion: diffuse noncentral collateral gains a
factor `1/W`, and only the shared captive-centre core remains undiluted.

### Corollary PP3aaj -- PROVED AS AN INTERFACE

A free transition sunflower bank completes under its existing endpoint spread
hypotheses whenever its centre-core source and paid terms fit below the petal
credit and its global petal-touching weights are `o(W)` after normalization.

Failure is a fixed-centre core, a global weight threshold, or failure of the free
endpoint host/spread hypothesis.

## 6. Revised transition endpoint

The transition sunflower is now reduced beyond raw paid star/resource conversion.
Its exact remaining cases are:

1. a source or `Xi` core supported at the shared captive centre;
2. global support-ranked source or insertion weight of order the bank credit;
3. a unary-forbidden resource matching;
4. hard-unary or residual endpoint-host failure;
5. paid completion through a free or one-pool credited endpoint.

Diffuse collateral on the disjoint petals is closed by bounded-support averaging.
