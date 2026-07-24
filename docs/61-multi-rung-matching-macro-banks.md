# Multi-rung matching macro-banks

The threshold in PP3cz suggests reducing the number of independent local
variables.  This chapter records the exact equal-margin state space obtained by
bundling many width-two intervals into one matching pool.  It also records an
important limitation: formal grouping alone does not reduce the interval-level
cross-support potential.

## 1. The complete macro bank

Let `E` be an `R`-edge source matching pool and let

\[
 I_1,\ldots,I_h
\]

be disjoint width-two new-coordinate intervals.  A macro state chooses ordered,
pairwise disjoint four-edge sets

\[
 D_1,\ldots,D_h\subseteq E
\]

and one of the 36 width-two degree geometries on each `D_j`.  Edges outside
`D_1 union ... union D_h` remain as source points.

### Proposition PP3da -- PROVED

Every macro state has the same row and column incidence vectors.  The number of
states in the complete macro bank is

\[
 \boxed{
 \frac{(R)_{4h}}{(4!)^h}\,36^h.
 }
\]

Each old coordinate incident with `E` has local incidence one, and every new row
and column in the `h` intervals has incidence two.

#### Proof

For every source edge, either the edge remains or exactly one movement and one
refill point restore its old column and row.  Every interval geometry contributes
two points to each of its two new rows and columns.  Hence all margins are state
independent.

Choose an ordered family of disjoint four-subsets in
`(R)_{4h}/(4!)^h` ways and then choose one of 36 geometries independently on
each interval. ∎

When `R=4h`, every pool edge is deleted in every state.  This removes all
retained-pool certificates while preserving one unit of incidence on every old
pool coordinate.

## 2. Exact uniform spread

Choose a macro state uniformly from the complete bank.

### Proposition PP3db -- PROVED

For a specified interval `I_i`:

1. a source edge belongs to `D_i` with probability `4/R`;
2. a prescribed movement or refill cell has probability at most

\[
 \frac2R;
\]

3. a prescribed same-edge movement/refill pair has probability at most

\[
 \frac1R;
\]

4. any other prescribed pair inside `I_i` has probability at most

\[
 \frac4{(R)_2}.
\]

For distinct intervals `I_i,I_j,I_k`:

5. prescribed cells in `I_i,I_j` have joint probability at most

\[
 \frac4{(R)_2};
\]

6. a prescribed same-edge pair in `I_i` and a prescribed cell in `I_j` have
   joint probability at most

\[
 \frac2{(R)_2};
\]

7. an ordinary prescribed pair in `I_i` and a prescribed cell in `I_j` have
   joint probability at most

\[
 \frac8{(R)_3};
\]

8. prescribed cells in `I_i,I_j,I_k` have joint probability at most

\[
 \frac8{(R)_3}.
\]

#### Proof

A specified edge is assigned to a specified interval with probability `4/R`.
Conditional on assignment, its movement row and refill column are independent
uniform binary choices.  This gives the cell and same-edge formulas.

Two specified edges are assigned to one specified interval with probability
`(4)_2/(R)_2`; the ordered pair partition realizes any prescribed feasible pair
with conditional probability at most `1/3`, giving `4/(R)_2`.

For two distinct intervals, two specified edges are assigned one to each with
probability `16/(R)_2`; their prescribed binary labels cost `1/4`.

A same-edge pair plus an external cell uses two controlling edges.  Assignment
cost is `16/(R)_2`, while the orientation cost is `1/4*1/2`.

An ordinary pair plus a cell uses three controlling edges.  Assignment cost is
`(4)_2*4/(R)_3=48/(R)_3`; the orientation cost is at most `1/3*1/2`.

Finally, three specified edges assigned to three intervals cost `64/(R)_3`, and
three prescribed binary labels cost `1/8`. ∎

Any clean subdomain of density `delta` preserves these bounds with an additional
factor `1/delta`.

## 3. Prime-gap macro scaling

Take

\[
 M=m^{0.05}
\]

macro pools and total extension width

\[
 T=m^{0.525}.
\]

If every macro pool installs

\[
 h=\frac{T}{2M}=\Theta(m^{0.475})
\]

width-two micro-rungs and uses `R=4h` source edges, then the total source-edge
budget is

\[
 MR=2T=o(m).
\]

Thus matching availability is not an obstacle: PP3bs supplies enough disjoint
source edges.  The complete state count of one macro variable is
superpolynomially large, and its specified-cell marginal is `Theta(1/R)`.

## 4. Grouping does not by itself compress support

### Proposition PP3dc -- PROVED

Let `J=Mh` be the total number of width-two intervals in a collection of complete
macro banks.  Before imposing an internally clean support restriction, the
PP3cx--PP3cy cross-pattern calculation depends on `J`, not merely on the formal
number `M` of macro variables.

In particular, random assignment of source edges to the macro pools gives the
same interval-level three-cell potential order

\[
 O(J^3/m)
\]

that would arise if the `J` intervals were treated as separate variables.

#### Proof

Every macro state still exposes one candidate cross support for each of its `h`
intervals.  Proposition PP3db gives the same fixed-rank cylinder probabilities
for specified interval cells and pairs as direct sampling without replacement
from the pool.  The PP3cx support count is performed interval by interval.
Summing it over all interval pairs and triples therefore introduces `J^2` and
`J^3`, regardless of which intervals share a variable.  Correlation inside one
macro variable does not remove a candidate pattern unless the state domain is
explicitly pruned to forbid it. ∎

This is a limitation of the complete product macro bank, not an impossibility
theorem for macro states.

## 5. Correct macro-state target

A useful large-width variable must have **support compression** in addition to
large state entropy.  It should satisfy at least one of:

1. every state is internally no-three across all `h` installed micro-rungs, and
   the union of candidate supports has only `O(R^2)` relevant cross incidences;
2. the state domain correlates interval choices so that three-interval bad boxes
   have probability much smaller than the complete-bank `Theta(R^-3)` cylinder
   scale;
3. a deterministic algebraic or monotone geometry replaces the `h` independent
   width-two crosses by a bounded number of internally clean components;
4. protected trades remove the interval-level transversal cores before the
   macro state is exposed.

Square-root parabolic rungs already have this compressed-component property and
need only `m^0.05` variables.  The open matching-first problem is to obtain a
comparable compressed macro geometry adapted to arbitrary or prepared source
matching endpoints.