# An independently verified public RLE certificate for p=47

The next finite certificate gap after `p=43` can be closed without relying on
the inaccessible Flammenkamp bulk-download endpoint.  The public
`mvr/no-three-in-line` repository stores fourfold-rotational configurations in
RLE form.  Its first `results/c4-46.out` record decodes to a saturated
no-three-in-line set on `[46]^2`.

This chapter records the source blob and then independently reconstructs the
configuration in every representation used by the prime-minus-one seed
programme.  The external search code is not trusted: the proof obligation is
discharged by exact decoding, permutation checks, symmetry reconstruction, and
all integer determinants.

This is a finite certificate for `p=47`.  It neither supplies a uniform
construction nor proves the asymptotic prime-minus-one seed theorem.

## 1. Public RLE record

The source record is the first line of

```text
repository: mvr/no-three-in-line
path:       results/c4-46.out
blob:       2b978710f7c315ad49020f449e81842e1c88fd06
```

and is stored verbatim in
`experiments/p47-public-rle-certificate.json`.

### Proposition PP3bgv -- VERIFIED FINITELY

The RLE record decodes to exactly `92` distinct cells of `[46]^2`, with exactly
two selected cells in every row and every column.

#### Verification

The independent parser expands decimal run lengths, blank runs, occupied runs,
row advances, and the terminal marker.  It rejects coordinates outside
`0,...,45`, duplicate cells, and every row or column multiplicity other than
two.  The decoded set has maximum coordinates `(45,45)` and cardinality
`2*46=92`. ∎

## 2. Quarter-turn decomposition

Let

```text
R(x,y)=(45-y,x),
J(x)=45-x.
```

### Proposition PP3bgw -- VERIFIED FINITELY

The decoded set is invariant under `R` and admits swapped, but not fixed,
quarter-turn action on its two permutation layers.

The swapped colouring gives the one-based permutations

```text
sigma =
[13,43,29,12,32,24,20,33,41,19,9,40,22,30,11,45,10,8,42,46,21,3,16,
 31,44,26,1,5,39,37,2,36,17,25,7,38,28,6,14,27,23,15,35,18,4,34],

tau =
[20,16,25,2,19,9,12,29,36,30,32,43,46,8,5,24,14,3,37,40,26,34,6,
 41,13,21,7,10,44,33,23,42,39,1,4,15,17,11,18,35,38,28,45,22,31,27].
```

They satisfy

```text
sigma J = J sigma,
tau = sigma^(-1) o J,
and sigma(x) != tau(x) for every x.
```

#### Verification

The checker constructs the row/column incidence graph of the decoded cells and
solves its exact parity-colouring constraints with quarter-turn parity one.
Each colour class is a permutation graph.  Direct inversion and composition
then verify the displayed identities and edge-disjointness. ∎

## 3. Signed pair cover and relative lift

Writing `46=2*23`, the first layer has signed pair data

```text
rho =
[13,4,18,12,15,23,20,14,6,19,9,7,22,17,11,2,10,8,5,1,21,3,16],

e =
[0,1,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0].
```

### Proposition PP3bgx -- VERIFIED FINITELY

The pair-cycle lengths and orientation xor parities are

```text
lengths  [22,1],
parities [ 1,0].
```

The exact lift theorem PP3bfm therefore gives relative-cycle partition

```text
[11,11,11,11,2].
```

Direct traversal of `pi=sigma^(-1) o tau` gives the same partition.

#### Verification

The checker derives `rho` and `e` from `sigma`, rather than trusting the stored
arrays, traverses every pair cycle, and evaluates its xor parity.  The even
22-cycle has

```text
delta=(22/2 mod 2) xor 1 = 0,
```

so it produces four 11-cycles; the fixed pair produces one relative
transposition. ∎

## 4. Exact no-three certificate

### Theorem PP3bgy -- VERIFIED FINITELY

The union of the two displayed permutation graphs is a saturated
no-three-in-line configuration of size `92` on `[46]^2`.  It is therefore a
valid prime-minus-one seed for

```text
p=47.
```

#### Verification

For every unordered triple of selected cells the checker evaluates the exact
integer determinant

```text
(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x).
```

It performs all

```text
C(92,3)=125580
```

checks and finds no zero.  The minimum nonzero absolute determinant is one. ∎

No floating-point geometric predicate is used.

## 5. Compact row-pair representation

### Proposition PP3bgz -- VERIFIED FINITELY

The same selected set has standard row-pair code

```text
oQX3UHLYiERMbQYDH5AGREb360OGcZf1MWach4906KPChUe5F2XKPdjaf279DNi4A7TLjdg8VITZeSWBJ8NIV1BOSFgCJ
```

using the alphabet of PP3bdy.

#### Verification

For each row the checker sorts its two decoded columns, maps them through the
standard alphabet, prepends the nonassertive tag `o`, and compares the result
with the stored code.  Decoding that code recovers the same 92 cells. ∎

## 6. Expanded finite suite

### Corollary PP3bha -- VERIFIED FINITELY

The canonical exact certificate suite now verifies prime-minus-one seeds for

```text
p=3,5,7,11,13,17,19,23,29,31,37,47,61,67,73.
```

The `p=47` case is independently decoded from the public RLE record above.  It
is also installed in the generic two-permutation, relative-cycle,
quarter-turn-normal-form, and signed-orbit regression suites.

## 7. Revised finite frontier

### Corollary PP3bhb -- PROVED / FINITE CERTIFICATE RECORDED

The missing prime certificates below the stored `p=61` case are now

```text
p=41,43,53,59.
```

The `p=41` four-line near-state and radius lower bound from PP3bgn--PP3bgu
remain unchanged.  The nominal `c4-52.out` path in the same external result
tree is currently an empty repository blob and is not evidence for `p=53`;
that case still requires an independently materialised configuration or a new
search.

The asymptotic seed theorem and the no-three-in-line conjecture remain open.

## 8. Diagnostic

Run

```bash
python scripts/check_p47_public_rle_certificate.py \
  experiments/p47-public-rle-certificate.json
```

The diagnostic begins from the external RLE representation and independently
checks every subsequent representation and every determinant.
