# Controller-shadow resource matching

The star-or-matching theorem PP3hu extracts structure from distinct blocker
pairs.  For patching, one also wants the associated candidate labels and
controller edges to be distinct.  Positive-density controller-shadow failure
contains enough entries to enforce all of these disjointness conditions at
once.

## 1. The bad-entry resource hypergraph

For every bad controller-aware movement or refill entry, choose one
noncontroller blocker pair as in PP3hr.  Represent the entry by the four-set

\[
 \{\lambda,e,p,q\},
\]

where:

- `lambda` is the typed new-coordinate label: a movement row or a refill
  column;
- `e` is the controller source edge;
- `{p,q}` is the chosen noncontroller blocker pair.

Typed labels and source points are disjoint resource classes.  Inside one
entry, the three source points `e,p,q` are distinct.

### Proposition PP3hw -- PROVED

The resource degrees satisfy:

1. every typed label belongs to at most `MR` bad entries;
2. every source point occurs as a controller in at most `2T` bad entries;
3. every fixed blocker pair contributes to at most `2T` bad entries.

#### Proof

For one movement or refill label, there are `M` pools and `R` possible
controller edges.  A fixed source point in the chosen matching layer controls
at most one movement entry for each of the `T` movement labels and at most one
refill entry for each of the `T` refill labels.  The blocker-pair bound is
PP3hr. ∎

## 2. Source-star or full resource matching

Let `U` be the number of bad entries, and let

\[
 D=MR.
\]

### Theorem PP3hx -- PROVED

At least one of the following holds.

1. **Source-star concentration.** Some source point is an endpoint of chosen
   blocker pairs in at least

   \[
    D-2T
   \]

   bad entries.

2. **Resource matching.** There are at least

   \[
    \boxed{
    \frac{U}{4MR}
    }
   \]

   bad entries with pairwise distinct typed labels and pairwise disjoint sets of
   all source points appearing as controllers or blocker endpoints.

#### Proof

Make the four-uniform resource hypergraph described above.  If some source
point has total degree at least `D`, at most `2T` of its incidences use it as a
controller by PP3hw.  The remaining at least `D-2T` incidences use it as a
blocker endpoint, giving alternative 1.

Otherwise every source-point degree is below `D`, while every label degree is
at most `MR=D`.  Greedily choose a hyperedge and delete every hyperedge sharing
one of its four resources.  One selection removes fewer than

\[
 D+3D=4D
\]

hyperedges.  Hence at least `U/(4MR)` pairwise resource-disjoint entries are
selected. ∎

## 3. Prime-gap-scale dichotomy

Assume a `delta` fraction of all `2MTR` controller-aware cell entries is bad.
Then

\[
 U\ge2\delta MTR.
\]

### Corollary PP3hy -- PROVED

At the slab-optimal parameters, one of the following holds.

1. One source point is incident to blocker pairs in at least

   \[
    \Omega(m^{19/40})
   \]

   distinct bad entries and in at least

   \[
    \Omega(m^{19/40})
   \]

   distinct blocker pairs.

2. There are

   \[
    \boxed{
    \Omega_\delta(m^{21/40})
    }
   \]

   bad entries having distinct movement/refill labels, distinct controller
   edges, and pairwise endpoint-disjoint blocker pairs; moreover no controller
   point is a blocker endpoint of another selected entry.

#### Proof

In the first alternative of PP3hx, `D=MR=Theta(m)` and `T=m^{21/40+o(1)}`, so
`D-2T=Theta(m)`.  A fixed blocker pair witnesses at most `2T` entries, hence the
number of distinct blocker partners is

\[
 \Omega(m/T)=\Omega(m^{19/40}).
\]

In the second alternative,

\[
 \frac{U}{4MR}
 \ge
 \frac{2\delta MTR}{4MR}
 =
 \frac\delta2T.
\]

Resource disjointness gives all stated properties. ∎

The star conclusion is stronger in entry multiplicity than PP3hu, while the
matching conclusion preserves the candidate resources needed by a patch or
trade construction.

## 4. Layer refinement of the resource matching

The controller points all belong to the matching layer from which the pools
were taken.  Classify each selected blocker pair by its unordered layer type
`P_0P_0`, `P_0P_1`, or `P_1P_1`.

### Corollary PP3hz -- PROVED

A resource matching of size `Q` contains a submatching of size at least `Q/3`
with one common blocker layer type.  Choosing one endpoint from every blocker
pair in a common available layer gives a source matching disjoint from all
selected controller points whenever that layer is the controller layer; in the
other same-layer case it gives a second disjoint matching layer.

#### Proof

Pigeonhole the three layer types and apply the endpoint choice from PP3hv.
Resource disjointness ensures that no chosen blocker endpoint equals a selected
controller point. ∎

## 5. Revised structured alternatives

Positive-density failure of the controller-aware graph now exposes one of two
objects at exactly the required scales.

- A blocker star with `m^{19/40}` distinct rays, aligned with alternating star
  neutralization.
- A resource matching with `m^{21/40}` candidate labels, controller deletions,
  and endpoint-disjoint blocker demands, aligned with matching-first or
  tomographic trade banks.

What remains is a collateral-controlled conversion theorem: use one of these
objects to enlarge the controller-aware safe domains or to install the
associated candidate entries while paying all blocker demands.  Diffuse
failure with no such structured resource bank is impossible.
