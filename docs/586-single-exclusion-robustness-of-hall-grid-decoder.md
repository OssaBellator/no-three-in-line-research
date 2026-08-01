# Single-exclusion robustness of the Hall grid decoder

`docs/580` decoded every Hall quotient choice into two fixed cells of a `4 x 4`
grid and found eighteen no-three-in-line perfect-matching extensions.  An actual
prime-patching host can forbid residual cells for unrelated geometric reasons.
This chapter measures the exact robustness of the decoder to one such exclusion.

## 1. Extension blocker number

### Theorem PP3csc -- PROVED / HALL EXTENSION BLOCKER DICHOTOMY

Among the twelve decoded quotient choices:

```text
six have one legal matching extension,
six have two legal matching extensions.
```

The minimum number of residual cells whose exclusion destroys every extension is
one in the first class and two in the second class.

#### Proof

For a fixed decoded pair the two unused rows and columns form `K_2,2`.  The
checker enumerates its two possible residual matchings and retains those whose
four grid cells contain no collinear triple.  When only one survives, either of
its two residual cells is a singleton blocker.  When both survive, they are
disjoint; one cell cannot meet both, while one selected cell from each matching
does. ∎

### Theorem PP3csd -- PROVED / EXACT ROBUST SUBSET

Exactly six quotient choices survive every single forbidden residual cell.  In
`(syndrome,choice)` coordinates they are

```text
(0,2),
(1,0),(1,1),(1,2),(1,3),
(2,1).
```

The remaining six choices are single-exclusion fragile.

#### Proof

These are precisely the choices with two legal extensions in the complete
census. ∎

## 2. Microscopic orientation cannot repair fragility

### Theorem PP3cse -- PROVED / ORIENTATION-INDEPENDENT BLOCKER

The two microscopic orientations of the cylinder state decode to the same pair
of grid cells.  Hence orientation cannot bypass a singleton blocker for any of
the six fragile quotient choices.

#### Proof

The decoder from `docs/568--580` depends on syndrome and local choice, not on
orientation.  Both orientations therefore inherit the same residual extension
family and the same blockers. ∎

## 3. Exact audit

Run

```bash
python scripts/check_hall_single_exclusion_robustness.py
```

The checker enumerates all twelve decoded pairs, all eighteen legal extensions,
and every minimum residual-cell blocker.

## 4. Frontier consequence

The complete-grid decoder is geometrically viable but not uniformly robust.
An actual endpoint host must either prove that the fragile extension cells are
never excluded, alter the quotient-to-cell map, or add host state recording the
available residual matching.  The Hall row is not promoted by this result.
