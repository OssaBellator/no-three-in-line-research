# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`.  It records the remaining asymptotic seed problem and the
most compressed currently verified probability and repair interfaces.

## Current global theorem

For `n=p-1`, find a permutation `sigma` and a derangement `pi`, put

```text
tau = sigma o pi,
```

and require every maximal Euclidean line of `[n]^2` to contain at most two cells
of the two permutation graphs.

Equivalently inside swapped quarter-turn action, find a canonical signed pair
cycle cover satisfying all maximal-line capacities.  The asymptotic existence
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

## Exact theorem ranges

| IDs | Statement | Status | Location |
|---|---|---|---|
| PP3biy--PP3bjf | Two-cycle-free generating function, near-Hamilton counts, exact cylinders, retained first-moment barrier, and finite suite audit | PROVED / VERIFIED FINITELY | `docs/302-two-cycle-free-near-hamilton-signed-cover-measures.md` |
| PP3bjg--PP3bjl | Three-edge Hamilton closure, involution, connectivity, reversible signed kernel, and targeted triple destruction | PROVED / VERIFIED FINITELY | `docs/303-hamilton-three-edge-switching-repair-kernel.md` |

## Current exact probability interfaces

For a directed path forest `F` of `r` prescribed oriented pair edges, the full
Hamilton signed measure satisfies

```text
Pr(F) = 1/[2^r (m-1)_r].
```

If `F` uses `v` pair vertices, the one-fixed near-Hamilton measure satisfies

```text
Pr(F) = (m-v)/m * 1/[2^r (m-2)_r].
```

These formulas are exact, not asymptotic estimates.  For strongly generic
collinear triples they give probability `Theta(m^-3)`, and summation over the
`Theta(n^4 log n)` strongly generic triples gives the retained
`Theta(n log n)` expectation.

## Current exact repair interface

A Hamilton state admits one three-edge successor rotation for every unordered
source triple.  On a cycle of length `ell`, the unsigned switching graph is
connected and regular of degree

```text
C(ell,3).
```

After independently choosing the three new orientation bits, the signed degree
is

```text
8 C(ell,3).
```

The transition kernel is symmetric and reversible under the uniform signed
Hamilton measure.  Targeting the three source assignments of a strongly generic
bad triple removes all three old orbit blocks while retaining matching,
Hamiltonicity, pair-2-cycle-freeness, and duplicate-orbit validity.

## Finite diagnostics

```bash
python scripts/check_two_cycle_free_near_hamilton_family.py \
  experiments/archived-prime-seed-codes.json \
  experiments/two-cycle-free-near-hamilton-family-audit.json

python scripts/check_hamilton_three_edge_switchings.py \
  experiments/hamilton-three-edge-switching-audit.json
```

The first diagnostic verifies thirteen pair-2-cycle-free public/code cases,
nine Hamilton or one-fixed cases, exact generating-function coefficients
through `m=10`, and `39,380` path-forest cylinders through `m=8`.  The second
verifies `5,910` Hamilton states and `310,104` directed switching moves through
cycle length eight.

## Next theorem target

The remaining constructive step is to control side effects of targeted
three-edge rotations.  A successful route must provide at least one of:

1. a nonnegative line-defect potential with negative conditional drift under a
   targeted switching schedule;
2. a cluster-expansion or lopsided local-lemma criterion using the exact
   Hamilton path-forest cylinders; or
3. a resampling-oracle termination theorem for the reversible switching kernel.

The exact first-moment results rule out simply sampling once from the uniform
Hamilton or one-fixed measures.  The asymptotic prime-minus-one seed theorem and
the no-three-in-line conjecture remain open.
