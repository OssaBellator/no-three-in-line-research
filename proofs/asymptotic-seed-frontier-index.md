# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`. It records the remaining asymptotic seed problem and the
most compressed verified probability, repair, parity, causality, regeneration,
and scheduling interfaces.

## Current global theorem

For `n=p-1`, find a permutation `sigma` and a derangement `pi`, put

```text
tau = sigma o pi,
```

and require every maximal Euclidean line of `[n]^2` to contain at most two cells
of the two permutation graphs. Equivalently, inside swapped quarter-turn action,
find a canonical signed pair cycle cover satisfying all maximal-line capacities.
The asymptotic existence theorem remains open.

## Current reductions and barriers

| Phase | Result | Status | Location |
|---|---|---|---|
| Signed orbit CSP | Swapped seeds are signed pair permutations with matching, duplicate-orbit, and line-capacity constraints | PROVED EQUIVALENCE | `docs/287` |
| Relative lift and cover count | Pair cycles lift exactly; duplicate-orbit avoidance costs only a limiting factor `exp(-1/4)` | PROVED | `docs/289` |
| Uniform edge-disjoint barrier | Uniform edge-disjoint signed covers have `Theta(n log n)` expected generic same-layer triples | PROVED | `docs/291` |
| Complete finite suite | Exact certificates exist for every odd prime through `73` | VERIFIED FINITELY | `docs/301` |
| Two-cycle-free Hamilton reduction | Pair 2-cycles can be excluded at constant asymptotic cost; Hamilton cylinders have exact path-forest probabilities | PROVED / VERIFIED FINITELY | `docs/302` |
| Hamilton first-moment barrier | Hamilton and one-fixed measures still have `Theta(n log n)` expected strongly generic triples | PROVED | `docs/302` |
| Complete flaw targeting | Two-owner flaws are deleted by one sign flip; three-owner flaws by one successor rotation | PROVED / VERIFIED FINITELY | `docs/303`, `docs/307` |
| One-step drift barrier | Mean targeted drift is negative, but raw potentials have increasing moves and local minima | PROVED / VERIFIED FINITELY | `docs/304` |
| Static dependency barrier | Coordinate overlap defeats symmetric LLL and standard cluster expansion by `Omega(log n)` | PROVED | `docs/305` |
| Exact-oracle dichotomy | Guaranteed deletion is incompatible with exact restoration of the uniform Hamilton measure | PROVED | `docs/306` |
| Finite bounded-horizon descent | Every signed Hamilton state through `m=7` reaches its optimum within four targeted moves | VERIFIED FINITELY | `docs/310` |
| Polynomial regeneration | The lazy combined chain has gap `Omega(m^-5)`; delete-then-mix gives approximate regeneration | PROVED / VERIFIED FINITELY | `docs/308`, `docs/309` |
| Immediate causal locality | A newly created flaw touches a newly inserted block; immediate outdegree is `O(n^2 log n)` | PROVED / VERIFIED FINITELY | `docs/311` |
| Residual three-owner scale | Three-owner probability times immediate causal degree is `O(log n/n)=o(1)` | PROVED | `docs/311` |
| Two-owner parity preprocessing | Fixed-cycle two-owner flaws form a signed XOR system solvable and countable in linear time | PROVED / VERIFIED FINITELY | `docs/312` |
| Two-owner mass bound | The complete two-owner family has size `O(n^3)` and expected count `O(n)` | PROVED | `docs/313` |
| Locality--charge endpoint tradeoff | Immediate actions have sparse causality but constant charge; fully mixed actions have near-probability charge but global possible causality | PROVED | `docs/314` |
| Parity-clean macro repair | Local parity updates and nearest recleaning give a conditional macro action; the clean cycle graph is connected through `m=7` | PROVED / VERIFIED FINITELY | `docs/315` |
| Owner-intersecting macro deletion | Every owner triple has a clean intersecting rotation through `m=8`; direct prescribed rotation is unnecessary | PROVED / VERIFIED FINITELY | `docs/316` |
| Trajectory-local causal light cone | One realized `t`-step path creates only `O((t+1)n^2 log n)` distinct collateral flaws | PROVED | `docs/317` |
| Logarithmic charge lower scale | Laziness forces at least `3 log_2 n-O(1)` steps before three-owner charge can reach `O(n^-3)` | PROVED | `docs/317` |
| Quarter-turn defect divisibility | Every swapped bad-triple count is divisible by four; `Psi=B_3/4` is the natural integer potential | PROVED | `docs/318` |
| Exact `m=8` signed census | All `1,290,240` signed Hamilton states were scored; exactly `28` are valid on `10` cycles | VERIFIED FINITELY | `docs/318` |

