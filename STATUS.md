# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

\[
 D(n)=2n
\]

remains open.  A July 2026 paper proves the analogous maximum `kn` for every
fixed `k>=3` and sufficiently large `n`, while leaving `k=2` as the exceptional
case.

This repository does **not** contain a complete proof.

## Established platform

The notebook contains complete proofs or exact conditional endpoints for:

- saturated two-per-row/column decomposition into permutation layers;
- clone-space and superregular perfect-matching selection;
- protected tomographic, cycle, subgroup, rectangle, and endpoint-permutation
  trade banks;
- modular-hyperbola, Möbius, carry, quotient, coset, gcd, and divisor structure;
- exact fixed- and variable-reservoir patching expectations;
- binary and multistate rank-at-most-three forbidden-box CSPs;
- first-moment, occurrence, and weighted-probability local-lemma criteria;
- exact finite certificate verification and exhaustive small searches.

The principal non-prime-patching route still lacks a second-generation
alternating-bank concentration/termination theorem and a monotone carry
potential or bounded-denominator absorber.

## All-n prime-patching track

### Exact degree and transfer interfaces

The branch proves the boundary and arbitrary-reservoir degree bookkeeping,
delete-and-restore selection endpoints, and the prime-gap transfer theorem under
a sufficiently wide absorber.  The published backward prime-gap exponent
requires a fixed positive multiple of `m^0.525`, with the usual constant and
rounding slack.

### Matching supply

Every saturated source decomposes into two perfect matching layers.  Uniform
subsets give exact hypergeometric matching reservoirs.  Independent old-column
and old-row template sampling cannot have constant matching-admissible density at
sublinear width, so matching coordinates must be correlated through source
edges.

### Slab-optimal square-root macro geometry

The product-LLL macro construction does not require monotone endpoint order.
Using consecutive column-slab pools permits the exponent-optimal balance

```text
macro variables M = m^(1/20+o(1))  = m^0.05
pool size R       = m^(19/20+o(1)) = m^0.95
macro width W     = m^(19/40+o(1)) = m^0.475
total width MW    = m^(21/40+o(1)) = m^0.525.
```

The branch proves:

- enough pairwise disjoint slab matching pools;
- exact equal-margin row/column restoration;
- internally no-three square-root macro patches by a product local lemma;
- conditioned fixed-rank cylinder spread `O(R^-q)`;
- optimality of the `m^0.05` macro-count exponent within any disjoint
  `W=Theta(sqrt(R))` architecture.

### Coordinate correction and global allocation

A numerical candidate label is an actual final row or column.  Selecting only
`W<L` labels from an `L`-coordinate interval and leaving the others empty does
**not** preserve saturation; arbitrary label compression does not preserve
collinearity.  The valid replacement uses all

\[
 T=MW
\]

final new rows and all `T` final new columns.  A balanced ownership assigns every
movement label to one macro, and one global refined perfect matching assigns
every refill label exactly once.

The strongest direct allocation criterion is complementary degree.  For every
incompatible triple `(i,A,B)`, it is sufficient that

\[
 \deg_{J_i}(A)+q_B
 \ge
 T+O(\sqrt{T\log T}),
\]

where `q_B` is the average refill degree across the macro graphs.  This strictly
weakens separate `T/2` minimum-degree requirements.

### Controller-aware source safety

Fixed-core safety is not enough for an active matching pool: unselected pool
edges remain in the source.  The correct unary domain consists of source-edge
values whose movement and refill cells have no blocker pair disjoint from the
selected controller edge, and whose same-slot movement/refill pair has no
retained source anchor.

If the controller-aware graphs admit the global allocation, every unary
retained-pair and same-slot anchor certificate is removed value by value.

### Weighted external geometry is closed at the slab scale

All anchors or geometric witnesses producing the same forbidden slot-value
pattern are grouped into one event.  The weighted local lemma charges total
incident probability rather than raw event count.

At the slab-optimal exponents, the branch now proves:

- every patch-only cross-macro rank-two event has total incident mass `o(1)`;
- all-movement and all-refill rank-three mass is `o(1)` by gcd sums;
- every mixed rank-three class is `o(1)` by divisor factorization;
- every ordinary two-slot source-anchor class is `o(1)` by congruence and
  divisor-square sums.

Therefore, once controller-aware global allocation is available, the weighted
endpoint produces the full `m^0.525` patch.  Cross-macro completion energy is no
longer a separate bottleneck.

### Structure forced by controller-shadow failure

A fixed source secant can witness at most one movement candidate per new row and
one refill candidate per new column.  Consequently, positive-density failure of
controller-aware safety forces one of:

1. a blocker star with `m^0.475` distinct rays; or
2. `m^0.525` resource-disjoint bad entries with distinct new labels, controller
   edges, and endpoint-disjoint blocker pairs.

The second alternative contains a matching-layer endpoint bank.  Permuting its
row endpoints preserves saturation and removes every selected blocker endpoint.
The controller-shadow potential has an exact removal-credit minus insertion-cost
identity.  Uniform derangements give a rank-three spread first-moment endpoint
for source validity and collateral.

## What remains conditional

The prime-patching track now lacks one conversion theorem.

- **Direct form:** prove the controller-aware global label graphs satisfy the
  complementary-degree allocation criterion.
- **Structured form:** when density fails, use the blocker-star or resource-bank
  alternative to construct a source-admissible endpoint, rectangle, or
  tomographic trade whose inserted shadow is below its paid removal credit.

The older constant-width width-two route remains a secondary diagnostic and
requires blocker-endpoint clustering or protected cross-block deletion trades.

## Important refutations and finite barriers

- Constant-density candidate pruning cannot overcome the candidate-only
  `Omega(n^4 log n)` triple population.
- Repeated boundary-only one-strip extension fails before side five.
- The unrestricted row-lift bank is not automatically clean.
- Aligned off-diagonal block doubling is impossible at every width.
- Independent sheared row/column boxes cannot have constant matching density at
  sublinear width.
- Canonical matching-block cleanliness is not universal.
- Independent constant-width deletion does not cover non-axis blockers at
  prime-gap scale.
- Unary blocker-cover domains are empty on both stored matching layers from side
  seven through ten.
- Every stored raw two-block width-two partition at sides eight through ten
  fails before patch-patch interactions.
- Unused numerical label coordinates cannot be discarded while claiming a
  smaller saturated grid.
- Fixed-core safe domains do not by themselves handle blocker pairs using
  unselected active-pool edges.

## Bottom line

There is no complete proof.  The prime-patching branch now closes matching-pool
supply, exponent-optimal prime-gap-scale internal macro width, degree
restoration, fixed-rank spread, saturation-compatible global allocation
interfaces, and all weighted rank-two/rank-three completion energy.

The exact remaining theorem is controller-shadow density or
collateral-controlled conversion of its forced star/resource structures.  Until
that theorem is proved, the branch does not prove the no-three-in-line
conjecture.
