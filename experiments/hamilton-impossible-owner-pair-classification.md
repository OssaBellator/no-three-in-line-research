# Hamilton impossible owner-pair classification audit

The checker reconstructs every compatible pair of directed pair assignments for
`4<=m<=80` and tests both relative orientation parities directly from the orbit
geometry.

For centered odd coordinates

```text
u=2m-1-2s,  v=2m-1-2t,
x=2m-1-2s', y=2m-1-2t',
```

the pair forbids both XOR values exactly when the two centered directions are
proportional up to coordinate swap and their odd scale factors satisfy one of
the four multiplier equations recorded in `docs/322`.

Selected exact counts are:

| `m` | impossible compatible owner pairs |
|---:|---:|
| 4--7 | 0 |
| 8--10 | 4 |
| 11--22 | 8 |
| 23--31 | 12 |
| 32 | 16 |
| 33--37 | 20 |
| 38--42 | 24 |
| 43--52 | 32 |
| 53--57 | 40 |
| 58--67 | 44 |
| 68--73 | 48 |
| 74--80 | 52 |

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_impossible_owner_pair_classification.cpp \
  -o /tmp/check_hamilton_impossible_owner_pair_classification
/tmp/check_hamilton_impossible_owner_pair_classification
```

The program compares the geometric predicate and the centered-ray formula for
every compatible assignment pair and checks the full stored count ledger.
