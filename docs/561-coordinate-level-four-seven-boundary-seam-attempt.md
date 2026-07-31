# Coordinate-level four/seven boundary seam attempt

`docs/555` showed that the four/seven marker catalogue had no coordinate-level
source.  This chapter supplies an independent finite attempt.  It does not
identify the blocks with the prime-patching boundary controller.  Instead it
constructs two saturated no-three-in-line blocks, labels their boundary ports,
and exhausts the most direct diagonal seam model.

For permutations `p,q` of `{0,...,n-1}`, write

```text
X(p,q)={(i,p(i)),(i,q(i)):0<=i<n}.
```

The stored blocks are

```text
P: n=4,
p=(0,1,3,2), q=(2,3,1,0),

Q: n=7,
p=(5,6,2,1,4,0,3), q=(3,0,4,5,2,6,1).
```

## 1. Independent saturated block census

### Theorem PP3cpf -- PROVED / COORDINATE-LEVEL BLOCK CERTIFICATE

Each of `P` and `Q` has exactly two points in every row and every column, has
respectively `8` and `14` points, and contains no collinear triple.

#### Proof

The two displayed maps are permutations and disagree at every row, giving two
points per row and column.  The determinant test

```text
(x_2-x_1)(y_3-y_1)-(y_2-y_1)(x_3-x_1) != 0
```

is checked for every triple.  This is a finite exact integer certificate. ∎

## 2. Ports and finite seam oracle

### Theorem PP3cpg -- PROVED / DIHEDRAL PORT-AND-SEAM CENSUS

Apply every symmetry of the square to each block and quotient duplicate point
sets.  Both blocks have four distinct dihedral variants.  For each variant, its
left and right controller ports are the two ordinates in the first and last
columns.  For every ordered pair of block types and every ordered pair of
variants, diagonal concatenation is decided by one finite collinearity test.

#### Proof

Square symmetries preserve row and column degrees and collinearity.  Duplicate
symmetries are removed by equality of finite point sets.  After translating the
second block by `(n,n)`, where `n` is the first block size, the union is finite;
triple determinants decide the seam exactly. ∎

## 3. Naive diagonal concatenation fails

### Theorem PP3cph -- PROVED / FOUR-SEVEN DIAGONAL-SEAM OBSTRUCTION

None of the `64` ordered dihedral seams

```text
P->P, P->Q, Q->P, Q->Q
```

is legal.  First witnesses for the identity variants are

| seam | collinear triple |
|---|---|
| `P->P` | `(0,0),(1,1),(4,4)` |
| `P->Q` | `(0,0),(1,1),(6,6)` |
| `Q->P` | `(0,3),(5,6),(10,9)` |
| `Q->Q` | `(0,3),(2,4),(8,7)` |

Twenty-nine of the sixty-four first witnesses have slope one.

#### Proof

There are four variants of each block, hence sixteen tests for each ordered
block-type pair.  Exact enumeration finds a collinear witness in every union.
The listed triples are the lexicographically first witnesses for the identity
variants. ∎

## 4. Stored exact audit

Run

```bash
python scripts/check_boundary_coordinate_seam_attempt.py
```

The checker verifies both local blocks, all port labels, all sixty-four seam
attempts, and a failure witness for every attempted seam.

## 5. Prime-patching consequence

This is genuine coordinate-level progress but a negative realization result.
The simplest diagonal four/seven concatenation cannot underlie the marker
semigroup of `docs/544`.  A successful boundary adapter must use additional
seam correctors, a nontrivial permutation of row and column bands, or different
local blocks.  The boundary loss row `7/120` is therefore not promoted.
