# Asymptotic prime-minus-one seed frontier

This index begins after the finite certificate suite was completed for every odd
prime through `73`. It records the remaining asymptotic seed problem and the
most compressed currently verified probability, dependency, repair, and
regeneration interfaces.

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

## Current complete repair interface

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

The one-step raw potentials still have local minima, but exhaustive directed
reachability for `m=4,5,6` shows maximum distance at most three from every state
to the global minimum defect level. Thus targetability is closed; scheduling
and collateral control remain open.

## Current regeneration interface

Let `K_m` be the balanced lazy combined chain: hold with probability `1/2`, flip
a random orientation with probability `1/4`, and perform a random signed
three-edge rotation with probability `1/4`.

Its spectral gap satisfies

```text
gap(K_m) = Omega(m^-5).
```

Consequently worst-case pointwise `epsilon`-mixing takes

```text
O(m^6 log m + m^5 log(1/epsilon))
```

steps. If `R_A` is any targeted deletion kernel for flaw `A`, then

```text
S_A = R_A K_m^t
```

has pointwise output density in `[1-epsilon,1+epsilon]` relative to the uniform
measure and uniform-measure flaw charge

```text
gamma_A <= (1+epsilon) mu(A).
```

This is approximate regeneration. The flaw may recur after mixing, as required
by the exact-oracle impossibility.

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

python scripts/check_hamilton_adjacent_transposition_embedding.py \
  experiments/hamilton-adjacent-transposition-embedding-audit.json
```

The cycle-family diagnostic verifies thirteen pair-2-cycle-free public/code
cases, nine Hamilton or one-fixed cases, `46,234` weighted pair permutations,
and `39,380` path-forest cylinders. The switching diagnostic verifies `5,910`
Hamilton states and `310,104` directed moves. The drift diagnostic exhausts
`8,544` signed Hamilton states and `134,432` targeted bad-triple occurrences.
The combined-repair diagnostic constructs `269,392` directed flaw-targeted
edges and proves distance at most three to global minima through `m=6`. The
mixing comparison diagnostic verifies `34,404` exact adjacent-transposition
embeddings through `m=8`.

## Current constructive targets

Several naive endpoints are closed:

1. raw one-step defect potentials are not monotone and have local minima;
2. source/target coordinate overlap is too dense for ordinary or standard
   cluster-expansion LLL criteria;
3. guaranteed immediate flaw deletion is not an exact resampling oracle;
4. the former two-owner targetability gap is closed by orientation flips.

The remaining plausible routes are sharper:

1. prove a geometrically weighted or two/three-step Lyapunov theorem using the
   complete flaw kernel;
2. prove a substantially smaller lopsided or causal graph using slope,
   cyclic-separation, incompatibility, or witness information;
3. combine delete-then-mix charges with a nonexact flaw-walk, partial-rejection,
   or witness-sequence criterion;
4. prove warm-start mixing so full worst-case regeneration is not paid after
   every deletion;
5. introduce a biased stationary cyclic-order measure that suppresses
   high-collateral assignments while retaining tractable cylinders.

The asymptotic prime-minus-one seed theorem and the no-three-in-line conjecture
remain open.
