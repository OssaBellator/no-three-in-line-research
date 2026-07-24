# Greedy square-root component-clean macro bank

The ordered-pool reduction PP3dh asks for width `Omega(sqrt(R))` from one
matching pool.  A complete internally clean macro patch is still open, but the
two movement/refill components can be cleaned universally at this width with a
greedy injection.  The remaining local obstruction is only a triple meeting
both components.

## 1. Slots and synchronized edge selection

Let

\[
 E=\{(x_e,y_e):e\in[R]\}
\]

be an `R`-edge matching pool, so all `x_e` and all `y_e` are distinct.  Fix a
positive integer `W` and a set `S` of `2W` labelled slots.  Let

\[
 \alpha:S\to[W],
 \qquad
 \beta:S\to[W]
\]

be balanced maps: every value has exactly two preimages under each map.  The
maps may be equal, or may encode two different pairings of the movement and
refill slots.

An injection `phi:S -> E` produces

\[
 M_\phi
 =
 \{(x_{\phi(s)},m+\alpha(s)):s\in S\},
\]

and

\[
 F_\phi
 =
 \{(m+\beta(s),y_{\phi(s)}):s\in S\}.
\]

Delete the `2W` source edges in the image of `phi` and insert
`M_phi union F_phi`.

## 2. Greedy component cleaning

Order the slots as `s_1,...,s_{2W}`.  Suppose the first `k` have been assigned.
Call an unused edge forbidden for `s_{k+1}` if adding it creates a collinear
triple wholly inside the current movement component or wholly inside the
current refill component.

### Proposition PP3di -- PROVED

At step `k`, at most

\[
 k+2\binom k2=k^2
\]

source edges are unavailable, including the `k` already used edges.
Consequently, if

\[
 \boxed{(2W-1)^2<R,}
\]

there is an injection `phi` for which both `M_phi` and `F_phi` are
no-three-in-line.

#### Proof

Take a pair of previously assigned movement points.  If their line can meet the
new movement row `m+alpha(s_{k+1})`, the intersection has one prescribed old
column.  Since the pool has distinct column coordinates, at most one unused
edge realizes it.  A line coinciding with the new row cannot occur: before a
slot is filled, at most one earlier movement point has that row label because
`alpha` has fibre size two.

Thus every pair of previous movement points forbids at most one edge.  The same
argument for the refill component uses the distinct row coordinates and the
balanced map `beta`, and forbids at most one further edge per previous pair.
Together with the `k` used edges, at most

\[
 k+2\binom k2=k^2
\]

edges are unavailable.

At the last step `k=2W-1`, the displayed hypothesis leaves at least one choice.
Choose greedily.  Every possible component-internal triple is excluded when its
last slot is assigned. ∎

No monotonicity of the pool endpoints is needed for PP3di.

### Corollary PP3dj -- PROVED

For every `R>=16`, taking

\[
 W=\left\lfloor\frac{\sqrt R}{4}\right\rfloor
\]

satisfies the greedy condition.  The operation adds net width `W`, preserves
exactly two points in every old and new row and column, and has two individually
no-three components of size `2W`.

#### Proof

One has `(2W-1)^2<R`.  Deleting the injection image creates one deficit in each
of its old rows and columns.  The movement component restores every selected old
column once and gives two points to each new row because `alpha` is balanced.
The refill component restores every selected old row once and gives two points
to each new column because `beta` is balanced.  The net gain is `4W-2W=2W`. ∎

## 3. A spread greedy distribution

At each step choose uniformly among the currently allowed unused edges.  Put

\[
 L=R-(2W-1)^2.
\]

### Proposition PP3dk -- PROVED

For any `q` prescribed slot-edge assignments compatible with their chronological
order, their joint probability under the random greedy algorithm is at most

\[
 \boxed{L^{-q}.}
\]

Consequently:

- a prescribed movement or refill cell has probability at most `2/L`;
- a prescribed pair controlled by two distinct source edges has probability at
  most `4/L^2`;
- any prescribed fixed-rank pattern on `q` distinct controlling edges has
  probability `O_q(L^{-q})`.

For `W<=sqrt(R)/4`, one has `L>=R/2` for all sufficiently large `R`, so cell and
ordinary-pair probabilities are `O(1/R)` and `O(1/R^2)`.

#### Proof

At every step there are at least `L` allowed choices, regardless of the previous
history.  Conditioning successively on prescribed assignments gives the
`L^{-q}` cylinder bound.  A grid cell with one new-coordinate label can be
realized by at most the two slots in the corresponding fibre of `alpha` or
`beta`.  Two prescribed cells on distinct controlling edges have at most four
slot realizations. ∎

A movement/refill pair controlled by the same source edge has only one
controlling edge and may have probability `O(1/R)`.  Varying the balanced map
`beta` can disperse the new-coordinate pair attached to that edge, but the
resulting mixed-component geometry still requires analysis.

## 4. Exact remaining local certificates

The union `M_phi union F_phi` is not asserted to be no-three-in-line.  PP3di
removes exactly the triples wholly inside `M_phi` or wholly inside `F_phi`.
Every remaining internal macro triple has one of the forms

\[
 2M+1F
 \qquad\text{or}\qquad
 1M+2F.
\]

Because each component is no-three, the number of such triples in any fixed
state is at most

\[
 4W(2W-1)
\]

by PP3ab.  The high-probability subfamily consists of mixed triples in which a
movement point and a refill point are controlled by the same selected source
edge.  All other mixed triples involve at least two, and usually three, distinct
controlling edges and inherit the PP3dk cylinder spread.

Thus the universal square-root macro problem is reduced to a **mixed-component
cleaning theorem**, with explicit `O(1/R)` cell spread and `O(1/R^2)` ordinary
pair spread already available.

## 5. Relation to the prime-gap reduction

At the exponents of PP3dh, `R=m^0.475` and `W=Theta(sqrt(R))=m^0.2375`.
PP3di therefore supplies the required width and component-clean spread on each
of the `m^0.2875` extracted pools.  To complete PP3dh it remains to:

1. clear the mixed `M/F` triples, especially the same-source-edge pair class;
2. clean the components against the opposite source layer using PP3cp, PP3cr,
   or protected trades;
3. retain the compressed cross-variable potential required in PP3dh.

The local theorem is no longer an arbitrary square-root construction.  Both
large components and their degree/spread structure are explicit; only their
mutual incidence remains open.