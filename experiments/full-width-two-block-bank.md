# Full width-two block-bank experiment

This experiment uses
[`scripts/analyze_full_width_two_block_bank.py`](../scripts/analyze_full_width_two_block_bank.py)
and the 36-state construction in
[`docs/54-full-width-two-block-banks.md`](../docs/54-full-width-two-block-banks.md).

The command is

```bash
python scripts/analyze_full_width_two_block_bank.py \
  certificates/prime-patching-small.json
```

For every four-edge deletion in each perfect matching layer, the analyzer checks
all 36 ordered movement/refill pair partitions against the retained points of
that layer.

| Side | Layer | Clean states / total | Clean deletion sets | Max clean geometries for one deletion | Clean-deletion matching | Clean-deletion transversal |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | `5/36` | 1 | 5 | 1 | 1 |
| 4 | 1 | `5/36` | 1 | 5 | 1 | 1 |
| 5 | 0 | `11/180` | 4 | 4 | 1 | 1 |
| 5 | 1 | `14/180` | 4 | 5 | 1 | 1 |
| 6 | 0 | `27/540` | 13 | 4 | 1 | 2 |
| 6 | 1 | `43/540` | 11 | 8 | 1 | 2 |
| 7 | 0 | `29/1260` | 15 | 4 | 1 | 2 |
| 7 | 1 | `53/1260` | 22 | 6 | 1 | 3 |
| 8 | 0 | `92/2520` | 34 | 8 | 2 | 3 |
| 8 | 1 | `83/2520` | 34 | 6 | 2 | 3 |
| 9 | 0 | `47/4536` | 29 | 4 | 2 | 3 |
| 9 | 1 | `59/4536` | 30 | 5 | 2 | 2 |
| 10 | 0 | `63/7560` | 33 | 4 | 2 | 3 |
| 10 | 1 | `83/7560` | 47 | 5 | 2 | 3 |

Compared with the canonical adjacent family:

- clean state multiplicity increases substantially;
- the number of usable four-edge deletion sets rises from at most eight to as
  many as 47;
- the clean-deletion matching number increases from one to two at sides eight,
  nine, and ten;
- the small transversal core persists, but no longer pins every state to one
  edge.

The finite result does not establish a growing matching number.  It provides a
concrete proof of concept that local geometry entropy can diffuse the reservoir
hypergraph without changing degree bookkeeping or source deletion size.