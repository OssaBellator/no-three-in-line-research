# Threshold exposure obstruction

The previous threshold chapters separate endpoint drift from transient scheduling.
This chapter consolidates the exact buffer-factorization and exposed-state results
under unique theorem identifiers.

## PP3dan — Complete three-round factorization

The twenty-four target-buffer incidences admit exactly forty-four unordered
factorizations into three edge-disjoint perfect matchings.  Therefore there are

```text
44*3! = 264
```

ordered three-round schedules in which every target uses all three of its possible
buffers once and every buffer is used once per round.  Choosing either native swap
order at each incidence gives

```text
264*2^24 = 4,429,185,024
```

fully ordered schedules.

## PP3dao — Matching-independent full-grid shared load

For any of the forty-nine perfect matchings, unite each target's six-cell support
with its selected transient cell.  The eight seven-cell footprints cover the
entire `4 x 4` grid, with invariant load histogram

```text
load 2: eight cells,
load 5: eight cells.
```

The load-five cells are exactly the non-unit source cells.  No matching reduces
the maximum shared-cell load below five.

## PP3dap — Unique balanced order remains illegal

Across all 12,544 one-round ordered distinct-buffer batches, the maximum cell
exposure has histogram

```text
2:49, 3:1553, 4:7970, 5:2972.
```

Exactly forty-nine batches attain the lower bound two.  Every perfect matching has
exactly one swap-order choice in which all sixteen cells are exposed exactly
twice.  None of the eight intermediate matrices in any of those forty-nine
balanced batches is a legal four-layer matrix: all 392 occurrences remain
matrix-illegal.

Exact checkers:

- `scripts/check_threshold_factorized_exposure_collision.py`
- `scripts/check_threshold_balanced_exposure_batch.py`
- `scripts/check_threshold_incidence_factorizations.py`

## Evidence boundary

Buffer reuse and exposure imbalance can both be eliminated, but native exposed
states remain illegal and every round has a coupled full-grid footprint with eight
fivefold-shared cells.  A geometric source operation must hide those states or
replace the native two-swap catalogue.
