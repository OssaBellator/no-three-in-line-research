# Side-ten opposite-pair fine-row fourteenth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `5200` through `5599` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1201 — `fc` obstruction on indices 5200 through 5599

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 5200 | 4,853,835 | 364,819 |
| 5300 | 6,883,830 | 331,606 |
| 5400 | 3,553,773 | 271,790 |
| 5500 | 2,690,688 | 133,796 |
| Total | 17,982,126 | 364,819 |

## PX1202 — `ff` obstruction on indices 5200 through 5599

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 5200 | 2,602,193 | 281,133 |
| 5300 | 2,674,421 | 243,337 |
| 5400 | 1,884,284 | 99,526 |
| 5500 | 2,343,861 | 186,593 |
| Total | 9,504,759 | 281,133 |

GitHub Actions run `30745622727` produced the first exact matrix. Run `30745722667` independently replayed the deterministic expected outputs before promotion.

## PX1203 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `5599` in both orientations:

- `fc`: 5,600 geometries, `202,321,011` nodes, maximum `1,877,339`;
- `ff`: 5,600 geometries, `121,526,788` nodes, maximum `909,040`.

No constructive witness appears in these 11,200 fine-row geometries. The next bounded prefix begins at pair index `5600`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_5200_5599.py
```
