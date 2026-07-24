# Random matching-block sparsification

The matching-first route no longer needs to assume that each large source block
is geometrically regular.  A random equipartition of one perfect-matching layer
makes the *same-layer local* certificate load small on almost every block when
`r=o(sqrt(m))`.  This closes clean-domain density and disjoint pool packing at
the prime-gap block scale.  The external opposite-layer shadow remains separate.

## 1. Global signature supersets

Let `P` be a perfect matching of `m` no-three-in-line source points.  Fix one
width-two new-coordinate interval `I={a,b}`.  For an edge `e=(x,y) in P`, its
candidate cells are

\[
 (x,a),(x,b),(a,y),(b,y).
\]

Define the following global signature supersets.  Only signatures feasible in a
canonical adjacent state are eventually used, so counting all candidates gives
valid upper bounds.

- `B_I` consists of triples `(p,q,z)` where `p,q,e` are three distinct edges of
  `P`, `z` is one of the four candidate cells controlled by `e`, and the source
  points `p,q,z` are collinear.
- `A_{1,I}` consists of triples `(p,z,w)` where `p` and `e` are distinct edges,
  `z,w` are one movement and one refill candidate controlled by `e`, and the
  three points are collinear.
- `A_{2,I}` consists of triples `(p,z,w)` where `p,e,f` are three distinct edges,
  `z,w` are candidate cells controlled by `e,f`, respectively, and the three
  points are collinear.

### Proposition PP3ck -- PROVED

For every interval `I`,

\[
 |B_I|\le 2m^2,
 \qquad
 |A_{1,I}|\le 8m,
 \qquad
 |A_{2,I}|\le 16m^2.
\]

#### Proof

Fix a candidate cell `z`.  The secant pairs of the no-three set `P` through the
external point `z` form a matching, so there are at most `floor(m/2)` of them.
There are four candidate cells for each of the `m` controlling edges.  Hence

\[
 |B_I|\le4m\lfloor m/2\rfloor\le2m^2.
\]

One edge has four movement/refill candidate pairs.  The line through one such
pair contains at most two points of `P`, because three source points on that line
would contradict the no-three property.  Thus

\[
 |A_{1,I}|\le4m\cdot2=8m.
\]

For an unordered pair of controlling edges there are at most `4*4=16`
candidate-cell pairs, and every resulting line contains at most two source
anchors.  Therefore

\[
 |A_{2,I}|\le32\binom m2<16m^2.
\]

Discarding signatures that are rank-infeasible or use a controlling edge as a
retained anchor only decreases these counts. ∎

## 2. One random block

Choose a uniform `r`-edge subset `E` of `P`, where `4<=r<=m`.  Use interval `I`
and form the canonical matching-block state family from PP3bx.  Let
`B(E),A_1(E),A_2(E)` be its exact feasible local signature families and put

\[
 \Lambda_I(E)
 =
 \frac{4|B(E)|}{r}
 +
 \frac{4|A_1(E)|}{r}
 +
 \frac{12|A_2(E)|}{r(r-1)}.
\]

### Theorem PP3cl -- PROVED

The expected local load satisfies

\[
 \boxed{
 \mathbb E\Lambda_I(E)
 \le
 \lambda(m,r)
 }
\]

where

\[
 \lambda(m,r)
 =
 \frac{8m(r-1)(r-2)}{(m-1)(m-2)}
 +
 \frac{32(r-1)}{m-1}
 +
 \frac{192m(r-2)}{(m-1)(m-2)}.
\]

In particular,

\[
 \lambda(m,r)=O(r^2/m+r/m).
\]

#### Proof

Every blocker or ordinary-anchor signature uses three distinct source edges, so
it survives in a uniform `r`-subset with probability `(r)_3/(m)_3`.  Every
same-edge anchor signature uses two distinct source edges and survives with
probability `(r)_2/(m)_2`.  Proposition PP3ck and linearity of expectation give

