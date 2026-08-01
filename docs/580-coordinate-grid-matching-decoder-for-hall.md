# Coordinate-grid matching decoder for Hall choices

`docs/574` decoded the cylinder quotient choices into compatible pairs of a
complete four-by-four endpoint grid and proved abstract matching extension.  This
chapter realizes the same grid as actual board cells and imposes the
no-three-in-line condition on the completed permutation.

Use rows `0,1,2,3` and columns `0,1,2,3`.  For syndrome `s in Z/3Z` and choice
`c in Z/4Z`, decode

```text
(s,c) -> ((0,c),(1,c+s+1 mod 4)).
```

## 1. Coordinate complete-grid decoder

### Theorem PP3crk -- PROVED / TWELVE COORDINATE PAIRS

The displayed map is a bijection from the twelve quotient-choice pairs onto all
ordered pairs of cells in rows zero and one that occupy distinct columns.

#### Proof

For fixed `c`, the three syndromes produce the three columns different from
`c`.  Conversely, for every ordered distinct column pair `(a,b)`, the nonzero
difference `b-a mod 4` is uniquely one of `1,2,3`, hence determines `s`. ∎

## 2. No-three-in-line matching extension

### Theorem PP3crl -- PROVED / GEOMETRIC RESIDUAL MATCHING

Every decoded pair extends to a four-cell permutation using every row and column
exactly once and containing no collinear triple.  Across the twelve pairs there
are exactly eighteen such extensions: six pairs have one extension and six have
two.

#### Proof

After fixing the first two cells, the two unused rows and columns form `K_2,2`,
so there are two candidate completions.  The checker tests every resulting
four-cell permutation against all four triples.  At least one completion is legal
for every decoded pair, and the exact total is eighteen. ∎

## 3. Microscopic witness lift

### Theorem PP3crm -- PROVED / ORIENTATION-DOUBLED CELL WITNESSES

Each decoded coordinate pair has exactly two cylinder microstate witnesses, one
for each orientation bit.  Hence the twenty-four microscopic witnesses project
to the twelve coordinate pairs and every pair has a geometric matching extension.

#### Proof

The decoder depends only on syndrome and choice, not orientation.  The two
orientation values are distinct microstates with the same decoded cells.
`PP3crl` supplies the extension. ∎

## 4. Exact audit and remaining gap

Run

```bash
python scripts/check_hall_coordinate_grid_extensions.py
```

This closes a coordinate-level complete-grid candidate.  It still does not
identify the four columns with endpoint cells of an actual prime-patching host,
nor does it audit additional exclusions imposed by such a host.
