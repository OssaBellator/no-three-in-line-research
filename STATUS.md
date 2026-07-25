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
- binary and multistate rank-at-most-three forbidden-box CSPs;
- weighted local-lemma and fixed-rank spread endpoints;
- modular-hyperbola, carry, quotient, gcd, divisor, Ramsey, and incidence
  structure;
- exact finite certificate verification and small exhaustive searches.

The principal non-prime-patching route still lacks its second-generation
alternating-bank concentration/termination theorem and final carry absorber.

## All-n prime-patching track

### Slab-optimal architecture

```text
macro variables M = m^(1/20+o(1))   = m^0.05
pool size R       = m^(19/20+o(1))  = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width MW    = m^(21/40+o(1))  = m^0.525.
```

Matching supply, degree restoration, internal macro geometry, fixed-rank spread,
and exponent optimality are proved.

### Controller-aware safety and external closure

Unselected active-pool edges remain in the source, so fixed-core safety is not
enough. Controller-aware domains test blockers against the full source.

At the slab-optimal scale, every remaining patch-only cross-macro class and every
ordinary two-slot source-anchor class has `o(1)` incident probability mass.
Any saturation-compatible controller-aware label allocation gives an
`Omega(m^0.525)` patch.

### Dynamic excess potential

Every candidate has one automatic controller-containing axis blocker. The
pairing-invariant excess potential

\[
\Xi(S)=\sum_z(b_S(z)-1)
\]

counts additional nonaxis blockers. Pool-compatible endpoint trades satisfy an
exact insertion-cost-minus-removal-credit identity. Uniform improving trades
terminate automatically.

## Four direct allocation interfaces

The branch has four independent global-label completion mechanisms:

1. one-sided movement ownership versus cumulative refill slack;
2. deterministic two-sided ownership with `r+s<=W`;
3. random two-sided ownership from per-macro complementary degree;
4. random one-sided ownership from average refill complementary degree.

At threshold `r`, balanced movement ownership exists exactly when

\[
W|N_M(X)|\ge|X|
\]

for every numerical-label set `X`. Failure gives an explicit all-bad
label-by-macro rectangle.

The total same-slot anchor energy is `m^(2+o(1))`, ruling out middle-density
anchor ownership failure. The remaining anchor object is a sublinear exceptional
label cluster or a nearly dead macro column.

## Source-valid endpoint trades

Adaptive endpoint thinning produces a growing bank with:

- no unary-invalid arc;
- no anchored transition;
- vanishing high-support source-invalid expectation;
- a fully source-valid derangement with one-cell probability `(1+o(1))/q`.

Source admissibility is closed in the sparse-unary endpoint branch.

## Hall, congestion, and rectangle extraction

After deleting direct recapture and residual unary-shadow cells, failure of the
source-safe endpoint host is exactly a Hall rectangle.

Binary shadow is governed by endpoint-resource congestion. The fractional cover
problem has factor-two rounding, an exact dual packing, and Hall inheritance.

A recapture-dominated Hall core yields a positive-density family of target-rich
repeated lines. Their two matching traces supply `Omega(q^3)` alternating
rectangle candidates and an `Omega(q)` pairwise row/column-disjoint rectangle
bank. Rectangle extraction is closed.

## Superregular rectangle installation

In the superregular branch:

- a small linear rectangle reservation leaves a residual perfect matching;
- the residual matching can be chosen source-valid and low-cost;
- all remaining geometry is an exact rank-at-most-three finite-state CSP;
- exact insertion shadow is a unary/binary finite-state cost;
- first-moment, local-lemma, and support-cleaning criteria close diffuse
  geometric and paid collateral.

## Cross-block signature bypass

The natural line and cross diagonals are not a terminal state space. Pair two
resource-disjoint rectangles and use only cells in the two cross resource blocks.
There are four equal-margin matching states. This bypasses every witness
supported solely on the original rectangle states.

The construction generalizes to growing blocks. Direct recapture alone cannot
kill the complete directional matching hosts, and signed or multistate
contradictions at any bounded level may be bypassed by a larger cross state
space.

## Unary-independent growing blocks

Let the rectangle bank have size `H`, and let the non-designated unary endpoint
graph have maximum degree `d=o(H)`.

Create a rectangle-interaction graph by joining two rectangles when a unary-
forbidden cell lies in either cross resource block. Its maximum degree is at most
`4d`. Properly colour it and split every independent colour class into growing
groups of size `b`, with `(d+1)b=o(H)`. Only `o(H)` rectangles are discarded.

Every group has zero non-designated unary edges internally. Split it into two
halves and use cross matchings. Direct recapture deletes at most `b/2` edges from
each directional `K_(b,b)`, so both hosts remain matchable.

After removing `o(b)` recapture-heavy rectangles, both directional hosts have
forbidden maximum degree `o(b)` and are near-complete superregular. Their product
matching distribution has fixed-rank probability `O(b^-r)` and retains
`(1-o(1))b` designated credits.

Therefore every sublinear unary-degree rectangle bank reduces to the explicit
paid spread inequality

\[
K^2\frac{P_b}{b^2}
+
K^3\frac{Q_b}{b^3}
+
\frac1{R_b}
\left(
K\frac{A_b}{b}
+
K^2\frac{B_b}{b^2}
\right)
<1.
\]

Arbitrary signed rectangle signatures, dense finite-state CSPs, bounded local
contradictions, irregular hierarchical state spaces, and infinite-depth
feasibility are no longer separate obstructions under sublinear unary degree.

## What remains conditional

The remaining conversion theorem has these structured forms.

1. Convert an ownership Hall/slack core, two-sided threshold gap, or score
   concentration surviving all four allocation interfaces.
2. Convert a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch.
3. Convert a unary endpoint resource with linear forbidden cross-block degree.
4. Convert source or shadow weights concentrated in the growing-block paid
   expression above.
5. Convert a linear-congestion original binary-shadow dual packing or
   witness-line pencil.
6. Build source-admissible pool-compatible trades with `Xi` insertion cost below
   star/resource removal credit.

## Important cautions

- Unused numerical labels cannot be discarded and compressed while preserving
  saturation.
- Fixed-core domains do not handle unselected active-pool edges.
- Unary-independent grouping does not cover linear unary maximum degree.
- Superregular residual theorems do not cover every matchable sparse host.
- The growing-block paid inequality is still conditional on its source/shadow
  weights.
- Finite diagnostics validate identities and expose obstructions; they do not
  prove the asymptotic conversion theorem.

## Bottom line

There is no complete proof. The branch closes matching supply, optimal macro
width, four allocation interfaces, external weighted geometry, source-valid
near-uniform endpoint trades, rectangle extraction, superregular residual
installation, arbitrary finite-state signature obstructions, and every
sublinear-unary rectangle hierarchy. The concentrated weighted, linear-unary,
non-superregular, original-binary, and dynamic-`Xi` cases remain open.
