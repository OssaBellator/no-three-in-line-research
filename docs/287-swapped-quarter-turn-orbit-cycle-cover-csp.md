# Swapped quarter-turn seeds as a signed orbit cycle-cover CSP

The swapped quarter-turn normal form of PP3bei uses one permutation `sigma`
commuting with coordinate reversal and forces

```text
tau=sigma^(-1) o J.
```

There is a still smaller exact encoding.  Pair each column with its reversal.
One signed assignment between two reversal pairs selects one complete
quarter-turn orbit of four board cells.  The entire seed is therefore a signed
cycle cover on `n/2` pair vertices with linear maximal-line capacities.

This chapter is an exact equivalence for the swapped-equivariant class.  It does
not assert that every seed has quarter-turn symmetry, and it does not prove the
asymptotic prime-minus-one seed theorem.

## 1. Reversal-pair coordinates

Put `n=2m`.  Represent a board coordinate by

```text
(i,b),
0<=i<m,
b in {0,1},
```

where `(i,0)` is coordinate `i` and `(i,1)` is `J(i)=n-1-i`.
A permutation commuting with `J` has the signed form

```text
sigma(i,b)=(rho(i), b xor e_i),
```

where `rho` is a permutation of `[m]` and `e_i` is a bit.

For pair indices `i,j` and orientation `e`, define the four-cell set

```text
O(i,j,0)=
{(i,j),(J(i),J(j)),(j,J(i)),(J(j),i)},

O(i,j,1)=
{(i,J(j)),(J(i),j),(j,i),(J(j),J(i))}.
```

Coordinates in these displays are ordinary board coordinates.

### Proposition PP3bev -- PROVED

If the signed assignment of `sigma` at pair `i` is

```text
rho(i)=j,
e_i=e,
```

then the two points contributed by `P_sigma` at the source columns of pair `i`
and the two points contributed by `P_tau` at the columns of pair `j` have union
exactly `O(i,j,e)`.

#### Proof

For `e=0`,

```text
sigma(i)=j,
sigma(J(i))=J(j).
```

Thus `sigma^(-1)(j)=i` and `sigma^(-1)(J(j))=J(i)`.  Since
`tau(x)=sigma^(-1)(J(x))`, the two `tau` points are

```text
(j,J(i)), (J(j),i).
```

Together these are `O(i,j,0)`.  The calculation for `e=1` reverses the two
images in each pair and gives `O(i,j,1)`. ∎

Thus one signed matching edge already packages one complete geometric
quarter-turn orbit.

## 2. Signed cycle-cover bijection

### Proposition PP3bew -- PROVED

Swapped-equivariant ordered layer pairs are in bijection with signed directed
cycle covers on the `m` reversal-pair vertices:

1. every vertex `i` has one outgoing edge `(i,rho(i),e_i)`;
2. every vertex `j` has one incoming edge; and
3. the selected cell set is the union of the corresponding orbit blocks
   `O(i,rho(i),e_i)`.

Ignoring edge-disjointness and no-three constraints, the number of signed cycle
covers is

```text
2^m m!.
```

#### Proof

This is the signed-permutation representation of PP3bej.  PP3bev identifies the
selected orbit block of each signed assignment. ∎

## 3. Duplicate-orbit and collision criterion

### Proposition PP3bex -- PROVED

For distinct pair vertices `i,j`,

```text
O(i,j,e)=O(j,i,1-e).
```

All other orbit blocks selected by a signed cycle cover are disjoint.  Hence the
two permutation layers are edge-disjoint exactly when the cycle cover contains
no oppositely oriented directed two-cycle:

```text
not both (i,j,e) and (j,i,1-e).
```

For a self-loop,

```text
O(i,i,0)=O(i,i,1),
```

so one may canonically keep only orientation zero on self-loops when searching
selected sets.

#### Proof

The displayed orbit equalities follow by listing their four cells.  A cell in
an orbit determines its unordered source-target pair indices.  Therefore two
blocks with different unordered pair-index sets cannot intersect.  For the
same two distinct indices, the only duplicate encoding is the displayed
reverse edge with complementary orientation.

In permutation language, a directed two-cycle `rho(i)=j,rho(j)=i` gives
`sigma^2=J` on those coordinate pairs exactly when `e_i xor e_j=1`, which is
the edge collision criterion of PP3bei.  A self-loop has two layer colourings
of the same four-cell orbit. ∎

## 4. Exact binary orbit CSP

Use binary variables

```text
z_(i,j,e),
0<=i,j<m,
e in {0,1},
```

with only `e=0` retained when `i=j`.
For a maximal nonaxis grid line `L`, put

