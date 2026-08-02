# Trajectory antichains: single-level reset or depth excess

PX294--PX299 extract an antichain child `Q` from every trajectory-saturated core
which has no historical back-edge reset. The allowed digraph inside `Q` is
empty, while all but at most `s Delta_0` of its off-diagonal cells are supplied
by historical partial matchings.

A full historical layer is not required for a reset. Any directed cycle inside
one releasable historical layer is already a principal cycle cover on its
vertices. Therefore a core with no one-level reset must decompose its dense
historical obstruction into directed path forests. Their maximum size gives a
sharp ancestor-depth lower bound.

## 1. Releasable historical layers

Retain the decomposition

\[
F=D\cup F_0\cup H_1\cup\cdots\cup H_d
\]

from PX294. Put

\[
\widehat H_j=H_j\setminus F_0.
\]

The sets `widehat H_j` are pairwise edge-disjoint, and deleting the ancestor
constraint `H_j` releases every edge of `widehat H_j`.

Let `Q` be an antichain child of order `s` from PX296. Thus `A[Q]` has no arcs.

### Theorem PX311 -- PROVED

If the directed partial permutation `widehat H_j[Q]` contains a directed cycle,
then releasing the single ancestor constraint `H_j` gives an executable
principal cycle trade on `Q`.

### Proof

Every edge of the directed cycle is absent only because of `H_j`: it is not in
`F_0`, and historical edge-disjointness excludes every other `H_i`. Removing
`H_j` therefore makes the whole cycle allowed. Its vertices have one incoming
and one outgoing cycle edge, so it is a principal cyclic rematching. \(\square\)

PX299 is the special case where `widehat H_j[Q]` is a fixed-point-free perfect
matching.

## 2. Cycle-free layers are path forests

### Theorem PX312 -- PROVED

If `widehat H_j[Q]` contains no directed cycle, then it is a vertex-disjoint
union of directed paths and isolated vertices. In particular,

\[
\boxed{|\widehat H_j\cap(Q\times Q)|\le s-1.}
\]

### Proof

A partial matching has indegree and outdegree at most one at every label. Every
component of its directed graph is therefore a directed path or a directed
cycle, with isolated vertices allowed. Under the cycle-free hypothesis only
paths remain. A path forest on `s` vertices has at most `s-1` edges. \(\square\)

## 3. Sharp depth-or-reset inequality

### Theorem PX313 -- PROVED

At least one of the following holds for the antichain child `Q`.

1. Some single ancestor level gives a principal reset by PX311.
2. The ancestor depth satisfies

   \[
   \boxed{
   d\ge
   \left\lceil
   \frac{s(s-1-\Delta_0)}{s-1}
   \right\rceil,
   }
   \]

   with the numerator replaced by zero when `s-1-Delta_0<0`.

### Proof

If item 1 fails, PX312 bounds every releasable historical layer inside
`Q times Q` by `s-1` edges. PX297 gives at least

\[
s(s-1-\Delta_0)
\]

releasable historical cells in total. Hence

\[
d(s-1)\ge s(s-1-\Delta_0),
\]

which is the displayed bound. \(\square\)

Equivalently, whenever

\[
d<\frac{s(s-1-\Delta_0)}{s-1},
\]

a one-history principal reset is forced.

### Corollary PX314 -- PROVED

In the base-free case `Delta_0=0`, every antichain child of order `s` either has
a one-level reset or satisfies

\[
\boxed{d\ge s.}
\]

In particular, if only `s-1` ancestor matchings are available, some level is a
fixed-point-free perfect matching on `Q` and PX299 resets every endpoint of the
child.

### Proof

PX313 gives `d>=s` in the no-reset case. If `d=s-1`, the `s(s-1)` off-diagonal
cells of `Q times Q` are distributed among `s-1` partial matchings of size at
most `s`. Every level must therefore have size `s`; each is a fixed-point-free
permutation and PX299 applies. \(\square\)

## 4. Updated terminal interface

A trajectory-saturated core now has the following finite hierarchy.

1. An allowed principal cycle gives PX287.
2. A historical back edge gives PX294.
3. A cyclic single historical layer on the antichain child gives PX311.
4. Otherwise the child is internally forbidden and requires the explicit depth
   excess of PX313.

Thus a genuinely frozen terminal certificate must exhibit both a sparse
reachability poset and a long path-forest decomposition of a dense historical
antichain. The next exact census can enumerate these path-forest templates,
rather than arbitrary forbidden graphs.

## 5. Verification

Run

```bash
python scripts/verify_product_trajectory_depth_or_reset.py
```

The verifier exhausts partial permutations through order seven, checks the
cycle-or-path-forest decomposition and size bound, and verifies the integer
threshold in PX313--PX314.
