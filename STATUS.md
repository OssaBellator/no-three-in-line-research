# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. A July 2026 paper proves the analogous maximum `kn` for every
fixed `k>=3` and sufficiently large `n`, while leaving `k=2` exceptional.

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

### Prime-gap-scale macro architecture

Every saturated source decomposes into two perfect matching layers. Consecutive
column-slab pools give the exponent-optimal disjoint square-root-macro balance

```text
macro variables M = m^(1/20+o(1))   = m^0.05
pool size R       = m^(19/20+o(1))  = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width MW    = m^(21/40+o(1))  = m^0.525.
```

The branch proves universal matching-pool supply, exact degree restoration,
internal no-three macro geometry, conditioned fixed-rank spread, and optimality
of these exponents among disjoint `O(sqrt(R))` macro architectures.

### Global labels and controller-aware safety

Every final numerical row and column must be used. Balanced movement-label
ownership and one global refined perfect matching provide a saturation-compatible
allocation. The strongest direct criterion is complementary degree:

\[
\deg_{J_i}(A)+q_B
\ge
T+O(\sqrt{T\log T})
\]

for every incompatible `(i,A,B)`, where `q_B` is the average refill degree.

Fixed-core safety is insufficient because unselected active-pool edges remain in
the source. The correct controller-aware domain permits a value only when every
blocker pair through either inserted cell contains its selected controller edge,
which is deleted, and when its same-slot movement/refill pair has no retained
source anchor.

### External macro geometry is closed

At the slab-optimal scale, the branch proves `o(1)` incident probability mass for
all remaining external classes:

- cross-macro patch pairs;
- pure movement and pure refill triples;
- mixed patch triples;
- ordinary two-slot source-anchor pairs.

Thus controller-aware global allocation alone would give the required
`Omega(m^0.525)` saturated no-three patch.

### Failure structure and monotone trades

Positive-density controller-aware failure forces one of:

1. a blocker star with `Omega(m^0.475)` distinct rays;
2. `Omega(m^0.525)` resource-disjoint bad entries with distinct labels and
   controllers and endpoint-disjoint blocker pairs.

Endpoint permutations preserve saturation and satisfy an exact
removal-credit-minus-insertion-cost identity. Every successful paid trade
strictly decreases a fixed nonnegative integer controller-shadow potential while
preserving the controller pools, so a uniform conversion theorem terminates
automatically.

### Resource-bank source validity is closed

Assume the resource endpoint rectangle has unary forbidden density `o(1)`. Thin
its `Q=Omega(m^0.525)` endpoints to

\[
q=m^\kappa,
\qquad
0<\kappa<\frac1{40}.
\]

The branch then constructs a saturation-preserving no-three endpoint permutation
using:

- superregular endpoint-host pruning;
- a permutation local lemma for unary cells, transpositions, directed
  transitions, and directed 3-cycles;
- a divisor factorization for anchored transitions;
- support-rank thinning for rank-four anchored pairs and all higher-support
  inserted triples.

Source admissibility is therefore no longer part of the resource-bank
bottleneck.

### Diffuse insertion shadow is closed exactly

The `q` designated removal-credit incidences may be protected from direct
recapture by forbidding a union of endpoint partial matchings.

After that, forbid every endpoint cell with any positive residual unary shadow
and every compatible endpoint-cell pair with any positive residual binary
shadow. If the simple support degrees satisfy

\[
\boxed{
d_{\rm rec}+d_1=o(q),
\qquad
d_2=o(q^2),
}
\]

the permutation local lemma produces a source-admissible endpoint trade with

\[
\mathcal I=0.
\]

The positive removal credit then gives a strict potential decrease. Witness
multiplicity is irrelevant: each positive support is forbidden once.

## What remains conditional

The remaining theorem is support-concentrated controller-shadow conversion.
One must prove at least one of the following routes closes every case:

- **direct allocation:** the controller-aware global label graphs satisfy the
  complementary-degree criterion;
- **blocker-star conversion:** an alternating, endpoint, rectangle, cycle, or
  tomographic trade improves the forced star;
- **resource concentration conversion:** handle a dense unary endpoint source
  shadow, rich designated-credit recapture fibre, unary insertion-shadow fibre,
  or binary insertion-shadow star.

Diffuse weighted residuals, endpoint source validity, cross-macro completion
energy, and termination are no longer open.

The older constant-width width-two route remains a secondary diagnostic and
requires blocker-endpoint clustering or protected cross-block deletion trades.

## Important refutations and finite barriers

- Candidate-only constant-density pruning cannot beat the
  `Omega(n^4 log n)` triple population.
- Repeated boundary-only one-strip extension fails before side five.
- The unrestricted row-lift bank is not automatically clean.
- Aligned off-diagonal block doubling is impossible at every width.
- Independent sheared row/column boxes cannot have constant matching density at
  sublinear width.
- Independent constant-width deletion does not cover nonaxis blockers at the
  prime-gap scale.
- Unused numerical labels cannot be discarded while claiming a smaller
  saturated grid.
- Fixed-core safe domains do not handle blocker pairs using unselected
  active-pool edges.

## Bottom line

There is no complete proof. The prime-patching branch now closes matching supply,
exponent-optimal macro width, degree restoration, fixed-rank spread,
saturation-compatible global allocation interfaces, all external weighted
completion energy, source-valid resource endpoint conversion, diffuse insertion
shadow, and monotone termination.

The exact remaining theorem concerns only the direct, blocker-star, and four
support-concentrated resource alternatives above. Until that theorem is proved,
the branch does not prove the no-three-in-line conjecture.