## Exact theorem ranges

| IDs | Statement | Status | Location |
|---|---|---|---|
| PP3biy--PP3bjf | Two-cycle-free counts, near-Hamilton cylinders, retained first-moment barrier, and finite audit | PROVED / VERIFIED FINITELY | `docs/302-two-cycle-free-near-hamilton-signed-cover-measures.md` |
| PP3bjg--PP3bjl | Three-edge Hamilton closure, involution, connectivity, reversible kernel, and targeted deletion | PROVED / VERIFIED FINITELY | `docs/303-hamilton-three-edge-switching-repair-kernel.md` |
| PP3bjm--PP3bjp | Zero stationary drift, negative mean targeted drift, best-sign increases, and local minima | PROVED / VERIFIED FINITELY | `docs/304-targeted-hamilton-switching-drift-and-local-minima.md` |
| PP3bjq--PP3bjs | Coordinate clique, symmetric-LLL failure, and arbitrary-weight cluster-expansion failure | PROVED | `docs/305-hamilton-coordinate-clique-lll-and-cluster-barriers.md` |
| PP3bju--PP3bjw | Guaranteed-deletion versus exact-restoration impossibility | PROVED | `docs/306-targeted-switching-resampling-oracle-dichotomy.md` |
| PP3bjx--PP3bkc | Owner dichotomy, orientation-flip repair, complete targeting, reversible combined graph, and short reachability | PROVED / VERIFIED FINITELY | `docs/307-complete-hamilton-flaw-targeting-and-short-reachability.md` |
| PP3bkd--PP3bkh | Lazy chain, adjacent-transposition comparison, polynomial gap, pointwise mixing, and approximate regeneration | PROVED / VERIFIED FINITELY | `docs/308-delete-then-mix-approximate-regeneration.md` |
| PP3bki--PP3bkl | Atomic probabilities, injective deletion images, exact warmness, and faster TV regeneration | PROVED / VERIFIED FINITELY | `docs/309-atomic-flaw-warm-start-regeneration.md` |
| PP3bkm--PP3bkp | Bounded-horizon descent, exact `m=7` reachability, four-step finite descent, and scheduling frontier | PROVED / VERIFIED FINITELY | `docs/310-bounded-horizon-hamilton-descent-and-m7-reachability.md` |
| PP3bkq--PP3bku | New-block locality, fixed-block flaw count, sparse causality, residual scale, and finite census | PROVED / VERIFIED FINITELY | `docs/311-immediate-hamilton-flaw-causality-and-residual-scale.md` |
| PP3bkv--PP3bkz | Reflection invariance, exact XOR reduction, signed-graph solution count, finite parity census, and preprocessing | PROVED / VERIFIED FINITELY | `docs/312-two-owner-hamilton-flaws-as-a-parity-csp.md` |
| PP3bla--PP3bld | Orbit-coordinate fibres, cubic two-owner count, linear expected mass, and scale separation | PROVED | `docs/313-two-owner-flaw-count-and-lower-order-expectation.md` |
| PP3ble--PP3blg | Immediate action charges, global causality after full mixing, and endpoint tradeoff | PROVED | `docs/314-locality-charge-endpoint-tradeoff.md` |
| PP3blh--PP3bln | Local parity updates, nearest recleaning, conditional macro repair, finite rotation connectivity, update-width census, and construction complexity | PROVED / VERIFIED FINITELY | `docs/315-parity-local-successor-rotations-and-macro-repair.md` |
| PP3blo--PP3blr | Owner-intersection deletion, clean-degree criterion, exact `m=8` extension, and universal finite macro targetability | PROVED / VERIFIED FINITELY | `docs/316-owner-intersecting-parity-clean-macro-deletion.md` |
| PP3bls--PP3blv | Trajectory block locality, pathwise flaw fanout, lazy charge lower bound, and logarithmic interpolation scale | PROVED | `docs/317-trajectory-local-causal-light-cones-and-logarithmic-interpolation.md` |
| PP3blw--PP3blz | Quarter-turn defect divisibility, owner-interaction decomposition, exact `m=8` census, and normalized descent potential | PROVED / VERIFIED FINITELY | `docs/318-quarter-turn-defect-divisibility-and-m8-hamilton-census.md` |

## Exact probability and defect scale

For a directed path forest `F` of `r` prescribed oriented pair edges,

```text
Pr_Hamilton(F) = 1/[2^r (m-1)_r].
```

If `F` uses `v` pair vertices in the one-fixed near-Hamilton measure,

