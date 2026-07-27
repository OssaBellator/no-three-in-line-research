# Signed-support fixed points and the exact p=41 radius-fourteen lower bound

The cycle-first normal form PP3bhj is exact for the set of sources whose
**targets change**. Canonical signed support is slightly broader: a source may
keep its old target and change only the orientation of its four-cell orbit.
This chapter separates those two notions, corrects the support interface, and
completes the full support-thirteen search for the audited `p=41` near-state.

Every one of the `75,140` owner-feasible signed supports is exhausted. No
repair exists, including repairs mixing target cycles with pure orientation
flips. Hence the recorded near-state has canonical signed-orbit repair radius
at least fourteen. No `p=41` seed is claimed.

## 1. Signed support versus target-change support

Let `(rho,e)` be a base canonical signed cycle cover and `(rho',e')` another
cover. Define

```text
A = {i : (rho'(i),e'(i)) != (rho(i),e(i))},
B = {i : rho'(i) != rho(i)},
F = A minus B.
```

Thus `A` is the full signed-assignment support, `B` is the target-change
support, and `F` is the pure orientation-flip set.

### Theorem PP3bij -- PROVED

Put `g=rho^(-1) o rho'`. Then:

1. `B` is contained in `A`;
2. `g` fixes every vertex outside `B`;
3. `g` maps `B` to itself and `g|B` is a derangement;
4. every `i` in `F` keeps target `rho(i)` and uses the opposite canonical
   orientation;
5. a base self-loop source `i` with `rho(i)=i` cannot lie in `F`, because its
   canonical orbit has only one orientation.

Conversely, choose a set `B` contained in `A`, a derangement `g_B` of `B`, and
put `F=A minus B`. If every vertex of `F` has a nonloop base edge, then

```text
rho' = rho o g_B
```

on `B`, `rho'=rho` elsewhere, the orientations on `F` are flipped, the old
assignments outside `A` are retained, and arbitrary canonical orientations are
chosen on the target-changed edges. Before duplicate-orbit and line-capacity
tests, this gives every signed cover with exact support `A` exactly once.

#### Proof

Sources outside `B` retain their old targets. Since both target maps are
permutations, the sources in `B` use exactly the complementary target set
`rho(B)`. Therefore `g` fixes the complement of `B`, maps `B` bijectively to
itself, and has no fixed point on `B`. A source in `F` changes its signed
assignment without changing target, so the only possible change is the other
canonical orientation; this is unavailable on a self-loop. The converse
construction reverses these steps. ∎

PP3bhj remains correct when its support is read as `B`. It is not by itself a
normal form for the full signed support `A`.

### Corollary PP3bik -- PROVED / EXACTLY COUNTED

Let

```text
Q = {i : rho(i) != i}.
```

For a fixed signed support `A` of size `k`, the number of target maps before
geometric tests is

```text
sum over F subseteq A intersect Q of !(k-|F|).
```

If `A` contains no base self-loop vertex, this sum is `k!`. If `A` contains
exactly one base self-loop vertex, it is `k!-(k-1)!`.

For the audited `p=41` state, source-pair vertex `6` is the unique fixed vertex
of `rho`. Among the `75,140` owner-feasible supports of size thirteen,

```text
48,568 contain vertex 6,
26,572 exclude vertex 6.
```

Consequently the complete signed-support target-map outer space is

```text
26,572 * 13! + 48,568 * (13!-12!)
= 444,634,193,203,200.
```

The target-change-only subspace from PP3bhq has

```text
75,140 * !13 = 172,130,180,910,480
```

target maps. Pure orientation fixed points enlarge the raw space by a factor
`2.5831274379...`.

#### Proof

Choose the pure-flip fixed set `F`; the complementary set must carry a
derangement. Summing over all admissible `F` gives the formula. The two
special cases are the standard decomposition of permutations by their fixed
set, with the self-loop vertex forbidden from that set. The displayed
`p=41` counts are direct binomial counts with the owner filter
`{15,18,20}`. ∎

## 2. Source-target symmetric exact branching

At a partial repair node, let `D_s` be the legal signed options remaining for
an unassigned source `s`. For an unused target `t`, let `D^t` be the legal
options incident with `t` among all unassigned sources.

### Proposition PP3bil -- PROVED

