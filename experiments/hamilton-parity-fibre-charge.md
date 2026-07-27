# Exact parity-fibre charge audit

Run

```bash
python scripts/check_hamilton_parity_fibre_charge.py \
  experiments/hamilton-parity-fibre-charge-audit.json
```

For one clean source cycle, one three-owner set, and one clean intersecting target
rotation, let

```text
c  = source parity-component count,
c' = target parity-component count,
r  = number of source components met by the three owners.
```

Uniform target-fibre regeneration has labelled column mass

```text
2^(c-c'-r).
```

The checker chooses the clean intersecting rotation maximizing

```text
Delta = r+c'-c
```

for every clean cycle and every owner triple.

| `m` | minimum guaranteed `Delta` |
|---:|---:|
| 4 | 3 |
| 5 | 3 |
| 6 | 3 |
| 7 | 3 |
| 8 | 3 |
| 9 | 3 |

Thus every audited owner triple has a labelled clean fibre action of column mass
at most `2^-3=1/8`.

Exact exponent distributions:

```text
m=4:  3:20, 4:4
m=5:  3:88, 4:100, 5:32
m=6:  3:728, 4:890, 5:532, 6:90
m=7:  3:5,242, 4:9,042, 5:7,134, 6:1,722, 7:100
m=8:  3:43,134, 4:78,402, 5:56,592, 6:17,922, 7:2,252, 8:50
m=9:  3:495,222, 4:950,218, 5:797,738, 6:341,198,
      7:70,986, 8:6,322, 9:108
```

This is a labelled-action charge calculation. Combining multiple rotation labels
may increase a column sum and requires a separate policy or witness analysis.
