# Repair owner covers and the corrected target-cycle normal form

The exact repair searches at `p=37` and `p=41` admit two reductions that are
independent of board size.

First, the sources whose **targets change** form a derangement under the old
target labelling, so target reassignment factors into disjoint cycle switches.
Second, each overloaded line gives a weighted covering inequality on the owners
of its selected cells, and that inequality constrains the full canonical signed
support.

These are different support notions. A source may keep its old target and flip
only the canonical orientation. The corrected combined interface is recorded in
PP3bho below and expanded in PP3bij. The earlier derangement statements remain
valid for target-change support; they must not be read as excluding pure
orientation flips.

## 1. Exact target-change derangement

Let `rho` be the base pair permutation, let `rho'` be a repaired pair
permutation, and put

```text
B={i: rho'(i) != rho(i)}.
```

### Proposition PP3bhj -- PROVED

Define

```text
g=rho^(-1) o rho'.
```

Then `g` fixes every vertex outside `B`, maps `B` to itself, and `g|B` is a
derangement. Conversely, every derangement `g_B` of `B`, extended by the
identity outside `B`, gives the unique exact target-change reassignment

```text
rho'=rho o g_B.
```

#### Proof

Outside `B`, equality of `rho` and `rho'` gives `g(i)=i`. The unchanged-target
sources retain exactly the targets `rho([m]\B)`. Since `rho'` is a permutation,
the target-changing sources must use the complementary target set `rho(B)`.
Hence `g` maps `B` bijectively to itself and has no fixed point there.
Conversely, composition with a derangement supported on `B` preserves
bijectivity, agrees with `rho` outside `B`, and changes every target in `B`. ∎

### Corollary PP3bhk -- PROVED

For exact target-change support size `k`, the number of possible target
reassignments is the subfactorial

```text
!k.
```

In particular, target-change support one is impossible before any geometric
constraint is considered.

## 2. Cycle-switch factorisation

### Proposition PP3bhl -- PROVED

Every exact target repair has a unique factorisation into disjoint cycles of
length at least two. A cycle

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

Use the unique disjoint-cycle decomposition of `g_B` from PP3bhj and the
identity `rho'=rho o g_B`. The counting formula divides `k!` by cycle rotations
and by permutations among equal-length cycles. ∎

Thus a target-change solver may branch on cycle type, then labelled cycle
switches, and only afterward on signed orientations.

## 3. Weighted bad-line owner covers

Write a swapped-quarter-turn state as a disjoint union of signed orbit blocks
`O_i`. For a selected maximal line `L`, define

```text
mu_L(i)=|O_i intersect L|,
q_L=sum_i mu_L(i).
```

Let

```text
A={i: the complete canonical signed assignment at i changes}.
```

### Theorem PP3bhm -- PROVED

Every valid repair satisfies

```text
sum_(i in A) mu_L(i) >= q_L-2
```

for every bad base line `L`.

#### Proof

Blocks owned outside `A` remain selected. Their inherited contribution to the
repaired line is

```text
q_L-sum_(i in A) mu_L(i).
```

A valid line contains at most two selected cells, giving the inequality. ∎

This condition is necessary, not sufficient: replacement blocks may add cells
back to the same line or create new overloaded lines.

### Corollary PP3bhn -- PROVED

One representative from each quarter-turn orbit of bad lines supplies all
owner-cover inequalities for that orbit.

#### Proof

Quarter-turn rotation preserves each orbit block setwise and therefore
preserves every owner multiplicity `mu_L(i)`. ∎

For a bad triple with three distinct owners, the weighted inequality reduces to
the ordinary hitting condition that at least one of those owners belongs to the
full signed support `A`.

## 4. Corrected owner-cover and cycle-first search

Let

```text
Q={i: rho(i) != i}
```

be the sources whose base edge has two canonical orientations.

### Proposition PP3bho -- PROVED / CORRECTED INTERFACE

A complete exact signed-support search may proceed as follows.

1. Choose a full signed support `A` satisfying every weighted owner-cover
   inequality and `|A|=k`.
2. Choose a pure orientation-flip set `F subseteq A intersect Q`.
3. Put `B=A\F` and choose a derangement of `B` by PP3bhj.
4. Flip the old orientation on every source in `F`.
5. Choose canonical orientations on the target-changed edges in `B`.
6. Apply duplicate-orbit, residual line-capacity, and Hall propagation.

This reaches every canonical signed repair of exact support `A` exactly once
before the final geometric rejection tests.

#### Proof

Every signed repair has a unique target-change set `B` and pure-flip set
`F=A\B`. PP3bhj gives the unique derangement representation on `B`. A pure
flip is possible exactly on a nonloop old edge, hence `F subseteq Q`. Conversely,
the listed choices determine the target map and every signed assignment on
`A`, while assignments outside `A` remain old. Uniqueness follows from the
unique sets `B,F`, the unique cycle decomposition, and the chosen canonical
orientations. ∎

The restricted choice `F=empty` is the target-change-only subspace studied in
`docs/297`--`docs/299`. The full signed-support search is completed in
`docs/300`.

Residual Hall tests remain useful after line-capacity and orientation deletions,
because those deletions may remove target choices inside an initially valid
cycle branch.

## 5. Finite p=37 and p=41 owner-cover audit

### Proposition PP3bhp -- VERIFIED FINITELY

For the two audited four-line near-states, the bad-line owner multisets are
constant around their quarter-turn orbits:

```text
p=37: {3:1,15:1,17:1},
p=41: {15:1,18:1,20:1}.
```

The weighted cover number is one. The complete minimum-cover families are

```text
p=37: {3},{15},{17},
p=41: {15},{18},{20}.
```

Consequently the number of full signed-support subsets of size `k` surviving
the owner filter is

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

## 6. Target-change support-thirteen cycle census

### Proposition PP3bhq -- VERIFIED FINITELY / EXACTLY COUNTED

For target-change support thirteen,

```text
13! = 6,227,020,800,
!13 = 2,290,792,932,
13!/!13 = 2.718281828538486...
```

The derangements split into exactly `24` cycle types, the partitions of
thirteen with no part one. The type formula in PP3bhl sums exactly to `!13`.
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

This census is for `F=empty`. For the audited `p=41` full signed-support family,
PP3bik gives the larger target-map outer space

```text
444,634,193,203,200.
```

## 7. Revised frontier

The corrected support interface is now closed at `p=41` through support
thirteen. The exhaustive signed search in PP3bin finds no repair, so the
audited near-state satisfies

```text
h_orbit>=14.
```

Support fourteen, a different search basin, and the global `p=41` seed remain
open. The asymptotic prime-minus-one seed theorem and the no-three-in-line
conjecture remain open.
