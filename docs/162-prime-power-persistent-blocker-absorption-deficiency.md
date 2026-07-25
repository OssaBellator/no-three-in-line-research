# A persistent unavailable cell is absorbable, meets the paid-line trace, or forces a two-endpoint absorption deficiency

CMR517--CMR521 reduce all unpriced temporal reuse to one edge which stays
continuously unavailable through many episodes.  The adaptive forbidden
matching from CMR507 can be chosen with knowledge of that persistent edge.

If the edge belongs to some maximum unavailable matching compatible with the
paid-line trace, absorb it into the forbidden matching and remove it from the
restoration inventory.  Otherwise its two endpoints are both saturated by
distinct unavailable edges in every maximum absorption matching.  Thus a
persistent blocker becomes a row-column cross rather than an arbitrary cell.

## 1. Maximum-matching allowed-edge criterion

Let `J` be a finite bipartite graph, let

\[
\nu=\nu(J),
\]

and fix an edge

\[
e=uv\in E(J).
\]

### Theorem CMR522 — PROVED

The edge `e` belongs to a maximum matching of `J` if and only if

\[
\boxed{
1+\nu(J-u-v)=\nu(J).
}
\]

### Proof

A matching containing `e` is exactly `e` together with a matching of the graph
obtained by deleting its two endpoints.  Maximizing the latter part gives the
displayed criterion. ∎

Call such an edge **maximum-allowed**.

## 2. Exact two-endpoint deficiency

### Theorem CMR523 — PROVED

If `e` is not maximum-allowed, then

\[
\boxed{
\nu(J-u-v)=\nu(J)-2.
}
\]

Consequently every maximum matching of `J`

1. matches `u`;
2. matches `v`;
3. uses two distinct matching edges at those endpoints;
4. does not use `e`.

### Proof

Deleting two vertices can destroy at most two edges of a maximum matching, so

\[
\nu(J-u-v)\ge\nu(J)-2.
\]

If `e` is not maximum-allowed, CMR522 gives

\[
1+\nu(J-u-v)<\nu(J),
\]

hence `\nu(J-u-v)\le\nu(J)-2`.  Equality follows.

If a maximum matching left `u` unmatched, deleting `u` and `v` would remove at
most the one edge incident with `v`, leaving a matching of size at least
`\nu(J)-1`, contradiction.  The same applies to `v`.  The two matching edges
are distinct because `e` itself is excluded. ∎

Thus a nonabsorbable edge consumes two separate slots of every maximum
unavailable matching.

## 3. Persistent-aware adaptive forbidden matching

Return to one line-clean cylinder.  Let `Q_L` be the residual paid-line trace,
let `B_L^0` be the unavailable residual graph before choosing `F_L`, and let
`J_L` be the unavailable graph after deleting the vertices of `Q_L`, as in
CMR507.

Fix one persistent unavailable edge

\[
e=uv\in B_L^0.
\]

### Corollary CMR524 — PROVED

Exactly one of the following structural actions is available.

1. **Paid-line trace contact.** The edge `e` shares a source or target endpoint
   with an edge of `Q_L`.
2. **Persistent-edge absorption.** The edge lies in `J_L` and is maximum-allowed.
   Choose a maximum matching `S_L` containing `e`, extend `Q_L\cup S_L` to
   `F_L`, and the line-clean cylinder avoids `e` at zero restoration cost.
3. **Two-endpoint absorption deficiency.** The edge lies in `J_L` but is not
   maximum-allowed.  Every maximum absorption matching contains two distinct
   unavailable edges
   \[
   \boxed{e_u=uv',\qquad e_v=u'v}
   \]
   through the two endpoints of `e`.

### Proof

If `e` is not vertex-disjoint from `Q_L`, use the first branch.  Otherwise it is
an edge of `J_L`.  Apply CMR522.  In the allowed branch choose a maximum matching
containing it and use CMR507.  In the forbidden branch apply CMR523 to every
maximum absorption matching. ∎

