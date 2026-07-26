# Archived seed-code decoding and additional prime certificates

The exact seed CSP accepts any machine-checkable family of two-permutation
certificates.  Public no-three configuration archives use a compact standard
row-pair notation: one leading symmetry symbol followed by two column
symbols for each row.  This chapter gives an independent decoder and exact
verifier for that notation.

Eight archived configurations have been decoded, decomposed into two
permutation layers, and rechecked from scratch by exact integer
determinants.  They add prime-minus-one certificates for

```text
p=17,19,23,29,31,61,67,73.
```

Archive provenance is retained in the input data, but acceptance does not
trust the archive's geometric claims: the local checker independently tests
saturation and every selected triple.

These finite certificates substantially extend the regression range.  They
do not constitute an asymptotic construction theorem.

## 1. Standard row-pair decoding

Use the ordered symbol alphabet

```text
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
#$%&@?!()[]<>{}=*+|-/~^_:;,.
```

with zero-based symbol values.  For a board of side `n`, a standard code has
one leading symmetry tag and then `2n` symbols.  The two symbols in positions
`2r,2r+1` after the tag are the two selected columns in row `r`.

### Proposition PP3bdy -- PROVED

A valid length-`1+2n` code decodes uniquely to a set of `2n` board cells.
It is saturated exactly when every decoded row pair has distinct columns
and every column symbol occurs exactly twice.

#### Proof

The alphabet map fixes every symbol value.  The row positions fix each
point's row, so decoding is unique.  Two symbols per row give row degree
two.  Distinct decoded cells and column multiplicity two give column degree
two, which is exactly saturation. ∎

The leading tag is retained as metadata and is not used to infer
no-three-in-line validity.

## 2. Deterministic two-layer decomposition

Regard every decoded cell `(x,y)` as an edge between column vertex `x` and
row vertex `y`.

### Proposition PP3bdz -- PROVED

Every saturated decoded configuration decomposes into two edge-disjoint
permutation graphs by alternately colouring each component of its
row--column incidence graph.  A deterministic alternating traversal gives a
machine-checkable pair `sigma,tau` whose union is exactly the decoded cell
set.

#### Proof

Every row and column vertex has degree two, so the bipartite incidence graph
is a disjoint union of even cycles.  Alternating two colours around each
cycle gives one edge of each colour at every vertex.  Each colour class is
therefore a perfect matching, hence a permutation graph.  Their disjoint
union is the original edge set. ∎

Different choices of the first colour on separate components may change the
encoded pair of layers without changing the selected configuration.

## 3. Independent exact verification

### Theorem PP3bea -- PROVED

For one archived code, the following finite procedure is a complete proof
of a prime-minus-one seed certificate.

1. Decode the `2n` cells by PP3bdy.
2. Check row and column degree two.
3. Test the exact integer determinant of every unordered selected triple.
4. Decompose the 2-regular incidence graph by PP3bdz.
5. Reconstruct the selected set from the two permutation layers.
6. Compute the relative derangement and its cycle partition.

Acceptance proves saturation and no-three-in-line without relying on
floating-point arithmetic or an archive-supplied layer decomposition.

#### Proof

Steps 1--2 prove saturation.  The determinant vanishes exactly on a
collinear triple, so step 3 proves the no-three property.  Steps 4--5 give
the equivalent two-permutation certificate, and step 6 checks its relative
normal form. ∎

## 4. An exact p=17 seed

The first decoded `n=16` archive code is

```text
oBC36570E0A4D7E9D26182B5F1F8A9C34.
```

One deterministic decomposition returned by the checker is

```text
sigma =
[4,10,9,16,6,12,2,3,14,15,5,11,1,8,7,13],

tau =
[5,13,11,2,16,3,9,7,10,8,14,1,15,6,4,12].
```

### Theorem PP3beb -- VERIFIED FINITELY

The union of these two permutation graphs is a saturated no-three set of
size `32` on `[16]^2`, hence a prime-minus-one seed for `p=17`.

Its relative cycle partition is

```text
[8,8],
```

and the incidence graph has two alternating components of length sixteen.

#### Verification

The code decoder finds two cells in every row and column.  The exact checker
tests all

```text
binom(32,3)=4960
```

selected triples and finds no zero determinant.  The alternating cycle
decomposition reconstructs the decoded cell set exactly. ∎

This resolves the finite `p=17` certificate target that the local
near-state search did not reach.

## 5. Eight additional archived prime certificates

### Proposition PP3bec -- VERIFIED FINITELY

The provenance-preserving archive-code checker independently verifies:

| `p` | `n=p-1` | points | determinant checks | relative cycle partition |
|---:|---:|---:|---:|---|
| 17 | 16 | 32 | 4,960 | `[8,8]` |
| 19 | 18 | 36 | 7,140 | `[10,2,2,2,2]` |
| 23 | 22 | 44 | 13,244 | `[5,5,5,5,2]` |
| 29 | 28 | 56 | 27,720 | `[26,2]` |
| 31 | 30 | 60 | 34,220 | `[5,5,5,5,2,2,2,2,2]` |
| 61 | 60 | 120 | 280,840 | `[58,2]` |
| 67 | 66 | 132 | 374,660 | `[16,16,16,16,2]` |
| 73 | 72 | 144 | 487,344 | `[36,36]` |

Across these cases the checker performs `1,230,128` exact determinant tests.
Every minimum nonzero absolute determinant is one.

#### Verification

Run

```bash
python scripts/check_archived_prime_seed_codes.py \
  experiments/archived-prime-seed-codes.json
```

The JSON records the source archive path and exact standard code for each
case.  The checker decodes and proves each certificate independently by
PP3bea. ∎

## 6. Relative-cycle diversity

### Corollary PP3bed -- VERIFIED FINITELY

The certified configurations exhibit all of the following relative
structures:

```text
two equal large cycles;
one large cycle plus one transposition;
four or five equal medium cycles plus one transposition;
one ten-cycle plus four transpositions;
four five-cycles plus five transpositions.
```

Thus neither connected incidence graphs nor one fixed relative cycle type
can be imposed as a universal finite-search ansatz.

#### Proof

Read the exact partitions in PP3bec and use PP3bcw to translate relative
cycles into alternating incidence components. ∎

The prevalence of one or several large cycles may still be useful as a
search heuristic, but it is not an equivalence reduction.

## 7. Revised finite seed frontier

### Corollary PP3bee -- PROVED / VERIFIED FINITELY

Combining the internally generated certificates with PP3bec, the repository
now stores exact prime-minus-one seeds for

```text
p=3,5,7,11,13,17,19,23,29,31,61,67,73.
```

For each listed prime, the local exact-width patch theorem may take the
verified seed as its finite initial input.  No interpolation between these
isolated certificates is implied.

The remaining global statement is still:

> for every sufficiently large prime `p`, a prime-minus-one seed exists.

Public finite archives can enlarge the checked range and reveal structure,
but they do not replace a uniform construction, probabilistic existence
proof, or effective certificate family covering all sufficiently large
primes.  The no-three-in-line conjecture remains unproved.

## 8. Diagnostics

Run

```bash
python scripts/check_archived_prime_seed_codes.py \
  experiments/archived-prime-seed-codes.json
python scripts/check_prime_minus_one_seed.py \
  experiments/prime-minus-one-seed-examples.json
```

The first command verifies the compact archive provenance records and
derives permutation layers.  The second verifies the expanded canonical
two-permutation certificate suite.
