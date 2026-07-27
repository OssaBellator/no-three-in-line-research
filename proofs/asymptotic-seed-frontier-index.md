# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`. It records the remaining asymptotic seed problem and the
most compressed currently verified probability, dependency, repair,
regeneration, causality, preprocessing, and scheduling interfaces.

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
| Coordinate-overlap cluster barrier | The same clique defeats standard cluster expansion even with arbitrary positive event weights | PROVED | `docs/305` |
| Exact-oracle dichotomy | Guaranteed deletion by one targeted move is incompatible with exact restoration of the uniform Hamilton measure | PROVED | `docs/306` |
| Complete flaw targeting | Every bad triple has two or three orbit owners and is deleted by a support-one flip or support-three rotation | PROVED / VERIFIED FINITELY | `docs/307` |
| Short finite reachability | Every signed Hamilton state through `m=7` reaches its global minimum defect level in at most four targeted moves | VERIFIED FINITELY | `docs/307`, `docs/310` |
| Polynomial unconditioned mixing | A balanced lazy combined chain has spectral gap `Omega(m^-5)` | PROVED / VERIFIED FINITELY | `docs/308` |
| Delete-then-mix regeneration | Polynomial mixing restores the uniform measure pointwise within `[1-epsilon,1+epsilon]` and gives charge at most `(1+epsilon)mu(A)` | PROVED | `docs/308` |
| Atomic warm starts | Exact deletion images are polynomially warm and total-variation regeneration takes `O(m^5[log m+log(1/epsilon)])` | PROVED / VERIFIED FINITELY | `docs/309` |
| Bounded-horizon descent | A uniform `D`-step strict-descent property would give termination in at most `D Phi(x_0)` moves | PROVED | `docs/310` |
| Exact `m=7` reachability | All `92,160` signed Hamilton states reach one of `36` valid states; maximum distance and descent horizon are four | VERIFIED FINITELY | `docs/310` |
| Immediate causal locality | A newly created flaw touches a newly inserted orbit block; immediate outdegree is `O(n^2 log n)` | PROVED / VERIFIED FINITELY | `docs/311` |
| Residual three-owner scale | Three-owner event probability times immediate causal degree is `O(log n/n)=o(1)` | PROVED | `docs/311` |
| Two-owner parity preprocessing | Fixed-cycle two-owner flaws form a signed XOR system solvable and countable in linear time | PROVED / VERIFIED FINITELY | `docs/312` |
| Two-owner mass bound | The complete two-owner atomic family has size `O(n^3)` and expected count `O(n)` | PROVED | `docs/313` |
| Locality--charge tradeoff | Immediate actions have sparse causality but constant charge; fully mixed actions have near-probability charge but global possible causality | PROVED | `docs/314` |
| Parity-preserving cycle mobility | A rotation changes only three source-stars in the parity graph; the satisfiable induced cycle graph is connected through `m=7` | PROVED / VERIFIED FINITELY | `docs/315` |
| Parity-clean macro repair | Nearest parity recleaning conditionally deletes a three-owner flaw and returns to the two-owner-clean manifold | PROVED | `docs/316` |

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
| PP3blh--PP3bll | Local parity updates, finite rotation audit, connected satisfiable induced graph, and parity-preserving frontier | PROVED / VERIFIED FINITELY | `docs/315-parity-satisfiable-hamilton-rotation-graph.md` |
| PP3blm--PP3blp | Nearest parity recleaning, conditional macro repair, construction complexity, and target-specific gap | PROVED | `docs/316-nearest-parity-recleaning-and-conditional-macro-repair.md` |

## Current exact probability interface

For a directed path forest `F` of `r` prescribed oriented pair edges,

```text
Pr_Hamilton(F) = 1/[2^r (m-1)_r].
```

If `F` uses `v` vertices in the one-fixed near-Hamilton measure,

```text
Pr_one-fixed(F) = (m-v)/m * 1/[2^r (m-2)_r].
```

Strongly generic three-owner triples have probability `Theta(n^-3)` and total
expected mass `Theta(n log n)`. Two-owner flaws have probability `Theta(n^-2)`,
but their complete family has only `O(n^3)` members and contributes only `O(n)`
expected mass.

The static coordinate-overlap graph remains too dense: its source-coordinate
clique gives an event-probability product `Omega(log n)`.

## Complete repair and bounded-horizon interface

