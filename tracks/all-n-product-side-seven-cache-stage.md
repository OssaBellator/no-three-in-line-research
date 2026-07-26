# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have now closed every top-signature tier of multiplicity at least `27`:

| Multiplicity | Signatures | Selectors | Status |
|---:|---:|---:|---|
| 46 | 4 | 184 | certified infeasible |
| 40 | 3 | 120 | certified infeasible |
| 38 | 3 | 114 | certified infeasible |
| 35 | 2 | 70 | certified infeasible |
| 32 | 3 | 96 | certified infeasible |
| 27 | 6 | 162 | certified infeasible |
| **Total** | **21** | **746** | **9,907,392 shared bottom-CSP nodes** |

Thus `71,114` support-twenty selectors remain active in this cache layer.

The latest exact results are PX617--PX620 in
[`docs/201-side-seven-cycle52-radius-three-support-twenty-multiplicity-twenty-seven.md`](../docs/201-side-seven-cycle52-radius-three-support-twenty-multiplicity-twenty-seven.md).

## Immediate task

The next tier has multiplicity `26`: six top signatures containing `156`
selectors. Regenerate the exact layer, record both clean-top order counts, and
exhaust all four radix orientations with the shared active-selector bottom CSP.
A complete tier result must assert the exact histogram, every top-search count,
every bottom-search node count, and either an explicit surviving configuration
or exact infeasibility.

## Stage completion criterion

This cache stage is complete when every selector in the radius-three,
support-twenty `(5,2)` layer is either certified infeasible in all four
orientations or accompanied by an independently checked no-three witness.
Afterward the side-seven classification must still address the remaining
support layers and relative-cycle classes.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity27.cpp \
  -o /tmp/side7_c52_s20_m27

for case_index in 0 1 2 3 4 5; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m27 "$case_index" "$orientation"
  done
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
