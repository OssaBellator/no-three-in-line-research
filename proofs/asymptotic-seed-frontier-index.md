# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`. It records the compressed probability, repair, parity,
causality, regeneration, descent, clean-macro, and clean-cycle mixing interfaces
for the remaining asymptotic problem.

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
| Relative lift and cover count | Pair cycles lift exactly; duplicate-orbit avoidance costs a limiting constant factor | PROVED | `docs/289` |
| Uniform-measure barrier | Edge-disjoint and Hamilton measures have `Theta(n log n)` expected generic triples | PROVED | `docs/291`, `docs/302` |
| Complete finite suite | Exact certificates exist for every odd prime through `73` | VERIFIED FINITELY | `docs/301` |
| Complete local targeting | Two-owner flaws are deleted by one sign flip; three-owner flaws by one successor rotation | PROVED / VERIFIED FINITELY | `docs/303`, `docs/307` |
| One-step drift barrier | Mean targeted drift is negative, but raw potentials have increasing moves and local minima | PROVED / VERIFIED FINITELY | `docs/304` |
| Static dependency barrier | Coordinate overlap defeats symmetric LLL and standard cluster expansion by `Omega(log n)` | PROVED | `docs/305` |
| Exact-oracle dichotomy | Guaranteed deletion is incompatible with exact restoration of the uniform Hamilton measure | PROVED | `docs/306` |
| Polynomial regeneration | The lazy combined chain has gap `Omega(m^-5)`; delete-then-mix gives approximate regeneration | PROVED / VERIFIED FINITELY | `docs/308`, `docs/309` |
| Immediate causal locality | A newly created flaw touches a newly inserted block; immediate outdegree is `O(n^2 log n)` | PROVED / VERIFIED FINITELY | `docs/311` |
| Residual three-owner scale | Three-owner probability times immediate causal degree is `O(log n/n)=o(1)` | PROVED | `docs/311` |
| Two-owner parity reduction | Fixed-cycle two-owner flaws form a signed XOR system | PROVED / VERIFIED FINITELY | `docs/312` |
| Two-owner atomic mass | The complete two-owner atomic family has size `O(n^3)` and expected count `O(n)` | PROVED | `docs/313` |
| Locality--charge endpoints | Immediate actions have sparse causality but constant charge; full mixing has small charge but global possible causality | PROVED | `docs/314` |
| Parity-clean macro repair | Local parity updates and clean-fibre recleaning give owner-intersecting macro deletion | PROVED / VERIFIED FINITELY | `docs/315`, `docs/316` |
| Trajectory-local light cone | One realized `t`-step path creates only `O((t+1)n^2 log n)` collateral flaws | PROVED | `docs/317` |
| Logarithmic charge lower scale | Laziness forces at least `3 log_2 n-O(1)` steps before three-owner charge can reach `O(n^-3)` | PROVED | `docs/317` |
| Integer defect potential | Every bad-triple count is divisible by four; `Psi=B_3/4` is integral | PROVED | `docs/318` |
| Exact `m=8` targeted descent | All `1,290,240` states reach validity; the strict-descent horizon is exactly five | VERIFIED FINITELY | `docs/319`, `docs/325` |
| Exact clean-fibre regeneration | Independent parity-component roots give the uniform clean orientation fibre | PROVED / VERIFIED FINITELY | `docs/320` |
| Exact labelled fibre charge | A labelled clean rotation has column mass `2^(c-c'-r)` | PROVED / VERIFIED FINITELY | `docs/321` |
| Impossible-pair classification | Pair-local impossibility is a centered-ray multiplier equation; only `O(m log m)` pairs occur | PROVED / VERIFIED FINITELY | `docs/322` |
| Logarithmic parity-edge mass | There are `O(m^2 log m)` one-XOR assignment pairs and `E q(rho)=O(log m)` | PROVED / VERIFIED FINITELY | `docs/323` |
| Merged charge transport | Optimal unlabelled fibre charge is an exact weighted Hall ratio | PROVED | `docs/324` |
| Logarithmic near-clean seed | Some pair-safe Hamilton cycle admits an orientation violating only `O(log m)` parity edges | PROVED / VERIFIED FINITELY | `docs/326` |
| Pair-safe frustration descent | Every positive-frustration pair-safe cycle through `m=10` has a direct clean rotation | VERIFIED FINITELY | `docs/327`, `docs/329` |
| Exact `m=8` clean macro graph | All `404,080` parity-clean states reach validity within three macro steps | VERIFIED FINITELY | `docs/328` |
| Exact `m=10` clean mobility | The 297,886 clean cycles form one component; every owner triple has at least 40 clean intersecting rotations | VERIFIED FINITELY | `docs/329` |
| Heat-kernel charge identity | Reversible clean-cycle mixing gives exact charge `||K^t f_A||_infinity` | PROVED | `docs/330` |
| Local signed parity repair | Through `m=9` signs remain fixed; at `m=10` at most two rotated-owner signs change | VERIFIED FINITELY | `docs/331` |
| Exact `m=9` clean macro graph | All `6,727,728` parity-clean signed states reach validity within four macro steps | VERIFIED FINITELY | `docs/332` |
| Sparse collateral-core barrier | Support and atomic counts have joint local minima, reduced to 68 sparse distance-four states | VERIFIED FINITELY | `docs/332` |
| Exact small weighted Hall audit | Every atomic flaw and every Hall subset are exhausted through `m=7`; worst charge is at most `4.422/m^3` | VERIFIED FINITELY | `docs/333` |

