# All-n route B: composite-modulus algebraic hosts

**Branch:** `research/all-n-composite-modulus`

This branch is independent of prime patching and product constructions. Its goal is an algebraic saturated seed directly at arbitrary or sufficiently broad composite side lengths.

The prime-field conic argument cannot be copied blindly: over a ring, a degree-two equation may have many roots and lines may intersect a conic in more than two residue points.

## CM1 — Composite channel definition

### Target statement

For a modulus `N`, define one or more permutation channels

\[
H_c(N)=\{(x,y_x):x\in[N]\}
\]

using units, affine permutations, CRT coordinates, or a controlled completion of the unit group, so that the union of two channels contains exactly two distinct points in every row and column.

The construction must cover nonunits rather than silently restricting to `Z_N^*`.

## CM2 — Ring line-intersection bound

### Target statement

Identify a class of moduli and channels for which every primitive integer line contains at most two points from one channel, or at least no three real-collinear lifted points.

A valid substitute for the field-conic proof may use:

- local bounds modulo each prime power;
- Hensel lifting with controlled multiplicity;
- CRT signatures that force a line triple to violate one local component;
- squarefree moduli with specially chosen channel parameters.

The theorem must address genuine real collinearity after standard integer lifting, not only modular incidence.

## CM3 — Two-channel cross-syndrome control

### Target statement

For distinct channels `H_a(N),H_b(N)`, prove:

- exact two-per-row/two-per-column saturation;
- a bounded real line cap;
- bounded displacement multiplicity;
- a total triple syndrome small enough for the repair machinery;
- a row-column graph with large alternating cycles or usable absorber blocks.

An `O(N log^C N)` syndrome bound would match the current prime-field pathway.

## CM4 — Prime-power carry calculus

### Target statement

Develop the analogue of the secant involution and carry filter at modulus `p^k`. Classify:

- tangent and secant multiplicities;
- product carries and coordinate carries;
- exceptional zero-divisor orbits;
- subgroup-coset absorbers in the unit group;
- interactions between unit and nonunit rows/columns.

The output should either support the existing alternating-core decoder or produce a simpler direct construction.

## CM5 — CRT assembly theorem

### Target statement

Given solved local components at coprime moduli `u,v`, combine them into a saturated configuration at `N=uv` while proving that every real collinear triple would project to a forbidden local triple in at least one component.

The coordinate map must preserve the ordered integer box `[N]^2`; a purely toroidal CRT solution is insufficient unless an exact lifting theorem is supplied.

## CM6 — Coverage of all n

### Target statement

Prove that the admissible modulus class is multiplicatively or additively rich enough to cover every sufficiently large `n`, preferably every `n` directly. Handle the remaining finite sizes by exact constructions.

## Candidate modulus classes

- prime powers with odd prime base;
- squarefree products of large primes;
- moduli whose least prime factor exceeds a controlled direction bound;
- specially chosen semiprimes supporting two compatible affine permutations;
- mixed CRT constructions with one component carrying saturation and another breaking collinearity.

## Mandatory counterexamples

- quadratic congruences with many roots modulo composite `N`;
- lines collapsing through zero divisors;
- distinct CRT points mapping to repeated rows or columns;
- toroidal no-three sets whose standard lifts contain real triples;
- nonunit rows omitted by a unit-group construction.

## Completion criterion

This branch is complete when CM1–CM6 give an exact saturated construction or a repairable bounded-syndrome seed for every sufficiently large composite side length, with real-grid—not merely modular—collinearity proved.