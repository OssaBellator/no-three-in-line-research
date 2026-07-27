# Parity-fibre regeneration and the `m=9` clean rotation graph

Run

```bash
python scripts/check_hamilton_parity_fibre_regeneration.py \
  experiments/hamilton-parity-fibre-regeneration-audit.json
```

The checker precomputes every two-owner pair predicate, classifies every Hamilton
cycle through `m=10`, and audits all `3,386,880` successor rotations at `m=9`.

## Clean fibre census

| `m` | Hamilton cycles | parity-satisfiable | total clean orientations | minimum components | maximum components |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 80 | 3 | 4 |
| 5 | 24 | 22 | 376 | 2 | 5 |
| 6 | 120 | 112 | 3,576 | 2 | 6 |
| 7 | 720 | 664 | 36,736 | 2 | 7 |
| 8 | 5,040 | 3,542 | 404,080 | 2 | 8 |
| 9 | 40,320 | 31,688 | 6,727,728 | 2 | 9 |
| 10 | 362,880 | 297,886 | 115,586,396 | 1 | 10 |

Every satisfiable parity constraint graph through `m=9` is a forest. At `m=10`,
296,298 satisfiable cycles still have forest constraint graphs, while 1,588 have
cyclomatic rank one. No satisfiable graph of larger rank occurs in the audited
range.

## `m=9` clean rotation graph

```text
clean cycles                                      31,688
clean induced components                               1
minimum clean degree                                  43
maximum clean degree                                  84
minimum clean rotations meeting any owner triple      26
maximum distance from an inconsistent cycle to clean   1
```

Directed transition counts:

```text
clean -> clean                2,273,712
clean -> inconsistent          388,080
inconsistent -> clean          388,080
inconsistent -> inconsistent   337,008
```

## Fibre kernel

If a clean parity graph has `c` connected components, choose one satisfying
orientation and independently complement each component with probability `1/2`.
This produces the exact uniform distribution on its `2^c` clean orientations.
For a graph with `q` parity edges, `c>=m-q`, so every output atom is at most
`2^(q-m)`.