The third branch gives a compatible paid pair: `u\ne u'` and `v\ne v'`.

## 4. Repeated persistent-blocker episodes

Suppose the same edge `e=uv` remains continuously unavailable through `r`
line-clean episodes.  In every episode choose the adaptive forbidden matching
with the priority rule of CMR524: absorb `e` whenever a maximum absorption
matching containing it exists.

### Theorem CMR525 — PROVED

If `e` is not absorbed, then every occurrence is assigned to one of two classes:

1. a paid-line trace contact at row `u` or column `v`;
2. a two-edge absorption pair `e_u,e_v` contained in the row-column cross
   \[
   \boxed{
   \{uw:w\ne v\}
   \cup
   \{zv:z\ne u\}.
   }
   \]

At least `\lceil r/2\rceil` occurrences belong to one class.

If `R` occurrences are in the absorption-pair class, then for every integer
`\lambda\ge2`, either

1. one partner edge occurs in at least `\lambda` of the chosen pairs; or
2. the union of partner edges has size at least
   \[
   \boxed{
   \frac{2R}{\lambda-1}.
   }
   \]

In the second branch those distinct cross edges carry exact labelled full-token
incidence at least

\[
\boxed{
(p+1)(h-1)
\frac{2R}{\lambda-1}
}
\]

for parent side `t=p^h`.

### Proof

CMR524 gives the two classes after the absorption action is excluded.
Pigeonhole gives the first count.  Every deficiency occurrence supplies two
distinct partner edges.  If no partner edge occurs `\lambda` times, each appears
in at most `\lambda-1` occurrences; double-count the `2R` partner incidences.
The token identity is CMR413. ∎

Thus persistent absorption deficiency produces a repeated or dispersed
unavailable cross centered at the persistent cell.

## 5. Rooted-arm trace witnesses

For the rooted secant-star bank of CMR495, all paid lines pass through the fixed
root cell `a` and are distinct.

### Corollary CMR526 — PROVED

Suppose a persistent edge `e=uv` is not absorbed in `R` distinct rooted-arm
cylinders and all `R` occurrences are paid-line trace contacts.  Then those
cylinders supply `R` distinct residual line cells in the union of row `u` and
column `v`.

### Proof

For each paid line choose its row-`u` trace cell when one exists, and otherwise
its column-`v` trace cell.  The chosen cell is not `e`, because an unavailable
paid-line cell belongs to `Q_L\subseteq F_L` and is therefore excluded from the
allowed inventory.

Two distinct rooted lines through `a` cannot have the same chosen row witness:
the unique real line through `a` and that witness would make them equal.  The
same holds for column witnesses.  A row witness cannot equal a column witness
unless it is `e`, which was excluded.  Hence all chosen witnesses are distinct.
∎

The rooted trace branch therefore also gives a distinct row-column cross
inventory, not repeated copies of one witness.

## 6. Revised frontier

After persistent-aware adaptation, one continuously unavailable cell reaches one
of the following endpoints.

- It is absorbed for free into the forbidden matching.
- It repeatedly meets the paid-line trace, giving row/column incidence geometry.
- It forces two distinct absorbed partner edges in every episode, producing a
  repeated or dispersed unavailable cross.

The remaining geometric theorem is now a cross-classification problem: convert
a large unavailable row-column cross into a Hall wall, heavy full-prefix token,
primitive-height/quotient/carry concentration, protected-reserve depletion, or
envelope expansion.  The heavy-star half is already covered by CMR512--CMR516;
what remains is to combine simultaneous row and column arms and account for
persistent trace witnesses across envelope ancestry.

No all-`n` theorem is claimed.  Maximum-allowed criteria, exact two-endpoint
deficiency, adaptive trichotomy, and cross-incidence arithmetic are checked in
[`scripts/verify_prime_power_persistent_blocker.py`](../scripts/verify_prime_power_persistent_blocker.py).
