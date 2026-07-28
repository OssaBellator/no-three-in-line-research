# Injective locally coupled direct-clean repair at `m=10`

`docs/344` proves that every one of the `12,786,720` optimal positive signed
Hamilton states at `m=10` has a covering locally coupled rotation directly into
the parity-clean manifold. Exactly 74 of those states have no such repair with
the sign mask fixed. This chapter resolves the finite predecessor-collision
question for that direct-clean action by constructing one globally injective
choice of repair.

No asymptotic matching or strict contraction theorem is claimed.

## 1. Fixed-sign direct-clean graph

Fix an owner-sign mask `e`. Let `S_e` be the optimal positive states
`(rho,e)`. Join `(rho,e)` to `(eta,e)` when one three-owner successor rotation
changes `rho` to `eta` and the unchanged sign mask is clean on `eta`.
Owner locality implies that every such edge automatically covers all violated
source parity edges.

The graph is bipartite: sources are optimal positive signed states and targets
are clean signed states with the same sign mask.

### Theorem PP3bra -- VERIFIED FINITELY / COMPLETE FIXED-SIGN MATCHINGS

At `m=10` the fixed-sign graph has

```text
12,786,646 nonisolated sources,
423,160,022 labelled edges,
1,024 sign-mask fibres.
```

Every sign-mask fibre has a matching covering all of its nonisolated sources.
There are exactly 74 isolated sources, agreeing with the fixed-sign exception
census in `docs/331` and `docs/344`.

#### Verification

For each sign mask independently, the checker compresses the clean target
cycles, builds the exact direct-clean adjacency list, and runs Hopcroft--Karp.
All 1,024 matching deficits are zero. The union of the fibre matchings assigns
distinct clean signed targets to all `12,786,646` fixed-sign nonexceptions. ∎

This is stronger than a fractional Hall certificate: it gives a deterministic
one-step action on every nonexception state.

## 2. Augmenting the 74 locally coupled exceptions

For each fixed-sign-isolated source `(rho,e)`, retain every labelled locally
coupled direct-clean target `(eta,e')` for which

```text
e' xor e is supported on the rotated owner triple.
```

After duplicate target states are removed, the 74 exception sources have 564
candidate clean targets in total.

### Theorem PP3brb -- VERIFIED FINITELY / GLOBAL AUGMENTING COMPLETION

The union of the 1,024 fixed-sign matchings extends to a matching covering all
`12,786,720` optimal positive signed states.

Under the deterministic matching produced by the checker:

```text
34 exceptions enter an unused clean target directly;
40 exceptions require one fixed-sign source to be rerouted;
maximum augmenting path source count = 2.
```

The complete augmentation explores only

```text
114 source vertices,
410 target vertices
```

across all 74 searches.

#### Verification

The checker begins with the complete fixed-sign matchings from PP3bra. It then
inserts the exception sources sequentially. An alternating breadth-first
search traverses locally coupled edges from exception sources and fixed-sign
edges from displaced ordinary sources. Every search reaches a free target.
The final occupied-target count is exactly `12,786,720`, with no duplicate
clean signed target. ∎

Thus the locally coupled signs are needed only to enter the matching; the
necessary rerouting remains one fixed-sign edge deep in this exact audit.

## 3. Reverse-collision consequence

### Corollary PP3brc -- PROVED / ONE-STEP NONAMPLIFYING SWITCH

There exists a deterministic covering direct-clean policy at `m=10` whose
signed target-column load is at most one:

```text
max_y sum_x P(x,y) <= 1.
```

Equivalently, the direct-clean action has reverse indegree at most one on the
complete optimal positive source family.

#### Proof

PP3brb assigns one clean target to every source and assigns no target twice.
The deterministic transition matrix therefore has one unit in each source row
and at most one unit in each target column. ∎

After clean fibre regeneration and any stochastic clean-cycle heat step, the
`L^infinity` inherited density still cannot increase. Unlike `docs/349`, this
result does not provide a factor strictly below one; it removes amplification
at the first nonforest size and isolates strict contraction as the remaining
quantitative problem.

Compile and run the exact certificate with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_covering_repair_injective_matching.cpp \
  -o /tmp/check_m10_covering_repair_injective_matching

OMP_NUM_THREADS=8 \
  /tmp/check_m10_covering_repair_injective_matching
```

## 4. Revised collision frontier

The finite collision picture is now:

1. target-optimal fixed-sign strict repair is fractionally contractive through
   `m=9` by `docs/349`;
2. direct covering repair at `m=10` admits an integral globally injective
   locally coupled policy;
3. only 74 sources need cross-sign-fibre edges, and every resulting augmenting
   path has at most two sources in the audited matching;
4. the open step is to obtain a uniform margin below one, preferably by a
   geometric weighting or several balanced injective layers that persist in the
   logarithmic frustration window.

The next theorem identifier after this chapter is `PP3brd`.
