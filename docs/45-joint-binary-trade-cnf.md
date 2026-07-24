# Joint binary rung-and-trade CNF

The matching-reservoir cycle theorem and the rectangle-bank theorem both turn
geometric choices into Boolean variables.  This chapter gives the common exact
interface, including cross-rung triples.

## 1. Binary local trades

Fix a set `F subseteq [n]^2`.  For each `i=1,...,r`, let

\[
 A_i^0,A_i^1\subseteq[n]^2
\]

be two local states.  Assume:

1. the support `A_i^0 union A_i^1` is disjoint from `F`;
2. supports belonging to distinct variables are disjoint;
3. `A_i^0` and `A_i^1` have the same row-incidence vector and the same
   column-incidence vector.

For `xi in {0,1}^r`, put

\[
 T_\xi=F\cup\bigcup_{i=1}^r A_i^{\xi_i}.
\]

The local states may overlap within one variable.  A point belonging to both
`A_i^0` and `A_i^1` is selected independently of `xi_i`.

### Proposition PP3be -- PROVED

If one state `T_xi` has exactly two points in every row and column, then every
state has exactly two points in every row and column.

#### Proof

Changing `xi_i` replaces `A_i^0` by `A_i^1` or conversely.  The two local states
have identical row and column incidence vectors, so this change preserves every
line sum.  Applying the changes one variable at a time proves that all states
have the same row and column sums. ∎

This includes:

- one protected alternating rectangle, whose two states are its diagonals;
- one matching-reservoir cycle, whose states are its alternating edge classes;
- a prepared parabolic rung with two admissible local patch states;
- any finite tomographic trade with two equal-margin realizations.

## 2. Selection sets of candidate points

For a point `z` in the support of variable `i`, define

\[
 \sigma_i(z)=\{\varepsilon\in\{0,1\}:z\in A_i^\varepsilon\}.
\]

Thus `sigma_i(z)` is one of `{0}`, `{1}`, or `{0,1}`.  For a triple `tau` of
candidate points and a variable `i`, intersect the selection sets of all points
of `tau` controlled by `i`:

\[
 \sigma_i(\tau)=
 \bigcap_{z\in\tau\cap(A_i^0\cup A_i^1)}\sigma_i(z).
\]

If this intersection is empty, the triple can never be selected.  If it is a
singleton, selecting the triple requires one value of `xi_i`.  If it is
`{0,1}`, that variable places no restriction.

For every collinear triple not ruled out by an empty intersection, negate the
conjunction of its singleton requirements.  Let `Psi` be the conjunction of the
resulting distinct clauses.  A collinear triple contained entirely in `F` gives
the empty clause.

### Theorem PP3bf -- PROVED

The following are equivalent.

1. Some assignment `xi` makes `T_xi` no-three-in-line.
2. The formula `Psi` is satisfiable.

The formula has clause rank at most three.  If every potentially selected
collinear triple has singleton requirements on at most two variables, then
`Psi` is a 2-CNF formula and exact selection reduces to 2-SAT.

#### Proof

By construction, a candidate triple is present in `T_xi` exactly when all its
fixed points lie in `F` and every variable controlling one of its points takes a
value in the corresponding intersection `sigma_i(tau)`.  Empty intersections
make the triple impossible.  Nonempty singleton intersections give the exact
required assignments, while `{0,1}` contributes no condition.  The clause added
to `Psi` is precisely the negation of the conjunction that selects the triple.
Therefore an assignment satisfies every clause if and only if it selects no
collinear triple.

A triple contains three points and the variable supports are disjoint, so it can
have singleton requirements on at most three variables. ∎

## 3. Joint parabolic-rung and rectangle banks

Suppose a prepared seed supplies several disjoint parabolic matching reservoirs.
For each rung retain two admissible patch/deletion states as one binary variable.
Add protected alternating rectangles, reservoir-cycle parities, or tomographic
trades as further binary variables.  Equal incidence vectors guarantee
saturation by PP3be.  The complete geometry, including:

- retained-core triples;
- triples internal to one local state;
- triples between two rungs;
- triples meeting three different rungs;
- patch-versus-rectangle collateral;

is represented exactly by `Psi`.

### Corollary PP3bg -- PROVED

If the prepared joint bank has no empty clause and every potential triple depends
nontrivially on at most two binary variables, then the existence of a complete
patch is decidable by one implication-graph 2-SAT instance.

This is the strongest exact formulation currently available for cross-rung
compatibility.  It replaces the requirement that every pair of rungs be
geometrically independent by the weaker requirement that all their forbidden
orientations be logically compatible.

## 4. Remaining asymptotic task

The multi-rung coordinate budget needs only about `m^0.05` square-root-scale
rungs for the published prime-gap exponent.  PP3bf shows what a preparation
theorem may target:

1. install two equal-margin states for each rung or trade variable;
2. ensure every external or cross-rung triple has bounded variable rank;
3. prove the resulting CNF satisfiable, preferably by arranging rank two and a
   noncontradictory implication graph;
4. alternatively, prove bounded occurrence or another structural property for
   the rank-three clauses.

The theorem does not prove that such a prepared seed exists.  It closes the
logical selection interface once the binary local states and their geometric
certificate formula have been constructed.
