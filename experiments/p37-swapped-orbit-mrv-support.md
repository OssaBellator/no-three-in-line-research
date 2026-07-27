# p=37 residual-orbit MRV support diagnostic

Compile:

```bash
g++ -O3 -std=c++17 \
  scripts/check_p37_swapped_orbit_mrv_support.cpp \
  -o /tmp/check_p37_orbit_mrv
```

For one support size `k` and sixteen shards, run:

```bash
for shard in $(seq 0 15); do
  /tmp/check_p37_orbit_mrv "$k" "$shard" 16 \
    > "mrv-k${k}-shard${shard}.json" &
done
wait
```

Repeat for `k=7,8,9,10,11`.

The checker:

1. verifies the stored near-state and its four zero determinants;
2. reconstructs all `70,726` maximal nonaxis lines;
3. removes the old orbit blocks of one support subset;
4. assigns the forced target set by MRV branching;
5. tracks occupied cells and full four-cell line coefficients exactly; and
6. accepts only a complete signed cycle cover with every line occupancy at most
   two.

Eligible support subsets are sharded by lexicographic index.  The aggregate
results are:

| support | subsets | MRV nodes | feasible leaves |
|---:|---:|---:|---:|
| 7 | 25,389 | 53,370 | 0 |
| 8 | 37,323 | 104,270 | 0 |
| 9 | 43,615 | 221,859 | 0 |
| 10 | 40,755 | 685,654 | 0 |
| 11 | 30,459 | 2,804,211 | 0 |

The complete range contains `177,541` support subsets and `3,869,364` MRV
nodes.  No support through eleven gives a repair, so the audited near-state has
canonical signed-orbit repair radius at least twelve.

Support twelve is not resolved by this record.  No valid `p=37` seed is
claimed.