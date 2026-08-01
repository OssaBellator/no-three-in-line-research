# Repeated corrected boundary transition

`docs/609` constructs sharp six-point seam correctors, and `docs/615` finds one
corrected seventh-block transition.  This chapter combines the complete eighth-
step spectrum with explicit corrected eighth and ninth transitions, retaining
the full inherited-line state and offset radius `32` throughout.

## 1. Complete eighth-step spectrum

### Theorem PP3cwd -- PROVED / COMPLETE RADIUS-32 TRANSVERSAL CENSUS

For the canonical corrected seventh state, the 520 typed eighth-block attempts
have exact minimum line-conflict transversal histogram

```text
4:1, 5:6, 6:21, 7:68, 8:164,
9:2, 10:4, 11:34, 12:41, 13:107, 14:72.
```

Exactly ninety-six attempts have minimum transversal at most seven.  Their
minimum-transversal families contain 808 distinct sets.  Restricting to minimum
sizes four and five leaves seven attempts and twenty-one minimum transversals.

#### Proof

`scripts/check_boundary_eighth_corrected_transition.py` reconstructs the corrected
seventh state, forms every old-old-new and old-new-new collinear triple, solves
minimum hitting set exactly, and enumerates all minimum sets through size seven.
The displayed histogram sums to 520.  ∎

## 2. Corrected eighth and ninth transitions

### Theorem PP3cwe -- PROVED / TWO EXPLICIT BUDGET-SEVEN TRANSITIONS

Among all 808 eighth-step minimum transversals and every enlargement to total
deletion size at most seven, exactly one degree-preserving legal eighth
correction exists.  It uses `P1` at offset `31` and has

```text
delete:
(0,2), (1,3), (23,108), (24,49),
(28,110), (28,113), (30,110)

add:
(0,110), (1,113), (23,2), (24,110),
(28,3), (28,108), (30,49).
```

The resulting sixty-four-point state has no raw ninth extension.  Nevertheless,
allowing a second correction gives sixteen ninth attempts of minimum transversal
at most five—four of minimum four and twelve of minimum five—with 120 minimum
transversals total.  The attempt `P0` at offset `-12` has the seven-point
correction

```text
delete:
(5,32), (12,48), (17,1), (21,105),
(26,82), (34,99), (35,98)

add:
(5,1), (12,105), (17,99), (21,98),
(26,48), (34,32), (35,82).
```

This produces a legal seventy-two-point nine-block state.

#### Proof

The eighth uniqueness statement is the complete correction search in
`scripts/check_boundary_eighth_corrected_transition.py`.  The ninth census and
displayed refill are independently checked by
`scripts/check_boundary_budget_seven_chain.py`.  Both checkers compare deleted
and added row/column multisets and verify every triple by exact determinants.  ∎

## 3. Tenth-step budget obstruction

### Theorem PP3cwf -- PROVED / NO BUDGET-SEVEN TENTH TRANSITION

From the corrected ninth state there is no raw tenth extension.  Exactly two
attempts have minimum transversal at most five:

```text
(P2,-32), (P3,-32).
```

Each has minimum transversal five and exactly one minimum transversal.  Neither
core admits a degree-preserving correction of total deletion size at most seven.

Thus the canonical corrected-state path reaches nine blocks but has no tenth
transition at the same correction budget in the audited radius.

#### Proof

The checker enumerates all 520 tenth attempts.  For each of the two surviving
minimum cores it checks every enlargement by zero, one, or two extra deletions
and every row-column-preserving inherited-line-safe refill.  All fail.  ∎

## Consequence

The corrected-state graph contains a genuine path through nine blocks, but no
verified periodic or strongly connected component.  A larger correction budget,
a wider offset range, a noncanonical state, or a different block catalogue is
still required.  This remains finite composition evidence, not an all-length
boundary construction.
