# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have now closed every top-signature tier of multiplicity at least `20`:

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
| 23 | 10 | 230 | certified infeasible |
| 20 | 1 | 20 | certified infeasible |
| **Total** | **46** | **1,344** | **20,687,852 shared bottom-CSP nodes** |

Thus `70,516` support-twenty selectors remain active in this cache layer.

The latest exact results are PX633--PX636 in
[`docs/205-side-seven-cycle52-radius-three-support-twenty-multiplicity-twenty.md`](../docs/205-side-seven-cycle52-radius-three-support-twenty-multiplicity-twenty.md).

## Immediate task

The next tier has multiplicity `19`: forty-two top signatures containing `798`
selectors. Regenerate the exact layer, record both clean-top order counts, and
exhaust all four radix orientations with the shared active-selector bottom CSP.
Because this tier is substantially wider than the completed tiers, batch the
signatures into independently reproducible verifier shards with exact aggregate
counts.

## Stage completion criterion

This cache stage is complete when every selector in the radius-three,
support-twenty `(5,2)` layer is either certified infeasible in all four
orientations or accompanied by an independently checked no-three witness.
Afterward the side-seven classification must still address the remaining
support layers and relative-cycle classes.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity20.cpp \
  -o /tmp/side7_c52_s20_m20

for orientation in 0 1 2 3; do
  /tmp/side7_c52_s20_m20 "$orientation"
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
