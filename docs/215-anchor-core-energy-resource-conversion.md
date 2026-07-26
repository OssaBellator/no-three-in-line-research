# Anchor-core energy converts to a source star or endpoint bank

The canonical same-slot anchor deficiency core PP3vn--PP3wa reduces direct
allocation failure to a slot-expanded anchor energy `E_slot` on `d` necessary
ownership crossings.  This chapter converts that weighted obstruction into the
same source structures already handled by the marked-star and recapture-free
endpoint-bank chains.

The conversion uses one exact multiplicity bound.  A physical controller--anchor
pair can contribute to at most `D_m` movement/refill label pairs by the product
factorization PP3dv--PP3dw, and can be replicated through at most `W` unused macro
slots in the slot-expanded core.  Thus no physical pair contributes more than
`W D_m` units to `E_slot`.

At the slab scale the threshold `u` used in the anchor ownership theorem is much
larger than `D_m W^3`.  Consequently every weighted core obstruction from PP3wa
already contains either a target-size source star or a target-size endpoint-
disjoint controller--anchor bank.

## 1. Physical anchor certificates in the completion core

Use the movement canonical core; the refill case is transposed.  Let

```text
L_0 = unmatched movement labels,
R_0 = unmatched macro slots,
|L_0|=|R_0|=d.
```

For a slot `s` belonging to macro `i(s)`, the completion weight is

```text
w(A,s)=U_(i(s))(A).
```

Expand each unit of `U_i(A)=sum_B u_i(A,B)` by choosing one retained anchor
witness `p` for every counted controller `e` in `U_(i,A,B)^ctrl`.  A resulting
physical certificate is

```text
(A,B,e,p,s),
```

where `s` is an unused clone of the macro containing `e` and

```text
(A-v_p)(B-u_p)=(x_e-u_p)(y_e-v_p)>0.
```

The total number of expanded certificates, counted with slot multiplicity, is
exactly `E_slot`.

### Proposition PP3akv -- PROVED

Fix one physical ordered controller--anchor pair `(e,p)`.  Its multiplicity in the
slot-expanded completion core is at most

```text
W D_m,
```

where

```text
D_m=max_(1<=n<=m^2) tau(n)=m^(o(1)).
```

#### Proof

For fixed `e,p`, PP3dw permits at most `D_m` label pairs `(A,B)`.  In one macro the
same physical label/controller certificate can be replicated through at most the
`W` capacity clones of that macro.  Multiply the two bounds. ∎

The statement is unaffected by duplicate anchor witnesses: choosing one witness
for each counted controller only decreases multiplicity.

## 2. Distinct controller--anchor pair population

Let `L_anc` be the number of distinct unordered source pairs `{e,p}` appearing in
at least one expanded core certificate.

### Corollary PP3akw -- PROVED

One has

```text
L_anc >= E_slot/(W D_m).
```

#### Proof

Assign each expanded certificate to its physical pair.  Proposition PP3akv bounds
every fibre by `W D_m`. ∎

Thus high slot energy cannot be created solely by clone replication or by many
divisor representations of one source pair.

## 3. Source-star or endpoint-disjoint anchor bank

Form the simple graph `K_anc` on the saturated source points whose edges are the
`L_anc` distinct controller--anchor pairs.

### Theorem PP3akx -- PROVED

For every integer `D>=1`, at least one of the following holds.

1. One source point lies in at least `D` physical anchor pairs.
2. There is an endpoint-disjoint family of at least

   ```text
   E_slot/(2D W D_m)
   ```

   controller--anchor pairs.

#### Proof

If the maximum degree of `K_anc` is at least `D`, use the first alternative.  If
not, greedily select an edge and delete every edge incident with either endpoint.
Each choice removes fewer than `2D` graph edges.  Corollary PP3akw then gives the
second bound. ∎

### Corollary PP3aky -- PROVED

If

```text
E_slot > 2 D_m W^3,
```

then the core contains either

1. a source star of degree at least `W`; or
2. an endpoint-disjoint family of at least `W` controller--anchor pairs.

#### Proof

Apply PP3akx with `D=W`. ∎

This is a local target-width conclusion; no positive-density assumption on the
whole controller-shadow table is used.

## 4. Anchor-layer refinement and batch puncturing

Take an endpoint-disjoint family

```text
{e_j,p_j},  j in [Q],
```

