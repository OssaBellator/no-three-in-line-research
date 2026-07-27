# Exact p=37 swapped-orbit repair census

The self-contained checker audits the four-line swapped-quarter-turn near-state
recorded in `p37-swapped-quarter-turn-near-example.json`.

Compile:

```bash
g++ -O3 -std=c++17 \
  scripts/check_p37_swapped_orbit_repair_support.cpp \
  -o /tmp/check_p37_orbit_repair
```

Supports one through five finish in one process:

```bash
/tmp/check_p37_orbit_repair 5
```

Support six contains `315,267,140` canonical candidates.  It may be partitioned
into eight disjoint subset-index shards:

```bash
for shard in 0 1 2 3 4 5 6 7; do
  /tmp/check_p37_orbit_repair 6 "$shard" 8 &
done
wait
```

The verified exact counts are:

```text
support 1:          3
support 2:        225
support 3:      9,500
support 4:    347,811
support 5: 11,090,546
support 6:315,267,140
          -----------
total:   326,715,225
```

No candidate repairs the state.  The enumeration includes every canonical
combination of target-pair reassignment and orientation change on the selected
support, including pure and mixed orientation flips.  The exact local lower
bound is therefore

```text
minimum swapped-orbit repair support >= 7.
```

The base state itself is not a seed: all `59,640` determinants contain exactly
four zero values, forming one quarter-turn orbit of bad lines.  The diagnostic
is a finite local repair result and does not prove `p=37` infeasible.