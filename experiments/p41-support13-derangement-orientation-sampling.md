# Reproducible p=41 support-thirteen derangement sampling

Compile:

```bash
g++ -O3 -std=c++17 -fopenmp \
  scripts/sample_p41_support13_derangement_orientations.cpp \
  -o /tmp/sample_p41_support13
```

Run the two recorded deterministic trial streams:

```bash
/tmp/sample_p41_support13 500000 32 20260731 0
/tmp/sample_p41_support13 500000 32 20260801 1
```

Mode `0` uses one thirteen-cycle on each sampled owner-feasible support.  Mode
`1` samples a uniformly rejected derangement of that support.  Each trial gets
its pseudorandom stream from the master seed and the trial index through
`splitmix64`, so the sample is independent of OpenMP scheduling.

The same commands were repeated with `8` and `32` threads and produced identical
ledgers.

Recorded results:

```text
single thirteen-cycle mode
  trials                              500,000
  owner-cover pass                    484,660
  initial empty orientation domain   477,997
  nonempty initial domain               6,663
  exact orientation DFS nodes          14,673
  node-cap hits                              0
  repair found                              no

uniform derangement mode
  trials                              500,000
  owner-cover pass                    484,660
  initial empty orientation domain   478,071
  nonempty initial domain               6,589
  exact orientation DFS nodes          14,417
  node-cap hits                              0
  repair found                              no
```

Thus approximately `98.63%` of owner-feasible sampled target maps in each mode
are rejected before orientation branching.  Since no trial hit the
`100,000`-node ledger cap, every owner-feasible sampled target map was fully
decided by exact orientation and line-capacity search.

Trials are not deduplicated, and the sample is not an exhaustive enumeration of
support-thirteen target maps.  The result does not prove support-thirteen
infeasibility and does not provide a `p=41` seed.
