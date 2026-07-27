# An independently verified Wikimedia coordinate certificate for p=59

The remaining finite gap `p=59` has a public machine-readable representative.
The Wikimedia Commons description of `No-Three-In-Line for N=58.png` gives all
116 grid coordinates, attributed to Prellberg and licensed CC BY-SA 4.0.  This
chapter preserves that attribution and independently verifies every geometric
and permutation claim.

No validity assertion is imported from the image or its caption.  The stored
coordinates are checked for saturation, quarter-turn structure, exact signed
cycle data, and every integer determinant.

This is a finite certificate.  It does not interpolate to other primes and
does not prove the asymptotic prime-minus-one seed theorem.

## 1. Coordinate record and attribution

The source metadata retained in
`experiments/p59-wikimedia-coordinate-certificate.json` is

```text
page:    https://commons.wikimedia.org/wiki/File:No-Three-In-Line_for_N=58.png
author:  Prellberg
date:    2025-10-29
licence: CC BY-SA 4.0
```

### Proposition PP3bhc -- VERIFIED FINITELY

The coordinate record contains exactly `116` distinct cells of `[58]^2`, with
exactly two selected cells in every row and every column.

#### Verification

The checker rejects noninteger coordinate pairs, duplicates, cells outside
`0,...,57`, and every row or column multiplicity other than two.  The retained
list has cardinality `2*58=116` and uses every row and column exactly twice. ∎

## 2. Quarter-turn decomposition

Let

```text
R(x,y)=(57-y,x),
J(x)=57-x.
```

### Proposition PP3bhd -- VERIFIED FINITELY

The selected set is invariant under `R`.  Its incidence graph admits swapped,
but not fixed, quarter-turn colouring into two permutation layers.

The swapped colouring gives the one-based permutations

```text
sigma =
[31,15,20,27,50,16,6,19,41,33,8,5,30,12,23,46,22,3,45,57,7,1,17,24,
 38,11,25,55,10,49,4,34,48,21,35,42,58,52,2,14,56,37,13,36,47,29,54,
 51,26,18,40,53,43,9,32,39,44,28],

tau =
[37,20,41,28,47,52,38,48,5,30,33,45,16,19,57,53,36,9,51,56,25,42,
 44,35,32,10,55,1,13,46,58,4,49,27,24,15,17,34,3,8,50,23,6,2,40,43,
 14,26,29,54,11,21,7,12,31,18,39,22].
```

They satisfy

```text
sigma J = J sigma,
tau = sigma^(-1) o J,
and sigma(x) != tau(x) for every x.
```

#### Verification

The exact parity-colouring algorithm imposes opposite colours on the two
selected cells in each row and column and parity one under quarter-turn.  Both
colour classes are permutation graphs.  The parity-zero system is inconsistent,
while direct inversion verifies the displayed swapped identities. ∎

## 3. Signed pair cover and relative lift

Writing `58=2*29`, the first layer has signed pair data

```text
rho =
[28,15,20,27,9,16,6,19,18,26,8,5,29,12,23,13,22,3,14,2,7,1,17,24,
 21,11,25,4,10],

e =
[1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0].
```

### Proposition PP3bhe -- VERIFIED FINITELY

The pair-cycle lengths and orientation xor parities are

```text
lengths  [28,1],
parities [ 0,0].
```

The lift theorem PP3bfm therefore gives relative-cycle partition

```text
[14,14,14,14,2].
```

Direct traversal of `pi=sigma^(-1) o tau` gives the same partition.

#### Verification

The checker derives `rho` and `e` from the reconstructed first layer.  The even
28-cycle has

```text
delta=(28/2 mod 2) xor 0 = 0,
```

so it produces four 14-cycles.  The fixed pair contributes one relative
transposition. ∎

## 4. Exact no-three certificate

### Theorem PP3bhf -- VERIFIED FINITELY

The union of the two displayed permutation graphs is a saturated
no-three-in-line configuration of size `116` on `[58]^2`.  It is therefore a
valid prime-minus-one seed for

```text
p=59.
```

#### Verification

The checker evaluates the exact integer determinant of every unordered triple
of selected cells.  It performs all

```text
C(116,3)=253460
```

checks and finds no zero.  The minimum nonzero absolute determinant is one. ∎

Equivalently, all `476358` maximal grid lines containing at least three board
cells have selected occupancy at most two.

## 5. Compact row-pair representation

### Proposition PP3bhg -- VERIFIED FINITELY

The same selected set has standard row-pair code

```text
oLRchHcUV8B6gKqAdHrPSPoDrSgdk1Z5CMant7D12XpGvEfNYKQlm3X3vjm9C0sOs9AVbNYGh0f6Otuio28LZjqMuBIFT4i7WTW4eIl5bFpknQRJeEJUa
```

using the alphabet of PP3bdy.

#### Verification

The checker sorts the two selected columns in every row, maps them through the
standard alphabet, and prepends the nonassertive tag `o`.  The resulting code
has length `1+2*58=117` and decodes back to exactly the stored coordinate set. ∎

## 6. Expanded canonical suite

### Corollary PP3bhh -- VERIFIED FINITELY

The canonical exact certificate suite now verifies prime-minus-one seeds for

```text
p=3,5,7,11,13,17,19,23,29,31,37,47,59,61,67,73.
```

The `p=59` case is independently derived from the attributed Wikimedia
coordinate record and is installed in the generic two-permutation,
relative-cycle, quarter-turn-normal-form, and signed-orbit regression suites.

## 7. Revised finite frontier

### Corollary PP3bhi -- PROVED / FINITE CERTIFICATE RECORDED

The remaining missing prime certificates below the stored `p=61` case are now

```text
p=41,43,53.
```

The local `p=41` support-thirteen problem remains unresolved.  No usable
`p=53` record was obtained from the empty historical `c4-52.out` repository
blob.  These finite gaps are separate from the remaining asymptotic theorem:

> for every sufficiently large prime `p`, a prime-minus-one seed exists.

That theorem and the no-three-in-line conjecture remain open.

## 8. Diagnostic

Run

```bash
python scripts/check_p59_wikimedia_coordinate_certificate.py \
  experiments/p59-wikimedia-coordinate-certificate.json
```

The diagnostic begins from the attributed coordinate list and independently
checks every derived representation and every determinant.