## Exact theorem ranges

| IDs | Statement | Status | Location |
|---|---|---|---|
| PP3biy--PP3bjf | Two-cycle-free counts, near-Hamilton cylinders, and first-moment barrier | PROVED / VERIFIED FINITELY | `docs/302-two-cycle-free-near-hamilton-signed-cover-measures.md` |
| PP3bjg--PP3bjl | Three-edge Hamilton closure, involution, connectivity, reversible kernel, and deletion | PROVED / VERIFIED FINITELY | `docs/303-hamilton-three-edge-switching-repair-kernel.md` |
| PP3bjm--PP3bjp | Stationary drift, negative mean targeted drift, increases, and local minima | PROVED / VERIFIED FINITELY | `docs/304-targeted-hamilton-switching-drift-and-local-minima.md` |
| PP3bjq--PP3bjs | Coordinate clique, symmetric-LLL failure, and cluster-expansion failure | PROVED | `docs/305-hamilton-coordinate-clique-lll-and-cluster-barriers.md` |
| PP3bju--PP3bjw | Guaranteed-deletion versus exact-restoration impossibility | PROVED | `docs/306-targeted-switching-resampling-oracle-dichotomy.md` |
| PP3bjx--PP3bkc | Owner dichotomy, complete targeting, combined graph, and short reachability | PROVED / VERIFIED FINITELY | `docs/307-complete-hamilton-flaw-targeting-and-short-reachability.md` |
| PP3bkd--PP3bkh | Lazy chain, polynomial gap, pointwise mixing, and approximate regeneration | PROVED / VERIFIED FINITELY | `docs/308-delete-then-mix-approximate-regeneration.md` |
| PP3bki--PP3bkl | Atomic probabilities, deletion images, warmness, and faster TV regeneration | PROVED / VERIFIED FINITELY | `docs/309-atomic-flaw-warm-start-regeneration.md` |
| PP3bkm--PP3bkp | Bounded-horizon lemma, exact `m=7` reachability, and four-step descent | PROVED / VERIFIED FINITELY | `docs/310-bounded-horizon-hamilton-descent-and-m7-reachability.md` |
| PP3bkq--PP3bku | New-block locality, fixed-block count, sparse causality, and residual scale | PROVED / VERIFIED FINITELY | `docs/311-immediate-hamilton-flaw-causality-and-residual-scale.md` |
| PP3bkv--PP3bkz | XOR reduction, signed-graph solution count, finite parity census, and preprocessing | PROVED / VERIFIED FINITELY | `docs/312-two-owner-hamilton-flaws-as-a-parity-csp.md` |
| PP3bla--PP3bld | Orbit fibres, cubic two-owner count, linear mass, and scale separation | PROVED | `docs/313-two-owner-flaw-count-and-lower-order-expectation.md` |
| PP3ble--PP3blg | Immediate charges, global causality after mixing, and endpoint tradeoff | PROVED | `docs/314-locality-charge-endpoint-tradeoff.md` |
| PP3blh--PP3bln | Local parity updates, nearest recleaning, macro repair, and clean connectivity | PROVED / VERIFIED FINITELY | `docs/315-parity-local-successor-rotations-and-macro-repair.md` |
| PP3blo--PP3blr | Owner-intersection deletion, clean-degree criterion, and finite macro targetability | PROVED / VERIFIED FINITELY | `docs/316-owner-intersecting-parity-clean-macro-deletion.md` |
| PP3bls--PP3blv | Trajectory locality, pathwise fanout, lazy lower bound, and logarithmic window | PROVED | `docs/317-trajectory-local-causal-light-cones-and-logarithmic-interpolation.md` |
| PP3blw--PP3blz | Defect divisibility, owner decomposition, exact `m=8` census, and normalized potential | PROVED / VERIFIED FINITELY | `docs/318-quarter-turn-defect-divisibility-and-m8-hamilton-census.md` |
| PP3bma--PP3bmc | Implicit reverse neighbours, exact `m=8` reachability, and five-step upper bound | PROVED / VERIFIED FINITELY | `docs/319-compressed-m8-targeted-reachability-and-five-step-descent.md` |
| PP3bmd--PP3bmi | Exact fibre regeneration, forest transition, `m=9` mobility, and randomized macro | PROVED / VERIFIED FINITELY | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmj--PP3bmm | Exact labelled charge, forest formula, charge-aware rotations, and merging gap | PROVED / VERIFIED FINITELY | `docs/321-exact-parity-fibre-action-charge-and-charge-aware-rotations.md` |
| PP3bmn--PP3bmq | Centered secant form, impossible-pair classification, count, and rarity | PROVED / VERIFIED FINITELY | `docs/322-impossible-owner-pair-ray-classification-and-asymptotic-rarity.md` |
| PP3bmr--PP3bmu | Hosted incidence count, logarithmic first moment, and sparse pair-safe cycle | PROVED / VERIFIED FINITELY | `docs/323-parity-constraint-incidence-count-and-logarithmic-edge-mass.md` |
| PP3bmv--PP3bmy | Merged-column formula, weighted Hall optimum, lower bound, and expansion criterion | PROVED | `docs/324-merged-fibre-charge-as-weighted-hall-transport.md` |
| PP3bmz--PP3bnc | Incremental lower-level BFS, exact `m=8` horizon, critical level, and policy | PROVED / VERIFIED FINITELY | `docs/325-exact-m8-strict-descent-horizon-and-critical-level.md` |
| PP3bnd--PP3bnh | Frustration basis, deletion core, logarithmic near-clean seed, and finite audit | PROVED / VERIFIED FINITELY | `docs/326-parity-frustration-basis-and-logarithmic-near-clean-seeds.md` |
| PP3bni--PP3bnk | Pair-safe frustration descent, marked-edge targeting, and termination through `m=9` | VERIFIED FINITELY | `docs/327-pair-safe-frustration-strict-descent-through-m9.md` |
| PP3bnl--PP3bnp | Sharp `m=8` witnesses, implicit macro graph, and three-step clean reachability | PROVED / VERIFIED FINITELY | `docs/328-m8-critical-witnesses-and-parity-clean-macro-graph.md` |
| PP3bnq--PP3bnu | Exact `m=10` frustration census, direct clean repair, connectivity, and marked-core targeting | VERIFIED FINITELY | `docs/329-m10-pair-safe-frustration-repair-and-clean-mobility.md` |
| PP3bnv--PP3bny | Fibre-weighted Metropolis kernel, exact heat charge, spectral bound, and pointwise endpoint | PROVED | `docs/330-clean-cycle-heat-kernel-charge-and-fibre-weighted-metropolis-chain.md` |
| PP3bnz--PP3bod | Fixed-sign descent through `m=9`, first exceptions at `m=10`, and two-sign locally coupled repair | VERIFIED FINITELY | `docs/331-local-sign-coupled-parity-repair-through-m10.md` |
| PP3boe--PP3boh | Exact `m=9` clean reachability, terminal covers, natural-potential barrier, and sparse collateral cores | VERIFIED FINITELY | `docs/332-exact-m9-clean-macro-reachability-and-sparse-collateral-cores.md` |
| PP3boi--PP3bok | Exact small weighted Hall audit, label-merging penalty census, and cubic-scale consistency | VERIFIED FINITELY | `docs/333-exact-small-size-weighted-hall-transport.md` |

