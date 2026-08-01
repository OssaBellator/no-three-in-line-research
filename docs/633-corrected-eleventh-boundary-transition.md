# Corrected eleventh boundary transition

`docs/627` extends the canonical corrected boundary path to ten blocks by widening
the offset radius to `64`.  This chapter audits every typed eleventh attempt from
that exact eighty-point state and searches degree-preserving corrections.

## 1. Complete eleventh transversal spectrum

### Theorem PP3cxn -- PROVED / RADIUS-64 ELEVENTH CENSUS

Across the `8*129=1032` typed eleventh-block attempts, the exact minimum
cross-line-transversal histogram is

```text
4:12, 5:35, 6:76, 7:135, 8:261,
9:21, 10:41, 11:79, 12:99, 13:170, 14:103.
```

The twelve minimum-four attempts have ninety-four minimum transversals in total.

#### Proof

The compiled checker forms every old-old-new and old-new-new collinear triple.
An exact branch-and-bound hitting-set solver computes the minimum for each typed
offset and enumerates all minimum sets for the twelve minimum-four attempts.  The
histogram sums to `1032`.  ∎

## 2. Corrected eleventh transitions

### Theorem PP3cxo -- PROVED / ALL MINIMUM-FOUR ATTEMPTS CORRECTABLE

Every one of the twelve minimum-four attempts has a row-and-column-preserving
legal correction of total deletion size at most seven.

The lexicographically first correction of minimum displayed size uses `P1` at
offset `31` and deletes

```text
(0,79), (6,34), (23,2), (40,196), (43,195),
```

then adds

```text
(0,196), (6,2), (23,195), (40,34), (43,79).
```

This five-point correction produces a legal eighty-eight-point eleven-block
state.

#### Proof

For each of the ninety-four minimum cores, the checker enlarges the deletion set
to total size at most seven and searches every row-column-multiset-preserving
refill with inherited-line pruning.  At least one correction is found for each of
the twelve typed attempts.  Direct multiplicity comparison and exact determinant
tests verify the displayed correction.  ∎

## 3. Raw twelfth obstruction

### Theorem PP3cxp -- PROVED / NO RAW RADIUS-64 TWELFTH STEP

From the displayed corrected eleventh state, none of the `1032` typed twelfth
attempts in offset radius `64` is immediately no-three-in-line.

#### Proof

Place every block type at the next horizontal origin and every offset in
`[-64,64]`; exact determinant testing finds a collinear triple in every union. ∎

The corrected path now reaches eleven blocks, but no corrected twelfth transition,
periodic component, or bounded-drift recurrence is known.
