# Monotone matching-pool extraction

The support-compressed macro target in PP3dc is easier when the source matching
endpoints have a common order.  Such pools are available in every perfect
matching layer at exactly the exponents required by the prime-gap ladder.

## 1. A self-contained monotone subsequence bound

Represent a perfect matching of `[m]` as a permutation sequence

\[
 y_1,\ldots,y_m,
\]

where `(i,y_i)` is the matching point in column `i`.

### Proposition PP3dd -- PROVED

Every sequence of `N` distinct real numbers contains an increasing subsequence
of length at least `sqrt(N)` or a decreasing subsequence of length at least
`sqrt(N)`.

#### Proof

For each position `j`, let `a_j` be the length of the longest increasing
subsequence ending at `j`, and let `b_j` be the length of the longest decreasing
subsequence ending at `j`.

The pairs `(a_j,b_j)` are distinct.  Indeed, if `i<j`, then either `y_i<y_j`, in
which case `a_j>a_i`, or `y_i>y_j`, in which case `b_j>b_i`.  If the maximum
increasing and decreasing lengths are `A,B`, there are at most `AB` possible
pairs.  Hence `N<=AB`, so `max(A,B)>=sqrt(N)`. ∎

## 2. Repeated disjoint extraction

### Theorem PP3de -- PROVED

Let `s,r` be positive integers satisfying

\[
 \boxed{
 2sr+r^2\le m.
 }
\]

Every perfect matching on `[m]` contains `s` pairwise edge-disjoint monotone
submatchings of size `r` having the same orientation: all increasing or all
decreasing.

#### Proof

Repeatedly remove a monotone subsequence of length `r`.  Before the
`j`-th extraction, with `j<2s`, at least

\[
 m-jr
 \ge
 m-2sr
 \ge
 r^2
\]

points remain.  Proposition PP3dd therefore supplies another increasing or
decreasing subsequence of length `r`.  After `2s` disjoint extractions, at least
`s` have the same orientation by the pigeonhole principle. ∎

### Corollary PP3df -- PROVED

Fix exponents

\[
 \mu=0.05,
 \qquad
 \rho=0.475.
\]

For all sufficiently large `m`, every perfect matching layer contains

\[
 s=\lfloor m^\mu\rfloor
\]

pairwise disjoint monotone pools, each containing

\[
 r=\lfloor m^\rho\rfloor
\]

source edges, all with one common orientation.

If the common orientation is decreasing, the global row reflection

\[
 (x,y)\longmapsto(x,m+1-y)
\]

turns all pools increasing while preserving the grid, saturation, and the
no-three property.

#### Proof

The two terms in the extraction condition have orders

\[
 2sr=O(m^{0.525})
 \qquad\text{and}\qquad
 r^2=O(m^{0.95}),
\]

both `o(m)`.  Thus `2sr+r^2<=m` for all sufficiently large `m`.  Reflection is
an affine grid automorphism and preserves collinearity and row/column degrees. ∎

## 3. Consequence for the macro route

The prime-gap target needs about `m^0.05` support-compressed variables, each
installing width on the order of `m^0.475`.  PP3df supplies exactly that many
disjoint matching-first pools of the corresponding size, with aligned endpoint
order inside every pool.

The unresolved macro construction may therefore assume, without loss at the
exponent level, that one local pool has the form

\[
 (x_1,y_1),\ldots,(x_r,y_r),
 \qquad
 x_1<\cdots<x_r,
 \qquad
 y_1<\cdots<y_r.
\]

This is much stronger than an arbitrary matching endpoint set.  It supports:

- monotone movement and refill assignments;
- sign-separated cross rectangles;
- ordered interval or convex-curve encodings;
- recursive subdivision into smaller aligned pools.

PP3df does not itself build an internally no-three macro patch.  It closes the
source-structure side of that problem: enough ordered endpoint pools exist in
every saturated source, independent of the geometry of its prime-size
construction.