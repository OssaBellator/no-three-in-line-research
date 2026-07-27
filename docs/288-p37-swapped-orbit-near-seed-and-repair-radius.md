# A four-line p=37 near-seed and its exact signed-orbit repair radius

The swapped quarter-turn orbit CSP of PP3bey gives a compact search space for
`p=37`, where `n=36` and there are `m=18` reversal-pair vertices.  A signed
cycle-cover search reaches a state with only one quarter-turn orbit of bad
lines.  This chapter records that near-state and exhausts every canonical
signed-orbit repair changing at most six pair assignments.

No such repair succeeds.  Thus this near-state has signed-orbit repair radius
at least seven inside the swapped quarter-turn class.  The result is local and
finite: it neither proves that no `p=37` seed exists nor gives an asymptotic
obstruction.

## 1. The audited swapped-equivariant state

Use the two permutation layers

```text
sigma =
[22,36,24,16,25,9,14,6,32,8,26,17,7,33,19,3,35,27,
 10,2,34,18,4,30,20,11,29,5,31,23,28,12,21,13,1,15],

tau =
[2,17,21,14,9,29,24,27,31,18,11,5,3,30,1,33,25,15,
 22,12,4,36,7,34,32,26,19,6,10,13,8,28,23,16,20,35].
```

### Proposition PP3bfc -- VERIFIED FINITELY

Both arrays are permutations, they are edge-disjoint, `sigma` commutes with
coordinate reversal, and

```text
tau=sigma^(-1) o J.
```

Their union has exactly four collinear triples:

```text
(3,24),  (19,22), (35,20),
(15,19), (17,35), (13,3),
(20,2),  (22,18), (24,34),
(34,13), (2,17),  (18,15).
```

The four supporting lines form one orbit under quarter-turn rotation.  Every
other maximal grid line has occupancy at most two.

#### Verification

The finite checker reconstructs all `72` selected cells, tests all

```text
binom(72,3)=59640
```

integer determinants, and groups the four zero determinants by their exact
primitive line equations. ∎

The state is therefore a near-seed, not a valid certificate.

## 2. Its signed pair cycle cover

The signed pair data are, in zero-based pair indices,

```text
rho =
[14,0,12,15,11,8,13,5,4,7,10,16,6,3,17,2,1,9],

e =
[1,1,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1].
```

### Proposition PP3bfd -- VERIFIED FINITELY

The pair-cycle partition of `rho` is

```text
[11,6,1].
```

All four bad lines contain points from exactly the same three old orbit blocks,
whose one-based source-pair indices are

```text
3,15,17.
```

#### Verification

Decode each signed edge by PP3bev and identify the unique orbit owner of every
selected cell in the four bad triples.  Each triple has owner set
`{3,15,17}`. ∎

Consequently every repair must replace at least one of these three orbit
assignments.

## 3. Canonical signed-orbit support

For a signed cycle cover `(rho,e)`, canonically replace the orientation of a
self-loop by zero, since PP3bex gives

```text
O(i,i,0)=O(i,i,1).
```

For another signed cycle cover `(rho',e')`, define its orbit support by

```text
A={i:(rho'(i),e'_i) differs canonically from (rho(i),e_i)}.
```

### Proposition PP3bfe -- PROVED

Fix an orbit support `A`.  The incoming and outgoing cycle-cover equations
force the multiset of new targets on `A` to be exactly `rho(A)`.  Therefore all
repairs of exact support `A` are enumerated by:

1. every permutation of the old targets `rho(A)`;
2. every orientation choice on non-self-loop new edges;
3. canonical orientation zero on new self-loops;
4. rejection of any source whose canonical signed assignment did not change;
5. rejection of oppositely oriented directed two-cycles.

#### Proof

Outside `A`, every outgoing edge and its target remain fixed.  Since every
pair vertex must still have one incoming edge, the changed sources must use the
complementary target multiset `rho(A)`.  The remaining items are precisely the
orientation choices, exact-support condition, self-loop quotient, and
duplicate-orbit criterion PP3bex. ∎

This includes target rearrangements, pure orientation flips, and mixed moves.

## 4. Exact line-delta test

### Proposition PP3bff -- PROVED

For one fixed support `A`, remove its old four-cell orbit blocks from the base
line occupancies.  Add the candidate replacement blocks one cell at a time.  A
candidate is valid exactly when:

1. no new block duplicates an unchanged block;
2. no affected maximal nonaxis line ever exceeds occupancy two; and
3. every previously overloaded line has final occupancy at most two.

Lines not meeting an old or new changed cell retain their base occupancy.

#### Proof

Orbit matching and PP3bex preserve saturation and distinctness.  The displayed
updates compute exact selected-cell occupancy on every affected line.  An
unaffected line is unchanged.  PP3bcy then makes occupancy at most two
identical to the no-three condition. ∎

The implementation uses integer primitive-direction line generation and no
floating-point geometry.

## 5. Complete support census through six

### Proposition PP3bfg -- VERIFIED FINITELY

After the necessary requirement that the support meet `{3,15,17}`, the exact
numbers of canonical signed-orbit candidates are:

| orbit support | candidates checked |
|---:|---:|
| 1 | 3 |
| 2 | 225 |
| 3 | 9,500 |
| 4 | 347,811 |
| 5 | 11,090,546 |
| 6 | 315,267,140 |

The total is

```text
326,715,225.
```

#### Verification

For every support subset, the checker performs the complete enumeration of
PP3bfe and independently counts the surviving canonical exact-support
assignments.  Support six is partitioned into eight disjoint subset-index
shards; their counts sum to `315,267,140`. ∎

### Theorem PP3bfh -- VERIFIED FINITELY

None of the `326,715,225` candidates is a saturated no-three seed.

#### Verification

Every enumerated candidate satisfies the signed cycle-cover matching equations
by construction.  Duplicate reverse orbits are removed by PP3bex, and every
remaining candidate is tested by the exact line-delta criterion PP3bff.  No
candidate leaves all maximal-line occupancies at most two. ∎

### Corollary PP3bfi -- VERIFIED FINITELY

The canonical signed-orbit repair radius of the audited `p=37` near-state is at
least seven.

This is a stronger local obstruction than absence of one elementary switch:
it includes all combinations of target reassignment and orientation change on
up to six pair vertices.

## 6. Exact p=37 orbit-CSP dimensions

### Proposition PP3bfj -- VERIFIED FINITELY

For `p=37`, the canonical swapped-orbit CSP PP3bey has:

```text
m=18 pair vertices,
630 binary orbit variables,
306 duplicate-orbit inequalities,
70726 maximal nonaxis line inequalities,
```

in addition to the `36` incoming and outgoing equalities.

#### Verification

Insert `m=18` into `2m^2-m` and `m(m-1)`.  Primitive-direction enumeration of
`[36]^2` gives `70,726` maximal nonaxis lines containing at least three grid
cells. ∎

A bounded HiGHS feasibility run on this exact model and diversified signed
local searches did not produce a valid certificate.  This is reported only as
search status, not as an infeasibility proof.

## 7. Revised p=37 frontier

### Corollary PP3bfk -- PROVED / FINITE BARRIER RECORDED

The first missing canonical certificate after `p=31` now has both:

1. a compact exact `630`-variable swapped-orbit formulation; and
2. a verified four-line near-state whose local orbit radius is at least seven.

The next productive targets are an exact orbit-CSP certificate, a support-seven
or larger structured switch, stronger cycle-cover propagation, or import and
independent verification of a public `n=36` configuration.  No `p=37`
certificate is claimed in this chapter.

The asymptotic prime-minus-one seed theorem and the no-three-in-line conjecture
remain unproved.