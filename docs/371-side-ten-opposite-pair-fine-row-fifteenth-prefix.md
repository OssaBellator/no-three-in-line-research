# Side-ten opposite-pair fine-row fifteenth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `5600` through `5999` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1208 — `fc` obstruction on indices 5600 through 5999

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 5600 | 4,273,810 | 329,264 |
| 5700 | 4,940,017 | 569,902 |
| 5800 | 3,618,878 | 794,719 |
| 5900 | 7,097,190 | 715,911 |
| Total | 19,929,895 | 794,719 |

## PX1209 — `ff` obstruction on indices 5600 through 5999

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 5600 | 2,277,537 | 477,189 |
| 5700 | 2,355,426 | 188,842 |
| 5800 | 2,987,768 | 357,401 |
| 5900 | 2,477,012 | 472,540 |
| Total | 10,097,743 | 477,189 |

GitHub Actions run `30746062601` produced the first exact matrix. Run `30746389101` independently replayed the deterministic expected outputs before promotion.

## PX1210 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `5999` in both orientations:

- `fc`: 6,000 geometries, `222,250,906` nodes, maximum `1,877,339`;
- `ff`: 6,000 geometries, `131,624,531` nodes, maximum `909,040`.

No constructive witness appears in these 12,000 fine-row geometries. The next bounded prefix begins at pair index `6000`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_5600_5999.py
```
