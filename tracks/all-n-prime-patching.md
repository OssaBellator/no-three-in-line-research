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

### Status: OPEN, reduced to structured concentration conversion

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

Positive controller-cell failure produces either:

1. a source-endpoint blocker star of size `Omega(m^0.475)`; or
2. `Omega(m^0.525)` resource-disjoint bad entries with distinct labels,
   controllers, and endpoint-disjoint blocker pairs.

Within-pool endpoint permutations preserve the pool coordinate sets and full
candidate-cell universe. Every candidate has one automatic controller-containing
axis blocker, so

\[
\Xi(S)=\sum_z(b_S(z)-1)
\]

counts exactly the additional nonaxis blockers. Pool-compatible trades satisfy
an exact insertion-cost-minus-removal-credit identity. Any uniform improving
trade theorem terminates automatically.

## 4. Controller-defect scores

For macro `i`, movement label `A`, and refill label `B`, the branch defines
controller-cell defects `a_i(A),b_i(B)` and same-slot anchor counts `u_i(A,B)`.
They give deterministic nondegree upper bounds

\[
\overline d_i(A)\le\rho_i(A),
\qquad
\overline e_i(B)\le\chi_i(B).
\]

The average refill score is `kappa(B)`. These quantities connect geometric
controller shadow directly to the label-allocation graphs.

## 5. One-sided bottleneck and refill slack

A balanced movement ownership assigns exactly `W` numerical movement labels to
each macro. Its score bottleneck is

\[
r_{\rm score}
=
\min_\sigma\max_A\rho_{\sigma(A)}(A).
\]

For refill label `B`, define cumulative local slack

\[
\Lambda_{\rm score}(B)
=
\sum_i(W-\chi_i(B))_+.
\]

The global allocation exists whenever

\[
\boxed{
r_{\rm score}
\le
\min_B\Lambda_{\rm score}(B).
}
\]

At a fixed threshold `r`, ownership is possible exactly when

\[
W|N_M(X)|\ge|X|
\]

for every movement-label set `X`. Failure gives an exact capacitated Hall set and
an all-bad label-by-macro rectangle.

Under a fixed refill-label margin,

\[
\Lambda_{\rm score}(B)
\ge
T-
\frac{
\sum_iA_i+\sum_iV_i(B)
}{\delta R}.
\]

Thus global excess-shadow and same-slot anchor mass, rather than the worst single
macro, control the refill side.

## 6. Two-sided label ownership

A symmetric architecture assigns exactly `W` movement and `W` refill labels to
every macro before matching them.

If the movement and refill ownership thresholds satisfy

\[
\boxed{r+s\le W,}
\]

then every induced `W by W` macro graph satisfies the bipartite Ore criterion and
has a perfect matching.

The two ownership maps have independent exact capacitated Hall criteria. Sparse
exceptional labels can therefore be routed away from their bad macros on both
sides.

## 7. Random allocation alternatives

Two probabilistic interfaces remain available.

### Random two-sided local Ore

Independent uniform balanced partitions sample each global nondegree down by
`W/T`. Allocation follows if every macro nonedge satisfies

\[
\rho_i(A)+\chi_i(B)
\le
T-h,
\]

where one may take

\[
h=2T\sqrt{\frac{\log(4MT)}W}
=m^{23/80+o(1)}.
\]

### Random one-sided complementary degree

The earlier ownership theorem completes whenever every incompatible triple
satisfies

\[
\rho_i(A)+\kappa(B)
\le
T-8\sqrt{T\log T}.
\]

A direct allocation failure must therefore survive four mechanisms:
one-sided bottleneck/slack, deterministic two-sided ownership, random two-sided
local Ore, and random one-sided average refill degree.

## 8. Source-valid resource endpoint

A resource bank of size `Q=Omega(m^0.525)` may be thinned to a growing subbank.
Under sparse unary source shadow, endpoint-host pruning, a permutation local
lemma, divisor regularisation, and support-rank thinning produce a saturation-
preserving no-three endpoint trade.

The thinning may be chosen adaptively so that the retained bank has:

- no unary-invalid endpoint arc;
- no anchored two-step transition;
- vanishing high-support source-invalid expectation;
- a fully source-valid derangement with one-cell probability `(1+o(1))/q`.

Source admissibility is closed with a near-uniform law.

## 9. Zero-unary Hall endpoint

Delete designated recapture cells and residual unary-shadow cells from the
source-safe endpoint host. Call the result `G_0`.

Every perfect matching of `G_0` has zero unary insertion shadow. Failure is
exactly a Hall rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

A macroscopic rectangle contains a quadratic core of one witness type.
Recapture-dominated rectangles produce dense target sets supported by designated
owner lines.

## 10. Binary congestion endpoint

A binary cover deletes at least one endpoint cell from every binary shadow pair.
Its cost is maximum old-row/old-column congestion.

The fractional minimum congestion has:

- factor-two integral rounding;
- an exact LP dual conflict packing;
- Hall inheritance under low-congestion deletion.

One nonaxis witness line has a congestion-one cover. A low-overlap family of
witness lines is also absorbed. The remaining binary cases are a linear-
congestion fractional dual packing or a high-overlap witness-line pencil through
common endpoint resources.

## 11. Rich-line owner energy

For owner-line loads `h_ij`, put

\[
H_0=\sum_i h_{ii},
\qquad
\mathcal W=\sum_{i,j}h_{ij}.
\]

Naive line-by-line deletion cannot solve a linear bank of linear-rich distinct
geometric lines: survivor-cover volume forces linear resource congestion.

Adaptive thinning preserves a positive-density Hall target set while removing
all low-support source-invalid events. Under the resulting source-valid
near-uniform derangement, either the owner-line potential strictly decreases or

\[
H_0=(1+o(1))|\mathcal A|,
\qquad
\mathcal W=(1-o(1))q|\mathcal A|.
\]

The latter is an incidence-extremal design. Szemerédi--Trotter forces one
nonaxis geometric line with

\[
\Omega(q^{1/3})
\]

pairwise resource-disjoint owner/replacement endpoint cells and their owner
candidate points.

The former second-generation grid-rich pencil is therefore reduced to one common
geometric carrier.

## 12. Current exact bottleneck

The missing conversion theorem is reduced to:

1. convert an ownership Hall/slack core, a two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces;
2. convert a Hall rectangle or matchable but non-superregular zero-unary host
   outside the recapture-line class;
3. convert the common nonaxis line matching from PP3oc;
4. convert a linear-congestion binary dual packing or witness-line pencil;
5. construct source-admissible pool-compatible trades with `Xi` insertion cost
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
