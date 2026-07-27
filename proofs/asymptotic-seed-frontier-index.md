# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`. It records the remaining asymptotic seed problem and the
most compressed currently verified probability, dependency, repair,
regeneration, causality, and scheduling interfaces.

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
| Exact-oracle dichotomy | Guaranteed deletion by one targeted move is incompatible with exact restoration of the uniform Hamilton measure | PROVED | `docs/306` |
| Complete flaw targeting | Every bad triple has two or three orbit owners and is deleted by a support-one orientation flip or support-three successor rotation | PROVED / VERIFIED FINITELY | `docs/307` |
| Short finite reachability | Every signed Hamilton state through `m=6` reaches its global minimum defect level in at most three flaw-targeted moves | VERIFIED FINITELY | `docs/307` |
| Polynomial unconditioned mixing | A balanced lazy combined chain has spectral gap `Omega(m^-5)` by adjacent-transposition comparison | PROVED / VERIFIED FINITELY | `docs/308` |
| Delete-then-mix regeneration | Targeted deletion followed by polynomial mixing restores the uniform measure pointwise within `1+-epsilon` and gives charge at most `(1+epsilon)mu(A)` | PROVED | `docs/308` |
| Atomic warm starts | Exact deletion images are polynomially warm and total-variation regeneration takes `O(m^5[log m+log(1/epsilon)])` | PROVED / VERIFIED FINITELY | `docs/309` |
| Bounded-horizon descent | A uniform `D`-step strict-descent property would give termination in at most `D Phi(x_0)` moves | PROVED | `docs/310` |
| Exact `m=7` reachability | All `92,160` signed Hamilton states reach one of `36` valid states; maximum distance and strict-descent horizon are four | VERIFIED FINITELY | `docs/310` |
| Immediate causal locality | A newly created flaw must touch a newly inserted orbit block; immediate outdegree is `O(n^2 log n)` | PROVED / VERIFIED FINITELY | `docs/311` |
| Residual three-owner scale | Three-owner atomic flaws have probability--causal-degree product `O(log n/n)=o(1)` | PROVED | `docs/311` |
| Two-owner parity preprocessing | For a fixed Hamilton cycle, all two-owner flaws form a signed-graph XOR system solvable and countable in linear time | PROVED / VERIFIED FINITELY | `docs/312` |

## Exact theorem ranges

| IDs | Statement | Status | Location |
|---|---|---|---|
| PP3biy--PP3bjf | Two-cycle-free generating function, near-Hamilton counts, exact cylinders, retained first-moment barrier, and finite suite audit | PROVED / VERIFIED FINITELY | `docs/302-two-cycle-free-near-hamilton-signed-cover-measures.md` |
| PP3bjg--PP3bjl | Three-edge Hamilton closure, involution, connectivity, reversible signed kernel, and targeted triple destruction | PROVED / VERIFIED FINITELY | `docs/303-hamilton-three-edge-switching-repair-kernel.md` |
| PP3bjm--PP3bjp | Reversible zero-drift identity, negative average targeted drift, best-sign increases, local minima, and targetability gaps | PROVED / VERIFIED FINITELY | `docs/304-targeted-hamilton-switching-drift-and-local-minima.md` |
| PP3bjq--PP3bjs | Coordinate clique, logarithmic symmetric-LLL failure, and arbitrary-weight cluster-expansion failure | PROVED | `docs/305-hamilton-coordinate-clique-lll-and-cluster-barriers.md` |
| PP3bju--PP3bjw | Guaranteed-deletion versus exact-restoration impossibility and stationarity-targeting dichotomy | PROVED | `docs/306-targeted-switching-resampling-oracle-dichotomy.md` |
| PP3bjx--PP3bkc | Orbit-owner dichotomy, orientation-flip repair, complete combined targeting, reversible combined graph, and short finite reachability | PROVED / VERIFIED FINITELY | `docs/307-complete-hamilton-flaw-targeting-and-short-reachability.md` |
| PP3bkd--PP3bkh | Balanced lazy chain, adjacent-transposition comparison, polynomial spectral gap, pointwise mixing, and delete-then-mix approximate regeneration | PROVED / VERIFIED FINITELY | `docs/308-delete-then-mix-approximate-regeneration.md` |
| PP3bki--PP3bkl | Atomic flaw probabilities, injective deletion images, exact warmness, spectral contraction, and faster total-variation regeneration | PROVED / VERIFIED FINITELY | `docs/309-atomic-flaw-warm-start-regeneration.md` |
| PP3bkm--PP3bkp | Bounded-horizon descent lemma, exact `m=7` reachability, four-step finite descent, and revised scheduling frontier | PROVED / VERIFIED FINITELY | `docs/310-bounded-horizon-hamilton-descent-and-m7-reachability.md` |
| PP3bkq--PP3bku | New-block locality, fixed-block flaw count, sparse immediate causality, residual probability scale, and finite causality census | PROVED / VERIFIED FINITELY | `docs/311-immediate-hamilton-flaw-causality-and-residual-scale.md` |
| PP3bkv--PP3bkz | Reflection parity invariance, exact two-owner XOR reduction, signed-graph solution count, finite parity census, and orientation preprocessing | PROVED / VERIFIED FINITELY | `docs/312-two-owner-hamilton-flaws-as-a-parity-csp.md` |

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

