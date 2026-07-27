# Complete Hamilton flaw targeting and short finite reachability

The support-three successor rotation from `docs/303` targets every bad triple
with three distinct orbit owners, but the drift census in `docs/304` found
states whose defects have only two owners.  This chapter supplies the missing
support-one move and combines the two primitives.

The result is an exact flaw interface: every collinear triple in a signed
Hamilton state can be deleted by a move changing at most three signed
assignments while preserving Hamiltonicity, matching, pair-2-cycle-freeness,
and duplicate-orbit validity.  The natural raw potentials still have one-step
local minima, but exhaustive directed reachability through pair size seven
shows that all such minima escape within at most four flaw-targeted moves.

No asymptotic termination theorem is claimed.

## 1. One orbit contributes at most two points to a line

A signed pair assignment selects one complete four-cell quarter-turn orbit.

### Proposition PP3bjx -- PROVED

Every nondegenerate signed Hamilton orbit block is the vertex set of a square
centred at the centre of the board.  Consequently every Euclidean line contains
at most two cells from one orbit owner.

#### Proof

Let `R` be quarter-turn rotation about the board centre and let `q` be any cell
in a nondegenerate orbit.  The four selected cells are

```text
q, Rq, R^2q, R^3q.
```

After translating the board centre to the origin, write `q=(u,v)`.  The four
vectors are

```text
(u,v), (-v,u), (-u,-v), (v,-u),
```

which are the vertices of a square.  No three vertices of a nondegenerate
square are collinear.  Thus a line meets the orbit in at most two cells. ∎

Hamilton pair permutations have no self-loops, so every orbit block here is
nondegenerate.

### Corollary PP3bjy -- PROVED

Every selected collinear triple in a signed Hamilton state has exactly two or
three orbit owners.  In the two-owner case the owner multiplicities are `2+1`.

#### Proof

One owner is impossible by PP3bjx.  Three cells can use at most three owners.
If exactly two owners occur, one contributes two cells and the other one. ∎

## 2. Pure orientation flips repair every two-owner flaw

Fix a Hamilton pair edge `i -> j`.  Its two orientation values select the two
four-cell orbits

```text
O_0(i,j) and O_1(i,j).
```

### Proposition PP3bjz -- PROVED / SUPPORT-ONE REPAIR

For a nonloop pair edge, `O_0(i,j)` and `O_1(i,j)` are disjoint.  Toggling the
orientation bit at source `i` therefore removes the complete old orbit block,
inserts the complementary block, and preserves the Hamilton pair cycle and all
matching and duplicate-orbit constraints.

In particular, if a bad triple has two owners, flipping either owner deletes
that triple.

#### Proof

In pair coordinates, the two signs exchange the target bit attached to each
source bit.  Their four coordinate pairs are complementary and are disjoint
when the source and target pairs are distinct.  A Hamilton cycle has no fixed
pair edge, so this condition holds.

The pair permutation is unchanged, hence source and target matching and
Hamiltonicity are unchanged.  A Hamilton pair permutation has no pair 2-cycle,
so duplicate-orbit validity remains automatic.  Every cell of the old owner
orbit disappears after the flip.  A two-owner bad triple contains at least one
cell of either owner, so flipping either one deletes it. ∎

The move is an involution.  If the source is chosen uniformly, pure orientation
flips form the usual `m`-dimensional hypercube kernel on the sign vector and are
symmetric under the uniform signed Hamilton measure.

## 3. A complete combined flaw kernel

Use the following rule for a present bad triple `T`.

```text
Two owners:   flip either owner orientation.
Three owners: rotate the three pair successors and choose fresh signs.
```

### Theorem PP3bka -- PROVED / COMPLETE FLAW TARGETING

Every bad triple in a signed Hamilton state has at least one legal combined
flaw-targeted move that deletes it.  Every such move changes at most three
signed assignments and remains inside the signed Hamilton state space.

#### Proof

PP3bjy gives the two possible owner counts.  PP3bjz handles the two-owner case
with support one.  PP3bjk handles the three-owner case with support three.
Both moves preserve Hamiltonicity and the exact signed-cover constraints. ∎

### Proposition PP3bkb -- PROVED

