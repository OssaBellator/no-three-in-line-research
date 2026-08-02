# Repeated semantic cores for orientation-three support mask 6975

PX1013--PX1015 semantically minimize the two top-order-zero covers supported on
mask `6975`. The same syntactic support occurs for both selectors at twelve of
the first 64 top orders:

`0, 1, 6, 7, 9, 50, 51, 56, 57, 60, 61, 63`.

This chapter minimizes all 24 covers and verifies every resulting pair core.

## 1. Two-mask semantic vocabulary

### Theorem PX1019 -- PROVED FINITE

For eleven of the twelve top orders, both selectors minimize to the same
six-column semantic mask

\[
\boxed{6936}.
\]

At top order `9`, both selectors minimize further to the same five-column mask

\[
\boxed{6920}.
\]

Thus all 24 selector covers collapse to only two semantic support masks:

| Pair mask | Size | Top orders |
|---:|---:|---:|
| `6936` | 6 | 11 |
| `6920` | 5 | 1 |

The selector-zero and selector-one masks coincide at every measured top order;
no union penalty is required anywhere in this repeated syntactic class.

## 2. Exact extension census

### Theorem PX1020 -- PROVED FINITE

The twelve pair cores certify 40 clean top extensions in total:

- eight six-column cores have four clean extensions;
- three six-column cores have two clean extensions;
- the five-column core has two clean extensions.

Both selectors are checked on every extension, giving exactly

\[
40\cdot2\cdot5040=\boxed{403{,}200}
\]

bottom-permutation checks.

Each transcript has an independent ordered digest. The verifier asserts all
twelve final masks, extension counts, top-search nodes, bottom-check totals, and
digests.

## 3. Semantic-class consequence

### Corollary PX1021 -- PROVED REDUCTION

The most common syntactic support class does not require twelve unrelated master
nogood shapes. Its 24 covers reduce to a two-mask semantic vocabulary, and eleven
of the twelve pair occurrences share the same six-column shape.

The literal values on those masks still depend on the reference top assignment,
so this is a support-shape compression theorem rather than a claim that one
single partial assignment covers all twelve references. Nevertheless, it
separates the reusable combinatorial mask from the reference-specific values and
shows that semantic minimization substantially strengthens raw syntactic support
reuse.

The next master-learning target is to deduplicate the actual partial assignments
on masks `6936` and `6920`, then measure the union of their clean-extension
families against the complete orientation-three top-order set.

This finite result does not advance the selector classification boundary and
does not prove an infinite product theorem.

## 4. Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_repeated_semantic_cores.py
```

The verifier regenerates and semantically minimizes all twelve pair occurrences,
checks the two-mask frequency, and asserts the aggregate 40 extensions and
403,200 bottom checks.
