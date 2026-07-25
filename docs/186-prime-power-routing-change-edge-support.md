# Routing-skeleton changes have explicit entering and leaving edge support

CMR659--CMR663 give a finite vertex-routing skeleton for every factor matching.
This chapter attaches physical edge support to every change of routing skeleton.
The support may be distributed over several alternating-cycle components, so all
payment statements are made for their union rather than for one component.

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

and

\[
y\longmapsto r(M^{-1}(y)).
\]

For perfect matchings `M,N`, define

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

Each of `A_X(M,N)` and `A_Y(M,N)` has size zero or at least two.  Furthermore,

\[
\boxed{
\Gamma(M)\ne\Gamma(N)
\iff
A_X(M,N)\cup A_Y(M,N)\ne\varnothing.
}
\]

### Proof

The number of matching edges entering each target child is fixed by the number
of target vertices in that child.  If exactly one source changed target-child
label, one child would lose one unit and another would gain one unit without
compensation.  Thus `A_X` cannot have size one.  The symmetric argument, using
the fixed source-child populations, handles `A_Y`.

The sets `X_{rs}` are determined by the first routing map and the sets `Y_{rs}`
by the second, so both changed sets are empty exactly when the skeletons agree.
∎

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

By CMR671, one changed vertex set has size at least two.  Matching edges incident
with distinct sources are distinct, as are matching edges incident with distinct
targets, giving both cardinality bounds.

A changed source cannot have the same edge in both matchings because its target-
child label changed.  A changed target cannot have the same incident edge because
its source-child label changed.  Hence the support lies in the stated set
differences. ∎

## 3. Alternating-component union support

### Theorem CMR673 — PROVED

Every edge of

\[
E^+_\Gamma(M,N)\cup E^-_\Gamma(M,N)
\]

lies on an alternating-cycle component of `M\triangle N` whose routing data
changes.  Let `\mathcal K_\Gamma(M,N)` be the union of all such components.
Then

\[
\boxed{
|N\cap\mathcal K_\Gamma(M,N)|\ge2,
\qquad
|M\cap\mathcal K_\Gamma(M,N)|\ge2.
}
\]

The compensating changes may occur on different alternating cycles.

### Proof

The symmetric difference of two perfect matchings is a disjoint union of even
alternating cycles.  CMR672 places every routing-support edge in that symmetric
difference.  A component containing such an edge changes at least one source or
target routing label and is therefore included in `\mathcal K_\Gamma`.

The union contains all of `E^+_\Gamma` and all of `E^-_\Gamma`, so CMR672 gives
the two lower bounds.  No assertion about one individual component is needed or
made. ∎

## 4. Finite routing-change stock or one recurrent edge

Consider `R` transitions at one fixed owner-labelled factor and envelope for
which the routing skeleton changes.

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
transition.  If no edge occurs `\lambda` times, every edge contributes at most
`\lambda-1` incidences, so

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
\sum_{j=1}^{R}|E^+_\Gamma(M_j,M_{j+1})|.
\]

Its exact labelled nonroot full-token incidence in the parent of side `t=p^h`
is

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
transition.  Any recreation assigned specifically to changed routing data is
supported on the alternating-component union `\mathcal K_\Gamma`.

### Proof

CMR413 assigns exactly `(p+1)(h-1)` labelled nonroot full-token incidences to
every physical parent edge.  Apply this with multiplicity and use CMR672.

The recreation statement is CMR418--CMR421.  A recreation assigned to changed
routing data must use an entering edge on a component where that routing data
changes, which is precisely the union in CMR673. ∎

Repeated occurrences are not declared fresh; CMR674 isolates a recurrent
physical edge first.

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