Every flaw has exactly two or three orbit owners:

```text
two owners:   flip either owner orientation;
three owners: rotate the three pair successors and choose fresh signs.
```

Both moves remain inside the signed Hamilton space. The unconditioned union is
connected, symmetric, and regular of degree

```text
m + 8 C(m,3).
```

Raw one-step potentials have local minima, but the finite graphs through `m=7`
satisfy a four-step strict-descent horizon. A uniform asymptotic horizon would
telescope to polynomial termination; the finite value four does not prove it.

## Regeneration and locality--charge interface

The balanced lazy chain has

```text
gap(K_m)=Omega(m^-5).
```

Worst-case pointwise regeneration costs

```text
O(m^6 log m + m^5 log(1/epsilon)),
```

while atomic warm starts give total-variation regeneration in

```text
O(m^5[log m + log(1/epsilon)]).
```

Immediate deletion has causal outdegree `O(n^2 log n)` but constant charge `1/2`
for two-owner flaws and `1/8` for three-owner flaws. Full mixing contracts charge
to the stationary scale but makes possible causality global. The missing object
is an intermediate-time or weighted causal light cone with subcritical combined
charge.

## Parity-clean dynamic interface

For a fixed Hamilton cycle, two-owner flaws are exactly a signed parity CSP. A
satisfiable graph with `c` components has `2^c` clean orientation vectors.

A successor rotation on source set `S` changes no parity predicate whose owner
pair is disjoint from `S`; at most `3m-6` constraints change. Through `m=7`, the
parity-satisfiable Hamilton cycles form one connected induced rotation component,
and every inconsistent audited cycle is one rotation from it.

If a targeted rotation lands on a parity-satisfiable cycle, a nearest clean
orientation can be found componentwise in linear time and changes at most
`floor(m/2)` bits. The macro action deletes the target, preserves Hamiltonicity
and duplicate-orbit validity, and returns to a state with no two-owner flaw.
The unresolved target-specific issue is that a flaw fixes its source triple; not
every such rotation is known to remain parity satisfiable.

## Finite diagnostics

```bash
python scripts/check_two_cycle_free_near_hamilton_family.py \
  experiments/archived-prime-seed-codes.json \
  experiments/two-cycle-free-near-hamilton-family-audit.json

python scripts/check_hamilton_three_edge_switchings.py \
  experiments/hamilton-three-edge-switching-audit.json

python scripts/check_hamilton_targeted_switching_drift.py \
  experiments/hamilton-targeted-switching-drift-audit.json

python scripts/check_hamilton_combined_flaw_reachability.py \
  experiments/hamilton-combined-flaw-reachability-audit.json

g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m7.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m7
/tmp/check_hamilton_combined_flaw_reachability_m7

python scripts/check_hamilton_adjacent_transposition_embedding.py \
  experiments/hamilton-adjacent-transposition-embedding-audit.json

python scripts/check_hamilton_atomic_flaw_warmness.py \
  experiments/hamilton-atomic-flaw-warmness-audit.json

python scripts/check_hamilton_immediate_flaw_causality.py \
  experiments/hamilton-immediate-flaw-causality-audit.json

python scripts/check_hamilton_two_owner_parity_csp.py \
  experiments/hamilton-two-owner-parity-csp-audit.json

python scripts/check_hamilton_parity_rotation_graph.py \
  experiments/hamilton-parity-rotation-graph-audit.json
```

The exact suites include `92,160` signed Hamilton states and `4,427,088` directed
combined-flaw edges at `m=7`, `2,376,384` immediate causal edges through `m=6`,
every Hamilton-cycle parity system through `m=7`, and `27,864` directed parity
rotations through `m=7`.

## Current constructive targets

1. prove a uniform bounded strict-descent horizon or a weighted multi-step
   Lyapunov theorem;
2. prove nonemptiness and useful connectivity of parity-satisfiable Hamilton
   cycles for all sufficiently large `m`;
3. show every relevant three-owner flaw admits a parity-satisfiable macro
   rotation, or design a larger parity-clean move;
4. prove an intermediate-time charge--causality interpolation theorem;
5. control witness sequences or partial rejection on the parity-clean residual
   three-owner process;
6. introduce a biased cyclic-order measure suppressing high-collateral
   assignments while retaining tractable cylinders.

The next available theorem identifier is `PP3blq`. The asymptotic
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.
