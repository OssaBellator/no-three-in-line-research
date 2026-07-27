# An exact support-thirteen repair and prime-thirty-seven seed

The Hall-propagated branch-and-bound of PP3bfx proves that the audited
quarter-turn near-state on `[36]^2` has no canonical signed-orbit repair of
support at most twelve.  Continuing the same exact residual cycle-cover search
at support thirteen produces a complete feasible leaf.

The resulting selected set is a saturated no-three configuration of size
seventy-two.  Thus the first missing finite prime after `p=31` in the canonical
repository suite is now certified, and the local repair radius of the audited
near-state is determined exactly.

This is a finite result.  It does not interpolate to later primes and does not
prove the asymptotic prime-minus-one seed theorem.

## 1. The support-thirteen signed repair

Use one-based pair indices.  The changed source pairs are

```text
A={1,2,3,4,6,7,10,12,13,15,16,17,18}.
```

Their new `(target,orientation)` assignments are

```text
1 ->(14,0),   2 ->(15,1),   3 ->(9,0),
4 ->(7,1),    6 ->(3,1),    7 ->(13,1),
10->(17,1),   12->(16,0),   13->(8,1),
15->(1,0),    16->(2,0),    17->(18,0),
18->(10,0).
```

The unchanged source pairs retain the assignments of the near-state.

### Proposition PP3bga -- VERIFIED FINITELY

The complete signed pair cover after this replacement is

```text
rho=
[14,15,9,7,12,3,13,6,5,17,11,16,8,4,1,2,18,10],

e=
[0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,0,0].
```

It is a canonical edge-disjoint signed directed cycle cover and differs from
the audited near-state on exactly the thirteen source pairs in `A`.

#### Verification

The target list is a permutation of `[18]`.  Canonical self-loop orientation
is zero, no changed source retains its old canonical assignment, and no
oppositely oriented reverse two-cycle is present.  Direct comparison with the
near-state gives the displayed support and no other changed source. ∎

## 2. Two permutation layers

The signed cover decodes through PP3bev and the forced swapped-action formula
to

```text
sigma=
[14,22,9,30,25,34,24,6,32,20,26,16,29,33,1,2,18,10,
 27,19,35,36,4,8,21,11,17,5,31,13,3,12,7,28,15,23],

tau=
[22,21,6,14,9,29,4,13,34,19,11,5,7,36,2,25,10,20,
 17,27,12,35,1,30,32,26,18,3,24,33,8,28,23,31,16,15].
```

### Theorem PP3bgb -- VERIFIED FINITELY

The union of these two permutation graphs is a saturated no-three-in-line set
of size `72` on `[36]^2`.  It is therefore a valid prime-minus-one seed for

```text
p=37.
```

#### Verification

Both arrays are permutations of `[36]` and differ in every column.  Hence their
union has exactly two distinct points in every row and column.  The exact
checker tests all

```text
binom(72,3)=59640
```

integer determinants and finds none equal to zero.  The minimum nonzero
absolute determinant is one. ∎

The first layer commutes with coordinate reversal and the second layer equals

```text
tau=sigma^(-1) o J,
```

so the certificate remains inside the swapped quarter-turn orbit class.

## 3. Exact repair radius

### Theorem PP3bgc -- PROVED / VERIFIED FINITELY

The canonical signed-orbit repair radius of the audited four-line `p=37`
near-state is exactly

```text
h_orbit=13.
```

#### Proof

PP3bfh excludes every support from one through six.  PP3bfx excludes every
support from seven through twelve by exact Hall-propagated branch-and-bound.
PP3bga--PP3bgb give a valid repair of support thirteen. ∎

Thus the previously observed near-state is neither locally repairable by a
small switch nor trapped globally: its first feasible signed-orbit move changes
thirteen of eighteen pair assignments.

## 4. Pair cycles and full relative cycles

### Proposition PP3bgd -- VERIFIED FINITELY

The repaired signed pair permutation has cycle partition

```text
[14,3,1]
```

with corresponding orientation xor parities

```text
[0,1,1].
```

The exact lift theorem PP3bfm therefore predicts the full relative-cycle
partition

```text
[14,14,6,2],
```

which agrees with the direct cycle decomposition of

```text
pi=sigma^(-1) o tau.
```

#### Verification

The even fourteen-cycle has `delta=1`, so it contributes two fourteen-cycles.
The odd three-cycle contributes one six-cycle, and the fixed pair contributes
one relative transposition.  Direct traversal of `pi` gives the same multiset.
∎

The incidence graph consequently has alternating component lengths

```text
[28,28,12,4].
```

## 5. Compact row-pair certificate

### Proposition PP3bge -- VERIFIED FINITELY

The same selected cell set is encoded by the standard row-pair code

```text
oEMEFRU6MBR27CWNU24GHAPKV7T03YZBYIQGQ9J9H1O01WZ6S4FAPIJVX5C3NSX8ODT58KLDL
```

using the alphabet of PP3bdy.

#### Verification

Decoding the two column symbols in every row produces exactly the union of the
displayed `sigma` and `tau` graphs.  The code has length

```text
1+2*36=73.
```

No geometric assertion is inferred from the leading tag; the determinant
checker independently verifies the decoded set. ∎

This compact form gives a provenance-independent regression record generated
inside the research branch.

## 6. Expanded canonical finite suite

### Corollary PP3bgf -- VERIFIED FINITELY

The canonical exact two-permutation certificate suite now verifies
prime-minus-one seeds for

```text
p=3,5,7,11,13,17,19,23,29,31,37,61,67,73.
```

The `p=37` case is generated by the exact support-thirteen repair above rather
than imported from the public archive.  The finite list still has gaps and does
not imply a construction for all primes.

## 7. Revised frontier

### Corollary PP3bgg -- PROVED / FINITE CERTIFICATE RECORDED

The first finite target after `p=31` is closed.  The exact signed-orbit search
pipeline now demonstrates a complete progression:

```text
four-line near-state,
raw support census through six,
Hall-propagated exclusion through twelve,
and a verified support-thirteen seed.
```

The next finite certificate gaps in increasing prime order are

```text
p=41,43,47,53,59,
```

before the stored `p=61` certificate.  Productive computational directions
include applying the signed orbit CSP at those sizes, searching multiple
near-state basins, and using pair-cycle parity and Hall propagation earlier in
the search.

The remaining global theorem is unchanged:

> for every sufficiently large prime `p`, a prime-minus-one seed exists.

One additional finite certificate does not prove that theorem.  The
prime-minus-one seed theorem and the no-three-in-line conjecture remain open.

## 8. Diagnostic

Run

```bash
python scripts/check_p37_swapped_orbit_support13_certificate.py \
  experiments/p37-swapped-orbit-support13-certificate.json \
  experiments/p37-swapped-quarter-turn-near-example.json
```

The checker reconstructs all three certificate representations, verifies exact
repair support, swapped quarter-turn identities, pair and relative cycles,
saturation, the compact code, and every integer determinant.