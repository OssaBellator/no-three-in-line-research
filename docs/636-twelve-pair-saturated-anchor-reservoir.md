# Twelve-pair saturated anchor reservoir

`docs/630` gives an eleven-pair saturated source for the size-thirty prefix
profile.  This chapter extends the finite reservoir by one complete row, column,
and anchor pair.

## 1. Explicit saturated source

### Theorem PP3cxw -- PROVED / TWELVE-BY-TWELVE SOURCE

Let

```text
P=(6,7,0,4,9,2,11,10,1,5,8,3),
Q=(2,9,11,7,0,4,10,8,3,6,1,5).
```

The twenty-four cells `(r,P[r])` and `(r,Q[r])` form a no-three-in-line subset of
the `12 x 12` grid.  Every row and every column has degree exactly two.

#### Proof

Both tuples are permutations, they disagree in every row, and exact determinant
testing rejects every triple among the twenty-four cells.  ∎

## 2. Anchor pairing and complete composition audit

### Theorem PP3cxx -- PROVED / TWELVE DISJOINT SOURCE PAIRS

Pair the `P`-cell in row `r` with the `Q`-cell in row

```text
(11,9,10,8,5,6,7,4,3,2,1,0)[r].
```

These are twelve disjoint pairs with distinct endpoint rows and columns.  Using
the pair secants as unary-run support lines, all `2^11=2048` ordered compositions
of twelve unary nodes admit integer embeddings with globally distinct insertion
rows and columns and zero mixed-run collinear triples.  The canonical greedy
audit has maximum coordinate magnitude `187`.

#### Proof

The pairing is a perfect matching of the twenty-four source cells and avoids
shared endpoint resources.  The insertion checker chooses primitive secant-line
points while excluding used resources and every mixed line through two existing
points.  Exact determinant checking verifies all compositions.  ∎

## 3. Finite scalability statement

### Theorem PP3cxy -- PROVED / CONSECUTIVE SATURATED SCALES

The repository now contains complete saturated anchor reservoirs for eleven and
twelve pairs, supporting all run compositions at their respective sizes.

This proves a genuine one-step scale extension, but not a nested construction or
an infinite family.  The next prefix obligation is a uniform extension rule from
`m` pairs to `m+1`, or an explicit unbounded family of two-per-row/two-per-column
no-three sources with compatible anchor pairings.
