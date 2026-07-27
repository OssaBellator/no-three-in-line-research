# A four-line p=41 near-state and its Hall-propagated repair radius

The swapped quarter-turn orbit model now closes the first missing finite target
`p=37`, but the next prime `p=41` remains open in the canonical repository
suite.  This chapter records a rigorously verified state on `[40]^2` with only
one quarter-turn orbit of bad lines and exhausts every canonical signed-orbit
repair changing at most twelve pair assignments.

No repair succeeds.  Hence this particular near-state has canonical orbit
repair radius at least thirteen.  This is a local finite obstruction: it does
not prove that no `p=41` seed exists and it does not rule out another search
basin.

## 1. Quarter-turn bad-line owners

Let a swapped-equivariant selected set be written as a disjoint union of its
four-cell orbit blocks

```text
S = union_i O_i.
```

For a selected cell `x`, call the unique index `i` with `x in O_i` its orbit
owner.

### Proposition PP3bgn -- PROVED

Let `R` be quarter-turn rotation.  If a selected triple on a line `L` has orbit
owner multiset `B`, then its rotated triple on `R^q(L)` has the same owner
multiset `B` for every integer `q`.

Consequently every repair of the complete bad-line orbit must alter at least
one orbit assignment whose index lies in `B`.

#### Proof

Each orbit block `O_i` is invariant as a set under `R`.  Therefore rotating a
cell owned by `i` produces another cell owned by the same `i`.  Rotation also
preserves collinearity, so the rotated triple lies on `R^q(L)` with exactly the
same owner multiset.  If no assignment indexed by `B` changes, the original
triple and all its rotations remain selected. ∎

This gives an exact support filter before any line-capacity or Hall search.

## 2. The audited p=41 state

Use the two one-based permutation layers

```text
sigma =
[22,20,28,27,10,6,11,39,25,40,33,4,15,34,18,12,38,17,36,32,
 9,5,24,3,29,23,7,26,37,8,1,16,2,30,35,31,14,13,21,19],

tau =
[10,8,17,29,19,35,14,11,20,36,34,25,3,4,28,9,23,26,1,39,
 2,40,15,18,32,13,37,38,16,7,5,21,30,27,6,22,12,24,33,31].
```

### Proposition PP3bgo -- VERIFIED FINITELY

Both arrays are permutations of `[40]`, they differ in every column, and their
union has exactly four collinear triples:

```text
(15,18), (18,17), (9,20),
(20,32), (17,23), (18,26),
(21,9),  (23,15), (24,18),
(23,24), (26,23), (32,21).
```

The four supporting lines form one orbit under quarter-turn rotation.  Every
other selected triple has nonzero integer determinant.

#### Verification

The exact diagnostic reconstructs all eighty selected cells, verifies two
points in every row and column, and tests all

```text
binom(80,3)=82160
```

integer determinants.  Exactly the four displayed determinants vanish. ∎

Thus the state is a near-seed, not a valid `p=41` certificate.

## 3. Signed pair data and relative cycles

The near-state has signed pair cover

```text
rho =
[19,20,13,14,10,6,11,2,16,1,8,4,15,7,18,12,3,17,5,9],

e =
[1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1].
```

### Proposition PP3bgp -- VERIFIED FINITELY

The pair-cycle lengths and their orientation xor parities are

```text
lengths  [10,5,4,1],
parities [ 0,0,1,0].
```

The lift theorem PP3bfm therefore gives the full relative-cycle partition

```text
[10,10,10,4,4,2].
```

Direct traversal of `pi=sigma^(-1) o tau` gives the same partition.

The four bad triples all have the same owner set

```text
{15,18,20}.
```

#### Verification

Decode every signed assignment into its four-cell block, identify the unique
owner of every bad-triple cell, and traverse the pair and relative
permutations.  PP3bgn explains why the owner set is preserved around the
quarter-turn orbit. ∎

Every valid repair must therefore change at least one of these three pair
assignments.

## 4. Exact residual Hall search

Fix an exact canonical support `A`.  By PP3bfs, the changed sources must use
exactly the target set `rho(A)`.  Remove the old blocks on `A`, retain all
unchanged blocks, and generate every canonical signed option from a source in
`A` to a target in `rho(A)`.

### Proposition PP3bgq -- PROVED

The following decision procedure is complete for one fixed support `A`:

