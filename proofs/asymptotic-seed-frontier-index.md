# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`. It records the most compressed verified probability,
repair, parity, causality, regeneration, and scheduling interfaces for the
remaining asymptotic problem.

## Current global theorem

For `n=p-1`, find a permutation `sigma` and a derangement `pi`, put

```text
tau = sigma o pi,
```

and require every maximal Euclidean line of `[n]^2` to contain at most two cells
of the two permutation graphs. Equivalently, inside swapped quarter-turn action,
find a canonical signed pair cycle cover satisfying every maximal-line capacity.
The asymptotic existence theorem remains open.

## Current reductions, constructions, and barriers

| Phase | Result | Status | Location |
|---|---|---|---|
| Signed orbit CSP | Swapped seeds are signed pair permutations with matching, duplicate-orbit, and line-capacity constraints | PROVED EQUIVALENCE | `docs/287` |
| Relative lift and cover count | Pair cycles lift exactly; duplicate-orbit avoidance costs a limiting factor `exp(-1/4)` | PROVED | `docs/289` |
| Uniform edge-disjoint barrier | Uniform edge-disjoint signed covers have `Theta(n log n)` expected generic same-layer triples | PROVED | `docs/291` |
| Complete finite suite | Exact certificates exist for every odd prime through `73` | VERIFIED FINITELY | `docs/301` |
| Two-cycle-free Hamilton reduction | Pair 2-cycles can be excluded at constant asymptotic cost; Hamilton cylinders have exact path-forest probabilities | PROVED / VERIFIED FINITELY | `docs/302` |
| Hamilton first-moment barrier | Hamilton and one-fixed measures retain `Theta(n log n)` expected generic triples | PROVED | `docs/302` |
| Complete flaw targeting | Two-owner flaws are deleted by one sign flip; three-owner flaws by one successor rotation | PROVED / VERIFIED FINITELY | `docs/303`, `docs/307` |
| One-step drift barrier | Mean targeted drift is negative, but raw potentials have increasing moves and local minima | PROVED / VERIFIED FINITELY | `docs/304` |
| Static dependency barrier | Coordinate overlap defeats symmetric LLL and standard cluster expansion by `Omega(log n)` | PROVED | `docs/305` |
| Exact-oracle dichotomy | Guaranteed deletion is incompatible with exact restoration of the uniform Hamilton measure | PROVED | `docs/306` |
| Polynomial regeneration | The lazy combined chain has gap `Omega(m^-5)`; delete-then-mix gives approximate regeneration | PROVED / VERIFIED FINITELY | `docs/308`, `docs/309` |
| Immediate causal locality | A newly created flaw touches a newly inserted block; immediate outdegree is `O(n^2 log n)` | PROVED / VERIFIED FINITELY | `docs/311` |
| Residual three-owner scale | Three-owner probability times immediate causal degree is `O(log n/n)=o(1)` | PROVED | `docs/311` |
| Two-owner parity preprocessing | Fixed-cycle two-owner flaws form a signed XOR system solvable and countable in linear time | PROVED / VERIFIED FINITELY | `docs/312` |
| Two-owner mass bound | The complete two-owner family has size `O(n^3)` and expected count `O(n)` | PROVED | `docs/313` |
| Locality--charge endpoint tradeoff | Immediate actions have sparse causality but constant charge; fully mixed actions have near-probability charge but global possible causality | PROVED | `docs/314` |
| Parity-clean macro repair | Local parity updates and nearest recleaning give a conditional macro action | PROVED / VERIFIED FINITELY | `docs/315` |
| Owner-intersecting macro deletion | A clean rotation touching one flaw owner deletes the flaw; universal clean targetability holds through `m=9` | PROVED / VERIFIED FINITELY | `docs/316`, `docs/320` |
| Trajectory-local causal light cone | One realized `t`-step path creates only `O((t+1)n^2 log n)` distinct collateral flaws | PROVED | `docs/317` |
| Logarithmic charge lower scale | Laziness forces at least `3 log_2 n-O(1)` steps before three-owner charge can reach `O(n^-3)` | PROVED | `docs/317` |
| Quarter-turn defect divisibility | Every swapped bad-triple count is divisible by four; `Psi=B_3/4` is the natural integer potential | PROVED | `docs/318` |
| Exact `m=8` signed census | All `1,290,240` signed Hamilton states were scored; exactly `28` are valid | VERIFIED FINITELY | `docs/318` |
| Exact `m=8` targeted reachability | Every signed Hamilton state reaches validity; maximum directed distance is five | VERIFIED FINITELY | `docs/319` |
| Exact clean-fibre regeneration | Independent parity-component roots give the uniform clean orientation fibre | PROVED / VERIFIED FINITELY | `docs/320` |
| Parity topology transition | Every clean parity graph is a forest through `m=9`; 1,588 rank-one clean graphs first occur at `m=10` | VERIFIED FINITELY | `docs/320` |
| Exact labelled fibre charge | A labelled clean rotation has column mass `2^(c-c'-r)`; charge-aware choices give at most `1/8` through `m=9` | PROVED / VERIFIED FINITELY | `docs/321` |

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
| PP3bma--PP3bmc | Implicit reverse neighbours, exact `m=8` reachability, and five-step descent upper bound | PROVED / VERIFIED FINITELY | `docs/319-compressed-m8-targeted-reachability-and-five-step-descent.md` |
| PP3bmd--PP3bmi | Exact fibre regeneration, component atom bound, forest transition, `m=9` clean mobility, and fibre-randomized macro | PROVED / VERIFIED FINITELY | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmj--PP3bmm | Exact labelled fibre charge, forest formula, universal finite `1/8` charge-aware rotations, and remaining label-merging gap | PROVED / VERIFIED FINITELY | `docs/321-exact-parity-fibre-action-charge-and-charge-aware-rotations.md` |

