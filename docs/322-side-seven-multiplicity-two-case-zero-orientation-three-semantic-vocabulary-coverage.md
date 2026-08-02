# Case-zero orientation-three semantic vocabulary coverage

PX1019--PX1021 show that the repeated syntactic support class `6975` has only
two minimized mask shapes across twelve measured reference top orders. This
chapter deduplicates the actual partial assignments, not merely their masks, and
measures their union coverage.

This is a finite certificate-compression result. It does not classify the full
top-order family, prove an infinite product theorem, or prove the no-three-in-line
conjecture.

## 1. Exact semantic vocabulary

### Theorem PX1030 -- PROVED FINITE

For multiplicity-two case zero in orientation three, use the twelve reference top
indices

`0, 1, 6, 7, 9, 50, 51, 56, 57, 60, 61, 63`.

At each reference, regenerate the two deterministic seven-triple covers and
perform semantic deletion minimization. The twelve resulting pair cores
collapse to exactly five distinct partial assignments:

- four keys have six-column mask `6936`;
- one key has five-column mask `6920`.

Thus twelve reference-specific obstruction pairs require only five stored
master-nogood keys.

## 2. Exact union coverage

### Theorem PX1031 -- PROVED FINITE

The twelve references have extension-set sizes summing to `40`. After exact
assignment deduplication, their five-key vocabulary covers exactly `14` distinct
clean top orders. Therefore the raw extension lists contain

\[
40-14=\boxed{26}
\]

repeated occurrences.

The measured compression ratios are therefore:

- reference cores to vocabulary keys: `12 -> 5`;
- extension occurrences to distinct covered orders: `40 -> 14`.

The result is deliberately a coverage measurement, not a claim that these five
keys cover every clean top order of the signature.

## 3. Exact selector verification

### Theorem PX1032 -- PROVED FINITE

For every clean top order in every extension list, both selector covers were
replayed against all `5,040` bottom permutations. The complete measurement uses

\[
40\cdot2\cdot5{,}040=\boxed{403{,}200}
\]

exact bottom checks. Every check is covered by at least one stored collinear
triple.

The ordered transcript digest is

`11777308162869991640`.

GitHub Actions run `30269022899` completed the exact measurement and uploaded the
transcript.

## 4. Consequence for proof-object design

The repeated support class exhibits two independent forms of compression:

1. mask-shape compression, from twelve references to masks `6936` and `6920`;
2. value-assignment compression, from twelve reference cores to five distinct
   partial assignments.

The next certificate frontier is to generate semantic cores for the remaining
support classes, deduplicate their actual partial assignments, and measure the
union of covered clean top orders before attempting multiplicity one.

## 5. Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary.py
```

The verifier compiles the exact C++ measurement, regenerates the twelve cores,
checks their ordered top indices, and asserts the complete final counts and
digest.
