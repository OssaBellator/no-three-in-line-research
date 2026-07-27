# Residual-orbit MRV propagation raises the p=37 repair radius

The direct support census in PP3bfg enumerated every complete signed assignment
through support six.  At larger support this becomes wasteful: most partial
replacement systems already violate a line capacity or leave some source with
no legal unused target.

This chapter replaces complete-candidate enumeration by an exact residual
cycle-cover search.  For each support subset it removes all old orbit blocks,
then assigns the forced old target multiset back to the changed sources using
minimum-remaining-values branching and exact cell and line-capacity
propagation.

The method exhausts supports seven through eleven for the `p=37` near-state.
No complete feasible replacement exists, so its canonical signed-orbit repair
radius is at least twelve.

This is a finite local statement.  It does not prove that no `p=37` seed exists
and does not settle support twelve.

## 1. Residual support instance

Fix a canonical orbit support `A` of size `k`.  By PP3bfe, the new targets used
by the changed sources are exactly the multiset

```text
rho(A).
```

Remove the old orbit block of every source in `A`.  Keep every orbit block
outside `A` fixed.

### Proposition PP3bfs -- PROVED

After the removals, a repair with exact support `A` is equivalent to a perfect
matching from the changed sources to the target set `rho(A)`, together with one
orientation bit on every non-self-loop matched edge, such that:

1. no source receives its old canonical signed assignment;
2. self-loop orientation is canonical zero;
3. no replacement block intersects a fixed or previously selected block; and
4. every maximal nonaxis line has final occupancy at most two.

#### Proof

The target-set statement is PP3bfe.  The first two items are exactly canonical
support.  Orbit intersection detects the duplicate reverse-orbit obstruction
of PP3bex.  The last item is the line-capacity equivalence PP3bey. ∎

## 2. Exact block-capacity propagation

For an orbit variable `v=(i,j,e)`, precompute the sparse coefficient list

```text
{(L, |L cap O(i,j,e)|): |L cap O(i,j,e)|>0}.
```

### Proposition PP3bft -- PROVED

At any partial residual assignment, the orbit variable `v` is legal exactly
when:

1. its target is unused;
2. its four cells are currently unoccupied; and
3. for every coefficient pair `(L,a)`,

   ```text
   current_occupancy(L)+a<=2.
   ```

Rejecting a variable by any of these tests removes no feasible completion.

#### Proof

The first condition is the incoming cycle-cover equality.  The second is orbit
distinctness.  The third is the exact contribution of all four cells of the
candidate block to each affected line; importantly, it includes the possibility
that two cells of one orbit block lie on the same line.  Every condition is
necessary in a completed orbit cover, and adding a legal block updates exactly
these quantities. ∎

The within-block multiplicity in item 3 is essential.  A cell-at-a-time cache
that ignores two cells of the same new orbit on one line is not a valid
verifier.

## 3. Complete MRV search for one support

### Theorem PP3bfu -- PROVED

The following depth-first procedure decides exact-support feasibility.

1. Remove the old blocks of `A` and reject if a previously bad line still has
   occupancy greater than two.
2. Among unassigned sources, choose one with the fewest legal pairs
   `(unused target,orientation)` under PP3bft.
3. Branch over all of those legal pairs, updating occupied cells and sparse
   line occupancies.
4. Accept exactly at depth `|A|`.

The search returns a repair if and only if one exists with canonical support
`A`.

#### Proof

By PP3bfs, every repair is one signed perfect matching on the changed source and
target sets.  Step 2 changes only the variable order.  Step 3 branches over
every value that can occur in a feasible completion, while PP3bft removes only
impossible values.  Thus every feasible signed matching reaches one depth
`|A|` leaf, and every accepted leaf satisfies all orbit-CSP constraints. ∎

## 4. Support-subset sharding

The four bad lines use exactly the old orbit owners

```text
B={3,15,17}
```

in one-based pair indices.

### Proposition PP3bfv -- PROVED

Every repair support must meet `B`.  For support size `k`, the exact number of
eligible subsets is

```text
C(18,k)-C(15,k).
```

Assigning eligible subsets by their increasing lexicographic index modulo a
shard count partitions the support family into disjoint exhaustive shards.

#### Proof

A support disjoint from `B` removes no point from any of the four overloaded
lines, so all four survive.  The displayed count subtracts the subsets chosen
from the other fifteen vertices.  Modular indexing gives every eligible subset
one and only one shard. ∎

## 5. Exact census through support eleven

### Proposition PP3bfw -- VERIFIED FINITELY

The complete residual searches give:

| support `k` | eligible subsets | MRV nodes | complete feasible leaves |
|---:|---:|---:|---:|
| 7 | 25,389 | 53,370 | 0 |
| 8 | 37,323 | 104,270 | 0 |
| 9 | 43,615 | 221,859 | 0 |
| 10 | 40,755 | 685,654 | 0 |
| 11 | 30,459 | 2,804,211 | 0 |

In total, the checker exhausts

```text
177541 support subsets
and
3869364 MRV nodes.
```

The node counts are deterministic for the stored MRV and value ordering.  They
are search-tree nodes, not estimates of the much larger number of unpropagated
complete signed assignments.

#### Verification

Compile

```bash
g++ -O3 -std=c++17 \
  scripts/check_p37_swapped_orbit_mrv_support.cpp \
  -o /tmp/check_p37_orbit_mrv
```

For each `k=7,...,11`, run all sixteen shards:

```bash
for shard in $(seq 0 15); do
  /tmp/check_p37_orbit_mrv "$k" "$shard" 16 &
done
wait
```

The JSON summary in

```text
experiments/p37-swapped-orbit-mrv-support-summary.json
```

records the aggregate subset and node counts.  Every shard reports zero
complete leaves and no repair. ∎

### Theorem PP3bfx -- VERIFIED FINITELY

No canonical signed-orbit repair of the audited `p=37` near-state changes at
most eleven pair assignments.

#### Proof

PP3bfh excludes supports one through six.  PP3bfw excludes every support seven
through eleven. ∎

### Corollary PP3bfy -- VERIFIED FINITELY

The canonical signed-orbit repair radius of the audited near-state satisfies

```text
radius >= 12.
```

This lower bound concerns distance from one labelled near-state inside the
swapped quarter-turn class.  It is not a lower bound on the distance between
arbitrary states and is not an infeasibility result for the full `p=37` orbit
CSP.

## 6. Revised computational frontier

### Corollary PP3bfz -- PROVED / FINITE BARRIER RECORDED

The local repair route at `p=37` now requires at least two thirds of the
`m=18` pair assignments to change.  Therefore elementary local switching is
not a credible complete strategy for this near-state.

The productive exact targets are now:

```text
support twelve or larger residual search,
full 630-variable orbit-CSP feasibility,
cycle-parity propagation from PP3bfn,
stronger matching or line-cover cuts,
or independent decoding of a public n=36 certificate.
```

No `p=37` certificate is claimed.  The prime-minus-one seed theorem remains
open.