## Exact probability, parity, and defect scales

For a directed path forest `F` of `r` prescribed oriented pair edges,

```text
Pr_Hamilton(F)=1/[2^r (m-1)_r].
```

Strongly generic three-owner triples have probability `Theta(n^-3)` and total
expected mass `Theta(n log n)`. The reduced pairwise parity structures are much
sparser:

```text
impossible compatible assignment pairs = O(m log m),
Pr(a uniform Hamilton cycle contains one)=O(log m/m),
one-XOR compatible assignment pairs = O(m^2 log m),
E[number of parity edges]=O(log m).
```

Consequently some pair-safe Hamilton cycle has only `O(log m)` parity edges and
an orientation violating only `O(log m)` of them. Quarter-turn symmetry gives the
integer potential `Psi=B_3/4`.

## Finite descent and preprocessing interface

The unrestricted targeted graph has exact maximum strict-descent horizons at
most three through `m=6`, four at `m=7`, and five at `m=8`. At `m=8`, exactly 44
states require five moves to lower `Psi`, all at `B_3=4`.

The clean-macro distance distributions are

```text
m=8: 0:28, 1:66,844, 2:303,576, 3:33,632;
m=9: 0:8, 1:59,008, 2:1,317,376, 3:4,873,296, 4:478,040.
```

