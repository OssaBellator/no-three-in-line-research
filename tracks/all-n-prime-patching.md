# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
prime-minus-one sides and asks for an exact row-column-preserving patch from side
`m` to side `m+t`.  The patch must add `2t` net points, leave exactly two points
in every old and new row and column, and create no collinear triple.

The active theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).

## PP1 — Degree interface

### Status: PROVED

Boundary and arbitrary-reservoir degree states are classified.  Matching-edge
deletions and movement/refill insertions restore exact old and new row/column
margins.  Degree bookkeeping is closed.

## PP2 — Selection interfaces

### Status: PROVED AS IMPLICATIONS

The branch contains clone-space local lemmas, deletion-aware expectations,
finite-state CSPs, 2-SAT/CNF endpoints, weighted local lemmas, and spread
perfect-matching selection.  The unresolved work is geometric preparation.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to structured concentration conversion

## 1. Slab-optimal architecture

Every saturated source decomposes into two perfect matching layers.  Consecutive
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

Balanced label maps restore exact saturation.  Product-space local lemmas give
internally no-three macros with fixed-rank `O(R^-r)` spread.

## 2. Saturation-compatible global allocation

Use exactly the final `T` new rows and `T` new columns.  A balanced ownership map
assigns `W` movement labels to each macro, and one global perfect matching uses
every refill label exactly once.

For macro graph `J_i` and average refill degree `q_B`, allocation follows if every
incompatible triple satisfies

\[
\deg_{J_i}(A)+q_B
\ge
T+8\sqrt{T\log T}.
\]

This is the complementary-degree endpoint PP3gl.

## 3. Controller-aware safety

Unselected matching-pool edges remain in the source.  A candidate value is safe
only when every blocker pair through its movement/refill cell contains its
controller edge, which is deleted, and its same-slot movement/refill pair has no
retained source anchor.

At the slab-optimal exponents, every remaining patch-only cross-macro class and
every ordinary two-slot source-anchor class has `o(1)` incident probability mass.
Thus controller-aware global allocation alone completes an
`Omega(m^0.525)` patch.

## 4. Dynamic excess shadow

Positive controller-cell failure produces either:

1. a source-endpoint blocker star of size `Omega(m^0.475)`; or
2. `Omega(m^0.525)` resource-disjoint bad entries with distinct labels,
   controllers, and endpoint-disjoint blocker pairs.

Within-pool endpoint permutations preserve the pool coordinate sets and the full
candidate-cell universe.  Every candidate has one automatic controller-containing
axis blocker, so

\[
\Xi(S)=\sum_z(b_S(z)-1)
\]

counts exactly the additional nonaxis blockers.  Pool-compatible trades satisfy
an exact insertion-cost-minus-removal-credit identity.  Any uniform improving
trade theorem terminates automatically.

## 5. Source-valid resource endpoint

A resource bank of size `Q=Omega(m^0.525)` may be thinned to

\[
q=m^\kappa,
\qquad
0<\kappa<\frac1{40}.
\]

Under sparse unary source shadow, endpoint-host pruning, a permutation local
lemma, divisor regularisation, and support-rank thinning produce a saturation-
preserving no-three endpoint trade.  Source admissibility is closed in this
regime.

## 6. Zero-unary Hall endpoint

Delete designated recapture cells and residual unary-shadow cells from the
source-safe endpoint host.  Call the result `G_0`.

Every perfect matching of `G_0` has zero unary insertion shadow.  Failure is
exactly a Hall rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

A macroscopic rectangle contains a quadratic core of one witness type.
Recapture-dominated rectangles produce linear banks of rich designated lines.

## 7. Binary congestion endpoint

A binary cover deletes at least one endpoint cell from every binary shadow pair.
Its cost is maximum old-row/old-column congestion.

The fractional minimum congestion has:

- factor-two integral rounding;
- an exact LP dual conflict packing;
- Hall inheritance under low-congestion deletion.

One nonaxis witness line has a congestion-one cover.  A low-overlap family of
witness lines is also absorbed.  The remaining binary cases are a linear-
congestion fractional dual packing or a linear witness-line pencil through common
endpoint resources.

## 8. Rich-line owner energy and survivor barrier

For owner-line loads `h_ij`, define

\[
H_0=\sum_i h_{ii},
\qquad
W_\mu=\sum_{(i,j)\text{ permitted}}h_{ij}.
\]

A source-valid spread endpoint permutation improves the line-incidence potential
whenever

\[
\frac KqW_\mu<H_0.
\]

Failure produces a quadratic grid-rich owner/replacement core and a linear
compatible matching of second-generation rich lines.

Naive line-by-line unary deletion cannot solve that core.  For `r` distinct
geometric lines, one survivor per allowed trace gives

\[
|C|
\ge
\frac{S^2}{S+r(r-1)},
\qquad
S=\sum_\lambda(|P_\lambda|-1).
\]

Hence a linear bank of linear-rich lines forces linear unary congestion.  The
owner lines must be moved or neutralised by a genuine rectangle/tomographic
trade.

## 9. Direct controller-defect scores

For movement/refill cell defects `a_i(A),b_i(B)` and same-slot anchor counts
`u_i(A,B)`, PP3ly gives explicit nondegree scores `rho_i(A),kappa(B)`.

Direct allocation follows when every nonedge satisfies

\[
\rho_i(A)+\kappa(B)
\le
T-8\sqrt{T\log T}.
\]

A fixed labelwise domain margin and

```text
Xi_i=o(RT),
max_A U_i(A)=o(RT),
max_B average_i V_i(B)=o(RT)
```

already imply the criterion.  Thus diffuse shadow is sufficient.  A direct
failure must contain one of five concentration objects:

1. a nearly dead movement label;
2. a nearly dead refill label;
3. `Omega(RT)` excess shadow in one macro;
4. `Omega(RT)` same-slot anchor mass in one movement row;
5. `Omega(RT)` average same-slot anchor mass in one refill column.

## 10. Current exact bottleneck

The missing conversion theorem is now reduced to:

1. regularise the five direct-allocation concentrations;
2. convert a Hall rectangle or matchable but non-superregular zero-unary host;
3. convert the second-generation grid-rich owner-line pencil;
4. convert a linear-congestion binary dual packing or witness-line pencil;
5. construct source-admissible pool-compatible trades with
   `Xi` insertion cost below star/resource removal credit.

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