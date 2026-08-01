# Sharp six-point boundary seam corrector

`docs/603` proves that every exact degree-preserving refill using at most five
deleted points fails for the four sharp radius-32 sixth-block seam repairs.  The
next finite class is therefore a six-point swap: delete three further points,
then refill the resulting six row and six column incidences exactly.

## 1. Sharp correction size

### Theorem PP3cut -- PROVED / SIX-POINT DEGREE-PRESERVING CORRECTION

Each of the four sharp three-deletion sixth-block repairs from `docs/585` admits
an exact six-point delete-and-refill correction that

- preserves the complete row-degree multiset;
- preserves the complete column-degree multiset;
- restores the original point count; and
- leaves no collinear triple.

Together with the exhaustive four- and five-point obstructions in `docs/597` and
`docs/603`, the minimum correction size in this degree-support swap class is
exactly six.

#### Proof

The checker reconstructs the four sharp repairs and searches triples of further
deletions in lexicographic order.  For each six-point deleted set, a pruned
bipartite matching search pairs the deleted column multiset with the deleted row
multiset.  Pairings are rejected immediately when they create a triple with two
old points, one old and one already selected refill point, or three refill
points.  One valid pairing is found for every sharp repair.  Exact row and column
counters, point count, and a complete triple audit certify each result.

No correction with at most five points exists by the complete enumerations in
`PP3ctl` and `PP3cud`.  Hence six is sharp. ∎

## 2. Explicit symmetric certificates

### Theorem PP3cuu -- PROVED / FOUR CANONICAL SEAM CORRECTORS

For the first negative-offset repair, one certificate deletes

```text
(1,1), (1,2), (5,-31), (9,-58), (16,-74), (18,-74)
```

and inserts

```text
(1,-74), (1,-58), (5,-74), (9,-31), (16,1), (18,2).
```

The other three repairs have the reflected certificates stored by
`scripts/check_boundary_six_point_corrector.py`.  The lexicographic searches find
their first witnesses after `1863,1864,57,56` extra-deletion cases respectively.

#### Proof

For every listed pair of deleted and inserted sets, the column multiplicities and
row multiplicities agree exactly.  The checker then audits all triples of the
corrected forty-eight-point six-block configuration.  All four certificates pass.
The remaining three are obtained by the two geometric symmetries already pairing
the sharp radius-32 repairs. ∎

## 3. Immediate non-composition

### Theorem PP3cuv -- PROVED / NO RAW SEVENTH BLOCK IN THE AUDITED RADIUS

None of the four corrected six-block configurations accepts an unmodified `P` or
`Q` seventh block in any of the eight typed variants and any vertical offset in
`[-32,32]`.

#### Proof

There are

```text
4 * 8 * 65 = 2080
```

candidate seventh blocks.  The checker forms the full corrected point set for
each candidate and performs a complete collinearity audit.  Every candidate
fails. ∎

## 4. Prime-patching consequence

The stored boundary fixture now has a sharp degree-preserving seam corrector, so
the previous saturation defect is removed at six blocks.  This is still not a
repeatable boundary controller: the corrected state has no raw seventh-block
extension in the audited offset radius.  A composable construction needs a
corrector-aware state transition, a larger offset theorem, or a new block
catalogue.
