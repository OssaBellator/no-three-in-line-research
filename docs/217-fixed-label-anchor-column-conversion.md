# Fixed-label anchor columns convert to stars or banks

The one-sided refill-slack theorem PP3ng--PP3nj leaves a possible obstruction in
one numerical refill label:

```text
sum_i V_i(B),
V_i(B)=sum_A u_i(A,B).
```

For a fixed refill label `B`, the same-slot product equation determines the
movement label `A` uniquely from a physical controller--anchor pair.  Thus this
column mass already counts distinct physical pairs; unlike the full anchor table,
there is no divisor multiplicity and no slot-clone multiplicity.

Consequently anchor column mass of order `R=W^2` contains a target-size source
star or a target-size endpoint-disjoint anchor bank.  The movement-row analogue is
identical.

## 1. Fixed-label physical-pair uniqueness

Fix a refill label `B`.  For every counted controller

```text
e=(x,y) in U_(i,A,B)^ctrl
```

choose one retained source anchor `p=(u,v)` satisfying

```text
(A-v)(B-u)=(x-u)(y-v)>0.
```

### Proposition PP3ali -- PROVED

A fixed ordered physical controller--anchor pair `(e,p)` occurs for at most one
movement label `A` when `B` is fixed.  Therefore it contributes at most one unit
to

```text
C_B=sum_i V_i(B).
```

The transposed statement holds for a fixed movement label `A` and the total row
mass `sum_i U_i(A)`.

#### Proof

For fixed `B,e,p`, the product equation gives

```text
A-v=((x-u)(y-v))/(B-u).
```

If the right side is a positive integer in the allowed range, it determines one
value of `A`; otherwise there is no certificate.  The controller belongs to one
active pool, so there is no macro duplication. ∎

Hence `C_B` distinct counted incidences yield `C_B` distinct physical source
pairs.

## 2. Star-or-matching extraction

Form the simple graph on source points whose edges are the distinct
controller--anchor pairs counted in `C_B`.

### Theorem PP3alj -- PROVED

For every integer `D>=1`, at least one of the following holds.

1. One source point lies in at least `D` fixed-label anchor pairs.
2. There is an endpoint-disjoint family of at least

   ```text
   C_B/(2D)
   ```

   controller--anchor pairs.

#### Proof

If the graph has maximum degree at least `D`, use the first alternative.
Otherwise greedily select an edge and delete all edges incident with its two
endpoints.  Each selection removes fewer than `2D` edges. ∎

### Corollary PP3alk -- PROVED

If, for one fixed constant `c>0`,

```text
C_B>=cR,
```

then at the slab scale `R=Theta(W^2)` the anchor column contains either

1. a source star of degree at least `W`; or
2. an endpoint-disjoint controller--anchor family of size `Omega_c(W)`.

The same conclusion holds for fixed movement-row mass `sum_iU_i(A)>=cR`.

#### Proof

Apply PP3alj with `D=W`.  In the matching branch,

```text
C_B/(2W)=Omega_c(R/W)=Omega_c(W).
```

∎

This conclusion is compatible with globally vanishing anchor density: one
numerical label alone may carry the whole concentration.

## 3. Conversion of the fixed-label anchor bank

Take an endpoint-disjoint family from PP3alk.  Pigeonhole the anchor endpoints
between the two source permutation layers and retain a common-layer subfamily.
Every retained anchor is disjoint from every retained controller.

If a retained anchor is itself an active controller elsewhere, puncture that
anchor value.  Its designated same-slot entry is controlled by the opposite
endpoint, so the credit survives.  At most `O(W)=o(R)` values are punctured in any
one macro.

### Theorem PP3all -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

A fixed-label anchor column or row of mass `Omega(R)` has one of the following
outcomes.

1. A free or one-controller-punctured source star of target size.
2. A controller-disjoint credited anchor endpoint bank of size `Omega(W)`.
3. A strict paid controller-shadow improvement after recapture-free thinning.
4. Robust final-state direct completion.
5. A positive-density ambient unary, rank-three, or rank-four foreign support
   core.
6. An explicit source, transition, anchor, Hall, alternating,
   distinguished-endpoint, or endpoint-host obstruction.
7. Controller-puncture reserve exhaustion or failure of the initial allocation
   certificate.

#### Proof

Convert the star using PP3agh--PP3akj.  For the matching branch, use the common-
layer refinement and batch puncture PP3akz, then apply the credited-line,
recapture-free, ambient-support, and final-state chains PP3afn--PP3ajx. ∎

## 4. Capped-refill anchor concentration is closed

The global refill-slack theorem PP3nj gives the alternative

```text
sum_i V_i(B)=Omega(R(T-r_score))
```

for some refill label `B`.

### Corollary PP3alm -- PROVED / CONDITIONAL CONVERSION INTERFACE

If the movement ownership bottleneck satisfies

```text
r_score<=T-1,
```

then every anchor-column concentration alternative in PP3nj has mass `Omega(R)`
and therefore enters PP3all.  It is no longer an independent capped-refill
obstruction.

If `r_score=T`, the movement ownership side is itself completely blocked and the
remaining object is the ownership Hall core, not refill-anchor concentration.

#### Proof

The integer gap `T-r_score` is at least one in the first case, so PP3nj gives
`C_B=Omega(R)`.  Apply PP3alk--PP3all.  The second statement is the definition of
the bottleneck endpoint. ∎

Thus the one-sided allocation frontier is narrowed to movement ownership-Hall
failure, macro-total controller defect or excess-shadow mass, fixed-label
movement/refill margin collapse already handled by PP3alc--PP3alh, explicit host
failure during conversion, or the fully blocked bottleneck value `r_score=T`.

No completion of the no-three-in-line conjecture is claimed.
