# Multi-rectangle trade banks

One alternating rectangle can repair a matching-patch near miss.  This chapter
records the exact Boolean structure of several protected rectangle switches and
gives a lossless finite search for two sequential switches.

## 1. Independent alternating rectangles

Let `T subseteq [n]^2` have exactly two points in every row and column.  For
`i=1,...,r`, let `R_i` be an axis-parallel rectangle whose four corners are
disjoint from the four corners of every other `R_j`.  Assume that exactly one
diagonal of `R_i` is selected in `T`.  Label that diagonal `D_i^0` and the other
diagonal `D_i^1`.

For an assignment

\[
 \xi=(\xi_1,\ldots,\xi_r)\in\{0,1\}^r,
\]

put

\[
 T_\xi
 =
 \left(T\setminus\bigcup_i D_i^0\right)
 \cup
 \bigcup_i D_i^{\xi_i}.
\]

### Proposition PP3ba -- PROVED

Every state `T_xi` has the same cardinality as `T` and exactly two selected
points in every row and column.

#### Proof

Toggling one rectangle removes one corner and adds one corner in each of its two
rows and columns.  Hence it preserves every row and column sum.  The corner sets
are disjoint, so all toggles are simultaneously well defined.  Composing the
individual line-sum-preserving switches proves the claim. ∎

The rectangles may share rows or columns; only their corner cells must be
disjoint.

## 2. Exact clause representation

A corner of `R_i` is selected under exactly one value of `xi_i`.  Every selected
point outside all rectangles is fixed.  Let `U` consist of the fixed selected
points and all rectangle corners.

For every collinear triple `tau subseteq U`, inspect the orientation requirements
of its three points.

- If `tau` contains two corners of one rectangle that require opposite values,
  then `tau` can never be selected and contributes no constraint.
- Otherwise `tau` is selected precisely when a conjunction of at most three
  distinct variable assignments holds.
- Negating that conjunction gives one clause of size at most three.
- A triple of fixed selected points gives the empty clause and makes the bank
  impossible.

Let `Phi(T,{R_i})` be the conjunction of all distinct clauses obtained this way.

### Theorem PP3bb -- PROVED

The following are equivalent.

1. Some rectangle orientation assignment `xi` makes `T_xi` no-three-in-line.
2. The formula `Phi(T,{R_i})` is satisfiable.

Moreover, `Phi` is a 3-CNF formula.  If no potentially selected collinear triple
meets three distinct rectangle variables, then `Phi` is a 2-CNF formula and the
repair problem is exactly 2-SAT.

#### Proof

By PP3ba every assignment preserves saturation.  A triple can occur in `T_xi`
exactly when all its fixed points are present and every rectangle corner in the
triple has its required orientation.  The clause attached to the triple is the
negation of that exact conjunction.  Therefore an assignment satisfies every
clause if and only if it selects no collinear triple.  A triple has three points,
so it can involve at most three distinct rectangle variables. ∎

This is an exact selection theorem rather than a first-moment condition.  Dense
certificate families are allowed when their forbidden orientations are
logically compatible.

## 3. A lossless filter for two sequential switches

Let `T_0` be any saturated state, let the first switch remove selected points
`a,b`, and suppose a second switch produces a no-three state `T_2`.

### Proposition PP3bc -- PROVED

The triples of `T_0` not containing `a` or `b` have a transversal of size at most
two among the original points of `T_0`.

#### Proof

A triple of `T_0` not containing `a` or `b` is unchanged after the first switch:
the first switch only removes `a,b`, and adding points cannot destroy an existing
triple.  Since `T_2` is triple-free, the second switch must remove at least one
point from every such surviving original triple.  It removes only two selected
points.  Any point introduced by the first switch belongs to no original triple,
so the original points among the second removed pair form a transversal of size
at most two. ∎

Consequently, a complete two-switch search may discard a first switch whenever
the untouched original triples have transversal number greater than two.  This
filter is necessary and therefore cannot remove a valid two-switch repair.

## 4. Exact finite classification on the stored width-two corpus

The script

```bash
python scripts/search_width_two_two_rectangle_repairs.py \
  certificates/prime-patching-small.json
```

starts from every distinct internally clean width-two matching-patch state.  It
uses PP3bc to filter first switches, enumerates every exact one-switch repair of
the intermediate state, rejects the trivial undo sequence, and independently
verifies every final state with integer determinants.

### Proposition PP3bd -- PROVED BY EXHAUSTIVE FINITE CHECK

For the stored source certificates:

| Source side | Initial states | Promising first switches | Two-switch sequences | Distinct two-switch finals | Additional finals beyond one switch |
|---:|---:|---:|---:|---:|---:|
| 4 | 20 | 804 | 63 | 10 | 9 |
| 5 | 149 | 7,365 | 39 | 8 | 7 |
| 6 | 969 | 41,599 | 83 | 15 | 14 |
| 7 | 3,686 | 51,906 | 0 | 0 | 0 |
| 8 | 9,813 | 49,324 | 0 | 0 | 0 |
| 9 | 22,555 | 13,308 | 0 | 0 | 0 |
| 10 | 43,539 | 21,928 | 0 | 0 | 0 |

Thus two switches substantially enlarge the finite target families at source
sides four through six, but no two-switch repair exists for any stored source
from side seven through ten.

The zero results are exhaustive for two sequential alternating rectangle
switches, not merely for disjoint or simultaneously exposed rectangles.

## 5. Revised asymptotic target

The one- and two-switch experiments show both sides of the patch-plus-trade
route.

- A small protected trade bank can strictly enlarge the set of usable patches.
- Unstructured post hoc rectangle depth two still fails on the larger stored
  seeds.

A scalable theorem should therefore install the rectangle bank during seed
preparation.  PP3bb gives an exact endpoint: arrange the protected rectangles so
that every patch certificate induces a bounded-rank clause and the resulting
CNF is satisfiable.  Particularly attractive sufficient targets are:

1. a rank-two bank with a satisfiable implication graph;
2. a sparse rank-three formula with a local-lemma or bounded-occurrence SAT
   certificate;
3. rectangles whose removed diagonals hit all high-load external certificates
   while their added diagonals have controlled secant shadow;
4. a joint parabolic-rung and rectangle-variable bank in which cross-rung triples
   also have bounded clause rank and codegree.
