# Width-two one-rectangle repair search

This experiment uses
[`scripts/search_width_two_rectangle_repairs.py`](../scripts/search_width_two_rectangle_repairs.py)
and the exact criterion in
[`docs/43-one-rectangle-patch-repair.md`](../docs/43-one-rectangle-patch-repair.md).

The command

```bash
python scripts/search_width_two_rectangle_repairs.py \
  certificates/prime-patching-small.json
```

starts from every distinct internally clean width-two matching-patch state in
the stored corpus, enumerates every alternating axis-parallel rectangle, and
verifies the switched configuration with exact integer determinants.

## Exhaustive result

| Source side | Target side | Internally clean initial states | Repairable initial states | Repairing switches | Distinct repaired configurations |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 20 | 1 | 1 | 1 |
| 5 | 7 | 149 | 1 | 1 | 1 |
| 6 | 8 | 969 | 1 | 1 | 1 |
| 7 | 9 | 3,686 | 0 | 0 | 0 |
| 8 | 10 | 9,813 | 0 | 0 | 0 |
| 9 | 11 | 22,555 | 0 | 0 | 0 |
| 10 | 12 | 43,539 | 0 | 0 | 0 |

Thus exactly three of the `80,731` distinct internally clean initial states are
repairable by one rectangle switch.

## Repaired configurations

### `4 -> 6`

The initial state has three triples.  Remove

```text
(2,6), (1,3)
```

and add

```text
(2,3), (1,6).
```

The repaired side-six configuration is

```text
(1,5), (1,6), (2,1), (2,3),
(3,2), (3,5), (4,4), (4,6),
(5,1), (5,2), (6,3), (6,4).
```

### `5 -> 7`

The initial state has two triples.  Remove

```text
(1,2), (5,5)
```

and add

```text
(1,5), (5,2).
```

The repaired side-seven configuration is

```text
(1,3), (1,5), (2,4), (2,7),
(3,2), (3,6), (4,1), (4,7),
(5,2), (5,6), (6,1), (6,4),
(7,3), (7,5).
```

### `6 -> 8`

The initial state has one triple.  Remove

```text
(1,2), (5,3)
```

and add

```text
(1,3), (5,2).
```

The repaired side-eight configuration is

```text
(1,3), (1,5), (2,5), (2,7),
(3,2), (3,8), (4,1), (4,7),
(5,2), (5,4), (6,6), (6,8),
(7,1), (7,3), (8,4), (8,6).
```

## Interpretation

A patch-plus-trade architecture is strictly stronger than the raw matching
patch family: three source certificates that had no clean width-two matching
patch do admit a clean width-two extension after one old-core rectangle switch.

The absence of one-switch repairs from source side seven onward is a finite
statement about the stored seeds.  The next scalable target is a protected
rectangle bank whose removed diagonals cover residual external certificates
and whose added diagonals have controlled collateral, rather than unrestricted
post hoc rectangle search.
