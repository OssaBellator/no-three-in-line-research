# Fixed-label blocker fibres convert margin collapse

The direct controller-aware allocation theorem can fail because one movement
label `A` in one macro has a large unsafe-controller count

```text
a_i(A)=R-|C_(i,A)^ctrl|,
```

or, by transposition, one refill label has large `b_i(B)`.  Global bad-entry
density may still be `o(1)` when only a few numerical labels are affected.  This
chapter shows that such a labelwise margin collapse is already a target-scale
source structure.

For one fixed movement label, a chosen noncontroller blocker pair determines at
most one bad controller entry.  Therefore a fibre with `Omega(R)` unsafe
controllers contains `Omega(R)` distinct blocker pairs.  A star-or-resource-
matching split at `W=sqrt(R)` gives a target-size source star or a target-size
endpoint bank even though the global blocker density vanishes.

## 1. Fixed-label witness uniqueness

Fix one macro pool `E_i`, one movement label `A`, and for every unsafe controller
`e=(x,y) in E_i` choose one noncontroller blocker pair `{p,q}` through the
candidate cell `(x,A)`.

### Proposition PP3alc -- PROVED

A fixed unordered source pair `{p,q}` is the chosen witness of at most one bad
movement entry in the fibre `(i,A)`.  The transposed statement holds for a fixed
refill label `(i,B)`.

#### Proof

The line `pq` meets the fixed new row `A` in at most one cell `(x,A)`.  The
matching layer containing `E_i` has at most one controller edge in old column
`x`.  Hence at most one entry of the fibre is witnessed by `{p,q}`.  For refill,
use the unique intersection with the fixed new column and uniqueness of a source
edge in an old row. ∎

Consequently a fibre of size `U` contains exactly `U` distinct chosen blocker
pairs.

## 2. Blocker star or full three-resource matching

Represent a bad entry by the three source resources

```text
{e,p,q},
```

where `e` is its controller and `{p,q}` its chosen blocker pair.  Controllers in
the fibre are automatically distinct.

Let `Delta_blk` be the maximum degree of a source point in the simple graph of
chosen blocker pairs.

### Theorem PP3ald -- PROVED

For every integer `D>=1`, a fixed-label fibre of size `U` has at least one of the
following outcomes.

1. A source point is an endpoint of at least `D` distinct blocker pairs.
2. There are at least

   ```text
   U/(3(D+1))
   ```

   bad entries with distinct controllers, endpoint-disjoint blocker pairs, and no
   selected controller equal to any selected blocker endpoint.

#### Proof

If `Delta_blk>=D`, use the first alternative.  Otherwise form the three-uniform
resource hypergraph on controller and blocker-point resources.  A source point
has blocker degree below `D` and controller degree at most one in the fixed-label
fibre, so its total hypergraph degree is below `D+1`.  Greedily select a hyperedge
and delete every hyperedge meeting one of its three source resources.  Each choice
removes fewer than `3(D+1)` entries. ∎

The second alternative is a full resource matching: candidate entries are
distinct because their controllers are distinct, even though their typed
movement or refill label is common.

## 3. Target-width consequence of one collapsed label

Use the slab scale

```text
R=m^(19/20+o(1)),
W=m^(19/40+o(1)),
R=Theta(W^2).
```

### Corollary PP3ale -- PROVED

Fix a constant `delta>0`.  If

```text
a_i(A)>=delta R
```

for one movement label, then for all sufficiently large `m` there is either

1. a blocker source star of degree at least `W`; or
2. a full fixed-label resource matching of size at least

   ```text
   (delta/4+o(1))W.
   ```

The same conclusion holds from `b_i(B)>=delta R`.

#### Proof

Apply PP3ald with `D=W`.  In the matching branch,

```text
U/(3(W+1))
>=
delta R/(3(W+1))
=
(delta/3+o(1))W.
```

The weaker displayed constant leaves room for an integral truncation. ∎

Thus a single collapsed controller denominator already has the local target
order; no positive global blocker density is required.

## 4. Layer refinement and credited endpoint bank

Take a full resource matching

```text
(e_j,{p_j,q_j}),  j in [Q].
```

Pigeonhole the chosen blocker pairs among the three unordered permutation-layer
types.  Retain at least `Q/3` pairs of one common type and choose one blocker
endpoint from a common layer in each pair.  The selected endpoints form a matching
layer bank and are disjoint from every selected controller.

Some selected blocker endpoints may themselves be active controllers elsewhere.
Puncture those endpoint values.  Since the designated fixed-label entry is
controlled by `e_j`, not by the selected blocker endpoint, every designated credit
incidence survives.  The cumulative domain loss in any macro is at most the
number of selected endpoints punctured there.

### Theorem PP3alf -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

A fixed-label resource matching of size `Omega(W)` has one of the following
outcomes.

1. After layer refinement and `O(W)=o(R)` batch puncturing, it becomes a
   controller-disjoint credited endpoint bank of size `Omega(W)`.
2. A source-regular thinning yields zero selected-credit self-recapture and a
   strict paid improvement.
3. Adaptive ambient thinning exposes a positive-density unary, rank-three, or
   rank-four foreign support core.
4. A source-valid selected state completes through final-state direct allocation.
5. Source, transition, anchor, Hall, alternating, distinguished-endpoint, or
   endpoint-host preparation fails explicitly.
6. The initial ownership/global-allocation certificate is absent.

#### Proof

The layer refinement is PP3hv--PP3hz.  Batch puncturing uses PP3akl and preserves
credit because selected blocker endpoints are disjoint from selected controllers.
The resulting tied bank enters PP3afn--PP3agg and the final-state allocation chain
PP3ahv--PP3ajx. ∎

Repeated endpoint punctures are governed by the reserve bookkeeping
PP3akk--PP3akp.

## 5. Labelwise margin collapse is converted

### Corollary PP3alg -- PROVED / CONDITIONAL CONVERSION INTERFACE

Suppose the initial controller-aware direct-allocation route has a movement- or
refill-margin collapse in the sense of PP3mf: for every fixed margin parameter
`delta>0`, along a subsequence some macro-label fibre has

```text
a_i(A)>(1-gamma-delta)R
```

or the transposed refill inequality.  Then that subsequence contains a fixed
positive `delta_0` for which PP3ale applies.  The margin collapse therefore yields
one of:

1. a free or punctured target-size source star;
2. a fixed-label credited endpoint bank of target order;
3. strict paid improvement or robust direct completion;
4. a positive-density ambient foreign support core;
5. an explicit source/transition/anchor/Hall/alternating/endpoint-host failure;
6. controller-puncture reserve exhaustion;
7. failure of the initial ownership/global-allocation certificate.

#### Proof

Choose any constant `delta_0<(1-gamma)/2`.  Eventual margin collapse gives a fibre
of size at least `delta_0R`.  Apply PP3ale.  Convert the star using
PP3agh--PP3akj and the bank using PP3alf. ∎

## 6. Revised vanishing-density blocker frontier

### Corollary PP3alh -- PROVED

The `o(1)` global movement/refill blocker-density regime cannot hide a labelwise
controller-margin collapse.  If every structured conversion above is excluded,
then for some fixed `delta>0`, eventually

```text
max_(i,A) a_i(A) <= (1-gamma-delta)R,
max_(i,B) b_i(B) <= (1-gamma-delta)R.
```

Hence all controller-defect denominators in PP3ly are uniformly `Omega(R)`.  The
remaining vanishing-density problem is purely quantitative: route labels through
the ownership host and control the capped refill and macro-total scores.  It is no
longer mixed with a collapsed individual movement or refill domain.

No completion of the no-three-in-line conjecture is claimed.
