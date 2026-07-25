# Pool-compatible cross-block trades for the dynamic excess potential

The dynamic potential PP3kx requires endpoint permutations to remain inside their
original controller pools. The cross-block construction is naturally
pool-compatible: pair current matching-layer endpoints inside one pool, group
the resulting \(2\)-by-\(2\) blocks, and use only permutations between resource
subblocks of that same pool.

This chapter imports the unary-independent superregular block theorem and the
chromatic paid criterion into the \(\Xi\)-potential setting. Diffuse hard-source
geometry, diffuse pool-local source mass, and diffuse \(\Xi\)-insertion weight then
give a strict pool-compatible potential decrease.

## 1. Natural endpoint rectangles inside one pool

Fix one controller pool

\[
E\subseteq X\times Y
\]

of the selected perfect-matching layer. Let

\[
R_0=\{r_1,\ldots,r_{2H}\}\subseteq E,
\qquad
r_s=(x_s,y_s),
\]

with all old columns and rows distinct.

Pair the endpoints arbitrarily. One pair \(r_{2j-1},r_{2j}\) forms a natural
\(2\)-by-\(2\) endpoint rectangle with its current and cross diagonals.

### Proposition PP3tg -- PROVED

The \(H\) natural rectangles are resource-disjoint. Any finite-state cross-block
construction formed from them:

1. preserves the old-column set \(X\) and old-row set \(Y\);
2. is a permutation of endpoints inside the same pool;
3. preserves saturation;
4. preserves the complete candidate-cell universe of PP3ku.

#### Proof

The original endpoints form a matching, so their left and right resources are
distinct. Every cross-block state is a perfect matching between subsets of the
same \(X\) and \(Y\), using each selected resource once. Apply PP3ku. ∎

Thus every installed state is eligible for

\[
\Xi(S')-\Xi(S)=\mathcal I_\Xi-\mathcal C_\Xi.
\]

## 2. Credit in the resource-bank branch

Suppose the endpoints come from a PP3hy resource matching, refined so that each
chosen endpoint belongs to one distinct designated blocker incidence.

### Proposition PP3th -- PROVED

The removal credit satisfies

\[
\mathcal C_\Xi(R_0)\ge2H.
\]

Every cross-block state that moves all \(2H\) endpoints retains this complete old
credit before insertion cost is subtracted.

#### Proof

Each chosen endpoint destroys its distinct designated blocker incidence. The
incidences occur among the old-pair terms of the exact credit, as in PP3ic and
PP3pn. Cross-block states use no current endpoint cell, so every endpoint moves.
∎

For a star bank, the same construction uses the exact possibly larger credit
from PP3ky; the uniform one-per-endpoint lower bound is not required.

## 3. Pool extraction from a global resource bank

### Proposition PP3ti -- PROVED

If \(q\) credited endpoints are distributed among \(M\) pools, one pool contains
at least

\[
\left\lceil\frac qM\right\rceil
\]

of them. At the slab-optimal scales this is

\[
m^{19/40+o(1)}
\]

when \(q=\Omega(m^{21/40})\).

#### Proof

Pigeonhole by pool and subtract exponents:

\[
\frac{21}{40}-\frac1{20}=\frac{19}{40}.
\]

∎

Thus pool compatibility still leaves a polynomially growing credited bank.

## 4. Hard-source unary graph and superregular blocks

On the natural endpoint rectangles inside the chosen pool, let \(F\) be the
simple graph of cells forbidden for source validity or collision. Direct
\(\Xi\)-recapture is not deleted; it is charged as insertion weight.

### Theorem PP3tj -- PROVED

If

\[
|E(F)|=o(H^2),
\]

then after deleting \(o(H)\) natural rectangles, the remaining endpoints split
into growing blocks whose cross-state directional hosts are near-complete
superregular and whose product perfect-matching law has fixed-rank probability

\[
O(b^{-r}).
\]

Every selected state is pool-compatible and moves all endpoints in its block.

#### Proof

Apply PP3sp--PP3sr and PP3si--PP3sm. Their proofs use only disjoint endpoint
resources and a simple hard-unary graph. Pool compatibility is PP3tg. ∎

The pool-local fixed-anchor pair and inserted-triple counts remain part of the
paid first moment. They may be bounded by a separate pool-local estimate or
entered explicitly into the theorem below. The global chromatic closure PP3td
cannot be invoked merely by pigeonholing a global resource bank into one pool.

## 5. Dynamic Xi source and insertion weights

Let:

- \(P_\Xi\) be the pool-local fixed-anchor compatible pair count;
- \(Q_\Xi\) be the pool-local inserted collinear-triple count;
- \(A_\Xi\) be the total \(\Xi\)-weight over one possible inserted cell and one
  unchanged source point;
- \(B_\Xi\) be the total \(\Xi\)-weight over compatible pairs of possible inserted
  cells.

Let \(k\) be the equitable-colouring count of the hard-unary rectangle
interaction graph.

### Theorem PP3tk -- PROVED

There is a fixed constant \(K\) such that a source-admissible pool-compatible
cross-block trade strictly decreases \(\Xi\) whenever

\[
K^2\frac{kP_\Xi}{H^2}
+
K^3\frac{k^2Q_\Xi}{H^3}
+
K\frac{kA_\Xi}{H^2}
+
K^2\frac{k^2B_\Xi}{H^3}
<1-o(1).
\]

In particular it is sufficient that all four scaled quantities vanish.

#### Proof

Apply the equitable-colour paid selection theorem PP3sx inside the pool, using
the product superregular state law from PP3tj and the exact removal credit from
PP3th. The resulting source-valid state has insertion cost below credit. Apply
the dynamic identity PP3kx. ∎

Unlike the global rectangle branch, no unconditional estimate for
\(P_\Xi,Q_\Xi\) at this pool-local scale is asserted here.

## 6. Star-centre version

### Corollary PP3tl -- PROVED

Suppose a pool contains a blocker-star centre with exact credit
\(C_{\rm star}\). Add enough pool endpoints to form a growing natural rectangle
bank containing the centre. If the source-safe block construction is available
and one source-admissible selected block state containing the centre has
insertion cost

\[
o(C_{\rm star}),
\]

then the trade moves the centre and strictly decreases \(\Xi\).

#### Proof

The centre credit is PP3ky. Cross-block states move every endpoint in the
selected block, including the centre. Apply PP3kx. ∎

The collateral need only be small relative to concentrated star credit, not
relative to the number of filler endpoints.

## 7. Revised dynamic-potential endpoint

### Corollary PP3tm -- PROVED

The pool-compatible dynamic-\(\Xi\) conversion is complete under:

1. zero-density hard source-invalid support on the credited endpoint bank;
2. chromatically diffuse pool-local source pair and triple mass;
3. chromatically diffuse unary and binary \(\Xi\)-insertion weight.

Failure requires one of:

- positive-density hard source-invalid endpoint support inside a pool;
- pool-local anchored-pair mass at scale \(H^2/k\);
- pool-local inserted-triple mass at scale \(H^3/k^2\);
- unary \(\Xi\)-weight at scale \(H^2/k\);
- binary \(\Xi\)-weight at scale \(H^3/k^2\);
- a star whose insertion collateral remains comparable with its concentrated
  removal credit.

Thus the combinatorial construction of a pool-compatible state is closed in the
diffuse regime. Pool-local source mass and \(\Xi\)-weight concentration remain
explicit quantitative inputs.