from PP3aky, with one designated same-slot candidate incidence for every pair.
All controller endpoints `e_j` lie in the matching layer supporting the active
pools.  Pigeonhole the anchor endpoints `p_j` between the two permutation layers.
After losing a factor two, assume all retained anchors lie in one common layer.
They have distinct old rows and columns because the source pairs are endpoint-
disjoint.

Some retained anchors may themselves be active controllers in other macros.  Let
`X_i` be those anchor points lying in controller pool `E_i`; puncture every point
of `X_i` before moving the anchor bank.

### Proposition PP3akz -- PROVED

The designated anchor incidences all survive the batch puncture, and every
controller-aware domain in macro `i` loses at most `|X_i|` values.  In particular,
for a bank of size `Q`,

```text
max_i |X_i| <= Q.
```

#### Proof

The designated entry for `{e_j,p_j}` is controlled by `e_j`.  Endpoint
disjointness gives `p_j!=e_k` for every selected pair, so puncturing any anchor
`p_j` deletes no designated entry.  The cumulative domain estimate is PP3akl:
deleting source points improves safety and only the punctured controller values
are unavailable. ∎

At the active scale, a target-size bank has `Q=O(W)=o(R)`, so this batch puncture
uses a vanishing fraction of every macro domain.

## 5. Credited endpoint-bank conversion

After the batch puncture, the selected anchors form a controller-disjoint matching
inside one permutation layer.  Moving anchor `p_j` while retaining controller
`e_j` destroys its designated same-slot anchor incidence.  Thus the anchor bank
has at least one removal-credit unit per endpoint.

### Theorem PP3ala -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

A target-size endpoint-disjoint anchor bank from PP3aky has one of the following
outcomes.

1. A source-regular thinning has zero selected-credit self-recapture and yields a
   strict paid controller-shadow improvement.
2. Adaptive ambient thinning exposes a positive-density unary, rank-three, or
   rank-four foreign support core.
3. A source-valid final state completes through robust direct allocation.
4. Source, transition, anchor, Hall, alternating, distinguished-endpoint, or
   endpoint-host preparation fails explicitly.
5. The initial controller-aware ownership/global-allocation certificate is absent.

#### Proof

Use Proposition PP3akz to make every selected anchor free relative to the active
controller infrastructure.  The selected physical anchor lines and their
designated candidate incidences form a credited tied endpoint bank.  Apply the
credited-line self-recapture theorem PP3afn--PP3aft, the recapture-free resource
endpoint PP3afu--PP3afz, adaptive ambient support thinning PP3aga--PP3agg, and the
final-state direct-allocation chain PP3ahv--PP3ajx. ∎

No credit is lost when an anchor is punctured, because its designated entry is
controlled by the opposite endpoint `e_j`.

## 6. Every weighted anchor-core obstruction crosses the threshold

Use the slab-optimal scales

```text
M=m^(1/20+o(1)),
R=m^(19/20+o(1)),
W=m^(19/40+o(1)),
T=MW=m^(21/40+o(1)).
```

The anchor threshold from PP3of is

```text
u=m^(-1/40+zeta) R T,
0<zeta<1/40.
```

Since `R=Theta(W^2)` and `T=MW`,

```text
u/(D_m W^3)
=
(m^(-1/40+zeta) M)/D_m
=
m^(1/40+zeta-o(1))
-> infinity.
```

### Corollary PP3alb -- PROVED / CONDITIONAL CONVERSION INTERFACE

Suppose the core-aware local Ore theorem PP3vy fails because one canonical
movement or refill core satisfies the energy alternative PP3wa.  Then, for all
sufficiently large `m`, that core contains either

1. a target-size source star; or
2. a target-size endpoint-disjoint controller--anchor bank.

The star is converted by the free-centre, partner-bank, or one-controller
puncture chains PP3agh--PP3akj.  The bank is converted by PP3ala.  Hence a weighted
same-slot anchor core is no longer an abstract terminal object.

#### Proof

PP3wa gives, for a nonzero deficiency `d`,

```text
E_slot/d > u + nonnegative local slack term.
```

Therefore `E_slot>u`.  The displayed active-scale ratio gives
`E_slot>2D_mW^3` eventually.  Apply PP3aky, then the stated conversion chains. ∎

The remaining direct anchor frontier is now confined to failure of the baseline
controller denominators/local Ore slack, explicit marked or endpoint-host
obstructions during conversion, puncture-reserve exhaustion, or a branch that
still insists on one-step potential descent.

No completion of the no-three-in-line conjecture is claimed.
