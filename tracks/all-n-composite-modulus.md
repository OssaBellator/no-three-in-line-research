# All-n route B: composite-modulus algebraic hosts

**Branch:** `research/all-n-composite-modulus`

This branch is independent of prime patching and product constructions. Its goal is an algebraic saturated seed directly at arbitrary or sufficiently broad composite side lengths.

The prime-field conic argument cannot be copied blindly: over a ring, a degree-two equation may have many roots and lines may intersect a conic in more than two residue points.

## Current progress

The first exact results are recorded in
[`docs/27-composite-modulus-obstructions.md`](../docs/27-composite-modulus-obstructions.md).

- **CM1 saturation: PROVED.** Two affine permutation channels saturate every modulus and use all unit and nonunit rows and columns.
- **CM2 for affine and unit-hyperbola candidates: REFUTED.** Every affine modular channel has a real collinear triple for \(N\ge5\). Natural unit hyperbolas have explicit squarefree and prime-power line collapses.
- **CM3 affine cycle structure: PROVED; geometric requirements fail.** A unit offset gives one alternating Hamiltonian cycle, but corresponding-column displacement multiplicity is \(\Omega(N)\).
- **CM4: PARTIAL.** Explicit Hensel-multiplicity and zero-divisor exceptional families are classified; a full prime-power carry calculus remains open.
- **CM5: PARTIAL.** Real collinearity always projects to modular collinearity, and naive CRT products have unavoidable mixed-projection triples. A positive ordered-box assembly theorem remains open.
- **CM6: OPEN.** No admissible nonlinear composite host class is yet known.

Finite checks are in
[`scripts/verify_composite_modulus.py`](../scripts/verify_composite_modulus.py).

## CM1 — Composite channel definition

### Target statement

For a modulus `N`, define one or more permutation channels

\[
H_c(N)=\{(x,y_x):x\in[N]\}
\]

using units, affine permutations, CRT coordinates, or a controlled completion of the unit group, so that the union of two channels contains exactly two distinct points in every row and column.

The construction must cover nonunits rather than silently restricting to `Z_N^*`.

### Completed subtask

For every \(N\ge2\), every unit \(m\), and distinct offsets \(c_0,c_1\), the affine channels

\[
A_{m,c_i}(N)=\{(x,[mx+c_i]_N):0\le x<N\}
\]

have exactly two distinct points in every row and column. This completes the saturation statement but not the line-cap statement.

## CM2 — Ring line-intersection bound

### Target statement

Identify a class of moduli and channels for which every primitive integer line contains at most two points from one channel, or at least no three real-collinear lifted points.

A valid substitute for the field-conic proof may use:

- local bounds modulo each prime power;
- Hensel lifting with controlled multiplicity;
- CRT signatures that force a line triple to violate one local component;
- squarefree moduli with specially chosen channel parameters.

The theorem must address genuine real collinearity after standard integer lifting, not only modular incidence.

### Completed negative classifications

- Every affine modular channel contains a real collinear triple for \(N\ge5\).
- For odd squarefree \(N\), \(H_1^\times(N)\) has \(2^{\omega(N)}\) points on \(y=x\).
- For \(N=p^k\), \(p\) odd and \(k\ge2\), a unit hyperbola has \(p^{\lfloor k/2\rfloor}\) points on one real anti-diagonal.
- For \(N=2^k\), \(k\ge3\), \(H_1^\times(N)\) has four points on \(y=x\).

The positive nonlinear-host problem remains open.

## CM3 — Two-channel cross-syndrome control

### Target statement

For distinct channels `H_a(N),H_b(N)`, prove:

- exact two-per-row/two-per-column saturation;
- a bounded real line cap;
- bounded displacement multiplicity;
- a total triple syndrome small enough for the repair machinery;
- a row-column graph with large alternating cycles or usable absorber blocks.

An `O(N log^C N)` syndrome bound would match the current prime-field pathway.

### Completed affine classification

For two affine layers with offset difference \(\delta\):

- saturation is exact;
- the row-column graph has \(\gcd(\delta,N)\) alternating cycles of length \(2N/\gcd(\delta,N)\);
- a unit offset gives one Hamiltonian cycle;
- corresponding-column displacement multiplicities are exactly \(\delta\) and \(N-\delta\), so the maximum is at least \(\lceil N/2\rceil\);
- each layer already contains a real triple for \(N\ge5\).

Thus affine pairs solve the graph bullet but fail the geometric and codegree bullets.

## CM4 — Prime-power carry calculus

### Target statement

Develop the analogue of the secant involution and carry filter at modulus `p^k`. Classify:

- tangent and secant multiplicities;
- product carries and coordinate carries;
- exceptional zero-divisor orbits;
- subgroup-coset absorbers in the unit group;
- interactions between unit and nonunit rows/columns.

The output should either support the existing alternating-core decoder or produce a simpler direct construction.

### Completed exceptional families

The anti-diagonal construction at odd prime powers gives an exact
\(p^{\lfloor k/2\rfloor}\)-fold Hensel collision inside one unit hyperbola.
The equation \(2(y-x)=0\pmod6\) also records why zero-divisor multiples of a
line equation merge distinct primitive fibres.

A full secant/carry classification, especially across nonunit strata, remains open.

## CM5 — CRT assembly theorem

### Target statement

Given solved local components at coprime moduli `u,v`, combine them into a saturated configuration at `N=uv` while proving that every real collinear triple would project to a forbidden local triple in at least one component.

The coordinate map must preserve the ordered integer box `[N]^2`; a purely toroidal CRT solution is insufficient unless an exact lifting theorem is supplied.

### Completed lifting facts

- Every real collinear triple is modularly collinear in every factor.
- The converse fails: determinant \(\pm N\) gives modular incidence without real incidence.
- If a modularly zero determinant has absolute value below \(N\), then it is zero.
- In every naive coordinatewise CRT product channel, the global columns \(0,u,v\) form a mixed-projection triple whose determinant is divisible by \(N\): one pair collapses modulo \(u\), another modulo \(v\).

Therefore local arc bounds alone do not prove the ordered-box theorem.

## CM6 — Coverage of all n

### Target statement

Prove that the admissible modulus class is multiplicatively or additively rich enough to cover every sufficiently large `n`, preferably every `n` directly. Handle the remaining finite sizes by exact constructions.

**Status:** OPEN. The affine family covers all moduli algebraically but is geometrically impossible for \(N\ge5\); the unit-hyperbola family neither saturates nor maintains a composite line cap.

## Candidate modulus classes

- prime powers with odd prime base;
- squarefree products of large primes;
- moduli whose least prime factor exceeds a controlled direction bound;
- specially chosen semiprimes supporting two compatible nonlinear permutations;
- mixed CRT constructions with one component carrying saturation and another breaking collinearity.

Affine permutations and uncompleted unit hyperbolas are now eliminated as direct solutions.

## Mandatory counterexamples

- [x] quadratic congruences with many roots modulo composite `N`;
- [x] lines collapsing through zero divisors;
- [x] distinct global CRT points with repeated local projections;
- [x] nonunit rows omitted by a unit-group construction;
- [x] lift-direction correction: a genuine toroidal no-three set cannot gain a real triple, because real collinearity always implies modular collinearity. The valid counterexamples go in the opposite direction.

## Completion criterion

This branch is complete when CM1–CM6 give an exact saturated construction or a repairable bounded-syndrome seed for every sufficiently large composite side length, with real-grid—not merely modular—collinearity proved.

The branch is not complete. It now contains a finished saturation theorem, a finished affine classification, the mandatory obstruction package, and a precise positive search boundary.
