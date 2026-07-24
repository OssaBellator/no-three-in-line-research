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

## 2. Random equipartition and clean local domains

Assume `m=Kr`.  Randomly equipartition `P` into ordered pools
`E_1,...,E_K` and assign distinct intervals `I_1,...,I_K`.

After the partition is exposed, suppose each retained pool has a state domain
`Omega_i` of density at least `delta` in its full 36-state bank, with:

- every state locally no-three;
- every state clean against the original source points under consideration.

Choose the pool states independently and uniformly.  PP3cg and conditioning give

\[
 q_1=\frac2{\delta r},
 \qquad
 q_h=\frac1{\delta r},
 \qquad
 q_2=\frac8{\delta r^2}.
\]

Let `Z_patch` count all selected patch-only triples meeting at least two pools.

### Theorem PP3cy -- PROVED

The joint expectation over the random equipartition and the independent pool
states satisfies

\[
 \boxed{
 \mathbb E Z_{\rm patch}
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

Proposition PP3cx gives at most `16m` global patterns, and a restricted pattern
is selected with probability at most `q_h q_1=2/(delta^2r^2)`.  The expected
contribution is at most

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

Using the `32m(m-1)` support cap and
`q_2q_1=16/(delta^2r^3)`, its expected contribution is at most

\[
 32m(m-1)
 \frac{(r)_2r}{(m)_3}
 \frac{16}{\delta^2r^3}
 \le
 \frac{512}{\delta^2(m-2)}.
\]

Now fix three distinct pools.  A global one-cell-per-pool pattern is controlled
by three distinct edges and lands in the specified pools with probability
`r^3/(m)_3`.  Proposition PP3cx and `q_1^3=8/(delta^3r^3)` give

\[
 64m^2
 \frac{r^3}{(m)_3}
 \frac8{\delta^3r^3}
 =
 \frac{512m}{\delta^3(m-1)(m-2)}.
\]

Sum over ordered pool pairs and unordered pool triples. ∎

### Corollary PP3cz -- PROVED

If `delta` is bounded below by a positive constant and

\[
 K=o(m^{1/3}),
\]

then

\[
 \mathbb E Z_{\rm patch}=o(1).
\]

Consequently some equipartition and state assignment has no patch-only
cross-pool triple.

The same conclusion holds together with PP3cm and PP3cv whenever their
exceptional pool fractions tend to zero: discard the exceptional pools using a
small amount of initial slack, and apply the expectation bound to the retained
ones.

## 3. Architectural consequence

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

At `K=m^0.05`, the patch-only expectation in PP3cy is `O(m^-0.85)` from pool
pairs and `O(m^-0.85)` from pool triples.  Thus cross-variable patch geometry is
not the obstruction at that scale.

## 4. Remaining macro-state problem

The unresolved construction is now a *large-width local variable*: from one
large matching pool, build a polynomial-density state family that installs many
internally compatible micro-rungs while preserving equal margins and source
cleanliness.  Once the number of such variables is below `m^(1/3)`, PP3cy closes
their mutual patch-only compatibility automatically.