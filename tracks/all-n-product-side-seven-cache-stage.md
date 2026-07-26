# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have now closed every top-signature tier of multiplicity at least `24`:

| Multiplicity | Signatures | Selectors | Status |
|---:|---:|---:|---|
| 46 | 4 | 184 | certified infeasible |
| 40 | 3 | 120 | certified infeasible |
| 38 | 3 | 114 | certified infeasible |
| 35 | 2 | 70 | certified infeasible |
| 32 | 3 | 96 | certified infeasible |
| 27 | 6 | 162 | certified infeasible |
| 26 | 6 | 156 | certified infeasible |
| 24 | 8 | 192 | certified infeasible |
| **Total** | **35** | **1,094** | **16,259,764 shared bottom-CSP nodes** |

Thus `70,766` support-twenty selectors remain active in this cache layer.

The latest exact results are PX625--PX628 in
[`docs/203-side-seven-cycle52-radius-three-support-twenty-multiplicity-twenty-four.md`](../docs/203-side-seven-cycle52-radius-three-support-twenty-multiplicity-twenty-four.md).

## Immediate task

The next tier has multiplicity `23`: ten top signatures containing `230`
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
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity24.cpp \
  -o /tmp/side7_c52_s20_m24

for case_index in 0 1 2 3 4 5 6 7; do
  for orientation in 0 1 2 3; do
    /tmp/side7_c52_s20_m24 "$case_index" "$orientation"
  done
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
