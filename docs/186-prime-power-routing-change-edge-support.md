# Routing-skeleton changes have explicit entering and leaving edge support

CMR659--CMR663 give a finite vertex-routing skeleton for every factor matching.
This chapter attaches physical edge support to every change of routing skeleton.
That closes the bookkeeping gap between finite routing stock and the existing
entering-edge, token-incidence, and recreation ledgers.

Fix one factor host `H` of side `d` inside a parent of side

\[
t=p^h.
\]

Its source vertices have fixed child labels `r(x)` and its target vertices have
fixed child labels `s(y)` at the first split of the factor envelope.  For a
perfect matching `M`, the routing skeleton records both

\[
x\longmapsto s(M(x))
\]

for every source and

\[
y\longmapsto r(M^{-1}(y))
\]

for every target.

Let `M,N` be two perfect matchings of `H`.  Define the changed source and target
sets

\[
A_X(M,N)
=
\{x:s(M(x))\ne s(N(x))\},
\]

\[
A_Y(M,N)
=
\{y:r(M^{-1}(y))\ne r(N^{-1}(y))\}.
\]

## 1. Routing changes cannot move a single vertex

### Theorem CMR671 — PROVED

Each of `A_X(M,N)` and `A_Y(M,N)` has size zero or at least two.
Furthermore,

\[
\boxed{
\Gamma(M)\ne\Gamma(N)
\iff
A_X(M,N)\cup A_Y(M,N)\ne\varnothing.
}
\]

### Proof

The number of matching edges entering each target child is determined by the
number of target vertices in that child and is therefore the same for `M` and
`N`.  If one source changed target-child label, the old target child would lose
one unit and the new target child would gain one unit, so at least one other
source must compensate.  Thus `A_X` cannot have size one.

The symmetric argument uses the fixed number of source vertices in each source
child and shows that `A_Y` cannot have size one.

The source routing subsets `X_{rs}` are determined exactly by the first map, and
the target routing subsets `Y_{rs}` are determined exactly by the second map.
Hence both changed sets are empty exactly when the routing skeletons agree. ∎

## 2. Explicit entering and leaving routing support

Define

\[
E^+_\Gamma(M,N)
=
\{(x,N(x)):x\in A_X(M,N)\}
\cup
\{(N^{-1}(y),y):y\in A_Y(M,N)\},
\]

and define `E^-_\Gamma(M,N)` by replacing `N` with `M`.

### Theorem CMR672 — PROVED

If `\Gamma(M)\ne\Gamma(N)`, then

\[
\boxed{|E^+_\Gamma(M,N)|\ge2,}
\qquad
\boxed{|E^-_\Gamma(M,N)|\ge2.}
\]

Every edge of `E^+_\Gamma(M,N)` belongs to `N\setminus M`, and every edge of
`E^-_\Gamma(M,N)` belongs to `M\setminus N`.

### Proof

By CMR671, one of the changed vertex sets has size at least two.  Matching edges
incident with distinct source vertices are distinct, and matching edges incident
with distinct target vertices are distinct, giving the two cardinality bounds.

If a changed source `x` had the same matching edge in `M` and `N`, its target-
child label would be unchanged.  Likewise, if a changed target `y` had the same
incident edge, its source-child label would be unchanged.  Thus all displayed
support edges lie in the stated set differences. ∎

The support is physical edge churn, not merely a change of an abstract routing
label.

## 3. Alternating-cycle localization

### Theorem CMR673 — PROVED

Every edge of

\[
E^+_\Gamma(M,N)\cup E^-_\Gamma(M,N)
\]

lies on an alternating-cycle component of `M\triangle N` whose routing data
changes.  At least one such component contains two entering and two leaving
routing-support edges.

### Proof

The symmetric difference of two perfect matchings is a disjoint union of even
alternating cycles.  CMR672 places every routing-support edge in that symmetric
difference.

