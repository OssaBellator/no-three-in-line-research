# Status and honesty ledger

**Last updated:** 24 July 2026

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
- protected tomographic, cycle, subgroup, and rectangle trade banks;
- modular-hyperbola, Möbius, carry, quotient, coset, and divisor structure;
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

### Square-root macro geometry

At the balanced exponents

```text
macro variables M = m^(23/80+o(1)) = m^0.2875
pool size R       = m^(19/40+o(1)) = m^0.475
macro width W     = Theta(sqrt R)  = m^0.2375
total width MW    = m^(21/40+o(1)) = m^0.525.
```

The branch proves universally:

- enough pairwise disjoint matching pools;
- exact equal-margin row/column restoration;
- internally no-three square-root macro patches by a product local lemma;
- conditioned fixed-rank cylinder spread `O(R^-q)`;
- random balanced coupling that disperses the same-edge movement/refill pair.

### Source cleaning

Dense movement/refill edge domains remove fixed-pair patch-cell blockers.  The
remaining same-edge anchored class has the exact factorization

\[
 (A-v)(B-u)=(x-u)(y-v),
\]

so label-dependent domain pruning removes it whenever a refined compatibility
matching exists.  Boundary-shadow, Hall, exact bad-label incidence, and divisor
energy give explicit success or concentration alternatives.

### Coordinate correction and global allocation

A numerical candidate label is an actual final row or column.  Selecting only
`W<L` labels from an `L`-coordinate interval and leaving the others empty does
**not** preserve saturation; arbitrary label compression does not preserve
collinearity.  The earlier informal “unused labels are free” shortcut is
refuted.

The valid replacement uses all

\[
 T=MW
\]

final new rows and all `T` final new columns.  A balanced ownership assigns every
movement label to one macro, and one global refined perfect matching assigns
every refill label exactly once.  A minimum-degree endpoint and a random balanced
ownership concentration theorem reduce this to explicit global label-graph
densities.

### Weighted global compatibility

All anchors witnessing the same forbidden slot-value pattern are grouped into
one pair or triple relation.  The strongest endpoint charges total incident
event probability rather than raw event count.

After the internal macro events are paid, it is sufficient that every slot `s`
satisfy

\[
 \Lambda_{\rm external}(s)
 \le
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}.
\]

Equivalently, the grouped pair and triple completion energies must satisfy the
PP3fp bound.  The conditioned global distribution retains fixed-rank spread.

### Universal one-sided cross-macro cancellation

Matching pools may be chosen from disjoint consecutive column slabs and their
movement-row intervals placed in the same order.  Then no movement point from
another macro lies on a slot's negative-slope movement/refill line.  The
transposed row-slab construction removes the refill version.  Thus one entire
high-probability cross-macro direction contributes zero weighted mass.

## What remains conditional

The all-n track now lacks two quantified statements.

1. **Global refined label allocation.** Prove the balanced ownership and global
   perfect-matching conditions for all or almost all macro pools, or exploit the
   resulting boundary-shadow, Hall, exact bad-incidence, and divisor-energy
   concentration with protected trades.
2. **Residual grouped completion energy.** After source cleaning and one-sided
   slab cancellation, prove ordinary source-anchor and residual cross-macro
   relations have total incident probability at most `1/48-o(1)` per slot.

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

## Bottom line

There is no complete proof.  The prime-patching branch now closes matching-pool
supply, prime-gap-scale internal macro width, degree restoration, fixed-rank
spread, fixed-pair cleaning under a refined label matching, same-edge anchor
pruning, saturation-compatible global label allocation, and a weighted global
local-lemma endpoint.

The exact remaining theorem is a global refined-label and weighted
completion-energy statement.  Until those two estimates are proved, the branch
does not prove the no-three-in-line conjecture.