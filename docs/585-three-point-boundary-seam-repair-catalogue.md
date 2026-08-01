# Three-point boundary seam repair catalogue

`docs/579` found eight globally legal five-block words for the explicit side-four
catalogue at vertical offset radius 32, but no unmodified sixth block.  This
chapter asks whether a bounded destructive seam corrector can cross that horizon.
The corrector is allowed to delete points after the sixth block is placed; no
replacement points are supplied here.

## 1. Exact repair number

### Theorem PP3crz -- PROVED / TWO-DELETION IMPOSSIBILITY

For every one of the eight five-block survivors from `docs/579`, every choice of
sixth block type, dihedral variant, and offset in `[-32,32]` leaves a collinear
triple after deletion of any set of at most two points.

There are exactly

```text
8 * 8 * 65 = 4160
```

candidate extensions.

#### Proof

The first five blocks and every individual sixth block are internally legal, so
every new triple contains points on both sides of the seam.  The checker records
the complete finite family of such triples and performs an exact branching
search for a hitting set of size at most two.  No candidate has one. ∎

### Theorem PP3csa -- PROVED / SHARP THREE-DELETION REPAIR

Exactly four of the 4160 candidate extensions become no-three-in-line after
three point deletions.  Consequently the minimum destructive repair cost in this
catalogue is three.

Each successful candidate initially has ten bad triples.  A minimum repair
removes three old points lying in three distinct columns and two distinct rows.
The four certificates are related by the reflection symmetries of the two
five-block survivor types.

#### Proof

The same exact hitting-set search finds four size-three transversals.  Direct
recomputation after each deletion set finds no collinear triple.  The
size-at-most-two result of `PP3crz` proves sharpness. ∎

## 2. Saturation defect

### Theorem PP3csb -- PROVED / REPAIR-THEN-RECLEAN OBLIGATION

Every sharp three-point repair destroys the original two-points-per-row and
two-points-per-column saturation pattern: three columns and two rows lose
points.  Therefore this repair catalogue does not realize the boundary row by
itself.  It creates a finite secondary recleaning obligation with defect support
of size five.

#### Proof

The four stored deletion certificates have three distinct first coordinates and
two distinct second coordinates.  Deleting those points changes the degree
profile on precisely those resources. ∎

## 3. Exact audit

Run

```bash
python scripts/check_boundary_three_point_seam_repair.py
```

The checker reconstructs the eight five-block survivors, scans all 4160 sixth
steps, proves the two-deletion lower bound, and verifies all four sharp
three-deletion certificates.

## 4. Frontier consequence

A destructive corrector is possible, but it is not a one-point seam patch.  The
next boundary task is now finite and explicit: refill the five affected row and
column resources without recreating any inherited line.  Until such a
replacement catalogue is constructed, the boundary ledger row remains
fixture-derived.
