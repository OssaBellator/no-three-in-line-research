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

1. a source-endpoint blocker star with `Omega(m^0.475)` distinct rays;
2. `Omega(m^0.525)` resource-disjoint bad entries with distinct labels and
   controllers and endpoint-disjoint blocker pairs.

Endpoint permutations preserve saturation and satisfy exact
removal-credit-minus-insertion-cost identities. Uniformly improving trades are
controlled by nonnegative integer potentials, so no separate recurrence argument
is needed once conversion is proved.

### Resource-bank source validity is closed

Assume the resource endpoint rectangle has unary forbidden density `o(1)`. Thin
its `Q=Omega(m^0.525)` endpoints to

\[
q=m^\kappa,
\qquad
0<\kappa<\frac1{40}.
\]

The branch then constructs a saturation-preserving no-three endpoint permutation
using superregular pruning, a permutation local lemma, divisor regularisation of
anchored transitions, and support-rank thinning of all remaining source
certificates. Source admissibility is therefore no longer part of the
resource-bank bottleneck.

### Zero-unary-shadow endpoint

Direct designated-credit recapture cells and every cell with positive residual
unary insertion shadow may be removed from the endpoint host before selection.
Call the resulting source-safe graph `G_0`.

Every perfect matching of `G_0` has zero unary insertion shadow and preserves the
designated credit. If `G_0` has no perfect matching, Hall's theorem gives exact
sets `X,Y` satisfying

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

A macroscopic Hall rectangle contains a quadratic core of one witness type. In
the recapture case this yields a linear bank of designated lines, each meeting
the endpoint rectangle in linearly many cells.

If `G_0` is superregular and its remaining anchored-pair, binary-shadow-pair, and
inserted-triple counts are summable, a spread perfect matching produces a
source-admissible trade with complete insertion cost zero.

### Isolated support concentrations are prunable

Deleting `o(q)` exceptional endpoint indices retains `(1-o(1))q` designated
credit units and can only decrease every source and shadow support. Persistent
failure forces a linear support core:

- `Omega(q^2)` simple unary support; or
- `Omega(q^3)` binary conflict support.

The cubic binary core yields either a linear endpoint-cell fan with candidate-line
structure or a linear family of resource-disjoint binary conflicts.

### Dynamic pool excess-shadow potential

For each fixed pool, the complete candidate-cell universe depends only on its old
column set and old row set, not on the current matching between them. Within-pool
endpoint permutations therefore preserve this universe even when controller
pairings change.

Every movement or refill candidate has exactly one automatic horizontal or
vertical blocker pair, and that pair contains its current controller point.
Every additional blocker pair is nonaxis and controller-disjoint. Hence

\[
\Xi(S)=\sum_z\bigl(b_S(z)-1\bigr)
\]

is a nonnegative integer counting exactly the excess cell-shadow incidences.
The number of bad cell entries is at most `Xi`.

Pool-compatible endpoint permutations satisfy an exact
`insertion cost - removal credit` identity for `Xi`. A star centre inside a
controller pool supplies its full linear blocker credit while the pool's column
set, row set, and candidate cells remain fixed.

For every fixed density threshold, a uniform improving pool-compatible trade
terminates below that threshold. A uniform threshold sequence tending to zero
gives `o(1)` bad cell-entry density, and improvement whenever `Xi>0` terminates
at `Xi=0`.

The earlier apparent controller-relabelling obstruction for captive star centres
is therefore removed. Their remaining difficulty is geometric: construct a
source-admissible within-pool endpoint trade whose `Xi` insertion cost is below
the star credit.

## What remains conditional

The remaining theorem is concentrated in the following structural endpoints:

- **direct allocation:** prove the controller-aware global label graphs satisfy
  the complementary-degree criterion;
- **unary Hall conversion:** convert a forbidden Hall rectangle or a matchable
  but non-superregular zero-unary endpoint host;
- **recapture-line conversion:** convert the linear tomographic bank of rich
  designated lines;
- **binary-core conversion:** neutralize the endpoint-cell fan or the
  resource-disjoint binary conflict bank;
- **pool-compatible paid conversion:** construct source-admissible within-pool
  endpoint trades with excess-shadow insertion cost below the star/resource
  removal credit.

Diffuse weighted residuals, endpoint source validity, isolated rich fibres,
dynamic controller relabelling, cross-macro completion energy, and termination
are no longer separate open problems.

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
- A source-endpoint blocker star is not automatically a common-candidate
  alternating star.

## Bottom line

There is no complete proof. The prime-patching branch now closes matching supply,
exponent-optimal macro width, degree restoration, fixed-rank spread,
saturation-compatible global allocation interfaces, all external weighted
completion energy, source-valid resource endpoint conversion, diffuse insertion
shadow, exact unary Hall reduction, sublinear support pruning, binary-fan
localisation, and pairing-invariant excess-shadow termination.

The exact remaining theorem concerns direct allocation, Hall or tomographic-line
conversion, binary-fan/resource-bank conversion, and source-admissible
pool-compatible paid trades. Until those cases are closed, the branch does not
prove the no-three-in-line conjecture.