The 68 distance-four states at `m=9` that are local minima for both support and
atomic counts have only one to three supports. Sixty reach a lower count after
two steps; eight one-support states first decrease on reaching validity after
four steps.

Cycle-level parity preprocessing extends through `m=10`:

```text
pair-safe cycles:                  342,720,
clean cycles:                      297,886,
positive-frustration cycles:        44,834,
maximum frustration index:               3,
maximum pair-safe distance to clean:     1.
```

The signed coupling is local:

```text
m<=9: strict descent with zero sign changes;
m=10: direct clean repair with at most two sign changes,
      both on the rotated source triple.
```

Only 74 of `12,786,720` optimal positive signed states at `m=10` fail fixed-sign
repair; 70 need one local sign change and four need two.

## Clean-cycle mobility and charge interface

At `m=10`, the clean successor-rotation graph is connected, has minimum degree
69, and every owner triple is met by at least 40 clean rotations. The first 1,588
clean rank-one parity graphs do not break connectivity or targetability.

For one atomic flaw `A`, the optimal one-step merged charge is

```text
gamma_A^*=max_(empty != U subseteq X_A) w_A(U)/v(N(U)).
```

For the canonical fibre-weighted reversible kernel `K`,

```text
gamma_A(t)=||K^t f_A||_infinity.
```

The exact one-step audit through `m=7` gives

```text
max_A gamma_A^* <= 4.422/m^3.
```

Proper Hall bottlenecks occur for 884 of 1,692 flaws at `m=6` and 4,864 of 5,100
flaws at `m=7`; the largest finite local/global penalty is `1.69555`. The worst
absolute charge at each audited size is nevertheless attained by the full source
set.

## Regeneration, causality, and the logarithmic window

For one realized deletion followed by `t` lazy local steps,

```text
inserted blocks <= 3(t+1),
new or first-appearing flaws = O((t+1)n^2 log n).
```

The all-hold trajectory gives `gamma_A(t)>=2^(-t)gamma_A(0)`. Therefore
three-owner probability-scale charge requires at least `3 log_2 n-O(1)` steps.
At `t=O(log n)`, the realized flaw light cone is only `O(n^2 log^2 n)`.

## Finite diagnostics

```bash
g++ -O3 -std=c++17 scripts/check_hamilton_strict_descent_horizon_m8.cpp \
  -o /tmp/check_hamilton_strict_descent_horizon_m8
g++ -O3 -std=c++17 scripts/check_hamilton_m10_pair_safe_clean_mobility.cpp \
  -o /tmp/check_hamilton_m10_pair_safe_clean_mobility
g++ -O3 -std=c++17 scripts/check_hamilton_parity_frustration_fixed_orientation.cpp \
  -o /tmp/check_hamilton_parity_frustration_fixed_orientation
g++ -O3 -std=c++17 scripts/check_hamilton_m10_local_sign_coupling.cpp \
  -o /tmp/check_hamilton_m10_local_sign_coupling
g++ -O3 -std=c++17 scripts/check_parity_clean_macro_terminal_core_m8.cpp \
  -o /tmp/check_parity_clean_macro_terminal_core_m8
g++ -O3 -std=c++17 scripts/check_parity_clean_macro_reachability_m9.cpp \
  -o /tmp/check_parity_clean_macro_reachability_m9
g++ -O3 -std=c++17 scripts/check_weighted_hall_transport_small.cpp \
  -o /tmp/check_weighted_hall_transport_small
```

The exact suites now include every `m=8` signed and clean-macro state, every
`m=9` clean signed state, every pair-safe frustration core through `m=10`, all
`43,545,600` successor rotations at `m=10`, and every weighted Hall subset for
every atomic flaw through `m=7`.

## Current constructive targets

1. Prove bounded local-sign repair for the asymptotic `O(log m)` frustration core.
2. Give a uniform collateral-repair word or structural Lyapunov function for the
   eight one-support four-step states.
3. Extend clean-macro reachability to `m=10` without storing all `115,586,396`
   clean orientations.
4. Prove asymptotic connectedness and polynomial owner-intersecting degree of the
   clean-cycle graph.
5. Prove a spectral gap, log-Sobolev inequality, evolving-set bound, or weighted
   Hall expansion for the fibre-weighted clean-cycle kernel.
6. Replace Hall subset enumeration at `m=8` by exact parametric min-cut and seek
   a uniform constant-factor bound over proper cuts.
7. Compare the stationary clean flaw mass `mu_cl(A)` with `Theta(m^-3)`.
8. Implement clean-cycle heat flow on signed states without losing the
   trajectory-local geometric light cone.
9. Convert charge and light-cone estimates into a witness-sequence or
   partial-rejection termination theorem.

The next available theorem identifier is `PP3bol`. The asymptotic
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.
