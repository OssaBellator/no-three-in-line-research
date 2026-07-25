# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
prime-minus-one sides and asks for an exact row-column-preserving patch from side
`m` to side `m+t`. The patch must add `2t` net points, leave exactly two points
in every old and new row and column, and create no collinear triple.

The active theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).

## PP1 — Degree interface

### Status: PROVED

Boundary and arbitrary-reservoir degree states are classified. Matching-edge
deletions and movement/refill insertions restore exact old and new row/column
margins. Degree bookkeeping is closed.

## PP2 — Selection interfaces

### Status: PROVED AS IMPLICATIONS

The branch contains clone-space local lemmas, deletion-aware expectations,
finite-state CSPs, 2-SAT/CNF endpoints, weighted local lemmas, and spread
perfect-matching selection. The unresolved work is geometric preparation.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to structured concentration and hierarchy conversion

## 1. Slab-optimal architecture

Every saturated source decomposes into two perfect-matching layers. Consecutive
column-slab pools give

```text
macro count M = m^(1/20+o(1)),
pool size   R = m^(19/20+o(1)),
macro width W = m^(19/40+o(1)),
total width T = MW = m^(21/40+o(1)).
```

This balance is optimal among disjoint source-pool architectures with local width
`O(sqrt(R))`.

Each macro deletes source edges `(x,y)` and inserts movement/refill points

\[
(x,A),
\qquad
(B,y).
\]

Balanced label maps restore exact saturation. Product-space local lemmas give
internally no-three macros with fixed-rank `O(R^-r)` spread.

## 2. Controller-aware safety and external closure

Unselected matching-pool edges remain in the source. A candidate value is safe
only when every blocker pair through its movement/refill cell contains its
controller edge, which is deleted, and its same-slot movement/refill pair has no
retained source anchor.

At the slab-optimal exponents, every remaining patch-only cross-macro class and
every ordinary two-slot source-anchor class has `o(1)` incident probability mass.
Thus any saturation-compatible controller-aware allocation completes an
`Omega(m^0.525)` patch.

## 3. Dynamic excess shadow

Every candidate has one automatic controller-containing axis blocker. The
pairing-invariant potential

\[
\Xi(S)=\sum_z(b_S(z)-1)
\]

counts additional nonaxis blockers. Pool-compatible endpoint trades satisfy an
exact insertion-cost-minus-removal-credit identity. Any uniform improving trade
theorem terminates automatically.

## 4. Four controller-aware allocation interfaces

Controller-cell defects and same-slot anchor counts give deterministic nondegree
upper bounds

\[
\overline d_i(A)\le\rho_i(A),
\qquad
\overline e_i(B)\le\chi_i(B).
\]

The branch has four completion mechanisms.

1. **One-sided bottleneck/slack:**
   
   \[
   r_{\rm score}\le\min_B\Lambda_{\rm score}(B).
   \]
2. **Deterministic two-sided ownership:** balanced movement/refill thresholds
   satisfy
   
   \[
   r+s\le W.
   \]
3. **Random two-sided local Ore:** every macro nonedge satisfies
   
   \[
   \rho_i(A)+\chi_i(B)
   \le
   T-m^{23/80+o(1)}.
   \]
4. **Random one-sided complementary degree:** every incompatible triple satisfies
   
   \[
   \rho_i(A)+\kappa(B)
   \le
   T-8\sqrt{T\log T}.
   \]

At threshold `r`, balanced movement ownership exists exactly when

\[
W|N_M(X)|\ge|X|
\]

for every movement-label set `X`. Failure gives an exact capacitated Hall set and
an all-bad label-by-macro rectangle.

The total same-slot anchor mass is `m^(2+o(1))`, so anchor-driven ownership
failure cannot remain at middle density. It is a sublinear exceptional label
cluster or a nearly dead macro column.

## 5. Source-valid resource endpoint

A resource bank of size `Q=Omega(m^0.525)` may be thinned adaptively to a growing
subbank with:

- no unary-invalid endpoint arc;
- no anchored transition event;
- vanishing high-support source-invalid expectation;
- a fully source-valid derangement with one-cell probability `(1+o(1))/q`.

Source admissibility is closed in the sparse-unary endpoint branch.

## 6. Hall and original binary-shadow endpoints

Delete designated recapture cells and residual unary-shadow cells from the
source-safe endpoint host. Failure is exactly a Hall rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

Binary shadow may be covered by unary deletion. Its fractional minimum resource
congestion has factor-two rounding, an exact LP dual conflict packing, and Hall
inheritance. The remaining original binary-shadow objects are a linear-
congestion dual packing or a high-overlap witness-line pencil.

## 7. Recapture-line rectangle extraction