```text
Pr_one-fixed(F) = (m-v)/m * 1/[2^r (m-2)_r].
```

Strongly generic three-owner triples have probability `Theta(n^-3)` and total
expected mass `Theta(n log n)`. Two-owner flaws have probability `Theta(n^-2)`,
but their complete family has only `O(n^3)` members and contributes `O(n)`
expected mass.

Quarter-turn symmetry partitions every bad triple into an orbit of size four.
Hence

```text
Psi = B_3/4
```

is a nonnegative integer and vanishes exactly on valid states.

## Complete repair and bounded-horizon interface

Every flaw has exactly two or three orbit owners:

```text
two owners:   flip either owner orientation;
three owners: rotate three successors and choose new signs.
```

Exhaustive signed-state reachability through `m=7` gives a four-step strict-
descent horizon. The exact state census now extends through `m=8`:

| `m` | signed states | minimum `B_3` | valid states | valid cycles |
|---:|---:|---:|---:|---:|
| 4 | 96 | 0 | 16 | 2 |
| 5 | 768 | 0 | 16 | 2 |
| 6 | 7,680 | 4 | 0 | 0 |
| 7 | 92,160 | 0 | 36 | 10 |
| 8 | 1,290,240 | 0 | 28 | 10 |

The complete directed `m=8` reachability graph and descent horizon remain open.
A uniform asymptotic horizon for `Psi` would telescope to polynomial
termination.

## Parity-clean macro interface

For a fixed Hamilton cycle, two-owner flaws are exactly a signed parity CSP. A
rotation on source set `T` changes at most `3m-6` parity predicates. If the new
cycle is parity satisfiable, a nearest clean orientation is found in linear time
and differs in at most `floor(m/2)` bits.

A three-owner flaw with owner set `S` is deleted by any rotation with
`T intersect S != empty`. The exact audit through `m=8` gives:

| `m` | cycles | parity-satisfiable | minimum clean degree | disjoint triples `C(m-3,3)` | minimum clean rotations meeting every owner triple |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 4 | 0 | 4 |
| 5 | 24 | 22 | 9 | 0 | 9 |
| 6 | 120 | 112 | 16 | 1 | 15 |
| 7 | 720 | 664 | 26 | 4 | 22 |
| 8 | 5,040 | 3,542 | 27 | 10 | 19 |

At `m=8`, the `1,498` inconsistent cycles split into `480` cycles with one owner
pair forbidding both XOR values and `1,018` cycles with a nonzero-XOR signed
cycle of shortest length three or four.

## Regeneration, causality, and the logarithmic window

For one realized deletion followed by `t` lazy chain steps,

```text
inserted blocks <= 3(t+1),
new or first-appearing flaws = O((t+1)n^2 log n).
```

The all-hold trajectory gives

```text
gamma_A(t) >= 2^(-t) gamma_A(0).
```

Thus three-owner probability-scale charge requires at least
`3 log_2 n-O(1)` steps. At `t=O(log n)`, the pathwise flaw light cone is only
`O(n^2 log^2 n)`, but no matching action-charge upper bound is yet proved.

## Finite diagnostics

```bash
python scripts/check_hamilton_owner_intersecting_parity_macro.py \
  experiments/hamilton-owner-intersecting-parity-macro-audit.json

g++ -O3 -std=c++17 \
  scripts/check_hamilton_signed_defect_census_m8.cpp \
  -o /tmp/check_hamilton_signed_defect_census_m8
/tmp/check_hamilton_signed_defect_census_m8

g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m7.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m7
/tmp/check_hamilton_combined_flaw_reachability_m7
```

The exact suites include all `282,240` Hamilton-cycle rotations at `m=8`, all
`1,290,240` signed Hamilton states at `m=8`, and the full `4,427,088`-edge
directed targeted graph at `m=7`.

## Current constructive targets

1. build the complete or parity-clean targeted graph at `m=8` and determine its
   strict-descent horizon for `Psi`;
2. prove nonemptiness and useful connectivity of parity-satisfiable Hamilton
   cycles for all sufficiently large `m`;
3. prove that every owner triple has a parity-satisfiable intersecting rotation,
   or classify exceptional triples asymptotically;
4. classify and avoid owner pairs that forbid both XOR values;
5. prove an upper charge bound in the `t=Theta(log n)` trajectory-local window;
6. control exponential moments or witness sequences of the pathwise flaw light
   cone;
7. prove that consecutive parity-clean macro outputs remain polynomially warm;
8. introduce a biased cyclic-order measure suppressing high-collateral
   assignments while retaining tractable cylinders.

The next available theorem identifier is `PP3bma`. The asymptotic
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.
