# Budget-seven corrected boundary chain

`docs/609` constructs a sharp six-point correction for a sixth boundary block,
and `docs/615` finds one corrected seventh transition.  This chapter continues
that exact typed state with corrections of total deletion size at most seven.
The block catalogue, inherited-line state, offset radius `32`, and canonical
seventh state are fixed throughout.

## 1. Eighth corrected transition

### Theorem PP3cwd -- PROVED / EIGHTH-STEP CORRECTION CENSUS

Among the `8*65=520` typed eighth-block attempts from the corrected seventh
state, exactly seven have conflict-transversal number at most five:

```text
(P0,21):5, (P1,30):4, (P1,31):5,
(P2,22):5, (P3,-31):5, (P3,29):5, (P3,32):5.
```

They have exactly twenty-one minimum transversals in total.  The attempt
`(P1,31)` has a minimum five-point core that extends to the degree-preserving
seven-point deletion

```text
(0,2), (1,3), (23,108), (24,49),
(28,110), (28,113), (30,110),
```

with refill

```text
(0,110), (1,113), (23,2), (24,110),
(28,3), (28,108), (30,49).
```

The resulting sixty-four-point eight-block state has no collinear triple and
preserves every row and column degree.

#### Proof

For each typed offset, enumerate all cross-block collinear triples.  Exact
bounded transversal search rejects every attempt of transversal number greater
than five and lists all minimum transversals for the seven survivors.  Direct
row and column multiplicity comparison verifies the displayed deletion/refill.
The inherited-line backtracking oracle verifies that the refill creates no old--
new, new--new--old, or refill-only triple.  ∎

## 2. Ninth corrected transition

### Theorem PP3cwe -- PROVED / NINTH-STEP CORRECTION CENSUS

From the corrected eighth state, sixteen of the 520 typed ninth attempts have
transversal number at most five: four have minimum four and twelve have minimum
five.  They have 120 minimum transversals in total.

The attempt `(P0,-12)` has the unique minimum core

```text
(12,48), (26,82), (34,99), (35,98),
```

and the seven-point degree correction

```text
delete:
(5,32), (12,48), (17,1), (21,105),
(26,82), (34,99), (35,98),

add:
(5,1), (12,105), (17,99), (21,98),
(26,48), (34,32), (35,82).
```

This gives a legal seventy-two-point nine-block state.

#### Proof

The same exact transversal and degree-refill checks as in `PP3cwd` apply.  The
minimum-core uniqueness is a direct enumeration of the four-subsets of the
cross-triple support.  ∎

## 3. Budget-seven stopping certificate

### Theorem PP3cwf -- PROVED / TENTH-STEP BUDGET OBSTRUCTION

From the corrected ninth state there is no raw tenth extension.  Exactly two
attempts have transversal number at most five:

```text
(P2,-32), (P3,-32).
```

Each has minimum transversal five and exactly one minimum transversal.  Neither
core admits a degree-preserving correction with total deletion size at most
seven.

Thus the canonical radius-32 chain reaches nine corrected blocks with correction
budget seven but has no tenth transition at the same budget.

#### Proof

The 520 typed attempts are enumerated.  For the two minimum-five attempts, all
zero-, one-, and two-point enlargements of the unique core are checked.  For
each deletion set, every row-column-preserving refill is searched with inherited
line pruning.  No refill is legal.  ∎

## 4. Scope

This is a bounded corrected path, not a periodic component and not an
all-offset theorem.  Progress now requires a larger correction budget, a
noncanonical minimum core, a wider offset range, or a different block catalogue.
