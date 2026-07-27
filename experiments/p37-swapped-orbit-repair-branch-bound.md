# Exact p=37 swapped-orbit repair branch-and-bound

This diagnostic extends the raw support-six census in
`p37-swapped-orbit-repair-support.md` by solving every exact support from seven
through twelve with residual line capacities, minimum-domain branching, and an
exact Hall matching test.

Compile:

```bash
g++ -O3 -std=c++17 \
  scripts/check_p37_swapped_orbit_repair_branch_bound.cpp \
  -o /tmp/check_p37_orbit_branch
```

Supports seven through ten may be run directly:

```bash
for support in 7 8 9 10; do
  /tmp/check_p37_orbit_branch \
    experiments/p37-swapped-quarter-turn-near-example.json \
    "$support" 0 1
done
```

The larger supports may be split into disjoint subset-index shards.  The stored
aggregate used eight shards for support eleven and sixteen for support twelve:

```bash
for shard in 0 1 2 3 4 5 6 7; do
  /tmp/check_p37_orbit_branch \
    experiments/p37-swapped-quarter-turn-near-example.json \
    11 "$shard" 8
done

for shard in $(seq 0 15); do
  /tmp/check_p37_orbit_branch \
    experiments/p37-swapped-quarter-turn-near-example.json \
    12 "$shard" 16
done
```

The exact aggregate is recorded in
`p37-swapped-orbit-repair-branch-bound-results.json`:

```text
support  subsets     search nodes   Hall failures   initial empty domains
      7   25,389            2,778           2,115                  22,980
      8   37,323           22,050          11,475                  22,317
      9   43,615           96,108          28,122                   8,499
     10   40,755          338,766          82,859                   1,050
     11   30,459        1,391,239         339,893                      36
     12   18,109        6,792,398       1,670,204                       0
          -------        ---------       ---------                  ------
 total   195,650        8,643,339       2,134,668                  54,882
```

No repair is found through support twelve.  Together with the earlier
exhaustive census through support six, this proves

```text
minimum canonical swapped-orbit repair support >= 13.
```

The same exact checker at support thirteen finds a feasible leaf in shard 6 of
64 after 26 support subsets and 78,466 branch nodes.  The resulting assignment
is stored and independently determinant-verified in

```text
experiments/p37-swapped-orbit-support13-certificate.json.
```

Therefore the lower bound is sharp:

```text
minimum canonical swapped-orbit repair support = 13.
```

The branch-and-bound enumerates every support subset meeting the necessary bad
owner set `{3,15,17}`.  For a fixed support, the target multiset is forced by
the cycle-cover equations.  Every legal target assignment and orientation is
then searched, while residual line overflows, duplicate orbit blocks, used
targets, and Hall-deficient remaining domains are rejected exactly.

The positive support-thirteen leaf is a finite `p=37` seed certificate.  It
does not imply an asymptotic seed family.