The unconditioned union of all single-owner orientation flips and all signed
three-edge successor rotations is a connected symmetric regular graph on the
signed Hamilton states.  Its degree is

```text
m + 8 C(m,3).
```

The associated uniform-choice kernel is reversible for the uniform signed
Hamilton measure.

#### Proof

There are `m` distinct sign-flip neighbours with unchanged pair permutation.
PP3bjj gives `8 C(m,3)` distinct rotation neighbours with changed pair
permutation, so the two neighbour sets are disjoint.  Every move is paired with
an inverse of the same type and probability.

For connectivity, PP3bji connects all Hamilton pair cycles using three-edge
rotations.  For a fixed cycle, single-bit flips connect all orientation vectors.
Thus the union graph is connected and symmetric. ∎

As before, defect-dependent targeting destroys symmetry and must be analysed as
a flaw walk rather than as the unconditioned reversible chain.

## 4. Exact finite flaw-targeted reachability

### Proposition PP3bkc -- VERIFIED FINITELY / LOOK-AHEAD FRONTIER

For every signed Hamilton state with `4<=m<=7`, form the directed graph whose
outgoing edges are all combined moves targeted at a currently present bad
triple.  Then every state reaches a state of globally minimum total collinear
triple count.

The exact results are:

| `m` | states | global minimum | minimum states | directed edges | maximum distance |
|---:|---:|---:|---:|---:|---:|
| 4 | 96 | 0 | 16 | 864 | 2 |
| 5 | 768 | 0 | 16 | 15,632 | 3 |
| 6 | 7,680 | 4 | 84 | 252,896 | 3 |
| 7 | 92,160 | 0 | 36 | 4,427,088 | 4 |

No defective state has zero legal combined moves.  The former support-three
targetability gaps are repaired by orientation flips: there are `32`, `32`,
and `56` defective states with no three-owner flaw at `m=5,6,7`, respectively.

The nonminimal one-step local minima and their distances to the global minimum
are:

| `m` | local minima | distance two | distance three | distance four |
|---:|---:|---:|---:|---:|
| 4 | 36 | 36 | 0 | 0 |
| 5 | 140 | 96 | 44 | 0 |
| 6 | 764 | 736 | 28 | 0 |
| 7 | 6,676 | 1,344 | 5,060 | 272 |

At `m=7`, an additional forward search computes the shortest horizon to any
strictly lower triple count:

```text
horizon 1: 85,448 states,
horizon 2:  5,936 states,
horizon 3:    692 states,
horizon 4:     48 states.
```

Thus every nonminimum state through `m=7` has a strictly descending path of
length at most four, even though one-step descent fails on thousands of states.

#### Verification

For `m=4,5,6`, run

```bash
python scripts/check_hamilton_combined_flaw_reachability.py \
  experiments/hamilton-combined-flaw-reachability-audit.json
```

For the larger `m=7` graph, run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m7.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m7
/tmp/check_hamilton_combined_flaw_reachability_m7
```

The compiled checker reconstructs all `92,160` signed Hamilton states, all
`2,563,584` bad-triple occurrences, and all `4,427,088` directed targeted
edges.  It builds forward and reverse CSR graphs and verifies both the distance
to the global minimum and the strict-descent horizon. ∎

For `m=4,5,7`, the global minimum is zero, so every signed Hamilton state reaches
a valid no-three state under some targeted path.  For `m=6`, the Hamilton
subfamily contains no valid state, and the conclusion is only reachability of
the four-triple optimum.

## 5. Revised constructive frontier

The targetability obstruction is closed: every flaw has a support-one or
support-three deletion move.  The remaining obstruction is scheduling and
collateral control.

The finite horizon-four result suggests three concrete next routes:

1. define a bounded-look-ahead Lyapunov function rather than a one-step defect
   count;
2. encode short escaping paths as witness atoms and prove a charge bound;
3. add geometric weights predicting collateral lines before selecting a move.

The observed horizon grows from two to four across `m=4,...,7`, so the data do
not support claiming a uniform constant bound.  The exact finite reachability
does not imply an asymptotic termination theorem.  The asymptotic seed theorem
and the no-three-in-line conjecture remain open.
