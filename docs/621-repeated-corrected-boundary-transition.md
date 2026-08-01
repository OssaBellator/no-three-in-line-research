# Repeated corrected boundary transition

`docs/615` found one corrected seventh-block transition from the four sharp
six-block seam states.  This chapter retains its full inherited-line state and
audits every eighth block before allowing another degree-preserving correction.

## 1. Eighth-step transversal spectrum

### Theorem PP3cwd — PROVED / COMPLETE SMALL-TRANSVERSAL CENSUS

For the canonical corrected seventh state, the 520 typed eighth-block attempts
within vertical offset radius thirty-two have minimum line-conflict transversal
spectrum

```text
size 4:       1 attempt
size 5:       6 attempts
size 6:      21 attempts
size greater than 6: 492 attempts.
```

The seven attempts of minimum size four or five have exactly twenty-one minimum
transversals in total.

#### Proof

`scripts/check_boundary_eighth_corrected_transition.py` reconstructs the complete
corrected seventh state from the stored block catalogue and correction history.
For each eighth block it forms all old-old-new and old-new-new collinear triples
and runs exact branch search for transversals of sizes one through six.  Direct
subset enumeration counts every minimum transversal for the seven smallest
attempts. ∎

## 2. Unique small corrected eighth transition

### Theorem PP3cwe — PROVED / SEVEN-POINT DEGREE CORRECTOR

Among all twenty-one minimum transversals of sizes four and five, and all
row-column-preserving corrections using at most two further deletions, exactly
one corrected eighth transition exists.  It uses `P` variant one at offset `31`.
Its minimum transversal is the fifth of the nine size-five transversals for that
attempt, and the full correction is

```text
delete:
(0,2), (1,3), (23,108), (24,49), (28,110), (28,113), (30,110)

add:
(0,110), (1,113), (23,2), (24,110), (28,3), (28,108), (30,49).
```

The correction has size seven, preserves the complete row and column degree
multisets, and produces a legal sixty-four-point eight-block state.  The two
corrected transition offsets are `-26` and `31`, with vertical drift `5`.

#### Proof

For each minimum transversal, the checker enumerates zero, one, or two additional
deletions and performs an incremental inherited-line-safe refill with the same
row and column multisets.  Only the displayed witness succeeds.  Direct triple
checking verifies the corrected state. ∎

## 3. Ninth-step obstruction

### Theorem PP3cwf — PROVED / NO RAW NINTH EXTENSION

The corrected eighth state has no unmodified ninth-block extension among all 520
typed radius-thirty-two attempts.

#### Proof

Append every `P/Q` variant at every permitted offset and check all triples in the
combined point set.  Every attempt contains a collinear triple. ∎

## Consequence

The corrected-state graph now contains a path of length two beyond the original
six-block corrector.  It still contains no verified cycle: the path has nonzero
vertical drift and terminates before an uncorrected ninth block.  This is finite
composition evidence, not an indefinitely repeatable boundary controller.
