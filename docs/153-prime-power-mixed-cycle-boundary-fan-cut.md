# Concentrated mixed-cycle witnesses force a boundary-edge fan or a small return cut

CMR472--CMR476 show that canonical mixed-cycle witnesses either pack
vertex-disjointly, disappear after deleting a sparse boundary interface, or
concentrate through one contraction vertex. This chapter sharpens the last
alternative. Label multiplicity through one vertex first converts to many
distinct mixed cycles through one actual colour-boundary arc. Directed edge
Menger then turns that boundary arc into an edge-disjoint return-path fan or a
small cut meeting every cycle through it.

Use the notation of CMR472--CMR476. Thus `D` is an `m`-vertex matching-
contraction digraph, `\beta:V(D)\to\{0,1\}` is the right-column colour, and

\[
\mathcal B
=
\{i\to j:\beta(i)\ne\beta(j),\ j\leadsto i\}
\]

is the family of cyclic colour-boundary arcs. For every `a\in\mathcal B`,
`\Gamma_a` is the canonical shortest-return witness of CMR473.

## 1. From vertex congestion to a boundary arc

Fix a contraction vertex `v` and write

\[
\Delta
=
|\{a\in\mathcal B:v\in V(\Gamma_a)\}|.
\]

Let `\mathcal C_v` be the set of distinct underlying directed cycles represented
among those `\Delta` labelled witnesses, and put

\[
C_v=|\mathcal C_v|.
\]

### Theorem CMR477 — PROVED

If `\Delta>0`, then

\[
\boxed{
C_v
\ge
\left\lceil\frac{\Delta}{m}\right\rceil.
}
\]

Moreover, some cyclic colour-boundary arc `a\in\mathcal B` belongs to at least

\[
\boxed{
L_v
\ge
\left\lceil\frac{2C_v}{|\mathcal B|}\right\rceil
\ge
\left\lceil\frac{2\Delta}{m|\mathcal B|}\right\rceil
}
\]

distinct mixed cycles from `\mathcal C_v`. Since

\[
|\mathcal B|\le m(m-1),
\]

one also has the universal lower bound

\[
\boxed{
L_v
\ge
\left\lceil
\frac{2\Delta}{m^2(m-1)}
\right\rceil
}
\]

for `m\ge2`.

### Proof

One underlying simple cycle has at most `m` arcs and therefore can carry at most
`m` distinct boundary-arc labels. Hence `\Delta` labelled witnesses represent at
least `\lceil\Delta/m\rceil` distinct cycles.

Every distinct mixed cycle contains at least two arcs of `\mathcal B` by
CMR472. Counting incidences between the `C_v` cycles and the boundary arcs gives
at least `2C_v` incidences. Pigeonholing over `|\mathcal B|` arcs yields the
first bound for `L_v`; the remaining estimates follow from `C_v\ge\Delta/m`
and the number of loopless directed arcs. ∎

Thus exchange-vertex concentration necessarily propagates to concentration on
one concrete source-switch edge.

## 2. Return paths through one boundary arc

Fix

\[
a=u\to w\in\mathcal B.
\]

Delete `a` from `D`. A **return path** for `a` is a simple directed path

\[
Q:w\leadsto u
\]

in `D-a`.

### Theorem CMR478 — PROVED

The map

\[
Q
\longmapsto
\{a\}\cup Q
\]

is a bijection between simple return paths for `a` and simple directed cycles
containing `a`. Every resulting cycle is mixed-colour.

### Proof

Adjoining `a=u\to w` to a simple path from `w` back to `u` gives a simple
directed cycle containing `a`. It is mixed because `a` crosses the colour
classes.

Conversely, removing `a` from a simple directed cycle containing it leaves a
simple directed path from `w` to `u`. The operations are inverse. ∎

The cycle-overlap problem through `a` is therefore exactly a directed path
packing problem.

## 3. Edge-disjoint theta fan or return cut

Let

\[
\nu(a)
\]

be the maximum number of pairwise edge-disjoint return paths from `w` to `u` in
`D-a`, and let

\[
\tau(a)
\]

be the minimum size of a directed edge cut in `D-a` meeting every such path.

### Theorem CMR479 — PROVED

One has

