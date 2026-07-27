# Reproducible p=41 support-thirteen cycle-first sampling

The derangement normal form PP3bhj reduces a fixed-support repair to a target
cycle switch followed by signed orientation choices.  This chapter applies that
order to the unresolved support-thirteen frontier of the audited `p=41`
near-state.

Two deterministic trial streams are recorded:

1. a single thirteen-cycle on each sampled support; and
2. a uniformly rejected derangement on each sampled support.

For every sampled target map, the remaining orientation problem is solved by
exact residual line-capacity search.  The experiment finds no repair, but it is
not exhaustive over support-thirteen target maps and therefore proves neither
infeasibility nor a stronger radius lower bound.

## 1. Fixed target maps leave only orientation search

Fix an exact support `A` and a derangement `g_A`.  By PP3bhj the repaired pair
permutation is

```text
rho'=rho o g_A.
```

Every changed source now has a fixed target and at most two canonical
orientation options.

### Proposition PP3bhr -- PROVED

For a fixed pair `(A,g_A)`, the following search returns a repair if and only if
one exists with that support and target derangement:

1. remove the old orbit blocks on `A`;
2. retain every old block outside `A`;
3. for each changed source, generate the one or two canonical orientations of
   its fixed target edge;
4. delete an orientation if its orbit duplicates a retained orbit or alone
   exceeds a residual maximal-line capacity;
5. branch on a source with minimum remaining orientation-domain size;
6. update exact integer line occupancies and used orbit blocks;
7. accept exactly when all changed sources are assigned.

#### Proof

PP3bhj fixes the target of every changed source.  The signed orbit normal form
PP3bew leaves only its canonical orientation choices.  Duplicate-orbit deletion
is exact by PP3bex, and residual line deletion is exact by PP3bft.  Every
surviving orientation is explicitly branched, so every canonical signed cover
with the fixed target map is reached.  Incremental line capacities are exactly
the maximal-line criterion PP3bcy. ∎

The raw leaf bound is at most `2^13=8192`, and geometric deletion usually makes
the actual tree much smaller.

## 2. Schedule-independent trial generation

### Proposition PP3bhs -- PROVED / IMPLEMENTED

The diagnostic trial indexed by `t` derives its random generator from

```text
splitmix64(master_seed xor t).
```

It reconstructs the ordered label set before every shuffle.  Therefore the
support and target derangement of each trial depend only on

```text
(mode, master_seed, t),
```

not on OpenMP scheduling or thread count.

#### Verification

The two recorded streams were run with both eight and thirty-two threads.  All
aggregate counters agree exactly. ∎

This schedule independence was added after a preliminary audit detected that
reusing mutable shuffled labels across trials made aggregate counts depend on
worker assignment.  No result from that preliminary version is retained.

## 3. Single-cycle trial stream

Mode zero chooses a uniformly shuffled cyclic ordering of the thirteen support
vertices and uses the resulting one-cycle derangement.

### Proposition PP3bht -- VERIFIED FINITELY

For

```text
trials=500000,
seed=20260731,
mode=0,
```

the deterministic ledger is

```text
owner-cover pass                    484660
initial empty orientation domain   477997
nonempty initial domain               6663
orientation DFS nodes                14673
duplicate-orbit rejections                0
node-cap hits                             0
repair found                             no
```

Since no trial reaches the `100000`-node ledger cap, PP3bhr completely decides
every owner-feasible sampled target map in this stream.

#### Verification

Compile and run the commands in
`experiments/p41-support13-derangement-orientation-sampling.md`.  The eight- and
thirty-two-thread runs produce the same counters. ∎

The trials are not deduplicated.  This is a complete decision of the recorded
trial stream, not of all labelled thirteen-cycles on all supports.

## 4. Uniform-derangement trial stream

Mode one shuffles the support image until no fixed point remains.  Rejection
from the uniform permutation distribution gives a uniform derangement on that
fixed support.

### Proposition PP3bhu -- VERIFIED FINITELY

For

```text
trials=500000,
seed=20260801,
mode=1,
```

the deterministic ledger is

```text
owner-cover pass                    484660
initial empty orientation domain   478071
nonempty initial domain               6589
orientation DFS nodes                14417
duplicate-orbit rejections                0
node-cap hits                             0
repair found                             no
```

Again, no trial reaches the node ledger cap, so every owner-feasible sampled
target map is completely decided by PP3bhr.

#### Verification

Run the recorded command at both thread counts.  The counters agree exactly. ∎

## 5. Initial orientation-domain barrier in the sample

### Proposition PP3bhv -- FINITE DIAGNOSTIC RECORDED

Among owner-feasible trials, the proportions rejected before orientation
branching are

```text
single thirteen-cycle: 477997/484660 = 0.9862522180...,
uniform derangement:    478071/484660 = 0.9864049024....
```

The surviving nonempty-domain trials require only

```text
14673/6663 = 2.202161...,
14417/6589 = 2.188040...
```

orientation DFS nodes on average, respectively.

#### Verification

These are exact ratios of the integer counters in PP3bht and PP3bhu. ∎

This does not establish a limiting probability or a bound for every support.
It records that, in these two deterministic samples, the principal rejection
occurs before orientation interaction: at least one changed source already has
no orientation compatible with the retained orbit blocks and residual line
capacities.

## 6. Revised support-thirteen frontier

### Corollary PP3bhw -- FINITE SEARCH STATUS

The cycle-first decomposition is computationally effective on sampled target
maps, but the support-thirteen decision remains open.  Productive exact next
steps are:

```text
precompute source-target residual feasibility signatures for each support,
branch on derangement cycles using those signatures,
learn owner-cover and empty-domain conflicts across support subsets,
and retain exact orientation search only for surviving target maps.
```

The sample contains no `p=41` repair.  It does not prove support-thirteen
infeasibility, does not raise the radius lower bound beyond thirteen, and does
not prove the asymptotic seed theorem.

## 7. Diagnostic

Compile and run

```bash
g++ -O3 -std=c++17 -fopenmp \
  scripts/sample_p41_support13_derangement_orientations.cpp \
  -o /tmp/sample_p41_support13

/tmp/sample_p41_support13 500000 32 20260731 0
/tmp/sample_p41_support13 500000 32 20260801 1
```

The exact ledger is stored in
`experiments/p41-support13-derangement-orientation-sampling.json`.
