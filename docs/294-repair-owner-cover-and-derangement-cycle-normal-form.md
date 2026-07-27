# Repair owner covers and the derangement-cycle normal form

The exact repair searches at `p=37` and `p=41` use two reductions that can be
separated from those particular board sizes.

First, once the changed source set is fixed, target conservation does more than
produce a bipartite matching problem: the new target assignment is exactly a
derangement of the changed sources, composed with the old pair permutation.
Thus every repair is a disjoint family of cycle switches.

Second, every overloaded line imposes a weighted covering inequality on the
owners of its selected cells.  Quarter-turn rotation preserves that owner
multiplicity vector, so one representative of each bad-line orbit suffices.
These constraints give a support filter before any orientation or line-capacity
branching.

The reductions are exact.  They do not prove that the remaining repair search
has a feasible leaf, and they do not prove the asymptotic prime-minus-one seed
theorem.

## 1. Exact support derangement

Let `rho` be the base pair permutation on `[m]`, let `rho'` be a repaired pair
permutation, and let

```text
A={i: rho'(i) != rho(i)}.
```

Outside `A`, the two permutations agree.

### Proposition PP3bgv -- PROVED

Define

```text
g = rho^(-1) o rho'.
```

Then `g` fixes every vertex outside `A`, maps `A` to itself, and its restriction
`g|A` is a derangement.  Conversely, every derangement `g_A` of `A`, extended by
the identity outside `A`, gives the unique target reassignment

```text
rho' = rho o g_A
```

with exact support `A`.

#### Proof

For `i` outside `A`, `rho'(i)=rho(i)`, hence `g(i)=i`.

The unchanged sources use exactly the targets `rho([m]\A)`.  Since `rho'` is a
permutation, the changed sources must use the complementary target set
`rho(A)`, as in PP3bfs.  Therefore `rho'(i)` lies in `rho(A)` for every `i` in
`A`, so `g(i)=rho^(-1)(rho'(i))` lies in `A`.  Because `rho'` and `rho` are
bijections, `g|A` is a permutation of `A`.

Finally, exact support means `rho'(i) != rho(i)` for each `i` in `A`, which is
equivalent to `g(i) != i`.  Thus `g|A` is a derangement.

Conversely, if `g_A` is a derangement of `A` and the identity elsewhere, then
`rho o g_A` is a permutation, agrees with `rho` outside `A`, and differs from it
at every vertex of `A`.  Uniqueness follows by applying `rho^(-1)`. ∎

This identifies the target part of the repair search independently of all
orientation and geometric constraints.

### Corollary PP3bgw -- PROVED

For an exact support of size `k`, the number of possible target reassignments is
exactly the subfactorial

```text
!k.
```

In particular, support one is impossible before geometry is considered.

#### Proof

PP3bgv is a bijection between target reassignments and derangements of the
support. ∎

## 2. Cycle-switch factorisation

A derangement has no one-cycles, so its cycle decomposition consists entirely
of cycles of length at least two.

### Proposition PP3bgx -- PROVED

Every exact repair target map has a unique factorisation into disjoint cycle
switches

```text
(i_1 i_2 ... i_r),  r>=2,
```

where the switch sends source `i_j` to the old target `rho(i_(j+1))`, cyclically.
Conversely, every disjoint family of such cycles on `A` gives one exact target
reassignment on `A`.

If the cycle lengths are the partition

```text
lambda=(2^a_2 3^a_3 ...),
```

then the number of derangements with that cycle type is

```text
k! / product_r (r^(a_r) a_r!).
```

#### Proof

Apply the unique disjoint-cycle decomposition to the derangement `g_A` from
PP3bgv.  The identity `rho'=rho o g_A` gives the displayed target action.
The standard labelled permutation count divides `k!` by the cyclic rotations
of each cycle and by permutations among cycles of equal length. ∎

Thus an exact search may branch first on a cycle partition, then on labelled
cycles, and only afterward on signed orientations.  Target uniqueness is then
built into the branch object rather than repeatedly tested by matching.

## 3. Weighted bad-line owner covers

Write a swapped-quarter-turn state as the disjoint union of signed orbit blocks
`O_i`.  For a selected maximal line `L`, define

```text
mu_L(i)=|O_i intersect L|,
q_L=sum_i mu_L(i).
```

A line is bad when `q_L>2`.

### Theorem PP3bgy -- PROVED

Let `A` be the support of any repair.  For every bad line `L` of the base state,

```text
sum_(i in A) mu_L(i) >= q_L-2.
```

