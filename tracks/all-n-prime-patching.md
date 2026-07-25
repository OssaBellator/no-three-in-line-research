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

## 4. Four controller-aware allocation interfaces

For macro `i`, movement label `A`, and refill label `B`, controller-cell defects
and same-slot anchor counts give deterministic nondegree upper bounds

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

The total same-slot anchor mass across all disjoint pools is `m^(2+o(1))`.
Combining it with the Hall rectangle rules out middle-density anchor ownership
failure. The anchor obstruction is a sublinear exceptional label cluster or a
nearly dead macro column.

## 5. Source-valid resource endpoint

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

## 6. Zero-unary Hall endpoint

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

## 7. Original binary-shadow congestion endpoint

A binary cover deletes at least one endpoint cell from every binary shadow pair.
Its cost is maximum old-row/old-column congestion.

The fractional minimum congestion has:

- factor-two integral rounding;
- an exact LP dual conflict packing;
- Hall inheritance under low-congestion deletion.

One nonaxis witness line has a congestion-one cover. A low-overlap family is also
absorbed. The remaining original binary-shadow cases are a linear-congestion
dual packing or a high-overlap witness-line pencil.

## 8. Recapture-line owner energy

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

Szemerédi--Trotter and a multiplicity split convert the latter into a positive
linear family of nonaxis lines. Every good line carries at least
`q^(1/3-delta)` resource-disjoint owner/replacement cells and
`q^(1-delta)` Hall-target cells, with total typed multiplicity `Omega(q^2)`.

## 9. Alternating rectangle extraction

Pair one owner/replacement cell and one Hall-target cell on a good line. Their
opposite rectangle diagonal lies off the line and has the opposite slope.

The line family supplies `Omega(q^3)` rectangle candidates. Every endpoint
resource occurs in only `O(q^2)` candidates, so a maximal four-resource matching
extracts

\[
\Omega(q)
\]

pairwise row/column-disjoint alternating rectangle blocks.

Rectangle extraction is closed.

## 10. Exact rectangle installation

Reserve the four endpoint resources of every block. Each rectangle has two
matching states, its line diagonal and cross diagonal. A residual perfect
matching on the unreserved resources plus one state from every block gives a
complete endpoint permutation.

For a fixed residual configuration:

- all no-three constraints form an exact binary CNF of rank at most three;
- exact controller-shadow change is a degree-at-most-two pseudo-Boolean cost.

In a superregular host, a small linear reservation leaves a residual perfect
matching. The residual matching may be chosen source-valid and, under diffuse
residual shadow, with base cost `o(h)` relative to rectangle credit `h`.

## 11. Paid rectangle selection

For independent rectangle states, a paid first moment succeeds when

\[
\sum_B\Pr(B)
+
\frac{\mathbb EC}{R_0}
<1.
\]

A variable local lemma succeeds when local bad-box mass is at most `1/24` and
the conditioned unary/binary cost is below the removal credit.

Unit preprocessing removes forced states. Ternary bad boxes have vanishing
density and may be removed on a growing subbank.

## 12. Signed Ramsey endpoint

Colour every variable pair by its complete forbidden-state signature

\[
\Sigma\subseteq\{0,1\}^2.
\]

Fixed-colour Ramsey gives a growing homogeneous subbank. Its paid capacity is
exact.

1. If `(1,1)` is allowed, the all-cross state is valid and protects one
   designated credit unit per rectangle.
2. If `(1,1)` is forbidden but `(0,0)` is allowed, every valid homogeneous
   assignment uses at most one cross-oriented rectangle. This is the exact
   credit-poor signature.
3. If both diagonal pairs are forbidden, three rectangles form an unsatisfiable
   core.

Dense all-cross conflict is geometric. A positive-density conflict graph gives a
linear star; witness classification yields a rich cross line or a large pencil
through one selected rectangle cell. Ramsey-homogeneous cliques collapse further
to a common cross line or a complete fixed-anchor secant design.

## 13. Diffuse paid-cost closure

For a cross-compatible all-cross bank:

- `o(K)` unary-shadow variables and `o(K^2)` binary-shadow edges contain a
  growing zero-cost subbank;
- total unary weight `o(K)` and binary weight `o(K^2)` contain a growing
  `o(K)`-cost subbank;
- a superregular residual perfect matching may be chosen simultaneously
  source-valid and low-cost by a paid spread first moment.

Therefore diffuse rectangle-dependent cost and diffuse residual base cost are
closed. Failure is a linear unary family, a quadratic binary family, residual
weighted shadow at rectangle-credit scale, a credit-poor signature, or a signed
geometric core.

## 14. Current exact bottleneck

The missing conversion theorem is reduced to:

1. convert an ownership Hall/slack core, a two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces;
2. convert a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch;
3. convert a credit-poor homogeneous rectangle signature, rich cross line or
   pencil, complete fixed-anchor secant design, or constant-size signed
   contradiction;
4. convert linear unary, quadratic binary, or residual weighted shadow
   concentration at rectangle-credit scale;
5. convert a linear-congestion original binary-shadow dual packing or
   witness-line pencil;
6. construct source-admissible pool-compatible trades with `Xi` insertion cost
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
