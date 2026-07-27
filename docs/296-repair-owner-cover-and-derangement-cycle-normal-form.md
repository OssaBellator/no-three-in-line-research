# Repair owner covers and the derangement-cycle normal form

The exact repair searches at `p=37` and `p=41` admit two reductions that are
independent of those board sizes.

First, once the changed source set is fixed, target conservation identifies the
new target assignment with a derangement of that support.  Every target repair
is therefore a disjoint family of cycle switches.

Second, each overloaded line gives a weighted covering inequality on the owners
of its selected cells.  Quarter-turn rotation preserves the complete owner
multiplicity vector, so one representative from each bad-line orbit suffices.

These reductions are exact search interfaces.  They do not assert that a
remaining branch is feasible and do not prove the asymptotic seed theorem.

## 1. Exact support derangement

Let `rho` be the base pair permutation, let `rho'` be a repaired pair
permutation, and put

```text
A={i: rho'(i) != rho(i)}.
```

### Proposition PP3bhj -- PROVED

Define

```text
g=rho^(-1) o rho'.
```

Then `g` fixes every vertex outside `A`, maps `A` to itself, and `g|A` is a
derangement.  Conversely, every derangement `g_A` of `A`, extended by the
identity outside `A`, gives the unique exact-support target reassignment

```text
rho'=rho o g_A.
```

#### Proof

Outside `A`, equality of `rho` and `rho'` gives `g(i)=i`.  The unchanged sources
retain exactly the targets `rho([m]\A)`.  Since `rho'` is a permutation, the
changed sources must use the complementary target set `rho(A)`.  Hence `g`
maps `A` bijectively to itself.  Exact support is equivalent to `g(i) != i` for
every `i` in `A`.

Conversely, composition with a derangement supported on `A` preserves
bijectivity, agrees with `rho` outside `A`, and changes every source in `A`.
Applying `rho^(-1)` proves uniqueness. ∎

### Corollary PP3bhk -- PROVED

For exact support size `k`, the number of possible target reassignments is the
subfactorial

```text
!k.
```

In particular, exact support one is impossible before any geometric constraint
is considered.

## 2. Cycle-switch factorisation

### Proposition PP3bhl -- PROVED

Every exact repair target map has a unique factorisation into disjoint cycles
of length at least two.  A cycle

```text
(i_1 i_2 ... i_r)
```

sends source `i_j` to the old target `rho(i_(j+1))`, cyclically.

If the derangement cycle type is

```text
lambda=(2^a_2 3^a_3 ...),
```

then the number of labelled target maps with that type is

```text
k! / product_r (r^(a_r) a_r!).
```

#### Proof

Use the unique disjoint-cycle decomposition of `g_A` from PP3bhj and the
identity `rho'=rho o g_A`.  The counting formula divides `k!` by cycle rotations
and by permutations among equal-length cycles. ∎

Thus an exact solver may branch on cycle type, then labelled cycle switches,
and only afterward on signed orientations.  Target uniqueness is built into
the branch object.

## 3. Weighted bad-line owner covers

Write a swapped-quarter-turn state as a disjoint union of signed orbit blocks
`O_i`.  For a selected maximal line `L`, define

```text
mu_L(i)=|O_i intersect L|,
q_L=sum_i mu_L(i).
```

### Theorem PP3bhm -- PROVED

If `A` is the support of any valid repair, then every bad base line satisfies

```text
sum_(i in A) mu_L(i) >= q_L-2.
```

#### Proof

Blocks owned outside `A` remain selected.  Their inherited contribution to the
repaired line is

```text
q_L-sum_(i in A) mu_L(i).
```

A valid line contains at most two selected cells, giving the inequality. ∎

This is necessary, not sufficient: replacement blocks may add cells back to
the same line or create new overloaded lines.

### Corollary PP3bhn -- PROVED

One representative from each quarter-turn orbit of bad lines supplies all
owner-cover inequalities for that orbit.

#### Proof

Quarter-turn rotation preserves each orbit block setwise and therefore
preserves every owner multiplicity `mu_L(i)`. ∎

For a bad triple with three distinct owners, the weighted inequality reduces
to the ordinary hitting condition that at least one of those owners changes.

## 4. Exact owner-cover and cycle-first search

### Proposition PP3bho -- PROVED

Let the representative bad-line constraints be

```text
sum_i mu_j(i) x_i >= d_j,
```

where `d_j=q_j-2`.  Exact support subsets of size `k` may be restricted without
loss to binary solutions of these inequalities and

```text
sum_i x_i=k.
```

For every surviving support, PP3bhj replaces the unrestricted target-matching
stage by a derangement of that support.

#### Proof

The support inequalities are necessary by PP3bhm, and the derangement
correspondence is bijective by PP3bhj. ∎

A canonical exact search order is therefore

```text
weighted owner-cover support,
derangement cycle type,
labelled cycle switches,
signed orientations,
residual maximal-line capacities.
```

Residual Hall tests remain useful after line-capacity and orientation deletions,
because those deletions may remove some target choices inside an initially
valid cycle branch.

## 5. Finite p=37 and p=41 audit

### Proposition PP3bhp -- VERIFIED FINITELY

For the two audited four-line near-states, the bad-line owner multisets are
constant around their quarter-turn orbits:

```text
p=37: {3:1,15:1,17:1},
p=41: {15:1,18:1,20:1}.
```

The weighted cover number is one.  The complete minimum-cover families are

```text
p=37: {3},{15},{17},
p=41: {15},{18},{20}.
```

Consequently the number of support subsets of size `k` surviving the owner
filter is

```text
C(m,k)-C(m-3,k).
```

At support thirteen this gives

```text
p=37:  8,463 subsets,
p=41: 75,140 subsets.
```

#### Verification

Run

```bash
python scripts/check_repair_owner_cover_and_derangement_cycles.py \
  experiments/p37-swapped-quarter-turn-near-example.json \
  experiments/p41-swapped-quarter-turn-near-example.json
```

The checker reconstructs every signed orbit block, assigns the unique owner of
each bad-triple cell, verifies the weighted covers by exhaustive subset
enumeration, and compares every support count with the binomial formula. ∎

## 6. Support-thirteen cycle census

### Proposition PP3bhq -- VERIFIED FINITELY / EXACTLY COUNTED

For support thirteen,

```text
13! = 6,227,020,800,
!13 = 2,290,792,932,
13!/!13 = 2.718281828538486...
```

The derangements split into exactly `24` cycle types, the partitions of
thirteen with no part one.  The type formula in PP3bhl sums exactly to `!13`.
The single-cycle type `[13]` contains

```text
12! = 479,001,600
```

target maps.

#### Verification

The diagnostic computes subfactorials by

```text
!k=(k-1)(!(k-1)+!(k-2))
```

and independently sums all labelled cycle-type counts through `k=13`. ∎

## 7. Revised frontier

The unresolved `p=41` support-thirteen search separates into

```text
75,140 owner-feasible supports,
24 target cycle types on each support,
and signed geometric feasibility after target assignment.
```

The next exact solver should branch on cycle switches directly, propagate
weighted owner covers from all bad-line orbits, and retain Hall propagation
after geometric option deletion.

No support-thirteen `p=41` repair is claimed.  The `p=41` seed, the asymptotic
prime-minus-one seed theorem, and the no-three-in-line conjecture remain open.
