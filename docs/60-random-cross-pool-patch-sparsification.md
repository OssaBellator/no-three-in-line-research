# Random cross-pool patch sparsification

After same-pool and source-containing triples have been removed, the remaining
obstruction is a triple using patch points from at least two pool variables.
Randomly distributing source matching edges among the pools gives an additional
factor that is absent from the deterministic support cap.  This chapter proves
that patch-only compatibility is automatic when the number of pool variables is
`o(m^(1/3))`.

## 1. Complete interval supports

Let `P` be a perfect matching of `m` source points.  For a width-two interval
`I={a,b}`, the complete candidate support over all edges of `P` is

\[
 U_I
 =
 ([m]\times\{a,b\})
 \cup
 (\{a,b\}\times[m]).
\]

It has `4m` points.  Supports belonging to disjoint intervals use distinct new
coordinates.

### Proposition PP3cx -- PROVED

For distinct intervals `I,J,L`:

1. the number of triples consisting of a same-edge movement/refill candidate
   pair from `I` and one candidate cell from `J` is at most `16m`;
2. the number consisting of an ordinary candidate pair controlled by two
   distinct source edges in `I` and one candidate cell from `J` is at most
   `32m(m-1)`;
3. the number consisting of one candidate cell from each of `I,J,L` is at most
   `64m^2`.

#### Proof

A line determined by candidate points from intervals other than `J` meets
`U_J` in at most four points, one on each of its two horizontal and two vertical
support lines.  It cannot coincide with one of those support lines because the
new-coordinate intervals are disjoint and the other coordinate of a candidate
cell lies in `[m]`.

There are four same-edge movement/refill pairs per source edge, hence `4m` such
pairs in `I`; multiply by four possible intersections with `U_J`.

For an unordered pair of distinct controlling edges there are at most sixteen
candidate-cell pairs, so there are at most
`16 binom(m,2)=8m(m-1)` ordinary pairs; multiply by four.

Finally, choose one point from `U_I` and one from `U_J`.  There are `16m^2`
ordered choices, and their line meets `U_L` in at most four points. ∎

The counts deliberately include patterns that no degree state can select; this
only enlarges the upper bounds.

## 2. A partition potential independent of local domains

Assume `m=Kr`.  Randomly equipartition `P` into ordered pools
`E_1,...,E_K` and assign distinct intervals `I_1,...,I_K`.

Fix a target lower bound `delta>0` for the clean-domain density that will later
be supplied on retained pools.  For any exposed equipartition, define
`X_delta` as follows:

- give every restricted same-edge-pair-plus-cell pattern weight
  `2/(delta^2 r^2)`;
- give every restricted ordinary-pair-plus-cell pattern weight
  `16/(delta^2 r^3)`;
- give every restricted one-cell-per-three-pools pattern weight
  `8/(delta^3 r^3)`;
- sum these weights over all ordered pool pairs and unordered pool triples.

This potential is defined whether or not a particular pool is locally good.  If
a collection of pools is later assigned independent clean domains of density at
least `delta`, its expected number of selected patch-only triples is at most the
restriction of `X_delta` to that collection.  Deleting pools can only decrease
the potential.

### Theorem PP3cy -- PROVED

The random equipartition satisfies

\[
 \boxed{
 \mathbb E X_\delta
 \le
 K(K-1)
 \left(
  \frac{32}{\delta^2(m-1)}
  +
  \frac{512}{\delta^2(m-2)}
 \right)
 +
 \binom K3
 \frac{512m}{\delta^3(m-1)(m-2)}.
 }
\]

#### Proof

Consider an ordered pair of distinct pools `i,j`.

A global same-edge-pair-plus-cell pattern from `I_i,I_j` is controlled by two
distinct source edges.  They land in the specified pools with probability

\[
 \frac{r^2}{m(m-1)}.
\]

Proposition PP3cx gives at most `16m` global patterns.  Multiplying by their
potential weight gives expected contribution

\[
 16m\frac{r^2}{m(m-1)}\frac2{\delta^2r^2}
 =
 \frac{32}{\delta^2(m-1)}.
\]

An ordinary-pair-plus-cell pattern is controlled by three distinct edges, two
assigned to pool `i` and one to pool `j`.  The assignment probability is

\[
 \frac{(r)_2r}{(m)_3}.
\]

Using the `32m(m-1)` support cap and its potential weight gives

\[
 32m(m-1)
 \frac{(r)_2r}{(m)_3}
 \frac{16}{\delta^2r^3}
 \le
 \frac{512}{\delta^2(m-2)}.
\]

For three distinct pools, a global one-cell-per-pool pattern is controlled by
three distinct edges and lands in the specified pools with probability
`r^3/(m)_3`.  Proposition PP3cx gives contribution

\[
 64m^2
 \frac{r^3}{(m)_3}
 \frac8{\delta^3r^3}
 =
 \frac{512m}{\delta^3(m-1)(m-2)}.
\]

Sum over ordered pool pairs and unordered pool triples. ∎

## 3. Composition with exceptional-pool deletion

Let `B` be any nonnegative count of pools that fail the desired same-pool or
source-clean preparation conditions.  Suppose a random equipartition satisfies

\[
 \mathbb E(B/K)=o(1)
\]

and every nonexceptional pool receives a clean domain of density at least a
fixed `delta>0`.  PP3cm and PP3cv give exactly this type of estimate under their
respective hypotheses.

### Corollary PP3cz -- PROVED

If

\[
 K=o(m^{1/3}),
\]

then there is an equipartition for which

\[
 B=o(K)
 \qquad\text{and}\qquad
 X_\delta=o(1).
\]

After discarding the exceptional pools, some independent choice of states on all
remaining pools contains no patch-only cross-pool triple.

#### Proof

The right side of PP3cy is `o(1)` under `K=o(m^(1/3))`.  Therefore

\[
 \mathbb E\left(B/K+X_\delta\right)=o(1).
\]

Some equipartition has both summands `o(1)`.  Discard the `B` exceptional pools;
this can only decrease `X_delta`.  On every remaining pool choose a clean state
independently.  The expected number of patch-only triples is at most
`X_delta=o(1)`, hence is below one for all sufficiently large `m`.  Some state
assignment therefore contains none. ∎

A small amount of initial pool slack replaces the discarded `o(K)` variables.

## 4. Architectural consequence

For the one-rung-per-pool constant-width proposal, the published transfer target
would require

\[
 K\asymp m^{0.525},
\]

which lies far beyond the `m^(1/3)` range of PP3cz.  The theorem therefore points
to one of two architectures:

1. **large-width variables:** retain only `m^mu` pool variables with `mu<1/3`,
   each state installing many width-two micro-rungs internally;
2. **square-root or endpoint-adapted macro-rungs:** return to the earlier
   `K=m^0.05` prime-gap ladder, now using matching-first and pattern-compression
   preparation instead of independent parabolic template conditioning.

At `K=m^0.05`, the patch-only potential in PP3cy is `O(m^-0.9)` from pool pairs
and `O(m^-0.85)` from pool triples.  Thus cross-variable patch geometry is not
the obstruction at that scale.

## 5. Remaining macro-state problem

The unresolved construction is now a *large-width local variable*: from one
large matching pool, build a polynomial-density state family that installs many
internally compatible micro-rungs while preserving equal margins and source
cleanliness.  Once the number of such variables is below `m^(1/3)`, PP3cy closes
their mutual patch-only compatibility automatically.