The static coordinate-overlap graph is closed as a direct route. Its largest
source-coordinate clique has size `Omega(n^3 log n)`, so the product of one
event probability and one clique size is `Omega(log n)`. This blocks both the
symmetric local lemma and the standard cluster-expansion criterion on that
graph.

## Current complete repair and descent interface

A four-cell quarter-turn orbit is a square, so a line contains at most two cells
from one owner. Every bad triple therefore has exactly two or three owners.

```text
two owners:   flip either owner orientation;
three owners: rotate the three pair successors and choose fresh signs.
```

Both moves delete the selected flaw and remain inside the signed Hamilton state
space. The unconditioned union is connected, symmetric, and regular of degree

```text
m + 8 C(m,3).
```

The one-step raw potentials still have local minima. However, exhaustive
directed reachability through `m=7` shows that every nonoptimal state reaches a
strictly lower total triple count within at most four flaw-targeted moves. At
`m=4,5,7` the global minimum is zero; at `m=6` the Hamilton subfamily minimum is
four.

A uniform bounded-horizon theorem would immediately telescope to termination.
The finite value four is evidence, not an asymptotic bound.

## Current regeneration interface

Let `K_m` be the balanced lazy combined chain: hold with probability `1/2`, flip
a random orientation with probability `1/4`, and perform a random signed
three-edge rotation with probability `1/4`. Its spectral gap satisfies

```text
gap(K_m) = Omega(m^-5).
```

Worst-case pointwise regeneration takes

```text
O(m^6 log m + m^5 log(1/epsilon))
```

steps. Atomic deletion outputs are only polynomially warm, so total-variation
regeneration improves to

```text
O(m^5[log m + log(1/epsilon)]).
```

The delete-then-mix charge remains within a factor `1+epsilon` of the stationary
atomic flaw probability.

## Current causal and parity interface

Immediate deletion causality is much sparser than static coordinate overlap.
A newly created flaw contains a newly inserted block, and one fixed block lies
in only `O(n^2 log n)` atomic flaws. Hence immediate causal outdegree is
`O(n^2 log n)`.

Atomic probabilities split by owner count:

```text
two owners:   Theta(n^-2),
three owners: Theta(n^-3).
```

Thus the probability--causal-degree products are

```text
two owners:   O(log n),
three owners: O(log n/n)=o(1).
```

The two-owner subsystem can be removed before dynamic repair. Horizontal board
reflection complements both signs on an owner pair, so every two-owner predicate
depends only on `e_i xor e_j`. For a fixed Hamilton cycle, all such flaws form a
signed parity graph. Consistency is decided by cycle parity, and a satisfiable
graph with `c` components has exactly `2^c` clean orientation vectors.

After parity preprocessing, every remaining flaw has three owners and lies at
the favorable `O(log n/n)` immediate-causal scale. Turning this scale into a
valid directed flaw-walk or witness theorem is the main remaining probabilistic
task.

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
```

The exact suites now include `92,160` signed Hamilton states and `4,427,088`
directed combined-flaw edges at `m=7`, `10,416` atomic deletion-image checks
through `m=6`, `2,376,384` immediate causal edges through `m=6`, and all
Hamilton-cycle parity systems through `m=7`.

## Current constructive targets

Several naive endpoints are closed:

1. raw one-step defect potentials are not monotone and have local minima;
2. source/target coordinate overlap is too dense for ordinary or standard
   cluster-expansion LLL criteria;
3. guaranteed immediate flaw deletion is not an exact resampling oracle;
4. the former two-owner targetability gap is closed by orientation flips;
5. the full two-owner orientation subsystem is now an exact parity CSP.

The remaining plausible routes are sharper:

1. prove a uniform bounded strict-descent horizon or a weighted multi-step
   Lyapunov theorem;
2. combine parity preprocessing with the residual three-owner
   `O(log n/n)` causal scale in a directed flaw-walk or witness-sequence theorem;
3. exploit delete-then-mix charges without paying full mixing after every local
   deletion;
4. prove that sequences of deletion outputs remain polynomially warm;
5. introduce a biased cyclic-order measure that suppresses high-collateral
   assignments while retaining tractable cylinders.

The next available theorem identifier is `PP3bla`. The asymptotic
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.
