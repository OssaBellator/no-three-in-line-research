# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

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
- modular-hyperbola, carry, quotient, gcd, divisor, Ramsey, and incidence
  structure;
- exact finite certificate verification and small exhaustive searches.

The principal non-prime-patching route still lacks its second-generation
alternating-bank concentration/termination theorem and final carry absorber.

## All-n prime-patching track

### Slab-optimal macro architecture

Every saturated source decomposes into two matching layers. Consecutive
column-slab pools give

```text
macro variables M = m^(1/20+o(1))   = m^0.05
pool size R       = m^(19/20+o(1))  = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width MW    = m^(21/40+o(1))  = m^0.525.
```

Matching-pool supply, exact degree restoration, internally no-three macros,
fixed-rank spread, and exponent optimality within disjoint square-root-macro
architectures are proved.

### Controller-aware safety and external closure

Unselected active-pool edges remain in the source, so fixed-core safety is not
enough. Controller-aware domains test every blocker against the full source and
permit a state only when its own controller deletion clears every unary source
obstruction.

At the slab-optimal scale, every remaining patch-only cross-macro class and every
ordinary two-slot source-anchor class has `o(1)` incident probability mass.
Any saturation-compatible controller-aware label allocation would therefore give
an `Omega(m^0.525)` patch.

### Dynamic excess-shadow potential

Every candidate cell has one automatic controller-containing axis blocker. The
pairing-invariant excess potential

\[
\Xi(S)=\sum_z(b_S(z)-1)
\]

counts the additional nonaxis blockers. Pool-compatible endpoint trades satisfy
an exact insertion-cost-minus-removal-credit identity. Uniform improving trades
terminate automatically.

## Four direct allocation interfaces

Controller-defect scores support four independent completion mechanisms.

1. One-sided movement ownership versus cumulative refill slack.
2. Deterministic balanced ownership on both label sides with `r+s<=W`.
3. Random two-sided ownership from per-macro complementary degree.
4. Random one-sided ownership from average refill complementary degree.

At threshold `r`, balanced movement ownership exists exactly when

\[
W|N_M(X)|\ge|X|
\]

for every numerical-label set `X`. Failure gives an explicit all-bad
label-by-macro rectangle.

The total same-slot anchor energy across all disjoint pools is `m^(2+o(1))`.
Combining it with the Hall rectangle eliminates middle-density anchor ownership
failure. The remaining anchor object is a sublinear exceptional label cluster or
a nearly dead macro column.

## Source-valid endpoint trades

A resource bank of size `Q=Omega(m^0.525)` may be thinned adaptively to a growing
bank with:

- no unary-invalid endpoint arc;
- no anchored two-step transition;
- vanishing high-support source-invalid expectation;
- a fully source-valid derangement with one-cell probability `(1+o(1))/q`.

Source admissibility of the endpoint trade is therefore closed in the sparse-
unary branch.

## Hall, line, and rectangle extraction

After deleting direct recapture and residual unary-shadow cells, failure of the
source-safe endpoint host is exactly a Hall rectangle.

Binary insertion shadow is governed by resource congestion. The fractional
cover problem has factor-two rounding, an exact dual packing, and Hall
inheritance under low-congestion deletion.

For a recapture-dominated Hall core, failed owner-line improvement gives a
positive-density family of target-rich repeated nonaxis lines. Pairing the two
matching traces on those lines produces `Omega(q^3)` alternating rectangle
candidates and an `Omega(q)` pairwise row/column-disjoint rectangle bank.
Rectangle extraction is closed.

## Superregular rectangle installation and paid selection

In the superregular branch:

- a small linear reservation leaves a residual perfect matching;
- the residual matching can be chosen source-valid and low-cost;
- every rectangle is an equal-margin two-state permutation block;
- all remaining geometric conditions form an exact binary rank-at-most-three
  CNF;
- exact insertion shadow is a unary/binary finite-state cost.

