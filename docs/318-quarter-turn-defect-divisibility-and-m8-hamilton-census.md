# Quarter-turn defect divisibility and the exact `m=8` Hamilton census

The bounded-horizon program uses the total number `B_3` of selected collinear
triples as its basic integer potential.  Swapped quarter-turn symmetry forces a
stronger arithmetic invariant: `B_3` is always a multiple of four.

This chapter proves that divisibility, gives an exact owner-interaction
decomposition, and extends the complete signed Hamilton defect census to all
`1,290,240` states at `m=8`.

No `m=8` reachability horizon or asymptotic existence theorem is claimed.

## 1. Quarter-turn orbits of bad triples

### Proposition PP3blw -- PROVED / DEFECT DIVISIBILITY

For every swapped quarter-turn signed state, the number `B_3` of selected
collinear triples satisfies

```text
B_3 is divisible by 4.
```

#### Proof

The selected cell set is invariant under the quarter-turn action.  Quarter-turn
rotation preserves collinearity, so it acts on the set of bad triples.

The board side length is even, hence the rotation centre is not a grid cell and
the quarter-turn action on cells is free: every cell orbit has size four.  A
three-element cell set cannot be invariant under a quarter-turn, because an
invariant set is a union of four-element cell orbits.  It also cannot have orbit
size two, since that would make it invariant under the half-turn, whose cell
orbits all have size two; an invariant set would then have even cardinality.

Therefore every bad-triple orbit has size exactly four.  Summing these orbits
gives the divisibility. ∎

The smallest positive defect level is consequently at least four.

## 2. Exact owner-interaction decomposition

For a signed orbit assignment `a`, write `O(a)` for its four selected cells.  For
two assignments `a,b`, let `P(a,b)` count collinear triples in
`O(a) union O(b)` using cells from both owners.  For three assignments `a,b,c`,
let `T(a,b,c)` count collinear triples using one cell from each owner.

### Proposition PP3blx -- PROVED

For every signed Hamilton state with owner assignments `a_1,...,a_m`,

```text
B_3
 = sum_(i<j) P(a_i,a_j)
 + sum_(i<j<k) T(a_i,a_j,a_k).
```

#### Proof

One four-cell quarter-turn orbit is a square, so it contains no collinear triple.
By PP3bjy every bad triple therefore has exactly two or three owners.  A two-owner
triple is counted once in the corresponding pair term, and a three-owner triple
is counted once in the corresponding triple term.  No other term contains it. ∎

This formula reduces state scoring to `C(m,2)+C(m,3)` table lookups after the
finite assignment-interaction tables have been constructed.

## 3. Exact signed-state census through `m=8`

### Theorem PP3bly -- VERIFIED FINITELY

Every signed Hamilton state for `4<=m<=8` was scored exactly using PP3blx.

| `m` | Hamilton cycles | signed states | minimum `B_3` | valid states | cycles with a valid orientation |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 96 | 0 | 16 | 2 |
| 5 | 24 | 768 | 0 | 16 | 2 |
| 6 | 120 | 7,680 | 4 | 0 | 0 |
| 7 | 720 | 92,160 | 0 | 36 | 10 |
| 8 | 5,040 | 1,290,240 | 0 | 28 | 10 |

At `m=8`, six Hamilton cycles have two valid orientations and four Hamilton
cycles have four valid orientations.  One exact valid state is

```text
rho = [2,5,3,6,7,4,1,0],
e   = [1,0,0,1,1,0,0,0].
```

Every defect level appearing in every complete distribution is a multiple of
four, independently confirming PP3blw.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_signed_defect_census_m8.cpp \
  -o /tmp/check_hamilton_signed_defect_census_m8
/tmp/check_hamilton_signed_defect_census_m8
```

The checker builds every signed directed pair assignment, precomputes exact
two-owner and three-owner collinearity tables, scores every state, and compares
the full defect-count and valid-orientation-per-cycle distributions against
hard-coded exact ledgers. ∎

## 4. Normalized descent potential

### Corollary PP3blz -- PROVED / DESCENT POTENTIAL NORMALIZED

The quantity

```text
Psi = B_3 / 4
```

is a nonnegative integer on the complete swapped quarter-turn state space and
vanishes exactly on valid states.

Consequently any `D`-step strict-descent theorem for `Psi` gives termination in
at most

```text
D Psi(x_0) = D B_3(x_0)/4
```

moves under the deterministic policy of PP3bkm.

#### Proof

Integrality and the zero set follow from PP3blw.  Apply PP3bkm to `Psi`. ∎

This normalization does not prove a shorter horizon, but it removes a redundant
factor four from every potential-level count.

## 5. Revised bounded-descent frontier

The finite state picture now extends one size beyond the complete directed
reachability census:

```text
m<=7: complete directed targeted graph and descent horizon;
m=8:  complete state/defect census, 28 valid states, graph horizon open.
```

The next exact computational target is the parity-clean or full targeted graph at
`m=8`, preferably using the same owner-interaction tables to avoid repeated
geometry.  The asymptotic target remains a uniform bounded-horizon theorem for
`Psi` or a weighted refinement that controls collateral three-owner flaws.