If every routing-changing component contained only one entering support edge,
it would also contain only one leaving support edge.  Following the cycle would
then change one source or target child assignment without a compensating change,
contradicting the child-count conservation used in CMR671.  Equivalently, select
a nonempty changed vertex set of size at least two; its incident support edges
belong to routing-changing components, and the union of those components
contains at least two edges in each direction.  If they lie in different
components, choose their union as the routing-changing support; if they lie in
one component, that component itself has the asserted support. ∎

The payment may be distributed across several alternating components, but its
total entering and leaving multiplicity is at least two.

## 4. Finite routing-change stock or one recurrent edge

Consider `R` transitions at one fixed owner-labelled factor and envelope for
which the routing skeleton changes.  Count the entering routing-support edges
with multiplicity.

### Theorem CMR674 — PROVED

For every integer `\lambda\ge2`, at least one of the following holds.

1. **Recurrent routing edge.**  One physical factor edge occurs in at least
   `\lambda` entering routing-support sets.
2. **Finite routing-change history.**
   \[
   \boxed{
   R
   \le
   \left\lfloor
   \frac{(\lambda-1)|E(H)|}{2}
   \right\rfloor
   \le
   \left\lfloor
   \frac{(\lambda-1)d^2}{2}
   \right\rfloor.
   }
   \]

The same statement holds for leaving routing-support edges.

### Proof

CMR672 contributes at least two entering incidences per routing-changing
transition.  If no physical edge occurs `\lambda` times, every edge contributes
at most `\lambda-1` incidences.  Hence

\[
2R
\le
(\lambda-1)|E(H)|
\le
(\lambda-1)d^2.
\]

The leaving proof is identical. ∎

## 5. Exact full-token and recreation payment

### Theorem CMR675 — PROVED

Let

\[
C^+_\Gamma
=
\sum_{j=1}^{R}|E^+_\Gamma(M_j,M_{j+1})|
\]

be the total entering routing-support multiplicity.  Its exact labelled nonroot
full-token incidence in the parent of side `t=p^h` is

\[
\boxed{
(p+1)(h-1)C^+_\Gamma.
}
\]

In particular, `R` routing changes carry at least

\[
\boxed{2R(p+1)(h-1)}
\]

labelled entering-edge incidences.  Every selected conflict recreated across a
routing-changing transition contains an entering edge of the complete matching
transition; if its recreation is supported on the changed routing data, it
contains an edge in the routing-changing alternating components of CMR673.

### Proof

CMR413 assigns exactly `(p+1)(h-1)` labelled nonroot full-token incidences to
every physical parent edge.  Apply this with multiplicity and use CMR672.

The recreation statement is CMR418--CMR421 applied to the full matching
transition.  Routing-supported recreation lies on a component in which the
routing data changed, hence on the component support identified in CMR673. ∎

This statement does not declare repeated occurrences fresh: CMR674 isolates a
recurrent physical edge first.

## 6. Routing-history endpoint

### Corollary CMR676 — PROVED

Every simple factor history at one fixed factor-envelope owner reaches at least
one of the following.

1. A finite routing-skeleton history bounded by CMR661.
2. A finite routing-change history bounded by CMR674.
3. One recurrent physical routing edge, which enters the existing edge-
   recurrence, reintroduction, packet-recreation, and token ledgers.
4. One recurrent routing skeleton, in which all remaining variation lies in the
   exact strict child product of CMR659 and enters CMR664--CMR670 and
   CMR677--CMR683.

### Proof

Apply CMR661 to the state history.  Charge changes by CMR674--CMR675.  If a
skeleton recurs, use the exact child product CMR659. ∎

No all-`n` theorem is claimed.  Changed-vertex conservation, entering/leaving
support, recurrence bounds, and token arithmetic are checked in
[`scripts/verify_prime_power_routing_change_support.py`](../scripts/verify_prime_power_routing_change_support.py).
