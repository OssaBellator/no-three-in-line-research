# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open.  This repository does **not** contain a complete proof.

A July 2026 result proves the corresponding eventual maximum `kn` for every
fixed `k>=3`; the saturated `k=2` case addressed here remains exceptional.

## Established platform

The notebook contains proved lemmas or exact conditional endpoints for:

- saturated two-per-row/column decomposition into two perfect-matching layers;
- clone-space, permutation, and superregular perfect-matching selection;
- protected rectangle, tomographic, cycle, subgroup, and endpoint trades;
- exact fixed- and variable-reservoir patch expectations;
- binary and multistate rank-at-most-three forbidden-box CSPs;
- weighted local-lemma and fixed-rank spread endpoints;
- modular-hyperbola, carry, quotient, gcd, and divisor structure;
- exact finite certificate verification and small exhaustive searches.

The principal non-prime-patching route still lacks its second-generation
alternating-bank concentration/termination theorem and final carry absorber.

## All-n prime-patching track

### Slab-optimal macro architecture

Every saturated source decomposes into two matching layers.  Consecutive
column-slab pools give

```text
macro variables M = m^(1/20+o(1))   = m^0.05
pool size R       = m^(19/20+o(1))  = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width MW    = m^(21/40+o(1))  = m^0.525.
```

The branch proves matching-pool supply, exact degree restoration, internally
no-three square-root macros, conditioned fixed-rank spread, and exponent
optimality within disjoint `O(sqrt(R))` macro architectures.

### Global labels and controller-aware domains

Every final numerical row and column must be used.  Balanced movement-label
ownership and one global refill matching provide a saturation-compatible
allocation.

The direct global endpoint is complementary degree.  For every incompatible
macro-label triple it is enough that

\[
\deg_{J_i}(A)+q_B
\ge
T+8\sqrt{T\log T},
\]

where `q_B` is the average refill-label degree over macro ownerships.

Fixed-core safety is insufficient because unselected pool edges remain in the
source.  Controller-aware safety tests blocker pairs against the full source and
allows only pairs cleared by deleting their own controller edge.

### External geometry is closed

At the slab-optimal scale, all remaining patch-only cross-macro events and all
ordinary two-slot source-anchor events have `o(1)` incident probability mass.
Thus controller-aware global allocation would complete an
`Omega(m^0.525)` saturated patch.

### Failure structure and dynamic potential

Positive controller shadow produces either:

1. a source-endpoint blocker star of size `Omega(m^0.475)`; or
2. `Omega(m^0.525)` resource-disjoint bad entries with distinct labels,
   controllers, and endpoint-disjoint blocker pairs.

Endpoint permutations preserve saturation.  Inside a fixed pool they also
preserve its old-column set, old-row set, and complete candidate-cell universe.
Every candidate cell has one automatic controller-containing axis blocker.
Therefore

\[
\Xi(S)=\sum_z\bigl(b_S(z)-1\bigr)
\]

is a nonnegative pairing-invariant excess-shadow potential.  Every pool-compatible
trade satisfies an exact insertion-cost-minus-removal-credit identity for `Xi`.
Uniform improving trades terminate automatically.

### Source-valid resource trades

A resource bank of size `Q=Omega(m^0.525)` may be thinned to

\[
q=m^\kappa,
\qquad
0<\kappa<\frac1{40}.
\]

Under sparse unary source shadow, superregular pruning, a permutation local
lemma, transition divisor regularisation, and support-rank thinning produce a
saturation-preserving no-three endpoint trade.  Source admissibility of this
resource trade is closed.

### Zero-unary Hall endpoint

Direct recapture cells and residual unary-shadow cells are deleted from one
source-safe endpoint host `G_0`.  A perfect matching in this host has zero unary
insertion shadow.  Failure gives an exact Hall rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

A macroscopic rectangle contains a quadratic core of one witness type.
Recapture-dominated rectangles produce linear banks of rich designated lines.

### Binary shadow is a congestion problem

