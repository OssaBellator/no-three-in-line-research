# Budget-seven corrected boundary chain

`docs/609` constructs a sharp six-point seam corrector and `docs/615` finds one
corrected seventh transition.  This chapter combines the complete eighth-step
transversal spectrum with explicit corrected eighth and ninth transitions,
retaining the full inherited-line state and offset radius `32`.

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

The checker reconstructs the corrected seventh state, forms every old-old-new
and old-new-new collinear triple, solves minimum hitting set exactly, and
enumerates all minimum sets through size seven.  ∎

## 2. Corrected eighth and ninth transitions

### Theorem PP3cwe -- PROVED / TWO EXPLICIT BUDGET-SEVEN TRANSITIONS

Among all 808 eighth-step minimum transversals and every enlargement to total
deletion size at most seven, exactly one degree-preserving legal eighth
correction exists.  It uses `P1` at offset `31`:

```text
delete:
(0,2), (1,3), (23,108), (24,49),
(28,110), (28,113), (30,110)

add:
(0,110), (1,113), (23,2), (24,110),
(28,3), (28,108), (30,49).
```

The resulting sixty-four-point state has no raw ninth extension.  Allowing a
second correction gives sixteen ninth attempts of minimum transversal at most
five—four of minimum four and twelve of minimum five—with 120 minimum
transversals total.  The attempt `P0` at offset `-12` has correction

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

Every candidate correction is checked for identical deleted/added row and column
multisets and for absence of inherited, mixed, and refill-only triples by exact
integer determinants.  ∎

## 3. Tenth-step budget obstruction

### Theorem PP3cwf -- PROVED / NO BUDGET-SEVEN TENTH TRANSITION

From the corrected ninth state there is no raw tenth extension.  Exactly two
attempts have minimum transversal at most five:

```text
(P2,-32), (P3,-32).
```

Each has minimum transversal five and exactly one minimum transversal.  Neither
core admits a degree-preserving correction of total deletion size at most seven.

#### Proof

All 520 tenth attempts are enumerated.  For each of the two surviving minimum
cores, every enlargement by zero, one, or two extra deletions and every row-
column-preserving inherited-line-safe refill is checked.  All fail.  ∎

## Consequence

The corrected-state graph contains a path through nine blocks but no verified
periodic component.  A larger correction budget, wider offset range,
noncanonical state, or different block catalogue is still required.  This is
finite composition evidence, not an all-length boundary construction.