1. delete the old signed assignment at every source in `A`;
2. reject options duplicating an unchanged orbit block;
3. reject options exceeding any residual maximal-line capacity;
4. reject if a source domain is empty;
5. test the remaining source-to-target graph for a perfect matching;
6. branch on a source of minimum current option-domain size;
7. update exact integer line occupancies, used targets, and used orbit blocks;
8. repeat the Hall test at every node.

It returns a repair if and only if one exists on exact support `A`.

#### Proof

Target conservation is PP3bfs.  Residual line deletions are exact by PP3bft,
and Hall rejection is exact by PP3bfu.  The remaining steps only choose branch
order and explicitly visit every surviving target and orientation option.
Every leaf is therefore one legal canonical signed cycle cover on `A`, and the
line-capacity test is equivalent to no three collinear by PP3bcy. ∎

## 5. Complete support census through twelve

By PP3bgn, a support must meet `{15,18,20}`.  Thus the number of support subsets
of size `k` is

```text
C(20,k)-C(17,k).
```

### Proposition PP3bgr -- VERIFIED FINITELY

The exact aggregate statistics are:

| support | support subsets | search nodes | Hall failures | initial empty domains |
|---:|---:|---:|---:|---:|
| 1 | 3 | 0 | 0 | 3 |
| 2 | 54 | 0 | 0 | 54 |
| 3 | 460 | 0 | 0 | 460 |
| 4 | 2,465 | 1 | 1 | 2,464 |
| 5 | 9,316 | 17 | 12 | 9,303 |
| 6 | 26,384 | 145 | 140 | 26,242 |
| 7 | 58,072 | 2,184 | 1,976 | 56,003 |
| 8 | 101,660 | 22,084 | 16,722 | 82,799 |
| 9 | 143,650 | 125,989 | 57,848 | 68,038 |
| 10 | 165,308 | 473,569 | 136,125 | 25,492 |
| 11 | 155,584 | 1,660,399 | 428,754 | 4,030 |
| 12 | 119,782 | 6,864,013 | 1,763,428 | 248 |
| **total** | **782,738** | **9,148,401** | **2,405,006** | **275,136** |

The support-subset counts agree with the displayed binomial formula in every
row.

### Theorem PP3bgs -- VERIFIED FINITELY

No canonical signed-orbit repair of the audited `p=41` near-state has support
at most twelve.

#### Verification

For every support subset meeting the necessary bad-owner set, PP3bgq exhausts
all legal signed target assignments and orientations.  The larger supports are
partitioned into disjoint subset-index shards.  Every shard reports
`found=0`. ∎

### Corollary PP3bgt -- PROVED / VERIFIED FINITELY

The canonical signed-orbit repair radius of the audited state satisfies

```text
h_orbit >= 13.
```

This is the same lower bound that preceded the successful support-thirteen
repair at `p=37`, but no support-thirteen `p=41` completion is claimed here.

## 6. Revised p=41 frontier

### Corollary PP3bgu -- PROVED / FINITE BARRIER RECORDED

The next finite target now has:

```text
m=20 pair vertices,
780 canonical orbit variables,
380 duplicate-orbit inequalities,
108190 maximal nonaxis line inequalities,
a verified four-line near-state,
and an exact local radius lower bound of thirteen.
```

The public archive directory lists a bulk `n40_rot4` configuration file, but no
configuration from that file is used in this chapter: the raw content was not
materialised in the present environment and therefore was not treated as a
certificate.

The next productive routes are:

```text
support-thirteen or larger exact repair,
a different signed-orbit near-state basin,
global branch-and-cut on the 780-variable orbit CSP,
cycle-parity-guided branching,
or independent retrieval and verification of one public n=40 code.
```

The `p=41` seed, the asymptotic prime-minus-one seed theorem, and the
no-three-in-line conjecture remain open.

## 7. Diagnostics

Run

```bash
python scripts/check_p41_swapped_orbit_near_state.py \
  experiments/p41-swapped-quarter-turn-near-example.json

g++ -O3 -std=c++17 \
  scripts/check_p41_swapped_orbit_repair_branch_bound.cpp \
  -o /tmp/check_p41_orbit_branch
```

The exact support commands and aggregate results are recorded in
`experiments/p41-swapped-orbit-repair-branch-bound.md` and
`experiments/p41-swapped-orbit-repair-branch-bound-results.json`.