\[
\boxed{\nu(a)=\tau(a).}
\]

Consequently, for every integer `q\ge1`, at least one of the following holds.

1. **Boundary theta fan.** There are `q` edge-disjoint return paths, yielding
   `q` distinct mixed cycles through `a` whose return portions are pairwise
   edge-disjoint.
2. **Small return cut.** There is an edge set
   \[
   \boxed{F_a\subseteq E(D-a),\qquad |F_a|<q}
   \]
   meeting every mixed cycle containing `a`.

### Proof

The equality is the directed edge form of Menger's theorem applied to the
ordered pair `(w,u)` in `D-a`. The two alternatives are the cases
`\nu(a)\ge q` and `\tau(a)<q`. By CMR478, a return-path cut meets exactly the
cycles containing `a`. ∎

The theta fan is structural rather than immediately simultaneous: all cycles
share `a` and may also share contraction vertices. The cut branch is a finite
exchange bottleneck.

## 4. Cut concentration gives a second common edge

### Corollary CMR480 — PROVED

Suppose `a` belongs to `L` distinct mixed cycles and a return cut `F_a` of size
`f` meets every one of them. Then `f\ge1`, and some edge `b\in F_a` belongs to
at least

\[
\boxed{
\left\lceil\frac{L}{f}\right\rceil
}
\]

of those cycles.

In particular, if the small-cut branch of CMR479 holds with `q\ge2`, some
second contraction edge occurs together with `a` in at least

\[
\boxed{
\left\lceil\frac{L}{q-1}\right\rceil
}
\]

distinct mixed cycles.

### Proof

Because `a` is cyclic, at least one return path exists, so a return cut cannot be
empty. Assign each of the `L` return paths to one cut edge it uses and apply the
pigeonhole principle. The second statement uses `f\le q-1`. ∎

Thus failure of an edge-disjoint theta fan creates a two-edge exchange
bottleneck with quantitatively increased multiplicity.

## 5. Combined concentration endpoint

### Corollary CMR481 — PROVED

Suppose one contraction vertex belongs to `\Delta>0` canonical witnesses. Let
`a` and `L_v` be supplied by CMR477. For every integer `q\ge2`, at least one of
the following holds.

1. **Boundary theta fan.** There are `q` mixed cycles through the same colour-
   boundary arc `a` whose return paths are pairwise edge-disjoint.
2. **Two-edge bottleneck.** A second contraction edge `b` occurs together with
   `a` in at least
   \[
   \boxed{
   \left\lceil\frac{L_v}{q-1}\right\rceil
   }
   \]
   distinct mixed cycles.

The boundary arc `a=i\to j` corresponds in the bipartite host to the same-level
source-switch edge

\[
\ell_i r_j,
\qquad
\beta(i)\ne\beta(j).
\]

Hence the first branch is a multi-route exchange fan around one actual source-
switch edge, while the second branch localizes the obstruction to two fixed
host edges.

### Proof

Apply CMR479 to the boundary arc supplied by CMR477. In its small-cut branch,
apply CMR480 to the `L_v` distinct cycles through `a`. The bipartite
interpretation is the definition of matching contraction and the colour-
boundary condition. ∎

## 6. Revised frontier

The concentration branch of CMR476 no longer ends at an anonymous high-
multiplicity vertex. It now yields one of two concrete structures.

- A colour-boundary source-switch edge supports many edge-disjoint return
  routes, forming a directed theta exchange fan.
- Two fixed contraction edges lie in many distinct mixed cycles, giving a
  narrow exchange bottleneck.

The next geometric step is to attach prefix, primitive-height, quotient, carry,
Hall, reserve, or envelope data to these fixed host edges and their return
routes. A large theta fan should provide many geometrically distinct repairs;
a repeated two-edge bottleneck should force concentration of the corresponding
line or carry signatures.

No simultaneous-flip claim is made for the theta fan, because its cycles share
the boundary edge. No all-`n` theorem is claimed. The incidence reduction,
cycle-path bijection, Menger equality, and cut pigeonhole are checked in
[`scripts/verify_prime_power_mixed_cycle_boundary_fan.py`](../scripts/verify_prime_power_mixed_cycle_boundary_fan.py).