First-moment and variable-local-lemma criteria close diffuse clause mass and
diffuse insertion collateral.

## Cross-block signature bypass

The two natural rectangle diagonals are not a terminal state space. Pair two
resource-disjoint rectangles and use only cells in the two cross resource
blocks. There are exactly four such perfect-matching states.

Before general unary pruning, at least one state directly protects both
designated owner credits. After pruning, state existence is exactly two small
`2 by 2` Hall tests.

If the non-designated unary endpoint graph has maximum degree `d`, every
rectangle has at most `4d` bad partners. Thus `d=o(h)` allows almost the entire
bank of `h` rectangles to pair into source-safe four-state supervariables with
at least two credits each.

This bypass does not depend on the original binary signature. Under sparse unary
degree it removes as separate obstructions:

- credit-poor Boolean signatures;
- three-rectangle signed contradictions;
- dense all-cross conflict graphs;
- rich cross lines and pencils;
- complete fixed-anchor secant designs supported on the original cross cells.

All geometry is recomputed in the four-state cross-block space.

## Multistate Ramsey completion

After local-state pruning, only finitely many nonempty state alphabets remain.
Adaptive thinning removes ternary bad boxes on a growing subbank. Fixed-colour
Ramsey homogenizes the complete pair signature.

For an alphabet of at most four states:

- if some diagonal pair `(a,a)` is allowed, the all-`a` state satisfies every
  binary constraint;
- if every diagonal pair is forbidden, at most five variables already form a
  contradiction.

Diffuse state cost gives a strict improvement against the two-credit-per-block
removal budget.

## Hierarchical cross-block amplification

The cross-block construction iterates. A level-`b` block contains `b` original
rectangles, `2b` resources per side, and at least `b` designated credits.
Pairing two such blocks gives `((2b)!)^2` cross states.

Direct recapture removes at most `b` edges from each directional `K_(2b,2b)`.
At least `2b` edge deletions are needed to destroy every perfect matching.
With non-designated unary maximum degree `d`, a level-`b` block has at most
`4d` bad partners, independently of `b`.

Consequently every contradiction at any fixed hierarchy depth can be bypassed
under sparse unary degree. Failure at all fixed depths is a coherent
infinite-depth hierarchy of locally feasible blocks with concentrated geometry
or cost, not a finite local CSP obstruction.

## What remains conditional

The remaining conversion theorem has these structured forms.

1. Convert an ownership Hall/slack core, two-sided threshold gap, or score
   concentration surviving all four allocation interfaces.
2. Convert a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch.
3. Convert a unary endpoint resource with linear forbidden cross-block degree.
4. Convert locally impossible hierarchical cross-block state sets or unary,
   binary, and residual weighted shadow concentrated at block-credit scale.
5. Rule out or convert an infinite-depth feasible cross-block hierarchy for
   which no fixed amplification depth admits diffuse paid completion.
6. Convert a linear-congestion original binary-shadow dual packing or
   witness-line pencil.
7. Build source-admissible pool-compatible trades with `Xi` insertion cost below
   star/resource removal credit.

## Important cautions

- Unused numerical labels cannot be discarded and compressed while preserving
  saturation.
- Fixed-core domains do not handle unselected active-pool edges.
- Sparse-unary cross-block results do not cover a resource with linear unary
  forbidden degree.
- Superregular residual results do not cover every matchable sparse host.
- Fixed-depth amplification does not prove eventual success of the hierarchy.
- Finite diagnostics validate identities and expose obstructions; they do not
  prove the asymptotic conversion theorem.

## Bottom line

There is no complete proof. The branch closes matching supply, exponent-optimal
macro width, four global allocation interfaces, external weighted geometry,
source-valid near-uniform endpoint trades, rectangle extraction, superregular
residual installation, signed and multistate CSP regularization, diffuse paid
selection, and every bounded-depth diagonal-signature contradiction under sparse
unary degree. The structured concentration and infinite-depth cases above remain
open.
