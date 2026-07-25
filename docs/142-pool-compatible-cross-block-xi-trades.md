# Pool-compatible cross-block trades for the dynamic excess potential

The dynamic potential PP3kx requires endpoint permutations to remain inside their
original controller pools.  The cross-block construction is naturally
pool-compatible: pair current matching-layer endpoints inside one pool, group
the resulting \(2\)-by-\(2\) blocks, and use only permutations between resource
subblocks of that same pool.

This chapter imports the unary-independent superregular block theorem and the
chromatic paid criterion into the \(\Xi\)-potential setting.  Diffuse hard-source
geometry and diffuse \(\Xi\)-insertion weight then give a strict pool-compatible
potential decrease.

## 1. Natural endpoint rectangles inside one pool

Fix one controller pool

\[
E\subseteq X\times Y
\]

of the selected perfect-matching layer.  Let

\[
R_0=\{r_1,\ldots,r_{2H}\}\subseteq E
\]

be an even endpoint set, with

\[
r_s=(x_s,y_s),
\]

all old columns and rows distinct.

Pair the endpoints arbitrarily.  One pair

\[
r_{2j-1},r_{2j}
\]

forms a natural \(2\)-by-\(2\) endpoint rectangle with:

- the current diagonal
  
  \[
  \{(x_{2j-1},y_{2j-1}),(x_{2j},y_{2j})\};
  \]
- the cross diagonal
  
  \[
  \{(x_{2j-1},y_{2j}),(x_{2j},y_{2j-1})\}.
  \]

### Proposition PP3tg -- PROVED

The \(H\) natural rectangles are resource-disjoint.  Any finite-state
cross-block construction formed from them:

1. preserves the old-column set \(X\) and old-row set \(Y\);
2. is a permutation of endpoints inside the same pool;
3. preserves saturation;
4. preserves the complete candidate-cell universe of PP3ku.

#### Proof

The original endpoints form a matching, so their left and right resources are
distinct.  Every cross-block state is a perfect matching between subsets of the
same \(X\) and \(Y\), using each selected resource once.  Apply PP3ku. ∎

Thus every installed state is eligible for the exact dynamic identity

\[
\Xi(S')-\Xi(S)=\mathcal I_\Xi-\mathcal C_\Xi.
\]

## 2. Credit in the resource-bank branch

Suppose the endpoints come from a PP3hy resource matching, refined so that each
chosen endpoint \(r_s\) belongs to one distinct designated blocker incidence.

### Proposition PP3th -- PROVED

The removal credit satisfies

\[
\mathcal C_\Xi(R_0)\ge2H.
\]

Every cross-block state that moves all \(2H\) endpoints retains this complete old
credit before insertion cost is subtracted.

#### Proof

Each chosen endpoint destroys its distinct designated blocker incidence.  The
incidences occur among the old-pair terms of the exact credit, as in PP3ic and
PP3pn.  Cross-block states use no current endpoint cell, so every endpoint moves.
∎

For a star bank, the same construction uses the exact possibly larger credit
from PP3ky; the uniform one-per-endpoint lower bound is not required.

## 3. Pool extraction from a global resource bank

Let a global resource bank have \(q\) credited endpoints distributed among the
\(M\) disjoint controller pools.

### Proposition PP3ti -- PROVED

One pool contains at least

\[
\left\lceil\frac qM\right\rceil
\]

credited endpoints.  At the slab-optimal scales this is

\[
m^{19/40+o(1)}
\]

when \(q=\Omega(m^{21/40})\).

#### Proof

Pigeonhole the endpoints by pool.  The exponent is

\[
\frac{21}{40}-\frac1{20}=\frac{19}{40}.
\]

∎

Thus pool compatibility still leaves a polynomially growing endpoint bank.
One may also apply the argument independently in several pools.

## 4. Hard-source unary graph and superregular blocks

On the natural endpoint rectangles inside the chosen pool, let \(F\) be the
simple graph of endpoint cells that are forbidden for source validity or
collision.  Direct \(\Xi\)-recapture is not deleted here; it is counted in the
insertion weight.

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

Apply the unary-density regularization PP3sp--PP3sr and the unary-independent
partition PP3si--PP3sm.  The proofs use only disjoint endpoint resources and a
simple hard-unary graph, both present here.  Pool compatibility is PP3tg. ∎

Source-invalid pair and triple counts are handled by the same PP3sg first
moment, or by the chromatic closure PP3tb--PP3td after a suitable secondary
thinning.

## 5. Dynamic Xi insertion weights

For possible inserted endpoint cells \(a,b\), use the pool-invariant pair weight

\[
\omega(a,p)
\]

from PP3kx.  Define:

- \(A_\Xi\): the total weight over one possible inserted cell and one unchanged
  source point;
- \(B_\Xi\): the total weight over compatible pairs of possible inserted cells.

These are exactly the unary and binary insertion-cost totals for
\(\mathcal I_\Xi\).

Let \(k\) be the equitable-colouring count of the hard-unary rectangle
interaction graph.

### Theorem PP3tk -- PROVED

Assume the source-valid pair and triple terms are \(o(1)\) at the chromatic scale.
If

\[
kA_\Xi=o(H^2)
\]

and

\[
k^2B_\Xi=o(H^3),
\]

then some source-admissible pool-compatible cross-block trade strictly decreases
\(\Xi\).

#### Proof

The global paid block selection PP3sy gives one source-admissible block state
whose expected \(\Xi\)-insertion cost is \(o(H/k)\), while its resource-bank
removal credit is \(\Omega(H/k)\) by PP3th.  More directly, apply PP3te with
\(A=A_\Xi\), \(B=B_\Xi\), and the exact credit.  The dynamic identity PP3kx then
gives strict decrease. ∎

For the secondary exponent \(\kappa<1/60\), PP3td makes the source-valid pair and
triple hypothesis automatic.

## 6. Star-centre version

### Corollary PP3tl -- PROVED

Suppose a pool contains a blocker-star centre with exact credit
\(C_{\rm star}\).  Add enough other pool endpoints to form a growing natural
rectangle bank containing the centre.  If the source-safe block construction is
available and one selected block state containing the centre has expected
insertion cost

\[
o(C_{\rm star}),
\]

then a source-admissible pool-compatible trade moves the centre and strictly
decreases \(\Xi\).

#### Proof

The centre credit is PP3ky.  Cross-block states move every endpoint in the
selected block, including the centre.  Apply PP3kx. ∎

The collateral need only be small relative to the concentrated star credit, not
relative to the number of filler endpoints.

## 7. Revised dynamic-potential endpoint

### Corollary PP3tm -- PROVED

The pool-compatible dynamic-\(\Xi\) conversion is complete under:

1. zero-density hard source-invalid support on the credited endpoint bank;
2. chromatically diffuse unary and binary \(\Xi\)-insertion weight;
3. the established source-valid pair/triple bounds.

Failure requires one of:

- positive-density hard source-invalid endpoint support inside a pool;
- unary \(\Xi\)-weight at scale \(H^2/k\);
- binary \(\Xi\)-weight at scale \(H^3/k^2\);
- a star whose insertion collateral remains comparable with its concentrated
  removal credit.

Thus construction of a pool-compatible trade is no longer a separate black-box
step in the diffuse regime.  The remaining dynamic obstruction is explicit
source or \(\Xi\)-weight concentration.