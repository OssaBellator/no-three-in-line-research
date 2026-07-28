# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`.  It records the compressed verified probability, repair,
parity, causality, regeneration, descent, and clean-cycle mixing interfaces for
the remaining asymptotic problem.

## Current global theorem

For `n=p-1`, find a permutation `sigma` and a derangement `pi`, put

```text
tau = sigma o pi,
```

and require every maximal Euclidean line of `[n]^2` to contain at most two cells
of the two permutation graphs.  Equivalently, inside swapped quarter-turn
action, find a canonical signed pair cycle cover satisfying every maximal-line
capacity.  The asymptotic existence theorem remains open.

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
| PP3bni--PP3bnk | One-step pair-safe frustration descent, marked-edge targeting, and finite termination through `m=9` | VERIFIED FINITELY | `docs/327-pair-safe-frustration-strict-descent-through-m9.md` |
| PP3bnl--PP3bnp | Sharp `m=8` witness classification, implicit macro graph, and three-step clean reachability | PROVED / VERIFIED FINITELY | `docs/328-m8-critical-witnesses-and-parity-clean-macro-graph.md` |
| PP3bnq--PP3bnu | Exact `m=10` frustration census, direct clean repair, connectivity, marked-core targeting, and interface | VERIFIED FINITELY | `docs/329-m10-pair-safe-frustration-repair-and-clean-mobility.md` |
| PP3bnv--PP3bny | Fibre-weighted Metropolis kernel, exact heat charge, spectral bound, and pointwise endpoint | PROVED | `docs/330-clean-cycle-heat-kernel-charge-and-fibre-weighted-metropolis-chain.md` |

## Exact probability, parity, and defect scales

For a directed path forest `F` of `r` prescribed oriented pair edges,

```text
Pr_Hamilton(F)=1/[2^r (m-1)_r].
```

Strongly generic three-owner triples have probability `Theta(n^-3)` and total
expected mass `Theta(n log n)`.  The reduced pairwise parity structures are much
sparser:

```text
impossible compatible assignment pairs = O(m log m),
Pr(a uniform Hamilton cycle contains one)=O(log m/m),
one-XOR compatible assignment pairs = O(m^2 log m),
E[number of parity edges]=O(log m).
```

Consequently some pair-safe Hamilton cycle has only `O(log m)` parity edges and,
by the frustration-core theorem, an orientation violating only `O(log m)` of
them.

Quarter-turn symmetry gives the integer potential

```text
Psi=B_3/4.
```

## Finite descent and preprocessing interface

The unrestricted targeted graph has the following exact frontier:

| `m` | signed states | optimum `B_3` | optimum states | maximum strict-descent horizon |
|---:|---:|---:|---:|---:|
| 4 | 96 | 0 | 16 | at most 3 |
| 5 | 768 | 0 | 16 | at most 3 |
| 6 | 7,680 | 4 | 84 | at most 3 |
| 7 | 92,160 | 0 | 36 | 4 |
| 8 | 1,290,240 | 0 | 28 | 5 |

At `m=8`, exactly 44 states require five moves to lower `Psi`; all lie at
`B_3=4`.  They split into 12 single two-owner supports and 32 single three-owner
supports.  On the parity-clean macro graph, all 404,080 states reach validity in
at most three macro steps:

```text
0:28, 1:66,844, 2:303,576, 3:33,632.
```

The cycle-level parity preprocessing frontier now extends through `m=10`:

```text
pair-safe cycles:                        342,720,
clean cycles:                            297,886,
positive-frustration cycles:              44,834,
maximum frustration index:                     3,
maximum pair-safe distance to clean:           1.
```

Every edge violated by every minimum-frustration orientation at `m=10` is hit by
a direct clean rotation; the worst audited edge still has six choices.

## Clean-cycle mobility and charge interface

At `m=10`, the clean induced successor-rotation graph is connected, has minimum
degree 69, and every owner triple is met by at least 40 clean rotations.  The
first 1,588 clean rank-one parity graphs do not break connectivity or
owner-intersecting targetability.

For one atomic three-owner flaw `A`, define on clean cycles

```text
v(rho)=2^c(rho),
w_A(rho)=2^(c(rho)-r_A(rho)),
f_A(rho)=w_A(rho)/v(rho).
```

The optimal one-step merged charge is the weighted Hall ratio

```text
gamma_A^*=max_(empty != U subseteq X_A) w_A(U)/v(N(U)).
```

For the canonical fibre-weighted reversible clean-cycle kernel `K`, running `t`
cycle steps and then regenerating the target clean fibre gives the exact charge

```text
gamma_A(t)=||K^t f_A||_infinity.
```

Thus weighted expansion, spectral mixing, and pointwise mixing are equivalent
routes to controlling label merging in the cycle coordinate.

## Regeneration, causality, and the logarithmic window

For one realized deletion followed by `t` lazy local steps,

```text
inserted blocks <= 3(t+1),
new or first-appearing flaws = O((t+1)n^2 log n).
```

The all-hold trajectory gives

```text
gamma_A(t)>=2^(-t)gamma_A(0).
```

Therefore three-owner probability-scale charge requires at least
`3 log_2 n-O(1)` steps.  At `t=O(log n)`, the realized flaw light cone is only
`O(n^2 log^2 n)`.  The remaining upper-bound problem is quantitative mixing of
the clean cycle coordinate together with a signed implementation that retains
this geometric locality.

## Finite diagnostics

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_strict_descent_horizon_m8.cpp \
  -o /tmp/check_hamilton_strict_descent_horizon_m8
/tmp/check_hamilton_strict_descent_horizon_m8

g++ -O3 -std=c++17 \
  scripts/check_hamilton_m8_critical_witnesses_and_clean_macro.cpp \
  -o /tmp/check_hamilton_m8_critical_witnesses_and_clean_macro
/tmp/check_hamilton_m8_critical_witnesses_and_clean_macro

g++ -O3 -std=c++17 \
  scripts/check_hamilton_parity_frustration_descent.cpp \
  -o /tmp/check_hamilton_parity_frustration_descent
/tmp/check_hamilton_parity_frustration_descent

g++ -O3 -std=c++17 \
  scripts/check_hamilton_m10_pair_safe_clean_mobility.cpp \
  -o /tmp/check_hamilton_m10_pair_safe_clean_mobility
/tmp/check_hamilton_m10_pair_safe_clean_mobility
```

The exact suites now include all compatible owner pairs through `m=80`, selected
constraint-incidence censuses through `m=60`, every `m=8` signed state and clean
macro state, every pair-safe frustration core through `m=10`, and all
`43,545,600` successor rotations at `m=10`.

## Current constructive targets

1. prove an asymptotic bounded clean-macro horizon or a weighted Lyapunov theorem;
2. prove that the `O(log m)` frustration core can be hit and cleaned by bounded or
   logarithmically many successor rotations while retaining pair safety;
3. prove asymptotic connectedness and polynomial owner-intersecting degree of the
   clean-cycle graph;
4. prove a spectral gap, log-Sobolev inequality, evolving-set bound, or weighted
   Hall expansion for the fibre-weighted clean-cycle kernel;
5. compare the stationary clean flaw mass `mu_cl(A)` with `Theta(m^-3)`;
6. implement clean-cycle heat flow on signed states without losing the
   trajectory-local geometric light cone;
7. convert the resulting charge and light-cone estimates into a witness-sequence
   or partial-rejection termination theorem;
8. construct a biased cyclic-order measure suppressing frustrated parity cycles
   and high-collateral assignments while retaining tractable cylinders.

The next available theorem identifier is `PP3bnz`.  The asymptotic
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.