Every binary conflict can be covered by deleting one of its two endpoint cells.
The fractional minimum resource congestion `tau^*(B)` has:

- factor-two threshold rounding to an integral unary cover;
- an exact LP dual weighted-conflict packing;
- Hall inheritance: a low-congestion cover cannot manufacture a new macroscopic
  Hall rectangle.

One nonaxis witness line is easy: its allowed trace is a matching, and all
conflicts assigned to that line have a congestion-one cover.  A family with
`o(q)` witness-line overlap is also absorbed.

The remaining binary objects are a linear-congestion fractional dual packing or
a linear pencil of distinct witness lines through common endpoint resources.

### Rich-line assignment energy

For owner-line loads `h_ij`, put

\[
H_0=\sum_i h_{ii},
\qquad
W_\mu=\sum_{(i,j)\text{ permitted}}h_{ij}.
\]

A source-valid endpoint distribution with one-cell spread `K/q` gives an
improving owner reassignment whenever

\[
\frac KqW_\mu<H_0.
\]

Failure produces a quadratic grid-rich assignment core and a linear compatible
matching of rich second-generation lines.

The one-survivor unary cover cannot replace this reconfiguration.  For `r`
distinct geometric witness lines with allowed traces `P_lambda`, every such cover
satisfies

\[
|C|
\ge
\frac{S^2}{S+r(r-1)},
\qquad
S=\sum_\lambda(|P_\lambda|-1).
\]

Hence a linear bank of linear-rich lines forces linear unary congestion.  This is
a proved barrier, not an open estimate.

### Direct allocation from geometric defect scores

Let `a_i(A)` and `b_i(B)` be movement/refill controller-cell defect counts and
let `u_i(A,B)` be same-slot anchor counts.  The compatibility-domain union bound
gives explicit row and column nondegree scores `rho_i(A)` and `kappa(B)`.
Direct allocation follows whenever every nonedge satisfies

\[
\rho_i(A)+\kappa(B)
\le
T-8\sqrt{T\log T}.
\]

Moreover, fixed labelwise margin together with

\[
\Xi_i=o(RT),
\qquad
\max_A U_i(A)=o(RT),
\qquad
\max_B\frac1M\sum_jV_j(B)=o(RT)
\]

already implies complementary degree and completes the patch.

Thus diffuse excess shadow is sufficient.  A direct failure must concentrate in
a nearly dead movement/refill label, a macro with `Omega(RT)` excess shadow, or a
same-slot anchor row/average-column of size `Omega(RT)`.

## What remains conditional

The remaining conversion theorem has the following concrete forms:

1. regularise the five explicit direct-allocation concentration objects;
2. convert a Hall rectangle or a matchable but non-superregular zero-unary host;
3. convert the second-generation grid-rich owner-line pencil;
4. convert a linear-congestion binary dual packing or witness-line pencil;
5. build source-admissible pool-compatible trades with
   `Xi` insertion cost below their star/resource removal credit.

Diffuse weighted residuals, external completion energy, source validity of the
resource endpoint, isolated rich fibres, raw binary-fan size, naive rich-line
covering, dynamic controller relabelling, and termination are no longer separate
open problems.

## Important cautions

- Unused numerical labels cannot be discarded and compressed while preserving
  saturation.
- Fixed-core domains do not handle unselected active-pool edges.
- A source-endpoint blocker star is not automatically a common-candidate star.
- A single rich line has bounded cover congestion, but a linear bank of
  linear-rich distinct lines need not.
- Finite diagnostics validate identities and expose obstructions; they do not
  prove the asymptotic conversion theorem.

## Bottom line

There is no complete proof.  The branch now closes matching supply, exponent-
optimal macro width, saturation-compatible allocation interfaces, external
weighted geometry, source-valid resource trades, binary low-congestion covering,
rich-line survivor barriers, direct geometric Ore scores, and monotone dynamic
shadow reduction.  The structured concentration cases above remain open.