#### Proof

Every orbit block with owner outside `A` remains unchanged.  Hence the repaired
line still contains at least

```text
sum_(i notin A) mu_L(i)
 = q_L-sum_(i in A) mu_L(i)
```

selected cells inherited from the base state.  A valid repair has line
occupancy at most two, so this inherited contribution must be at most two.
Rearranging gives the inequality. ∎

This is a necessary condition only: changing an owner removes its old block but
the replacement block may add new cells to the same line or create other bad
lines.

### Corollary PP3bgz -- PROVED

Choose one representative from each quarter-turn orbit of bad lines.  The
weighted inequalities from those representatives imply the inequalities for
all rotated lines in the orbit.

#### Proof

Quarter-turn rotation preserves every orbit block setwise.  It therefore
preserves each owner multiplicity `mu_L(i)`, as in PP3bgn. ∎

The bad-line owner system is consequently a finite weighted set-cover instance
on the pair vertices.  Its optimum is a rigorous lower bound on repair support.
For triple lines with three distinct owners, the inequality reduces to the
ordinary hitting-set condition that at least one owner must change.

## 4. Exact support filtering

### Proposition PP3bha -- PROVED

Let the representative bad-line owner constraints be

```text
sum_i mu_j(i) x_i >= d_j,
```

where `x_i` records membership in the repair support and `d_j=q_j-2`.
Then exact support subsets of size `k` may be restricted, without loss, to the
binary solutions of

```text
sum_i x_i=k
```

together with all owner-cover inequalities.

After a support survives this filter, PP3bgv replaces the target-matching stage
by a derangement on that support.

#### Proof

The owner inequalities are necessary by PP3bgy, and PP3bgv is an exact
bijection for every surviving support. ∎

This gives the canonical exact search order

```text
owner-cover support,
derangement cycle type,
labelled cycle switches,
signed orientations,
residual maximal-line capacities.
```

Hall propagation remains useful after orientation and line-capacity deletions,
because those deletions can destroy some target choices inside an initially
valid derangement branch.

## 5. Finite audit at p=37 and p=41

### Proposition PP3bhb -- VERIFIED FINITELY

For both audited four-line near-states, the four bad triples form one
quarter-turn line orbit and have a constant owner multiset with three distinct
owners:

```text
p=37: {3:1,15:1,17:1},
p=41: {15:1,18:1,20:1}.
```

The weighted owner-cover number is one.  The complete minimum-cover families
are respectively

```text
{3},{15},{17}
```

and

```text
{15},{18},{20}.
```

For support size `k`, the number of surviving support subsets is therefore

```text
C(m,k)-C(m-3,k).
```

At support thirteen this gives

```text
p=37, m=18:  8,463 subsets,
p=41, m=20: 75,140 subsets.
```

#### Verification

Run

```bash
python scripts/check_repair_owner_cover_and_derangement_cycles.py \
  experiments/p37-swapped-quarter-turn-near-example.json \
  experiments/p41-swapped-quarter-turn-near-example.json
```

The checker reconstructs every signed orbit block, assigns the unique owner of
each bad-triple cell, checks the weighted covers by exhaustive subset
enumeration, and compares every support count with the binomial formula. ∎

## 6. The support-thirteen cycle census

### Proposition PP3bhc -- VERIFIED FINITELY / EXACTLY COUNTED

For support thirteen,

```text
13! = 6,227,020,800,
!13 = 2,290,792,932,
13!/!13 = 2.718281828538486...
```

The derangements split into exactly `24` cycle types, namely the integer
partitions of thirteen with no part equal to one.  For each partition the count
is the formula in PP3bgx, and the counts sum exactly to `!13`.

The single-cycle type `[13]` contains

```text
12! = 479,001,600
```

derangements.

#### Verification

The diagnostic computes subfactorials by the exact recurrence

```text
!k=(k-1)(!(k-1)+!(k-2))
```

and independently sums the labelled cycle-type counts for every `k<=13`. ∎

## 7. Revised repair frontier

The current `p=41` support-thirteen search is not closed.  The new normal form
does, however, isolate three exact layers that should not be conflated:

```text
75,140 owner-feasible support subsets,
24 target cycle types on each support,
and signed geometric feasibility after target assignment.
```

A productive exact solver should branch on cycle switches directly, propagate
weighted owner covers across every bad-line orbit, and retain residual Hall
checks after geometric option deletion.

The `p=41` seed, the asymptotic prime-minus-one seed theorem, and the
no-three-in-line conjecture remain open.
