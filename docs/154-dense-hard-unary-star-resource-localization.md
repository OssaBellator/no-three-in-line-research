# Dense hard-unary support localizes to stars or resource banks

PP3sp--PP3su absorb every zero-density hard-unary rectangle support. The
remaining case has a positive-density interaction graph on the resource-disjoint
rectangle bank. Density first produces a linear star of rectangle pairs. After
pigeonholing the finite cross-cell orientation, all selected forbidden cells
share one endpoint resource.

Choose one retained-source witness pair for each forbidden cell. Those witness
pairs form a graph on source points. A second star/matching dichotomy yields
either one source point clearing many unary cells when moved, or a large
vertex-disjoint blocker-pair bank. These are the same two structural inputs as
PP3hx and PP3hy.

## 1. Hard-unary rectangle interaction graph

Let

```text
R_1, ..., R_H
```

be pairwise row/column-disjoint endpoint rectangles. Each rectangle has two left
resources and two right resources, ordered canonically.

Join rectangles `R_s,R_t` when at least one cell in either directional cross
block

```text
L_s x R_t
or
L_t x R_s
```

is forbidden by a retained-source unary no-three condition. Direct designated
recapture cells and pure collision cells are excluded from this hard-unary graph;
they are handled separately by PP3jo--PP3jq and the endpoint-host definition.

Call the resulting simple interaction graph `G_U`.

## 2. Dense interaction gives one fixed-resource star

### Proposition PP3wc -- PROVED

If

$$
|E(G_U)| >= c H^2
$$

for a fixed positive `c`, then there is a rectangle `R_s` and a set of at least
`2cH` partner rectangles incident with it.

After passing to a constant-fraction substar, there are:

- one fixed left or right resource `x` of `R_s`;
- one fixed directional cross-block orientation;
- one fixed resource position inside every partner rectangle;

such that every retained star edge has a unary-forbidden cross cell

$$
z_t = (x,y_t)
$$

or its transposed form, where the partner resources `y_t` are all distinct.

#### Proof

Take a vertex of at least average degree. Each interaction edge has one of at
most eight refined orientations: which rectangle supplies the left resource,
which of the two centre resources is used, and which of the two partner-resource
positions is used. Pigeonhole. Partner rectangles are resource-disjoint, so the
selected `y_t` are distinct. ∎

Thus positive-density hard-unary support contains a linear forbidden-cell star
on one endpoint row or column resource.

## 3. Witness pairs are distinct and nonaxis

For each selected forbidden cell `z_t`, choose one retained-source pair

```text
{p_t,q_t}
```

collinear with `z_t` after the current endpoint deletions.

### Proposition PP3wd -- PROVED

The chosen witness line is nonvertical in the fixed-column form and nonhorizontal
in the transposed fixed-row form. Consequently one retained-source pair can
witness at most one selected forbidden cell, and the witness pairs may be treated
as distinct edges of a graph on source points.

#### Proof

In the fixed-column form, the current selected-layer endpoint in that old column
is deleted before insertion. Only the opposite-layer source point in the column
remains, so two retained source points do not form a vertical unary witness with
the replacement cell. Hence the witness line is nonvertical and meets the fixed
column in at most one cell. The row statement is transposed. ∎

This is the same nonaxis feature used in PP3jo.

## 4. Source-witness star or matching

Let `h` be the number of selected forbidden cells and form the simple graph
`W_src` whose edges are their chosen witness pairs.

### Proposition PP3we -- PROVED

For every integer `L>=1`, one of the following holds.

1. One source point belongs to at least `L` witness pairs.
2. The witness graph contains a matching of size at least
   
   $$
   h/(2L).
   $$

#### Proof

Take a maximal matching of size `m`. If `m>=h/(2L)`, use it. Otherwise its
`2m` endpoints cover all `h` witness edges, so one cover vertex has degree larger
than `L`. ∎

Taking `L=ceil(sqrt(h))` gives a square-root source star or a square-root
vertex-disjoint blocker bank. For a linear forbidden-cell star, both outputs
grow polynomially.

## 5. Source-star conversion interface

### Proposition PP3wf -- PROVED

In the first alternative of PP3we, moving the common source point destroys at
least `L` distinct hard-unary witness incidences on the fixed endpoint resource.

If the point lies outside the controller pools, this is the free source-star
credit of PP3ki--PP3km. If it lies inside one pool, it is exact dynamic `Xi`
credit under PP3ky and the pool-compatible cross-block interface PP3tg--PP3tm.

#### Proof

The witness pairs and forbidden cells are distinct by PP3wd. Every selected
incidence contains the common source point, so moving it removes all of them.
The cited star theorems give the appropriate fixed or dynamic potential identity.
∎

The unresolved quantity is the insertion collateral of the source-admissible
trade moving the star centre.

## 6. Vertex-disjoint witness matching

Assume the second alternative of PP3we. Every source point belongs to one of the
two permutation layers of the saturated source.

### Proposition PP3wg -- PROVED

A constant-fraction submatching has one fixed ordered layer type for its witness
pairs. From every pair in that submatching, choose the endpoint in one fixed
layer position. The chosen endpoints then:

1. lie in one common permutation layer;
2. have pairwise distinct old rows and columns;
3. each destroy a distinct hard-unary witness incidence when moved.

Hence they form a resource-disjoint credited endpoint bank of size
`Omega(h/L)`.

#### Proof

There are only four ordered layer types for a witness pair. Pigeonhole one type
and one endpoint position. Distinct points in one permutation layer use distinct
rows and columns. Witness edges were vertex-disjoint, so the chosen endpoints are
distinct and each belongs to its own witness incidence. ∎

This is the endpoint-resource input required by PP3hy, PP3pn, and the later
cross-block trade machinery.

## 7. Revised positive-density unary endpoint

### Corollary PP3wh -- PROVED

Positive-density hard-unary rectangle support is not a terminal graph-density
case. It yields one of:

1. a source-star centre with polynomial removal credit on one fixed endpoint
   resource;
2. a polynomial resource-disjoint endpoint bank with one hard-unary credit per
   endpoint;
3. concentrated insertion collateral preventing the corresponding star/resource
   trade from being paid.

Thus the hard-unary frontier rejoins the dynamic star/resource conversion
problem. The only remaining unary obstruction is paid collateral or a failure of
the source-admissible trade host, not raw positive-density support.