## Exact probability and defect scale

For a directed path forest `F` of `r` prescribed oriented pair edges,

```text
Pr_Hamilton(F) = 1/[2^r (m-1)_r].
```

Strongly generic three-owner triples have probability `Theta(n^-3)` and total
expected mass `Theta(n log n)`. Two-owner flaws have probability `Theta(n^-2)`,
but their complete family has only `O(n^3)` members and contributes `O(n)`
expected mass.

Quarter-turn symmetry gives the integer potential

```text
Psi = B_3/4.
```

## Complete repair and finite descent interface

Every flaw has exactly two or three orbit owners:

```text
two owners:   flip either owner orientation;
three owners: rotate three successors and choose new signs.
```

The complete finite results are:

| `m` | signed states | optimum `B_3` | optimum states | maximum directed distance to optimum |
|---:|---:|---:|---:|---:|
| 4 | 96 | 0 | 16 | at most 3 |
| 5 | 768 | 0 | 16 | at most 3 |
| 6 | 7,680 | 4 | 84 | at most 3 |
| 7 | 92,160 | 0 | 36 | 4 |
| 8 | 1,290,240 | 0 | 28 | 5 |

At `m=8` the exact distance distribution to validity is

```text
0: 28, 1: 1,560, 2: 57,408, 3: 736,212, 4: 493,728, 5: 1,304.
```

A uniform asymptotic bound for `Psi`, or a weighted replacement, remains open.

## Parity-clean regeneration and charge interface

For a clean cycle with `c` parity components, independent component-root bits
produce the exact uniform distribution on its `2^c` clean orientations. If the
constraint graph has `q` edges, then

```text
c >= m-q,
maximum fibre atom <= 2^(q-m).
```

Every satisfiable constraint graph through `m=9` is a forest. At `m=10`, exactly
1,588 satisfiable cycles have cyclomatic rank one; the remaining 296,298 clean
cycles are forests.

At `m=9`:

```text
clean cycles:                                      31,688
clean induced components:                               1
minimum clean degree:                                  43
minimum clean rotations meeting any owner triple:      26
maximum distance from inconsistent to clean:             1
```

For one labelled fibre-randomized action, let `c,c'` be the source and target
component counts and let `r` be the number of source components met by the flaw
owners. Its exact column mass is

```text
2^(c-c'-r).
```

Through `m=9`, every clean cycle and owner triple admits a clean intersecting
rotation with `r+c'-c>=3`, hence labelled mass at most `1/8`. This does not yet
bound an action that merges multiple rotation labels.

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
`O(n^2 log^2 n)`. The missing upper bound is now concentrated in the cycle
coordinate and in rotation-label merging; the clean sign fibre itself can be
regenerated exactly in one step.

## Finite diagnostics

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m8.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m8
/tmp/check_hamilton_combined_flaw_reachability_m8

python scripts/check_hamilton_parity_fibre_regeneration.py \
  experiments/hamilton-parity-fibre-regeneration-audit.json

python scripts/check_hamilton_parity_fibre_charge.py \
  experiments/hamilton-parity-fibre-charge-audit.json
```

The exact suites now include the full `m=8` signed state space, the implicit
complete `m=8` targeted graph, every parity fibre through `m=10`, every
`m=9` successor rotation, and every clean-cycle/owner-triple charge-aware choice
through `m=9`.

## Current constructive targets

1. prove a uniform bounded strict-descent horizon or weighted multi-step
   Lyapunov theorem for `Psi`;
2. prove asymptotic nonemptiness and useful connectivity of parity-satisfiable
   Hamilton cycles;
3. prove asymptotic clean owner-intersecting mobility;
4. classify and avoid owner pairs that forbid both XOR values;
5. control consistent signed parity cycles, which first appear at `m=10`;
6. choose or weight rotation labels so merged fibre-action charge remains small;
7. prove a cycle-coordinate charge upper bound in the `t=Theta(log n)` window;
8. convert trajectory-local light cones into an exponential-moment or witness
   theorem;
9. introduce a biased cyclic-order measure suppressing high-collateral
   assignments while retaining tractable cylinders.

The next available theorem identifier is `PP3bmn`. The asymptotic
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.