Every completion chooses exactly one option from each remaining source domain
and exactly one option from each remaining target domain. Therefore branching
on all options in any one `D_s` or any one `D^t` is complete. Choosing a
minimum-cardinality domain among both families is an exact source-target
symmetric MRV rule.

A Hall failure in the current source-to-target projection still rejects the
node exactly.

#### Proof

The cycle-cover equations require one outgoing edge at each source and one
incoming edge at each target. Every completion must therefore contain one
option incident with the selected source or target. The branches partition all
completions according to that unique option. Hall rejection is PP3bfu. ∎

This rule converts target singletons into actual propagation and reduces the
support-thirteen search tree substantially relative to source-only branching.

## 3. Complete support-thirteen decision procedure

For each exact signed support `A` of size thirteen meeting the necessary owner
cover `{15,18,20}`, remove the old blocks on `A` and retain all old blocks
outside `A`.

Two modes are useful:

```text
target mode: reject every option with target rho(s),
signed mode: reject only the exact old signed option at s.
```

The second mode contains the first and is the mode relevant to canonical signed
repair radius.

### Theorem PP3bim -- PROVED

For either mode, the following procedure returns a repair if and only if one
exists in that mode on the fixed support:

1. generate every individually residual-feasible canonical option;
2. reject options duplicating a retained orbit block;
3. maintain exact unused-target and unused-orbit conditions;
4. maintain every maximal-line occupancy incrementally;
5. reject a node on an empty source domain, empty target domain, or Hall
   failure;
6. branch by PP3bil;
7. accept only after all thirteen sources are assigned.

#### Proof

The initial option deletions are exact by PP3bft and PP3bid. The maintained
matching, orbit, and line constraints are exactly the signed cycle-cover CSP of
PP3bfb. PP3bil partitions every surviving completion at each branch. Hence no
legal completion is omitted and every accepted leaf is a valid repair. ∎

## 4. Exact p=41 census

### Theorem PP3bin -- VERIFIED FINITELY

All `75,140` owner-feasible supports were partitioned into `1,024` disjoint
lexicographic-ordinal shards. The complete ledgers are

| mode | supports | search nodes | Hall failures | initial empty domains | repairs |
|---|---:|---:|---:|---:|---:|
| target change only | 75,140 | 16,503,767 | 1,412,973 | 7 | 0 |
| full signed support | 75,140 | 21,604,931 | 1,851,407 | 5 | 0 |

Every shard reports `found=0`, and the shard support totals equal

```text
C(20,13)-C(17,13)=75,140.
```

#### Verification

The diagnostic reconstructs all `108190` maximal nonaxis lines, all `780`
canonical orbit variables, the retained base state, and every support. It
performs exact integer line tests and an augmenting-path Hall test at every
node. The machine-readable aggregate is stored in
`experiments/p41-support13-signed-branch-bound-results.json`. ∎

The target-mode result closes the restricted subspace studied in
PP3bhr--PP3bii. The signed-mode result additionally closes every mixed branch
with pure orientation flips.

### Corollary PP3bio -- PROVED / VERIFIED FINITELY

The earlier signed search excludes supports one through twelve, and PP3bin
excludes support thirteen. Therefore the audited near-state satisfies

```text
h_orbit >= 14.
```

No assertion is made about support fourteen.

## 5. Revised p=41 frontier

### Corollary PP3bip -- PROVED / FINITE BARRIER RECORDED

The current `p=41` local state has:

```text
one quarter-turn orbit of four bad triples,
common bad-owner set {15,18,20},
no canonical signed repair through support thirteen,
and repair radius at least fourteen.
```

The next exact routes are support-fourteen branch-and-bound, a different
near-state basin, global branch-and-cut on the `780`-variable orbit CSP, or an
independently retrieved and verified public `n=40` certificate.

The `p=41` seed, the asymptotic prime-minus-one seed theorem, and the
no-three-in-line conjecture remain open.

## 6. Diagnostic

Compile and run

```bash
g++ -O3 -std=c++17 -fopenmp \
  scripts/check_p41_support13_signed_branch_bound.cpp \
  -o /tmp/check_p41_support13_signed

/tmp/check_p41_support13_signed \
  experiments/p41-swapped-quarter-turn-near-example.json signed 8

/tmp/check_p41_support13_signed \
  experiments/p41-swapped-quarter-turn-near-example.json target 8
```
