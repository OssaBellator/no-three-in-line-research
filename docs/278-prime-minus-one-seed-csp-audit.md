# Prime-minus-one seeds as an exact two-permutation determinant CSP

The local slab-patching architecture has reduced the global all-`n` route to one
genuinely external geometric input: for every sufficiently large prime `p`, construct a
saturated no-three-in-line set on

```text
[p-1]^2.
```

This chapter makes that seed problem exact.  Saturation is equivalent to the union of
two edge-disjoint permutation graphs.  The no-three condition is a finite family of
integer determinant inequalities.  Conversely every saturated certificate decomposes
into two permutation layers because its row--column incidence graph is bipartite and
2-regular.

The reformulation supplies a compact certificate format, an exact checker, and a
constraint-programming target.  It does not prove the asymptotic seed theorem.

## 1. Two-permutation seed states

Put

```text
n=p-1.
```

For permutations `sigma,tau` of `[n]`, define

```text
S(sigma,tau)
=
{(x,sigma(x)):x in [n]}
union
{(x,tau(x)):x in [n]}.
```

### Proposition PP3bcg -- PROVED

The set `S(sigma,tau)` has exactly two points in every row and column if and only if

```text
sigma(x) != tau(x)
```

for every `x`.

In that case `|S(sigma,tau)|=2n`.

#### Proof

Each permutation graph contributes one point to every column and one point to every
row.  The union has two distinct points in column `x` exactly when the two permutation
values differ there.  Edge-disjointness then gives `2n` distinct cells and every row
also receives one point from each layer. ∎

Thus the seed search may work directly with two permutation variables rather than
arbitrary `2n`-subsets of the board.

## 2. Exact determinant constraints

For points `a=(x_a,y_a)`, `b=(x_b,y_b)`, and `c=(x_c,y_c)`, write

```text
Delta(a,b,c)
=
(x_b-x_a)(y_c-y_a)
-
(y_b-y_a)(x_c-x_a).
```

### Proposition PP3bch -- PROVED

The two-permutation state `S(sigma,tau)` is no-three-in-line if and only if

```text
Delta(a,b,c) != 0
```

for every unordered triple of distinct cells of `S(sigma,tau)`.

All constraints are exact integer inequalities with coordinate magnitude at most
`p-1`.

#### Proof

The determinant is twice the signed Euclidean area of the triangle.  It vanishes
exactly for collinear triples. ∎

No modular relaxation is sufficient: an integer determinant may be a nonzero multiple
of `p`, and the seed problem is Euclidean rather than an affine-plane cap problem.

## 3. Every saturated certificate has two layers

Let `S subseteq [n]^2` contain exactly two points in every row and column.  Regard each
point `(x,y)` as an edge between column vertex `x` and row vertex `y`.

### Proposition PP3bci -- PROVED

The incidence graph of `S` is a disjoint union of even cycles.  Alternating the edge
colours on every component decomposes

```text
S=P_sigma dot-union P_tau
```

into two perfect matchings, hence two permutation graphs.

#### Proof

Every column and row vertex has degree two, so every connected component of the finite
bipartite graph is a cycle.  Bipartite cycles are even.  Alternating two colours gives
one incident edge of each colour at every vertex, so each colour class is a perfect
matching. ∎

Therefore the two-permutation format is equivalent to the original saturated seed
problem, not a restricted ansatz.

## 4. Exact finite CSP

Introduce binary variables

```text
x_(i,j,l) in {0,1},
i,j in [n],
l in {0,1},
```

where layer `l` selects cell `(i,j)`.

### Theorem PP3bcj -- PROVED

Prime-minus-one seed feasibility for one prime `p` is equivalent to the following
finite CSP.

1. For every layer and column,

   ```text
   sum_j x_(i,j,l)=1.
   ```

2. For every layer and row,

   ```text
   sum_i x_(i,j,l)=1.
   ```

3. For every cell,

   ```text
   x_(i,j,0)+x_(i,j,1)<=1.
   ```

4. For every Euclidean collinear triple of board cells `a,b,c`,

   ```text
   u_a+u_b+u_c<=2,
   u_(i,j)=x_(i,j,0)+x_(i,j,1).
   ```

A feasible assignment decodes to a saturated seed, and every saturated seed produces a
feasible assignment.

#### Proof

Items 1--3 are exactly the two edge-disjoint permutation conditions of PP3bcg.  Item 4
is PP3bch.  The forward and reverse encodings are immediate. ∎

The triple constraints may be generated exactly by primitive direction vectors or by
enumerating triples and testing the determinant.

## 5. Certificate and verification interface

Use the compact JSON record

```json
{
  "p": 7,
  "sigma": [5,4,2,1,3,6],
  "tau":   [2,5,1,6,4,3]
}
```

with one-based permutation values.

### Proposition PP3bck -- PROVED

The script

```text
scripts/check_prime_minus_one_seed.py
```

verifies:

1. primality of `p`;
2. `n=p-1`;
3. both permutation constraints;
4. pointwise edge-disjointness;
5. saturation of all rows and columns; and
6. every exact integer determinant among the `2n` selected cells.

Acceptance is a complete finite proof of the stated seed instance.

#### Proof

The checker implements PP3bcg and PP3bch directly.  It performs all
`binom(2n,3)` determinant tests without floating-point arithmetic. ∎

## 6. Exact asymptotic seed frontier

### Theorem PP3bcl -- PROVED AS AN EQUIVALENCE

The global seed hypothesis used by PP3awy is equivalent to:

> For every sufficiently large prime `p`, the CSP of PP3bcj with `n=p-1` is feasible.

Equivalently, there exist two edge-disjoint permutations `sigma_p,tau_p` of `[p-1]`
whose union satisfies every determinant inequality of PP3bch.

#### Proof

Apply PP3bcg--PP3bcj for each prime. ∎

This equivalence isolates the remaining global theorem without any patching,
prime-gap, allocation, or host terminology.

### Corollary PP3bcm -- PROVED

The local prime-patching chain does not require a canonical algebraic formula for the
seeds.  Any uniformly proved construction, probabilistic existence theorem, or
machine-checkable certificate family satisfying PP3bcl is sufficient.

Finite certificates alone do not prove PP3bcl, but they can:

1. test proposed constructions;
2. identify recurring permutation or cycle structure;
3. certify the finite initial range below an effective asymptotic threshold; and
4. provide exact counterexamples to overrestrictive seed ansatzes.

The asymptotic prime-minus-one seed theorem and therefore the no-three-in-line
conjecture remain unproved.

## 7. Stored examples

Run

```bash
python scripts/check_prime_minus_one_seed.py \
  experiments/prime-minus-one-seed-examples.json
```

The stored file contains verified seeds for

```text
p=3,5,7,11
```

corresponding to side lengths `2,4,6,10`.  These are finite regression certificates,
not evidence of an asymptotic construction theorem.