\[
 \mathbb E|B(E)|
 \le
 2m^2\frac{(r)_3}{(m)_3},
\]

\[
 \mathbb E|A_1(E)|
 \le
 8m\frac{(r)_2}{(m)_2},
\]

and

\[
 \mathbb E|A_2(E)|
 \le
 16m^2\frac{(r)_3}{(m)_3}.
\]

Substitution into the definition of `Lambda_I(E)` and cancellation gives the
three displayed terms of `lambda(m,r)`. ∎

The estimate is uniform in the location of the width-two interval.

## 3. Simultaneous disjoint pools

Assume for simplicity that `m=Kr`.  Randomly permute the edges of `P` and split
them into ordered blocks `E_1,...,E_K` of size `r`.  Assign any fixed disjoint
width-two intervals `I_1,...,I_K` to the blocks.  Each marginal `E_i` is a uniform
`r`-subset, although the blocks are not independent.

### Theorem PP3cm -- PROVED

There exists an equipartition satisfying

\[
 \frac1K\sum_{i=1}^K\Lambda_{I_i}(E_i)
 \le
 \lambda(m,r).
\]

For every `eta>0`, the same equipartition has at least

\[
 \boxed{
 \left(1-\frac{\lambda(m,r)}{\eta}\right)K
 }
\]

blocks with

\[
 \Lambda_{I_i}(E_i)\le\eta.
\]

Every such block has canonical clean-state density at least `1-eta` by PP3ca.

#### Proof

Linearity of expectation and PP3cl give

\[
 \mathbb E\frac1K\sum_i\Lambda_{I_i}(E_i)
 \le\lambda(m,r).
\]

Hence some equipartition has average no larger than this value.  In that
partition, if `g` blocks have load greater than `eta`, then
`g eta<K lambda(m,r)`.  The claimed count follows, and PP3ca supplies the clean
state density. ∎

Taking `eta=sqrt(lambda(m,r))` shows that whenever `r=o(sqrt(m))`, all but
`o(K)` blocks have canonical clean density `1-o(1)`.

### Corollary PP3cn -- PROVED

For each good block, retain the full 36-state geometry bank and then restrict to
its locally clean states.  Its clean density inside the full bank is at least

\[
 \boxed{
 \delta_i\ge\frac{1-\eta}{36}.
 }
\]

Thus if `r=o(sqrt(m))`, an equipartition exists in which all but `o(K)` disjoint
blocks have full-bank clean density `1/36-o(1)`.

#### Proof

Every clean canonical deletion state is one state of the full 36-state bank.
There are at least `(1-eta) binom(r,4)` such states among
`36 binom(r,4)` total full-bank states. ∎

## 4. Prime-gap scaling consequence

At the constant-width target

\[
 K\asymp m^{0.525},
 \qquad
 r\asymp m^{0.475},
\]

one has

\[
 \lambda(m,r)=O(m^{-0.05}).
\]

With `eta=sqrt(lambda)`, all but an `O(m^{-0.025})` fraction of the disjoint
matching pools have canonical clean density at least `1-O(m^{-0.025})`, and full
36-state clean density at least `1/36-O(m^{-0.025})`.

A fixed amount of slack in the initial number of pools absorbs the discarded
`o(K)` blocks.  Therefore the two formerly separate requirements

1. polynomial local clean-domain density;
2. a packing of the required number of disjoint source reservoirs;

are simultaneously available for every saturated source, using either perfect
matching layer.

## 5. Remaining obstruction

The theorem cleans triples involving the retained points of the *same matching
pool*.  It does not control:

- secants through points in the opposite matching layer;
- source points lying in other pool variables;
- patch-patch triples between distinct pools.

Those are exactly the external and cross-block profiles in PP3ci.  The remaining
geometric problem is therefore narrower: after the universal sparsification
above, prove a boundary secant-shadow or protected-trade theorem for those
profiles.  Local clean density and disjoint pool packing are no longer open.