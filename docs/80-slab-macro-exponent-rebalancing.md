# Slab macro exponent rebalancing

The balanced reduction PP3dg used monotone matching-pool extraction.  The
Erdos--Szekeres step imposed the constraint `R^2=o(m)` and led to

\[
 R=m^{19/40},\qquad M=m^{23/80}.
\]

The product-LLL macro theorem PP3dn does not require endpoint monotonicity.
After PP3ga, arbitrary matching pools can instead be taken from consecutive
column slabs.  Their only supply constraint is `MR<=m`.  Re-optimizing under
that weaker constraint produces much larger local pools and far fewer macro
variables.

## 1. Prime-gap-scale slab parameters

Fix constants `a,b>0` with

\[
 ab<1.
\]

Put

\[
 M=\lfloor a m^{1/20}\rfloor,
 \qquad
 R=\lfloor b m^{19/20}\rfloor.
\]

Choose `M` disjoint consecutive old-column intervals of length `R`, and let
`E_i` be the matching edges whose columns lie in the `i`-th interval, as in
PP3ga.

### Theorem PP3gr -- PROVED

For all sufficiently large `m`, every perfect matching layer contains these
`M` pairwise disjoint matching pools, each of size `R`.  Moreover

\[
 MR=(ab+o(1))m<m.
\]

If every macro has slot domains of size at least `gamma R`, then each pool
supports internally no-three width

\[
 W=\left\lfloor\frac{\gamma\sqrt R}{16}\right\rfloor
\]

by PP3ea, and the total installed width satisfies

\[
 \boxed{
 MW
 =
 \left(
 \frac{a\gamma\sqrt b}{16}+o(1)
 \right)m^{21/40}.
 }
\]

#### Proof

The pool supply follows from `MR<m` and PP3ga.  PP3ea gives the displayed width
on every pool.  Finally,

\[
 M\sqrt R
 =
 (a\sqrt b+o(1))
 m^{1/20+19/40}
 =
 (a\sqrt b+o(1))m^{21/40}.
\]

Multiply by `gamma/16`. ∎

Thus the published prime-gap exponent is reached with

\[
 \boxed{
 M=m^{1/20+o(1)},
 \qquad
 R=m^{19/20+o(1)},
 \qquad
 W=m^{19/40+o(1)}.
 }
\]

The total number of selected source-pool edges is a fixed fraction of one
matching layer rather than `o(m)`, but remains below `m` by the choice `ab<1`.
Only `2W` values are ultimately selected from each pool.

## 2. Comparison with the monotone-pool balance

The previous exponents were

\[
 M=m^{23/80},\qquad R=m^{38/80},\qquad W=m^{19/80}.
\]

The slab balance gives

\[
 M=m^{4/80},\qquad R=m^{76/80},\qquad W=m^{38/80}.
\]

Both have

\[
 MW=m^{42/80}=m^{21/40},
\]

but the number of macro variables falls by the factor

\[
 m^{19/80},
\]

while each local domain grows by the reciprocal square-scale factor.  This is
available precisely because neither the product-LLL internal patch nor the
one-sided slab separation needs monotone endpoint order inside a pool.

## 3. Two-slot external mass becomes negligible

Let

\[
 T=MW
\]

be the total new width, so there are `2T` slots globally.  Suppose every slot
domain has size at least `gamma R`.

### Proposition PP3gs -- PROVED

Assume every grouped external pair event containing slots `s,t` has probability
at most

\[
 \frac C R
\]

for an absolute constant `C`.  Even if every other slot is an active partner,
the total external pair-event mass incident to one slot is at most

\[
 \boxed{
 \frac{2CT}{R}
 =
 O(m^{-17/40}).
 }
\]

In particular it is `o(1)`.

#### Proof

There are fewer than `2T` partner slots.  Sum the probability bound and use

\[
 \frac TR
 =m^{21/40-19/20+o(1)}
 =m^{-17/40+o(1)}.
\]

∎

This applies to:

- ordinary fixed-anchor pair events when their relation size is `O(R)`;
- cross-macro pair events under the universal PP3gh probability bound;
- any additional grouped rank-two relation with `O(1/R)` probability.

Therefore two-slot classes with that probability scale no longer consume a
positive fraction of the PP3fj budget.  The asymptotic obstruction is rank
three or unary controller-shadow density.

## 4. Rank-three scale

Without geometric compression, one slot belongs to `Theta(T^2)` slot triples.
At probability `O(1/R)`, their total mass has scale

\[
 \frac{T^2}{R}
 =m^{2/20+o(1)}
 =m^{1/10+o(1)}.
\]

### Proposition PP3gt -- PROVED

In the column-slab architecture, the `2M+1F` events localized by PP3gp have at
most

\[
 (2W-1)(2T-2W)+(M-1)\binom{2W}{2}
 =O(MW^2)
\]

formal slot triples incident to one slot.  Under the universal `O(1/R)` event
probability bound, their total coarse mass is

\[
 \boxed{
 O\left(\frac{MW^2}{R}\right)
 =O(M)
 =O(m^{1/20}).
 }
\]

#### Proof

Use PP3gq and `W^2=Theta(R)`. ∎

Thus slab localization saves another factor `M`: the repeated-movement mixed
class needs a completion-energy saving of only `m^{1/20+o(1)}`, while a fully
unrestricted rank-three population would need `m^{1/10+o(1)}`.

## 5. Controller-aware weighted endpoint

### Corollary PP3gu -- PROVED

Use the controller-aware domains PP3hn--PP3ho, the global coordinate allocation
PP3fw, and the column-slab architecture.  Assume:

1. all external grouped pair events have total incident mass `o(1)`;
2. the grouped rank-three relations satisfy, for every slot `s`,

\[
 \sum_{\{t,u\}}
 \frac{|\Xi_{s,t,u}|}{|H_s||H_t||H_u|}
 \le
 \frac1{48}-o(1).
\]

Then a simultaneous saturated no-three assignment exists, and its fixed-rank
cylinders retain the PP3fl spread bound.

#### Proof

Controller-aware domains remove every unary retained-pair and same-slot anchor
certificate.  The internal mass is at most `1/16+o(1)` by PP3fj.  Hypotheses 1
and 2 keep the remaining external mass within the residual `1/48-o(1)` budget.
Apply PP3fk and PP3fl. ∎

The corresponding row-slab statement is obtained by transposition.

## 6. Subsequent closure of the energy side

The later chapters strengthen this preliminary endpoint.

- PP3he proves all patch-only cross-macro mass is `o(1)` at the slab-optimal
  scale.
- PP3hk proves all ordinary two-slot source-anchor mass is `o(1)`.
- PP3ho supplies the exact controller-aware unary safety interface.

Thus the remaining task is not rank-two or rank-three completion energy.  It is
the density and saturation-compatible global allocation of the
controller-aware domains `H_{A,B}^{ctrl}`, or a collateral-controlled trade
that improves their noncontroller blocker shadow.