```text
a_(L,i,j,e)=|L cap O(i,j,e)|.
```

### Theorem PP3bey -- PROVED

A swapped-quarter-turn saturated no-three selected set on `[2m]^2` is
equivalent to a zero-one solution of:

1. one outgoing signed edge per pair vertex,
   ```text
   sum_(j,e) z_(i,j,e)=1;
   ```
2. one incoming signed edge per pair vertex,
   ```text
   sum_(i,e) z_(i,j,e)=1;
   ```
3. no duplicate reverse orbit,
   ```text
   z_(i,j,e)+z_(j,i,1-e)<=1
   ```
   for `i<j` and both orientations; and
4. every maximal-line capacity,
   ```text
   sum_(i,j,e) a_(L,i,j,e) z_(i,j,e)<=2.
   ```

The model has

```text
2m^2-m
```

canonical binary variables and `m(m-1)` duplicate-orbit inequalities before
line constraints.

#### Proof

Items 1--2 select a signed cycle cover.  By PP3bev its edge blocks produce the
swapped-equivariant pair `(sigma,tau)`.  PP3bex makes item 3 exactly the
edge-disjointness and distinct-orbit condition.  The coefficient in item 4 is
the number of selected cells contributed to `L` by that orbit, so the sum is
exactly the occupancy of `L`.  PP3bcy makes all line capacities equivalent to
no three collinear.

Conversely, a swapped-equivariant seed has a signed cycle cover by PP3bew;
PP3bex and no-three validity imply items 3--4.  Self-loop orientation
canonicalisation does not change the selected set. ∎

This removes the inverse permutation from the optimisation model: both layers
are already present inside each orbit variable.

## 5. Exact coefficient generation

### Proposition PP3bez -- PROVED

Every coefficient `a_(L,i,j,e)` lies in `{0,1,2,3,4}` and is computed by four
integer membership tests.  If it is at least three, the variable
`z_(i,j,e)` is individually forbidden.  Otherwise no triple enumeration is
needed: primitive-direction maximal-line generation gives the complete linear
system.

#### Proof

Each orbit block has four cells.  The coefficient is their exact intersection
count with `L`.  A single selected orbit containing three cells of one line is
already invalid.  Completeness of primitive-direction line generation is
PP3bcz. ∎

## 6. Pair-cycle structure of stored quarter-turn seeds

For a signed cycle cover, call the cycle partition of `rho` its *pair-cycle
partition*.

### Proposition PP3bfa -- VERIFIED FINITELY

The swapped-equivariant decompositions of the eight stored quarter-turn
certificates have pair-cycle partitions:

| `p` | `m=(p-1)/2` | pair cycles of `rho` | relative cycles of `pi` |
|---:|---:|---|---|
| 17 | 8 | `[8]` | `[8,8]` |
| 19 | 9 | `[5,4]` | `[10,2,2,2,2]` |
| 23 | 11 | `[10,1]` | `[5,5,5,5,2]` |
| 29 | 14 | `[13,1]` | `[26,2]` |
| 31 | 15 | `[10,4,1]` | `[5,5,5,5,2,2,2,2,2]` |
| 61 | 30 | `[29,1]` | `[58,2]` |
| 67 | 33 | `[32,1]` | `[16,16,16,16,2]` |
| 73 | 36 | `[36]` | `[36,36]` |

Every decoded orbit cycle cover satisfies all matching, duplicate-orbit, and
maximal-line constraints, while its orbit union exactly reconstructs the
archive-selected set.

#### Verification

Run

```bash
python scripts/check_swapped_quarter_turn_orbit_csp.py \
  experiments/archived-prime-seed-codes.json
```

The checker first repeats the exact determinant verification, solves the
swapped parity colouring, derives `(rho,e)`, reconstructs all orbit blocks, and
checks the linear occupancy system. ∎

The finite data favour a long pair cycle, often with one fixed pair, but this
is a heuristic observation rather than a valid restriction.

## 7. Revised structured frontier

### Corollary PP3bfb -- PROVED AS AN EQUIVALENCE

Within swapped quarter-turn symmetry, the global seed problem is now an exact
signed orbit cycle-cover problem with linear line capacities.  A future route
may therefore use:

```text
cycle-cover branch and bound,
SAT or integer programming on orbit variables,
random signed cycle covers with structured conditioning,
or local switches on pair cycles.
```

The reduction is substantial, but existence of a feasible orbit cycle cover
for every sufficiently large `m` is unproved.  Nor is it known that the
unrestricted seed theorem can be reduced to quarter-turn symmetry.  The
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.