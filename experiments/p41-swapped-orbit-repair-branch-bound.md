# Exact p=41 swapped-orbit repair branch-and-bound

The input is the four-line near-state in
`p41-swapped-quarter-turn-near-example.json`.

Verify its geometry first:

```bash
python scripts/check_p41_swapped_orbit_near_state.py \
  experiments/p41-swapped-quarter-turn-near-example.json
```

Compile the exact repair decision procedure:

```bash
g++ -O3 -std=c++17 \
  scripts/check_p41_swapped_orbit_repair_branch_bound.cpp \
  -o /tmp/check_p41_orbit_branch
```

For one support and one subset-index shard, run:

```bash
/tmp/check_p41_orbit_branch \
  experiments/p41-swapped-quarter-turn-near-example.json \
  SUPPORT SHARD SHARDS
```

The search is complete for every exact canonical signed-orbit support from one
through twelve.  Every support must meet the bad-owner set `{15,18,20}`, so the
number of support subsets at size `k` is

```text
C(20,k)-C(17,k).
```

The exact aggregate is:

| support | support subsets | search nodes | Hall failures | initial empty domains |
|---:|---:|---:|---:|---:|
| 1 | 3 | 0 | 0 | 3 |
| 2 | 54 | 0 | 0 | 54 |
| 3 | 460 | 0 | 0 | 460 |
| 4 | 2,465 | 1 | 1 | 2,464 |
| 5 | 9,316 | 17 | 12 | 9,303 |
| 6 | 26,384 | 145 | 140 | 26,242 |
| 7 | 58,072 | 2,184 | 1,976 | 56,003 |
| 8 | 101,660 | 22,084 | 16,722 | 82,799 |
| 9 | 143,650 | 125,989 | 57,848 | 68,038 |
| 10 | 165,308 | 473,569 | 136,125 | 25,492 |
| 11 | 155,584 | 1,660,399 | 428,754 | 4,030 |
| 12 | 119,782 | 6,864,013 | 1,763,428 | 248 |
| **total** | **782,738** | **9,148,401** | **2,405,006** | **275,136** |

Every shard reports `found=0`.  Thus the recorded near-state has canonical
signed-orbit repair support at least thirteen.

The result is local and finite.  It does not prove that no `p=41` seed exists,
and it does not rule out another near-state with a smaller repair radius.
