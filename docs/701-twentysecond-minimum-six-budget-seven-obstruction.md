# Twenty-second minimum-six budget-seven obstruction

This chapter continues from the certified 168-point, twenty-one-block endpoint in
`docs/694-alternative-boundary-continuation-through-twenty-one-blocks.md` and the
budget-six census in
`docs/695-twentysecond-boundary-budget-six-obstruction.md`.

## PP3dfj — Exact minimum-six budget-seven layer

The raw twenty-second spectrum has minimum six. Its minimum layer contains

```text
26 attempts,
178 minimum-six cores.
```

For each core, add one further deleted point and enumerate every seven-point
row-and-column-preserving replacement. The attempt geometry is reconstructed from
the certified twenty-one-block state; the 26 attempts are processed independently
and the 178 core results are then combined.

The exact number of tested replacement permutations per core has histogram

```text
212,940 : 49 cores,
423,360 : 92 cores,
841,680 : 37 cores.
```

## PP3dfk — No minimum-six repair through budget seven

Every tested seven-point replacement fails the complete no-three condition. The
exact rejected total is

```text
49*212,940 + 92*423,360 + 37*841,680
= 80,525,340.
```

Together with the budget-six layer from `docs/695`, the same 178 minimum-six cores
now account for

```text
68,580 + 80,525,340 = 80,593,920
```

rejected preserving replacements and zero repairs through budget seven.

The audit is
`scripts/check_boundary_twentysecond_budget_seven_obstruction_701.py`.

## PP3dfl — Exact remaining twenty-second frontier

The certified finite chain remains at twenty-one blocks. This chapter closes only
the minimum-six raw layer through deletion budget seven.

A budget-seven twenty-second transition could still arise from one of the 205 raw
minimum-seven attempts. Alternatively, a minimum-six core could first repair at
budget eight. Neither frontier is excluded here, and no recurrence or periodic
state invariant is claimed.

## Evidence boundary

This is a finite exact obstruction on one certified state. It does not promote the
boundary evidence row and does not prove an all-length prime-patching
construction.
