# Base-tournament census for the residual trajectory core

PX315--PX318 show that an antichain child with no reset using at most two
historical layers has order at most `2Delta_0+1`.  The proof selects at least
one base-forbidden orientation from every unordered label pair.

Those selected orientations form a tournament.  The row and column degree
bounds on the base graph become simultaneous outdegree and indegree bounds.
At the sharp order the tournament is forced to be regular, giving a small
canonical obstruction family.

## 1. Tournament orientation cover

Let `Q` be a no-two-history-reset antichain child of order `s`.

### Theorem PX327 -- PROVED

There is a tournament `T` on `Q` such that every arc of `T` belongs to
`F_0[Q]` and

\[
\boxed{
d_T^+(v)\le\Delta_0,
\qquad
d_T^-(v)\le\Delta_0
\quad(v\in Q).
}
\]

### Proof

PX316 says that for every unordered pair `{u,v}`, at least one of the two
orientations belongs to `F_0`.  Choose exactly one such orientation.  The
chosen arcs form a tournament.  Since it is a subgraph of `F_0`, its
outdegrees are bounded by the base row degree and its indegrees by the base
column degree. \(\square\)

This recovers `s<=2Delta_0+1` vertex by vertex, since

\[
s-1=d_T^+(v)+d_T^-(v)\le2\Delta_0.
\]

## 2. Sharp cores are regular tournaments

### Theorem PX328 -- PROVED

If

\[
\boxed{s=2\Delta_0+1,}
\]

then every tournament orientation cover `T` from PX327 is
`Delta_0`-regular:

\[
\boxed{
d_T^+(v)=d_T^-(v)=\Delta_0
\quad(v\in Q).
}
\]

Moreover `F_0[Q]` has no additional off-diagonal arcs.  Thus the residual base
graph on `Q` is exactly a regular tournament.

### Proof

At every vertex,

\[
d_T^+(v)+d_T^-(v)=s-1=2\Delta_0.
\]

Both summands are at most `Delta_0`, so both equal `Delta_0`.  The tournament
already uses `Delta_0` outgoing and `Delta_0` incoming base cells at every
vertex.  The maximum row and column degree bounds leave no capacity for an
additional opposite base arc. \(\square\)

Consequently equality in PX316 is highly rigid rather than an arbitrary
constant-size core.

## 3. The first sharp templates

### Corollary PX329 -- PROVED FINITE

Up to relabelling:

1. for `Delta_0=1`, the unique sharp residual core has `s=3` and base
   tournament the directed three-cycle;
2. for `Delta_0=2`, the unique sharp residual core has `s=5` and base
   tournament the cyclic regular tournament

   \[
   i\to i+1,\ i+2\pmod5.
   \]

Thus for base degree two, every trajectory antichain child either has a
one/two-history reset, has order at most four, or is the explicit cyclic
five-vertex base core.  The latter has only `5!=120` principal permutation
states.

### Proof

A regular tournament on three vertices is necessarily the directed triangle.
The finite verifier enumerates all tournaments on five vertices, filters for
indegree and outdegree two, and finds one isomorphism class represented by the
cyclic tournament. \(\square\)

For larger fixed `Delta_0`, PX327 reduces the exact terminal census to regular
and near-regular tournaments on at most `2Delta_0+1` vertices.

## 4. Verification

Run

```bash
python scripts/verify_product_base_tournament_core.py
```

The verifier exhausts all tournaments through order five, checks PX327--PX328,
computes canonical isomorphism representatives, and confirms the unique sharp
templates for base degrees one and two.
