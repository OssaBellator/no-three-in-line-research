# Public quarter-turn certificates close p=41, p=43, and p=53

The finite prime-minus-one certificate suite previously had three gaps below
`p=73`: `p=41,43,53`. The public Flammenkamp archive contains quarter-turn
configuration files for boards `n=40,42,52`. This chapter records the first
standard row-pair code of each file and independently verifies every geometric
and permutation-theoretic obligation.

The complete bulk files are not treated as proofs by authority. The repository
stores their SHA-256 digests and compact first records, then reconstructs the
selected cells, the two permutation layers, the swapped quarter-turn action,
the signed pair cover, and every integer determinant.

## 1. Reproducible archive snapshot

### Proposition PP3biq -- VERIFIED FINITELY

On 2026-07-27 the files

```text
n40_rot4  44,362 bytes   541 records
n42_rot4  64,156 bytes   746 records
n52_rot4 536,572 bytes 5,062 records
```

were retrieved from the public configuration archive. Their SHA-256 digests
are respectively

```text
913347983500d7448b8bcd75b378fd70b4256b448e7f78bb9ba80daf7fde6e30
74915c10720d8e29fc8d9775c2fde8132bc20dd262c267c199d5570e77012a1f
de9812a0977327ce4e9f2418e6cf7d57661a6ad36060e501271ca136133b84ca.
```

The stored standard codes are exactly the first lines of those three files.

#### Verification

The archive-aware diagnostic checks each complete byte stream, digest, line
count, and first record. The permanent repository certificate retains the
hashes and first records; it does not copy the bulk archives. ∎

## 2. Exact row-pair decoding and swapped colouring

### Proposition PP3bir -- PROVED / VERIFIED FINITELY

For an even board size `n`, a standard row-pair code with payload length `2n`
decodes uniquely to two selected columns in each row. For each of the three
stored records, the decoded set has exactly two cells in every row and every
column and is invariant under

```text
R(x,y)=(n-1-y,x).
```

#### Proof

The alphabet maps each payload symbol to one column. Consecutive pairs are the
sorted selected columns of successive rows, so decoding is unique. The
checker directly counts all row and column incidences and compares the selected
set with its rotated image. ∎

### Proposition PP3bis -- VERIFIED FINITELY

Each decoded incidence graph has a deterministic two-colouring in which row
mates, column mates, and quarter-turn images receive opposite colours. The two
colour classes are disjoint permutation graphs `sigma` and `tau`, with

```text
tau = sigma^(-1) o J,
sigma o J = J o sigma,
J(x)=n-1-x.
```

#### Verification

Breadth-first parity propagation checks consistency on every incidence and
rotation edge. Both colour classes are then checked as permutations, and the
displayed identities are evaluated entry by entry. ∎

## 3. Three exact prime-minus-one seeds

### Theorem PP3bit -- VERIFIED FINITELY

The first `n40_rot4` record is a saturated no-three-in-line set of size `80` on
`[40]^2`, hence a valid prime-minus-one seed for `p=41`.

Its signed pair cycles are

```text
lengths  [19,1],
parities [ 1,0],
```

and its relative-cycle partition is `[38,2]`. All

```text
C(80,3)=82,160
```

integer determinants are nonzero. ∎

### Theorem PP3biu -- VERIFIED FINITELY

The first `n42_rot4` record is a saturated no-three-in-line set of size `84` on
`[42]^2`, hence a valid prime-minus-one seed for `p=43`.

Its signed pair cycles have lengths `[17,3,1]`, orientation parities `[1,0,0]`,
and relative-cycle partition `[34,6,2]`. All

```text
C(84,3)=95,284
```

integer determinants are nonzero. ∎

### Theorem PP3biv -- VERIFIED FINITELY

The first `n52_rot4` record is a saturated no-three-in-line set of size `104` on
`[52]^2`, hence a valid prime-minus-one seed for `p=53`.

Its signed pair cycles have lengths `[12,8,5,1]`, orientation parities
`[0,1,1,0]`, and relative-cycle partition

```text
[10,8,8,6,6,6,6,2].
```

All

```text
C(104,3)=182,104
```

integer determinants are nonzero. ∎

For all three seeds, the minimum absolute determinant is one.

## 4. Complete odd-prime finite suite through 73

### Corollary PP3biw -- VERIFIED FINITELY

The canonical exact certificate suite now verifies prime-minus-one seeds for
every odd prime through `73`:

```text
p=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,73.
```

The three formerly missing finite cases are installed in the generic
permutation, relative-cycle, archived-code, quarter-turn, and signed-orbit
regression suites. ∎

### Corollary PP3bix -- PROVED / FINITE FRONTIER CLOSED

There is no remaining finite certificate gap among odd primes `p<=73`.
This does not interpolate to larger primes. The remaining global theorem is
still:

> For every sufficiently large prime `p`, some derangement `pi` and permutation
> `sigma` satisfy the maximal-line system on `[p-1]^2`.

The asymptotic seed theorem and the no-three-in-line conjecture remain open.
