# Min-plus critical graphs for tied marker schedules

`docs/519` obtains eventual residue formulas when one marker block has strictly
smallest mean cost. A geometric controller can instead have several tied
periodic blocks. This chapter replaces the unique-block argument by the
critical graph of the associated min-plus system.

Let `G=(V,E)` be a finite directed graph. Each edge has unit duration, rational
cost `c_e`, and a rational action vector `a_e`. Positive-duration macro edges
are covered by subdividing them into unit edges. Write `F_uv(N)` for the
minimum cost of a length-`N` walk from `u` to `v`.

## 1. Eventual min-plus periodicity

### Theorem PP3clb -- PROVED / CRITICAL-GRAPH QUASIPERIODICITY

Let `mu` be the minimum directed-cycle mean cost. There is a positive integer
`Gamma` such that, on every residue class modulo `Gamma` containing arbitrarily
long `u`--`v` walks, there are constants `beta_r` and `N_r` with

```text
F_uv(N)=mu N+beta_r
```

for all `N>=N_r` in that residue. Equivalently,

```text
F_uv(N+Gamma)=F_uv(N)+Gamma mu
```

eventually on every attainable residue.

#### Proof

Clear cost denominators and write `mu=a/b`. The edge weights `bc_e-a` have no
negative directed cycle. Shortest-path potentials therefore give numbers
`h_v` for which

```text
r_e=bc_e-a+h_tail(e)-h_head(e)>=0.
```

Edges lying on a minimum-mean cycle have zero total reduced cost; the union of
all zero-reduced cycles is the critical graph. For each attainable residue,
a fixed entry walk, a sufficiently long critical walk, and a fixed exit walk
give a uniform upper bound on the reduced cost of an optimum. Hence an optimal
long walk uses only a bounded number of positive-reduced edges. Removing those
bounded pieces leaves walks in finitely many critical strongly connected
components. In each such component, sufficiently long walk lengths are
periodic modulo the gcd of its directed-cycle lengths. Taking a common multiple
of these cyclicities and minimizing over the finitely many entry and exit types
gives the displayed formula. ∎

## 2. Critical action-rate polytope

### Theorem PP3clc -- PROVED / TIED-CRITICAL RATE POLYTOPE

The limiting average action vectors of walks whose cost is `mu N+O(1)` form the
convex hull of the mean action vectors of the accessible critical cycles.
Every rational point of this polytope has a deterministic periodic realization
up to a bounded entry, exit, and residue correction.

#### Proof

The reduced-cost argument in `PP3clb` bounds the number of noncritical edges in
an asymptotically optimal walk. Empirical frequencies on the remaining
critical edges converge, after taking subsequences, to normalized circulations.
Cycle decomposition expresses every such circulation as a convex combination
of critical cycles. Conversely, clear the denominators of any rational convex
combination, concatenate the requested critical cycles, and add fixed bounded
connectors. ∎

## 3. Finite exact critical-graph audit

### Theorem PP3cld -- PROVED / MIN-PLUS RESIDUE CERTIFICATE

Exact minimum-cycle-mean computation, zero-reduced-edge extraction, critical
cyclicity, and a finite min-plus dynamic program give a complete certificate for
`PP3clb`. Stored predecessors reconstruct one optimal schedule in every
residue; repeated normalized dynamic-programming states certify the eventual
period.

#### Proof

All quantities are rational and the graph is finite. Minimum cycle mean and
shortest-path potentials are exact finite computations. Once the normalized
cost vector and its residue repeat, min-plus determinism forces the subsequent
orbit to repeat with the corresponding affine cost increment. ∎

## 4. Stored exact fixture

The audit `scripts/check_multicritical_marker_minplus.py` uses three macro
blocks:

```text
P: length 2, cost 2, action vector (2,0),
Q: length 4, cost 4, action vector (0,4),
R: length 1, cost 2, action vector (1,0).
```

`P` and `Q` tie at critical mean one and have critical cyclicity two. Through
length 400 the exact optimum is

```text
F(N)=N     for even N,
F(N)=N+1   for odd N.
```

The critical action-rate polytope is the full segment
`conv((1,0),(0,1))`; the finite attained mesh is at most `4/N`.

## 5. Prime-patching consequence

Boundary marker controllers may now retain several equally efficient periodic
repair modes. Exact large-side formulas and deterministic rates come from the
finite critical graph rather than from an artificial choice of one preferred
cycle.
