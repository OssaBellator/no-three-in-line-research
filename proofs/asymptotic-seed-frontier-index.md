# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`. It records the remaining asymptotic seed problem and the
most compressed currently verified probability, dependency, and repair
interfaces.

## Current global theorem

For `n=p-1`, find a permutation `sigma` and a derangement `pi`, put

```text
tau = sigma o pi,
```

and require every maximal Euclidean line of `[n]^2` to contain at most two cells
of the two permutation graphs.

Equivalently inside swapped quarter-turn action, find a canonical signed pair
cycle cover satisfying all maximal-line capacities. The asymptotic existence
theorem remains open.

## Current reductions and barriers

| Phase | Result | Status | Location |
|---|---|---|---|
| Signed orbit CSP | Swapped seeds are signed pair permutations with matching, duplicate-orbit, and line-capacity constraints | PROVED EQUIVALENCE | `docs/287` |
| Relative lift and cover count | Pair cycles lift exactly; duplicate-orbit avoidance costs only a limiting factor `exp(-1/4)` | PROVED | `docs/289` |
| Uniform edge-disjoint barrier | Uniform edge-disjoint signed covers have `Theta(n log n)` expected generic same-layer triples | PROVED | `docs/291` |
| Complete finite suite | Exact certificates exist for every odd prime through `73` | VERIFIED FINITELY | `docs/301` |
| Two-cycle-free reduction | Forbidding every pair 2-cycle removes all duplicate-orbit inequalities at only another factor `exp(-1/4)` | PROVED / VERIFIED FINITELY | `docs/302` |
| Hamilton cylinders | Full Hamilton and one-fixed near-Hamilton covers have exact path-forest cylinder probabilities | PROVED / VERIFIED FINITELY | `docs/302` |
| Hamilton first-moment barrier | The Hamilton and one-fixed measures still have `Theta(n log n)` expected strongly generic triples | PROVED | `docs/302` |
| Three-edge repair kernel | Cyclic successor rotation is an involutive, connected, reversible support-three switching that destroys a targeted triple | PROVED / VERIFIED FINITELY | `docs/303` |
| Targeted drift census | Fresh signs give negative average finite drift, but raw potentials have increasing moves, local minima, and targetability gaps | PROVED / VERIFIED FINITELY | `docs/304` |
| Coordinate-overlap LLL barrier | A source-coordinate clique has size `Omega(n^3 log n)` and defeats symmetric LLL by `Omega(log n)` | PROVED | `docs/305` |
| Coordinate-overlap cluster barrier | The same clique defeats the standard cluster-expansion criterion even with arbitrary positive event weights | PROVED | `docs/305` |
| Exact-oracle dichotomy | Guaranteed deletion by the targeted switch is incompatible with exact restoration of the uniform Hamilton measure | PROVED | `docs/306` |

## Exact theorem ranges

| IDs | Statement | Status | Location |
|---|---|---|---|
| PP3biy--PP3bjf | Two-cycle-free generating function, near-Hamilton counts, exact cylinders, retained first-moment barrier, and finite suite audit | PROVED / VERIFIED FINITELY | `docs/302-two-cycle-free-near-hamilton-signed-cover-measures.md` |
| PP3bjg--PP3bjl | Three-edge Hamilton closure, involution, connectivity, reversible signed kernel, and targeted triple destruction | PROVED / VERIFIED FINITELY | `docs/303-hamilton-three-edge-switching-repair-kernel.md` |
| PP3bjm--PP3bjp | Reversible zero-drift identity, negative average targeted drift, best-sign increases, local minima, and targetability gaps | PROVED / VERIFIED FINITELY | `docs/304-targeted-hamilton-switching-drift-and-local-minima.md` |
| PP3bjq--PP3bjs | Coordinate clique, logarithmic symmetric-LLL failure, and arbitrary-weight cluster-expansion failure | PROVED | `docs/305-hamilton-coordinate-clique-lll-and-cluster-barriers.md` |
| PP3bju--PP3bjw | Guaranteed-deletion versus exact-restoration impossibility and stationarity-targeting dichotomy | PROVED | `docs/306-targeted-switching-resampling-oracle-dichotomy.md` |

## Current exact probability interface

For a directed path forest `F` of `r` prescribed oriented pair edges, the full
Hamilton signed measure satisfies

```text
Pr(F) = 1/[2^r (m-1)_r].
```

If `F` uses `v` pair vertices, the one-fixed near-Hamilton measure satisfies

```text
Pr(F) = (m-v)/m * 1/[2^r (m-2)_r].
```

For strongly generic collinear triples these probabilities are `Theta(m^-3)`.
There are `Theta(n^4 log n)` such triples, giving the retained
`Theta(n log n)` first moment.

The static coordinate-overlap graph is now also closed as a direct route. Its
largest source-coordinate clique has size `Omega(n^3 log n)`, so the product of
one event probability and one clique size is `Omega(log n)`. This blocks both
the symmetric local lemma and the standard cluster-expansion criterion on that
graph.

## Current exact repair interface

A Hamilton state admits one three-edge successor rotation for every unordered
source triple. On a cycle of length `ell`, the unsigned switching graph is
connected and regular of degree

```text
C(ell,3).
```

After independently choosing the three new orientation bits, the signed degree
is

```text
8 C(ell,3).
```

The unconditioned transition kernel is symmetric and reversible under the
uniform signed Hamilton measure and therefore has zero stationary drift for
every potential. Targeting a strongly generic bad triple removes its three old
orbit blocks, but the resulting targeted rule is neither pointwise decreasing
for the natural raw defect potentials nor an exact resampling oracle.

## Finite diagnostics

```bash
python scripts/check_two_cycle_free_near_hamilton_family.py \
  experiments/archived-prime-seed-codes.json \
  experiments/two-cycle-free-near-hamilton-family-audit.json

python scripts/check_hamilton_three_edge_switchings.py \
  experiments/hamilton-three-edge-switching-audit.json

python scripts/check_hamilton_targeted_switching_drift.py \
  experiments/hamilton-targeted-switching-drift-audit.json
```

The cycle-family diagnostic verifies thirteen pair-2-cycle-free public/code
cases, nine Hamilton or one-fixed cases, `46,234` weighted pair permutations,
and `39,380` path-forest cylinders. The switching diagnostic verifies `5,910`
Hamilton states and `310,104` directed moves. The drift diagnostic exhausts
`8,544` signed Hamilton states and `134,432` targeted bad-triple occurrences for
`m=4,5,6`, including all eight sign outcomes.

## Current constructive targets

The three naive endpoints are now excluded:

1. raw one-step defect potentials are not monotone and have local minima;
2. source/target coordinate overlap is too dense for ordinary or standard
   cluster-expansion LLL criteria;
3. guaranteed flaw deletion is not an exact resampling oracle for the uniform
   measure.

The remaining plausible routes are therefore sharper:

1. construct a geometrically weighted or multi-step potential with negative
   conditional drift and a second primitive for non-targetable defects;
2. prove a substantially smaller lopsided dependency graph using slope,
   cyclic-separation, or incompatibility information;
3. analyse the targeted process as a nonexact flaw walk using charges, witness
   sequences, commutativity, or approximate regeneration;
4. introduce a biased stationary cyclic-order measure that suppresses
   high-collateral assignments while retaining tractable cylinders.

The asymptotic prime-minus-one seed theorem and the no-three-in-line conjecture
remain open.