For a recapture-dominated Hall core, adaptive thinning preserves a dense target
set. If the owner-line potential does not decrease, Szemerédi--Trotter and a
multiplicity split give a positive linear family of nonaxis lines. Every good
line carries:

- at least `q^(1/3-delta)` resource-disjoint owner/replacement cells;
- at least `q^(1-delta)` Hall-target cells;
- total typed multiplicity `Omega(q^2)` over the family.

Pairing one cell from each trace gives `Omega(q^3)` alternating rectangle
candidates. A four-resource greedy matching extracts `Omega(q)` pairwise
row/column-disjoint rectangle blocks.

Rectangle extraction is closed.

## 8. Superregular rectangle installation

Reserve a small linear rectangle bank. In a superregular source-safe endpoint
host:

- the residual host has a perfect matching;
- the residual matching may be chosen source-valid;
- the same matching may be chosen low-cost when residual unary/binary shadow is
  diffuse;
- each rectangle is an equal-margin two-state permutation block;
- all remaining no-three constraints form an exact rank-at-most-three CNF;
- exact insertion shadow is a unary/binary finite-state cost.

First-moment, variable-local-lemma, and support-cleaning arguments close diffuse
geometric and paid collateral.

## 9. Cross-block signature bypass

The original line and cross diagonals are not a terminal state space. Pair two
resource-disjoint rectangles and select only cells in the two cross resource
blocks.

There are exactly four cross-block perfect-matching states. Before general unary
pruning, at least one state preserves both designated owner credits. After
pruning, safe state existence is exactly two `2 by 2` Hall tests.

If the non-designated unary endpoint graph has maximum degree `d`, each rectangle
has at most `4d` bad partners. Hence `d=o(h)` allows almost all `h` rectangles to
pair into source-safe four-state supervariables with at least two credits each.

This construction ignores every witness supported only on the original
rectangle diagonals. Under sparse unary degree it bypasses:

- credit-poor homogeneous Boolean signatures;
- three-rectangle signed contradictions;
- dense all-cross conflict graphs;
- rich cross lines and pencils;
- complete fixed-anchor secant designs on the original cross cells.

## 10. Multistate Ramsey completion

After local-state pruning, pigeonhole a common nonempty alphabet of at most four
states. Adaptive thinning removes ternary bad boxes on a growing subbank.
Fixed-colour Ramsey makes the complete pair signature homogeneous.

- If some diagonal pair `(a,a)` is allowed, the all-`a` state satisfies every
  binary constraint.
- If every diagonal pair is forbidden, at most five variables already form a
  contradiction.

A constant state with diffuse unary/binary cost gives a strict paid improvement
against the two-credit-per-supervariable budget.

## 11. Hierarchical cross-block amplification

A level-`b` block contains `b` original rectangles, `2b` left and `2b` right
resources, and at least `b` designated credits. Pairing two level-`b` blocks and
using only cross matchings gives

\[
((2b)!)^2
\]

formal states.

Direct recapture removes at most `b` edges in each directional `K_(2b,2b)`.
At least `2b` deleted edges are necessary to eliminate every perfect matching.
If the non-designated unary graph has maximum degree `d`, every level-`b` block
has at most `4d` bad partners, independently of `b`.

Therefore every contradiction involving boundedly many states at any fixed
hierarchy level may be bypassed by one more amplification round. For every fixed
`k`, almost all rectangles may be organized into level-`2^k` blocks under sparse
unary degree.

This does not prove that some finite depth must succeed. It isolates a new
possible obstruction: an infinite-depth hierarchy of locally feasible blocks
whose geometric or weighted cost remains concentrated at every fixed level.

## 12. Current exact bottleneck

The missing conversion theorem is reduced to:

1. convert an ownership Hall/slack core, two-sided threshold gap, or score
   concentration surviving all four allocation interfaces;
2. convert a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch;
3. convert a unary endpoint resource with linear forbidden cross-block degree;
4. convert locally impossible hierarchical state sets or unary, binary, and
   residual weighted shadow concentrated at block-credit scale;
5. rule out or convert an infinite-depth feasible cross-block hierarchy for
   which no fixed amplification depth has diffuse paid completion;
6. convert a linear-congestion original binary-shadow dual packing or
   witness-line pencil;
7. construct source-admissible pool-compatible trades with `Xi` insertion cost
   below star/resource removal credit.

A successful conversion either produces the global allocation directly or
strictly decreases a nonnegative integer potential.

The branch does not prove the no-three-in-line conjecture.

## PP4 — Prime-gap transfer

### Status: PROVED UNDER PP2--PP3

A fixed positive constant times `m^0.525` patch width covers the published
backward prime-gap scale, with standard constant and rounding slack.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; STORED CERTIFICATES CHECKED FOR `2<=n<=10`

The eventual threshold and finite exception list depend on the missing PP3
conversion theorem.
