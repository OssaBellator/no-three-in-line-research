# Hall-propagated p=37 swapped-orbit repair radius through support twelve

The four-line `p=37` near-state from PP3bfc has no canonical signed-orbit repair
of support at most six by PP3bfh.  This chapter replaces raw assignment
enumeration at the next scales by an exact constraint search using residual
line capacities and Hall propagation.

Every exact support from seven through twelve is exhausted.  No repair exists,
so the canonical signed-orbit repair radius of this near-state is at least
thirteen.

This is a local finite obstruction.  It does not prove that the swapped-orbit
CSP at `p=37` is infeasible, and it does not rule out another near-state with a
smaller repair radius.

## 1. Forced target multiset on a fixed support

Let the base signed cycle cover be `(rho,e)`, and let `A` be the exact set of
source-pair vertices whose canonical signed assignments change.

### Proposition PP3bfs -- PROVED

Every repaired cycle cover agrees with the base cover outside `A`, and the
multiset of targets used by the changed sources is exactly

```text
rho(A).
```

Consequently, a complete search on support `A` needs only:

1. one bijection from `A` to `rho(A)`;
2. one legal canonical orientation on each chosen edge;
3. exclusion of the old canonical assignment at every source;
4. exclusion of duplicate reverse orbit blocks.

#### Proof

The unchanged sources retain their outgoing edges and therefore retain all
targets in `rho([m]\A)`.  Since a cycle cover has one incoming edge at every
target vertex, the changed sources must use the complementary target set,
which is `rho(A)`.  The remaining conditions are exactly canonical signed
support and the duplicate-orbit criterion PP3bex. ∎

This is the support normal form PP3bfe with the target conservation isolated as
a matching constraint.

## 2. Residual line domains

Remove the old orbit blocks belonging to `A` and keep every old block outside
`A`.  For each maximal nonaxis line `L`, let

```text
r_A(L)=2-(number of unchanged selected cells on L)
```

be its residual capacity.

### Proposition PP3bft -- PROVED

A candidate signed edge on support `A` may be deleted immediately if its
four-cell orbit block alone exceeds some residual capacity `r_A(L)`.  This
deletion is exact.

During search, after some replacement blocks have been installed, any further
option may likewise be deleted if adding its block would make a line occupancy
exceed two.

#### Proof

All orbit contributions to a line are nonnegative.  If one candidate block
already exceeds the residual capacity before any other changed block is added,
no completion containing it can restore feasibility.  The same monotonicity
holds at every partial search node. ∎

Unlike the raw support-six enumeration, this often proves an entire support
subset impossible before branching.

## 3. Hall propagation on remaining targets

At a partial node, each unassigned source has a current set of target vertices
appearing in at least one line-feasible, orbit-distinct orientation option.

### Proposition PP3bfu -- PROVED

If the bipartite graph from unassigned sources to these current target domains
has no perfect matching, the partial node has no cycle-cover completion.

Rejecting such a node is exact.

#### Proof

Every completion must assign one distinct unused target to every unassigned
source.  These assignments form a perfect matching in the current domain
graph.  Hall failure therefore excludes every completion. ∎

The diagnostic tests this condition by a complete augmenting-path matching
algorithm at every branch node.

## 4. Complete branch-and-bound algorithm

### Theorem PP3bfv -- PROVED

For a fixed exact support `A`, the following algorithm returns a repair if and
only if one exists.

1. Remove the old blocks on `A` and compute all residual line capacities.
2. Generate every canonical signed option from each source in `A` to each
   target in `rho(A)`.
3. Delete the old assignment, duplicate unchanged orbits, and every option
   violating a residual line capacity.
4. Reject if any source domain is empty.
5. Repeatedly apply the Hall test PP3bfu.
6. Choose an unassigned source of minimum current option-domain size.
7. Branch over every remaining target and orientation option, updating exact
   integer line occupancies and used orbit blocks.
8. At a leaf, require every previously overloaded base line and every affected
   line to have occupancy at most two.

#### Proof

PP3bfs proves that the generated target set and assignments are complete.
PP3bft and PP3bfu prove that every deletion is sound.  Minimum-domain selection
changes only branch order.  Every surviving option is tried, so every legal
canonical signed cycle cover of exact support `A` is reached.  The leaf test is
exactly the maximal-line criterion PP3bcy. ∎

The algorithm is therefore an exact finite decision procedure, not a local
search heuristic.

## 5. Exhaustion of supports seven through twelve

Every repair must change at least one of the three bad-line owner assignments

```text
{3,15,17}
```

in one-based pair indices.  Hence the number of exact support subsets of size
`k` that need examination is

```text
C(18,k)-C(15,k).
```

### Proposition PP3bfw -- VERIFIED FINITELY

The complete branch-and-bound statistics are:

| support `k` | support subsets | search nodes | Hall failures | initial empty domains |
|---:|---:|---:|---:|---:|
| 7 | 25,389 | 2,778 | 2,115 | 22,980 |
| 8 | 37,323 | 22,050 | 11,475 | 22,317 |
| 9 | 43,615 | 96,108 | 28,122 | 8,499 |
| 10 | 40,755 | 338,766 | 82,859 | 1,050 |
| 11 | 30,459 | 1,391,239 | 339,893 | 36 |
| 12 | 18,109 | 6,792,398 | 1,670,204 | 0 |

In total the checker exhausts

```text
195,650 support subsets,
8,643,339 branch nodes,
2,134,668 Hall-deficient nodes,
54,882 initial empty-domain supports.
```

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_p37_swapped_orbit_repair_branch_bound.cpp \
  -o /tmp/check_p37_orbit_branch
```

using the commands in

```text
experiments/p37-swapped-orbit-repair-branch-bound.md.
```

The disjoint shard totals are recorded in

```text
experiments/p37-swapped-orbit-repair-branch-bound-results.json.
```

The support-subset totals agree with `C(18,k)-C(15,k)` for every row. ∎

### Theorem PP3bfx -- VERIFIED FINITELY

No canonical swapped-orbit repair of the audited `p=37` near-state has exact
support between seven and twelve.

#### Verification

PP3bfv exhausts every support subset and every legal signed target assignment
and orientation.  Every shard reports `found=0`. ∎

## 6. Improved local radius

### Corollary PP3bfy -- PROVED / VERIFIED FINITELY

The minimum canonical signed-orbit repair support of the audited near-state
satisfies

```text
h_orbit >= 13.
```

#### Proof

PP3bfh excludes supports one through six.  PP3bfx excludes supports seven
through twelve. ∎

This lower bound concerns changed pair-orbit assignments.  One changed orbit
assignment can alter up to four selected board cells, so it is not numerically
identical to the labelled two-layer assignment support used in the `p=17`
census.

## 7. Revised p=37 search frontier

### Corollary PP3bfz -- PROVED / FINITE BARRIER RECORDED

The recorded four-line state cannot be repaired by any small signed-orbit
switch of radius at most twelve.  Productive next routes must therefore use at
least one of:

```text
a support-thirteen or larger orbit switch,
a different near-state basin,
global branch-and-cut on the 630-variable orbit CSP,
cycle-parity branching from PP3bfm,
or independent decoding of a valid public n=36 configuration.
```

The result does not prove `p=37` infeasibility.  No `p=37` seed certificate is
claimed here.  The asymptotic prime-minus-one seed theorem and the
no-three-in-line conjecture remain unproved.
