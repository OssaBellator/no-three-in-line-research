# Structural legality for one-row-overlapping swap words

**Branch:** `research/sparse-algebraic-spread`

SAS5hi--SAS5hl close the matching-validity part of disjoint operation squares.
The next structural case is a two-swap word whose transpositions share exactly
one row.  The composition is a directed three-cycle on the three current
images, so host and opposite-layer legality have a complete six-atom test.

Let `pi` be a perfect matching from rows to columns in a host `G`.  Fix three
distinct rows `i,j,k`, and apply first `sigma_ij` and then `sigma_jk`.

## SAS5hm -- exact overlapping composition -- PROVED

The composed state `tau pi = sigma_jk sigma_ij pi` satisfies

\[
\boxed{
(\tau\pi)(i)=\pi(j),\qquad
(\tau\pi)(j)=\pi(k),\qquad
(\tau\pi)(k)=\pi(i).
}
\]

All other rows are unchanged.  Thus `tau` is the three-cycle of the three
current column images, and its inverse is the reverse two-swap word.

### Proof

After the first swap the images at `(i,j,k)` are
`(pi(j),pi(i),pi(k))`.  Swapping the latter two positions gives the displayed
triple.  Reversing the transpositions reverses the cycle. QED.

## SAS5hn -- exact one-layer host criterion -- PROVED

The composed state is a perfect matching of `G` if and only if the three new
host edges

\[
\boxed{
(i,\pi(j)),\qquad(j,\pi(k)),\qquad(k,\pi(i))
}
\]

belong to `G`.

No additional bijectivity check is required.

### Proof

A cyclic permutation of three distinct column images preserves bijectivity.
Only the displayed three edges differ from the original matching. QED.

## SAS5ho -- exact two-layer simple-state criterion -- PROVED

Let `(pi,rho)` be two edge-disjoint perfect matchings of `G`, and switch only
`pi`.  Then `(tau pi,rho)` is a pair of edge-disjoint host matchings if and only
if the three host edges in SAS5hn are present and

\[
\boxed{
\pi(j)\ne\rho(i),\qquad
\pi(k)\ne\rho(j),\qquad
\pi(i)\ne\rho(k).
}
\]

No other duplicate-cell condition can change.

### Proof

Rows outside `{i,j,k}` are unchanged.  At each changed row, collision with the
second layer is exactly the corresponding displayed equality. QED.

## SAS5hp -- six-atom overlapping structural router -- PROVED

A failed one-row-overlapping two-swap word has one of exactly six least
structural witnesses:

1. missing host edge `(i,pi(j))`;
2. missing host edge `(j,pi(k))`;
3. missing host edge `(k,pi(i))`;
4. opposite-layer collision at row `i`;
5. opposite-layer collision at row `j`;
6. opposite-layer collision at row `k`.

Fixing the ordered row triple, its current images and the witness type gives a
complete finite obstruction address.  If all six tests pass, the forward and
reverse three-cycle words are structurally legal; remaining failure fields are
arithmetic-word, collinearity, boundary, owner, payment or context guards.

### Proof

SAS5hn--SAS5ho are necessary and sufficient.  Order their six conditions and
return the first failure.  The reverse word uses the old valid edges when it
returns to the original state, while its intermediate edge legality is already
certified by the two constituent legal swaps. QED.

## Remaining structural frontier

Matching validity is now exact for one swap, two disjoint swaps, and two swaps
sharing exactly one row.  Longer overlapping words reduce to directed cycles on
the affected current images; their structural host test is the list of new
cycle edges, with one opposite-layer collision test per affected row.

The unresolved sparse legality work is therefore arithmetic and geometric, or
concerns longer words whose intermediate states—not merely their final matching—
must satisfy additional payment-sensitive guards.

## Finite check

`scripts/verify_sas_overlapping_swap_structure.py` exhausts small one- and
two-layer matchings, verifies the three-cycle identity, and compares direct
host/layer validity with the six-atom criterion.
