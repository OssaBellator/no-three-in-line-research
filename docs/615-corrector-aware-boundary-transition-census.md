# Corrector-aware boundary transition census

This chapter continues the exact radius-32 boundary catalogue after the sharp
six-point seam correctors of `docs/609`.  The corrected six-block states restore
all row and column degrees, but no unmodified seventh block can be appended.  We
therefore include the correction operation in the transition state.

## 1. Four corrected source states

### Theorem PP3cvl — PROVED / CORRECTED-STATE RECONSTRUCTION

The four six-point correctors recorded in `docs/609` reconstruct four distinct
forty-eight-point, row-column-degree-preserving, no-three-in-line states.

#### Proof

`scripts/check_boundary_corrector_transition_state.py` rebuilds the five-block
states and sixth blocks from the `P/Q` coordinate catalogue, applies the stored
six deletions and six additions, verifies equality of deleted and added row and
column multisets, and checks every collinear triple. ∎

## 2. Seventh-block transversal census

### Theorem PP3cvm — PROVED / SIX MINIMUM-FOUR TRANSITION CANDIDATES

Among the `4*8*65=2080` typed seventh-block attempts within vertical offset
radius thirty-two:

- 2,074 have no line-conflict transversal of size at most four;
- exactly six have minimum transversal size four;
- those six attempts have exactly eighty-two minimum four-point transversals in
  total.

#### Proof

For every attempt the checker constructs the complete family of old-old-new and
old-new-new collinear triples.  Exact branch search rejects transversal sizes at
most three.  Direct four-subset enumeration gives the six surviving attempts and
the eighty-two witnesses. ∎

## 3. One canonical corrected transition

### Theorem PP3cvn — PROVED / CANONICAL SEVENTH CORRECTOR AND EIGHTH OBSTRUCTION

Choose the lexicographically first minimum transversal for each of the six
attempts.  Search exact row-column-preserving corrections obtained by adding at
most two further deletions.  Exactly one canonical attempt admits a correction:

```text
source corrected state: 3
seventh block:            P variant 1
vertical offset:          -26
minimum transversal:      (0,58),(8,61),(13,49),(24,79)
full deleted set:          (0,58),(1,77),(8,61),(13,49),(23,105),(24,79)
full added set:            (0,79),(1,61),(8,105),(13,77),(23,58),(24,49)
```

The successful correction has size six.  The resulting fifty-six-point state has
no raw eighth-block extension among the 520 typed radius-32 attempts.

#### Proof

The correction search preserves the exact deleted row and column multisets and
checks inherited lines incrementally.  The witness appears at the 142nd
lexicographic extra-deletion pair.  Direct enumeration of all eighth blocks and
offsets then returns the empty extension set. ∎

## Consequence

Correctors can participate in the boundary state graph: the corrected-state
transition relation is not empty.  The current catalogue nevertheless has no
uncorrected eighth step and supplies no corrected-state cycle, zero-drift cycle,
or indefinitely composable controller.
